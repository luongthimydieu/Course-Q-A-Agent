# LLM-Agent-Demo: 极简课程答疑智能体

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg"/>
  <img src="https://img.shields.io/badge/LLM-智谱AI GLM4-red.svg"/>
  <img src="https://img.shields.io/badge/核心代码-30行-brightgreen.svg"/>
</p>

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