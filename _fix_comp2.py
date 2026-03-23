with open('js/components.js', encoding='utf-8') as f:
    txt = f.read()

# Desktop nav - add Inicio before Sobre
OLD_D = 'hidden lg:flex items-center gap-1">\\n            <li>\\n              <a href="\' + base + \'sobre/"'
NEW_D = ('hidden lg:flex items-center gap-1">\\n            <li>\\n'
         '              <a href="\' + (base || \'/\') + \'" class="nav-link relative group px-5 py-2.5 text-sm font-medium text-slate-600 transition-all duration-300 rounded-full hover:bg-slate-50" style="font-family:\'Inter\',sans-serif;">\\n'
         '                <span class="relative z-10">In\\u00edcio</span>\\n'
         '                <span class="absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full bg-blue-500 opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125"></span>\\n'
         '              </a>\\n'
         '            </li>\\n'
         '            <li>\\n'
         '              <a href="\' + base + \'sobre/"')

# Mobile menu - add Inicio before Sobre
OLD_M = '<ul class="flex flex-col gap-1">\\n              <li>\\n                <a href="\' + base + \'sobre/"'
NEW_M = ('<ul class="flex flex-col gap-1">\\n'
         '              <li>\\n'
         '                <a href="\' + (base || \'/\') + \'"\\n'
         '                   class="flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]"\\n'
         '                   style="font-family:\'Inter\',sans-serif;">\\n'
         '                  In\\u00edcio <i class="fas fa-chevron-right text-xs opacity-30"></i>\\n'
         '                </a>\\n'
         '              </li>\\n'
         '              <li>\\n'
         '                <a href="\' + base + \'sobre/"')

d = txt.count(OLD_D)
m = txt.count(OLD_M)
print(f'desktop={d} mobile={m}')

txt = txt.replace(OLD_D, NEW_D, 1)
txt = txt.replace(OLD_M, NEW_M, 1)

with open('js/components.js', 'w', encoding='utf-8') as f:
    f.write(txt)
print('Done')
