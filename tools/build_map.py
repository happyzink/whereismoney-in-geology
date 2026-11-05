# -*- coding: utf-8 -*-
"""把 map-data.json 注入 map-template.html，产出单文件交互地图（无外部依赖）。"""
import json, pathlib

root = pathlib.Path(r"")
tpl = (root / "tools" / "map-template.html").read_text(encoding="utf-8")
data = json.loads((root / "tools" / "map-data.json").read_text(encoding="utf-8"))

# 校验：文件是否真实存在
missing = []
for d in data:
    p = root / "成稿" / d["file"]
    if not p.exists():
        missing.append(d["file"])

payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
out = tpl.replace("__DATA__", payload)
dest = root / "钱在哪里-交互版全景地图.html"
dest.write_text(out, encoding="utf-8")

print("OK items=%d  missing=%d  bytes=%d" % (len(data), len(missing), len(out.encode("utf-8"))))
if missing:
    print("MISSING:", missing)
    raise SystemExit(1)
