#!/usr/bin/env python3
"""
Reverts subpages to inline header/footer HTML (no components.js dependency).
- Keeps index.html with the component approach.
- Restores inline headerWrapper, hamburger CSS, footer, and hamburger JS for all subpages.
- Uses the NEW design: 3-bar hamburger, no phone number in nav.
"""
import os

BASE_DIR = r'c:\Users\crist\Desktop\projeto-rameh\gustavo-rameh'

SUBPAGES = [
    'sobre/index.html',
    'atendimento-online/index.html',
    'individual/index.html',
    'casal/index.html',
    'grupo/index.html',
    'coaching/index.html',
    'emagrecimento/index.html',
    'blog/index.html',
]

HAMBURGER_STYLE = """    <style id="hamburger-styles">
        @keyframes shine { 100% { left: 125%; } }
        .animate-shine { animation: shine 0.8s ease; }
        .mobile-menu-open #navMenu {
            transform: scale(1) !important;
            opacity: 1 !important;
            visibility: visible !important;
        }
        #mobileMenuBtn .ham-bar {
            display: block;
            width: 20px;
            height: 2px;
            background: #475569;
            border-radius: 9999px;
            transition: transform 0.35s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.25s ease;
            transform-origin: center;
        }
        .mobile-menu-open #mobileMenuBtn .ham-bar:nth-child(1) {
            transform: translateY(8px) rotate(45deg);
        }
        .mobile-menu-open #mobileMenuBtn .ham-bar:nth-child(2) {
            opacity: 0;
            transform: scaleX(0);
        }
        .mobile-menu-open #mobileMenuBtn .ham-bar:nth-child(3) {
            transform: translateY(-8px) rotate(-45deg);
        }
    </style>"""

