# 汽车焊装机器人涂胶仿真与现场调试周期缩短系统调研报告

> 调研日期：2026-06-10  
> 目标：围绕“从传统离线轨迹仿真升级为胶条质量仿真，并通过现场标定补偿减少试胶调试”，调研汽车及相关行业的共性痛点、已有技术、可借鉴案例与分阶段实施方案。

## 0. 执行摘要

汽车白车身焊装、总装玻璃胶、电池包密封/导热胶、电子 FIPG 点胶、航空航天复合材料胶接等行业均存在类似问题：离线编程通常能解决可达性、干涉、节拍、机器人程序生成，但不能可靠预测实际胶条的宽度、高度、截面积、位置、连续性和起停/转角缺陷。行业现行做法主要是“离线轨迹 + 工艺经验表 + 现场试胶 + 视觉检测/人工复核 + 参数微调”。近年出现的方向包括：

1. **3D 胶条在线检测与自适应控制**：Coherix、Atlas Copco/SCA、Nordson、HA-TEC 等方案可在线测量胶宽、胶高、体积、位置和连续性，并将缺陷、Z 距、横向位置、体积偏差反馈给机器人或计量系统。
2. **速度同步流量控制**：将出胶量与机器人实际 TCP 速度同步，解决转角减速、加减速段堆胶/缺胶。
3. **数据驱动/数字孪生建模**：已有学术研究显示，可用数字孪生预测胶线宽度/厚度，并优化转角参数；也可用贝叶斯优化把现场调参从“天级”压缩到“小时级”。
4. **现场标定与补偿**：机器人基坐标、TCP、胶嘴偏差、工件定位偏差、CAD 到实物配准、3D 视觉 Z-tracking/lateral tracking 是让仿真轨迹落地的关键。

本项目最可行技术路线不是单纯 CFD 全物理仿真，而是采用 **“简化物理守恒模型 + 材料/设备台架试验 + 数据驱动校正 + 3D 视觉闭环验证 + 现场坐标/TCP/工件误差补偿”** 的混合路线。目标若是把单台机器人现场涂胶调试周期缩短到约 4 天，建议先将仿真系统覆盖 80% 以上直线/缓曲率胶段的胶宽、胶位、胶量预测，再逐步攻克起停胶、转角堆胶、曲面法向与动态姿态误差。

---

## 1. 行业痛点总结

### 1.1 共性问题

| 行业/场景 | 共性问题 | 与汽车焊装涂胶的相似性 |
|---|---|---|
| 汽车白车身结构胶、折边胶、密封胶 | 胶条位置、胶宽/胶高、连续性直接影响强度、密封、防腐；转角、起停、搭接处容易堆胶/断胶 | 高度相似，均为机器人沿 CAD 曲线挤出高黏度材料 |
| 总装车窗玻璃聚氨酯胶 | 胶条截面、位置、连续性关系到水密和安全；黑胶黑底检测困难 | 相似，尤其关注三角胶截面、起停接头、位置偏差 |
| 动力电池包密封胶/导热胶/结构胶 | 胶量不足导致密封/导热不足，胶量过多导致溢胶、装配干涉；热界面材料对体积均匀性敏感 | 相似，但面积更大、材料更高填料/高黏度，温度和流变更关键 |
| 电子制造 FIPG、灌封、导电胶 | 微小胶宽/胶高公差、起停区域缺陷、点胶位置误差影响密封/EMI/电性能 | 工艺尺度不同，但建模、检测、闭环优化高度可借鉴 |
| 航空航天复材胶接/密封 | 大曲面、复杂姿态、长路径、质量可追溯要求高 | 与白车身复杂曲面涂胶、低返修目标相似 |
| 高黏度流体 3D 打印/挤出 | 流动滞后、非线性、剪切变稀、路径拐角堆料 | 对动态补偿、模型预测控制、路径/流量协同优化有参考价值 |

### 1.2 是否存在“离线仿真轨迹与实际胶条质量不一致”

结论：**存在，而且是跨行业共性问题**。

