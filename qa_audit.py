#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static quality, actionable translation, and button-class audit for ArabSea."""
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CORE = (ROOT / 'assets/js/core/app.js').read_text(encoding='utf-8')
ACTION_SOURCE = (ROOT / 'assets/js/core/actions.js').read_text(encoding='utf-8')
I18N = (ROOT / 'assets/js/core/i18n.js').read_text(encoding='utf-8')
TRANSLATED = {key for key, _ in re.findall(r"'((?:\\.|[^'])*)'\s*:\s*'((?:\\.|[^'])*)'", I18N)}
NAME_ONLY = re.compile(r'^(?:أ\.|م\.|د\.|الأستاذ|الأستاذة|المهندس|المهندسة)\s*[\u0600-\u06ff ]{2,}$')

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack=[]; self.nodes=[]; self.roots=[]; self.controls=[]; self.text_leaves=[]
        self.ids=set(); self.duplicates=[]; self.targets=[]; self.assets=[]; self.forms=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); node={'tag':tag,'attrs':a,'text':'','direct':[],'leaves':[],'icons':''}
        if tag=='i':
            for parent in self.stack: parent['icons']+=' '+a.get('class','')
        if self.stack:self.stack[-1].setdefault('children',[]).append(node)
        else:self.roots.append(node)
        self.stack.append(node); self.nodes.append(node)
        if a.get('id'):
            if a['id'] in self.ids:self.duplicates.append(a['id'])
            self.ids.add(a['id'])
        if tag in ('button','a','input','select','textarea') or a.get('role') in ('button','link','tab','menuitem'):
            if not(tag=='input' and a.get('type') in ('hidden','submit')):self.controls.append(node)
        if tag=='a' and 'href' in a:self.targets.append(a['href'])
        if tag=='form':self.forms.append(node)
        if tag in ('script','link'):
            value=a.get('src') or (a.get('href') if a.get('rel')=='stylesheet' else '')
            if value:self.assets.append(value)
    def handle_data(self,data):
        text=' '.join(data.split())
        if not text:return
        self.text_leaves.append((text,tuple(x['tag'] for x in self.stack)))
        for node in self.stack:
            node['text'] += (' ' if node['text'] else '')+text
            node['leaves'].append(text)
        if self.stack:self.stack[-1]['direct'].append(text)
    def handle_endtag(self,tag):
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i]['tag']==tag:del self.stack[i:];break

def has_arabic(value): return bool(re.search(r'[\u0600-\u06ff]',value or ''))
def norm(value): return ' '.join((value or '').split())
def is_nav_link(node):
    return node['tag']=='a' and ('nav' in node.get('ancestors',()) or node['attrs'].get('role') in ('link','menuitem'))
def action_registry():
    result=[]
    for line in ACTION_SOURCE.splitlines():
        match=re.search(r'\[/((?:\\.|[^/])*)\$/\s*,\s*\{(.*)\}\],',line)
        if not match:continue
        route=match.group(1).replace('\\/','/')
        actions=dict(re.findall(r"'([^']+)'\s*:\s*'([^']+)'",match.group(2)))
        try: pattern=re.compile(route)
        except re.error: continue
        result.append((pattern,actions))
    return result
REGISTRY=action_registry()

def registered_create(page,label):
    rel=page.as_posix()
    for route,actions in REGISTRY:
        if route.search(rel):
            for name,schema in actions.items():
                if norm(name)==norm(label):return schema
    return None