HEADER_HTML = """    <div id="headerWrapper" class="fixed top-4 inset-x-0 z-50 px-4 sm:px-6 pointer-events-none">
        <div class="relative max-w-6xl mx-auto bg-white/80 backdrop-blur-xl rounded-[2rem] border border-white/60 shadow-[0_8px_32px_-4px_rgba(0,0,0,0.08)] ring-1 ring-black/5 pointer-events-auto">
            <nav class="flex items-center justify-between px-6 py-3">
                <a href="../" class="flex items-center gap-3 group shrink-0">
                    <div class="relative overflow-hidden rounded-full border border-slate-200 shadow-sm transition-transform duration-500 group-hover:scale-105">
                        <img src="../img/logonova.png" alt="Gustavo Rameh" class="h-10 w-10 object-cover">
                    </div>
                    <span class="hidden sm:block font-bold text-slate-800 tracking-tight text-lg" style="font-family: 'Poppins', sans-serif;">Gustavo Rameh</span>
                </a>
                <ul class="hidden lg:flex items-center gap-1">
                    <li>
                        <a href="../sobre/" class="relative group px-5 py-2.5 text-sm font-medium text-slate-600 transition-all duration-300 rounded-full hover:bg-slate-50" style="font-family: 'Inter', sans-serif;">
                            <span class="relative z-10">Sobre</span>
                            <span class="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full bg-blue-500 opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125"></span>
                        </a>
                    </li>
                    <li>
                        <a href="../atendimento-online/" class="relative group px-5 py-2.5 text-sm font-medium text-slate-600 transition-all duration-300 rounded-full hover:bg-slate-50" style="font-family: 'Inter', sans-serif;">
                            <span class="relative z-10">Terapia Presencial e Online</span>
                            <span class="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full bg-blue-500 opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125"></span>
                        </a>
                    </li>
                    <li class="flex items-center gap-1 ml-2">
                        <a href="https://www.instagram.com/gustavoramehpsi/" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full hover:bg-slate-100 transition-colors text-slate-600" title="Instagram">
                            <i class="fab fa-instagram text-base"></i>
                        </a>
                        <a href="https://wa.me/5532988178494" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full hover:bg-slate-100 transition-colors text-slate-600" title="WhatsApp">
                            <i class="fab fa-whatsapp text-base"></i>
                        </a>
                    </li>
                </ul>
                <div class="flex items-center gap-3">
                    <a href="https://wa.me/5532988178494" target="_blank" class="hidden lg:flex group relative items-center gap-2 px-5 py-2.5 rounded-full text-white text-sm font-bold overflow-hidden transition-all duration-300 hover:-translate-y-0.5" style="background-color: #3b82f6; box-shadow: 0 4px 14px rgba(59,130,246,0.4); font-family: 'Poppins', sans-serif;">
                        <div class="absolute top-0 -inset-full h-full w-1/2 z-5 block transform -skew-x-12 bg-gradient-to-r from-transparent to-white opacity-20 group-hover:animate-shine"></div>
                        <i class="fab fa-whatsapp text-base relative z-10"></i>
                        <span class="relative z-10">Agendar Consulta</span>
                    </a>
                    <button id="mobileMenuBtn" class="lg:hidden w-11 h-11 flex flex-col items-center justify-center gap-[6px] rounded-full hover:bg-slate-100/50 transition-colors" aria-label="Abrir menu" aria-expanded="false">
                        <span class="ham-bar"></span>
                        <span class="ham-bar"></span>
                        <span class="ham-bar"></span>
                    </button>
                </div>
            </nav>
            <div id="navMenu" class="absolute top-[calc(100%+10px)] left-0 right-0 origin-top transform scale-95 opacity-0 invisible transition-all duration-300 ease-[cubic-bezier(0.16,1,0.3,1)]">
                <div class="bg-white/95 backdrop-blur-2xl border border-white/60 rounded-[2rem] p-6 shadow-[0_20px_40px_-5px_rgba(0,0,0,0.1)] ring-1 ring-black/5">
                    <ul class="flex flex-col gap-1">
                        <li>
                            <a href="../sobre/" class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]" style="font-family: 'Inter', sans-serif;">
                                Sobre <i class="fas fa-chevron-right text-xs opacity-30"></i>
                            </a>
                        </li>
                        <li>
                            <a href="../atendimento-online/" class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]" style="font-family: 'Inter', sans-serif;">
                                Terapia Presencial e Online <i class="fas fa-chevron-right text-xs opacity-30"></i>
                            </a>
                        </li>
                        <li>
                            <a href="https://www.instagram.com/gustavoramehpsi/" target="_blank" class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]" style="font-family: 'Inter', sans-serif;">
                                <span><i class="fab fa-instagram mr-2 text-pink-500"></i>Instagram</span>
                                <i class="fas fa-chevron-right text-xs opacity-30"></i>
                            </a>
                        </li>
                        <li>
                            <a href="https://wa.me/5532988178494" target="_blank" class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]" style="font-family: 'Inter', sans-serif;">
                                <span><i class="fab fa-whatsapp mr-2 text-green-500"></i>WhatsApp</span>
                                <i class="fas fa-chevron-right text-xs opacity-30"></i>
                            </a>
                        </li>
                    </ul>
                    <div class="mt-5 pt-5 border-t border-slate-100">
                        <a href="https://wa.me/5532988178494" target="_blank" class="group relative flex items-center justify-center gap-2 w-full px-5 py-3 rounded-full text-white text-sm font-bold overflow-hidden transition-all duration-300" style="background-color: #3b82f6; box-shadow: 0 4px 14px rgba(59,130,246,0.4); font-family: 'Poppins', sans-serif;">
                            <div class="absolute top-0 -inset-full h-full w-1/2 z-5 block transform -skew-x-12 bg-gradient-to-r from-transparent to-white opacity-20 group-hover:animate-shine"></div>
                            <i class="fab fa-whatsapp text-base relative z-10"></i>
                            <span class="relative z-10">Agendar Consulta</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>"""

