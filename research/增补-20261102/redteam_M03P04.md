# 红队五 · 攻击 M03 矿业估值与 P04 资产配置（反方立场）

- 日期：2026-11-02 ｜ 立场：红队反方，攻击而非辩护
- 对象：成稿第M03期《资源租金与矿业估值——把石头变成现金流》、成稿第P04期《资产配置20年——躺在账户里涨的钱》及其研究底稿
- 方法：本地计划文档逐句摘录（文件:行号）+ 公开来源检索 12 次（另有 2 次 C-REITs 检索为空结果，见 §3.3 与 §5）
- 引用契约：`[^id]` 语义句柄，源定义紧跟所在小节；本地计划文件以 `L-` 前缀标注（路径:行号）。关键数字均逐字摘录并附「信度/时间窗/口径」。

---

## 0. 结论摘要

1. **M03 的"NAV 实算与市场互证"是插值游戏而非验证（高置信）**：长期价格假设是拼凑变量（plug）——先调价凑到市值，再宣布"市场隐含价 = 我们的中性价"。M03 自己承认"NAV 即上移约770亿……可以完全不依赖任何新基本面信息"[L-M03d1:69]，那么 NAV≈市值 只证明"我们选的拼凑值 ≈ 市场选的拼凑值"，不构成对 NAV 数值的独立证据。
2. **折现率被断言"不重要"，但算术不支持（高置信）**：成稿写"NAV的分歧从来不在折现率，在长期价格假设"[L-M03cg:23]，却只披露了价格敏感性、未披露折现率敏感性。按标准年金算术（25年+终端增长2%），折现率±1pp ≈ NAV∓8-9%、±2pp ≈ ∓15-20%，**与"价格±20%→NAV±10%"同量级甚至更大**。
3. **储量口径风险真实存在（高置信）**：紫金官网自报铜"储量"5,661万吨，而《中国矿产资源报告2024》口径全国铜储量 4,065 万吨——同名指标两套口径；JORC 下 Ore Reserve 只能来自 Measured/Indicated，GB/T 17766-2020 下资源量仅完成"概略研究"程度的技术经济评价。M03 的 NAV 用产量指引绕开储量结构，等于把口径风险藏进未披露的矿山寿命与期末假设里。
4. **90分位成本线在 2026 年铜上已经脱锚（高置信）**：价格 13,000→14,000+ 美元/吨创新高，与 ICSG 账面过剩（2026Q1 过剩 396,000 吨）并存；印尼镍的 RKAB 配额管制（2026 年上限 250-260 百万吨 vs 2025 年 379 百万吨）证明政策可以直接改写供给函数。M03 研究底稿自己承认"成本分位线不是铁底"[L-M03d3:52]，成稿却升级为"价格地板"操作规则。
5. **P04 三档模板三个输入都缺依据（中-高置信）**：「100-年龄」被退休阶段实证（Pfau-Kitces 2014：平稳或上升路径优于递减路径）直接反驳其普适性；黄金 10-15% 无任何引用且研究区间严重分歧（IGWT 2024 主张 14-18% vs Erb-Harvey 无现金流批判）；REITs 的税费覆盖有政策空洞、流动性数据本轮未能独立核到（如实记为空结果）。

---

## 1. 攻击一：M03 NAV 实算

### 1.1 储量口径风险：JORC 与中国 GB/T 17766 混用的三重漏洞

**发现 1.1a｜"储量"一词在公开材料中承载两套口径，且数字直接冲突（确定，一手标准+公司自报）。**

- 公司侧：紫金矿业官网"储量与资源量"页"储量"列：铜 5,661 万吨、金 1,996 吨、碳酸锂 797 万吨 LCE、银 3,231 吨[^zj-store]（信度：高——公司自报；时间窗：在线页面，截至日期未在摘要中显示，待核；口径：公司全球资产合计，混合适用境内外规范）。
- 国家侧：紫金 2024 业绩页转引"《中国矿产资源报告 2024》，2023年中国铜储量 4065 万吨、黄金储量 3204吨"[^zj-perf]（信度：高——自然资源部口径经公司转引；时间窗：2023年末；口径：中国境内、GB 分类）。另紫金 2025 年报摘要："2025年中国实现矿山产金381吨，公司矿山产金相当于中国总量的23%"[^zj-ar25]。
- 攻击点：一家公司自报的铜"储量"超过全国口径铜储量（5,661 vs 4,065 万吨），唯一解释是两套口径并行（公司含境外资产、按 JORC 等国际规范）。任何把"紫金储量"与"全国储量"放进同一张表或同一个 NAV 输入的读法，都已经在混用口径——而 M03 成稿与研究底稿未见任何储量口径脚注（待证，见 §5）。

