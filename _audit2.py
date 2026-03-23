import os
base_dir = r'c:\Users\crist\Desktop\projeto-rameh\gustavo-rameh'
pages = [
    'index.html', 'sobre/index.html', 'blog/index.html',
    'individual/index.html', 'coaching/index.html'
]
for p in pages:
    with open(os.path.join(base_dir, p.replace('/', os.sep)), encoding='utf-8') as f:
        html = f.read()
    checks = {
        'site-header':    'id="site-header"' in html,
        'site-footer':    'id="site-footer"' in html,
        'components.js':  'js/components.js' in html,
        'NO headerWrapper': 'id="headerWrapper"' not in html,
        'NO bg-slate-footer': '<footer class="bg-slate-900' not in html,
        'NO hamburger-styles': 'hamburger-styles' not in html,
        'NO inline-js': 'var wrapper = document.getElementById' not in html,
    }
    status = all(checks.values())
    fails = [k for k, v in checks.items() if not v]
    print(f'{"OK" if status else "FAIL"} {p}' + (f' -- FAILS: {fails}' if fails else ''))
