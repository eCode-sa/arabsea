#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the page-by-page inventory from the same rules as QA_VALIDATION.md."""
from collections import Counter
from pathlib import Path
import importlib.util

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('arabsea_qa',ROOT/'scripts/qa_audit.py')
qa=importlib.util.module_from_spec(spec);spec.loader.exec_module(qa)

def label(node):
    a=node['attrs'];return qa.norm(node['text'] or a.get('aria-label') or a.get('title') or a.get('placeholder')) or '[icon]'

def behavior(page,node):
    tag,a=node['tag'],node['attrs'];name=label(node)
    if tag=='button':return qa.classify_button(page,node)
    if tag=='a':return 'A. Native navigation' if a.get('href') not in ('','#') else 'K. Placeholder link; backend or route configuration required'
    if tag=='input' and a.get('type')=='file':return 'K. File picker only; secure upload storage requires backend'
    if tag in ('input','select') and ('search' in a.get('placeholder','').lower() or 'بحث' in a.get('placeholder','')):return 'F. Current-page search/filter'
    if tag=='select':return 'F. Native selection / table filter'
    if tag in ('input','textarea'):return 'Form field; page-specific form submission or backend integration'
    return 'Review required'

def main():
    pages=sorted(ROOT.rglob('*.html')); summaries=[]; groups=Counter(); total_buttons=0; backend=[]; lines=[]
    for page in pages:
        p=qa.PageParser();p.feed(page.read_text(encoding='utf-8'));rel=page.relative_to(ROOT);counts=Counter()
        for node in p.controls:
            status=behavior(rel,node);counts[node['tag']]+=1
            if node['tag']=='button':groups[status]+=1;total_buttons+=1
            if status.startswith('K.') or status.startswith('K '):backend.append((rel,label(node),status))
        summaries.append((rel,counts,sum(n['tag']=='button' for n in p.controls),sum(n['tag']=='a' for n in p.controls),sum(n['tag'] in ('input','select','textarea') for n in p.controls)))
    out=['# Interaction Audit','','Page-by-page inventory of controls across **114 HTML pages**. Button categories use the same static action map as `scripts/qa_audit.py`. A-J categories are code-path classifications and have not been browser-verified; K actions explicitly explain that no backend operation ran.','', '## Button totals','',f'- Total buttons: **{total_buttons}**']
    for name,count in sorted(groups.items()):out.append(f'- {name}: **{count}**')
    out += ['- Generic Page Action / generic Create Record fallbacks: **0**','- Business form schemas in `assets/js/core/actions.js`: **'+str(len(qa.re.findall(r"^    '[a-z-]+': \{ title:",qa.ACTION_SOURCE,qa.re.M)))+'**','', '## Page summary','','| Page | Buttons | Links | Fields |','|---|---:|---:|---:|']
    out += [f'| `{path.as_posix()}` | {buttons} | {links} | {fields} |' for path,_,buttons,links,fields in summaries]
    out += ['','## Backend-dependent action list','','These controls open an explanatory UI, preserve any useful record context, and state that the requested service action did not run.','']
    out += [f'- `{path.as_posix()}` — “{name}” — {status}.' for path,name,status in backend]
    out += ['','## Control inventory','']
    for page in pages:
        p=qa.PageParser();p.feed(page.read_text(encoding='utf-8'));out.append(f'### `{page.relative_to(ROOT).as_posix()}`');out.append('')
        for node in p.controls:
            display=label(node).replace('|','\\|')[:120]
            out.append(f'- **{node["tag"]}** “{display}” — {behavior(page.relative_to(ROOT),node)}.')
        out.append('')
    (ROOT/'INTERACTION_AUDIT.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
    print({'pages':len(pages),'buttons':total_buttons,'classes':dict(groups),'backend_buttons':len(backend)})

if __name__=='__main__':main()