FOOTER_HTML = """    <footer class="bg-slate-900 text-white pt-14 pb-10">
        <div class="max-w-5xl mx-auto px-6 text-center">
            <div class="flex justify-center mb-5">
                <img src="../img/logonova.png" alt="Gustavo Rameh" class="h-16 w-16 rounded-full object-cover border-2 border-white/20">
            </div>
            <h3 class="font-bold text-xl mb-1" style="font-family: 'Poppins', sans-serif;">Gustavo Rameh</h3>
            <p class="text-slate-400 text-sm mb-6">Psic\u00f3logo Cl\u00ednico &middot; CRP 04/43395</p>
            <div class="flex justify-center gap-3 mb-8">
                <a href="https://www.instagram.com/gustavoramehpsi/" target="_blank" class="w-10 h-10 bg-white/10 hover:bg-white/20 rounded-full flex items-center justify-center transition-colors text-sm" title="Instagram"><i class="fab fa-instagram"></i></a>
                <a href="https://wa.me/5532988178494" target="_blank" class="w-10 h-10 bg-white/10 hover:bg-white/20 rounded-full flex items-center justify-center transition-colors text-sm" title="WhatsApp"><i class="fab fa-whatsapp"></i></a>
                <a href="https://www.facebook.com/psicologogustavorameh" target="_blank" class="w-10 h-10 bg-white/10 hover:bg-white/20 rounded-full flex items-center justify-center transition-colors text-sm" title="Facebook"><i class="fab fa-facebook-f"></i></a>
                <a href="tel:+5532988178494" class="w-10 h-10 bg-white/10 hover:bg-white/20 rounded-full flex items-center justify-center transition-colors text-sm" title="Telefone"><i class="fas fa-phone"></i></a>
            </div>
            <div class="border-t border-white/10 pt-6">
                <p class="text-slate-500 text-sm">&copy; 2025 Gustavo Rameh &middot; Todos os direitos reservados.</p>
            </div>
        </div>
    </footer>"""

HAMBURGER_JS = """    <script>
    document.addEventListener('DOMContentLoaded', function() {
        var wrapper = document.getElementById('headerWrapper');
        var btn = document.getElementById('mobileMenuBtn');
        if (btn && wrapper) {
            btn.addEventListener('click', function(e) {
                e.stopPropagation();
                var isOpen = wrapper.classList.toggle('mobile-menu-open');
                btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
            });
            document.addEventListener('click', function(e) {
                if (wrapper && !wrapper.contains(e.target)) {
                    wrapper.classList.remove('mobile-menu-open');
                    btn.setAttribute('aria-expanded', 'false');
                }
            });
        }
        window.addEventListener('scroll', function() {
            var nav = wrapper && wrapper.querySelector(':scope > div');
            if (nav) {
                nav.style.boxShadow = window.scrollY > 30
                    ? '0 16px 48px -8px rgba(0,0,0,0.18)'
                    : '';
            }
        }, { passive: true });
    });
    </script>"""

print('Reverting subpages to inline header/footer...')
for page in SUBPAGES:
    full_path = os.path.join(BASE_DIR, page.replace('/', os.sep))
    with open(full_path, 'r', encoding='utf-8') as f:
        html = f.read()
    changes = []

    # 1. Add hamburger-styles before </head>
    if 'hamburger-styles' not in html:
        html = html.replace('</head>', HAMBURGER_STYLE + '\n</head>', 1)
        changes.append('added hamburger-styles')

    # 2. Replace site-header placeholder with inline header
    if '<div id="site-header"></div>' in html:
        html = html.replace('<div id="site-header"></div>', HEADER_HTML, 1)
        changes.append('restored inline header')
    else:
        print(f'  WARNING: site-header not found in {page}')

    # 3. Replace site-footer placeholder with inline footer
    if '<div id="site-footer"></div>' in html:
        html = html.replace('<div id="site-footer"></div>', FOOTER_HTML, 1)
        changes.append('restored inline footer')
    else:
        print(f'  WARNING: site-footer not found in {page}')

    # 4. Replace components.js script tag with inline hamburger JS
    if '<script src="../js/components.js"></script>' in html:
        html = html.replace('<script src="../js/components.js"></script>', HAMBURGER_JS, 1)
        changes.append('restored inline JS')
    else:
        print(f'  WARNING: components.js script not found in {page}')

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  OK  {page}: {", ".join(changes) if changes else "no changes"}')

print('\nDone! index.html still uses components.js.')
