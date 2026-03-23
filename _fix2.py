f = r'c:/Users/crist/Desktop/projeto-rameh/gustavo-rameh/index.html'
c = open(f, encoding='utf-8').read()

changes = []

# ============================================================
# 1. DESKTOP NAV
# ============================================================
old_desk = '<a href="#sobre" class="relative group px-5 py-2.5 text-sm font-medium transition-all duration-300 rounded-full hover:bg-slate-50" style="color: #475569; font-family: \'Inter\', sans-serif;">\n                        <span class="relative z-10">Sobre</span>'
new_desk1_check = '#sobre' in c and '#servicos' in c and '#faq' in c
changes.append(f"Desktop nav check: {new_desk1_check}")

# Use broad replace on the whole desktop ul block
import re

# Desktop nav replacement
desk_pattern = r'(<ul class="hidden lg:flex items-center gap-1">)(.*?)(</ul>)'
desk_match = re.search(desk_pattern, c, re.DOTALL)
if desk_match:
    old_ul = desk_match.group(0)
    new_ul = '''<ul class="hidden lg:flex items-center gap-1">
                            
                <li>
                    <a href="sobre/" class="relative group px-5 py-2.5 text-sm font-medium transition-all duration-300 rounded-full hover:bg-slate-50" style="color: #475569; font-family: 'Inter', sans-serif;">
                        <span class="relative z-10">Sobre</span>
                        <span class="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125" style="background-color: #3b82f6; box-shadow: 0 0 8px #3b82f6;"></span>
                    </a>
                </li>
                <li>
                    <a href="atendimento-online/" class="relative group px-5 py-2.5 text-sm font-medium transition-all duration-300 rounded-full hover:bg-slate-50" style="color: #475569; font-family: 'Inter', sans-serif;">
                        <span class="relative z-10">Terapia Presencial e Online</span>
                        <span class="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125" style="background-color: #3b82f6; box-shadow: 0 0 8px #3b82f6;"></span>
                    </a>
                </li>
                <li class="flex items-center gap-1">
                    <a href="tel:+5532988178494" class="flex items-center gap-1.5 px-3 py-2 text-xs font-semibold rounded-full hover:bg-slate-50 transition-colors" style="color: #475569; font-family: 'Inter', sans-serif;" title="(32) 98817-8494">
                        <i class="fas fa-phone text-xs" style="color: #3b82f6;"></i>
                        <span>(32) 98817-8494</span>
                    </a>
                    <a href="https://www.instagram.com/gustavoramehpsi/" target="_blank" class="w-8 h-8 flex items-center justify-center rounded-full hover:bg-slate-100 transition-colors" style="color: #475569;" title="Instagram">
                        <i class="fab fa-instagram text-sm"></i>
                    </a>
                    <a href="https://wa.me/5532988178494" target="_blank" class="w-8 h-8 flex items-center justify-center rounded-full hover:bg-slate-100 transition-colors" style="color: #475569;" title="WhatsApp">
                        <i class="fab fa-whatsapp text-sm"></i>
                    </a>
                </li>
            
                        </ul>'''
    c = c.replace(old_ul, new_ul, 1)
    changes.append("Desktop nav updated")
else:
    changes.append("FAIL: Desktop nav not found")

