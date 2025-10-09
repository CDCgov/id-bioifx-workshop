#!/usr/bin/env python3
"""
Fix question numbering in the questionnaire.
Renumbers all questions sequentially from 1 onwards.
"""

import re

questionnaire_path = '../questionaire/pre-workshop-questionaire.md'

with open(questionnaire_path, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
new_lines = []
next_number = 1

for line in lines:
    match = re.match(r'^### (\d+)\. (.+)$', line)
    if match:
        question_text = match.group(2)
        new_lines.append(f'### {next_number}. {question_text}')
        next_number += 1
    else:
        new_lines.append(line)

# Write back
with open(questionnaire_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print(f"Fixed question numbering. Total questions: {next_number - 1}")