**发现 1.1b｜JORC 与 GB/T 17766-2020 的转化条件不同，"资源量"不能当"储量"用（确定，标准原文）。**

- JORC 2012 原文："An 'Ore Reserve' is the economically mineable part of a Measured and/or Indicated Mineral Resource"[^jorc]（信度：高——标准原文；口径：JORC Code 2012 Edition 定义）。由定义直接推论：Inferred（推断）资源量不在可转化范围内。
- GB/T 17766-2020 原文："按照地质可靠程度由低到高，资源量分为推断资源量、控制资源量和探明资源量"，储量分为证实与可信[^gbt2020][^gbt-baike]（信度：高——标准文本；时间窗：2020-03-31 发布、2020-05-01 实施）。UNECE 衔接文件："根据 GB/T 17766-2020 的术语定义，资源量是经矿产资源勘查查明，通过技术经济评价工作（概略研究）……"[^unfce2020]——即资源量的经济评价只到**概略研究**程度，储量需更高阶段可行性研究。
- 旧版残留风险：GB/T 17766-1999 的分级体系是另一套（G 轴四级：探明的、控制的、推断的、预测的[^unfce1999]）。2020 年前后两套体系的"储量/基础储量"不可直接对表，跨版数据混用是行业现实风险。

**发现 1.1c｜M03 的 NAV 用产量指引绕开了储量结构，把口径风险转移进"寿命假设"（推理级，基于摘录）。**

- 实算输入是"2026年产量指引（铜120万吨、金105吨）"[L-M03d1:6]（信度：中——公司指引；时间窗：2026年度；口径：矿产铜/矿产金）。产量指引不含储量年限信息；三段式模型的尾部现金流隐含"储量可持续支撑寿命"，而各资产储量中推断资源量占比、海外资产适用规范清单，在 M03 摘录范围内均未披露。**NAV 不是因为没有直接使用资源量就免役——它只是把口径不确定性转移到了未披露的寿命与期末假设里。**

[^zj-store]: 紫金矿业官网·储量与资源量. 在线页面. https://www.zjky.cn/global/zi-yuan-yu-chu.htm
[^zj-perf]: 紫金矿业官网·2024业绩（转引《中国矿产资源报告2024》）. https://www.zjky.cn/investor/2024-performance.htm
[^zj-ar25]: 紫金矿业集团股份有限公司2025年年度报告摘要. 2026-03-20. https://www.zjky.cn/upload/file/2026/03/20/bb50638f28b449db9b1688af53a7bfd7.pdf
[^jorc]: JORC Code, 2012 Edition. 2012-12-20. https://www.jorc.org/docs/JORC_code_2012.pdf （另见 Geoscience Australia, Australia's Identified Mineral Resources 2024 Appendices, 2025-02-27, 同一定义：https://www.ga.gov.au/aimr2024/appendices）
[^gbt2020]: 《固体矿产资源储量分类》GB/T 17766-2020（标准文本PDF转载）. 实施日期2020-05-01. https://www.dzxzch.cn/zcjx/ch/202004/P020200423709369463784.pdf ；国家标准全文公开系统条目：https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=3F98C03DE9AB232432B3732A491983E7
[^gbt-baike]: 百度百科·固体矿产资源储量分类（GB/T 17766-2020 条目）. https://baike.baidu.com/item/%E5%9B%BA%E4%BD%93%E7%9F%BF%E4%BA%A7%E8%B5%84%E6%BA%90%E5%82%A8%E9%87%8F%E5%88%86%E7%B1%BB/53570752 （三级转述，与标准文本互证）
[^unfce2020]: UNECE, Updated Chinese Minerals-UNFC Bridging Document（GB/T 17766-2020 衔接文件）. 2022-10-25. https://unece.org/sites/default/files/2024-03/Updated%20Chinese%20Minerals-UNFC-BD%2025Oct2022_CEFR.pdf
[^unfce1999]: UNECE, 中国国家标准《固体矿产资源/储量分类》(GB/T 17766-1999) 衔接文件. https://www.unece.org/fileadmin/DAM/energy/se/pdfs/UNFC/UNFC-China-Bridging-Document-Public-Comment/Chinese_Mineral_BD_Final.pdf

### 1.2 折现率：被断言"不重要"的变量，弹性与价格同量级

**发现 1.2a｜敏感性披露不对称（确定，原文对照）。** 成稿给了价格敏感性："敏感性：单一商品价格±20%→NAV约±10%；铜金同向±20%→约±20%"[L-M03cg:24]，同时断言"NAV的分歧从来不在折现率，在长期价格假设"[L-M03cg:23]。检索范围内未见任何折现率敏感性表（dive_01 自述"模型为简化三段式，关键输入均有来源，但矿山级现金流是板块级近似"[L-M03d1:6]，折现率是否披露见 §5 待证）。

