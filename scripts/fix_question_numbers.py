#!/usr/bin/env python3
"""
Fix question numbering in the questionnaire.
Questions 1-19 are correct.
Questions after 19 need to be renumbered sequentially from 20 onwards.
"""

import re

questionnaire_path = '../questionaire/pre-workshop-questionaire.md'

with open(questionnaire_path, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
new_lines = []
next_number = 20
seen_19 = False

for line in lines:
    match = re.match(r'^### (\d+)\. (.+)$', line)
    if match:
        current_num = int(match.group(1))
        question_text = match.group(2)
        
        # Keep questions 1-19 as-is
        if current_num < 20 and not seen_19:
            new_lines.append(line)
            if current_num == 19:
                seen_19 = True
        # After seeing Q19, renumber everything from 20 onwards
        elif seen_19:
            new_lines.append(f'### {next_number}. {question_text}')
            next_number += 1
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

# Write back
with open(questionnaire_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print(f"Fixed question numbering. Last question number: {next_number - 1}")