# ============================================================
# 2. MOBILE NAV - replace using regex
# ============================================================
mob_pattern = r'(<ul class="flex flex-col gap-2">)(.*?)(</ul>)'
mob_match = re.search(mob_pattern, c, re.DOTALL)
if mob_match:
    old_mob_ul = mob_match.group(0)
    new_mob_ul = '''<ul class="flex flex-col gap-2">
                                    <li>
                                        <a href="sobre/" class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]" style="font-family: 'Inter', sans-serif;">
                                            Sobre
                                            <i class="fas fa-chevron-right text-xs opacity-30"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="atendimento-online/" class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]" style="font-family: 'Inter', sans-serif;">
                                            Terapia Presencial e Online
                                            <i class="fas fa-chevron-right text-xs opacity-30"></i>
                                        </a>
                                    </li>
                                    <li class="px-4 py-3">
                                        <div class="text-xs font-bold text-slate-400 uppercase tracking-widest mb-3">Contato</div>
                                        <div class="flex flex-col gap-2.5">
                                            <a href="tel:+5532988178494" class="flex items-center gap-3 text-slate-700 hover:text-blue-500 transition-colors font-medium text-sm">
                                                <i class="fas fa-phone w-5 text-center" style="color: #3b82f6;"></i> (32) 98817-8494
                                            </a>
                                            <a href="https://www.instagram.com/gustavoramehpsi/" target="_blank" class="flex items-center gap-3 text-slate-700 hover:text-blue-500 transition-colors font-medium text-sm">
                                                <i class="fab fa-instagram w-5 text-center" style="color: #3b82f6;"></i> @gustavoramehpsi
                                            </a>
                                            <a href="https://wa.me/5532988178494" target="_blank" class="flex items-center gap-3 text-slate-700 hover:text-green-500 transition-colors font-medium text-sm">
                                                <i class="fab fa-whatsapp w-5 text-center text-green-500"></i> WhatsApp
                                            </a>
                                        </div>
                                    </li>
                            </ul>'''
    c = c.replace(old_mob_ul, new_mob_ul, 1)
    changes.append("Mobile nav updated")
else:
    changes.append("FAIL: Mobile nav not found")

# ============================================================
# 3. HERO TAGLINE
# ============================================================
old_tag = "Te ajudo a superar os desafios e conquistar seus objetivos utilizando a psicologia e a metodologia Coaching a seu favor."
new_tag = "Utilizo a Terapia Cognitivo-Comportamental para promover um atendimento humanizado e personalizado, auxiliando voc\u00ea a superar desafios emocionais e conquistar uma vida mais saud\u00e1vel."
if old_tag in c:
    c = c.replace(old_tag, new_tag, 1)
    changes.append("Hero tagline updated")
else:
    changes.append("FAIL: Hero tagline not found -- checking: " + str(c[c.find('metodologia'):c.find('metodologia')+80] if 'metodologia' in c else 'not found'))

# ============================================================
# 4. ABOUT H2
# ============================================================
if '<h2>Sou Gustavo Rameh</h2>' in c:
    c = c.replace('<h2>Sou Gustavo Rameh</h2>', '<h2>Ol\u00e1! Muito prazer.</h2>\n                        <h3 style="font-size:1.1rem; font-weight:600; color:#1e3a8a; margin-bottom:1rem;">Sou Gustavo Rameh, Psic\u00f3logo Cl\u00ednico (CRP 04/43395)</h3>', 1)
    changes.append("About h2 updated")
else:
    changes.append("FAIL: About h2 not found")

# ABOUT PARAGRAPH - find anchor text
old_para_start = "Psic\u00f3logo com mais de uma d\u00e9cada de atua\u00e7\u00e3o cl\u00ednica"
old_para_end = "onde quer que voc\u00ea esteja.</p>"
if old_para_start in c and old_para_end in c:
    ps = c.index(old_para_start)
    # go back to find the <p> tag
    p_open = c.rfind('<p>', 0, ps)
    pe = c.index(old_para_end, ps) + len(old_para_end)
    new_para = """<p>A vida sempre nos traz alguns problemas e, muitos deles, conseguimos resolver sozinhos. J\u00e1 outros, precisamos de ajuda. \u00c0s vezes, quando passamos por problemas mais delicados, a parte mais dif\u00edcil desse processo \u00e9 chegar \u00e0 conclus\u00e3o que, nesse momento, a ajuda de um profissional ser\u00e1 importante.</p>
                        <p style="margin-top:1rem;">Muitas vezes surgem pensamentos como: <em>&ldquo;Ser\u00e1 que meu problema \u00e9 grave o suficiente?&rdquo;</em> ou <em>&ldquo;Como conversar com algu\u00e9m pode me ajudar?&rdquo;</em>.</p>
                        <p style="margin-top:1rem; font-style:italic; background:#eff6ff; padding:1rem; border-left:4px solid #3b82f6; border-radius:4px;">Gostaria de esclarecer que n\u00e3o existe problema pequeno ou grande. O que existe \u00e9 a sua dor, a sua ang\u00fastia e a sua ansiedade. Se estiver incomodando, merece toda a aten\u00e7\u00e3o.</p>"""
    c = c[:p_open] + new_para + c[pe:]
    changes.append("About paragraph updated")
