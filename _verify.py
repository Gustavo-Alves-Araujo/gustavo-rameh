import os
base = r'c:\Users\crist\Desktop\projeto-rameh\gustavo-rameh'
pages = ['sobre/index.html','individual/index.html','blog/index.html']
for p in pages:
    with open(os.path.join(base, p.replace('/',os.sep)), encoding='utf-8') as f:
        html = f.read()
    checks = {
        'has headerWrapper':    'id="headerWrapper"' in html,
        'has 3 ham-bars':       html.count('<span class="ham-bar">') == 3,
        'has footer inline':    '<footer class="bg-slate-900' in html,
        'has hamburger-styles': 'hamburger-styles' in html,
        'has inline JS':        'wrapper.classList.toggle' in html,
        'NO site-header':       'id="site-header"' not in html,
        'NO site-footer':       'id="site-footer"' not in html,
        'NO components.js':     'components.js' not in html,
    }
    ok = all(checks.values())
    fails = [k for k,v in checks.items() if not v]
    print(('OK' if ok else 'FAIL') + f'  {p}' + (f'  -- {fails}' if fails else ''))