**发现 1.2b｜年金算术：折现率弹性与价格弹性同量级（确定——纯算术，可复算，无外部引用）。**
取 25 年现金流 + 终端增长 2%，每 1 元年现金流的现值因子：

| 折现率 r | 8% | 9% | 10% | 11% | 12% |
|---|---|---|---|---|---|
| PV 因子 | 12.68 | 11.57 | 10.61 | 9.77 | 9.03 |
| 相对 10% | +19.5% | +9.1% | — | −7.9% | −14.9% |

即 **±1pp ≈ NAV∓8-9%，±2pp ≈ NAV∓15-20%**，不小于 M03 自己披露的"价格±20%→±10%"。"分歧从来不在折现率"在算术上不成立；成立的说法只能是"两者都重要，且都必须给区间"。

**发现 1.2c｜单一折现率无法覆盖国别风险（推理级）。** 紫金资产横跨刚果（金）、塞尔维亚、哥伦比亚、苏里南、巴新等司法辖区，板块级近似[L-M03d1:6]意味着矿山级国别风险溢价、税制与汇率的差异被抹平。这不是要求重做模型，而是要求：**至少披露基准 r 与分档国别溢价的敏感性**——当前披露水平下，7,700-7,800 亿这一 NAV 不可审计。

### 1.3 隐含铜价 11,000 美元：单点假设的双向脆弱 + "互证"的循环性

**发现 1.3a｜M03 的原始主张（原文逐字）。**
- "以2026年产量指引（铜120万吨、金105吨）与中性长期价格假设（铜11,000美元/吨、金3,600美元/盎司）做NAV实算……权益NAV约7,800亿元，与2026年10月15日总市值7,812亿元几乎完全吻合——市场当前定价隐含的中长期价格假设约等于本报告的中性假设，而非现货顶格价（铜14,400美元+、金4,170美元）"[L-M03d1:6]（信度：中——自建简化模型；时间窗：2026-10-15 市值；口径：权益 NAV≈市值互证）。
- 成稿解读："你如果相信铜的结构性短缺兑现，当前市值低估；如果相信均值回归，当前定价准确"[L-M03cg:23]。

**发现 1.3b｜"互证"是循环论证（高置信）。** M03 自己写下："任何投行报告只需把长期铜价假设从9,000调到11,000美元，NAV即上移约770亿，'目标价上调'可以完全不依赖任何新基本面信息"[L-M03d1:69]。既然 NAV 对价格假设近线性，则"NAV≈市值"只是**同义反复**：中性价本来就是让 NAV 贴到市值的拼凑值。它不能证明"7,700-7,800 亿是公允 NAV"，只能证明"我们和市场选了同一个拼凑值"。

**发现 1.3c｜反方向自检成立：若供给紧张持续，11,000 是低估（高置信——2026 年市场证据链）。**

| 关键数字 | 逐字摘录 | 信度 | 时间窗 | 口径 |
|---|---|---|---|---|
| ICSG 预测摇摆 | "ICSG expects a refined copper surplus of about 289,000 metric tons for 2025 and another 209,000 tons for 2026."[^icsg-rt] | 高 | 2025-05-02 | 精炼铜供需平衡 |
| ICSG 再修正 | "projected to return to a surplus of 96,000 metric tons in 2026, reversing a previously anticipated deficit of 150,000 tons."[^icsg-am] | 中（二手转述） | 2025 秋季预测 | 精炼铜供需平衡 |
| 2026Q1 实际过剩 | "the global copper market posted a 396000-tonne surplus in Q1 2026, up from 135000 tonnes a…"（E03 已录）[L-E03d5:106] | 中 | 2026Q1，2026-05-25 发布 | ICSG Copper Bulletin |
| 价格新高 | "Copper prices soared to records above $13,000 a metric ton on Monday, driven by fears of shortages and expectations turmoil in Venezuela…"[^cu-mining] | 高 | 2026-01-05 | LME |
| 14,000 关口 | "Copper reaches two-month high of $14000 as inventories drop……LME copper prices have risen 18% this year, mainly due to large metal flows to the US on speculation regarding tariffs on refined Copper."[^cu-oe] | 高 | 2026-08-04 | LME |
| 现金结算价 | "cash copper settling at $14,424.50 a tonne, $207.50 above the…"[^cu-ob] | 高 | 2026-08-28 | LME 现货结算 |

