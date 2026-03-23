import re

f = r'c:/Users/crist/Desktop/projeto-rameh/gustavo-rameh/index.html'
c = open(f, encoding='utf-8').read()
original_len = len(c)

changes = []

# ============================================================
# 1. UPDATE DESKTOP NAV
# ============================================================
old_desk = """<ul class="hidden lg:flex items-center gap-1">
                            
                <li>
                    <a href="#sobre" class="relative group px-5 py-2.5 text-sm font-medium transition-all duration-300 rounded-full hover:bg-slate-50" style="color: #475569; font-family: 'Inter', sans-serif;">
                        <span class="relative z-10">Sobre</span>
                        <span class="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125" style="background-color: #3b82f6; box-shadow: 0 0 8px #3b82f6;"></span>
                    </a>
                </li>
                <li>
                    <a href="#servicos" class="relative group px-5 py-2.5 text-sm font-medium transition-all duration-300 rounded-full hover:bg-slate-50" style="color: #475569; font-family: 'Inter', sans-serif;">
                        <span class="relative z-10">Serviços</span>
                        <span class="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125" style="background-color: #3b82f6; box-shadow: 0 0 8px #3b82f6;"></span>
                    </a>
                </li>
                <li>
                    <a href="#component-emagrecimento" class="relative group px-5 py-2.5 text-sm font-medium transition-all duration-300 rounded-full hover:bg-slate-50" style="color: #475569; font-family: 'Inter', sans-serif;">
                        <span class="relative z-10">Emagrecimento</span>
                        <span class="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125" style="background-color: #3b82f6; box-shadow: 0 0 8px #3b82f6;"></span>
                    </a>
                </li>
                <li>
                    <a href="#component-modalidades" class="relative group px-5 py-2.5 text-sm font-medium transition-all duration-300 rounded-full hover:bg-slate-50" style="color: #475569; font-family: 'Inter', sans-serif;">
                        <span class="relative z-10">Modalidades</span>
                        <span class="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125" style="background-color: #3b82f6; box-shadow: 0 0 8px #3b82f6;"></span>
                    </a>
                </li>
                <li>
                    <a href="#achievements" class="relative group px-5 py-2.5 text-sm font-medium transition-all duration-300 rounded-full hover:bg-slate-50" style="color: #475569; font-family: 'Inter', sans-serif;">
                        <span class="relative z-10">Experiência</span>
                        <span class="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125" style="background-color: #3b82f6; box-shadow: 0 0 8px #3b82f6;"></span>
                    </a>
                </li>
                <li>
                    <a href="#faq" class="relative group px-5 py-2.5 text-sm font-medium transition-all duration-300 rounded-full hover:bg-slate-50" style="color: #475569; font-family: 'Inter', sans-serif;">
                        <span class="relative z-10">FAQ</span>
                        <span class="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125" style="background-color: #3b82f6; box-shadow: 0 0 8px #3b82f6;"></span>
                    </a>
                </li>
            
                        </ul>"""

new_desk = """<ul class="hidden lg:flex items-center gap-1">
                            
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
            
                        </ul>"""

if old_desk in c:
    c = c.replace(old_desk, new_desk, 1)
    changes.append("Desktop nav updated")
else:
    changes.append("FAIL: Desktop nav not found")

# ============================================================
# 2. UPDATE MOBILE NAV
# ============================================================
old_mob = """<ul class="flex flex-col gap-2">
                                    <li>
                                        <a href="#sobre" class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]" style="font-family: 'Inter', sans-serif;">
                                            Sobre
                                            <i class="fas fa-chevron-right text-xs opacity-30"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#servicos" class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]" style="font-family: 'Inter', sans-serif;">
                                            Serviços
                                            <i class="fas fa-chevron-right text-xs opacity-30"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#component-emagrecimento" class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]" style="font-family: 'Inter', sans-serif;">
                                            Emagrecimento
                                            <i class="fas fa-chevron-right text-xs opacity-30"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#component-modalidades" class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]" style="font-family: 'Inter', sans-serif;">
                                            Modalidades
                                            <i class="fas fa-chevron-right text-xs opacity-30"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#achievements" class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]" style="font-family: 'Inter', sans-serif;">
                                            Experiência
                                            <i class="fas fa-chevron-right text-xs opacity-30"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#faq" class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]" style="font-family: 'Inter', sans-serif;">
                                            FAQ
                                            <i class="fas fa-chevron-right text-xs opacity-30"></i>
                                        </a>
                                    </li>
                            </ul>"""

new_mob = """<ul class="flex flex-col gap-2">
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
                            </ul>"""

if old_mob in c:
    c = c.replace(old_mob, new_mob, 1)
    changes.append("Mobile nav updated")
