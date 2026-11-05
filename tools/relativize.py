#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把《钱在哪里》公开版的 tools 脚本里的绝对路径改为相对路径。"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"

SUBS = [
    (r'str(ROOT)', 'str(ROOT)'),
    (r'str(ROOT)', 'str(ROOT)'),
    (r'str(ROOT)', 'str(ROOT)'),
    (r'ROOT', 'ROOT'),
    (r'str(ROOT / "成稿")', 'str(ROOT / "成稿")'),
]

for f in TOOLS.glob("*.py"):
    t = f.read_text(encoding="utf-8")
    orig = t
    for a, b in SUBS:
        t = t.replace(a, b)
    if t != orig:
        # 确保有 ROOT 定义
        if "ROOT = pathlib.Path(__file__)" not in t and "str(ROOT)" in t:
            t = t.replace("import pathlib", "import pathlib\n\nROOT = pathlib.Path(__file__).resolve().parent.parent", 1)
        f.write_text(t, encoding="utf-8")
        print("FIXED", f.name)

# 残留绝对路径检查
left = []
for f in list(TOOLS.glob("*.py")) + list(ROOT.rglob("*.md")):
    t = f.read_text(encoding="utf-8", errors="ignore")
    for m in re.finditer(r"[A-Za-z]:[\\/](?:Users|job)[\\/]", t):
        left.append((f.name, t[max(0,m.start()-30):m.end()+30].replace("\n"," ")))
print("\n残留绝对路径：%d" % len(left))
for n, frag in left[:10]:
    print("  ", n, "::", frag)
