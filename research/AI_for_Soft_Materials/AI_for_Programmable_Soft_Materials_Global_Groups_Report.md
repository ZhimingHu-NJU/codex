# 面向智能形变高分子材料的 AI for Soft Materials 国际课题组调研报告

> 资料来源说明：本报告基于公开实验室主页、学校/机构官网、论文主页、PubMed/PMC/arXiv、期刊 DOI 页面和官方新闻整理；每个课题组的来源集中列于第 3 节和 CSV 表格。若机构/职务在 2026 年前后发生变化，报告以 2026-06-05 可检索公开信息为准，并在不确定处标注“待核实”。

## 1. Executive Summary

AI for Materials 正从“用机器学习预测少数无机晶体性质”扩展为“数据、模拟、自动化实验、机器视觉、机器人和生成式模型共同组成的材料研发闭环”。这一变化对无机晶体、催化、电池和光伏材料非常明显，但对你的研究方向而言，更合适的切入点并不是泛泛地追随“AI 发现新材料”，而是聚焦 **AI for Soft Materials / Polymer Informatics / Intelligent Actuators**：以高分子配方、交联网络、液晶取向、刺激响应、器件几何和动态形变为核心对象，构建从材料分子到软执行器性能的可学习关系。

为什么不能只看无机晶体材料发现？第一，无机晶体通常具有明确化学计量、晶体结构和 DFT 可计算属性，数据结构相对规整；而 LCE、智能高分子和软执行器具有多组分配方、合成历史、交联密度、取向方式、制膜/打印工艺、热/光/电刺激边界条件和器件几何等多层变量。第二，无机材料 AI 常以带隙、形成能、离子电导、吸附能等静态或准静态性质为目标；你的方向需要预测和优化的是驱动应变、曲率、响应时间、恢复时间、力输出、疲劳寿命、自感知信号、循环稳定性和仿生运动轨迹。第三，LCE 与软执行器的关键数据往往来自视频、图像、偏光显微、热台实验、循环驱动曲线和器件级测试，而不是单纯来自晶体数据库。因此你的方向应将机器视觉、实验视频数据库、闭环制备和器件评价作为特色。

国际上可分为五条路线：其一是 Ramprasad、Nagata、Ferguson、de Pablo 代表的 polymer informatics / soft-material simulation 路线，解决高分子结构—性能预测、聚合物数据库和软材料机理模拟问题；其二是 Aspuru-Guzik、Abolhasani、Warren、Shijing Sun 代表的 self-driving lab 路线，解决自动化合成、在线表征、贝叶斯优化和主动学习闭环；其三是 Gómez-Bombarelli、Buehler、Walsh/Ganose 代表的生成式设计路线，解决分子、材料组成和仿生结构的逆向生成；其四是 Kozinsky、Ceriotti、Ferguson、de Pablo、Buehler 代表的 ML potentials 与多尺度模拟路线，解决原子/分子尺度动力学、相变和结构—性能解释；其五是 Rothemund、Pikul、Seelecke/Rizzello、Shea、Katzschmann 代表的 soft actuator / soft robotics 路线，解决执行器结构、软机器人、人工肌肉、控制和性能评价。

与 LCE、人工肌肉和柔性执行器最相关的不是单一路线，而是几条路线的组合：材料端学习 Polymer Genome 和 NIMS/Nick Warren 的聚合物自动化；机理端学习 Ferguson/de Pablo 的软材料模拟和液晶物理；平台端学习 Matter Lab、Abolhasani 和 Shijing Sun 的自驱动实验室；结构端学习 Buehler/Shea 的生成式结构设计；应用端学习 Katzschmann、Rothemund、Pikul 和 Saarland 的软执行器建模控制。你的潜在定位可写为：**面向智能形变高分子材料的 AI 辅助分子—配方—取向—结构协同设计，结合机器视觉驱动表征和贝叶斯闭环优化，实现 LCE/人工肌肉/柔性执行器的可编程制备与性能提升。** 这个定位避开了泛泛的 AI for Materials，也不是简单复制 Polymer Genome 或无机材料自驱动实验室，而是把软材料动态形变和器件闭环作为核心科学问题。

## 2. 国际发展路线图谱

### 2.1 Polymer Informatics 路线

Polymer informatics 的核心不是“把已有机器学习算法套到高分子上”，而是解决高分子本身难以结构化表达的问题：重复单元、共聚比例、端基、分子量分布、交联密度、结晶/取向状态、加工历史和环境条件都会影响性能。Ramprasad 的 Polymer Genome 路线最系统，强调数据平台、结构表示、物性预测、逆向筛选和实验验证。对 LCE 来说，最重要的启发是建立专用数据结构：单体/介晶基元、柔性间隔链、交联剂、手性/偶氮/导电/离子基团、配比、聚合方式、取向方式、固化条件、Tg/Tni、序参量、模量、驱动应变、响应速度、疲劳寿命和器件几何必须同时记录。

Yuuya Nagata 和 Nick Warren 代表了 polymer informatics 与自动化聚合物实验的结合。Nagata 在 NIMS 明确提出机器人实验、机器学习和信息科学结合的自主聚合物创成；Warren 则展示了自驱动实验室可用于聚合物合成，尤其是乳液聚合和功能聚合物构筑单元。这比很多无机材料 SDL 更接近 LCE，因为 LCE 的“候选空间”主要是配方、合成工艺和后处理，而不是晶体结构枚举。Ferguson 和 de Pablo 则补足软材料物理：LCE 的宏观形变来自微观取向、相变、网络弹性和缺陷结构，仅靠黑箱模型很难外推，必须借助统计热力学、分子模拟、粗粒化模型和机器学习增强采样。

### 2.2 Self-driving Lab 路线

Self-driving laboratory 的基本闭环是 design–make–test–learn：算法提出实验，机器人执行制备，在线/离线表征得到数据，模型更新并推荐下一轮实验。Matter Lab 和 Acceleration Consortium 提供了国际上最完整的生态范式；Abolhasani 提供模块化、低体积、在线流体平台的工程样例；Nick Warren 将 SDL 推进到聚合物合成；Shijing Sun 强调材料加速平台的可复用架构和社区实践。

迁移到 LCE 时，闭环不应照搬无机薄膜或钙钛矿流程，而应设计为：配方推荐 → 微量混合/涂布/打印/光取向/热固化 → 偏光显微或光谱检查取向 → 热/光/电刺激下视频表征 → 机器视觉提取曲率、应变、响应/恢复时间和循环衰减 → 贝叶斯优化推荐下一组配方、取向和几何。第一阶段可以半自动，而不是一开始追求全机器人。真正的创新点在于“动态形变视频数据进入闭环”，这也是区别于多数 self-driving inorganic labs 的关键。

### 2.3 Generative Design 路线

生成式材料设计可分为分子生成、配方生成、结构生成和器件生成。Gómez-Bombarelli 的 VAE/逆向分子设计适合迁移到可聚合介晶、偶氮苯光响应单体、可导电/离子化侧链和可动态交联单体的设计。Buehler 的图推理、扩散模型和三维仿生结构生成适合迁移到 LCE 可编程取向图案、折纸/曲面执行器和层级结构设计。Walsh/Ganose 的强项在材料表示、计算工作流和 AI 模型互操作，虽然对象偏无机，但可为 LCE 数据平台提供方法借鉴。

需要注意，生成式 AI 在 LCE 中不应被写成“生成一种新材料”这么宽泛，而应绑定明确输出：生成一组满足 Tg/Tni/驱动温度约束的单体组合；生成一张二维 director field 使薄膜加热后形成目标曲面；生成一种多层/多材料执行器几何以达到目标弯曲角和力输出；生成实验条件以最大化循环稳定性。

### 2.4 Machine Learning Potentials and Multiscale Simulation 路线

Kozinsky 和 Ceriotti 代表机器学习原子模拟的先进方法，包括等变神经网络势、不确定性量化、主动学习、原子环境描述符和无监督结构分析。这些方法对 LCE 的价值在于解释局部相互作用、介晶堆积、柔性链段动力学、界面相容性和相变行为。但它们不能直接给出宏观执行器弯曲角，因为 LCE 的驱动跨越从原子到网络、薄膜、结构和外场的多个尺度。因此建议把 ML potentials 定位为“机理解释和模拟数据增强”而不是主平台。

更可执行的多尺度路线是：用小分子/低聚物模拟计算介晶相互作用、偶氮光异构化能垒或链段柔性；用粗粒化/有限元模型描述取向网络和热致收缩；用机器学习把配方—取向—几何映射到驱动性能；用实验视频校准模型。Ferguson、de Pablo 和 Buehler 的软材料/多尺度模拟可在这个桥接中发挥作用。

### 2.5 Soft Actuator / Soft Robotics 路线

Rothemund、Pikul、Seelecke/Rizzello、Shea 和 Katzschmann 的价值在于提醒你：LCE 不是只发表材料合成，而应进入执行器指标体系。Rothemund 的电液软执行器强调功率密度、速度、能效和模块化；Pikul 强调软传感和可变形表面；Saarland 强调智能材料执行器的模型化、自感知与控制；Shea 强调计算设计和可制造结构；Katzschmann 强调人工肌肉、软机器人、机器视觉闭环制造和学习控制。

