(function () {
  'use strict';

  // ── 1. Detect base path (root = '', subpage = '../') ────────────────────
  var path = window.location.pathname;
  var depth = path.replace(/\/index\.html$/, '/').replace(/\/$/, '').split('/').filter(Boolean).length;
  var base = depth > 0 ? '../'.repeat(depth) : '';

  // ── 2. Inject component styles ──────────────────────────────────────────
  var styleEl = document.createElement('style');
  styleEl.id = 'site-components-style';
  styleEl.textContent = [
    '@keyframes shine { 100% { left: 125%; } }',
    '.animate-shine { animation: shine 0.8s ease; }',

    /* Mobile menu open state */
    '.mobile-menu-open #navMenu {',
    '  transform: scale(1) !important;',
    '  opacity: 1 !important;',
    '  visibility: visible !important;',
    '}',

    /* Hamburger bars shared style */
    '#mobileMenuBtn .ham-bar {',
    '  display: block;',
    '  width: 20px;',
    '  height: 2px;',
    '  background: #475569;',
    '  border-radius: 9999px;',
    '  transition: transform 0.35s cubic-bezier(0.23,1,0.32,1), opacity 0.25s ease, width 0.2s ease;',
    '  transform-origin: center;',
    '}',

    /* X animation when menu is open */
    '.mobile-menu-open #mobileMenuBtn .ham-bar:nth-child(1) {',
    '  transform: translateY(8px) rotate(45deg);',
    '}',
    '.mobile-menu-open #mobileMenuBtn .ham-bar:nth-child(2) {',
    '  opacity: 0;',
    '  transform: scaleX(0);',
    '}',
    '.mobile-menu-open #mobileMenuBtn .ham-bar:nth-child(3) {',
    '  transform: translateY(-8px) rotate(-45deg);',
    '}',

    /* Active nav link */
    '#headerWrapper .nav-link.active {',
    '  color: #2563eb;',
    '  font-weight: 600;',
    '  background-color: #eff6ff;',
    '}'
  ].join('\n');
  document.head.appendChild(styleEl);

  // ── 3. Header HTML ───────────────────────────────────────────────────────
  var headerHTML = '\n    <div id="headerWrapper" class="fixed top-4 inset-x-0 z-50 px-4 sm:px-6 pointer-events-none">\n      <div class="relative max-w-6xl mx-auto bg-white/80 backdrop-blur-xl rounded-[2rem] border border-white/60 shadow-[0_8px_32px_-4px_rgba(0,0,0,0.08)] ring-1 ring-black/5 pointer-events-auto">\n        <nav class="flex items-center justify-between px-6 py-3">\n\n          <a href="' + (base || '/') + '" class="flex items-center gap-3 group shrink-0">\n            <div class="relative overflow-hidden rounded-full border border-slate-200 shadow-sm transition-transform duration-500 group-hover:scale-105">\n              <img src="' + base + 'img/logonova.png" alt="Gustavo Rameh" class="h-10 w-10 object-cover">\n            </div>\n            <span class="hidden sm:block font-bold text-slate-800 tracking-tight text-lg" style="font-family:\'Poppins\',sans-serif;">Gustavo Rameh</span>\n          </a>\n\n          <ul class="hidden lg:flex items-center gap-1">\n            <li>\n              <a href="' + (base || '/') + '" class="nav-link relative group px-5 py-2.5 text-sm font-medium text-slate-600 transition-all duration-300 rounded-full hover:bg-slate-50" style="font-family:'Inter',sans-serif;">\n                <span class="relative z-10">In\u00edcio</span>\n                <span class="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full bg-blue-500 opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125"></span>\n              </a>\n            </li>\n            <li>\n              <a href="' + base + 'sobre/" class="nav-link relative group px-5 py-2.5 text-sm font-medium text-slate-600 transition-all duration-300 rounded-full hover:bg-slate-50" style="font-family:\'Inter\',sans-serif;">\n                <span class="relative z-10">Sobre</span>\n                <span class="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full bg-blue-500 opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125"></span>\n              </a>\n            </li>\n            <li>\n              <a href="' + base + 'atendimento-online/" class="nav-link relative group px-5 py-2.5 text-sm font-medium text-slate-600 transition-all duration-300 rounded-full hover:bg-slate-50" style="font-family:\'Inter\',sans-serif;">\n                <span class="relative z-10">Terapia Presencial e Online</span>\n                <span class="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full bg-blue-500 opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125"></span>\n              </a>\n            </li>\n            <li class="flex items-center gap-1 ml-2">\n              <a href="https://www.instagram.com/gustavoramehpsi/" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full hover:bg-slate-100 transition-colors text-slate-600" title="Instagram">\n                <i class="fab fa-instagram text-base"></i>\n              </a>\n              <a href="https://wa.me/5532988178494" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full hover:bg-slate-100 transition-colors text-slate-600" title="WhatsApp">\n                <i class="fab fa-whatsapp text-base"></i>\n              </a>\n            </li>\n          </ul>\n\n          <div class="flex items-center gap-3">\n            <a href="https://wa.me/5532988178494" target="_blank"\n               class="hidden lg:flex group relative items-center gap-2 px-5 py-2.5 rounded-full text-white text-sm font-bold overflow-hidden transition-all duration-300 hover:-translate-y-0.5"\n               style="background-color:#3b82f6;box-shadow:0 4px 14px rgba(59,130,246,0.4);font-family:\'Poppins\',sans-serif;">\n              <div class="absolute top-0 -inset-full h-full w-1/2 z-5 block transform -skew-x-12 bg-gradient-to-r from-transparent to-white opacity-20 group-hover:animate-shine"></div>\n              <i class="fab fa-whatsapp text-base relative z-10"></i>\n              <span class="relative z-10">Agendar Consulta</span>\n            </a>\n            <button id="mobileMenuBtn"\n                    class="lg:hidden w-11 h-11 flex flex-col items-center justify-center gap-[6px] rounded-full hover:bg-slate-100/50 transition-colors"\n                    aria-label="Abrir menu" aria-expanded="false">\n              <span class="ham-bar"></span>\n              <span class="ham-bar"></span>\n              <span class="ham-bar"></span>\n            </button>\n          </div>\n        </nav>\n\n        <div id="navMenu" class="absolute top-[calc(100%+10px)] left-0 right-0 origin-top transform scale-95 opacity-0 invisible transition-all duration-300 ease-[cubic-bezier(0.16,1,0.3,1)]">\n          <div class="bg-white/95 backdrop-blur-2xl border border-white/60 rounded-[2rem] p-6 shadow-[0_20px_40px_-5px_rgba(0,0,0,0.1)] ring-1 ring-black/5">\n            <ul class="flex flex-col gap-1">\n              <li>\n                <a href="' + (base || '/') + '"\n                   class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]"\n                   style="font-family:'Inter',sans-serif;">\n                  In\u00edcio <i class="fas fa-chevron-right text-xs opacity-30"></i>\n                </a>\n              </li>\n              <li>\n                <a href="' + base + 'sobre/"\n                   class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]"\n                   style="font-family:\'Inter\',sans-serif;">\n                  Sobre <i class="fas fa-chevron-right text-xs opacity-30"></i>\n                </a>\n              </li>\n              <li>\n                <a href="' + base + 'atendimento-online/"\n                   class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]"\n                   style="font-family:\'Inter\',sans-serif;">\n                  Terapia Presencial e Online <i class="fas fa-chevron-right text-xs opacity-30"></i>\n                </a>\n              </li>\n              <li>\n                <a href="https://www.instagram.com/gustavoramehpsi/" target="_blank"\n                   class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]"\n                   style="font-family:\'Inter\',sans-serif;">\n                  <span><i class="fab fa-instagram mr-2 text-pink-500"></i>Instagram</span>\n                  <i class="fas fa-chevron-right text-xs opacity-30"></i>\n                </a>\n              </li>\n              <li>\n                <a href="https://wa.me/5532988178494" target="_blank"\n                   class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]"\n                   style="font-family:\'Inter\',sans-serif;">\n                  <span><i class="fab fa-whatsapp mr-2 text-green-500"></i>WhatsApp</span>\n                  <i class="fas fa-chevron-right text-xs opacity-30"></i>\n                </a>\n              </li>\n            </ul>\n            <div class="mt-5 pt-5 border-t border-slate-100">\n              <a href="https://wa.me/5532988178494" target="_blank"\n                 class="group relative flex items-center justify-center gap-2 w-full px-5 py-3 rounded-full text-white text-sm font-bold overflow-hidden transition-all duration-300"\n                 style="background-color:#3b82f6;box-shadow:0 4px 14px rgba(59,130,246,0.4);font-family:\'Poppins\',sans-serif;">\n                <div class="absolute top-0 -inset-full h-full w-1/2 z-5 block transform -skew-x-12 bg-gradient-to-r from-transparent to-white opacity-20 group-hover:animate-shine"></div>\n                <i class="fab fa-whatsapp text-base relative z-10"></i>\n                <span class="relative z-10">Agendar Consulta</span>\n              </a>\n            </div>\n          </div>\n        </div>\n      </div>\n    </div>\n  ';

  // ── 4. Footer HTML ───────────────────────────────────────────────────────
  var footerHTML = '\n    <footer class="bg-slate-900 text-white pt-14 pb-10">\n      <div class="max-w-5xl mx-auto px-6 text-center">\n        <div class="flex justify-center mb-5">\n          <img src="' + base + 'img/logonova.png" alt="Gustavo Rameh" class="h-16 w-16 rounded-full object-cover border-2 border-white/20">\n        </div>\n        <h3 class="font-bold text-xl mb-1" style="font-family:\'Poppins\',sans-serif;">Gustavo Rameh</h3>\n        <p class="text-slate-400 text-sm mb-6">Psic\u00f3logo Cl\u00ednico &middot; CRP 04/43395</p>\n        <div class="flex justify-center gap-3 mb-8">\n          <a href="https://www.instagram.com/gustavoramehpsi/" target="_blank" class="w-10 h-10 bg-white/10 hover:bg-white/20 rounded-full flex items-center justify-center transition-colors text-sm" title="Instagram"><i class="fab fa-instagram"></i></a>\n          <a href="https://wa.me/5532988178494" target="_blank" class="w-10 h-10 bg-white/10 hover:bg-white/20 rounded-full flex items-center justify-center transition-colors text-sm" title="WhatsApp"><i class="fab fa-whatsapp"></i></a>\n          <a href="https://www.facebook.com/psicologogustavorameh" target="_blank" class="w-10 h-10 bg-white/10 hover:bg-white/20 rounded-full flex items-center justify-center transition-colors text-sm" title="Facebook"><i class="fab fa-facebook-f"></i></a>\n          <a href="tel:+5532988178494" class="w-10 h-10 bg-white/10 hover:bg-white/20 rounded-full flex items-center justify-center transition-colors text-sm" title="Telefone"><i class="fas fa-phone"></i></a>\n        </div>\n        <div class="border-t border-white/10 pt-6">\n          <p class="text-slate-500 text-sm">&copy; 2025 Gustavo Rameh &middot; Todos os direitos reservados.</p>\n        </div>\n      </div>\n    </footer>\n  ';

  // ── 5. Inject into placeholders ──────────────────────────────────────────
  var headerPlaceholder = document.getElementById('site-header');
  if (headerPlaceholder) {
    headerPlaceholder.outerHTML = headerHTML;
  }

  var footerPlaceholder = document.getElementById('site-footer');
  if (footerPlaceholder) {
    footerPlaceholder.outerHTML = footerHTML;
  }

  // ── 6. Active nav link highlight ─────────────────────────────────────────
  var currentPath = window.location.pathname;
  document.querySelectorAll('#headerWrapper .nav-link').forEach(function (a) {
    var href = a.getAttribute('href') || '';
    // Normalize: remove leading ../
    var normalized = href.replace(/^(\.\.\/)+/, '/');
    if (normalized !== '/' && currentPath.indexOf(normalized.replace(/\/$/, '')) !== -1) {
      a.classList.add('active');
    }
  });

  // ── 7. Hamburger toggle ───────────────────────────────────────────────────
  var wrapper = document.getElementById('headerWrapper');
  var btn = document.getElementById('mobileMenuBtn');
  if (btn && wrapper) {
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var isOpen = wrapper.classList.toggle('mobile-menu-open');
      btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
    document.addEventListener('click', function (e) {
      if (wrapper && !wrapper.contains(e.target)) {
        wrapper.classList.remove('mobile-menu-open');
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // ── 8. Scroll shadow ─────────────────────────────────────────────────────
  window.addEventListener('scroll', function () {
    var nav = wrapper && wrapper.querySelector(':scope > div');
    if (nav) {
      nav.style.boxShadow = window.scrollY > 30
        ? '0 16px 48px -8px rgba(0,0,0,0.18)'
        : '';
    }
  }, { passive: true });

})();
