# AI for Soft Materials / LCE / Intelligent Actuators 一页总结

## 最值得关注的 10 个课题组

> 非官方排名，为基于方向相关性和领域影响力的综合判断。

1. **Rampi Ramprasad — Georgia Tech**：Polymer Genome、polyBERT、聚合物结构—性能预测；最适合学习 LCE 数据库和预测模型。
2. **Yuuya Nagata — NIMS**：自主高分子设计、合成机器人、NIMO/贝叶斯优化；最适合学习聚合物闭环实验。
3. **Nick Warren — University of Sheffield**：AI-powered polymer synthesis/self-driving polymer lab；聚合物自动化合成高度相关。
4. **Juan de Pablo — University of Chicago**：聚合物、液晶、软物质模拟；最适合 LCE 取向/相变/网络机理。
5. **Robert Katzschmann — ETH Zurich**：软机器人、人工肌肉、机器视觉闭环制造；最适合执行器应用端对标。
6. **Milad Abolhasani — NC State**：self-driving fluidic lab、闭环优化、微流控；适合搭建小型软材料 SDL。
7. **Andrew Ferguson — University of Chicago**：机器学习、统计热力学、软材料模拟；适合可解释软材料 AI。
8. **Rafael Gómez-Bombarelli — MIT**：生成式分子/材料设计；适合 LCE 单体和响应基元逆向设计。
9. **Philipp Rothemund — University of Stuttgart**：电液软执行器和性能优化；适合执行器性能指标对标。
10. **Timothy Swager — MIT**：聚合物传感、连续流、贝叶斯优化；适合自感知/环境响应器件。

## 最适合借鉴的 5 个方法

1. **LCE 专用聚合物信息学数据库**：从 Polymer Genome 学结构—性能表示，但加入取向、工艺、视频和动态驱动指标。
2. **机器视觉执行器表征**：从驱动视频自动提取曲率、弯曲角、响应时间、恢复时间、循环衰减。
3. **贝叶斯优化/主动学习闭环**：在小样本条件下推荐下一轮 LCE 配方、取向方式和器件几何。
4. **生成式 director field / 几何设计**：面向目标曲面、运动轨迹和力输出生成取向图案与结构参数。
5. **自感知软执行器集成**：将 LCE 驱动层与导电聚合物/CNT/离子凝胶/液态金属传感层集成。

## 未来方向一句话定位

**面向智能形变高分子材料，建立 AI 辅助分子—配方—取向—结构协同设计、机器视觉动态表征与闭环优化制备平台，实现可编程 LCE 人工肌肉和自感知柔性执行器。**

## 推荐 3 年发展路线

### 第 1 年：数据和机器视觉

* 建立 LCE 配方—取向—驱动数据库；
* 建立统一视频拍摄和刺激测试规范；
* 开发曲率、角度、响应时间和循环稳定性自动提取工具。

### 第 2 年：预测模型和实验推荐

* 建立配方—性能、多任务预测模型；
* 引入贝叶斯优化/主动学习；
* 完成第一轮 AI-assisted LCE screening。

### 第 3 年：闭环平台和器件示范

* 联合优化材料配方、取向图案、几何结构和驱动性能；
* 建立半自动闭环制备—表征—优化系统；
* 示范 LCE 人工肌肉、仿生夹爪或自感知软执行器。