else:
    changes.append("FAIL: Mobile nav not found")

# ============================================================
# 3. HERO TAGLINE
# ============================================================
old_tagline = "Te ajudo a superar os desafios e conquistar seus objetivos utilizando a psicologia e a metodologia Coaching a seu favor."
new_tagline = "Utilizo a Terapia Cognitivo-Comportamental para promover um atendimento humanizado e personalizado, auxiliando você a superar desafios emocionais e conquistar uma vida mais saudável."

if old_tagline in c:
    c = c.replace(old_tagline, new_tagline, 1)
    changes.append("Hero tagline updated")
else:
    changes.append("FAIL: Hero tagline not found")

# ============================================================
# 4. UPDATE ABOUT SECTION TEXT (in component-about-image-features-clinical-2)
# ============================================================
old_about_text = """                    <div class="about-text">
                        <span class="section-tag">Sobre o Psicólogo</span>
                        <h2>Sou Gustavo Rameh</h2>
                        <p>Psicólogo com mais de uma década de atuação clínica dedicada ao equilíbrio emocional de adultos e adolescentes. Minha prática é pautada na ética e no desenvolvimento de estratégias saudáveis para lidar com os desafios do cotidiano. <p></p> Ofereço atendimento flexível — presencial ou online — garantindo que o cuidado com a sua saúde mental seja humanizado, prático e de alta qualidade, onde quer que você esteja.</p>
                            <ul class="about-list">
                                
                <li><i class="fas fa-brain"></i> Especialista em Terapia Cognitivo-Comportamental</li>
            
                <li><i class="fas fa-star"></i> Pós-graduado em Psicologia Positiva e Coaching</li>
            
                <li><i class="fas fa-hospital"></i> Pós graduação em Psicologia Hospitalar</li>
            
                <li><i class="fas fa-users"></i> Capacitação em Psicologia de Grupos</li>
            
                            </ul>
                        
                        <div style="margin-top: 2rem;">
                            <a href="https://wa.me/5532988178494" style="display: inline-flex; align-items: center; gap: 10px; background-color: #3b82f6; color: white; padding: 14px 32px; border-radius: 50px; font-weight: 700; font-size: 0.9rem; text-decoration: none; transition: all 0.3s ease;">
                                <i class="fab fa-whatsapp"></i>
                                Entre em Contato
                            </a>
                        </div>
                    </div>"""

new_about_text = """                    <div class="about-text">
                        <span class="section-tag">Sobre o Psicólogo</span>
                        <h2>Olá! Muito prazer.</h2>
                        <h3 style="font-size:1.1rem; font-weight:600; color:#1e3a8a; margin-bottom:1rem;">Sou Gustavo Rameh, Psicólogo Clínico (CRP 04/43395)</h3>
                        <p>A vida sempre nos traz alguns problemas e, muitos deles, conseguimos resolver sozinhos. Já outros, precisamos de ajuda. Às vezes, quando passamos por problemas mais delicados, a parte mais difícil desse processo é chegar à conclusão que, nesse momento, a ajuda de um profissional será importante.</p>
                        <p style="margin-top:1rem;">Muitas vezes surgem pensamentos como: <em>"Será que meu problema é grave o suficiente?"</em> ou <em>"Como conversar com alguém pode me ajudar?"</em>.</p>
                        <p style="margin-top:1rem; font-style:italic; background:#eff6ff; padding:1rem; border-left:4px solid #3b82f6; border-radius:4px;">Gostaria de esclarecer que não existe problema pequeno ou grande. O que existe é a sua dor, a sua angústia e a sua ansiedade. Se estiver incomodando, merece toda a atenção.</p>
                            <ul class="about-list" style="margin-top:1.5rem;">
                <li><i class="fas fa-brain"></i> Especialista em Terapia Cognitivo-Comportamental</li>
                <li><i class="fas fa-star"></i> Pós-graduado em Psicologia Positiva e Coaching</li>
                <li><i class="fas fa-hospital"></i> Pós graduação em Psicologia Hospitalar</li>
                <li><i class="fas fa-users"></i> Capacitação em Psicologia de Grupos</li>
                            </ul>
                        
                        <div style="margin-top: 2rem;">
                            <a href="https://wa.me/5532988178494" style="display: inline-flex; align-items: center; gap: 10px; background-color: #3b82f6; color: white; padding: 14px 32px; border-radius: 50px; font-weight: 700; font-size: 0.9rem; text-decoration: none; transition: all 0.3s ease;">
                                <i class="fab fa-whatsapp"></i>
                                Entre em Contato
                            </a>
                        </div>
                    </div>"""

if old_about_text in c:
    c = c.replace(old_about_text, new_about_text, 1)
    changes.append("About section text updated")