def classify_button(page,node):
    a=node['attrs']; label=norm(node['text'] or a.get('aria-label') or a.get('title'))
    if 'disabled' in a or a.get('aria-disabled')=='true':return 'L. Intentionally disabled'
    if registered_create(page,label):return 'C. Create (business schema)'
    low=label.lower(); icon=node['icons']
    if 'onclick' in a and page.as_posix()=='login.html':
        return 'B. Modal / drawer' if re.search(r'العودة للرئيسية|return home',low) else 'A. Navigation'
    if re.fullmatch(r'\d+',label):return 'A. Navigation / pagination'
    if any(x in icon for x in ('fa-bars','fa-moon','fa-sun','fa-bell')) or a.get('id')=='themeToggle':return 'A. Navigation / shared shell'
    if re.search(r'قرارات إدارية|الموارد البشرية|تقنية المعلومات|الرواتب والأجور|أوامر الشراء|فواتير الموردين|عهد ومصروفات|الإجازات والمغادرات|خطابات التعريف|السلف والعهد|الرحلات والانتدابات|^الكل$',low):return 'F. Filter'
    if re.search(r'بيانات الشركة|الأمان وحماية البيانات|التنبيهات والإشعارات|الربط التقني|تغيير$|إيقاف$|إعدادات|settings|حفظ التغييرات',low) and (page.as_posix().endswith('admin_settings.html') or page.as_posix().endswith('fin_settings.html') or page.as_posix().endswith('admin/profile.html')):return 'J. Settings'
    if re.search(r'export|تصدير|excel|csv|pdf|طباعة|print',low):return 'G. Export'
    if re.search(r'download|تحميل|preview|استعراض|عرض|تفاصيل|fa-eye|fa-file|fa-folder',low+' '+icon):return 'H. Download / preview'
    if re.search(r'filter|تصفية|الكل|all|الرواتب والأجور|أوامر الشراء|فواتير الموردين|عهد ومصروفات|الإجازات والمغادرات|خطابات التعريف|السلف والعهد|الرحلات والانتدابات',low):return 'F. Filter'
    if re.search(r'approve|اعتماد|موافقة|رفض|reject|إرجاع|return|تصويت|vote|إقرار|تسجيل قراءة|تأكيد القراءة|إغلاق|close|complete|مكتمل|تذكير|remind|حضور|attendance|مراجعة|update assessment|تحديث التقييم|متابعة.*cap|إدخال رد الإدارة|مصفوفة المخاطر|استلام|إلغاء الطلب|تغيير الحالة|إعادة للمراجعة|fa-check|fa-ban|fa-unlock|fa-play|fa-rotate',low+' '+icon):return 'E. Workflow action'
    if re.search(r'مشاركة رابط|share link|رسالة|مراسلة|توجيه تعميم|نشر وتعميم|إرسال تعميم',low):return 'I. Communication'
    if re.search(r'مراجعة الطلبات|الانضمام للأنظمة|لوحة المشاريع|مشاريع|السجل الكامل|السجل الشامل|سجل المهام',low):return 'A. Navigation'
    if re.search(r'مكالمة|صوتية|مرئية|رسالة|مراسلة|محادثة|chat|message|fa-phone|fa-video',low+' '+icon):return 'I. Communication'
    if re.search(r'إعداد|settings|حفظ|save|ربط|integration|شعار|security|أمان|الصلاحيات',low):return 'J. Settings'
    if re.search(r'edit|تعديل|تحرير|تحديث المستهدفات|تحديث النسب|إدارة الصلاحيات|تغيير كلمة المرور|fa-pen|fa-key',low+' '+icon):return 'D. Edit'
    if re.search(r'عرض|تفاصيل|معلومات|preview|fa-circle-info',low+' '+icon):return 'B. Modal / drawer'
    # The shared listener now opens an explicit backend-required explanation and performs no fake update.
    return 'K. Backend-dependent (explicit explanation; no fake completion)'

