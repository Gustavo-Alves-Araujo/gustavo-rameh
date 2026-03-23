import os

BASE = r'c:\Users\crist\Desktop\projeto-rameh\gustavo-rameh'

# --- components.js: add Início link in desktop ul and mobile navMenu ---
# Desktop: before the Sobre <li>
COMP = os.path.join(BASE, 'js', 'components.js')
with open(COMP, encoding='utf-8') as f:
    txt = f.read()

OLD_DESKTOP = r"              <a href=\"' + base + 'sobre/\" class=\"nav-link"
NEW_DESKTOP = (
    r"              <a href=\"' + (base || '/') + '\" class=\"nav-link relative group px-5 py-2.5 text-sm font-medium text-slate-600 transition-all duration-300 rounded-full hover:bg-slate-50\" style=\"font-family:'Inter',sans-serif;\">"
    + "\n"
    + r"                <span class=\"relative z-10\">Início</span>"
    + "\n"
    + r"                <span class=\"absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full bg-blue-500 opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125\"></span>"
    + "\n"
    + r"              </a>"
    + "\n"
    + r"            </li>"
    + "\n"
    + r"            <li>"
    + "\n"
    + r"              <a href=\"' + base + 'sobre/\" class=\"nav-link"
)

OLD_MOBILE = r"              <li>" + "\n" + r"                <a href=\"' + base + 'sobre/\""
NEW_MOBILE = (
    r"              <li>"
    + "\n"
    + r"                <a href=\"' + (base || '/') + '\""
    + "\n"
    + r"                   class=\"flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]\""
    + "\n"
    + r"                   style=\"font-family:'Inter',sans-serif;\">"
    + "\n"
    + r"                  Início <i class=\"fas fa-chevron-right text-xs opacity-30\"></i>"
    + "\n"
    + r"                </a>"
    + "\n"
    + r"              </li>"
    + "\n"
    + r"              <li>"
    + "\n"
    + r"                <a href=\"' + base + 'sobre/\""
)

n1 = txt.count(OLD_DESKTOP)
n2 = txt.count(OLD_MOBILE)
txt = txt.replace(OLD_DESKTOP, NEW_DESKTOP, 1)
txt = txt.replace(OLD_MOBILE, NEW_MOBILE, 1)
with open(COMP, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f'components.js: desktop={n1} mobile={n2}')

# --- Subpages: add Início in desktop ul and mobile navMenu ---
SUBPAGES = [
    'sobre/index.html', 'atendimento-online/index.html', 'individual/index.html',
    'casal/index.html', 'grupo/index.html', 'coaching/index.html',
    'emagrecimento/index.html', 'blog/index.html',
]

DESKTOP_OLD = '''                    <li>
                        <a href="../sobre/" class="relative group px-5 py-2.5 text-sm font-medium text-slate-600 transition-all duration-300 rounded-full hover:bg-slate-50" style="font-family: 'Inter', sans-serif;">
                            <span class="relative z-10">Sobre</span>'''

DESKTOP_NEW = '''                    <li>
                        <a href="../" class="relative group px-5 py-2.5 text-sm font-medium text-slate-600 transition-all duration-300 rounded-full hover:bg-slate-50" style="font-family: 'Inter', sans-serif;">
                            <span class="relative z-10">Início</span>
                            <span class="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full bg-blue-500 opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125"></span>
                        </a>
                    </li>
                    <li>
                        <a href="../sobre/" class="relative group px-5 py-2.5 text-sm font-medium text-slate-600 transition-all duration-300 rounded-full hover:bg-slate-50" style="font-family: 'Inter', sans-serif;">
                            <span class="relative z-10">Sobre</span>'''

MOBILE_OLD = '''                        <li>
                            <a href="../sobre/" class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]" style="font-family: 'Inter', sans-serif;">
                                Sobre <i class="fas fa-chevron-right text-xs opacity-30"></i>'''

MOBILE_NEW = '''                        <li>
                            <a href="../" class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]" style="font-family: 'Inter', sans-serif;">
                                Início <i class="fas fa-chevron-right text-xs opacity-30"></i>
                            </a>
                        </li>
                        <li>
                            <a href="../sobre/" class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]" style="font-family: 'Inter', sans-serif;">
                                Sobre <i class="fas fa-chevron-right text-xs opacity-30"></i>'''

for page in SUBPAGES:
    path = os.path.join(BASE, page.replace('/', os.sep))
    with open(path, encoding='utf-8') as f:
        html = f.read()
    d = html.count(DESKTOP_OLD)
    m = html.count(MOBILE_OLD)
    html = html.replace(DESKTOP_OLD, DESKTOP_NEW, 1)
    html = html.replace(MOBILE_OLD, MOBILE_NEW, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'{page}: desktop={d} mobile={m}')
