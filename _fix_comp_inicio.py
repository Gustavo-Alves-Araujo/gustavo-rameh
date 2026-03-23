import os, re

path = r'c:\Users\crist\Desktop\projeto-rameh\gustavo-rameh\js\components.js'
with open(path, encoding='utf-8') as f:
    txt = f.read()

# Desktop: add Início before Sobre
OLD_D = (
    r'<ul class=\"hidden lg:flex items-center gap-1\">\n            <li>\n'
    r'              <a href=\"\' + base + \'sobre/\" class=\"nav-link'
)
NEW_D = (
    r'<ul class=\"hidden lg:flex items-center gap-1\">\n            <li>\n'
    r'              <a href=\"\' + (base || \'/\') + \'\" class=\"nav-link relative group px-5 py-2.5 text-sm font-medium text-slate-600 transition-all duration-300 rounded-full hover:bg-slate-50\" style=\"font-family:\'Inter\',sans-serif;\">\n'
    r'                <span class=\"relative z-10\">Início</span>\n'
    r'                <span class=\"absolute bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full bg-blue-500 opacity-0 transition-all duration-300 group-hover:opacity-100 group-hover:scale-125\"></span>\n'
    r'              </a>\n'
    r'            </li>\n'
    r'            <li>\n'
    r'              <a href=\"\' + base + \'sobre/\" class=\"nav-link'
)

# Mobile: add Início before Sobre
OLD_M = (
    r'<ul class=\"flex flex-col gap-1\">\n              <li>\n'
    r'                <a href=\"\' + base + \'sobre/\"\n'
    r'                   class=\"flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]\"\n'
    r'                   style=\"font-family:\'Inter\',sans-serif;\">\n'
    r'                  Sobre <i class=\"fas fa-chevron-right text-xs opacity-30\"></i>'
)
NEW_M = (
    r'<ul class=\"flex flex-col gap-1\">\n              <li>\n'
    r'                <a href=\"\' + (base || \'/\') + \'\"\n'
    r'                   class=\"flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]\"\n'
    r'                   style=\"font-family:\'Inter\',sans-serif;\">\n'
    r'                  Início <i class=\"fas fa-chevron-right text-xs opacity-30\"></i>\n'
    r'                </a>\n'
    r'              </li>\n'
    r'              <li>\n'
    r'                <a href=\"\' + base + \'sobre/\"\n'
    r'                   class=\"flex items-center justify-between p-4 rounded-2xl text-base font-semibold text-slate-700 transition-all hover:bg-slate-50 hover:pl-6 active:scale-[0.98]\"\n'
    r'                   style=\"font-family:\'Inter\',sans-serif;\">\n'
    r'                  Sobre <i class=\"fas fa-chevron-right text-xs opacity-30\"></i>'
)

d = txt.count(OLD_D)
m = txt.count(OLD_M)
print(f'desktop matches: {d}, mobile matches: {m}')

if d == 1:
    txt = txt.replace(OLD_D, NEW_D, 1)
if m == 1:
    txt = txt.replace(OLD_M, NEW_M, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(txt)
print('Done')