解读：**全年实际价格（13,000-14,400+）系统性高于 M03 的"中性价"11,000 与高盛 2025-12-11 预测的"回落至10,000–11,000美元区间"[L-E03d5:107]（该预测在一个月内被击穿顶部）**。若 E03 的供给侧逻辑成立（"新矿开发周期17.9年且仍在拉长"[L-E03cg:71]、capex 十年新高、投产要到 2030s），则高价可持续，基于 11,000 的 NAV≈7,800 亿是**下限而非公允值**。M03 引用的"现货顶格价14,449美元"在自家底稿中标为待证[L-M03d3:9]——本轮检索已旁证到 8-28 的 $14,424.50[^cu-ob]，但仍未见 14,449 本身。

**发现 1.3d｜上行尾部同样存在：11,000 也可能高估（中置信）。** ICSG 2026Q1 过剩 396,000 吨是已发生的账面过剩[L-E03d5:106]；高盛 2026 预测本就是"回落"[L-E03cg:72]。若关税套利出清（"large metal flows to the US on speculation regarding tariffs"[^cu-oe]）、库存回流、委内瑞拉等事件性溢价消失，价格回落速度可能同样超出"温和均值回归"想象。**单点 11,000 的两个尾部（持续短缺→低估；过剩兑现+需求走弱→高估）都未处理。**

**发现 1.3e｜±20%→±10% 的对称线性敏感性掩盖尾部不对称（推理级）。** 深跌 20% 时高成本资产面临减产、减值与储量核销（期权价值损失），上涨 20% 时有未开发资源与扩产期权增益——NAV 对下行尾部的真实敏感度应大于上行。成本结构未披露，凸性无法计算，但这正是问题：**只给对称线性敏感性，等于没给尾部。**

[^icsg-rt]: ICSG predicts copper surplus for 2025. Recycling Today. 2025-05-02. https://www.recyclingtoday.com/news/icsg-copper-surplus-2025-rising-inventories-shanghai-china-recycling
[^icsg-am]: Global Refined Copper Market Expected to Move into Surplus. Asian Metal. https://wap.asianmetal.com/news/viewNews.am?nId=2318138
[^cu-mining]: Record copper price signals accelerating race for supplies. Mining.com. 2026-01-05. https://www.mining.com/web/record-copper-price-signals-accelerating-race-for-supplies
[^cu-oe]: Copper reaches two-month high of $14000 as inventories drop. OE Digital（energynews）. 2026-08-04. https://energynews.oedigital.com/mineral-resources/2026/08/04/copper-reaches-twomonth-high-of-14000-as-inventories-drop
[^cu-ob]: Copper Squeeze Broke, Price Held: Antofagasta. OpenBook Analytics. 2026-08-28. https://www.openbookanalytics.com/news/insights/copper-squeeze-broke-price-held-antofagasta （另：第三方 2026 铜价预测区间 $9,800-12,500/吨，Accio 聚合站，2026-08-24，https://www.accio.com/business/lme-copper-price-trend ，低信度仅作分散度参考）

---

## 2. 攻击二：成本曲线 90 分位法的失效场景

**发现 2.1｜M03 成稿与自家研究底稿相互矛盾（确定，内部证据）。**
- 成稿核心规则："核心规则：90分位现金成本线≈价格底部区域。"[L-M03cg:41]；"底由成本曲线决定，顶由需求脉冲决定"[L-M03cg:11]。
- 同一份计划的底稿却写："成本分位线不是铁底，只是「概率支撑」：2015-2016年铜价曾长时间运行在90分位成本线之下（亏损可以靠库存现金撑，减产滞后于价格），锂在2024-2025也出现过「击穿成本线后继续阴跌」"[L-M03d3:52]；"技术变革会让成本曲线整体下移"[L-M03d3:53]。
- 攻击：方法学论文（底稿）承认的失效场景，被成稿一句"≈价格地板"抹平。**这是同一份计划内部的口径不一致，红队只需指出，不需外援。**

**发现 2.2｜失效场景一：政策数量管制直接改写供给函数——印尼镍（高置信，外部证据）。**

| 关键数字/事实 | 逐字摘录 | 信度 | 时间窗 | 口径 |
|---|---|---|---|---|
| 2026 配额上限 | "Indonesia has lowered the 2026 nickel production quota cap to 250-260 million tons, down sharply from 379 million tons in 2025."[^ni-yieh] | 中-高 | 2025→2026 | RKAB 镍矿配额（湿吨） |
| 配额消耗进度 | "smelters consumed 120.6 million wmt of nickel ore during January–June 2026, equivalent to 46.2% of the 2026 RKAB quota"[^ni-smm26] | 高 | 2026-07-22 | 隐含 2026 配额约 261 百万吨，与上限互证 |
| 政策动机自认 | "Indonesia's National Economic Council (DEN): RKAB production cuts prove effective, nickel price rise significantly boosts state revenue."[^ni-den] | 高（官方表态转述） | 2025-03 | 配额减产的目标就是价格本身 |
| 监管口径 | "ESDM has repeatedly stated in public interviews that it will stabilize nickel prices…"[^ni-smm25] | 高 | 2025-03-04 | 能源矿产部公开表态 |
| 价格反应 | "Nickel prices soar on supply concerns amid Indonesia's RKAB uncertainty""Nickel prices rebound strongly above Yuan 120,000…"[^ni-ms-jan] | 中 | 2026-01-07 | 沪镍回升至 12 万元/吨上方 |