这条路线与 AI 的结合空间包括：机器视觉自动提取执行器运动参数；基于贝叶斯优化的配方/几何/取向联合优化；基于仿真和实验数据的 surrogate model；基于强化学习或模型预测控制的软机器人控制；基于生成式模型的仿生形态设计。对你的方向来说，软执行器路线应作为“应用端对标”，而 Polymer Informatics 和 SDL 作为“方法端对标”。
## 3. 重点课题组逐一分析

### Rampi Ramprasad / Ramprasad Group / Polymer Genome

* 所在学校/机构：Georgia Institute of Technology
* 国家/地区：美国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://ramprasad.mse.gatech.edu/
* 研究关键词：Polymer Genome; polymer informatics; polyBERT; graph neural networks; polymer dielectric; materials AI
* 主要研究方向：以机器学习、量子计算和高通量数据建立聚合物结构—性能模型，发展 Polymer Genome 与 Matmerize 平台，面向介电、力学、热、光电和可持续聚合物进行逆向设计。
* 代表性成果：Polymer Genome 平台、polyBERT 聚合物语言模型、多任务 GNN、AI 设计可合成/可回收/耐久聚合物与高能量密度介电聚合物。
* 代表性论文 / 平台 / 软件 / 数据库：Polymer Genome; polyBERT; Polymer informatics with multi-task learning; Polymer informatics at-scale with multitask graph neural networks; Informatics framework for sustainable polymers
* 使用的 AI 方法：分子/聚合物指纹、图神经网络、多任务学习、语言模型、贝叶斯/主动筛选、可合成性约束逆向设计
* 是否涉及实验自动化或闭环优化：否/以计算平台为主
* 是否涉及高分子或软材料：是；soft/robotics：间接
* 是否涉及 LCE、液晶、执行器或软机器人：中高：可直接借鉴 LCE 单体、液晶基元、交联密度、Tni/Tg、驱动应变等数据库和结构—性能预测框架。；柔性执行器相关性：中：材料端强，器件端需结合软机器人/机器视觉。
* 与我未来方向的相关性：这是聚合物信息学最接近“AI 辅助 LCE 配方设计”的国际标杆，可学习数据库、描述符、模型验证和产业化路径。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：必须重点学习
* 可靠来源链接：https://ramprasad.mse.gatech.edu/ ; https://www.nature.com/articles/s41578-021-00383-3 ; https://arxiv.org/abs/2209.13557 ; https://arxiv.org/abs/2303.12938 ; https://arxiv.org/abs/2409.15354

### Yuuya Nagata / Autonomous Polymer Design and Discovery Group

* 所在学校/机构：National Institute for Materials Science (NIMS)
* 国家/地区：日本
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://www.nims.go.jp/group/autonomous/index_en.html
* 研究关键词：autonomous polymer discovery; synthesis robot; NIMO; Bayesian optimization; polymer chemistry
* 主要研究方向：建设集成合成机器人、机器学习和信息科学的自主高分子设计、合成与评价系统。
* 代表性成果：NIMS 新建自主高分子创成团队，引入 Chemspeed 自动合成机器人，并计划与 Bayesian optimization program NIMO 联动。
* 代表性论文 / 平台 / 软件 / 数据库：Autonomous Polymer Design and Discovery Group; NIMS SAMURAI profile; NIMO Bayesian optimization program（平台信息）
* 使用的 AI 方法：贝叶斯优化、实验自动化、机器人合成、数据回流、信息化学
* 是否涉及实验自动化或闭环优化：是
* 是否涉及高分子或软材料：是；soft/robotics：间接
* 是否涉及 LCE、液晶、执行器或软机器人：高：对象就是高分子，流程可迁移到 LCE 交联网络/制膜条件探索。；柔性执行器相关性：中高：若加入机器视觉表征即可转为执行器闭环优化。
* 与我未来方向的相关性：比无机自驱动实验室更贴近“聚合物合成—表征—优化”，是 LCE 小型闭环平台的重要参考。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：必须重点学习
* 可靠来源链接：https://www.nims.go.jp/group/autonomous/index_en.html ; https://samurai.nims.go.jp/profiles/nagata_yuuya?locale=en ; https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=201401033751489408

### Andrew Ferguson / Ferguson Lab

* 所在学校/机构：University of Chicago
* 国家/地区：美国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://www.ferglab.com/
* 研究关键词：soft materials; molecular simulation; machine learning; statistical thermodynamics; enhanced sampling
* 主要研究方向：用统计热力学、分子模拟、高性能计算和机器学习理解并工程化分子与软材料，强调自组装、生物/仿生软材料和增强采样。
* 代表性成果：机器学习集体变量发现、增强采样、软/生物材料数据驱动设计综述。
* 代表性论文 / 平台 / 软件 / 数据库：Data-Driven Design and Autonomous Experimentation in Soft and Biological Materials Engineering; Machine learning for collective variable discovery and enhanced sampling
* 使用的 AI 方法：深度学习/流形学习、增强采样、自由能估计、主动/自动实验综述方法
* 是否涉及实验自动化或闭环优化：方法综述/非主线
* 是否涉及高分子或软材料：部分；soft/robotics：是
* 是否涉及 LCE、液晶、执行器或软机器人：中：更偏计算软物质，可迁移到液晶相变、网络构象和驱动自由能景观。；柔性执行器相关性：中：偏材料机理而非器件。
* 与我未来方向的相关性：适合为 LCE 多尺度模拟、少数据学习和机理解释提供计算理论支撑。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：高度相关
* 可靠来源链接：https://www.ferglab.com/ ; https://chemistry.uchicago.edu/andrew-ferguson ; https://pubmed.ncbi.nlm.nih.gov/35236085/

### Juan de Pablo / de Pablo Group / UChicago PME

* 所在学校/机构：University of Chicago
* 国家/地区：美国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://pme.uchicago.edu/faculty/juan-de-pablo
* 研究关键词：polymers; liquid crystals; molecular simulation; complex materials; soft matter
* 主要研究方向：聚合物、液晶和复杂软材料的分子模拟、理论与工程设计，关注液晶界面、取向、有序结构和复杂材料。
* 代表性成果：液晶界面微观结构、可自主运动液晶/活性液晶系统、聚合物物理和软物质模拟。
* 代表性论文 / 平台 / 软件 / 数据库：Research reveals inner workings of liquid crystals; Controlling chaos in liquid crystals; polymer physics/simulation publications
* 使用的 AI 方法：分子模拟、统计力学、部分机器学习/计算材料方法
* 是否涉及实验自动化或闭环优化：否
* 是否涉及高分子或软材料：是；soft/robotics：是
* 是否涉及 LCE、液晶、执行器或软机器人：高：液晶和聚合物直接相关，是 LCE 取向、界面和相变机理的核心对标。；柔性执行器相关性：中高：液晶驱动和活性行为对 LCE 执行器有机理启发。
* 与我未来方向的相关性：在“液晶+聚合物+软物质模拟”上与 LCE 最近，虽不是典型 AI 组，但对机制建模不可替代。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：必须重点学习
* 可靠来源链接：https://pme.uchicago.edu/faculty/juan-de-pablo ; https://news.uchicago.edu/story/research-reveals-inner-workings-liquid-crystals ; https://pme.uchicago.edu/news/controlling-chaos-liquid-crystals-gaining-precision-autonomous-technologies

### Alán Aspuru-Guzik / Matter Lab / Acceleration Consortium

* 所在学校/机构：University of Toronto
* 国家/地区：加拿大
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://www.matter.toronto.edu/
* 研究关键词：self-driving laboratory; AI chemistry; robotics; molecular materials; Acceleration Consortium
* 主要研究方向：以 AI、量子化学、机器人和自驱动实验室加速分子与材料发现，牵头 Acceleration Consortium。
* 代表性成果：自驱动实验室概念和生态建设、化学/材料自动化平台、视觉感知机器人、AI 分子发现。
* 代表性论文 / 平台 / 软件 / 数据库：Self-driving Lab subgroup; Acceleration Consortium; k-agents for self-driving laboratories
* 使用的 AI 方法：贝叶斯优化、主动学习、强化学习、自动化表征、计算机视觉、代理系统
* 是否涉及实验自动化或闭环优化：是
* 是否涉及高分子或软材料：部分；soft/robotics：间接
* 是否涉及 LCE、液晶、执行器或软机器人：中：平台范式强，但对象多为分子/功能材料；需要把 make-test-analyze 改成 LCE 制膜/取向/驱动表征。；柔性执行器相关性：中
* 与我未来方向的相关性：自驱动实验室国际影响力最高之一，适合作为闭环平台、组织模式和国际合作的标杆。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：必须重点学习
* 可靠来源链接：https://www.matter.toronto.edu/basic-content-page/self-driving-lab ; https://acceleration.utoronto.ca/ ; https://www.chemistry.utoronto.ca/news/media-u-t%E2%80%99s-acceleration-consortium-changing-way-do-scienceprofessor-al%C3%A1n-aspuru-guzik

### Milad Abolhasani / Abolhasani Research Group / Self-Driving Fluidic Lab

