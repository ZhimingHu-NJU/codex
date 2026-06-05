# AI for Programmable Soft Materials 推荐阅读清单

> 说明：以下清单按“可迁移到 LCE / 智能高分子 / 柔性执行器”的价值排序，而不是按引用次数排序。链接优先给出实验室主页、论文 DOI、PubMed/PMC/arXiv 或官方新闻页。建议阅读时建立 Zotero 文件夹，并为每条文献标注：材料对象、输入变量、输出性能、AI 方法、是否有数据/代码、能否迁移到 LCE。

## 1. Polymer informatics

1. **Polymer Genome / Polymer Informatics（平台与系列论文）**  
   * 作者/团队：Rampi Ramprasad 等；Georgia Tech。  
   * 年份/期刊：系列工作，2010s–2020s。  
   * 链接：https://ramprasad.mse.gatech.edu/ ；https://www.nature.com/articles/s41578-021-00383-3  
   * 为什么值得读：这是聚合物结构—性能数据库、描述符、机器学习预测和逆向筛选最系统的路线。  
   * 与 LCE / 智能高分子 / 柔性执行器关系：可直接借鉴为 LCE 建立“单体—介晶—交联剂—取向—性能”数据库。

2. **Polymer informatics at-scale with multitask graph neural networks**  
   * 作者：Rishi Gurnani, Christopher Kuenneth, Aubrey Toland, Rampi Ramprasad 等。  
   * 期刊/年份：2022–2023 相关预印本/论文。  
   * 链接：https://arxiv.org/abs/2209.13557  
   * 为什么值得读：展示多任务 GNN 如何从大规模聚合物库预测多性能。  
   * 关系：LCE 方向也需要同时预测 Tg/Tni、模量、应变、响应速度、疲劳寿命等多目标。

3. **polyBERT: a chemical language model for polymers**  
   * 作者：Christopher Kuenneth, Rampi Ramprasad 等。  
   * 期刊/年份：2023 前后。  
   * 链接：https://ramprasad.mse.gatech.edu/  
   * 为什么值得读：展示如何把聚合物字符串/结构表示转化为可学习语言模型表示。  
   * 关系：可发展 LCE 专用“介晶/柔性间隔链/交联网络语言模型”。

4. **Polymer Informatics Beyond Homopolymers**  
   * 作者：Shukla, Christopher Kuenneth, Rampi Ramprasad 等。  
   * 期刊/年份：2023。  
   * 链接：https://arxiv.org/abs/2303.12938  
   * 为什么值得读：LCE 通常不是简单均聚物，而是共聚、交联、取向网络；该文有助于走出均聚物限制。  
   * 关系：对 LCE 交联网络、混合配方和多组分体系尤其重要。

5. **An Informatics Framework for Sustainable, Chemically Recyclable, Synthetically-Accessible and Durable Polymers**  
   * 作者：Joseph Kern, Yongliang Su, Will Gutekunst, Rampi Ramprasad 等。  
   * 期刊/年份：2024。  
   * 链接：https://arxiv.org/abs/2409.15354  
   * 为什么值得读：把可合成性、可回收性、耐久性加入设计约束。  
   * 关系：LCE 执行器未来也必须考虑可制备、可循环、疲劳耐久和环境稳定性。

## 2. AI for polymers

1. **Autonomous Polymer Design and Discovery Group（NIMS）**  
   * 作者/团队：Yuuya Nagata。  
   * 年份：2025 起。  
   * 链接：https://www.nims.go.jp/group/autonomous/index_en.html  
   * 为什么值得读：聚合物自动化合成、机器人实验、NIMO 贝叶斯优化的最新团队路线。  
   * 关系：最接近“LCE 配方—制备—测试—优化”的实验闭环。

