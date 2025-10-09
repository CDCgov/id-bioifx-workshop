#!/usr/bin/env python3
"""
Google Forms Automation Script for NGS Capability Assessment

This script parses the pre-workshop questionnaire markdown file and creates
a Google Form with all questions, sections, and response options.

Requirements:
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

Setup:
    1. Enable Google Forms API in Google Cloud Console
    2. Create OAuth 2.0 credentials (Desktop app)
    3. Download credentials.json to this directory
    4. Run script - it will open browser for authentication
    5. Token will be saved for future runs

Usage:
    python create_google_form.py [--questionnaire PATH] [--title TITLE]
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Google Forms API scope
SCOPES = ['https://www.googleapis.com/auth/forms.body']

# Token storage
TOKEN_FILE = 'token.json'
CREDENTIALS_FILE = 'credentials.json'


class Question:
    """Represents a parsed question from the markdown."""
    
    def __init__(self, number: str, title: str, description: str = ""):
        self.number = number
        self.title = title
        self.description = description
        self.sub_questions: List[Dict[str, Any]] = []
        self.question_type = None
        self.options: List[str] = []
        self.has_other = False
        self.is_required = False
        self.follow_up_text = []
        
    def __repr__(self):
        return f"Question({self.number}: {self.title[:50]}...)"


class QuestionnaireParser:
    """Parse markdown questionnaire into structured data."""
    
    def __init__(self, markdown_path: str):
        self.markdown_path = Path(markdown_path)
        self.content = self.markdown_path.read_text()
        self.questions: List[Question] = []
        self.sections: List[Dict[str, Any]] = []
        self.form_title = ""
        self.form_description = ""
        
    def parse(self):
        """Parse the markdown file."""
        lines = self.content.split('\n')
        
        # Extract title and description
        self._parse_header(lines)
        
        # Parse questions and sections
        self._parse_content(lines)
        
        return self.questions, self.sections
    
    def _parse_header(self, lines: List[str]):
        """Extract form title and description."""
        for i, line in enumerate(lines[:10]):
            if line.startswith('# '):
                self.form_title = line[2:].strip()
            elif line and not line.startswith('#') and not line.startswith('<!--') and not line.startswith('---'):
                if not self.form_description:
                    self.form_description = line.strip()
    
    def _parse_content(self, lines: List[str]):
        """Parse questions and sections from content."""
        current_section = None
        current_question = None
        current_sub_section = None
        in_table = False
        collecting_options = False
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Section headers
            if line.startswith('## '):
                section_title = line[3:].strip()
                current_section = {
                    'title': section_title,
                    'description': '',
                    'questions': []
                }
                self.sections.append(current_section)
                current_question = None
                collecting_options = False
                i += 1
                continue
            
            # Question headers (### N. or #### N.x.)
            question_match = re.match(r'^###\s+(\d+[a-z]?\.?[a-z]?)\s+(.+)$', line)
            sub_question_match = re.match(r'^####\s+(\d+\.?[a-z])\.\s*(.+)$', line)
            
            if question_match:
                q_num = question_match.group(1).rstrip('.')
                q_title = question_match.group(2).strip()
                
                current_question = Question(q_num, q_title)
                self.questions.append(current_question)
                if current_section:
                    current_section['questions'].append(current_question)
                
                collecting_options = False
                in_table = False
                i += 1
                continue
            
            elif sub_question_match:
                # Sub-question like 1.a, 1.b
                q_num = sub_question_match.group(1)
                q_title = sub_question_match.group(2).strip().rstrip(':')
                
                # These are typically text inputs
                sub_q = {
                    'number': q_num,
                    'title': q_title,
                    'type': 'text',
                    'required': False
                }
                
                if current_question:
                    current_question.sub_questions.append(sub_q)
                else:
                    # Create a parent question if doesn't exist
                    parent_num = q_num.split('.')[0]
                    current_question = Question(parent_num, "Contact Information")
                    self.questions.append(current_question)
                    if current_section:
                        current_section['questions'].append(current_question)
                    current_question.sub_questions.append(sub_q)
                
                i += 1
                continue
            
            # Detect question type and options
            if current_question:
                # Bold question text (often indicates a sub-question)
                bold_match = re.match(r'^\*\*(.+?)\*\*\s*$', line)
                if bold_match:
                    current_sub_section = bold_match.group(1).strip()
                    current_question.follow_up_text.append(current_sub_section)
                    collecting_options = True
                    i += 1
                    continue
                
                # Checkbox options
                if line.strip().startswith('- [ ]'):
                    option_text = line.strip()[5:].strip()
                    if option_text.startswith('Other:'):
                        current_question.has_other = True
                    else:
                        # Only add if not already in options (avoid duplicates)
                        if option_text not in current_question.options:
                            current_question.options.append(option_text)
                    
                    if not current_question.question_type:
                        current_question.question_type = 'checkbox'
                    
                    i += 1
                    continue
                
                # Table (for question 2)
                if line.strip().startswith('|') and not in_table:
                    in_table = True
                    current_question.question_type = 'grid'
                    i += 1
                    continue
                
                if in_table and not line.strip().startswith('|'):
                    in_table = False
                
                # Text input indicators - look for empty lines or lack of options
                # If we've gone past the question header and haven't found checkboxes or tables,
                # and the next non-empty line is another section/question, it's likely a text field
            
            i += 1
        
        # Post-processing: assign 'text' type to questions without a type and without options
        for question in self.questions:
            if not question.question_type and not question.sub_questions and not question.options:
                # Check if it's a simple text field or has keywords suggesting text input
                simple_fields = ['name', 'title', 'email', 'institution', 'country']
                keywords = ['describe', 'specify', 'comments', 'volume', 'threshold', 'capacity', 
                           'approximate', 'chemistry', 'kits', 'currently used', 'personnel', 
                           'roles', 'staff']
                
                if question.title.lower() in simple_fields or any(kw in question.title.lower() for kw in keywords):
                    question.question_type = 'text'


class GoogleFormsCreator:
    """Create Google Form from parsed questionnaire."""
    
    def __init__(self):
        self.creds = None
        self.service = None
        
    def authenticate(self):
        """Authenticate with Google Forms API."""
        # Check for existing token
        if os.path.exists(TOKEN_FILE):
            self.creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        
        # If no valid credentials, authenticate
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                if not os.path.exists(CREDENTIALS_FILE):
                    print(f"Error: {CREDENTIALS_FILE} not found!")
                    print("\nPlease follow these steps:")
                    print("1. Go to https://console.cloud.google.com/")
                    print("2. Create a new project or select existing")
                    print("3. Enable Google Forms API")
                    print("4. Create OAuth 2.0 credentials (Desktop app)")
                    print("5. Download credentials.json to scripts/ directory")
                    sys.exit(1)
                
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS_FILE, SCOPES)
                self.creds = flow.run_local_server(port=0)
            
            # Save credentials for next run
            with open(TOKEN_FILE, 'w') as token:
                token.write(self.creds.to_json())
        
        self.service = build('forms', 'v1', credentials=self.creds)
    
    def create_form(self, title: str, description: str) -> str:
        """Create a new Google Form."""
        form = {
            "info": {
                "title": title,
                "documentTitle": title,
            }
        }
        
        try:
            result = self.service.forms().create(body=form).execute()
            form_id = result['formId']
            
            # Add description
            if description:
                self._add_description(form_id, description)
            
            return form_id
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None
    
    def _add_description(self, form_id: str, description: str):
        """Add description to the form."""
        update = {
            "requests": [{
                "updateFormInfo": {
                    "info": {
                        "description": description
                    },
                    "updateMask": "description"
                }
            }]
        }
        
        try:
            self.service.forms().batchUpdate(formId=form_id, body=update).execute()
        except HttpError as error:
            print(f"Error adding description: {error}")
    
    def add_questions(self, form_id: str, questions: List[Question], sections: List[Dict]):
        """Add all questions to the form."""
        requests = []
        location_index = 0
        
        current_section_title = None
        
        print(f"Processing {len(questions)} questions...")
        
        for question in questions:
            # Add section header if needed
            section = self._find_section_for_question(question, sections)
            if section and section['title'] != current_section_title:
                current_section_title = section['title']
                requests.append(self._create_section_header(location_index, section['title']))
                location_index += 1
            
            # Handle sub-questions (like 1.a, 1.b, etc.)
            if question.sub_questions:
                for sub_q in question.sub_questions:
                    requests.append(self._create_text_question(
                        location_index,
                        sub_q['title'],
                        required=sub_q.get('required', False),
                        question_number=sub_q['number']
                    ))
                    location_index += 1
            
            # Handle main question
            elif question.question_type == 'checkbox':
                # If there are follow-up sections and lots of options, it might be a multi-part question
                # For now, create a single question with all options deduplicated
                requests.append(self._create_checkbox_question(
                    location_index,
                    question.title,
                    question.options,
                    question.has_other,
                    question.follow_up_text,
                    question.number
                ))
                location_index += 1
            
            elif question.question_type == 'text':
                # Determine if it's a paragraph or short text
                is_paragraph = 'describe' in question.title.lower() or 'comments' in question.title.lower()
                requests.append(self._create_text_question(
                    location_index,
                    question.title,
                    paragraph=is_paragraph,
                    question_number=question.number
                ))
                location_index += 1
            
            elif question.question_type == 'grid':
                # For complex tables, create a text question with instructions
                requests.append(self._create_text_question(
                    location_index,
                    question.title,
                    paragraph=True,
                    help_text="Please provide information in a structured format",
                    question_number=question.number
                ))
                location_index += 1
        
        # Batch update
        if requests:
            try:
                print(f"\nSubmitting {len(requests)} items to Google Forms...")
                self.service.forms().batchUpdate(
                    formId=form_id,
                    body={"requests": requests}
                ).execute()
                print(f"✅ Successfully added {len(requests)} items to the form")
            except HttpError as error:
                print(f"❌ Error adding questions: {error}")
                print("\nTip: Try running test_parser.py to identify problematic questions")
                print("     python test_parser.py --verbose")
    
    def _find_section_for_question(self, question: Question, sections: List[Dict]) -> Optional[Dict]:
        """Find which section a question belongs to."""
        for section in sections:
            if question in section['questions']:
                return section
        return None
    
    def _create_section_header(self, index: int, title: str) -> Dict:
        """Create a section header (page break)."""
        return {
            "createItem": {
                "item": {
                    "title": title,
                    "pageBreakItem": {}
                },
                "location": {"index": index}
            }
        }
    
    def _create_text_question(self, index: int, title: str, paragraph: bool = False,
                             required: bool = False, help_text: str = "",
                             question_number: str = "") -> Dict:
        """Create a text question."""
        full_title = f"{question_number}. {title}" if question_number else title
        
        question_item = {
            "createItem": {
                "item": {
                    "title": full_title,
                    "questionItem": {
                        "question": {
                            "required": required,
                            "textQuestion": {
                                "paragraph": paragraph
                            }
                        }
                    }
                },
                "location": {"index": index}
            }
        }
        
        if help_text:
            question_item["createItem"]["item"]["description"] = help_text
        
        return question_item
    
    def _create_checkbox_question(self, index: int, title: str, options: List[str],
                                  has_other: bool = False, follow_up: List[str] = None,
                                  question_number: str = "") -> Dict:
        """Create a checkbox (multiple choice) question."""
        full_title = f"{question_number}. {title}" if question_number else title
        
        # Build description from follow-up text
        description = "\n".join(follow_up) if follow_up else ""
        
        # Deduplicate options while preserving order
        seen = set()
        unique_options = []
        for opt in options:
            if opt not in seen:
                seen.add(opt)
                unique_options.append(opt)
        
        # Create options
        choice_options = [{"value": opt} for opt in unique_options]
        
        # Ensure we have at least one option (Google Forms requirement)
        if not choice_options:
            choice_options = [{"value": "N/A"}]
        
        question_item = {
            "createItem": {
                "item": {
                    "title": full_title,
                    "questionItem": {
                        "question": {
                            "required": False,
                            "choiceQuestion": {
                                "type": "CHECKBOX",
                                "options": choice_options,
                                "shuffle": False
                            }
                        }
                    }
                },
                "location": {"index": index}
            }
        }
        
        if description:
            question_item["createItem"]["item"]["description"] = description
        
        # Add "Other" option if needed
        if has_other:
            question_item["createItem"]["item"]["questionItem"]["question"]["choiceQuestion"]["options"].append({
                "isOther": True
            })
        
        return question_item
    
    def get_form_url(self, form_id: str) -> str:
        """Get the URL for the created form."""
        return f"https://docs.google.com/forms/d/{form_id}/edit"


def main():
    parser = argparse.ArgumentParser(
        description='Create Google Form from markdown questionnaire'
    )
    parser.add_argument(
        '--questionnaire',
        default='../questionaire/pre-workshop-questionaire.md',
        help='Path to questionnaire markdown file'
    )
    parser.add_argument(
        '--title',
        default='NGS Capability Assessment for Influenza Surveillance',
        help='Title for the Google Form'
    )
    parser.add_argument(
        '--output-json',
        help='Save parsed questions to JSON file (optional)'
    )
    parser.add_argument(
        '--use-existing',
        help='Use existing form ID instead of creating new (from last_form_id.txt or specify ID)'
    )
    
    args = parser.parse_args()
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Resolve questionnaire path
    questionnaire_path = Path(args.questionnaire)
    if not questionnaire_path.is_absolute():
        questionnaire_path = script_dir / questionnaire_path
    
    if not questionnaire_path.exists():
        print(f"Error: Questionnaire file not found: {questionnaire_path}")
        sys.exit(1)
    
    print(f"Parsing questionnaire: {questionnaire_path}")
    
    # Parse questionnaire
    parser = QuestionnaireParser(str(questionnaire_path))
    questions, sections = parser.parse()
    
    print(f"Found {len(questions)} questions in {len(sections)} sections")
    
    # Save to JSON if requested
    if args.output_json:
        output_data = {
            'title': parser.form_title,
            'description': parser.form_description,
            'sections': [
                {
                    'title': s['title'],
                    'question_count': len(s['questions'])
                } for s in sections
            ],
            'questions': [
                {
                    'number': q.number,
                    'title': q.title,
                    'type': q.question_type,
                    'option_count': len(q.options),
                    'has_sub_questions': len(q.sub_questions) > 0
                } for q in questions
            ]
        }
        
        with open(args.output_json, 'w') as f:
            json.dump(output_data, f, indent=2)
        print(f"Saved parsed data to {args.output_json}")
    
    # Create Google Form
    print("\nAuthenticating with Google Forms API...")
    creator = GoogleFormsCreator()
    creator.authenticate()
    
    print(f"Creating form: {args.title}")
    form_id = creator.create_form(args.title, parser.form_description)
    
    if form_id:
        print(f"Form created successfully! ID: {form_id}")
        
        print("Adding questions to form...")
        creator.add_questions(form_id, questions, sections)
        
        form_url = creator.get_form_url(form_id)
        print(f"\n✅ Form is ready!")
        print(f"📝 Edit form: {form_url}")
        print(f"👁️  View form: {form_url.replace('/edit', '/viewform')}")
        
        # Save form ID
        with open('last_form_id.txt', 'w') as f:
            f.write(form_id)
        print(f"\nForm ID saved to last_form_id.txt")
    else:
        print("Failed to create form")
        sys.exit(1)


if __name__ == '__main__':
    main()