* 所在学校/机构：North Carolina State University
* 国家/地区：美国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://www.abolhasanilab.com/
* 研究关键词：self-driving fluidic lab; microfluidics; flow chemistry; closed-loop optimization; AlphaFlow
* 主要研究方向：发展流体微处理器、自驱动实验室、连续流合成和在线表征，用 AI 进行闭环材料优化。
* 代表性成果：自驱动流体实验室、钙钛矿纳米晶自主掺杂、AlphaFlow、SDL 综述和 ARPA-E human-AI-robot 平台。
* 代表性论文 / 平台 / 软件 / 数据库：Autonomous Nanocrystal Doping by Self-Driving Fluidic Micro-Processors; AlphaFlow; Self-driving labs interview/reviews
* 使用的 AI 方法：闭环贝叶斯优化、强化学习、代理模型、在线传感、高通量流动实验
* 是否涉及实验自动化或闭环优化：是
* 是否涉及高分子或软材料：间接；soft/robotics：间接
* 是否涉及 LCE、液晶、执行器或软机器人：中高：微流控/流动配方、在线表征和闭环优化可迁移到 LCE 配方、涂布、光固化和薄膜制备。；柔性执行器相关性：中高：平台理念可迁移到执行器制备—视频表征闭环。
* 与我未来方向的相关性：非常适合学习“低成本模块化闭环实验平台”的工程架构。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：必须重点学习
* 可靠来源链接：https://www.abolhasanilab.com/ ; https://news.ncsu.edu/2022/03/self-driving-lab/ ; https://cbe.ncsu.edu/accelerating-discovery-2/ ; https://engr.ncsu.edu/news/2026/04/20/nc-state-receives-funding-to-advance-self-driving-laboratory-research/

### Nick Warren / Warren Group / Polymer Self-driving Lab

* 所在学校/机构：University of Sheffield
* 国家/地区：英国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://www.sheffield.ac.uk/cmbe/people/academic-staff/nick-warren
* 研究关键词：AI-powered polymer synthesis; emulsion polymerization; self-driving laboratory; sustainable polymers
* 主要研究方向：聚合物合成、胶体/乳液聚合、自动化反应平台和机器学习驱动聚合物优化。
* 代表性成果：闭环自优化乳液聚合平台，自动反应、产品分析并用机器学习调整条件；用于绿色聚合物和 PFPA 功能聚合物构筑单元。
* 代表性论文 / 平台 / 软件 / 数据库：Self-driving labs: making chemical research faster and smarter; closed-loop self-optimization of emulsion polymers; PFPA autonomous synthesis
* 使用的 AI 方法：机器学习优化、多目标优化、自动化反应、在线/离线分析
* 是否涉及实验自动化或闭环优化：是
* 是否涉及高分子或软材料：是；soft/robotics：间接
* 是否涉及 LCE、液晶、执行器或软机器人：高：聚合物自动化合成对象与 LCE 材料端高度接近。；柔性执行器相关性：中高：可迁移到执行器材料配方窗口探索。
* 与我未来方向的相关性：在“自驱动实验室 + 聚合物合成”交叉点上特别相关，优先级高于许多无机材料 SDL。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：必须重点学习
* 可靠来源链接：https://www.sheffield.ac.uk/cmbe/news/self-driving-labs-making-chemical-research-faster-and-smarter ; https://www.sheffield.ac.uk/cmbe/people/academic-staff/nick-warren ; https://phys.org/news/2025-05-labs-enable-faster-smarter-polymer.pdf

### Shijing Sun / Sun Group / Autonomous Materials Discovery

* 所在学校/机构：University of Cambridge
* 国家/地区：英国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://www.msm.cam.ac.uk/people/sun
* 研究关键词：autonomous materials discovery; materials acceleration platforms; high-throughput experiments; ML-guided diagnosis
* 主要研究方向：机器学习、高通量实验和自驱动平台用于能源/功能材料发现，关注材料加速平台的实用化和社区最佳实践。
* 代表性成果：高通量光伏材料开发与机器学习诊断，自主实验室社区综述，MAP-E 等材料加速平台。
* 代表性论文 / 平台 / 软件 / 数据库：Accelerating Photovoltaic Materials Development via High-Throughput Experiments and ML-assisted Diagnosis; Autonomous laboratories survey; MAP-E
* 使用的 AI 方法：主动学习、贝叶斯优化、高通量数据诊断、自动化平台、数字孪生
* 是否涉及实验自动化或闭环优化：是
* 是否涉及高分子或软材料：否/较少；soft/robotics：较少
* 是否涉及 LCE、液晶、执行器或软机器人：中：对象偏能源材料，但平台规划、实验设计和评价指标可借鉴。；柔性执行器相关性：中
* 与我未来方向的相关性：适合学习 MAP/SDL 的组织、指标和社区实践；对象需大幅软材料化。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：方法值得借鉴
* 可靠来源链接：https://www.msm.cam.ac.uk/people/sun ; https://arxiv.org/abs/1812.01025 ; https://www.cambridge.org/engage/api-gateway/coe/assets/orp/resource/item/65e0ce79e9ebbb4db993d6fe/original/autonomous-laboratories-for-accelerated-materials-discovery-a-community-survey-and-practical-insights.pdf

### Rafael Gómez-Bombarelli / Learning Matter Lab

* 所在学校/机构：Massachusetts Institute of Technology
* 国家/地区：美国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://gomezbombarelli.mit.edu/
* 研究关键词：generative models; inverse design; organic materials; polymers; molecular simulation
* 主要研究方向：融合数据科学、工程、DFT/MD 等物理模拟和机器学习，在复杂组合空间中设计有机电子、储能聚合物/分子和催化材料。
* 代表性成果：VAE/生成模型分子设计、分子材料逆向设计、聚合物和有机功能材料筛选。
* 代表性论文 / 平台 / 软件 / 数据库：Automatic chemical design using a data-driven continuous representation of molecules; Learning Matter research; generative/inverse design materials
* 使用的 AI 方法：VAE、生成模型、图模型、主动学习、物理模拟+ML、逆向设计
* 是否涉及实验自动化或闭环优化：部分
* 是否涉及高分子或软材料：部分/是；soft/robotics：间接
* 是否涉及 LCE、液晶、执行器或软机器人：中高：适合迁移到液晶单体、交联剂、光响应基元和可聚合介晶的生成式设计。；柔性执行器相关性：中：材料分子端强，器件端需另建。
* 与我未来方向的相关性：能帮助把 LCE 从“经验配方”推进到“目标性能驱动的分子/单体生成”。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：高度相关
* 可靠来源链接：https://gomezbombarelli.mit.edu/ ; https://mrl.mit.edu/node/337 ; https://ilp.mit.edu/read/G%C3%B3mez-Bombarelli

### Markus J. Buehler / Laboratory for Atomistic and Molecular Mechanics

* 所在学校/机构：Massachusetts Institute of Technology
* 国家/地区：美国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://web.mit.edu/mbuehler/www/research/
* 研究关键词：generative AI; bioinspired materials; multiscale mechanics; graph reasoning; 3D structures
* 主要研究方向：多尺度材料力学、仿生材料、生成式 AI、知识图谱和结构设计，连接分子、材料层级结构与力学性能。
* 代表性成果：基于语言/图/扩散模型的 3D 仿生结构生成，图推理促进材料创新，多尺度材料设计课程与框架。
* 代表性论文 / 平台 / 软件 / 数据库：Generating 3D architectured nature-inspired materials using diffusion models; graph-based AI model maps the future of innovation; Bioinspired123D
* 使用的 AI 方法：生成式 AI、知识图谱、多模态 LLM、扩散模型、图神经/图推理、多尺度模拟
* 是否涉及实验自动化或闭环优化：否
* 是否涉及高分子或软材料：部分；soft/robotics：间接/仿生结构强
* 是否涉及 LCE、液晶、执行器或软机器人：中：不是 LCE 专家，但可借鉴可编程取向图案、三维结构和仿生执行器几何生成。；柔性执行器相关性：中高：结构设计与可编程形变高度相关。
* 与我未来方向的相关性：适合作为“AI + 仿生结构 + 多尺度力学”的方法标杆，不宜照搬其宏大生成式叙事。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：高度相关
* 可靠来源链接：https://web.mit.edu/mbuehler/www/research/ ; https://news.mit.edu/2024/graph-based-ai-model-maps-future-innovation-1112 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC9767007/

### Aron Walsh / Alex Ganose / Materials Design / AI for Materials

* 所在学校/机构：Imperial College London
* 国家/地区：英国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://www.imperial.ac.uk/materials/research/ai-for-materials/
* 研究关键词：AI for materials; computational materials design; generative AI; workflows; electronic materials
* 主要研究方向：计算材料设计、AI 材料模型、数据/工作流和可解释材料发现，主要面向无机/能源/功能材料。
* 代表性成果：材料模型共享表示空间、计算材料设计和材料数据工作流，Alex Ganose 参与开源材料工具与电子结构分析。
* 代表性论文 / 平台 / 软件 / 数据库：Imperial AI for materials theme; AI models common language; computational materials design papers/tools
* 使用的 AI 方法：图模型、表示学习、生成式 AI、自动化计算工作流、可解释 ML
* 是否涉及实验自动化或闭环优化：部分
* 是否涉及高分子或软材料：较少；soft/robotics：较少
* 是否涉及 LCE、液晶、执行器或软机器人：低中：对象远，但模型互操作、表示学习和计算工作流值得借鉴。；柔性执行器相关性：低中
* 与我未来方向的相关性：适合学习 AI for Materials 工具链和表征学习，但不应作为 LCE 方向主要对标。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：方法值得借鉴
* 可靠来源链接：https://www.imperial.ac.uk/materials/research/ai-for-materials/ ; https://www.imperial.ac.uk/news/articles/engineering/materials/2026/imperial-study-finds-ai-models-share-a-common-language-for-materials-/ ; https://aronwalsh.github.io/

