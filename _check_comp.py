import re

with open('js/components.js', encoding='utf-8') as f:
    txt = f.read()

# Find all font-family occurrences and check for unescaped quotes
matches = [(m.start(), m.group()) for m in re.finditer(r"font-family:[^;\"]+Inter", txt)]
for start, match in matches:
    print(repr(txt[start-20:start+60]))
print('---')
print('Total font-family Inter occurrences:', len(matches))