else:
    changes.append("FAIL: About paragraph anchors not found")

# ============================================================
# 5. MOVE MODALIDADES AFTER ABOUT
# ============================================================
# About section wrapper ends: ...section>\n        </div><div id="component-help-transform-life">
# We need to insert modalidades between </div> and <div id="component-help-transform-life">

MOD_START = '\n\n        <!-- Se\u00e7\u00e3o Modalidades de Atendimento -->\n        <div id="component-modalidades">'
MOD_END_DIV = '\n        </div>\n\n        <div id="component-achievements-numbers-grid-4">'
ABOUT_END = '</div><div id="component-help-transform-life">'

if MOD_START in c and MOD_END_DIV in c and ABOUT_END in c:
    ms_idx = c.index(MOD_START)
    me_marker_idx = c.index(MOD_END_DIV, ms_idx)
    me_idx = me_marker_idx + len('\n        </div>')
    modal_block = c[ms_idx:me_idx]

    # Remove modalidades from current position
    c = c[:ms_idx] + c[me_idx:]

    # Insert after about section (before component-help-transform-life)
    about_end_idx = c.index(ABOUT_END)
    insert_point = about_end_idx + len('</div>')
    c = c[:insert_point] + modal_block + '\n\n        ' + c[insert_point:]
    changes.append("Modalidades moved after about section")
else:
    changes.append(f"FAIL Modalidades: MOD_START={'found' if MOD_START in c else 'MISSING'}, MOD_END={'found' if MOD_END_DIV in c else 'MISSING'}, ABOUT_END={'found' if ABOUT_END in c else 'MISSING'}")

# ============================================================
# 6. REMOVE COACHING SECTION
# ============================================================
COACH_START = '\n\n        <!-- Se\u00e7\u00e3o Coaching -->\n        <div id="component-coaching">'
COACH_END_MARKER = '\n        </div>\n\n        <!-- Se\u00e7\u00e3o Emagrecimento -->'

if COACH_START in c and COACH_END_MARKER in c:
    cs = c.index(COACH_START)
    ce_m = c.index(COACH_END_MARKER, cs)
    ce = ce_m + len('\n        </div>')
    remainder = c[ce:]
    # remainder starts with '\n\n        <!-- SeCão Emagrecimento -->'
    c = c[:cs] + remainder
    changes.append("Coaching section removed")
else:
    changes.append(f"FAIL Coaching: start={'found' if COACH_START in c else 'MISSING'}, end={'found' if COACH_END_MARKER in c else 'MISSING'}")

# ============================================================
# 7. SERVICE CARD
# ============================================================
found_card = False
for raw in ['Terapia Online & Coaching', 'Terapia Online &amp; Coaching']:
    if raw in c:
        c = c.replace(raw, 'Terapia Presencial e Online', 1)
        changes.append(f"Service card title updated: {raw!r}")
        found_card = True
        break
if not found_card:
    changes.append("FAIL: Service card title not found")

old_card_desc = "Processo que visa elevar a performance do indiv\u00edduo, realizado do conforto do seu ambiente."
if old_card_desc in c:
    c = c.replace(old_card_desc, "Atendimento presencial em consult\u00f3rio ou online por videochamada, com total flexibilidade para voc\u00ea.", 1)
    changes.append("Service card desc updated")

if 'href="#component-coaching"' in c:
    c = c.replace('href="#component-coaching"', 'href="atendimento-online/"', 1)
    changes.append("Service card link updated")