### Shyue Ping Ong / Materials Virtual Lab

* 所在学校/机构：UC San Diego（用户名单写 NUS，需核实；当前公开主页为 UCSD）
* 国家/地区：美国/新加坡籍学者
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://materialsvirtuallab.org/
* 研究关键词：materials informatics; pymatgen; atomate; matminer; Materials Project; workflows
* 主要研究方向：材料信息学、自动化第一性原理工作流、数据库、pymatgen/atomate/matminer 等开源工具。
* 代表性成果：pymatgen 创始/维护、Materials Project 早期基础设施、Materials Virtual Lab 工具链。
* 代表性论文 / 平台 / 软件 / 数据库：pymatgen; matminer; atomate2; Materials Project API
* 使用的 AI 方法：特征工程、工作流自动化、数据挖掘、计算数据库、机器学习模型
* 是否涉及实验自动化或闭环优化：否
* 是否涉及高分子或软材料：否/少；soft/robotics：否/少
* 是否涉及 LCE、液晶、执行器或软机器人：低中：对象偏无机，但数据结构、API、工作流管理对自建 LCE 数据平台极有用。；柔性执行器相关性：低中
* 与我未来方向的相关性：学习如何把材料数据、计算、模型和软件变成可复用基础设施。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：方法值得借鉴
* 可靠来源链接：https://materialsvirtuallab.org/ ; https://pymatgen.org/ ; https://www.sciencedirect.com/science/article/pii/S0927025618303252

### Boris Kozinsky / Materials Intelligence Research Group

* 所在学校/机构：Harvard University
* 国家/地区：美国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://mir.g.harvard.edu/
* 研究关键词：machine learning potentials; NequIP; Allegro; FLARE; active learning; atomistic simulation
* 主要研究方向：第一性原理、机器学习势、主动学习和大规模分子动力学，研究复杂材料的输运、反应和界面动力学。
* 代表性成果：NequIP/Allegro 等等变神经网络势，FLARE Bayesian force fields，十亿原子级反应动力学模拟。
* 代表性论文 / 平台 / 软件 / 数据库：MIR group; NequIP/Allegro/FLARE; unified ML potential energy/polarization models
* 使用的 AI 方法：等变神经网络势、Gaussian process/Bayesian force fields、主动学习、不确定性量化、大规模 MLMD
* 是否涉及实验自动化或闭环优化：否
* 是否涉及高分子或软材料：部分；soft/robotics：间接
* 是否涉及 LCE、液晶、执行器或软机器人：中：可用于 LCE 单体/界面/链段微观相互作用，但距离器件尺度远。；柔性执行器相关性：低中
* 与我未来方向的相关性：适合学习原子尺度模型如何与主动学习结合；对 LCE 需粗粒化/多尺度桥接。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：方法值得借鉴
* 可靠来源链接：https://mir.g.harvard.edu/people/boris-kozinsky ; https://mir.g.harvard.edu/people/open-positions ; https://www.mrsec.harvard.edu/pages/news-2025-nsf-mrsec-Modeling-electric-response-of-materials.php

### Michele Ceriotti / Laboratory of Computational Science and Modelling (COSMO)

* 所在学校/机构：EPFL
* 国家/地区：瑞士
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://cosmo.epfl.ch/
* 研究关键词：machine learning atomic simulation; atomistic modelling; statistical mechanics; SOAP; ML potentials
* 主要研究方向：发展统计力学、机器学习和原子尺度模拟方法，用于分子和材料结构—性能关系。
* 代表性成果：SOAP/原子环境表示、无监督原子模拟分析、ML 原子尺度模型综述、COSMO 工具与方法。
* 代表性论文 / 平台 / 软件 / 数据库：Machine learning at the atomic-scale; Beyond potentials; Unsupervised machine learning in atomistic simulations
* 使用的 AI 方法：原子环境描述符、核方法、无监督学习、ML 势、结构表示、统计采样
* 是否涉及实验自动化或闭环优化：否
* 是否涉及高分子或软材料：部分；soft/robotics：间接
* 是否涉及 LCE、液晶、执行器或软机器人：中：可借鉴分子/介晶局部结构表征和相变分析，不是直接执行器方向。；柔性执行器相关性：低中
* 与我未来方向的相关性：是机器学习原子模拟方法论标杆，适合作为 LCE 分子模拟的底层方法库。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：方法值得借鉴
* 可靠来源链接：https://people.epfl.ch/michele.ceriotti?lang=en ; https://www.epfl.ch/labs/cosmo/ ; https://arxiv.org/abs/2012.04616 ; https://arxiv.org/abs/2208.06139

### Philipp Rothemund / Functional Soft Robotic Matter

* 所在学校/机构：University of Stuttgart
* 国家/地区：德国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://www.iams.uni-stuttgart.de/institute/team/Rothemund/
* 研究关键词：electrohydraulic soft actuators; HASEL; soft robotic matter; energy efficiency; modeling
* 主要研究方向：功能软机器人材料、电液软执行器、软静电执行器能效、可重构高速机器人模块和软机器人智能控制。
* 代表性成果：可降解电液执行器、六边形电液模块、高频软逻辑门、软执行器能效模型。
* 代表性论文 / 平台 / 软件 / 数据库：Biodegradable electrohydraulic actuators; Hexagonal electrohydraulic modules; Physical control in soft robotics; soft electrostatic actuator energy efficiency
* 使用的 AI 方法：建模优化、物理控制，AI 使用不是主线
* 是否涉及实验自动化或闭环优化：否
* 是否涉及高分子或软材料：是/弹性体；soft/robotics：是
* 是否涉及 LCE、液晶、执行器或软机器人：中：不是 LCE，但软执行器性能指标、能效、模块化器件设计非常可迁移。；柔性执行器相关性：高
* 与我未来方向的相关性：执行器端标杆，可帮助定义 LCE 人工肌肉的性能评价和器件架构。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：高度相关
* 可靠来源链接：https://www.iams.uni-stuttgart.de/institute/team/Rothemund/ ; https://www.science.org/doi/10.1126/scirobotics.adl3546 ; https://doi.org/10.1073/pnas.2527676123

### Kevin Pikul / Pikul Research Group

* 所在学校/机构：University of Wisconsin–Madison
* 国家/地区：美国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://pikulgroup.engr.wisc.edu/
* 研究关键词：soft actuators; soft sensors; shape transformable materials; visuotactile sensing; bioinspired surfaces
* 主要研究方向：软执行器、软传感、仿生可变形表面、可编程形变材料和机器人材料。
* 代表性成果：章鱼/头足类启发形变表面，软执行器与传感器，RGB/ToF/触觉融合软传感。
* 代表性论文 / 平台 / 软件 / 数据库：Soft Actuators and Sensors; electroadhesive clutches; multimodal visuotactile sensor
* 使用的 AI 方法：建模、传感数据处理、机器人感知；ML 不是主线但可结合机器视觉
* 是否涉及实验自动化或闭环优化：否
* 是否涉及高分子或软材料：是/弹性体；soft/robotics：是
* 是否涉及 LCE、液晶、执行器或软机器人：中高：形变表面、软传感和仿生执行器指标适合 LCE 器件迁移。；柔性执行器相关性：高
* 与我未来方向的相关性：与“人工肌肉/自感知软执行器”应用端高度契合，可对标器件评价。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：高度相关
* 可靠来源链接：https://pikulgroup.engr.wisc.edu/research/soft-actuators-and-sensors/ ; https://pikulgroup.engr.wisc.edu/ ; https://scholar.google.com/citations?user=waC_84EAAAAJ

### Stefan Seelecke / Gianluca Rizzello / Intelligent Material Systems Lab / Smart Material Systems

* 所在学校/机构：Saarland University
* 国家/地区：德国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://imsl.de/
* 研究关键词：dielectric elastomer actuators; smart materials; actuator modelling; self-sensing control; soft robotics
* 主要研究方向：智能材料执行器/传感器、介电弹性体人工肌肉、模型化设计、自感知控制和软机器人。
* 代表性成果：三维介电弹性体软触手机器人项目、软聚合物圆顶模型优化、可变刚度 DEA 交互控制。
* 代表性论文 / 平台 / 软件 / 数据库：DEA SOFT ROBOTS SPP2100; Model-Based Design Optimization of Soft Polymeric Domes; Robust interaction control of DEA
* 使用的 AI 方法：物理建模、系统辨识、优化控制、自感知控制；ML 可作为增强工具
* 是否涉及实验自动化或闭环优化：否
* 是否涉及高分子或软材料：是；soft/robotics：是
* 是否涉及 LCE、液晶、执行器或软机器人：中高：同属智能聚合物执行器，建模/自感知控制对 LCE 人工肌肉很有用。；柔性执行器相关性：高
* 与我未来方向的相关性：非常适合作为智能材料驱动、建模、控制和自感知方向对标。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：高度相关
* 可靠来源链接：https://www.spp2100.de/project/dea-soft-robots ; https://publikationen.sulb.uni-saarland.de/bitstream/20.500.11880/31799/1/actuators-10-00209-v2.pdf ; https://arxiv.org/abs/2112.10440