- RoboDK、KUKA.Sim、Siemens Process Simulate、DELMIA 等离线编程/仿真工具主要优势在于可达性、碰撞、节拍、程序生成和虚拟调试，通常不内置可直接预测高黏度胶条成形质量的材料-设备-机器人耦合模型。RoboDK 文档明确其离线编程用于创建、仿真并生成机器人程序；KUKA 也强调离线仿真用于可达性、碰撞、节拍和离线编程准备。[RoboDK OLP](https://www.robodk.com/doc/en/Robot-Programs.html)，[KUKA 3D offline simulation](https://www.kuka.com/en-us/services/service_robots-and-machines/selection-planning-simulation-robot-systems/3d-offline-simulation)
- 工业资料反复指出，实际胶条会受喷嘴尺寸、机器人速度、压力、黏度、针嘴高度、环境、零件变化影响；机器人转角减速若不与流量同步，会造成转角堆胶或缺胶。[RBTX bead dispensing control](https://learn.rbtx.com/knowledge-resource/controlling-your-bead-in-dispensing/)，[Automate.org dispensing robots](https://www.automate.org/robotics/industry-insights/dispensing-profits-with-dispensing-robots)
- 2025 年机器人涂胶数字孪生论文明确以“预测胶线质量和优化涂胶参数”为目标，说明传统机器人自动涂胶仍需要实时预测和优化参数；该研究报告胶线宽度误差控制在 ±0.5 mm、厚度误差 ±0.3 mm，并通过优化降低转角宽度和厚度以避免堆胶。[ScienceDirect DT gluing](https://www.sciencedirect.com/science/article/abs/pii/S0278612525001177)
- 2025 年自动化人机协同调试论文指出，胶水点胶过程调参耗时且昂贵，模型难构建，实际需要黑箱模型/贝叶斯优化；其案例把机器人速度、喷嘴高度、预压力作为优化变量，并用线激光扫描胶条轮廓。[Springer glue dispensing commissioning](https://link.springer.com/article/10.1007/s00170-025-15121-w)

---

## 2. 问题本质分析

传统离线仿真不能预测真实胶条质量的根本原因是：**胶条质量不是几何轨迹的单变量函数，而是材料流变、计量设备动态、机器人运动、工件几何与现场误差共同决定的动态耦合结果**。

### 2.1 材料因素

关键材料参数包括：

- 黏度、密度、表面张力、接触角、润湿性；
- 温度敏感性；
- 触变性、剪切变稀、屈服应力；
- 双组分混合比例、固化反应、开放时间；
- 填料含量和颗粒分布，例如导热胶、结构胶、FIPG 材料。

电子 FIPG 资料指出，胶条高度和宽度受零件尺寸变化、点胶参数与材料影响；宽度与高度因自由成形和黏度相关，更多颗粒填充的材料会形成更窄胶条。[Modus FIP gasket guide](https://www.modusadvanced.com/form-in-place-gasket-guide)

### 2.2 设备因素

关键设备参数包括：

- 胶泵类型：齿轮泵、柱塞泵、螺杆泵、伺服计量、时间-压力；
- 压力、预压力、背压、阀响应时间；
- 胶嘴直径、长度、磨损、弯曲、堵塞、挂胶；
- 温控、管路长度、管路弹性、材料可压缩性；
- 吸回/回抽、开关胶提前/滞后时间。

Nordson 资料显示汽车胶粘/密封系统通常由控制器、计量器、阀和视觉集成组成，并可依据 3D 胶条质量反馈提高生产信心。[Nordson Process Sentry](https://www.nordson.com/en/products/industrial-coating-solutions-products/process-sentry-plc-system-controller)

### 2.3 机器人运动因素

关键机器人参数包括：

- TCP 速度、加速度、jerk；
- 转角减速、圆弧过渡、姿态变化；
- 机器人控制器插补方式与实际速度曲线；
- 姿态变化导致胶嘴出口相对工件法向角变化；
- 动态跟随误差、手腕翻转、奇异区速度波动。

行业资料指出，机器人转角保持恒速很难，速度变化会扰动胶条尺寸和流量；速度同步流量控制因此成为高一致性点胶的关键。[Automate.org dispensing robots](https://www.automate.org/robotics/industry-insights/dispensing-profits-with-dispensing-robots)，[RBTX bead dispensing control](https://learn.rbtx.com/knowledge-resource/controlling-your-bead-in-dispensing/)

### 2.4 工件与现场误差

现场误差包括：

- 机器人基坐标与仿真坐标不一致；
- TCP/胶嘴实际安装偏差；
- 胶嘴弯曲、磨损、换嘴后偏移；
- 工装定位误差、夹具磨损、工件批次变形；
- CAD 名义曲面与实际白车身钣金偏差；
- 温湿度和胶材批次差异。

Coherix 的 TCP Locator 方案即针对“弯曲或错装胶嘴导致胶条位置错误”，通过 3D 测量实际喷嘴位置并将偏移发送给机器人动态修正路径。[Coherix 3D TCP Locator](https://coherix.com/coherix-3d-tcp-locator/)

---

## 3. 国内外已有解决方案分类

### 3.1 胶条成形仿真模型

#### 3.1.1 简化物理模型

最基础模型来自体积守恒：

- 单位长度胶量：`A = Q / v`，其中 `A` 为胶条截面积，`Q` 为体积流量，`v` 为 TCP 速度；
- 若近似截面形状为圆弧、椭圆、三角形或梯形，可由 `A` 反推宽度、高度；
- 胶嘴高度、角度、基材润湿性和表面张力决定截面形状因子；
- 转角区需考虑机器人实际速度变化和出胶系统响应滞后。

优点：计算快、可嵌入离线编程；缺点：难以处理触变、剪切变稀、起停胶、复杂曲面和固化收缩。LivePhysics 的工业科普资料也采用 `A = Q/v` 和 `h = Q/(w v)` 等关系说明流量、速度、喷宽/胶宽和厚度之间的关系。[LivePhysics nozzle dispensing](https://livephysics.com/infographics/robotics-spray-and-dispensing-nozzles/)

#### 3.1.2 CFD/流体仿真

CFD 可分析喷嘴内部压降、非牛顿黏度、液滴/胶条铺展、接触角、表面张力、固化等。Frontiers 2023 论文用计算机仿真研究高黏度导电胶接触点胶过程，并指出针尖-基材接触角、表面张力、黏度等对过程有显著影响。[Frontiers conductive adhesive dispensing](https://www.frontiersin.org/articles/10.3389/fmats.2023.1183747)

优点：物理解释强，可用于胶嘴设计、工艺窗口探索；缺点：计算慢，参数难获取，难在白车身长路径多工况下实时使用。

#### 3.1.3 数据驱动模型

典型方法：

- DOE 试验采集 `材料批次/温度/压力/流量/速度/高度/角度/曲率 → 胶宽/胶高/位置/缺陷`；
- 用回归、随机森林、XGBoost、神经网络、高斯过程、贝叶斯优化建立质量预测和参数推荐模型；
- 对直线段、转角段、起停段、曲面段分别建模。

Springer 2025 案例用贝叶斯优化处理机器人速度、喷嘴高度、点胶预压力，并通过线激光计算胶宽与截面积标准差，调试时间从天级降到小时级。[Springer glue dispensing commissioning](https://link.springer.com/article/10.1007/s00170-025-15121-w)

#### 3.1.4 物理 + 数据校正混合模型

推荐采用：

- 用体积守恒和计量系统动态模型给出先验；
- 用台架试验拟合流量-压力-温度-黏度关系；
- 用视觉检测数据校正截面形状因子、转角补偿系数、起停时序；
- 用现场数据持续更新模型。

Siemens/RAMPF 案例用 Simcenter Amesim 建模胶水设备的液压、管路材料流动、泵和阀行为，以预测所需点胶体积并加快配置。[Siemens RAMPF glue dispensing case](https://resources.sw.siemens.com/en-US/case-study-rampf-production-systems/)

### 3.2 机器人轨迹与工艺参数协同优化

优化对象包括：

- 速度：直线段保持目标单位长度胶量；转角减速时同步降流量；短段避免速度尚未稳定就进入收胶；
- 胶嘴姿态：保持胶嘴轴线与工件法向或工艺要求角度一致，避免姿态突变；
- 胶嘴高度：在允许范围内保持稳定，过高会粘附差/拉丝，过低会刮胶/压扁；
- 压力/流量：与速度、黏度、温度联动；
- 起胶/收胶时序：开胶提前、收胶提前、回抽、减速段流量斜坡；
- 转角/曲率补偿：角点提前降流量、外侧路径微偏移、圆角化轨迹、分段速度上限。

ABB 白车身资料明确指出，点胶设备由机器人、喷嘴、计量器和泵组成，机器人路径与速度需要同计量器和喷嘴共同控制，以把胶施加在正确位置和形状/数量上。[ABB BIW dispensing](https://new.abb.com/products/robotics/manufacturing-solutions/body-in-white/technologies-and-process-expertise/mechanical-joining-techniques)

### 3.3 现场安装误差补偿

推荐采用四级补偿：

1. **机器人/工作站级标定**：机器人基坐标、工装坐标、外部轴、离线模型与现场实体对齐；
2. **工具级标定**：TCP、胶嘴长度/弯曲、胶嘴出口方向、换嘴后自动检查；
3. **工件级配准**：3D 扫描/视觉定位若干基准特征，CAD 与实际工件配准，生成路径整体偏置或局部形变补偿；
4. **过程级跟踪**：喷嘴前方/周围 3D 传感器实时 Z-tracking 和 lateral tracking，修正喷嘴高度和横向胶位。

RoboDK 机器人标定文档说明可在离线站点中建立校准项目，并通过基座、工具、校准测量和验证测量提高离线程序准确性。[RoboDK robot calibration](https://robodk.com/doc/en/Robot-Calibration-Creaform-Offline-setup.html)

### 3.4 胶条质量检测与闭环控制

#### 2D 视觉

- 能检测有无胶、胶宽、位置、断胶、明显溢胶；
- 对黑胶黑底、透明胶、反光表面、胶高/体积不敏感；
- 适合低成本后检或对比度良好的场景。

#### 3D 视觉/激光轮廓

- 通过线激光/多激光/结构光/OCT 获得胶条截面；
- 可测胶宽、胶高、截面积/体积、位置、连续性、气泡/凹陷、断胶、堆胶；
- 可做在线检测、自动修补、Z 跟踪、横向跟踪、体积自适应控制。

Coherix 3D 宣称可在生产线速度下检测胶条高度、宽度和体积，并用于白车身结构胶/密封胶、玻璃胶、电池导热胶等场景。[Coherix 3D](https://coherix.com/predator3d/) Atlas Copco RTVision.3d 可检测宽度、位置、连续性、高度和体积，并适用于黑胶黑底等困难场景。[Atlas Copco RTVision.3d](https://www.atlascopco.com/en-ca/itba/products/quality-inspection-systems-21013.22148/rtvision.3d-sku731216)

### 3.5 数字孪生和离线编程

数字孪生应包括：

- 机器人与工装几何孪生；
- 真实控制器/PLC/点胶控制器接口；
- 胶材与计量系统模型；
- 过程质量预测模型；
- 视觉检测数据回流与模型更新；
- 程序后处理与现场坐标补偿。

Siemens Process Simulate 强调可用真实 PLC 代码、硬件、OPC UA 和实际机器人程序进行更真实虚拟调试；但其通用能力仍需结合涂胶专用质量模型才能实现“胶条质量仿真”。[Siemens Process Simulate](https://www.siemens.com/en-gb/products/tecnomatix/process-simulate-software/)

---

## 4. 典型案例表格

完整 CSV 见 `summary_table.csv`。下表摘录 18 个代表性案例。

| # | 行业/场景 | 公司或研究机构 | 解决的问题 | 方法 | 能否预测/检测胶宽高位 | 现场补偿 | 参考价值 | 来源 |
|---:|---|---|---|---|---|---|---|---|
| 1 | 汽车/电池/电子胶条 | Coherix | 在线胶条质量、缺陷、位置偏差 | 360° 3D 多激光 + APC | 检测宽高体积位置 | 支持 Z/横向/TCP/体积补偿 | 极高 | https://coherix.com/predator3d/ |
| 2 | 汽车胶条 | Coherix AutoRepair | 断胶、气泡、低体积 | 在线 3D 检测 + 自动修补 | 检测并修补缺陷 | 支持 | 极高 | https://coherix.com/auto-repair-for-adhesive-dispensing/ |
| 3 | 汽车胶条 | Coherix TCP Locator | 胶嘴弯曲/换嘴后 TCP 偏差 | 3D 测喷嘴并更新 TCP | 间接保证位置 | 支持 | 极高 | https://coherix.com/coherix-3d-tcp-locator/ |
| 4 | 汽车/电子/医疗 | Atlas Copco SCA/Scheugenpflug | 胶条宽高体积位置与追溯 | RTVision.t/s/3d | 检测 | 部分支持 | 很高 | https://www.atlascopco.com/en-ca/itba/plp/dispensing-potting-bonding/integrated-bead-inspection |
| 5 | 汽车胶粘密封 | Nordson + Coherix | 点胶控制与 3D 检测一体化 | Process Sentry + Predator3D | 检测 3D 胶条 | 支持自动修正 | 很高 | https://coherix.com/nordson-coherix-fully-integrated-bead-dispensing-inspection-and-process-control-solution/ |
| 6 | 汽车密封 | Dürr | 白车身密封自动化质量与节拍 | 机器人 + 专用喷嘴 | 未明确预测 | 未明确 | 中高 | https://www.durr.com/en/products/sealing-gluing-technology/sealing-process |
| 7 | 汽车 BIW | ABB | 路径/速度/计量协同 | Integrated Dispensing Function Package | 控制形状/数量 | 未明确 | 高 | https://new.abb.com/products/robotics/manufacturing-solutions/body-in-white/technologies-and-process-expertise/mechanical-joining-techniques |
| 8 | 航空机器人涂胶 | 学术论文 2025 | 胶线质量预测与转角堆胶 | 数字孪生 + 参数优化 | 预测宽度/厚度 | 未重点 | 极高 | https://www.sciencedirect.com/science/article/abs/pii/S0278612525001177 |
| 9 | 工业胶水点胶 | KU Leuven 等 2025 | 调参耗时 | 线激光 + 贝叶斯优化 | 检测宽度/面积 | 未重点 | 极高 | https://link.springer.com/article/10.1007/s00170-025-15121-w |
| 10 | 高黏度挤出/3D 打印 | UMich 等 2022 | 动态滞后与非线性 | 集总参数模型 + iLQR 补偿 | 间接预测沉积质量 | 路径补偿 | 高 | https://arxiv.org/abs/2210.10747 |
| 11 | 导电胶点胶 | Frontiers 2023 | 高黏度接触点胶过程 | 计算机仿真 + 试验 | 预测液滴/形貌趋势 | 否 | 中高 | https://www.frontiersin.org/articles/10.3389/fmats.2023.1183747 |
| 12 | 点胶装备数字孪生 | Siemens/RAMPF | 胶量预测和机器配置 | Amesim 液压/流动/泵阀模型 | 预测点胶体积 | 设备级 | 高 | https://resources.sw.siemens.com/en-US/case-study-rampf-production-systems/ |
| 13 | 汽车/电子 3D 胶条检测 | HA-TEC | 密封胶轮廓、断胶 | 3D 激光三角测量 | 检测宽高位置 | 自动修补路径 | 高 | https://ha-tec.com/solutions/vision/sealant-inspection |
| 14 | 汽车/电子案例 | Nextomation | 机器人 3D 胶条检测 | 3D 视觉 | 检测 | 未明确 | 中 | https://nextomation.com/case-study/robotic-3d-glue-bead-inspection-system/ |
| 15 | 电子 FIPG | Modus Advanced | FIP 胶条设计公差 | 工艺设计规则 | 经验预测宽高关系 | 否 | 中 | https://www.modusadvanced.com/form-in-place-gasket-guide |
| 16 | 离线编程/标定 | RoboDK | CAD 到机器人程序与标定 | OLP + 标定 | 不预测质量 | 支持坐标补偿 | 中高 | https://robodk.com/doc/en/Robot-Calibration-Creaform-Offline-setup.html |
| 17 | 汽车/工业 OLP | Siemens Process Simulate | 虚拟产线与虚拟调试 | PLC/机器人程序仿真 | 不直接预测胶条 | 坐标/逻辑层 | 中高 | https://www.siemens.com/en-gb/products/tecnomatix/process-simulate-software/ |
| 18 | 中国专利 | CN107702653B | 2D 难测高度、同色胶检测 | 机器人涂胶三维信息视觉检测 | 检测三维胶条 | 部分 | 高 | https://patents.google.com/patent/CN107702653B/zh |

---

## 5. 各类方案优缺点

| 方案 | 优点 | 缺点 | 对本项目建议 |
|---|---|---|---|
| 传统 OLP + 经验参数 | 成熟、成本低、易集成 | 不能预测胶宽/胶高/起停缺陷，现场调试重 | 作为基础平台保留，但必须增加质量模型 |
| CFD 全物理仿真 | 可解释性强，适合喷嘴/材料研究 | 慢、参数难、难覆盖全路径 | 仅用于离线机理研究和特征数据生成 |
| 简化物理模型 | 快、可嵌入仿真、可解释 | 精度依赖校正，复杂缺陷难预测 | 作为主模型骨架 |
| 数据驱动模型 | 能学习复杂耦合，迭代快 | 需大量高质量数据，外推风险 | 用台架 + 现场视觉数据训练校正 |
| 3D 视觉检测 | 直接测量胶宽/高/体积/位置 | 硬件成本和集成复杂，受空间/节拍限制 | 必须配置至少验证型，关键线体可在线闭环 |
| 在线闭环控制 | 能应对零件/温度/喷嘴漂移 | 控制器接口、实时性和安全验证难 | 先离线闭环/批次优化，再实时局部闭环 |
| TCP/工件标定补偿 | 解决仿真到现场落差 | 需要标定流程和传感器 | 必须作为 4 天目标的核心模块 |
| 数字孪生 | 贯通仿真、控制、检测、追溯 | 建设周期长，需数据治理 | 分阶段搭建，不追求一步到位 |

---

## 6. 可借鉴技术路线

建议总体方案：

```text
材料与设备参数建模
  → 胶条成形预测
  → 机器人轨迹与工艺参数协同优化
  → 现场标定与误差补偿
  → 视觉检测闭环验证
  → 离线程序直接导入现场
```

### 6.1 核心模块

1. **材料/设备台架模型**
   - 建立胶材黏度-温度-剪切速率曲线；
   - 建立压力/泵速/阀开度到流量的静态和动态模型；
   - 建立开胶、收胶、回抽响应延迟模型；
   - 输出：`Q(t)`、出胶延迟、流量滞后、压力窗口。

2. **胶条截面预测模型**
   - 直线段：`A=Q/v` + 截面形状因子；
   - 曲率/转角段：引入实际速度曲线、曲率、加速度和角点停留时间；
   - 曲面段：引入喷嘴高度、法向角、表面曲率；
   - 输出：胶宽、胶高、截面积、胶位偏差、缺陷风险评分。

3. **轨迹-工艺参数优化器**
   - 输入 CAD 样条、胶条设计规格、设备约束、机器人约束；
   - 优化速度、姿态、高度、流量、压力、起停提前量、转角补偿；
   - 输出机器人程序和点胶控制参数表。

4. **现场标定补偿**
   - 机器人基坐标/工装坐标标定；
   - TCP/胶嘴自动标定；
   - 工件扫描与 CAD 配准；
   - 生成全局刚体偏置 + 局部路径修正。

5. **3D 视觉检测闭环**
   - 试件/首件检测胶宽、高、体积、位置；
   - 自动计算偏差并回写模型参数；
   - 对断胶/起停/转角缺陷生成局部修补或参数调整建议。

---

## 7. 分阶段实施方案：面向单台机器人 4 天调试目标

### 阶段一：胶宽/胶位基础预测模型（0–6 个月）

目标：覆盖直线和缓曲率胶段，减少现场基础试胶。

**工作内容**

- 选取 1–2 种典型胶材、1 套泵阀系统、1 种胶嘴规格；
- 建立材料黏度/温度基础数据库；
- 通过标准试板 DOE 建立 `速度-流量-高度-角度 → 胶宽/胶高/位置` 模型；
- 将模型嵌入离线轨迹生成软件；
- 建立首件 3D 检测流程。

**验收指标建议**

- 直线段胶宽预测误差 ≤ ±0.5 mm；
- 直线段胶位误差经标定后 ≤ ±0.5 mm；
- 现场调试由传统多轮试胶减少到 1–2 轮；
- 单机器人基础导入与验证控制在 6–7 天。

### 阶段二：转角、起停胶、曲面区域质量预测和参数优化（6–12 个月）

目标：解决现场最耗时的转角堆胶、起停缺陷、曲面高度变化。

**工作内容**

- 采集转角半径、夹角、速度规划、流量响应与堆胶关系；
- 建立起胶/收胶延迟和回抽模型；
- 建立曲面法向、喷嘴高度、姿态变化对胶条截面的影响模型；
- 开发速度-流量同步表和角点局部补偿算法；
- 引入贝叶斯优化/主动学习，减少 DOE 数量。

**验收指标建议**

- 转角胶宽/胶高超差点减少 70% 以上；
- 起停缺陷长度减少 50% 以上；
- 典型零件现场调试压缩至 4–5 天；
- 离线程序一次导入后，80% 以上胶段无需人工修改轨迹。

### 阶段三：现场视觉检测、误差补偿和闭环控制（12–24 个月）

目标：实现“虚拟调试 + 首件验证 + 少量自动补偿”，达到单台机器人约 4 天。

**工作内容**

- 部署 3D 胶条检测：在线或离线首件扫描；
- 引入 TCP 自动检查、喷嘴偏差补偿；
- 工件基准扫描与 CAD 配准，生成轨迹整体/局部偏置；
- 检测结果自动回写仿真模型和参数优化器；
- 对关键缺陷实现自动修补或下一件自适应修正。

**4 天调试节拍建议**

| 天数 | 主要任务 | 输出 |
|---|---|---|
| Day 0（进场前） | 离线完成轨迹、可达性、碰撞、节拍、胶条质量预测、参数表 | 可导入机器人程序、点胶参数、风险清单 |
| Day 1 | 机器人/工装/工具/TCP 标定，现场模型对齐 | 坐标补偿矩阵、TCP 偏差报告 |
| Day 2 | 干跑 + 首件低风险试胶 + 3D 检测 | 胶宽/高/位偏差图、局部参数修正 |
| Day 3 | 全路径试胶 + 转角/起停局部优化 | 合格程序 V1、缺陷闭环报告 |
| Day 4 | 连续件验证、节拍验证、交付冻结 | 量产程序、参数包、检测追溯模板 |

---

## 8. 项目核心创新点提炼

1. **从“轨迹仿真”升级为“胶条质量仿真”**：不仅看机器人能否走到、是否干涉、节拍是否满足，还预测胶宽、胶高、截面积、位置偏差和缺陷风险。
2. **从“现场试错调试”升级为“虚拟调试 + 少量验证”**：将大量 DOE 和参数寻优前移到仿真和台架，现场只做标定、首件验证和局部补偿。
3. **从“固定样条曲线输出”升级为“轨迹、速度、压力、流量协同优化”**：把机器人速度曲线、计量系统动态和胶条目标规格统一优化。
4. **从“仿真与现场脱节”升级为“标定补偿后的仿真轨迹直接投产”**：通过基坐标、TCP、工件配准和视觉反馈缩小虚实差距。
5. **从“事后检测”升级为“检测数据驱动模型迭代”**：将 3D 检测结果用于模型校正、参数推荐和缺陷预防。

---

## 9. 最终建议方案

### 9.1 最推荐技术组合

建议采用：

- **离线平台**：Process Simulate/DELMIA/RoboDK/企业自研 OLP 任选其一作为几何与机器人程序平台；
- **胶条质量模型**：简化物理模型 + 台架 DOE 数据驱动校正；
- **设备模型**：泵阀/管路/压力/流量动态模型；
- **优化算法**：规则补偿 + 贝叶斯优化/高斯过程/主动学习；
- **现场补偿**：机器人基坐标、TCP 自动标定、工件 3D 配准；
- **检测系统**：3D 激光轮廓或环绕式 3D 胶条检测；
- **闭环方式**：第一步采用首件/批次闭环，成熟后升级关键段在线闭环。

### 9.2 为什么适合 4 天目标

- 单纯 OLP 无法解决胶条质量，需要现场反复试胶；单纯 3D 检测只能发现问题，不能提前减少试错；单纯 CFD 太慢且难落地。
- 混合模型可在进场前给出可执行参数初值，显著减少现场试胶次数。
- 标定补偿可把仿真轨迹与现场实物对齐，避免把大量时间花在手动改点。
- 3D 检测可量化首件偏差，自动定位问题属于“胶量/速度/高度/位置/TCP/工件偏差”的哪一类。
- 贝叶斯优化和主动学习适合少样本现场调参，可把“经验师傅多轮试错”变成“少量有目的试验”。

### 9.3 风险与边界

- **未找到可靠来源**证明当前主流 OLP 软件可直接、通用地预测汽车焊装胶条宽度/高度/断胶/拉丝等全质量指标；公开资料更多强调几何仿真、离线编程和虚拟调试。
- **未找到可靠来源**证明已有商业系统能在无需材料试验、无需现场检测的情况下实现所有胶材和所有零件的“仿真即生产”。
- 因此，本项目应避免承诺“一步取消所有现场试胶”，更合理目标是：先把现场试胶从反复人工调试压缩为基于模型的首件验证和少量闭环修正。

---

## 10. 参考资料清单

1. Coherix 3D inline bead inspection and adaptive process control: https://coherix.com/predator3d/
2. Coherix 3D TCP Locator: https://coherix.com/coherix-3d-tcp-locator/
3. Coherix Auto Repair for Adhesive Dispensing: https://coherix.com/auto-repair-for-adhesive-dispensing/
4. Atlas Copco integrated bead inspection: https://www.atlascopco.com/en-ca/itba/plp/dispensing-potting-bonding/integrated-bead-inspection
5. Atlas Copco RTVision.3d: https://www.atlascopco.com/en-ca/itba/products/quality-inspection-systems-21013.22148/rtvision.3d-sku731216
6. Nordson Process Sentry PLC controller: https://www.nordson.com/en/products/industrial-coating-solutions-products/process-sentry-plc-system-controller
7. Nordson-Coherix integration: https://coherix.com/nordson-coherix-fully-integrated-bead-dispensing-inspection-and-process-control-solution/
8. ABB Body-in-White dispensing: https://new.abb.com/products/robotics/manufacturing-solutions/body-in-white/technologies-and-process-expertise/mechanical-joining-techniques
9. Dürr sealing process: https://www.durr.com/en/products/sealing-gluing-technology/sealing-process
10. Siemens Process Simulate: https://www.siemens.com/en-gb/products/tecnomatix/process-simulate-software/
11. Siemens/RAMPF glue dispensing digital twin case: https://resources.sw.siemens.com/en-US/case-study-rampf-production-systems/
12. ScienceDirect, Digital twin modeling of robotic gluing system: https://www.sciencedirect.com/science/article/abs/pii/S0278612525001177
13. Springer, Automated human-in-the-loop commissioning: https://link.springer.com/article/10.1007/s00170-025-15121-w
14. arXiv, Lumped-Parameter Modeling and Control for Robotic High-Viscosity Fluid Dispensing: https://arxiv.org/abs/2210.10747
15. Frontiers, Modeling contact dispensing of conductive adhesives: https://www.frontiersin.org/articles/10.3389/fmats.2023.1183747
16. Modus Advanced FIP gasket guide: https://www.modusadvanced.com/form-in-place-gasket-guide
17. RBTX bead dispensing control: https://learn.rbtx.com/knowledge-resource/controlling-your-bead-in-dispensing/
18. Automate.org dispensing robots: https://www.automate.org/robotics/industry-insights/dispensing-profits-with-dispensing-robots
19. RoboDK robot programs: https://www.robodk.com/doc/en/Robot-Programs.html
20. RoboDK robot calibration: https://robodk.com/doc/en/Robot-Calibration-Creaform-Offline-setup.html
21. HA-TEC sealant inspection: https://ha-tec.com/solutions/vision/sealant-inspection
22. CN107702653B patent: https://patents.google.com/patent/CN107702653B/zh