2. **Self-driving labs enable faster and smarter polymer synthesis**  
   * 作者/团队：Nick Warren 团队。  
   * 期刊/年份：University of Sheffield 新闻，2025。  
   * 链接：https://www.sheffield.ac.uk/cmbe/news/self-driving-labs-making-chemical-research-faster-and-smarter  
   * 为什么值得读：展示可无人值守运行的聚合物合成平台。  
   * 关系：LCE 的配方筛选与聚合条件优化可以采用类似平台架构。

3. **Data-Driven Design and Autonomous Experimentation in Soft and Biological Materials Engineering**  
   * 作者：Andrew Ferguson 等。  
   * 期刊/年份：Annual Review 相关，2022。  
   * 链接：https://pubmed.ncbi.nlm.nih.gov/35236085/  
   * 为什么值得读：将数据驱动设计、迁移学习、自主实验放在软/生物材料语境，而不是无机晶体语境。  
   * 关系：为 LCE/人工肌肉写项目提供框架语言。

## 3. Generative AI for materials

1. **Automatic chemical design using a data-driven continuous representation of molecules**  
   * 作者：Gómez-Bombarelli 等。  
   * 期刊/年份：ACS Central Science, 2018。  
   * 链接：https://pubs.acs.org/doi/10.1021/acscentsci.7b00572  
   * 为什么值得读：VAE 分子生成的经典论文。  
   * 关系：可迁移到可聚合介晶、偶氮苯光响应单体、柔性链段设计。

2. **Learning Matter Lab research pages**  
   * 作者/团队：Rafael Gómez-Bombarelli。  
   * 链接：https://gomezbombarelli.mit.edu/  
   * 为什么值得读：清楚区分 forward model 与 inverse design。  
   * 关系：帮助将 LCE 从经验筛选转为目标驱动的分子/网络设计。

3. **Generating 3D architectured nature-inspired materials and granular media using diffusion models based on language cues**  
   * 作者：Markus J. Buehler 等。  
   * 期刊/年份：2022/2023。  
   * 链接：https://pmc.ncbi.nlm.nih.gov/articles/PMC9767007/  
   * 为什么值得读：把生成式模型用于三维仿生结构。  
   * 关系：对 LCE 可编程取向图案、折纸/曲面执行器几何生成有启发。

4. **Graph-based AI model maps the future of innovation**  
   * 作者/团队：Markus J. Buehler。  
   * 年份：MIT News, 2024。  
   * 链接：https://news.mit.edu/2024/graph-based-ai-model-maps-future-innovation-1112  
   * 为什么值得读：说明知识图谱与多模态推理在材料创新中的用法。  
   * 关系：可为 LCE 文献知识图谱和实验设计代理提供思路。

## 4. Self-driving laboratories

1. **Self-driving Lab（Matter Lab）**  
   * 作者/团队：Alán Aspuru-Guzik。  
   * 链接：https://www.matter.toronto.edu/basic-content-page/self-driving-lab  
   * 为什么值得读：SDL 的典型定义、AI 优化、机器人、自动表征和视觉感知机器人。  
   * 关系：LCE 平台应借鉴“design–make–test–learn”的闭环，但把测试端换成机器视觉驱动表征。

2. **Autonomous Nanocrystal Doping by Self-Driving Fluidic Micro-Processors**  
   * 作者：Fazel Bateni, Robert Epps, Milad Abolhasani 等。  
   * 期刊/年份：Advanced Intelligent Systems, 2022。  
   * 链接：https://news.ncsu.edu/2022/03/self-driving-lab/  
   * 为什么值得读：非常清楚地展示闭环流体平台、代理模型和目标导向优化。  
   * 关系：可迁移到 LCE 混合、涂布、光固化、刺激响应表征。

3. **Autonomous laboratories for accelerated materials discovery: community survey and practical insights**  
   * 作者：Shijing Sun, Santosh Suram 等。  
   * 期刊/年份：2026 前后预印本。  
   * 链接：https://www.cambridge.org/engage/api-gateway/coe/assets/orp/resource/item/65e0ce79e9ebbb4db993d6fe/original/autonomous-laboratories-for-accelerated-materials-discovery-a-community-survey-and-practical-insights.pdf  
   * 为什么值得读：从社区角度总结 SDL 建设痛点。  
   * 关系：适合规划小型软材料 SDL 的设备、数据标准和人机协作流程。