### Kristina Shea / Computational Design Laboratory

* 所在学校/机构：ETH Zurich
* 国家/地区：瑞士
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://cdl.ethz.ch/
* 研究关键词：computational design; generative design; optimization; computational fabrication; 4D printing
* 主要研究方向：交互式设计、几何处理、计算制造、工程设计计算和结构优化。
* 代表性成果：计算设计实验室、生成式设计、可制造结构与机器人结构，涉及 4D printing 和软机器人相关设计。
* 代表性论文 / 平台 / 软件 / 数据库：Computational Design Laboratory; generative design/4D printing works; ETH Engineering Design and Computing
* 使用的 AI 方法：优化算法、生成式设计、几何处理、仿真驱动设计
* 是否涉及实验自动化或闭环优化：否
* 是否涉及高分子或软材料：部分；soft/robotics：部分
* 是否涉及 LCE、液晶、执行器或软机器人：中：取向图案、几何结构、4D 打印路径和可编程结构设计可迁移。；柔性执行器相关性：中高
* 与我未来方向的相关性：对“材料—结构—器件一体化设计”的计算设计层很有价值。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：方法值得借鉴
* 可靠来源链接：https://cdl.ethz.ch/ ; https://ethz.ch/en/the-eth-zurich/organisation/who-is-who/mavt/details.MjI4NzY=.TGlzdC8xNTg0LDIwNDExODE0NTg=.html ; https://en.wikipedia.org/wiki/Kristina_Shea

### Robert Katzschmann / Soft Robotics Lab

* 所在学校/机构：ETH Zurich
* 国家/地区：瑞士
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://srl.ethz.ch/
* 研究关键词：soft robotics; artificial muscles; soft robot fabrication; vision-controlled jetting; control and learning
* 主要研究方向：软机器人、生物混合机器人、电/流体驱动、建模控制和机器学习算法，强调仿生机器与人工肌肉。
* 代表性成果：vision-controlled jetting 复合机器人打印、静音人工肌肉、软机器人建模控制和学习。
* 代表性论文 / 平台 / 软件 / 数据库：Vision-controlled jetting for composite systems and robots; NCCR SRL; modular soft robotic fish
* 使用的 AI 方法：机器视觉闭环制造、模型/无模型控制、机器学习控制、仿真优化
* 是否涉及实验自动化或闭环优化：部分（制造闭环）
* 是否涉及高分子或软材料：是/软材料；soft/robotics：是
* 是否涉及 LCE、液晶、执行器或软机器人：高：虽非 LCE 材料本体，但机器视觉闭环打印和人工肌肉应用端非常契合。；柔性执行器相关性：高
* 与我未来方向的相关性：是“机器视觉 + 软机器人制造 + 人工肌肉应用”的重要对标，可补足 Polymer Genome 的器件端短板。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：必须重点学习
* 可靠来源链接：https://srl.ethz.ch/ ; https://robert.katzschmann.de/ ; https://www.nature.com/articles/s41586-023-06684-3 ; https://nccr-robotics.ch/laboratory/soft-robotics-lab/

### Timothy Swager / The Swager Group

* 所在学校/机构：Massachusetts Institute of Technology
* 国家/地区：美国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://swagergroup.mit.edu/
* 研究关键词：polymer sensing materials; conducting polymers; chemical sensors; Bayesian optimization; continuous flow
* 主要研究方向：功能高分子、分子/纳米线传感、导电聚合物和 CNT 化学传感，近年结合连续流与贝叶斯优化。
* 代表性成果：分子线/导电聚合物传感放大、聚合物包覆 CNT 传感器、连续流+贝叶斯优化甲烷传感材料。
* 代表性论文 / 平台 / 软件 / 数据库：Continuous Flow Chemistry and Bayesian Optimization for Polymer-Functionalized CNT Methane Sensors; Molecular and Nanowire Based Sensors; Sensor Technologies Empowered by Materials and Molecular Innovations
* 使用的 AI 方法：贝叶斯优化、主动学习、连续流参数优化、传感信号分析
* 是否涉及实验自动化或闭环优化：部分
* 是否涉及高分子或软材料：是；soft/robotics：部分/柔性传感
* 是否涉及 LCE、液晶、执行器或软机器人：中：不是 LCE，但环境响应、自感知和柔性传感材料高度相关。；柔性执行器相关性：中高：可为自感知 LCE 执行器提供传感材料思路。
* 与我未来方向的相关性：适合将 LCE 执行器从“形变材料”拓展为“环境响应/自感知器件”。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：高度相关
* 可靠来源链接：https://swagergroup.mit.edu/research ; https://swagergroup.mit.edu/research/molecular-and-nanowire-based-sensors/ ; https://swagergroup.mit.edu/continuous-flow-chemistry-and-bayesian-optimization-polymer-functionalized-carbon-nanotube-based

### Timothy J. White / White Research Group

* 所在学校/机构：University of Colorado Boulder
* 国家/地区：美国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://www.colorado.edu/lab/white/
* 研究关键词：liquid crystal elastomers; 4D printing; photomechanical materials; soft actuators; programmable shape change
* 主要研究方向：LCE、液晶网络、光/热响应形变、4D 打印和可编程软材料。
* 代表性成果：LCE 4D 打印、光响应聚合物网络、可编程形变结构和软执行器。
* 代表性论文 / 平台 / 软件 / 数据库：Liquid Crystal Elastomers and Networks; 4D printed LCE actuators; photomechanical LCN/LCE works
* 使用的 AI 方法：AI 不是主线；可作为领域数据源和器件对标
* 是否涉及实验自动化或闭环优化：否
* 是否涉及高分子或软材料：是；soft/robotics：是
* 是否涉及 LCE、液晶、执行器或软机器人：极高：LCE 直接核心。；柔性执行器相关性：高
* 与我未来方向的相关性：虽然不是 AI 组，但作为 LCE/4D 打印执行器领域核心组，应作为数据集和应用指标来源。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：必须重点学习（补充）
* 可靠来源链接：https://www.colorado.edu/lab/white/ ; https://www.colorado.edu/mechanical/timothy-white ; https://scholar.google.com/citations?user=Jq2TzQwAAAAJ

### Ryan C. Hayward / Hayward Group

* 所在学校/机构：University of Colorado Boulder
* 国家/地区：美国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://www.colorado.edu/lab/hayward/
* 研究关键词：responsive polymers; hydrogel; liquid crystal elastomers; shape morphing; soft materials
* 主要研究方向：刺激响应高分子、水凝胶、LCE/LCN、薄膜不稳定性和可编程形变软材料。
* 代表性成果：响应性聚合物图案化、形变薄膜、光/热响应软材料、软材料力学。
* 代表性论文 / 平台 / 软件 / 数据库：responsive polymer and LCE/LCN shape morphing papers; Hayward group research
* 使用的 AI 方法：AI 不是主线；适合作为物理机制和数据来源
* 是否涉及实验自动化或闭环优化：否
* 是否涉及高分子或软材料：是；soft/robotics：是
* 是否涉及 LCE、液晶、执行器或软机器人：极高：LCE/响应性软材料直接相关。；柔性执行器相关性：高
* 与我未来方向的相关性：对 LCE 形变机理、响应高分子和机器视觉可量化指标最直接；AI 需由你引入。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：必须重点学习（补充）
* 可靠来源链接：https://www.colorado.edu/lab/hayward/ ; https://www.colorado.edu/chbe/ryan-hayward ; https://scholar.google.com/citations?user=q4vQm2EAAAAJ

### Arri Priimagi / Smart Photonic Materials / Priimagi Group

* 所在学校/机构：Tampere University
* 国家/地区：芬兰
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://research.tuni.fi/spm/
* 研究关键词：photoresponsive liquid crystal networks; light-driven actuators; azobenzene; soft robotics; photonics
* 主要研究方向：光响应液晶网络、偶氮苯材料、光驱动软执行器、可编程光子软材料。
* 代表性成果：光驱动 LCN/LCE 执行器、光控软机器人与液晶网络形变。
* 代表性论文 / 平台 / 软件 / 数据库：Smart Photonic Materials group; azobenzene LCN actuators; light-fueled soft robotics works
* 使用的 AI 方法：AI 不是主线；适合作为光驱动 LCE/LCN 数据源
* 是否涉及实验自动化或闭环优化：否
* 是否涉及高分子或软材料：是；soft/robotics：是
* 是否涉及 LCE、液晶、执行器或软机器人：极高：光响应 LCN/LCE 直接相关。；柔性执行器相关性：高
* 与我未来方向的相关性：如果你的 LCE 包含光响应/取向图案，该组比多数泛 AI 组更接近研究对象。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：必须重点学习（补充）
* 可靠来源链接：https://research.tuni.fi/spm/ ; https://www.tuni.fi/en/arri-priimagi ; https://scholar.google.com/citations?user=xZA4VjwAAAAJ

