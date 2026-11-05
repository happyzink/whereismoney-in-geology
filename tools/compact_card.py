# -*- coding: utf-8 -*-
"""压缩速查卡排版，使 A4 单页装下。"""
import pathlib

p = pathlib.Path(r"钱在哪里-口径速查卡.html")
h = p.read_text(encoding="utf-8")

SUBS = [
    ("@page{size:A4 portrait;margin:10mm}", "@page{size:A4 portrait;margin:7mm}"),
    ("font-size:9.2pt;line-height:1.45", "font-size:8.5pt;line-height:1.33"),
    ("h1{font-size:16pt;margin:0 0 2px", "h1{font-size:13pt;margin:0 0 1px"),
    (".lead{font-size:8.4pt;color:var(--dim);border-bottom:2px solid var(--gold);padding-bottom:4px;margin-bottom:7px}",
     ".lead{font-size:7.5pt;color:var(--dim);border-bottom:2px solid var(--gold);padding-bottom:2px;margin-bottom:4px}"),
    ("h2{font-size:9.6pt;margin:7px 0 3px;padding:2px 6px", "h2{font-size:8.6pt;margin:3px 0 1px;padding:1px 5px"),
    ("table{width:100%;border-collapse:collapse;font-size:8.1pt;margin-bottom:2px",
     "table{width:100%;border-collapse:collapse;font-size:7.4pt;margin-bottom:1px"),
    ("th,td{border-bottom:1px solid var(--line);padding:2px 3px", "th,td{border-bottom:1px solid var(--line);padding:1px 2px"),
    (".note{font-size:7.6pt", ".note{font-size:6.9pt"),
    (".check{border:1.5px solid var(--gold);border-radius:4px;padding:5px 8px;margin-top:7px",
     ".check{border:1.2px solid var(--gold);border-radius:4px;padding:3px 7px;margin-top:4px"),
    (".check h3{margin:0 0 3px;font-size:9pt}", ".check h3{margin:0 0 1px;font-size:8.4pt}"),
    (".check ol{margin:0;padding-left:15px;font-size:8.2pt}",
     ".check ol{margin:0;padding-left:14px;font-size:7.4pt;column-count:2;column-gap:6mm}"),
    (".check li{margin-bottom:1.5px}", ".check li{margin-bottom:0}"),
    (".foot{margin-top:6px;border-top:1px solid var(--line);padding-top:4px;font-size:7.4pt",
     ".foot{margin-top:3px;border-top:1px solid var(--line);padding-top:2px;font-size:6.7pt"),
    ('table style="font-size:7.7pt"', 'table style="font-size:7.1pt"'),
]

applied, missed = 0, []
for a, b in SUBS:
    if b in h and a not in h:
        continue
    if a in h:
        h = h.replace(a, b); applied += 1
    else:
        missed.append(a[:36])

p.write_text(h, encoding="utf-8")
print("applied=%d missed=%s" % (applied, missed))
