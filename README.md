# LLM-Agent-Demo: 极简课程答疑智能体

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg"/>
  <img src="https://img.shields.io/badge/LLM-智谱AI GLM4-red.svg"/>
  <img src="https://img.shields.io/badge/核心代码-30行-brightgreen.svg"/>
</p>
<p align="left">
<a href="https://github.com/luongthimydieu/Course-Q-A-Agent">
<img src="https://img.shields.io/badge/GitHub-Repository-blue?logo=github"/>
</a>
<a href="https://cnb.cool/jin.twelve/Course-Q-A-Agent">
<img src="https://img.shields.io/badge/TencentCNB-代码仓库-007ACC?logo=tencent"/>
</a>
<a href="https://stars.github.com/nominate/">
  <img src="https://img.shields.io/badge/给个-Star-欢迎!-brightgreen"/>
</a>

一个基于大型语言模型（LLM）构建的轻量级课程答疑助手。

该项目通过简洁的代码演示了如何利用智谱AI的GLM-4-Flash模型，创建一个能够持续对话的计算机专业课程智能体。

## 🎯 核心代码 (`agent.py`)

```python
class CourseAgent:
    def __init__(self, api_key):
        self.client = ZhipuAI(api_key=api_key)
        self.history = [{"role": "system", "content": "你是计算机专业助教"}]
    
    def chat(self, user_input):
        self.history.append({"role": "user", "content": user_input})
        response = self.client.chat.completions.create(
            model="glm-4-flash",
            messages=self.history
        )
        reply = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": reply})
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

## 🚀 快速开始

**前置要求**
### 前置要求

- Python 3.8+
- 有效的智谱AI API Key（[申请地址](https://open.bigmodel.cn/)）

**安装步骤**

- 克隆仓库

```bash
git clone https://github.com/luongthimydieu/Course-Q-A-Agent.git
cd Course-Q-A-Agent
```

- 安装依赖
项目所需依赖较少，使用pip快速安装：

```bash
pip install -r requirements.txt
```

- 配置API密钥

将项目根目录下的 .env.example 文件复制并重命名为 .env。

在 .env 文件中填入您自己的智谱AI API Key：

```ini
API_KEY=your_zhipuai_api_key_here
```
重要：请确保 .env 文件已添加到 .gitignore 中，避免将密钥提交至版本控制系统。

- 使用方法

在项目根目录下，直接运行 main.py 即可启动命令行交互程序：

```bash
python main.py
```

程序启动后，您可以在命令行中输入问题，智能体会以计算机专业助教的身份进行回答。输入 **退出** 可以退出程序。

### 使用示例
```bash
> 什么是面向对象编程？
助教：面向对象编程（OOP）是一种编程范式，它将数据和方法封装在对象中...

> 能举个例子吗？
助教：当然！例如，我们可以创建一个"学生"类，包含姓名、学号等属性...
```

## 📁 项目文件结构

```text
Course-Q-A-Agent/
├── agent.py          # 核心智能体类 (CourseAgent) 定义
├── main.py           # 命令行交互入口程序
├── requirements.txt  # Python项目依赖包列表
├── .env.example      # 环境变量配置文件示例
└── README.md         # 项目说明文档（本文档）
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

## 📈 项目动态
![Star History Chart](https://api.star-history.com/svg?repos=luongthimydieu/Course-Q-A-Agent&type=Date)

## 🙏 致谢

- 感谢智谱AI提供优秀的GLM模型
- 灵感来源于实际教学中的答疑需求

<p align="center">
  <sub>如果这个项目对您有帮助，请给个 ⭐️ 支持一下！</sub>
</p>