## 5. Autonomous polymer synthesis

1. **Sheffield self-driving polymer synthesis platform**  
   * 作者/团队：Nick Warren。  
   * 链接：https://www.sheffield.ac.uk/cmbe/news/self-driving-labs-making-chemical-research-faster-and-smarter  
   * 为什么值得读：对象就是聚合物，且强调乳液聚合、绿色材料和闭环优化。  
   * 关系：比多数无机材料 SDL 更适合 LCE 配方和反应条件优化。

2. **NIMS Autonomous Polymer Design and Discovery Group**  
   * 作者/团队：Yuuya Nagata。  
   * 链接：https://samurai.nims.go.jp/profiles/nagata_yuuya?locale=en  
   * 为什么值得读：日本 NIMS 在自主聚合物发现上的新布局。  
   * 关系：可作为亚洲范围合作和平台建设对标。

3. **Continuous Flow Chemistry and Bayesian Optimization for Polymer-Functionalized CNT Methane Sensors**  
   * 作者：John Dunlap, Haosheng Feng, Timothy Swager, Luke Baldwin 等。  
   * 期刊/年份：ACS Applied Materials & Interfaces, 2024。  
   * 链接：https://swagergroup.mit.edu/continuous-flow-chemistry-and-bayesian-optimization-polymer-functionalized-carbon-nanotube-based  
   * 为什么值得读：把聚合物传感材料、连续流和多目标贝叶斯优化连接起来。  
   * 关系：对环境响应 LCE/自感知执行器材料优化非常有启发。

## 6. Machine learning potentials

1. **Machine learning at the atomic-scale**  
   * 作者：Félix Musil, Michele Ceriotti 等。  
   * 年份：2020。  
   * 链接：https://arxiv.org/abs/2012.04616  
   * 为什么值得读：原子尺度机器学习表示和势函数综述。  
   * 关系：用于理解 LCE 介晶相互作用、链段堆积和界面作用，但不能直接解决宏观驱动。

2. **Beyond potentials: integrated machine-learning models for materials**  
   * 作者：Michele Ceriotti 等。  
   * 年份：2022。  
   * 链接：https://arxiv.org/abs/2208.06139  
   * 为什么值得读：说明 ML 不只预测能量，也可学习多种物性。  
   * 关系：LCE 需要从分子局域结构走向相变、模量和响应行为的多尺度联系。

3. **MIR Group / NequIP / Allegro / FLARE 路线**  
   * 作者/团队：Boris Kozinsky。  
   * 链接：https://mir.g.harvard.edu/people/open-positions  
   * 为什么值得读：将主动学习、不确定性和大规模 MLMD 工程化。  
   * 关系：可借鉴到 LCE 单体/界面局部相互作用，不宜直接替代实验闭环。

## 7. AI-assisted soft materials design

1. **Ferguson Lab research statement**  
   * 作者/团队：Andrew Ferguson。  
   * 链接：https://www.ferglab.com/  
   * 为什么值得读：把机器学习、统计热力学和软材料工程放在同一框架。  
   * 关系：适合 LCE 的机理解释和模拟数据增强。

2. **de Pablo liquid crystal / polymer simulation works**  
   * 作者/团队：Juan de Pablo。  
   * 链接：https://news.uchicago.edu/story/research-reveals-inner-workings-liquid-crystals  
   * 为什么值得读：液晶取向和界面是 LCE 驱动性能的核心。  
   * 关系：比泛 AI 文献更直接触及 LCE 的物理本质。

3. **Polymer Genome + LCE 专用数据库迁移阅读**  
   * 作者/团队：Ramprasad 等 + LCE 领域综述。  
   * 链接：https://ramprasad.mse.gatech.edu/  
   * 为什么值得读：学习如何定义可学习的聚合物输入输出。  
   * 关系：建议你建立 LCE formulation–orientation–actuation 数据表。