### Sergei Kalinin / AI for Autonomous Experiments / Microscopy

* 所在学校/机构：University of Tennessee / ORNL background
* 国家/地区：美国
* 所在院系：公开信息见主页；若无院系信息则待核实。
* 实验室主页：https://mse.utk.edu/people/sergei-kalinin/
* 研究关键词：autonomous microscopy; physics-informed AI; automated experiments; image analysis; active learning
* 主要研究方向：AI 驱动的自主显微表征、物理约束机器学习、主动实验和图像数据分析。
* 代表性成果：自主扫描探针/电子显微实验、材料图像分析和闭环表征。
* 代表性论文 / 平台 / 软件 / 数据库：autonomous microscopy and physics-informed ML publications; SDL perspective papers
* 使用的 AI 方法：主动学习、强化学习、物理约束 ML、计算机视觉、自动表征
* 是否涉及实验自动化或闭环优化：是（表征端）
* 是否涉及高分子或软材料：较少；soft/robotics：较少
* 是否涉及 LCE、液晶、执行器或软机器人：中：可迁移到偏光显微、热台视频、形变图像和闭环表征策略。；柔性执行器相关性：中高
* 与我未来方向的相关性：对“机器视觉表征与闭环优化”部分非常有帮助，尽管材料对象常偏无机/显微。
* 可以直接学习的地方：数据字段定义、实验/模拟/表征闭环、可迁移的 AI 方法和性能评价指标。
* 可以借鉴但不宜照搬的地方：若对象偏无机/能源/分子，应避免照搬材料对象和评价指标；若对象偏软机器人，应避免忽略 LCE 化学与取向网络。
* 推荐关注等级：方法值得借鉴（补充）
* 可靠来源链接：https://mse.utk.edu/people/sergei-kalinin/ ; https://www.ornl.gov/staff-profile/sergei-v-kalinin ; https://scholar.google.com/citations?user=-cuxoSQAAAAJ

## 4. 横向对比表

> 推荐优先级和排名均为“非官方排名，为基于方向相关性和领域影响力的综合判断”。

| 推荐优先级 | 教授/课题组 | 单位 | 核心方向 | AI 方法 | 是否偏高分子/软材料 | 是否有自动化实验 | 是否有数据库/平台 | 是否接近 LCE/执行器 | 对我方向的启发 |
| ----- | ------ | -- | ---- | ----- | ---------- | -------- | --------- | ------------ | ------- |
| 必须重点学习 | Rampi Ramprasad / Ramprasad Group / Polymer Genome | Georgia Institute of Technology | Polymer Genome | 分子/聚合物指纹、图神经网络、多任务学习、语言模型、贝叶斯/主动筛选、可合成性约束逆向设计 | 是 | 否/以计算平台为主 | 是 | 中高：可直接借鉴 LCE 单体、液晶基元、交联密度、Tn | 这是聚合物信息学最接近“AI 辅助 LCE 配方设计”的国际标杆，可学习数据库、描述 |
| 必须重点学习 | Yuuya Nagata / Autonomous Polymer Design and Discovery Group | National Institute for Materials Science (NIMS) | autonomous polymer discovery | 贝叶斯优化、实验自动化、机器人合成、数据回流、信息化学 | 是 | 是 | 是 | 高：对象就是高分子，流程可迁移到 LCE 交联网络/制膜 | 比无机自驱动实验室更贴近“聚合物合成—表征—优化”，是 LCE 小型闭环平台的重要参 |
| 高度相关 | Andrew Ferguson / Ferguson Lab | University of Chicago | soft materials | 深度学习/流形学习、增强采样、自由能估计、主动/自动实验综述方法 | 部分 | 方法综述/非主线 | 部分 | 中：更偏计算软物质，可迁移到液晶相变、网络构象和驱动自由 | 适合为 LCE 多尺度模拟、少数据学习和机理解释提供计算理论支撑。 |
| 必须重点学习 | Juan de Pablo / de Pablo Group / UChicago PME | University of Chicago | polymers | 分子模拟、统计力学、部分机器学习/计算材料方法 | 是 | 否 | 部分 | 高：液晶和聚合物直接相关，是 LCE 取向、界面和相变机 | 在“液晶+聚合物+软物质模拟”上与 LCE 最近，虽不是典型 AI 组，但对机制建模 |
| 必须重点学习 | Alán Aspuru-Guzik / Matter Lab / Acceleration Consortium | University of Toronto | self-driving laboratory | 贝叶斯优化、主动学习、强化学习、自动化表征、计算机视觉、代理系统 | 部分 | 是 | 部分 | 中：平台范式强，但对象多为分子/功能材料；需要把 mak | 自驱动实验室国际影响力最高之一，适合作为闭环平台、组织模式和国际合作的标杆。 |
| 必须重点学习 | Milad Abolhasani / Abolhasani Research Group / Self-Driving Fluidic Lab | North Carolina State University | self-driving fluidic lab | 闭环贝叶斯优化、强化学习、代理模型、在线传感、高通量流动实验 | 间接 | 是 | 是 | 中高：微流控/流动配方、在线表征和闭环优化可迁移到 LC | 非常适合学习“低成本模块化闭环实验平台”的工程架构。 |
| 必须重点学习 | Nick Warren / Warren Group / Polymer Self-driving Lab | University of Sheffield | AI-powered polymer synthesis | 机器学习优化、多目标优化、自动化反应、在线/离线分析 | 是 | 是 | 部分 | 高：聚合物自动化合成对象与 LCE 材料端高度接近。 | 在“自驱动实验室 + 聚合物合成”交叉点上特别相关，优先级高于许多无机材料 SDL。 |
| 方法值得借鉴 | Shijing Sun / Sun Group / Autonomous Materials Discovery | University of Cambridge | autonomous materials discovery | 主动学习、贝叶斯优化、高通量数据诊断、自动化平台、数字孪生 | 否/较少 | 是 | 部分 | 中：对象偏能源材料，但平台规划、实验设计和评价指标可借鉴 | 适合学习 MAP/SDL 的组织、指标和社区实践；对象需大幅软材料化。 |
| 高度相关 | Rafael Gómez-Bombarelli / Learning Matter Lab | Massachusetts Institute of Technology | generative models | VAE、生成模型、图模型、主动学习、物理模拟+ML、逆向设计 | 部分/是 | 部分 | 部分 | 中高：适合迁移到液晶单体、交联剂、光响应基元和可聚合介晶 | 能帮助把 LCE 从“经验配方”推进到“目标性能驱动的分子/单体生成”。 |
| 高度相关 | Markus J. Buehler / Laboratory for Atomistic and Molecular Mechanics | Massachusetts Institute of Technology | generative AI | 生成式 AI、知识图谱、多模态 LLM、扩散模型、图神经/图推理、多尺度模拟 | 部分 | 否 | 部分 | 中：不是 LCE 专家，但可借鉴可编程取向图案、三维结构 | 适合作为“AI + 仿生结构 + 多尺度力学”的方法标杆，不宜照搬其宏大生成式叙事。 |
| 方法值得借鉴 | Aron Walsh / Alex Ganose / Materials Design / AI for Materials | Imperial College London | AI for materials | 图模型、表示学习、生成式 AI、自动化计算工作流、可解释 ML | 较少 | 部分 | 部分 | 低中：对象远，但模型互操作、表示学习和计算工作流值得借鉴 | 适合学习 AI for Materials 工具链和表征学习，但不应作为 LCE 方 |
| 方法值得借鉴 | Shyue Ping Ong / Materials Virtual Lab | UC San Diego（用户名单写 NUS，需核实；当前公开主页为 UCSD） | materials informatics | 特征工程、工作流自动化、数据挖掘、计算数据库、机器学习模型 | 否/少 | 否 | 是 | 低中：对象偏无机，但数据结构、API、工作流管理对自建  | 学习如何把材料数据、计算、模型和软件变成可复用基础设施。 |
| 方法值得借鉴 | Boris Kozinsky / Materials Intelligence Research Group | Harvard University | machine learning potentials | 等变神经网络势、Gaussian process/Bayesian force fields、主动学习、不确定性量化、大规模 MLMD | 部分 | 否 | 部分 | 中：可用于 LCE 单体/界面/链段微观相互作用，但距离 | 适合学习原子尺度模型如何与主动学习结合；对 LCE 需粗粒化/多尺度桥接。 |
| 方法值得借鉴 | Michele Ceriotti / Laboratory of Computational Science and Modelling (COSMO) | EPFL | machine learning atomic simulation | 原子环境描述符、核方法、无监督学习、ML 势、结构表示、统计采样 | 部分 | 否 | 部分 | 中：可借鉴分子/介晶局部结构表征和相变分析，不是直接执行 | 是机器学习原子模拟方法论标杆，适合作为 LCE 分子模拟的底层方法库。 |
| 高度相关 | Philipp Rothemund / Functional Soft Robotic Matter | University of Stuttgart | electrohydraulic soft actuators | 建模优化、物理控制，AI 使用不是主线 | 是/弹性体 | 否 | 部分 | 中：不是 LCE，但软执行器性能指标、能效、模块化器件设 | 执行器端标杆，可帮助定义 LCE 人工肌肉的性能评价和器件架构。 |
| 高度相关 | Kevin Pikul / Pikul Research Group | University of Wisconsin–Madison | soft actuators | 建模、传感数据处理、机器人感知；ML 不是主线但可结合机器视觉 | 是/弹性体 | 否 | 部分 | 中高：形变表面、软传感和仿生执行器指标适合 LCE 器件 | 与“人工肌肉/自感知软执行器”应用端高度契合，可对标器件评价。 |
| 高度相关 | Stefan Seelecke / Gianluca Rizzello / Intelligent Material Systems Lab / Smart Material Systems | Saarland University | dielectric elastomer actuators | 物理建模、系统辨识、优化控制、自感知控制；ML 可作为增强工具 | 是 | 否 | 部分 | 中高：同属智能聚合物执行器，建模/自感知控制对 LCE  | 非常适合作为智能材料驱动、建模、控制和自感知方向对标。 |
| 方法值得借鉴 | Kristina Shea / Computational Design Laboratory | ETH Zurich | computational design | 优化算法、生成式设计、几何处理、仿真驱动设计 | 部分 | 否 | 部分 | 中：取向图案、几何结构、4D 打印路径和可编程结构设计可 | 对“材料—结构—器件一体化设计”的计算设计层很有价值。 |
| 必须重点学习 | Robert Katzschmann / Soft Robotics Lab | ETH Zurich | soft robotics | 机器视觉闭环制造、模型/无模型控制、机器学习控制、仿真优化 | 是/软材料 | 部分（制造闭环） | 部分 | 高：虽非 LCE 材料本体，但机器视觉闭环打印和人工肌肉 | 是“机器视觉 + 软机器人制造 + 人工肌肉应用”的重要对标，可补足 Polymer |
| 高度相关 | Timothy Swager / The Swager Group | Massachusetts Institute of Technology | polymer sensing materials | 贝叶斯优化、主动学习、连续流参数优化、传感信号分析 | 是 | 部分 | 是 | 中：不是 LCE，但环境响应、自感知和柔性传感材料高度相 | 适合将 LCE 执行器从“形变材料”拓展为“环境响应/自感知器件”。 |
| 必须重点学习（补充） | Timothy J. White / White Research Group | University of Colorado Boulder | liquid crystal elastomers | AI 不是主线；可作为领域数据源和器件对标 | 是 | 否 | 部分 | 极高：LCE 直接核心。 | 虽然不是 AI 组，但作为 LCE/4D 打印执行器领域核心组，应作为数据集和应用指 |
| 必须重点学习（补充） | Ryan C. Hayward / Hayward Group | University of Colorado Boulder | responsive polymers | AI 不是主线；适合作为物理机制和数据来源 | 是 | 否 | 部分 | 极高：LCE/响应性软材料直接相关。 | 对 LCE 形变机理、响应高分子和机器视觉可量化指标最直接；AI 需由你引入。 |
| 必须重点学习（补充） | Arri Priimagi / Smart Photonic Materials / Priimagi Group | Tampere University | photoresponsive liquid crystal networks | AI 不是主线；适合作为光驱动 LCE/LCN 数据源 | 是 | 否 | 部分 | 极高：光响应 LCN/LCE 直接相关。 | 如果你的 LCE 包含光响应/取向图案，该组比多数泛 AI 组更接近研究对象。 |
| 方法值得借鉴（补充） | Sergei Kalinin / AI for Autonomous Experiments / Microscopy | University of Tennessee / ORNL background | autonomous microscopy | 主动学习、强化学习、物理约束 ML、计算机视觉、自动表征 | 较少 | 是（表征端） | 部分 | 中：可迁移到偏光显微、热台视频、形变图像和闭环表征策略。 | 对“机器视觉表征与闭环优化”部分非常有帮助，尽管材料对象常偏无机/显微。 |

