with open('js/components.js', encoding='utf-8') as f:
    txt = f.read()

# The Inicio links were written with unescaped 'Inter' (bare single quotes inside the JS string)
# This breaks the JS string. We need backslash-escaped: \'Inter\'

# Actual bad string in file: style="font-family:'Inter',sans-serif;"
# Actual good string:        style="font-family:\'Inter\',sans-serif;"

bad  = "font-family:'Inter',sans-serif;"
good = "font-family:\\'Inter\\',sans-serif;"

count = txt.count(bad)
print(f'Broken occurrences to fix: {count}')
txt = txt.replace(bad, good)

with open('js/components.js', 'w', encoding='utf-8') as f:
    f.write(txt)
print('Done')
