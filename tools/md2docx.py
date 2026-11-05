# -*- coding: utf-8 -*-
"""md2docx.py — 《钱在哪里》全景计划 成稿批量转换（Markdown → docx）
用法: python md2docx.py
输入: 成稿/*.md + 项目根 00-总任务书.md / 01-进度看板.md
输出: 成稿/docx/<同名>.docx
"""
import re, glob, os
from docx import Document
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH

BASE = r""
OUT_DIR = os.path.join(BASE, "成稿", "docx")
os.makedirs(OUT_DIR, exist_ok=True)

def set_fonts(doc):
    st = doc.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(10.5)
    st._element.rPr.rFonts.set(qn("w:eastAsia"), "微软雅黑")
    for i in range(1, 5):
        h = doc.styles[f"Heading {i}"]
        h.font.name = "Calibri"
        h._element.rPr.rFonts.set(qn("w:eastAsia"), "微软雅黑")
        h.font.color.rgb = RGBColor(0x1F, 0x3B, 0x5C)

INLINE = re.compile(r"(\*\*.+?\*\*|\[[^\]]+\]\([^)]+\)|`[^`]+`)")

def add_inline(p, text):
    for tok in INLINE.split(text):
        if not tok:
            continue
        if tok.startswith("**") and tok.endswith("**"):
            r = p.add_run(tok[2:-2]); r.bold = True
        elif tok.startswith("`") and tok.endswith("`"):
            r = p.add_run(tok[1:-1]); r.font.name = "Consolas"
        elif tok.startswith("[") and "](" in tok:
            m = re.match(r"\[([^\]]+)\]\(([^)]+)\)", tok)
            label, url = m.group(1), m.group(2)
            r = p.add_run(label + " ")
            r.font.color.rgb = RGBColor(0x1A, 0x5F, 0xB4)
            r2 = p.add_run(f"({url})")
            r2.font.size = Pt(8); r2.font.color.rgb = RGBColor(0x88, 0x88, 0x88)
        else:
            p.add_run(tok)

def is_table_line(l):
    return l.strip().startswith("|") and l.strip().endswith("|")

def is_sep_row(l):
    return re.fullmatch(r"\s*\|?[\s:\-|]+\|?\s*", l) is not None and "-" in l

def convert(md_path, out_path):
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    doc = Document()
    set_fonts(doc)
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()
        if not s:
            i += 1; continue
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            lvl = min(len(m.group(1)), 4)
            doc.add_heading(m.group(2), level=lvl)
            i += 1; continue
        if is_table_line(s):
            rows = []
            while i < n and is_table_line(lines[i].strip()):
                if not is_sep_row(lines[i]):
                    cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                    rows.append(cells)
                i += 1
            if rows:
                cols = max(len(r) for r in rows)
                t = doc.add_table(rows=len(rows), cols=cols)
                t.style = "Light Grid Accent 1"
                for ri, r in enumerate(rows):
                    for ci in range(cols):
                        cell = t.cell(ri, ci)
                        cell.text = ""
                        p = cell.paragraphs[0]
                        add_inline(p, r[ci] if ci < len(r) else "")
                        for run in p.runs:
                            run.font.size = Pt(9)
                            if ri == 0:
                                run.bold = True
            continue
        if s.startswith(">"):
            p = doc.add_paragraph(style="Intense Quote")
            add_inline(p, s.lstrip("> ").strip())
            i += 1; continue
        if re.fullmatch(r"-{3,}|={3,}|\*{3,}", s):
            i += 1; continue
        m = re.match(r"^(\s*)[-*]\s+\[( |x|X)\]\s+(.*)$", line)
        if m:
            box = "☑ " if m.group(2).lower() == "x" else "☐ "
            p = doc.add_paragraph(style="List Bullet")
            add_inline(p, box + m.group(3))
            i += 1; continue
        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if m:
            p = doc.add_paragraph(style="List Bullet")
            add_inline(p, m.group(1))
            i += 1; continue
        m = re.match(r"^\s*\d+[\.、)]\s+(.*)$", line)
        if m:
            p = doc.add_paragraph(style="List Number")
            add_inline(p, m.group(1))
            i += 1; continue
        p = doc.add_paragraph()
        add_inline(p, s)
        i += 1
    doc.save(out_path)

def main():
    targets = sorted(glob.glob(os.path.join(BASE, "成稿", "*.md")))
    for extra in ("00-总任务书.md", "01-进度看板.md"):
        p = os.path.join(BASE, extra)
        if os.path.exists(p):
            targets.append(p)
    ok, fail = 0, []
    for md in targets:
        name = os.path.splitext(os.path.basename(md))[0] + ".docx"
        try:
            convert(md, os.path.join(OUT_DIR, name))
            ok += 1
            print("OK", name)
        except Exception as e:
            fail.append((name, repr(e)))
            print("FAIL", name, repr(e))
    print(f"DONE ok={ok} fail={len(fail)} out={OUT_DIR}")

if __name__ == "__main__":
    main()