else:
    changes.append("FAIL: About text not found")

# ============================================================
# 5. MOVE MODALIDADES SECTION after about section
#    a) Extract modalidades block
#    b) Remove from original position
#    c) Insert after about section
# ============================================================
# The about section ends with: </section>\n        </div><div id="component-help-transform-life">
about_end_marker = '\n            </section>\n        </div><div id="component-help-transform-life">'

# Modalidades section: starts with the comment line and ends just before achievements
# We need to find exact bounds
mod_comment = '\n\n        <!-- Seção Modalidades de Atendimento -->\n        <div id="component-modalidades">'
mod_end = '\n        </div>\n\n        <div id="component-achievements-numbers-grid-4">'

if mod_comment in c and mod_end in c:
    mod_start_idx = c.index(mod_comment)
    mod_end_search_from = c.index(mod_end, mod_start_idx)
    mod_end_idx = mod_end_search_from + len('\n        </div>')
    modal_block = c[mod_start_idx:mod_end_idx]
    
    # Remove from original position (replace with empty)
    c = c[:mod_start_idx] + c[mod_end_idx:]
    
    # Now insert after about section
    if about_end_marker in c:
        insert_pos = c.index(about_end_marker)
        c = c[:insert_pos] + modal_block + c[insert_pos:]
        changes.append("Modalidades moved after about section")
    else:
        changes.append("FAIL: About end marker not found for insert")
else:
    changes.append(f"FAIL: Modalidades bounds not found. mod_comment={mod_comment in c}, mod_end={mod_end in c}")

# ============================================================
# 6. REMOVE ENTIRE COACHING SECTION
# ============================================================
coaching_start = '\n\n        <!-- Seção Coaching -->\n        <div id="component-coaching">'
coaching_end = '\n        </div>\n\n        <!-- Seção Emagrecimento -->'

if coaching_start in c and coaching_end in c:
    cs_idx = c.index(coaching_start)
    ce_idx = c.index(coaching_end, cs_idx)
    ce_end_idx = ce_idx + len('\n        </div>')
    c = c[:cs_idx] + '\n\n        <!-- Seção Emagrecimento -->' + c[ce_end_idx + len('\n\n        <!-- Seção Emagrecimento -->'):]
    changes.append("Coaching section removed")
else:
    changes.append(f"FAIL: Coaching section not found. start={coaching_start in c}, end={coaching_end in c}")

# ============================================================
# 7. SERVICE CARD: "Terapia Online & Coaching" -> "Terapia Presencial e Online"
#    and update the link from #component-coaching to atendimento-online/
# ============================================================
old_card = """                <h3 class="mb-3 text-xl font-bold tracking-tight text-slate-900 group-hover:text-black transition-colors">
                    Terapia Online & Coaching
                </h3>

                <p class="mb-8 text-sm font-medium leading-relaxed text-slate-500 flex-grow">
                    Processo que visa elevar a performance do indivíduo, realizado do conforto do seu ambiente.
                </p>

                <div class="mt-auto flex flex-col gap-2">
                    <a href="#component-coaching" class="inline-flex items-center justify-center gap-2 w-full py-3 rounded-full font-bold text-xs transition-all duration-300 hover:bg-slate-100 border border-slate-200" style="color: #3b82f6;">
                        <i class="fas fa-arrow-down text-xs"></i>
                        Saiba Mais
                    </a>"""
new_card = """                <h3 class="mb-3 text-xl font-bold tracking-tight text-slate-900 group-hover:text-black transition-colors">
                    Terapia Presencial e Online
                </h3>

                <p class="mb-8 text-sm font-medium leading-relaxed text-slate-500 flex-grow">
                    Atendimento presencial em consultório ou online por videochamada, com total flexibilidade para você.
                </p>

                <div class="mt-auto flex flex-col gap-2">
                    <a href="atendimento-online/" class="inline-flex items-center justify-center gap-2 w-full py-3 rounded-full font-bold text-xs transition-all duration-300 hover:bg-slate-100 border border-slate-200" style="color: #3b82f6;">
                        <i class="fas fa-arrow-right text-xs"></i>
                        Saiba Mais
                    </a>"""

if old_card in c:
    c = c.replace(old_card, new_card, 1)
    changes.append("Service card updated")
else:
    changes.append("FAIL: Service card not found")

# ============================================================
# 8. EMAGRECIMENTO: Remove "e Coaching" references
# ============================================================
c = c.replace("Emagrecimento sustentável com Psicoterapia Cognitivo-Comportamental e Coaching.", 
              "Emagrecimento sustentável com Psicoterapia Cognitivo-Comportamental.", 1)
