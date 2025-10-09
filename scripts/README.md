# Scripts Directory

This directory contains utility scripts for the ID Bioinformatics Workshop project.

## Available Scripts

### 1. Google Forms Automation (`create_google_form.py`)

Automatically creates a Google Form from the NGS Capability Assessment questionnaire markdown file.

**Quick Start:**
```bash
./setup_google_forms.sh      # One-time setup
python create_google_form.py  # Create the form
```

**Features:**
- Parses markdown questionnaire into structured data
- Creates Google Form with all 54 questions
- Organizes questions into sections
- Handles multiple choice, text, and checkbox questions
- Supports "Other" options and sub-questions

**Documentation:** See [README_GOOGLE_FORMS.md](README_GOOGLE_FORMS.md) for detailed setup instructions.

**Requirements:**
- Python 3.7+
- Google account
- Google Cloud project with Forms API enabled
- OAuth credentials

### 2. Parser Test (`test_parser.py`)

Tests the questionnaire parser without creating a Google Form. Useful for validating the questionnaire structure.

**Usage:**
```bash
python test_parser.py              # Basic test
python test_parser.py --verbose    # Detailed output
python test_parser.py --questionnaire /path/to/file.md
```

**Output:**
- Question count and types
- Section breakdown
- Validation warnings
- Option counts

### 3. Markdown to DOCX Converter (`md2docx.sh`)

Converts markdown lesson files to Microsoft Word format using pandoc.

**Usage:**
```bash
./md2docx.sh input.md [output.docx]
```

**Requirements:**
- pandoc

**Install pandoc:**
```bash
# macOS
brew install pandoc

# Ubuntu/Debian
sudo apt-get install pandoc

# Windows (via chocolatey)
choco install pandoc
```

### 4. Setup Script (`setup_google_forms.sh`)

Automated setup for Google Forms automation. Creates Python virtual environment and installs dependencies.

**Usage:**
```bash
./setup_google_forms.sh
```

This script:
- Checks Python installation
- Creates virtual environment
- Installs required packages
- Validates credentials file
- Provides next steps

## File Descriptions

| File | Type | Description |
|------|------|-------------|
| `create_google_form.py` | Python Script | Main Google Forms creation script |
| `test_parser.py` | Python Script | Test questionnaire parsing |
| `setup_google_forms.sh` | Bash Script | Automated environment setup |
| `md2docx.sh` | Bash Script | Convert markdown to Word |
| `requirements.txt` | Python Deps | Python package dependencies |
| `README_GOOGLE_FORMS.md` | Documentation | Detailed Google Forms setup guide |
| `.gitignore` | Git Config | Prevents committing credentials |

## Setup Overview

### For Google Forms Automation

1. **Install Python dependencies:**
   ```bash
   ./setup_google_forms.sh
   ```

2. **Set up Google Cloud credentials:**
   - Create project in Google Cloud Console
   - Enable Google Forms API
   - Create OAuth 2.0 credentials
   - Download `credentials.json`

3. **Create form:**
   ```bash
   python create_google_form.py
   ```

### For Markdown Conversion

1. **Install pandoc:**
   ```bash
   brew install pandoc  # macOS
   ```

2. **Convert files:**
   ```bash
   ./md2docx.sh lesson.md output.docx
   ```

## Common Tasks

### Create Google Form from Questionnaire
```bash
cd scripts
./setup_google_forms.sh  # First time only
python create_google_form.py
```

### Test Questionnaire Structure
```bash
cd scripts
python test_parser.py --verbose
```

### Convert Lesson to Word
```bash
cd scripts
./md2docx.sh ../lessons/06-computer-basics.md computer-basics.docx
```

### Batch Convert All Lessons
```bash
cd scripts
for lesson in ../lessons/*.md; do
    name=$(basename "$lesson" .md)
    ./md2docx.sh "$lesson" "output/${name}.docx"
done
```

## Troubleshooting

### "credentials.json not found"
- Download OAuth credentials from Google Cloud Console
- Place in `scripts/` directory
- See README_GOOGLE_FORMS.md for details

### "pandoc: command not found"
- Install pandoc: `brew install pandoc` (macOS)
- Or visit: https://pandoc.org/installing.html

### "Permission denied" when running scripts
- Make scripts executable: `chmod +x script_name.sh`

### Python import errors
- Activate virtual environment: `source venv/bin/activate`
- Or run setup: `./setup_google_forms.sh`

## Security Notes

⚠️ **Important:** Never commit sensitive files to version control:
- `credentials.json` - OAuth credentials
- `token.json` - Authentication token
- `last_form_id.txt` - Form IDs

These are listed in `.gitignore` and should not be shared publicly.

## Contributing

When adding new scripts:
1. Add appropriate shebang line (`#!/bin/bash` or `#!/usr/bin/env python3`)
2. Include usage documentation in comments
3. Make script executable (`chmod +x script.sh`)
4. Update this README with script description
5. Add any credentials/tokens to `.gitignore`

## Support

For issues with:
- **Google Forms scripts**: See README_GOOGLE_FORMS.md
- **Markdown conversion**: Check pandoc installation
- **General scripting**: Review error messages and logs

## Related Documentation

- [Developer Guide](../DEVELOPER_GUIDE.md) - Full site development guide
- [Questionnaire](../questionaire/pre-workshop-questionaire.md) - Source questionnaire
- [MS Forms Guide](../questionaire/ms-forms-import-guide.md) - Manual form creation guide
