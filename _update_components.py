#!/usr/bin/env python3
"""
Replaces inline header/footer/hamburger in all pages with shared components.
- Removes <style id="hamburger-styles"> block
- Replaces <div id="headerWrapper">...</div> with <div id="site-header"></div>
- Replaces <footer class="bg-slate-900...">...</footer> (or its wrapper div for index.html)
  with <div id="site-footer"></div>
- Removes inline hamburger JS <script> block
- Adds <script src="{base}js/components.js"></script> before </body>
"""
import re
import os

BASE_DIR = r'c:\Users\crist\Desktop\projeto-rameh\gustavo-rameh'

PAGES = [
    ('index.html', ''),
    ('sobre/index.html', '../'),
    ('atendimento-online/index.html', '../'),
    ('individual/index.html', '../'),
    ('casal/index.html', '../'),
    ('grupo/index.html', '../'),
    ('coaching/index.html', '../'),
    ('emagrecimento/index.html', '../'),
    ('blog/index.html', '../'),
]


def find_div_end(html, start):
    """Return the index after the closing </div> of the div element at 'start'."""
    depth = 0
    i = start
    n = len(html)
    while i < n:
        if html[i] == '<':
            # Check for opening <div ...> or <div>
            if html[i:i+4] == '<div' and (i + 4 >= n or html[i+4] in ' \t\n\r>'):
                depth += 1
                i += 4
            elif html[i:i+6] == '</div>':
                depth -= 1
                i += 6
                if depth == 0:
                    return i
            else:
                i += 1
        else:
            i += 1
    return -1


def process_page(page_path, base):
    full_path = os.path.join(BASE_DIR, page_path.replace('/', os.sep))
    with open(full_path, 'r', encoding='utf-8') as f:
        html = f.read()

    changes = []

    # ── 1. Remove <style id="hamburger-styles">...</style> ──────────────────
    new_html, n = re.subn(
        r'\s*<style id="hamburger-styles">.*?</style>',
        '',
        html,
        flags=re.DOTALL
    )
    if n:
        html = new_html
        changes.append('removed hamburger-styles')

    # ── 2. Replace headerWrapper div with site-header placeholder ───────────
    hw_idx = html.find('<div id="headerWrapper"')
    if hw_idx != -1:
        hw_end = find_div_end(html, hw_idx)
        if hw_end != -1:
            html = html[:hw_idx] + '<div id="site-header"></div>' + html[hw_end:]
            changes.append('replaced headerWrapper')
        else:
            print(f'  WARNING: Could not find end of headerWrapper in {page_path}')
    else:
        print(f'  WARNING: headerWrapper not found in {page_path}')

    # ── 3. Replace footer ────────────────────────────────────────────────────
    if base == '':
        # index.html: footer wrapped in component-footer-contact-* div
        footer_wrapper_match = re.search(r'<div id="component-footer[^"]*">', html)
        if footer_wrapper_match:
            fw_idx = footer_wrapper_match.start()
            fw_end = find_div_end(html, fw_idx)
            if fw_end != -1:
                html = html[:fw_idx] + '<div id="site-footer"></div>' + html[fw_end:]
                changes.append('replaced footer wrapper (root)')
            else:
                print(f'  WARNING: Could not find end of footer wrapper in {page_path}')
        else:
            # Fallback: plain footer tag
            fm = re.search(r'<footer\b[^>]*bg-slate-900[^>]*>', html)
            if fm:
                f_start = fm.start()
                f_end = html.find('</footer>', f_start) + len('</footer>')
                html = html[:f_start] + '<div id="site-footer"></div>' + html[f_end:]
                changes.append('replaced footer (root fallback)')
            else:
                print(f'  WARNING: Footer not found in {page_path}')
    else:
        # Subpages: plain <footer class="bg-slate-900...">
        fm = re.search(r'<footer\b[^>]*bg-slate-900[^>]*>', html)
        if fm:
            f_start = fm.start()
            f_end_match = re.search(r'</footer>', html[f_start:])
            if f_end_match:
                f_end = f_start + f_end_match.end()
                # Preserve any leading whitespace before the footer tag
                html = html[:f_start] + '<div id="site-footer"></div>' + html[f_end:]
                changes.append('replaced footer (subpage)')
            else:
                print(f'  WARNING: No </footer> found in {page_path}')
        else:
            print(f'  WARNING: Footer not found in {page_path}')

    # ── 4. Replace inline hamburger JS with components.js script tag ─────────
    # Match a <script>...</script> block that contains the headerWrapper init code
    script_pattern = re.compile(
        r'<script>((?:(?!</script>).)*var wrapper\s*=\s*document\.getElementById\(["\']headerWrapper["\'](?:(?!</script>).)*)</script>',
        re.DOTALL
    )
    m = script_pattern.search(html)
    if m:
        html = html[:m.start()] + f'<script src="{base}js/components.js"></script>' + html[m.end():]
        changes.append('replaced hamburger JS')
    else:
        print(f'  WARNING: Hamburger JS script not found in {page_path}')

    # ── Write output ─────────────────────────────────────────────────────────
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'  OK  {page_path}: {", ".join(changes) if changes else "no changes"}')


if __name__ == '__main__':
    print('Updating pages...')
    for page_path, base in PAGES:
        process_page(page_path, base)
    print('\nDone!')