## 5. 最值得我关注的课题组排名

> 以下所有排名均为“非官方排名，为基于方向相关性和领域影响力的综合判断”。

### 5.1 按与“AI for Soft Materials / LCE / 柔性执行器”相关性排名（前 10）

1. **Rampi Ramprasad**：聚合物信息学、Polymer Genome 和 polyBERT 是建立 LCE 数据库与预测模型的最直接方法来源。
2. **Yuuya Nagata**：自主高分子设计与合成机器人直接面向聚合物，最接近 LCE 配方闭环。
3. **Nick Warren**：自驱动聚合物合成平台，优先级高于多数无机材料 SDL。
4. **Juan de Pablo**：液晶和聚合物模拟直接关联 LCE 取向、界面和相变。
5. **Robert Katzschmann**：人工肌肉、软机器人与视觉闭环制造对执行器端极其重要。
6. **Timothy J. White**：LCE/4D 打印核心数据源，虽然 AI 不是主线。
7. **Ryan Hayward**：响应高分子和 LCE 形变机理核心对标。
8. **Arri Priimagi**：光响应 LCN/LCE 和光驱动执行器高度相关。
9. **Milad Abolhasani**：模块化自驱动流体实验室可迁移到软材料配方—表征闭环。
10. **Stefan Seelecke / Gianluca Rizzello**：智能材料执行器建模、自感知和控制对 LCE 人工肌肉很有价值。

### 5.2 按 AI for Materials 国际影响力排名（前 10）

1. **Alán Aspuru-Guzik**：自驱动实验室和 Acceleration Consortium 的国际组织影响力突出。
2. **Rampi Ramprasad**：Polymer Genome 是 polymer informatics 代表性平台。
3. **Shyue Ping Ong**：pymatgen、Materials Project 相关工具链在材料信息学基础设施中影响巨大。
4. **Rafael Gómez-Bombarelli**：生成式分子/材料设计代表人物。
5. **Markus J. Buehler**：生成式 AI、图推理、仿生材料和多尺度力学影响广泛。
6. **Michele Ceriotti**：机器学习原子模拟、SOAP/原子表示和统计采样方法标杆。
7. **Boris Kozinsky**：ML potentials、主动学习和大规模 MLMD 重要代表。
8. **Milad Abolhasani**：自驱动流体实验室和闭环材料实验影响力快速上升。
9. **Andrew Ferguson**：软/生物材料数据驱动和机器学习模拟方法影响力强。
10. **Aron Walsh / Alex Ganose**：计算材料设计、AI 表示和工作流方面影响力显著。

### 5.3 按最适合作为我未来课题组对标对象排名（前 5）

1. **Rampi Ramprasad + Polymer Genome**：学习数据库、聚合物表示、模型验证和平台化；避免只做静态物性预测，应加入取向、形变视频和器件性能。
2. **Yuuya Nagata / NIMS**：学习聚合物自动化和贝叶斯闭环；避免追求昂贵全自动机器人，先做半自动数据回流。
3. **Nick Warren / Sheffield**：学习自驱动聚合物合成；避免只关注合成转化率，要加入 LCE 驱动性能表征。
4. **Robert Katzschmann / ETH**：学习机器视觉闭环制造、人工肌肉应用和软机器人评价；避免忽略材料化学基础。
5. **Juan de Pablo + Andrew Ferguson**：学习软物质/液晶模拟和可解释模型；避免把模拟与实验平台割裂。

## 6. 对我未来方向的具体建议

你的方向在国际 AI for Materials 版图中应定位为 **AI for programmable soft polymeric actuators**，而不是笼统的 AI for Materials。更具体地说，它处在 polymer informatics、self-driving labs、machine vision characterization、generative structural design 和 soft robotics 的交叉点。科学问题不是“AI 能否发现新材料”，而是“如何让 AI 学会高分子网络、液晶取向、软结构几何与动态驱动行为之间的映射，并通过闭环实验持续改进”。

它与无机晶体 AI 发现的区别在于：输入变量不只是化学组成和晶体结构，还包括配方、交联网络、加工历史、取向图案和器件几何；输出变量不只是带隙/形成能，而是时间依赖的形变轨迹、曲率、力输出和循环衰减；数据来源不只是 DFT 数据库，而是视频、图像、显微、热机械和执行器测试。它与 Polymer Genome 的关系是“继承但扩展”：继承聚合物结构—性能表示和数据库思想，扩展到 LCE 的取向—结构—器件—动态性能。它与 self-driving labs 的关系是“借鉴闭环而非照搬对象”：不是做无机薄膜或小分子反应的全自动平台，而是做软材料制备、机器视觉表征和执行器评价闭环。

建议形成五个特色关键词：**LCE-specific database、vision-derived actuation metrics、Bayesian closed-loop formulation、director-field/geometry co-design、self-sensing intelligent actuator**。这五个词能明确区分你的方向与传统 AI for Materials、Polymer Genome 和无机材料 SDL。

## 7. 可执行 3–5 年研究路线

### 第一年：数据和表征基础

