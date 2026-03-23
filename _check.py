c = open('index.html', encoding='utf-8').read()
cs = open('sobre/index.html', encoding='utf-8').read()

checks = [
    ('Coaching section removed', 'id="component-coaching"' not in c),
    ('Hero tagline updated', 'Terapia Cognitivo-Comportamental para promover' in c),
    ('About bio updated', 'Muito prazer.' in c),
    ('Modalidades before help-transform', c.index('component-modalidades') < c.index('component-help-transform-life')),
    ('Payment section present', 'component-pagamento' in c),
    ('No Coaching  & old title', 'Terapia Online & Coaching' not in c),
    ('Emagrecimento updated', 'e Coaching.' not in c),
    ('Estrategias e Metas', 'Estrat\u00e9gias e Metas' in c),
    ('Phone in nav', '98817-8494' in c),
    ('Sobre nav link', 'href="sobre/"' in c),
    ('Atendimento link', 'href="atendimento-online/"' in c),
    ('[SOBRE] Desktop nav updated', 'Terapia Presencial e Online' in cs),
    ('[SOBRE] TCC updated', 'A TCC \u00e9 uma abordagem pr\u00e1tica' in cs),
    ('[SOBRE] Blockquote updated', 'raramente est\u00e1 no fato em si' in cs),
    ('[SOBRE] Role text updated', 'identificar distor\u00e7\u00f5es' in cs),
    ('[SOBRE] No coaching nav', 'Coaching Individual' not in cs),
]

for name, ok in checks:
    print(('  [OK] ' if ok else '  [FAIL] ') + name)
