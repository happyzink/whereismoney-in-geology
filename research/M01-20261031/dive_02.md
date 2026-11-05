## Dimension 02: 平台收租四种方式的单位经济

### Current State

- **佣金型（交易抽成/take rate）**：平台按GMV或单量抽成，收入≈GMV×佣金率，成本主要是履约与获客。美团外卖官方口径实际商户佣金仅6%-8%（配送费另计、大头付骑手）[^meituan-commission]；携程住宿预订综合佣金率8%-10%[^sina-ota-commission]。佣金型天花板=GMV增速×佣金率上限，受监管与商户承受力双重约束（美团外卖单均经营利润被测算在1元/单量级，靠佣金率+广告变现率+1P比例三因素抬升[^dfcfw-meituan-ue]）。
- **广告型（竞价/eCPM）**：平台把流量放入竞价队列，按eCPM=出价×预估点击率×预估转化率排序，收入≈曝光量×eCPM。头部平台吃「流量×变现率」双杠杆：字节2024年收入1550亿美元[^xueqiu-byteincome]，其中抖音国内广告约4200亿元人民币、TikTok广告超300亿美元[^lanjinger-social]。oCPM/GCPA等智能竞价把计费单位从曝光迁移到转化，实质是平台用算法承担了定向风险、换取更高eCPM[^zhihu-cpm]。
- **增值服务型（订阅/内购）**：向C端收「会员费」或向开发者/商家收「摊位+道具」。苹果App Store标准佣金30%、小微企业计划15%，2026年3月起中国市场标准佣金降至25%[^sina-apple-commission][^ifanr-apple15]；京东PLUS会员ARPU曾达非会员的10倍[^jd-plus-arpu]；Costco以低商品毛利+会员费盈利，会员费是利润的主体[^scharvest-costco]。
- **金融型（支付+小贷+理财导流分润）**：支付收通道费（微信支付普通商户默认费率约0.6%-1%[^huaweicloud-wxpay]），信贷与理财按撮合规模分润——蚂蚁微贷业务曾贡献近40%营收[^wallstreetcn-ant]，官方定位是连接2000+金融机构的平台化分润[^antgroup-official]。金融型单位经济=交易流水×净费率−资金成本−坏账，监管（资本金、断直连）直接压缩分润率。
- **毛利率排序（头部平台，2025年前后口径）**：游戏/虚拟增值（腾讯整体毛利率53%→56%[^qq-tencent2025]）＞广告（平台侧毛利高但买量成本上升）≈App Store佣金（近乎纯利但监管退坡）＞电商佣金（履约重、毛利低）＞金融（受资金成本与坏账拖累）。
- **护城河比较（判断，中置信）**：最抗竞争的是**双边网络效应+转换成本叠加的金融/支付型**（清算网络如Visa/Mastercard的交换费体系由卡组织与发卡行分润，挑战者需同时攻破双边网络[^mastercard-interchange]）；**最抗竞争且已验证规模的单一形态是游戏+广告双轮（腾讯）**——虚拟商品边际成本近零、社交关系链锁死用户。纯佣金型最易被「更低佣金率的挑战者+监管」侵蚀（拼多多2025年千亿惠商投入即是降租换增长[^xueqiu-pddq4]）。
- **模式演进信号**：拼多多2025Q4交易服务收入639亿元（+19%）首次超过在线营销服务收入（+5%），收租重心从广告转向交易抽成[^wallstreetcn-pddq4]。

### Key Evidence

