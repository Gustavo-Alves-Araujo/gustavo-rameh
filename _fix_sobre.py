f = r'c:/Users/crist/Desktop/projeto-rameh/gustavo-rameh/sobre/index.html'
c = open(f, encoding='utf-8').read()
changes = []

# ============================================================
# 1. PAGE TITLE - remove Coach reference
# ============================================================
OLD_TITLE = '<title>Sobre Mim - Gustavo Rameh | Psic\u00f3logo Cl\u00ednico e Coach</title>'
NEW_TITLE = '<title>Sobre Mim - Gustavo Rameh | Psic\u00f3logo Cl\u00ednico</title>'
if OLD_TITLE in c:
    c = c.replace(OLD_TITLE, NEW_TITLE, 1)
    changes.append("Title updated")

# ============================================================
# 2. DESKTOP NAV - replace entire <nav> block
# ============================================================
OLD_DESK_NAV = '''            <nav class="hidden lg:flex items-center gap-4 xl:gap-5 font-medium text-primary text-sm xl:text-base">
                <a href="../individual/" class="hover:text-secondary transition-colors">Terapia Individual</a>
                <a href="../casal/" class="hover:text-secondary transition-colors">Terapia de Casal</a>
                <a href="../grupo/" class="hover:text-secondary transition-colors">Terapia em Grupo</a>
                
                 <div class="relative group">
                    <button class="flex items-center hover:text-secondary transition-colors cursor-pointer py-2">
                        Coaching <i class="fas fa-chevron-down text-xs ml-1"></i>
                    </button>
                    <div class="absolute left-0 top-full pt-2 w-56 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 transform group-hover:translate-y-0 translate-y-2">
                        <div class="bg-white rounded-xl shadow-xl border border-gray-100 overflow-hidden">
                            <a href="../coaching/" class="block px-6 py-3 hover:bg-blue-50 text-primary hover:text-secondary transition-colors border-b border-gray-50">Coaching Individual</a>
                            <a href="../emagrecimento/" class="block px-6 py-3 hover:bg-blue-50 text-primary hover:text-secondary transition-colors">Emagrecimento</a>
                        </div>
                    </div>
                </div>

                <a href="../atendimento-online/" class="hover:text-secondary transition-colors">Atendimento Online</a>
                <a href="index.html" class="text-secondary font-bold">Sobre</a>
            </nav>'''

NEW_DESK_NAV = '''            <nav class="hidden lg:flex items-center gap-4 xl:gap-5 font-medium text-primary text-sm xl:text-base">
                <a href="index.html" class="text-secondary font-bold">Sobre</a>
                <a href="../atendimento-online/" class="hover:text-secondary transition-colors">Terapia Presencial e Online</a>
                <a href="tel:+5532988178494" class="flex items-center gap-1.5 hover:text-secondary transition-colors" title="(32) 98817-8494">
                    <i class="fas fa-phone text-xs"></i> (32) 98817-8494
                </a>
                <a href="https://www.instagram.com/gustavoramehpsi/" target="_blank" class="hover:text-secondary transition-colors" title="Instagram">
                    <i class="fab fa-instagram text-lg"></i>
                </a>
                <a href="https://wa.me/5532988178494" target="_blank" class="hover:text-secondary transition-colors" title="WhatsApp">
                    <i class="fab fa-whatsapp text-lg"></i>
                </a>
            </nav>'''

if OLD_DESK_NAV in c:
    c = c.replace(OLD_DESK_NAV, NEW_DESK_NAV, 1)
    changes.append("Desktop nav updated")
else:
    changes.append("FAIL: Desktop nav not found")