changes.append("Emagrecimento coaching ref removed")

# Also rename "O Papel do Coaching" card in emagrecimento
c = c.replace("""                            <h3 class="text-base font-bold text-slate-900">O Papel do Coaching</h3>
                                    <p class="text-xs text-slate-500">Focado na ação e no futuro.</p>""",
              """                            <h3 class="text-base font-bold text-slate-900">Estratégias e Metas</h3>
                                    <p class="text-xs text-slate-500">Focado na ação e no futuro.</p>""", 1)

# ============================================================
# 9. ADD PAYMENT SECTION after modalidades section
# ============================================================
payment_section = """

        <!-- Seção Formas de Pagamento -->
        <div id="component-pagamento">
            <section class="relative py-16 overflow-hidden bg-white">
                <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                    <div class="text-center mb-10">
                        <span class="inline-block py-1 px-3 rounded-full text-[10px] font-black uppercase tracking-[0.2em] mb-4" style="background-color: rgba(59,130,246,0.1); color: #3b82f6;">Pagamento</span>
                        <h2 class="text-2xl md:text-3xl font-black text-slate-900 mb-3 tracking-tight">Formas de Pagamento</h2>
                        <p class="text-base text-slate-500">Facilidade e praticidade para você cuidar da sua saúde mental.</p>
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-2xl mx-auto">
                        <!-- PIX -->
                        <div class="flex flex-col items-center bg-slate-50 border border-slate-100 rounded-[1.5rem] p-8 transition-all duration-300 hover:shadow-lg hover:-translate-y-1">
                            <div class="mb-4 inline-flex h-16 w-16 items-center justify-center rounded-2xl" style="background-color: rgba(59,130,246,0.1);">
                                <svg viewBox="0 0 512 512" class="w-8 h-8" fill="#3b82f6" xmlns="http://www.w3.org/2000/svg"><path d="M242.4 292.5C247.8 287.1 247.8 278.2 242.4 272.7L115.8 146.1c-18.58-18.59-48.85-18.59-67.43 0L1.037 193.4C-3.305 197.8-3.305 204.8 1.037 209.2L133.4 341.5c.6836.6836 1.426 1.23 2.195 1.664L242.4 292.5zM269.6 219.5L162.8 112.6c-.6836-.6836-1.426-1.23-2.195-1.664L53.78 161.6L269.6 377.4l106.8-106.9c.6836-.6836 1.23-1.426 1.664-2.195L269.6 219.5zM510.9 302.6L378.6 170.3c-.6836-.6836-1.426-1.23-2.195-1.664L269.6 219.5l122.3 122.3c18.58 18.59 48.85 18.59 67.43 0L510.9 341.2C515.3 336.8 515.3 307.1 510.9 302.6zM242.4 219.5L348.1 113.8c.6836-.6836 1.426-1.23 2.195-1.664L458.2 163L242.4 378.8L135.7 272.1c-.6836-.6836-1.23-1.426-1.664-2.195L242.4 219.5z"/></svg>
                            </div>
                            <h3 class="text-lg font-bold text-slate-900 mb-1">PIX</h3>
                            <p class="text-sm text-slate-500 text-center">Transferência instantânea, rápida e sem taxas.</p>
                        </div>
                        <!-- Cartão de Crédito -->
                        <div class="flex flex-col items-center bg-slate-50 border border-slate-100 rounded-[1.5rem] p-8 transition-all duration-300 hover:shadow-lg hover:-translate-y-1">
                            <div class="mb-4 inline-flex h-16 w-16 items-center justify-center rounded-2xl" style="background-color: rgba(59,130,246,0.1);">
                                <i class="fas fa-credit-card text-3xl" style="color: #3b82f6;"></i>
                            </div>
                            <h3 class="text-lg font-bold text-slate-900 mb-1">Cartão de Crédito</h3>
                            <p class="text-sm text-slate-500 text-center">Parcele suas sessões com facilidade e segurança.</p>
                        </div>
                    </div>
                </div>
            </section>
        </div>
"""

# Insert after the modalidades section (which is now after the about section)
# Find the about section end to position correctly
# Actually, insert after the modalidades section wherever it now is
# The modalidades section now comes right after about section
mod_div_end = '</div>\n\n        <div id="component-help-transform-life">'
if mod_div_end in c:
    c = c.replace(mod_div_end, '</div>' + payment_section + '\n        <div id="component-help-transform-life">', 1)
    changes.append("Payment section added")
else:
    changes.append("FAIL: Payment section insert point not found")

# ============================================================
# WRITE FILE
# ============================================================
open(f, 'w', encoding='utf-8').write(c)
print("DONE. Final length:", len(c))
for ch in changes:
    print(" -", ch)