## 8. AI for soft actuators

1. **Soft Robotics Lab at ETH Zurich**  
   * 作者/团队：Robert Katzschmann。  
   * 链接：https://srl.ethz.ch/ ；https://robert.katzschmann.de/  
   * 为什么值得读：软机器人、人工肌肉、机器视觉闭环制造和控制。  
   * 关系：对 LCE 执行器应用端最直接。

2. **Vision-controlled jetting for composite systems and robots**  
   * 作者：Katzschmann 团队。  
   * 期刊/年份：Nature, 2023。  
   * 链接：https://www.nature.com/articles/s41586-023-06684-3  
   * 为什么值得读：机器视觉闭环制造软机器人。  
   * 关系：可迁移到 LCE 光取向/打印过程的视觉闭环质量控制。

3. **Functional Soft Robotic Matter / Rothemund works**  
   * 作者/团队：Philipp Rothemund。  
   * 链接：https://www.iams.uni-stuttgart.de/institute/team/Rothemund/  
   * 为什么值得读：电液软执行器的能效、模块化和性能优化。  
   * 关系：用于定义 LCE 人工肌肉的对标指标：功率密度、响应速度、寿命、能效。

4. **DEA SOFT ROBOTS**  
   * 作者/团队：Stefan Seelecke / Gianluca Rizzello。  
   * 链接：https://www.spp2100.de/project/dea-soft-robots  
   * 为什么值得读：智能材料执行器的建模、自感知和控制。  
   * 关系：适合把 LCE 发展为自感知、可控人工肌肉。

## 9. Machine vision for actuator characterization

1. **Vision-controlled jetting for composite systems and robots**  
   * 作者：Robert Katzschmann 团队。  
   * 链接：https://www.nature.com/articles/s41586-023-06684-3  
   * 为什么值得读：闭环视觉不仅用于表征，也直接控制制造。  
   * 关系：LCE 光取向/打印/驱动测试均可引入类似视觉反馈。

2. **Soft Actuators and Sensors（Pikul Group）**  
   * 作者/团队：Kevin Pikul。  
   * 链接：https://pikulgroup.engr.wisc.edu/research/soft-actuators-and-sensors/  
   * 为什么值得读：软传感、视觉触觉融合和可变形表面评价。  
   * 关系：有助于设计 LCE 执行器视频分析、触觉/形变同步表征。

3. **Autonomous microscopy / physics-informed ML（Kalinin）**  
   * 作者/团队：Sergei Kalinin。  
   * 链接：https://mse.utk.edu/people/sergei-kalinin/  
   * 为什么值得读：自主表征和图像主动学习的方法可迁移。  
   * 关系：可用于偏光显微、取向缺陷识别和驱动视频自动标注。

## 10. Bayesian optimization for materials experiments

1. **Matter Lab Self-driving Lab**  
   * 作者/团队：Alán Aspuru-Guzik。  
   * 链接：https://www.matter.toronto.edu/basic-content-page/self-driving-lab  
   * 为什么值得读：了解 BO/主动学习如何嵌入机器人实验。  
   * 关系：为 LCE 小型闭环平台提供顶层架构。

2. **Abolhasani Self-Driving Fluidic Lab**  
   * 作者/团队：Milad Abolhasani。  
   * 链接：https://www.abolhasanilab.com/  
   * 为什么值得读：模块化流体平台和代理模型路线非常工程化。  
   * 关系：适合 LCE 配方、固化和在线表征闭环。

3. **Swager/Baldwin continuous-flow Bayesian optimization sensor paper**  
   * 作者：Dunlap, Feng, Swager, Baldwin 等。  
   * 链接：https://pubs.acs.org/doi/abs/10.1021/acsami.4c14279  
   * 为什么值得读：具体展示多目标贝叶斯优化在聚合物功能器件中的用法。  
   * 关系：LCE 环境响应器件可以采用类似“合成参数—传感/驱动性能”的优化框架。
