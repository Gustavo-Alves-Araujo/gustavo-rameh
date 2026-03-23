import os, re

pages = [
    'index.html',
    'sobre/index.html',
    'atendimento-online/index.html',
    'individual/index.html',
    'casal/index.html',
    'grupo/index.html',
    'coaching/index.html',
    'emagrecimento/index.html',
    'blog/index.html'
]

for p in pages:
    c = open(p, encoding='utf-8').read()
    has_header_wrapper = 'id="headerWrapper"' in c
    has_footer = '</footer>' in c
    phone_in_ul = bool(re.search(r'<ul[^>]*>(.*?)98817-8494(.*?)</ul>', c, re.DOTALL))
    phone_li = '(32) 98817-8494' in c
    print(f'{p}: headerWrapper={has_header_wrapper} footer={has_footer} phone_li={phone_li}')
