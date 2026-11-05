import sys, re, pypdf
path, kw = sys.argv[1], sys.argv[2]
r = pypdf.PdfReader(path)
out = []
for i, p in enumerate(r.pages):
    try:
        t = p.extract_text() or ""
    except Exception:
        continue
    if kw in t:
        for m in re.finditer(kw, t):
            s = max(0, m.start() - 220)
            out.append((i + 1, t[s:m.end() + 420].replace("\n", " ")))
print("PAGES", len(r.pages), "HITS", len(out))
for pg, s in out[:8]:
    print("=== p%d: %s" % (pg, s))