# ============================================================
# 3. MOBILE NAV - replace entire mobile nav <nav> block
# ============================================================
OLD_MOB_NAV = '''                <nav class="flex flex-col gap-1.5 pt-3">
                    <a href="../individual/" class="px-4 py-2.5 hover:bg-blue-50 rounded-lg transition-colors text-primary hover:text-secondary font-medium text-sm">
                        <i class="fas fa-brain mr-2"></i> Terapia Individual
                    </a>
                    <a href="../casal/" class="px-4 py-2.5 hover:bg-blue-50 rounded-lg transition-colors text-primary hover:text-secondary font-medium text-sm">
                        <i class="fas fa-user-group mr-2"></i> Terapia de Casal
                    </a>
                    <a href="../grupo/" class="px-4 py-2.5 hover:bg-blue-50 rounded-lg transition-colors text-primary hover:text-secondary font-medium text-sm">
                        <i class="fas fa-users mr-2"></i> Terapia em Grupo
                    </a>
                    <div class="px-4 py-2.5">
                        <button id="coaching-mobile-btn" class="w-full flex items-center justify-between text-primary hover:text-secondary font-medium text-sm">
                            <span><i class="fas fa-chart-line mr-2"></i> Coaching</span>
                            <i class="fas fa-chevron-down text-xs transition-transform" id="coaching-chevron"></i>
                        </button>
                        <div id="coaching-mobile-menu" class="hidden mt-2 ml-6 space-y-1.5">
                            <a href="../coaching/" class="block px-4 py-2 hover:bg-blue-50 rounded-lg transition-colors text-primary hover:text-secondary text-sm">
                                <i class="fas fa-user-tie mr-2"></i> Coaching Individual
                            </a>
                            <a href="../emagrecimento/" class="block px-4 py-2 hover:bg-blue-50 rounded-lg transition-colors text-primary hover:text-secondary text-sm">
                                <i class="fas fa-weight mr-2"></i> Emagrecimento
                            </a>
                        </div>
                    </div>
                    <a href="../atendimento-online/" class="px-4 py-2.5 hover:bg-blue-50 rounded-lg transition-colors text-primary hover:text-secondary font-medium text-sm">
                        <i class="fas fa-laptop-house mr-2"></i> Atendimento Online
                    </a>
                    <a href="index.html" class="px-4 py-2.5 hover:bg-blue-50 rounded-lg transition-colors text-primary hover:text-secondary font-medium text-sm">
                        <i class="fas fa-user mr-2"></i> Sobre
                    </a>
                    <a href="https://wa.me/5532988178494" target="_blank"
                        class="mx-4 mt-2 bg-gradient-to-r from-secondary to-orange-600 text-white font-semibold text-sm py-2.5 px-5 rounded-full transition-all transform hover:scale-105 shadow-md flex items-center justify-center gap-2">
                        <i class="fab fa-whatsapp"></i> Agendar Consulta
                    </a>
                </nav>'''

NEW_MOB_NAV = '''                <nav class="flex flex-col gap-1.5 pt-3">
                    <a href="index.html" class="px-4 py-2.5 hover:bg-blue-50 rounded-lg transition-colors text-primary hover:text-secondary font-medium text-sm">
                        <i class="fas fa-user mr-2"></i> Sobre
                    </a>
                    <a href="../atendimento-online/" class="px-4 py-2.5 hover:bg-blue-50 rounded-lg transition-colors text-primary hover:text-secondary font-medium text-sm">
                        <i class="fas fa-laptop-house mr-2"></i> Terapia Presencial e Online
                    </a>
                    <div class="px-4 py-2.5 border-t border-gray-100 mt-1">
                        <p class="text-xs font-bold text-gray-400 uppercase tracking-widest mb-2">Contato</p>
                        <a href="tel:+5532988178494" class="flex items-center gap-3 py-1.5 text-primary hover:text-secondary font-medium text-sm">
                            <i class="fas fa-phone text-xs"></i> (32) 98817-8494
                        </a>
                        <a href="https://www.instagram.com/gustavoramehpsi/" target="_blank" class="flex items-center gap-3 py-1.5 text-primary hover:text-secondary font-medium text-sm">
                            <i class="fab fa-instagram"></i> @gustavoramehpsi
                        </a>
                        <a href="https://wa.me/5532988178494" target="_blank" class="flex items-center gap-3 py-1.5 text-primary hover:text-secondary font-medium text-sm">
                            <i class="fab fa-whatsapp text-green-500"></i> WhatsApp
                        </a>
                    </div>
                    <a href="https://wa.me/5532988178494" target="_blank"
                        class="mx-4 mt-2 bg-gradient-to-r from-secondary to-orange-600 text-white font-semibold text-sm py-2.5 px-5 rounded-full transition-all transform hover:scale-105 shadow-md flex items-center justify-center gap-2">
                        <i class="fab fa-whatsapp"></i> Agendar Consulta
                    </a>
                </nav>'''