结论：当边际供给由**配额**而非 90 分位成本决定时，价格可以长期停在成本清算价之上（2024-2026 的镍），也可以在配额放开时跌穿清算价——成本曲线锚两头失效。镍的今日就是任何"战略金属"的明日，铜的出口管制与关税版本已在发生。

**发现 2.3｜失效场景二：金融与贸易流定价——2026 年铜"过剩+新高"并存（高置信）。** "large metal flows to the US on speculation regarding tariffs"[^cu-oe] + "LME backwardation hit $550 a tonne, LME inventories down around 14%"[^cu-ob] + ICSG 2026Q1 过剩 396,000 吨[L-E03d5:106]：同一时间窗内，**成本锚（90分位不变）与平衡表锚（过剩）都解释不了价格**——价格由关税套利、库存挪移与金融持仓决定。E03 自己也记下"现货升水207.50美元/吨 vs 过剩预测9.6万吨"的矛盾[L-E03d5:108]。90 分位法对此沉默。

**发现 2.4｜失效场景三：货币属性品种（中置信）。** 黄金价格 2026-01 逼近 5,600 美元/盎司后"倒V形"走弱[L-E03d5:73]，价格由央行购金与地缘需求驱动，与矿山成本几乎无关；学术侧 Erb-Harvey（FAJ 2013）的核心批判即黄金无现金流、无成本清算价可言[^erb]。对金用成本曲线定底是范畴错误。

**发现 2.5｜失效场景四：曲线整体移动与成本刚性（中置信，内部证据）。** "技术变革会让成本曲线整体下移"[L-M03d3:53]（锂云母提锂、铜浸出）；同期采矿工资成本刚性上行（"中国采矿工资143,361元排第6但增速1.9%倒数第三——成本刚性问题开始侵蚀矿山利润"[L-M03d3:16]）。用**静态**90 分位线抄底的人，可能被**移动的曲线**套住。

**发现 2.6｜操作规则的传导风险（高置信）。** D02 行动方案把方法写成了触发器："矿业窗口关闭（周期反转）｜E03 成本曲线法反向使用：窗口关闭=等下一轮90分位线"[L-D02:75]。若上述任一失效场景成立，该规则产生两类损失：**假信号**（跌到成本线=底部，实际继续阴跌，如锂 2024-2025）与**永不触发**（政策/金融驱动体制下价格回不到旧成本线，投资者在场外空转十年）。方法论文（底稿）给的是"概率支撑"，操作方案拿它当"铁底"，降级发生在从 research 到 成稿 的那一步。

**90分位法适用前提清单（红队建议随方法一并披露）**：①边际产能是利润最大化的私人主体；②无配额/禁令/出口管制等数量干预；③需求以工业属性为主；④市场一体化、无关税割裂；⑤技术与成本路径稳定。2026 年：铜违反④、镍违反②、金违反③、锂 2024-25 违反①②——**四个主要矿种同时处于前提失效状态，这本身就是必须写进 M03 的警示。**

[^ni-yieh]: Indonesia maintains strict nickel output cap despite RKAB revision window. Yieh.com. https://www.yieh.com/en/News/indonesia-maintains-strict-nickel-output-cap-despite-rkab-revision-window/161484
[^ni-smm26]: SMM: Indonesia's RKAB Quota Policy Remains Key Driver for Nickel Market. 2026-07-22. https://news.metal.com/newscontent/104017696-smm-nickel-flash-news-indonesias-rkab-quota-policy-remains-key-driver-for-nickel-market
[^ni-den]: Mysteel FLASH: Indonesia's National Economic Council (DEN): RKAB production cuts prove effective…（转载于印尼基准价新规分析页）. 2025-03-04. https://www.mysteel.net/analysis/5078661-indonesia-revises-regulations-on-mineral-benchmark-prices
[^ni-smm25]: SMM In-Depth Analysis: Impact of Numerous New Indonesian Policies on the Nickel Market. 2025-03-04. https://news.metal.com/newscontent/103207349
[^ni-ms-jan]: Mysteel FLASH: Indonesia's 2026 nickel ore RKAB quota reaches upper limit…（含 2026-01-07 镍价快讯）. 2026-06-24. https://www.mysteel.net/news/5129413
[^erb]: Erb C.B., Harvey C.R. The Golden Dilemma. Financial Analysts Journal, 69(4), 2013. https://rpc.cfainstitute.org/research/financial-analysts-journal/2013/the-golden-dilemma ；NBER Working Paper 18706: https://www.nber.org/system/files/working_papers/w18706/w18706.pdf