def main():
    pages=sorted(ROOT.rglob('*.html')); total=Counter(); missing=[]; bad_frag=[]; dup=[]; control_rows=[]; form_count=0; target_count=0; page_texts=[]
    actionable=Counter(); translated_actionable=Counter(); untranslated=defaultdict(set); untranslated_placeholders=set(); names_excluded=set(); sample_excluded=set(); all_ui=set(); translated_ui=set()
    action_paths=Counter(); button_classes=Counter(); backend_buttons=[]
    for page in pages:
        text=page.read_text(encoding='utf-8'); p=PageParser(); p.feed(text); rel=page.relative_to(ROOT); form_count+=len(p.forms)
        # Ancestor tags are recovered by a second tree traversal for links and controls.
        def tag_tree(node, ancestors=()):
            node['ancestors']=ancestors
            for child in node.get('children',[]):tag_tree(child,ancestors+(node['tag'],))
        for node in p.roots:tag_tree(node)
        total['pages']+=1; total['buttons']+=sum(c['tag']=='button' for c in p.controls); total['links']+=sum(c['tag']=='a' for c in p.controls)
        total['fields']+=sum(c['tag'] in ('input','select','textarea') for c in p.controls);total['tables']+=text.lower().count('<table')
        if p.duplicates:dup.extend((rel,x) for x in p.duplicates)
        for href in p.targets:
            target_count+=1
            if href.startswith('#') and len(href)>1 and href[1:] not in p.ids:bad_frag.append((rel,href))
            u=urlparse(href)
            if not href or href.startswith(('http:','https:','mailto:','tel:','javascript:')) or not u.path:continue
            if not(page.parent/u.path).resolve().exists():missing.append((rel,href))
        for asset in p.assets:
            if asset.startswith(('http:','https:')):continue
            if not(page.parent/asset).resolve().exists():missing.append((rel,'asset '+asset))
        if 'assets/js/core/app.js' not in text or 'assets/js/core/i18n.js' not in text or 'assets/js/core/actions.js' not in text:total['pages_missing_core']+=1
        for phrase,ancestors in p.text_leaves:
            if has_arabic(phrase) and 'tbody' in ancestors:sample_excluded.add(phrase)
        for node in p.controls:
            tag,a=node['tag'],node['attrs']; label=norm(node['text'] or a.get('aria-label') or a.get('title') or a.get('placeholder'))
            if tag=='button':
                category=classify_button(page.relative_to(ROOT),node);button_classes[category]+=1
                control_rows.append((rel,label or '[icon]',category));
                if category.startswith('K.') : backend_buttons.append((rel,label or '[icon]'))
            if tag=='button' or (tag=='a' and is_nav_link(node)):
                actionable['buttons' if tag=='button' else 'navigation']+=1
                for leaf in node['leaves']:
                    if has_arabic(leaf):
                        if NAME_ONLY.fullmatch(leaf):names_excluded.add(leaf);continue
                        all_ui.add(leaf)
                        if leaf in TRANSLATED:translated_ui.add(leaf)
                        else:untranslated['buttons' if tag=='button' else 'navigation'].add(leaf)
            if tag=='label':
                label_text=norm(' '.join(node['direct']))
                if has_arabic(label_text):
                    actionable['form labels']+=1
                    if NAME_ONLY.fullmatch(label_text):names_excluded.add(label_text)
                    else:
                        all_ui.add(label_text)
                        if label_text in TRANSLATED:translated_ui.add(label_text)
                        else:untranslated['form labels'].add(label_text)
            if tag in ('th','option','h1','h2','h3','h4','h5','h6'):
                val=norm(' '.join(node['direct']))
                if has_arabic(val) and not NAME_ONLY.fullmatch(val):
                    all_ui.add(val)
                    if val in TRANSLATED:translated_ui.add(val)
            for attr in ('placeholder','title','aria-label'):
                val=norm(a.get(attr,''))
                if has_arabic(val):
                    all_ui.add(val)
                    if val in TRANSLATED:translated_ui.add(val)
                    elif tag=='button':untranslated['buttons'].add(val)
                    elif tag=='a' and is_nav_link(node):untranslated['navigation'].add(val)
                    elif attr=='placeholder':untranslated_placeholders.add(val)
        # Include option/status strings in actionable UI metrics, but exclude sample record cells.
        page_texts.append(p)
    total['forms']=form_count;total['internal_targets']=target_count
    # The all-untranslated sets are keyed by category and contain unique phrases.
    unique_count=len(all_ui); translated_count=len(translated_ui); ui_percent=100*translated_count/unique_count if unique_count else 100
    # Confirm old generic page-action/create-record fallbacks are absent from the source.
    generic_fallbacks=0
    if "'Page Action'" in CORE or "Create new record" in CORE or 'إجراء الصفحة' in CORE: generic_fallbacks=1
    report=['# ArabSea QA Validation','','Generated by `scripts/qa_audit.py`. Static classifications describe the implemented route or explicit backend-required response; they do not substitute for browser verification.','', '## Acceptance metrics','',f'- Total buttons: **{total["buttons"]}**',f'- Contextually classified buttons (A–J): **{total["buttons"]-button_classes["K. Backend-dependent (explicit explanation; no fake completion)"]-button_classes["L. Intentionally disabled"]}**',f'- Backend-dependent buttons (K): **{button_classes["K. Backend-dependent (explicit explanation; no fake completion)"]}**',f'- Intentionally disabled buttons (L): **{button_classes["L. Intentionally disabled"]}**',f'- Generic Page Action / generic Create Record fallback buttons: **{generic_fallbacks}**','', '## Translation coverage','',f'- Unique appropriate UI strings: **{unique_count}**',f'- Translated unique appropriate UI strings: **{translated_count}**',f'- Overall appropriate UI translation coverage: **{ui_percent:.1f}%**',f'- Proper-name exclusions: **{len(names_excluded)} unique strings**',f'- Sample table data excluded from UI denominator: **{len(sample_excluded)} unique strings**',f'- Untranslated actionable buttons: **{len(untranslated["buttons"])} unique strings**',f'- Untranslated navigation: **{len(untranslated["navigation"])} unique strings**',f'- Untranslated form labels: **{len(untranslated["form labels"])} unique strings**',f'- Untranslated placeholders: **{len(untranslated_placeholders)} unique strings**','', '## Static repository checks','',f'- HTML pages: **{total["pages"]}**',f'- Links: **{total["links"]}**',f'- Form controls: **{total["fields"]}**',f'- Tables: **{total["tables"]}**',f'- Forms: **{total["forms"]}**',f'- Duplicate IDs: **{len(dup)}**',f'- Missing local targets/assets: **{len(missing)}**',f'- Broken fragment targets: **{len(bad_frag)}**',f'- Pages missing shared scripts: **{total["pages_missing_core"]}**','', '## Button classification','', '| Class | Count |','|---|---:|']
    report += [f'| {name} | {count} |' for name,count in sorted(button_classes.items())]
    report += ['','## Untranslated actionable UI','']
    for group in ('buttons','navigation','form labels'):
        report += [f'### {group.title()}','']
        vals=sorted(untranslated[group])
        report += ([f'- {s}' for s in vals] if vals else ['- None.'])+['']
    excluded=set().union(*untranslated.values())
    other_missing=sorted(all_ui-translated_ui-excluded)
    report += ['### Other untranslated appropriate UI strings','']+([f'- {s}' for s in other_missing] if other_missing else ['- None.'])+['']
    if backend_buttons:
        report += ['## Backend-dependent button inventory','','These actions open an explicit explanation and do not claim the business operation was performed.','']
        report += [f'- `{path}` — {label}' for path,label in backend_buttons]
    if dup or missing or bad_frag or total['pages_missing_core']:
        report += ['## Structural findings','']
        report += [f'- Duplicate ID: `{path}` — `{value}`' for path,value in dup]
        report += [f'- Missing target: `{path}` — `{value}`' for path,value in missing]
        report += [f'- Broken fragment: `{path}` — `{value}`' for path,value in bad_frag]
    (ROOT/'QA_VALIDATION.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
    print({'pages':total['pages'],'buttons':total['buttons'],'contextual':total['buttons']-button_classes['K. Backend-dependent (explicit explanation; no fake completion)']-button_classes['L. Intentionally disabled'],'backend':button_classes['K. Backend-dependent (explicit explanation; no fake completion)'],'disabled':button_classes['L. Intentionally disabled'],'generic_fallback':generic_fallbacks,'ui_unique':unique_count,'ui_translated':translated_count,'ui_percent':round(ui_percent,1),'untranslated_buttons':len(untranslated['buttons']),'untranslated_navigation':len(untranslated['navigation']),'untranslated_form_labels':len(untranslated['form labels']),'untranslated_placeholders':len(untranslated_placeholders)})
    print(f'duplicate_ids={len(dup)} missing_targets_assets={len(missing)} broken_fragments={len(bad_frag)} pages_missing_core={total["pages_missing_core"]}')

if __name__=='__main__':main()