else:
    changes.append("FAIL: Service card link already changed or not found")

if '<i class="fas fa-arrow-down text-xs"></i>' in c:
    c = c.replace('<i class="fas fa-arrow-down text-xs"></i>', '<i class="fas fa-arrow-right text-xs"></i>', 1)

# ============================================================
# 8. EMAGRECIMENTO
# ============================================================
old_emag = "Emagrecimento sustent\u00e1vel com Psicoterapia Cognitivo-Comportamental e Coaching."
if old_emag in c:
    c = c.replace(old_emag, "Emagrecimento sustent\u00e1vel com Psicoterapia Cognitivo-Comportamental.", 1)
    changes.append("Emagrecimento subheading updated")
else:
    changes.append("FAIL: Emagrecimento subheading not found")

old_coaching_h = '>O Papel do Coaching<'
if old_coaching_h in c:
    c = c.replace(old_coaching_h, '>Estrat\u00e9gias e Metas<', 1)
    changes.append("Coaching card heading renamed")
else:
    changes.append("FAIL: O Papel do Coaching not found")

# ============================================================
# 9. PAYMENT SECTION - insert before component-help-transform-life
# ============================================================
HELP_MARKER = '<div id="component-help-transform-life">'
payment_html = '''
        <!-- Se\u00e7\u00e3o Formas de Pagamento -->
        <div id="component-pagamento">
            <section class="relative py-16 overflow-hidden bg-white">
                <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                    <div class="text-center mb-10">
                        <span class="inline-block py-1 px-3 rounded-full text-[10px] font-black uppercase tracking-[0.2em] mb-4" style="background-color: rgba(59,130,246,0.1); color: #3b82f6;">Pagamento</span>
                        <h2 class="text-2xl md:text-3xl font-black text-slate-900 mb-3 tracking-tight">Formas de Pagamento</h2>
                        <p class="text-base text-slate-500">Facilidade e praticidade para voc\u00ea cuidar da sua sa\u00fade mental.</p>
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-2xl mx-auto">
                        <div class="flex flex-col items-center bg-slate-50 border border-slate-100 rounded-[1.5rem] p-8 transition-all duration-300 hover:shadow-lg hover:-translate-y-1">
                            <div class="mb-4 inline-flex h-16 w-16 items-center justify-center rounded-2xl" style="background-color: rgba(59,130,246,0.1);">
                                <i class="fas fa-qrcode text-3xl" style="color: #3b82f6;"></i>
                            </div>
                            <h3 class="text-lg font-bold text-slate-900 mb-1">PIX</h3>
                            <p class="text-sm text-slate-500 text-center">Transfer\u00eancia instant\u00e2nea, r\u00e1pida e sem taxas.</p>
                        </div>
                        <div class="flex flex-col items-center bg-slate-50 border border-slate-100 rounded-[1.5rem] p-8 transition-all duration-300 hover:shadow-lg hover:-translate-y-1">
                            <div class="mb-4 inline-flex h-16 w-16 items-center justify-center rounded-2xl" style="background-color: rgba(59,130,246,0.1);">
                                <i class="fas fa-credit-card text-3xl" style="color: #3b82f6;"></i>
                            </div>
                            <h3 class="text-lg font-bold text-slate-900 mb-1">Cart\u00e3o de Cr\u00e9dito</h3>
                            <p class="text-sm text-slate-500 text-center">Parcele suas sess\u00f5es com facilidade e seguran\u00e7a.</p>
                        </div>
                    </div>
                </div>
            </section>
        </div>

        '''

if HELP_MARKER in c:
    idx = c.index(HELP_MARKER)
    c = c[:idx] + payment_html + c[idx:]
    changes.append("Payment section inserted")
else:
    changes.append("FAIL: help-transform marker not found")

# ============================================================
# WRITE
# ============================================================
open(f, 'w', encoding='utf-8').write(c)
print("DONE. Final length:", len(c))
for ch in changes:
    print(" -", ch)