---

## 3. 攻击三：P04 三档模板

### 3.1 「100-年龄%权益」：经验法则被当作"解法"

**P04 原文**："解法：宽基被动为主+股债配置（100-年龄%）+阈值再平衡"[L-P04cg:12]；三档共同规则第2条"股债配置：权益比例≈100-年龄%"[L-P04cg:44]。

**发现 3.1a｜退休阶段实证方向相反（高置信——同行评议研究）。**
- Pfau & Kitces（Journal of Financial Planning, 2014-01，被引 91）："A steady or rising glide path provides superior results compared to starting at 60 percent equities and declining to 30 percent over time."[^pfau]
- Kitces（2013-09-25）："the research shows that rising glidepaths can be so effective, they may actually lead to lower average equity exposure throughout retirement"[^kitces13]
- Estrada（2015，国际数据检验）："Pfau and Kitces (2014) argue that a rising-equity glidepath lowers the probability of failure relative to a declining-equity glidepath."[^estrada]
- 攻击：100-年龄 是**单调递减**路径；在退休/临近退休阶段，主流实证支持**平稳或上升**（退休初期低权益、随余寿缩短回升）。P04 把一个对累积期大致成立的经验默认值，写成了全生命周期的"解法"，方向性错误发生在退休段。

**发现 3.1b｜无理论最优性，且中国语境未校准（推理级）。** 生命周期理论下最优权益比例取决于超额收益/方差与风险厌恶（Merton 框架）及人力资本性质，与年龄无必然线性关系；年轻家庭的人力资本偏"类债"，理论上支持更高初始权益而非机械公式。同时 P04d1 内部数据显示 A 股 2005-2025 年化约 6.8%（价格口径）[L-P04d1:6]——波动与回撤特征与美股不同，美式规则的参数未做本地化校准即进模板。
**公允性备注**：作为防手痒的默认纪律，100-年龄 并非无价值；红队攻击的是 P04 将其呈现为学术结论而非"未经论证的默认值"。

[^pfau]: Pfau W.D., Kitces C. Reducing Retirement Risk with a Rising Equity Glide Path. Journal of Financial Planning. 2014-01. https://www.financialplanningassociation.org/article/journal/JAN14-reducing-retirement-risk-rising-equity-glide-path
[^kitces13]: Kitces M. Should Equity Exposure Decrease In Retirement, Or Is A Rising Equity Glidepath Actually Better? 2013-09-25. https://www.kitces.com/blog/should-equity-exposure-decrease-in-retirement-or-is-a-rising-equity-glidepath-actually-better
[^estrada]: Estrada J. The Retirement Glidepath: An International Perspective. 2015. https://blog.iese.edu/jestrada/files/2015/08/Glidepath-2.pdf

### 3.2 黄金 10-15%：权重没有依据，只有后视镜

**P04 原文**："平衡档：宽基40%±+黄金10-15%+债30%+现金（目标4-6%）"[L-P04cg:57]；"进取档：宽基60-70%+黄金10%+行业主题≤10%"[L-P04cg:58]；行动方案直接执行："定投升级至平衡档（宽基40%±+黄金10-15%+债30%）"[L-D02:62]。

**发现 3.2a｜无依据引用（确定——检索范围内未发现任何支撑文献）。** 成稿与研究底稿的摘录中，10-15% 这个数没有对应任何优化研究或风险预算推导（P04 底稿是否另有出处见 §5 待证）。

**发现 3.2b｜研究区间严重分歧，10-15% 落在争议区上半段（高置信）。**
- 一端：In Gold We Trust 报告 2024 版"supports a gold allocation between 14% and 18% to enhance the Sharpe ratio of equity/bond portfolios"（USAGOLD 转述）[^igwt]（信度：中——二手转述报告）。
- 另一端：Erb & Harvey《The Golden Dilemma》（FAJ 69(4), 2013, 10-42，被引 343）[^erb]：黄金无现金流、价值锚是金价/CPI 比率的均值回归——最优权重对假设极敏感，不存在稳健的"共识区间"（该文具体比率数值本轮未逐字核对，见 §5）。
- 攻击：行业对"黄金该配多少"的答案横跨个位数到 18%，P04 恰好取了分歧区间的上半段而未说明取舍理由。

