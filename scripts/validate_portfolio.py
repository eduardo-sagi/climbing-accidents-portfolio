#!/usr/bin/env python3
"""Small deterministic gate for the public portfolio."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.hrefs = []
        self.div_depth = 0
        self.bad_balance = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        if tag == 'a' and 'href' in attrs: self.hrefs.append(attrs['href'])
        if tag == 'div': self.div_depth += 1
    def handle_endtag(self, tag):
        if tag == 'div':
            self.div_depth -= 1
            if self.div_depth < 0: self.bad_balance = True

def main(path):
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    parser = Parser(); parser.feed(text)
    errors = []
    if parser.bad_balance or parser.div_depth != 0: errors.append('unbalanced div tags')
    for href in parser.hrefs:
        if href.startswith('#') and href[1:] not in parser.ids:
            errors.append(f'broken anchor: {href}')
    if re.search(r'(?i)overuse|sobreuso|performance|tendinopatia|tendinopathy', text):
        errors.append('forbidden overuse/performance vocabulary')
    lang = re.search(r'<html\s+lang="([^"]+)"', text)
    language = lang.group(1) if lang else 'unknown'
    required_by_language = {
        'pt-BR': ['EUA', 'NEISS', 'AAC/ANAC', 'IATR', 'Agrupamento possível', 'Fontes e rastreabilidade'],
        'en': ['USA', 'NEISS', 'AAC/ANAC', 'IATR', 'What we will not do', 'Sources and traceability'],
        'es': ['EE. UU.', 'NEISS', 'AAC/ANAC', 'IATR', 'Lo que no haremos', 'Fuentes y trazabilidad'],
    }
    for item in required_by_language.get(language, required_by_language['pt-BR']):
        if item not in text: errors.append(f'missing required evidence: {item}')
    if errors:
        for error in errors: print(f'FAIL: {error}')
        return 1
    print(f'PASS: {p} | sections={text.count("<section")} | anchors={len(parser.hrefs)}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else 'index.html'))
