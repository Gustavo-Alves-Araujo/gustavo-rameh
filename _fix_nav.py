import os
base = r'c:\Users\crist\Desktop\projeto-rameh\gustavo-rameh'
files = [
    'js/components.js',
    'sobre/index.html', 'atendimento-online/index.html', 'individual/index.html',
    'casal/index.html', 'grupo/index.html', 'coaching/index.html',
    'emagrecimento/index.html', 'blog/index.html', 'blog/post.html'
]
patterns = [
    (
        '<span class="relative z-10">Atendimento Online</span>',
        '<span class="relative z-10">Terapia Presencial e Online</span>'
    ),
    (
        'Atendimento Online <i class="fas fa-chevron-right text-xs opacity-30"></i>',
        'Terapia Presencial e Online <i class="fas fa-chevron-right text-xs opacity-30"></i>'
    ),
]
for f in files:
    path = os.path.join(base, f.replace('/', os.sep))
    with open(path, encoding='utf-8') as fh:
        html = fh.read()
    total = 0
    for old, new in patterns:
        count = html.count(old)
        html = html.replace(old, new)
        total += count
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print(f'{f}: {total} replaced')