**发现 3.2c｜20 年年化 10.3% 是后视镜 + 幸存者起点（高置信）。** P04d1 自己的口径："伦敦金从2005年10月约469.9美元涨至2025年约3875美元高位（回调前），约8.2倍、年化约11.2%（美元），扣除人民币对美元约15.6%的累计升值后人民币口径年化约10.3%"[L-P04d1:7]。起点 2005 年 10 月是金价历史低位区；近端驱动（央行购金潮+地缘）正在退坡——E03 已录"2026年1月逼近5,600美元/盎司后「倒V形」走弱""央行购金节奏放缓被WGC归因于金价上涨本身（高位抑制买盘）"[L-E03d5:73]。**用一段正在退坡的非常态驱动外推静态权重，是教科书式 recency bias。**
**公允性备注**：中国低利率环境（P04 内部：存款 0.95%）降低无息资产的机会成本，黄金入档本身有分散证据支撑；攻击的是"10-15% 这个数"，不是"配黄金"这件事。

[^igwt]: USAGOLD. Research-Backed Insights On Gold Allocation For Risk-Conscious Investors. 2024-08-14. https://www.usagold.com/finding-balance-research-backed-insights-on-gold-allocation-for-risk-conscious-investors （转引 In Gold We Trust 2024 报告）

### 3.3 REITs：流动性与税费被低估

**发现 3.3a｜税收政策存在未定价空洞（高置信——政策原文）。**
- 财政部/税务总局公告 2022 年第 3 号（2022-01-28 发布）："原始权益人和项目公司不确认所得，不征收企业所得税""基础设施REITs设立阶段，原始权益人向基础设施REITs转让项目公司股权实现的资产转让评估增值，当期（可暂不缴纳企业所得税，允许递延至……）"[^tax-cls]；"对原始权益人按照战略配售要求自持的基础设施REITs份额对应的资产转让评估增值，允许递延至实际转让时缴纳企业所得税。"[^tax-waizi]
- 攻击：3 号公告只覆盖**设立前重组与设立环节**（递延性质，且"递延至实际转让时缴纳"意味着解禁减持时税负回归）；**运营环节（项目公司企业所得税等常规税负）与投资者环节的长期税收安排至今无专门文件**，学术侧也指出 REITs 税收优惠仍待制度化[^tax-iolaw]。P04 若按"现金分派率"对标无风险利率而未做税后口径与政策变动披露，则高估净回报（P04 成稿 REITs 段落原文本轮 grep 未命中，见 §5 待证）。

**发现 3.3b｜流动性折价：本轮未取得独立数据（空结果，如实申报）。** 两轮检索（"中证REITs指数 折价 成交清淡 流动性"、"公募REITs 折价 流动性 成交额"）均未返回可用来源。机制层面可确认的只有：战配自持份额对应资产转让评估增值"递延至实际转让时缴纳"[^tax-waizi]，说明战略配售份额存在锁定期、锁定期内不可流通；REITs 定价锚是底层资产现金流，对利率与出租率敏感。**折价率、成交额等数字本轮不引用任何未经核实的值**——该子项证据等级降为"机制推理"，是三个必答中最薄的一节，也是最高优先级的补课项（见 §6）。

[^tax-cls]: 税务总局发文明确基础设施领域不动产投资信托基金（REITs）试点税收政策（财联社转发）. 2022-01-28. https://m.cls.cn/detail/926740
[^tax-waizi]: 财政部 税务总局关于基础设施领域不动产投资信托基金（REITs）试点税收政策的公告（公告2022年第3号，全文转载）. 2022-02-14. https://www.waizi.org.cn/tax/128134.html
[^tax-iolaw]: REITs税收激励机制：课税原则与税收优惠. 中国法学网（中国社会科学院法学研究所）. 2022-01-13. http://iolaw.cssn.cn/zxzp/202201/t20220113_5388292.shtml

---

## 4. 修正清单（M03 / P04）

### 4.1 M03 修正清单（每条附验收标准）

| # | 修正项 | 内容 | 验收标准 |
|---|---|---|---|
| M03-1 | 储量口径表 | NAV 附录增加"储量/资源量分列 + 各资产适用规范（GB/T 17766-2020 / JORC 2012 / 当地规范）+ 推断资源量占比"；推断资源量单列并给价值折扣区间 | 任一海外资产可指出其 Competent Person 与适用规范；储量与全国口径不再同表混用 |
| M03-2 | 折现率敏感性 | 披露基准折现率区间与 ±1pp 敏感性矩阵（含国别风险溢价分档）；删除或改写"NAV的分歧从来不在折现率"[L-M03cg:23] | 敏感性表显示折现率 ±2pp 的影响 ≥ 价格 ±20% 的影响（约 ∓15-20%，见 §1.2b） |
| M03-3 | 铜价情景化 | 11,000 单点 → 三情景（如 9,000 / 11,000 / 14,000）概率加权 + 远期曲线对照 + 分资产盈亏平衡价；"市值隐含价"标注为 plug 逆运算而非验证 | 删除"NAV与市值吻合=定价准确"式表述[L-M03d1:6]，改为双向解读（§1.3c/1.3d 两个尾部都呈现） |
| M03-4 | 90分位法降格 | 成稿"90分位现金成本线≈价格底部区域"[L-M03cg:41] 加适用前提清单（§2 之①-⑤）；补失效案例（2015-16 铜长期破线、锂击穿后阴跌[L-M03d3:52]、2026 铜"过剩+新高"、印尼镍配额[^ni-yieh]） | D02:75 的操作规则加"失效豁免条款"；成稿与底稿口径一致（都叫"概率支撑"） |
| M03-5 | NAV 口径对账 | 8,700 亿 → −890 亿净债务 → 7,800 亿[L-M03d1:6] 的链条披露少数股东、租赁、或有负债处理；±20%→±10% 弹性给出成本结构依据 | 弹性可由外部读者用公开产量与成本假设复算 |