建立 LCE / 智能高分子材料配方数据库，字段包括单体、交联剂、液晶基元、柔性间隔链、光响应/导电/离子基团、比例、聚合方式、取向方式、刺激方式、Tg/Tni、序参量、模量、驱动应变、响应速度和疲劳寿命。同步建立实验视频数据库，用统一背景、标尺、温度/光强/电压记录格式拍摄驱动过程。开发 Python 图像分析流程，从视频中自动提取边缘、中心线、曲率、弯曲角、响应时间、恢复时间和循环衰减。第一年目标不是复杂深度学习，而是保证数据可信、可追踪、可复现。

### 第二年：机器学习预测与配方优化

建立配方—结构—性能预测模型。输入可先用人工描述符：介晶长度、柔性链长度、交联密度、极性/氢键/π-π 指标、Tg/Tni、取向方式和厚度；输出为驱动温度、应变、模量、响应速度、寿命。模型从 Random Forest、Gaussian Process、XGBoost 和小型 GNN 开始，避免过早追求大模型。结合贝叶斯优化或主动学习推荐下一轮实验，并建立 ELN/CSV/数据库回流系统，形成 AI-assisted LCE material screening workflow。

### 第三年：闭环优化与器件设计

构建 AI-assisted LCE actuator design platform，将材料配方、取向方式、几何结构和驱动性能联合优化。将 3D 打印、光取向、纤维组装、层级组装纳入变量。引入可编程 director field 和器件形状参数，目标函数从单一应变扩展到多目标：低驱动温度、高曲率、高力输出、快速响应、低滞后和长寿命。面向人工肌肉、仿生夹爪和柔性机器人末端执行器形成设计准则。

### 第四至第五年：自驱动软材料实验平台

构建小型自驱动软材料实验平台，实现材料设计—制备—表征—建模—优化—器件验证闭环。平台不必一开始昂贵：可由自动移液/微量混合、刮涂/打印、可编程光取向、热台/光源/电源刺激、相机/偏光显微和 Python 控制软件组成。重点发展自感知 LCE 执行器，将 CNT/导电聚合物/离子凝胶/液态金属等传感层与 LCE 驱动层集成，实现驱动和反馈一体化。最终产出数据库、软件工具、闭环平台论文和智能执行器论文。

## 8. 可以优先建设的数据集和工具

1. **LCE 配方—性能数据库**：记录化学配方、交联密度、热转变、力学与驱动性能。
2. **LCE 取向方式—驱动行为数据库**：记录单轴拉伸、表面摩擦、光取向、磁/电场取向、打印路径与 director field。
3. **软执行器视频—形变轨迹数据库**：所有视频附带标尺、帧率、刺激程序和样品元数据。
4. **人工肌肉纤维结构—收缩性能数据库**：适合纤维状 LCE、卷曲纤维、导电复合纤维。
5. **刺激响应材料图像—颜色/形变/性能数据库**：用于光/热/湿/化学响应器件。
6. **Python 图像分析工具**：OpenCV/scikit-image + napari/trackpy，实现边缘、中心线和曲率提取。
7. **Bayesian optimization 实验推荐工具**：基于 BoTorch/GPyTorch/scikit-optimize，输出下一组配方和工艺。
8. **LCE actuator design guideline**：将材料参数、几何参数、刺激条件和性能指标标准化。
9. **软材料闭环实验记录模板**：把 ELN、CSV、视频、图像和模型版本统一管理。

## 9. 推荐优先阅读清单

详见单独文件 `AI_for_Programmable_Soft_Materials_Reading_List.md`。建议阅读顺序为：先读 Ramprasad/Polymer Genome 与 Ferguson 软材料数据驱动综述，建立“软材料数据结构”概念；再读 Matter Lab、Abolhasani、Warren、Nagata 的 self-driving/polymer automation，建立闭环平台概念；随后读 Katzschmann、Rothemund、Pikul、Saarland，建立执行器性能指标；最后读 Gómez-Bombarelli、Buehler、Kozinsky、Ceriotti，将生成式设计和多尺度模拟作为增强模块。

## 10. 最终结论

最值得重点学习的课题组可分为三类。第一类是材料数据与聚合物 AI：Ramprasad、Nagata、Nick Warren、Ferguson 和 de Pablo，它们直接决定你能否建立 LCE 专用数据平台和可解释预测模型。第二类是闭环平台与自驱动实验：Aspuru-Guzik、Abolhasani、Shijing Sun，特别是 Abolhasani 的模块化流体平台和 Matter Lab 的 SDL 顶层架构。第三类是执行器和软机器人应用端：Katzschmann、Rothemund、Pikul、Seelecke/Rizzello，以及补充的 White、Hayward、Priimagi。

最适合迁移到 LCE 和智能高分子材料的方法包括：聚合物结构—性能数据库、多任务学习、贝叶斯优化/主动学习、机器视觉视频表征、director field/几何生成、软执行器模型化控制和自感知传感集成。只适合方法借鉴但不宜直接照搬的方向包括：无机晶体 DFT 数据库、大规模无机材料 SDL、纯原子尺度 ML potentials 和过于宏观的生成式 AI 叙事。它们可提供工具，但不能定义你的科学问题。

你的未来方向应写成“面向智能形变高分子材料的 AI 辅助设计、机器视觉表征与闭环优化制备”。核心不是 AI 本身，而是让 AI 服务于 LCE/人工肌肉/柔性执行器的动态形变性能。只有把化学配方、液晶取向、加工工艺、器件结构和视频表征统一到闭环中，才能形成区别于无机晶体材料 AI 发现和传统 Polymer Genome 的特色。

## 附录 A：如何避免泛泛而谈的 AI for Materials

1. **把对象写窄**：不要写“AI 发现新材料”，而写“AI 辅助 LCE/智能高分子执行器的分子—配方—取向—结构协同设计”。
2. **把输出写成动态性能**：使用曲率、应变、响应时间、恢复时间、力输出、循环寿命和自感知信号，而不是只写 Tg、模量或导电率。
3. **把数据来源写清**：文献数据、实验配方、偏光显微图像、驱动视频、热机械曲线和循环测试数据。
4. **把闭环写成可执行流程**：算法推荐 → 制备 → 机器视觉表征 → 模型更新 → 下一轮实验。
5. **把 AI 方法与物理机制连接**：贝叶斯优化用于少样本实验推荐；GNN/语言模型用于分子表示；有限元/粗粒化用于形变机制；计算机视觉用于自动化评价。
6. **把对标对象组合化**：材料端对标 Ramprasad/Nagata/Warren，平台端对标 Aspuru-Guzik/Abolhasani，器件端对标 Katzschmann/Rothemund/Pikul，而不是只对标单个 AI 大组。

## 附录 B：建议数据库字段模板

* 样品 ID、批次、操作者、日期、原始文献/实验记录链接。
* 单体 A/B/C、液晶基元、柔性间隔链、手性/偶氮/导电/离子基团、交联剂、引发剂、溶剂。
* 摩尔比、质量比、分子量、分子量分布、交联密度估计。
* 聚合方式、温度、时间、光强、催化剂、后处理。
* 取向方式：拉伸、摩擦、表面取向、光取向、磁场、电场、打印路径。
* 样品几何：厚度、宽度、长度、层数、纤维直径、图案参数。
* 表征：DSC、DMA、POM、SAXS/WAXS、拉伸、热机械、光谱。
* 驱动：刺激类型、温度/光强/电压/湿度/pH、频率、循环次数。
* 输出：最大应变、曲率、弯曲角、响应时间、恢复时间、输出力、功率密度、能效、寿命。
* 视频/图像：文件路径、帧率、标尺、ROI、分割算法版本、提取结果。

## 附录 C：补充课题组加入理由

* **Timothy J. White**：LCE/4D 打印和可编程形变材料核心组；虽然不是 AI 组，但作为 LCE 数据来源和器件指标标杆，比部分泛 AI for Materials 课题组更接近你的材料对象。
* **Ryan Hayward**：响应高分子、LCE/LCN 形变和软材料物理直接相关；适合作为智能形变机制和可编程薄膜结构对标。
* **Arri Priimagi**：光响应液晶网络和光驱动执行器直接对应 LCE 光驱动方向；如果你关注光取向/光响应，该组优先级很高。
* **Sergei Kalinin**：材料对象不一定是软材料，但自主显微、机器视觉和主动表征方法对“机器视觉表征与闭环优化”非常关键。

## 附录 D：3–5 年平台最小可行版本（MVP）

**硬件**：自动移液器或低成本液体处理器、微量混合模块、刮涂/旋涂/简易直写打印、UV/可见光源、热台、电源、工业相机、偏光显微镜、力传感器、环境箱。

**软件**：样品数据库、实验计划器、OpenCV 视频分析、BoTorch 贝叶斯优化、实验报告自动生成、模型版本管理。

**第一版闭环目标**：在 30–60 个样品内优化一个 LCE 薄膜在指定温度下的最大曲率和响应时间；第二版加入循环寿命；第三版加入多层结构和自感知信号。

**论文产出路径**：
1. 数据库/基准论文：LCE formulation–orientation–actuation dataset。
2. 方法论文：machine-vision-based actuation metrics extraction。
3. 平台论文：closed-loop optimization of LCE actuators。
4. 材料论文：AI-guided discovery of fast/low-temperature/fatigue-resistant LCE artificial muscles。
5. 器件论文：self-sensing programmable LCE soft gripper or artificial muscle.