if OLD_MOB_NAV in c:
    c = c.replace(OLD_MOB_NAV, NEW_MOB_NAV, 1)
    changes.append("Mobile nav updated")
else:
    changes.append("FAIL: Mobile nav not found")

# ============================================================
# 4. TCC DESCRIPTION PARAGRAPH
# ============================================================
OLD_TCC = '            \u00c9 uma abordagem mais espec\u00edfica, breve e focada no problema atual do paciente. Ela explica que o que nos afeta n\u00e3o s\u00e3o os acontecimentos em si, mas a forma com que os <strong>interpretamos</strong>.'
NEW_TCC = '            A TCC \u00e9 uma abordagem pr\u00e1tica, estruturada e voltada para a resolu\u00e7\u00e3o dos seus desafios atuais. O objetivo \u00e9 identificar e transformar os padr\u00f5es mentais que geram sofrimento, permitindo que voc\u00ea recupere o bem-estar e o protagonismo sobre sua pr\u00f3pria vida.'

if OLD_TCC in c:
    c = c.replace(OLD_TCC, NEW_TCC, 1)
    changes.append("TCC description updated")
else:
    # Try without leading spaces
    ALT_TCC = '\u00c9 uma abordagem mais espec\u00edfica, breve e focada no problema atual do paciente.'
    if ALT_TCC in c:
        # Find the full paragraph
        idx = c.index(ALT_TCC)
        p_start = c.rfind('<p', 0, idx)
        p_end = c.index('</p>', idx) + 4
        old_p = c[p_start:p_end]
        new_p = '<p class="text-blue-100 text-lg leading-relaxed mb-6">\n            A TCC \u00e9 uma abordagem pr\u00e1tica, estruturada e voltada para a resolu\u00e7\u00e3o dos seus desafios atuais. O objetivo \u00e9 identificar e transformar os padr\u00f5es mentais que geram sofrimento, permitindo que voc\u00ea recupere o bem-estar e o protagonismo sobre sua pr\u00f3pria vida.\n        </p>'
        c = c.replace(old_p, new_p, 1)
        changes.append("TCC description updated (alt match)")
    else:
        changes.append("FAIL: TCC description not found")

# ============================================================
# 5. BLOCKQUOTE
# ============================================================
OLD_BQ = '"O que nos afeta n\u00e3o s\u00e3o os ACONTECIMENTOS e sim a formas com que os INTERPRETAMOS."'
NEW_BQ = '"O peso de um acontecimento raramente est\u00e1 no fato em si, mas na lente que sua mente escolhe para observ\u00e1-lo."'
if OLD_BQ in c:
    c = c.replace(OLD_BQ, NEW_BQ, 1)
    changes.append("Blockquote updated")
else:
    changes.append("FAIL: Blockquote not found")

# ============================================================
# 6. ROLE TEXT
# ============================================================
OLD_ROLE = '<strong>Meu papel:</strong> Ajudar voc\u00ea a identificar e intervir nesses pensamentos para mudar padr\u00f5es nocivos.'
NEW_ROLE = '<strong>Meu papel:</strong> Ajudar voc\u00ea a identificar distor\u00e7\u00f5es no seu pensamento para que possamos, juntos, desconstruir padr\u00f5es de sofrimento e estruturar uma mentalidade mais saud\u00e1vel e funcional.'
if OLD_ROLE in c:
    c = c.replace(OLD_ROLE, NEW_ROLE, 1)
    changes.append("Role text updated")
else:
    changes.append("FAIL: Role text not found")

# ============================================================
# WRITE
# ============================================================
open(f, 'w', encoding='utf-8').write(c)
print("DONE. Final length:", len(c))
for ch in changes:
    print(" -", ch)
