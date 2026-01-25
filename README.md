# LLM-Agent-Demo: 极简课程答疑智能体

<p align="center"> <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg"/> <img src="https://img.shields.io/badge/LLM-智谱AI GLM4-red.svg"/> <img src="https://img.shields.io/badge/版本-1.0.0-brightgreen.svg"/> <img src="https://img.shields.io/badge/许可证-MIT-yellow.svg"/> </p>

<p align="center">
<a href="https://github.com/luongthimydieu/Course-Q-A-Agent">
<img src="https://img.shields.io/badge/GitHub-Repository-blue?logo=github"/>
</a>
<a href="https://cnb.cool/jin.twelve/Course-Q-A-Agent">
<img src="https://img.shields.io/badge/TencentCNB-代码仓库-007ACC?logo=tencent"/>
</a>


一个基于大型语言模型的轻量级课程答疑助手，专为计算机专业学习场景设计。通过简洁的代码演示LLM智能体的核心实现原理，适合学习、教学和快速原型开发。

## ✨ 核心特性

### 🎯 专有角色设定 - 预置"计算机专业助教"角色，针对课程学习场景优化

### 💬 持续对话能力 - 自动维护对话历史，支持多轮上下文交互

### ⚡ 极简实现 - 核心代码仅30行，清晰展示LLM智能体工作原理

### 🔌 标准API兼容 - 遵循OpenAI API标准，易于切换不同模型后端

### 🚀 开箱即用 - 简单配置即可运行，无需复杂依赖

## 🚀 快速开始

**前置要求**

- Python 3.8+
- 有效的智谱AI API Key（[申请地址](https://open.bigmodel.cn/)）

**安装步骤**

- 克隆仓库

```bash
git clone https://github.com/luongthimydieu/Course-Q-A-Agent.git
cd Course-Q-A-Agent
```

- 安装依赖

```bash
pip install -r requirements.txt
```

- 配置API密钥

复制环境变量配置文件：

```bash
cp .env.example .env
```

编辑.env文件，填入您的API密钥：

```ini
ZHIPU_API_KEY=your_actual_api_key_here
```

- 使用方法

在项目根目录下，直接运行 main.py 即可启动命令行交互程序：

```bash
python main.py
```

程序启动后，您可以在命令行中输入问题，智能体会以计算机专业助教的身份进行回答。

输入 **退出** 可以退出程序。

### 交互示例：

```bash
🎓 计算机专业智能答疑助手
==================================================
💡 输入'清空记忆'清除对话历史
🚪 输入'退出'结束对话

你: 什么是面向对象编程的三大特性？

🤖 助手: 面向对象编程的三大特性是：
1. 封装（Encapsulation） - 将数据和方法包装在类中...
2. 继承（Inheritance） - 子类可以继承父类的属性和方法...
3. 多态（Polymorphism） - 同一操作作用于不同对象产生不同行为...

你: 能举个例子说明多态吗？

🤖 助手: 当然！以图形绘制为例，有一个基类Shape...
```

## 🏗️ 项目架构

### 📁 文件结构

```text
Course-Q-A-Agent/
├── agent.py          # 核心智能体类 (CourseAgent) 定义
├── main.py           # 命令行交互入口程序
├── requirements.txt  # Python项目依赖包列表
├── .env.example      # 环境变量配置文件示例
└── README.md         # 项目说明文档
```

## 💻 核心实现

项目的核心逻辑位于 agent.py 中的 CourseAgent 类：

```python
class CourseAgent:
    def __init__(self, api_key):
        self.client = ZhipuAI(api_key=api_key) # 初始化智谱AI客户端
        self.history = [{"role": "system", "content": "你是计算机专业助教"}] # 设定系统角色

    def chat(self, user_input):
        self.history.append({"role": "user", "content": user_input}) # 记录用户输入
        # 调用GLM-4-Flash模型
        response = self.client.chat.completions.create(
            model="glm-4-flash",
            messages=self.history
        )
        reply = response.choices[0].message.content # 获取模型回复
        self.history.append({"role": "assistant", "content": reply}) # 记录助手回复
        return reply
```

## 🎯 核心功能

| 功能 | 说明 |
|------|------|
| **专有角色扮演** | 智能体被设定为"计算机专业助教"，针对课程学习场景进行针对性答疑 |
| **持续对话** | 自动维护对话历史，实现多轮上下文连贯的交互体验 |
| **简易集成** | 代码结构清晰、轻量，易于集成到其他项目或进行功能扩展 |
| **开箱即用** | 提供完整的依赖列表和环境配置示例，一键安装即可运行 |
| **API标准化** | 遵循OpenAI API标准，便于切换不同模型后端 |

## 📈 后续开发建议

### 🎨 功能扩展
| 方向 | 实现建议 | 难度 |
|------|----------|------|
| **文件处理** | 添加PDF/PPT/Word文档解析功能 | ⭐⭐ |
| **联网搜索** | 集成搜索引擎API获取最新信息 | ⭐⭐⭐ |
| **知识库检索** | 结合向量数据库实现RAG功能 | ⭐⭐⭐⭐ |
| **多轮对话优化** | 添加对话状态管理和话题跟踪 | ⭐⭐ |

### 🌐 界面开发
- **Web界面**：使用Gradio或Streamlit快速搭建Web界面
- **桌面应用**：使用PyQt或Tkinter开发桌面客户端
- **API服务**：使用FastAPI或Flask提供HTTP API接口

### 🔧 工程优化
- 添加日志记录和错误处理
- 实现对话历史持久化存储
- 添加API调用频率限制和缓存
- 支持多模型切换（OpenAI、DeepSeek等）

### 🎓 教学定制
- 为特定课程定制专业知识库
- 添加编程代码执行和调试功能
- 集成在线评测系统接口
- 添加学习进度跟踪功能

## 🤝 贡献指南
**我们欢迎各种形式的贡献！以下是参与步骤：**

- Fork 项目仓库

- 创建特性分支 (git checkout -b feature/AmazingFeature)

- 提交更改 (git commit -m 'Add some AmazingFeature')

- 推送到分支 (git push origin feature/AmazingFeature)

- 创建 Pull Request

**开发规范**

- 遵循PEP 8代码规范

- 添加适当的注释和文档

- 为新功能编写测试用例

- 更新README中的相关部分

## 📝 常见问题

**Q: 如何获取智谱AI API Key？**

**A:** 访问智谱AI开放平台，注册账号并创建API Key。

**Q: 支持哪些Python版本？**

**A:** 支持Python 3.8及以上版本。

**Q: 如何修改系统提示词？**

**A:** 在agent.py中修改__init__方法中的system角色内容。

**Q: 可以商用吗？**

**A:** 本项目采用MIT许可证，允许商用，但需遵守智谱AI API的使用条款。

## 📄 许可证

本项目采用 MIT 许可证 - 查看 LICENSE 文件了解详情。

## 🧑‍💻 维护者

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/luongthimydieu">
        <img src="https://avatars.githubusercontent.com/luongthimydieu?v=4" width="60px;" alt="你的头像"/><br />
        <sub><b>luongthimydieu</b></sub>
      </a><br />
    </td>
  </tr>
</table>

## 🙏 致谢

- 感谢智谱AI提供优秀的GLM模型
- 灵感来源于实际教学中的答疑需求
- 感谢所有贡献者和用户的支持

<p align="center">
  <sub>如果这个项目对您有帮助，请给个 ⭐️ 支持一下！</sub>
</p>