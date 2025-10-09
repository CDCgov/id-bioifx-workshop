# Google Forms Automation

This directory contains a Python script to automatically create a Google Form from the NGS Capability Assessment questionnaire markdown file.

## Prerequisites

- Python 3.7 or higher
- Google account with access to Google Forms
- Google Cloud Project with Forms API enabled

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

Or using a virtual environment (recommended):

```bash
cd scripts
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### 2. Set Up Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Forms API:
   - Navigate to "APIs & Services" > "Library"
   - Search for "Google Forms API"
   - Click "Enable"

### 3. Create OAuth 2.0 Credentials

1. In Google Cloud Console, go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth client ID"
3. If prompted, configure the OAuth consent screen:
   - Choose "External" user type
   - Fill in application name (e.g., "NGS Questionnaire Form Creator")
   - Add your email as a test user
   - Save and continue through the remaining steps
4. Back in "Create OAuth client ID":
   - Application type: "Desktop app"
   - Name: "Forms Creator Script"
   - Click "Create"
5. Download the credentials file (click the download icon)
6. Rename it to `credentials.json` and place it in the `scripts/` directory

### 4. Run the Script

```bash
cd scripts
python create_google_form.py
```

On first run, the script will:
1. Open your web browser
2. Ask you to log in to your Google account
3. Request permission to manage your Google Forms
4. Save a token for future runs (so you don't need to authenticate again)

### 5. Access Your Form

After successful creation, the script will output:
- Form edit URL (to customize and configure)
- Form view URL (to share with participants)
- Form ID (saved to `last_form_id.txt`)

## Usage

### Basic Usage

```bash
python create_google_form.py
```

### Custom Options

```bash
# Specify a different questionnaire file
python create_google_form.py --questionnaire /path/to/questionnaire.md

# Set a custom title
python create_google_form.py --title "Custom Questionnaire Title"

# Save parsed questions to JSON (for debugging)
python create_google_form.py --output-json parsed_questions.json
```

### Help

```bash
python create_google_form.py --help
```

## What the Script Does

The script automatically:

1. **Parses the markdown file** to extract:
   - Form title and description
   - Section headers
   - Questions (numbered 1-54)
   - Question types (text, checkbox, etc.)
   - Multiple choice options
   - Sub-questions (like 1.a, 1.b)

2. **Creates a Google Form** with:
   - All sections as page breaks
   - Text questions for open-ended responses
   - Checkbox questions for multiple-choice
   - Proper formatting and help text
   - "Other" options where applicable

3. **Outputs URLs** for editing and sharing the form

## Limitations

- **Tables**: Complex tables (like Question 2's personnel table) are converted to paragraph text fields with instructions
- **Conditional logic**: The script doesn't set up conditional branching (you'll need to add this manually in the Form UI)
- **Validation**: No field validation is set (e.g., email format, number ranges)
- **Grid questions**: Not implemented (Google Forms API has limited support)

## Manual Adjustments Recommended

After creating the form, you may want to:

1. **Question 2 (Personnel table)**: Consider using Google Sheets linked response or convert to multiple questions
2. **Required fields**: Mark critical questions as required
3. **Validation rules**: Add email validation for email fields, number ranges, etc.
4. **Response validation**: Set up conditional logic for follow-up questions
5. **Section descriptions**: Add more detailed section descriptions if needed
6. **Question ordering**: Verify all questions are in the correct order
7. **Response destination**: Link to a Google Sheet for easy data analysis

## Troubleshooting

### "credentials.json not found"
- Make sure you downloaded the OAuth credentials from Google Cloud Console
- Rename the file to exactly `credentials.json`
- Place it in the `scripts/` directory

### "Access blocked: This app's request is invalid"
- Make sure you enabled the Google Forms API in your Google Cloud project
- Try recreating your OAuth credentials
- Verify you're using "Desktop app" type credentials

### "Insufficient Permission"
- The script requires Forms creation permission
- Make sure you granted all requested permissions during authentication
- Delete `token.json` and re-authenticate

### Authentication issues
- Delete `token.json` and run the script again
- Make sure you're logged into the correct Google account
- Check that your OAuth consent screen is properly configured

## Files Created

- `token.json` - Stores authentication credentials (do not commit to git!)
- `last_form_id.txt` - ID of the most recently created form
- `credentials.json` - OAuth credentials (do not commit to git!)

## Security Notes

⚠️ **Important**: 
- Never commit `credentials.json` or `token.json` to version control
- These files contain sensitive authentication information
- Add them to `.gitignore`

## Alternative: Manual Creation Guide

If you prefer to create the form manually, refer to `ms-forms-import-guide.md` in the `questionaire/` directory for a structured guide to entering all 54 questions.

## Support

For issues with:
- **The script**: Check the error message and troubleshooting section above
- **Google Forms API**: Consult [Google Forms API documentation](https://developers.google.com/forms/api)
- **The questionnaire content**: Refer to the source markdown file

## License

This script is part of the ID Bioinformatics Workshop project and follows the same license terms.