### 4.2 P04 修正清单

| # | 修正项 | 内容 | 验收标准 |
|---|---|---|---|
| P04-1 | 「100-年龄」降格 | 标注为"默认值"而非"解法"[L-P04cg:12]；附 Pfau-Kitces 退休期证据[^pfau]与 Merton 式替代；退休前后分段（累积期可保留，退休段改 U 型/上升型） | 文中出现学理争议标注与至少一条替代路径 |
| P04-2 | 黄金权重给依据 | 10-15% 附优化/风险预算来源；如无，改"2-10% + 专项论证"；标注 Erb-Harvey 无现金流批判[^erb]、金价高位与央行购金退坡[L-E03d5:73] | 权重数字可追溯到研究；recency 标注到位 |
| P04-3 | REITs 税后净收益 | 收益测算扣减：运营环节税负、投资者环节税收政策不确定性[^tax-cls][^tax-waizi]、锁定期与流动性假设；补折价率与成交额数据来源 | 分派率→税后净收益的换算表可复核 |
| P04-4 | 三档模板压力测试 | 用 1990s 日本 / 1970s 美国利率与通胀情景重跑三档达成率；"目标 4-6%/6-8%"给出资产级来源 | 三档预期收益有分资产推导（红队总榜已指出进取档 8% 上限缺推导的问题，本轮不重复展开） |

---

## 5. 待证项（未定位、值得跟进）

1. **M03 dive_01 全文的折现率与储量脚注**：本轮仅凭 grep 摘录断言"未披露"，需读全文确认。查法：read `research/M03-20261031/dive_01.md`。
2. **紫金官网"储量与资源量"页的数据截至日期与资源量列数值**：摘要截断。查法：打开 zjky.cn 页面全文。
3. **"现货顶格价14,449美元"**：M03 底稿自标待证[L-M03d3:9]；本轮仅旁证 2026-08-28 的 $14,424.50[^cu-ob]。查法：LME/Reuters 2026 年 9-10 月行情数据。
4. **C-REITs 折价率/成交额/战配锁定期细则**：两轮检索空结果（§3.3b）。查法：中证指数官网 REITs 板块、基金业协会统计、《公开募集基础设施证券投资基金指引（试行）》战配锁定条款。
5. **P04 成稿 REITs 段落原文**：grep 未在 P04 命中 REITs 行（任务简报认定 P04 含 REITs）。查法：read 第P04期全文。
6. **Erb-Harvey 的金价/CPI 比率具体数值**：本轮仅引用文献地位，未逐字核对数字。查法：Duke/ NBER PDF 全文。
7. **行业 WACC 外部锚（Damodaran 等）**：本轮未检索，折现率攻击以年金算术自足；如需外部锚可补 Damodaran 分行业 WACC 数据集。

## 6. 建议的下一步

1. 关闭 §5 的 1、5 两项（读 dive_01 与 P04 全文）——成本最低、直接决定 M03-2 与 P04-3 两条修正是否成立。
2. 如继续投入 M03：做紫金分板块（卡莫阿/巨龙/紫金铜业等）NAV 复算，检验"±20%→±10%"弹性是否可由公开数据复现；不可复现即坐实 M03-5。
3. 如继续投入 P04：先补 C-REITs 流动性一手数据（§5-4），再决定 REITs 在三档模板中的去留与权重。
4. 全景层面：把 §2 的"90分位法适用前提清单"作为 E03/M03/D02 三期的共享警示框，避免同一方法在三处被赋予不同强度。

---

*红队五 · 完。检索 12 次（web_search），本地计划文档引用均给出 文件:行号；两个尾部风险（§1.3c/1.3d）与三个内部矛盾（§0-1、§2.1、§4.2-P04-4）为本攻击的主承重结构。*