| 数据点 | 数值 | 时间 | 原文摘录(逐字) | 自评信度 | 来源 |
|---|---|---|---|---|---|
| 美团外卖实际商户佣金 | 6%-8% | 2024-12-25 | 「一、美团外卖实际商户佣金为6%-8%　二、不同配送方式佣金有差异　三、美团从商户端获得的配送收入大部分用于支付骑手薪资」 | 高（平台官方口径） | [meituan.com新闻](https://www.meituan.com/news/NN241225051008799) |
| 美团外卖单均经营利润测算 | 1.12元/单（2025E） | 2021-06-21 | 「基于 2025 年1P 订单比例下降至60%的假设，2025 年美团外卖业务单均OP 有望提升至1.12 元/单，其中广告变现率提升贡献15%，佣金率提升贡献36」 | 中（卖方测算） | [东方财富PDF研报](https://pdf.dfcfw.com/pdf/H3_AP202106211499064377_1.pdf) |
| 携程住宿预订综合佣金率 | 8%-10% | 2025-11-28 | 「中泰证券研报数据显示，目前携程住宿预订业务综合佣金率在8%到10%。这也是携程多年以来维持的水平」 | 中（券商研报转引） | [新浪财经](https://finance.sina.com.cn/tech/csj/2025-11-28/doc-infyyanx9117803.shtml) |
| 携程2025核心OTA GMV与住宿收入 | GMV约1.1万亿元；住宿收入261亿 | 2026-02-28 | 「2025 年携程的核心 OTA 业务成交额约为1.1万亿元，其中机票业务贡献约5500亿元（占50%），住宿业务贡献约2800亿元（占25%）。但在收入端，住宿预订却以261亿」 | 中（媒体估算） | [DoNews](https://www.donews.com/article/detail/6279/97386.html) |
| 拼多多2025Q4交易服务收入超在线营销 | 交易服务639亿(+19%) vs 在线营销(+5%)；总营收1239亿(+12%) | 2025Q4（2026-03-25发布） | 「第四季度，拼多多营收同比增长12%至1239亿元，增速环比有所改善。其中，交易服务收入表现更为亮眼，同比增长19%至639亿元；在线营销服务收入同比增长5%至」 | 高（财报数字，媒体转述） | [华尔街见闻](https://wallstreetcn.com/articles/3768364) |
| App Store中国标准佣金下调 | 30%→25%（2026-03-15起） | 2026-03-13 | 「Apple App内购买及付费App的标准佣金率将由目前的30%改为25%。」 | 高（官方政策，媒体转述） | [新浪财经](https://finance.sina.com.cn/jjxw/2026-03-13/doc-inhqvamt7897270.shtml) |
| App Store小企业计划佣金 | 30%→15%（年收入<100万美元） | 2020-11-19 | 「若开发商在年内的收入低于100 万美元，那么他们的佣金抽成比例会从30%下调至15%」 | 高（官方政策，媒体转述） | [爱范儿](https://www.ifanr.com/1380165) |
| 中国App Store生态交易额与免佣比例 | 4万亿元；>95%免佣 | 2020→2025 | 「2020年，中国App Store生态系统促成的营业额和销售额达到近2万亿元人民币，到2025年已增长到4万亿元人民币。其中，超过95%的交易额无需向苹果」 | 中（苹果委托研究，媒体转述） | [凤凰网](https://feng.ifeng.com/c/8x44pw3nNRw) |
| 字节跳动2024年收入 | 1550亿美元(+29%)；净利润约330亿美元 | 2024财年（2025-04披露） | 「字节跳动在2024 年的收入增长了29%，达到 1550 亿美元（11314.07 亿人民币）；全年净利润小幅增长至约330 亿美元」 | 中（非上市公司，媒体/雪球转述） | [雪球](https://xueqiu.com/4926075175/331425840) |
| 抖音/TikTok广告收入估算 | 抖音国内4200亿元；TikTok超300亿美元（2025） | 2025 | 「2025 年TikTok的广告收入超300 亿美元。再加上抖音在国内4200亿元人民币的广告收入，字节的广告收入也有近千亿美元规模」 | 低-中（机构估算，未经公司确认） | [蓝鲸财经](https://www.lanjinger.com/d/1779430640059768554) |
| 腾讯2025年毛利率 | 53%→56%；毛利4225.93亿(+21%) | 2025年报（2026-03-18发布） | 「腾讯2025年全年收入达7517.66亿元……毛利4225.93亿元，同比增长21%，毛利率从53%提升至56%」 | 高（公司财报） | [腾讯新闻](https://news.qq.com/rain/a/20260318A07DR500) |
| 京东PLUS会员ARPU倍数 | PLUS会员ARPU为非PLUS的10倍（2021口径）；会员3400万（2023Q4） | 2021 / 2023Q4 | 「21年PLUS会员ARPU值是非PLUS会员的10倍」；「京东PLUS会员在籍会员数量截至四季度末达3400万」 | 中（平台自披露，宣传口径） | [京东PLUS白皮书](https://mtt.m.jd.com/article/articleView/6e37d1e2-a2c1-44c5-b600-398be66430b2.action?from=recommand)、[央广网](https://tech.cnr.cn/techph/20230309/t20230309_526177115.shtml) |
| 蚂蚁微贷收入占比 | 近40% | 2020-09 | 「微贷业务为蚂蚁集团贡献了近40%的营收，如今蚂蚁是中国最大的线上消费信贷和小微经营者信贷科技服务商」 | 高（招股阶段公开分析+官方数据） | [华尔街见闻](https://wallstreetcn.com/articles/3604465) |
| 微信支付商户费率 | 默认0.6%-1%，最低约0.2% | 2025-09 | 「普通商户默认费率通常在0.6%-1%，但通过服务商渠道，符合条件的商户」 | 中（服务商渠道信息，非官方原文） | [华为云社区](https://bbs.huaweicloud.com/blogs/461493) |
| Costco会员费盈利模式 | 商品低毛利+会员费为利润主体 | 2024-08 / 2025-03 | 「会员费利润占比高，返现对销售毛利率影响较小」；「Costco采用会员制和低毛利策略，依靠高销量和会员费实现盈利」 | 中（二手分析+媒体） | [世华资本](https://www.scharvestcap.com/research/info.aspx?itemid=4014)、[21经济网](https://www.21jingji.com/article/20250311/herald/2d604a0c879b0c101c81a4c74a631a63.html) |

[^meituan-commission]: 美团外卖的真实佣金比例究竟是多少？美团官方. 2024-12-25. https://www.meituan.com/news/NN241225051008799
[^dfcfw-meituan-ue]: UE模型视角下政策规则变化对美团外卖的短期与长期影响（东方财富研报PDF）. 2021-06-21. https://pdf.dfcfw.com/pdf/H3_AP202106211499064377_1.pdf
[^sina-ota-commission]: 酒旅不赚钱，都怪OTA？新浪财经. 2025-11-28. https://finance.sina.com.cn/tech/csj/2025-11-28/doc-infyyanx9117803.shtml
[^donews-ctrip]: 携程的"黄金时代". DoNews. 2026-02-28. https://www.donews.com/article/detail/6279/97386.html
[^wallstreetcn-pddq4]: 拼多多Q4营收同比增长12%，净利润下滑11%. 华尔街见闻. 2026-03-25. https://wallstreetcn.com/articles/3768364
[^sina-apple-commission]: 苹果公司宣布，3月15日起下调中国App Store佣金率至25%. 新浪财经. 2026-03-13. https://finance.sina.com.cn/jjxw/2026-03-13/doc-inhqvamt7897270.shtml
[^ifanr-apple15]: 苹果降低了App Store抽成，开发者们能赚更多钱了. 爱范儿. 2020-11-19. https://www.ifanr.com/1380165
[^ifeng-appstore-cn]: 2025年苹果中国App Store生态交易额达4万亿元. 凤凰网. 2026-10-08. https://feng.ifeng.com/c/8x44pw3nNRw
[^xueqiu-byteincome]: 字节跳动2024年收入增长29%至1550亿美元. 雪球. 2025-04-12. https://xueqiu.com/4926075175/331425840
[^lanjinger-social]: 全球社交的旧王与新王. 蓝鲸财经. 2026-05-24. https://www.lanjinger.com/d/1779430640059768554
[^zhihu-cpm]: 一分钟读懂广告投放各计费CPM、CPC等. 知乎专栏. https://zhuanlan.zhihu.com/p/146391463
[^qq-tencent2025]: 腾讯2025年营收超7500亿元，同比增长14%. 腾讯新闻. 2026-03-18. https://news.qq.com/rain/a/20260318A07DR500
[^jd-plus-arpu]: 京东PLUS白皮书V22-4. 京东麦头条. https://mtt.m.jd.com/article/articleView/6e37d1e2-a2c1-44c5-b600-398be66430b2.action?from=recommand
[^cnr-jdplus]: 京东PLUS会员达3400万. 央广网. 2023-03-09. https://tech.cnr.cn/techph/20230309/t20230309_526177115.shtml
[^wallstreetcn-ant]: 蚂蚁微贷的盔甲与软肋. 华尔街见闻. 2020-09-09. https://wallstreetcn.com/articles/3604465
[^antgroup-official]: 蚂蚁集团官网. https://www.antgroup.com/
[^huaweicloud-wxpay]: 微信支付0.2%费率商户号如何开通. 华为云社区. 2025-09-16. https://bbs.huaweicloud.com/blogs/461493
[^scharvest-costco]: Costco如何实现基业长青. 世华资本. 2024-08-19. https://www.scharvestcap.com/research/info.aspx?itemid=4014
[^21jingji-costco]: 主打低价的Costco，盯上了有钱人的生意. 21经济网. 2025-03-11. https://www.21jingji.com/article/20250311/herald/2d604a0c879b0c101c81a4c74a631a63.html
[^mastercard-interchange]: Mastercard Interchange Fees and Rates Explained. Mastercard官网. https://www.mastercard.com/us/en/business/support/merchant-interchange-rates.html
[^xueqiu-pddq4]: 拼多多2025年四季度业绩会实录. 雪球. 2026-03-25. https://xueqiu.com/7949779229/381152654

### Tensions & Counter-arguments

- **佣金率口径之争**：美团自称实际佣金6%-8%，但商户体感为「技术服务费+履约服务费+点金推广」合计20%上下；官方口径剔除了配送与广告。佣金型平台普遍用「窄口径佣金」回应「宽口径抽成」批评，比较跨平台take rate时必须统一口径（是否含履约、是否含广告）。
- **「拼多多交易服务收入超广告」≠租金刚性增强**：交易服务收入增长部分来自百亿补贴/多多买菜等自营相关与全托管模式（自营成分毛利远低于纯佣金），2025年公司同步推出千亿惠商降费[^xueqiu-pddq4]，即「收租品类扩张+降租换量」并行，不能直接读成变现率上行。
- **广告型eCPM高毛利的反例**：字节2025年海外营收+50%但净利润下滑超70%[^tmtpost-byte]，说明广告型单位经济在大规模AI/算力资本开支下并非无懈可击；eCPM竞价红利随流量大盘增速放缓而摊薄。
- **App Store佣金护城河被监管持续侵蚀**：中国标准佣金30%→25%（2026-03）[^sina-apple-commission]、欧盟DMA下开放侧载、超95%中国区生态交易额免佣[^ifeng-appstore-cn]——「纯佣金近零边际成本」的模型正被政策单边压低take rate，且苹果委托研究报告口径（4万亿生态交易额）有美化动机。
- **金融型「最抗竞争」的脆弱面**：蚂蚁案例表明监管（资本金要求、断直连、利率上限）可以在一夜之间重写金融分润的单位经济；其「近40%营收来自微贷」[^wallstreetcn-ant]是2020年IPO前口径，与今日合规框架不可直接比。
- **待证项**：①美团/滴滴最新（2025-2026）单均UE的官方口径拆分（佣金vs广告vs履约）——建议查两家最新季报管理层点评；②Visa/Mastercard最新财年毛利率（约80%量级，常被引用但本期未逐字核实）——建议查10-K原文；③游戏内购（米哈游/腾讯游戏）具体分成案例的流水与分成比例一手数据。

[^tmtpost-byte]: 字节跳动：一场利润的"假摔". 钛媒体. 2026-04-24. https://www.tmtpost.com/7964717.html
