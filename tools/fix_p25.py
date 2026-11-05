# -*- coding: utf-8 -*-
"""第25期定点修正：E02 骑手倍数口径 + REITs 分派率补位。精确串替换，幂等。"""
import pathlib

p = pathlib.Path(r"成稿\第25期-全集精编一册通读版.md")
t = p.read_text(encoding="utf-8")
orig = t

FIXES = [
    # E02 骑手倍数：30-60 → 28-53，并注明口径
    ("同一生态差约30-60倍；48%骑手年接单不足30天（大量过渡性就业）。",
     "同一生态差约**28-53倍**（红队修正；原30-60倍系分子分母分属拼多多与美团、口径错配；48%骑手年接单不足30天，大量为过渡性就业）。"),
    # P04 三档：补 REITs 分派率口径提示（若原文有 4.18 则改；否则在 0-7% 处加脚注提示）
    ("未来预期统一按**0-7%**规划（红队修正，进取档4-7%）",
     "未来预期统一按**0-7%**规划（红队修正，进取档4-7%；REITs 分派率全市场5.37% 与产权类4.18% 属不同口径，不可互换）"),
]

applied, missed = 0, []
for old, new in FIXES:
    if new in t:
        continue  # 已修正
    if old in t:
        t = t.replace(old, new, 1)
        applied += 1
    else:
        missed.append(old[:24])

if t != orig:
    p.write_text(t, encoding="utf-8")

print("applied=%d missed=%s bytes %d -> %d" % (applied, missed, len(orig.encode('utf-8')), len(t.encode('utf-8'))))
