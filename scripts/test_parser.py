#!/usr/bin/env python3
"""
Test the questionnaire parser without creating a Google Form.

This script validates that the questionnaire can be parsed correctly
and shows statistics about the parsed content.

Usage:
    python test_parser.py [--questionnaire PATH] [--verbose]
"""

import argparse
import sys
from pathlib import Path

# Import the parser from create_google_form
try:
    from create_google_form import QuestionnaireParser
except ImportError:
    print("Error: Could not import QuestionnaireParser")
    print("Make sure create_google_form.py is in the same directory")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Test questionnaire parser'
    )
    parser.add_argument(
        '--questionnaire',
        default='../questionaire/pre-workshop-questionaire.md',
        help='Path to questionnaire markdown file'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed information about each question'
    )
    
    args = parser.parse_args()
    
    # Resolve path
    script_dir = Path(__file__).parent
    questionnaire_path = Path(args.questionnaire)
    if not questionnaire_path.is_absolute():
        questionnaire_path = script_dir / questionnaire_path
    
    if not questionnaire_path.exists():
        print(f"❌ Error: File not found: {questionnaire_path}")
        sys.exit(1)
    
    print(f"📄 Parsing: {questionnaire_path.name}")
    print("=" * 60)
    print()
    
    # Parse
    try:
        qp = QuestionnaireParser(str(questionnaire_path))
        questions, sections = qp.parse()
    except Exception as e:
        print(f"❌ Error parsing questionnaire: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    # Summary
    print(f"📋 Form Title: {qp.form_title}")
    print(f"📝 Description: {qp.form_description[:100]}...")
    print()
    print(f"✅ Successfully parsed:")
    print(f"   - {len(sections)} sections")
    print(f"   - {len(questions)} questions")
    print()
    
    # Section breakdown
    print("📑 Sections:")
    print("-" * 60)
    for i, section in enumerate(sections, 1):
        q_count = len(section['questions'])
        print(f"  {i}. {section['title']} ({q_count} questions)")
    print()
    
    # Question type breakdown
    type_counts = {}
    sub_q_count = 0
    option_count = 0
    
    for q in questions:
        qtype = q.question_type or 'unknown'
        type_counts[qtype] = type_counts.get(qtype, 0) + 1
        sub_q_count += len(q.sub_questions)
        option_count += len(q.options)
    
    print("📊 Question Types:")
    print("-" * 60)
    for qtype, count in sorted(type_counts.items()):
        print(f"  - {qtype}: {count}")
    print(f"  - Sub-questions: {sub_q_count}")
    print(f"  - Total options: {option_count}")
    print()
    
    # Verbose output
    if args.verbose:
        print("📋 Detailed Question List:")
        print("=" * 60)
        for q in questions:
            print(f"\nQ{q.number}: {q.title}")
            print(f"  Type: {q.question_type or 'unknown'}")
            if q.sub_questions:
                print(f"  Sub-questions: {len(q.sub_questions)}")
                for sq in q.sub_questions:
                    print(f"    - {sq['number']} {sq['title']}")
            if q.options:
                print(f"  Options: {len(q.options)}")
                for opt in q.options[:3]:  # Show first 3
                    print(f"    - {opt}")
                if len(q.options) > 3:
                    print(f"    ... and {len(q.options) - 3} more")
            if q.follow_up_text:
                print(f"  Follow-up sections: {len(q.follow_up_text)}")
        print()
    
    # Validation warnings
    print("⚠️  Validation Warnings:")
    print("-" * 60)
    
    warnings = []
    
    # Check for questions without types
    no_type = [q for q in questions if not q.question_type and not q.sub_questions]
    if no_type:
        warnings.append(f"  - {len(no_type)} questions have no detected type:")
        for q in no_type[:5]:
            warnings.append(f"    • Q{q.number}: {q.title[:50]}...")
        if len(no_type) > 5:
            warnings.append(f"    ... and {len(no_type) - 5} more")
    
    # Check for questions without options (when expected)
    empty_checkbox = [q for q in questions if q.question_type == 'checkbox' and not q.options]
    if empty_checkbox:
        warnings.append(f"  - {len(empty_checkbox)} checkbox questions have no options")
    
    # Check for duplicate options in checkbox questions
    duplicates = []
    for q in questions:
        if q.question_type == 'checkbox' and q.options:
            seen = set()
            dups = set()
            for opt in q.options:
                if opt in seen:
                    dups.add(opt)
                seen.add(opt)
            if dups:
                duplicates.append((q.number, q.title, list(dups)))
    
    if duplicates:
        warnings.append(f"\n  - {len(duplicates)} questions have duplicate options:")
        for q_num, q_title, dups in duplicates[:5]:
            warnings.append(f"    • Q{q_num}: {q_title[:40]}...")
            warnings.append(f"      Duplicates: {', '.join(dups[:3])}")
        if len(duplicates) > 5:
            warnings.append(f"    ... and {len(duplicates) - 5} more")
    
    if warnings:
        print("\n".join(warnings))
    else:
        print("  None - all questions parsed successfully!")
    
    print()
    print("=" * 60)
    print("✅ Parsing test complete!")
    print()
    print("To create a Google Form from this questionnaire, run:")
    print("  python create_google_form.py")


if __name__ == '__main__':
    main()
