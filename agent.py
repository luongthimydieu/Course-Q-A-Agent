from zhipuai import ZhipuAI

class CourseAgent:
    def __init__(self, api_key):
        self.client = ZhipuAI(api_key=api_key)
        self.history = [{"role": "system", "content": "你是计算机专业助教，回答简洁准确"}]
    
    def chat(self, user_input):
        self.history.append({"role": "user", "content": user_input})
        response = self.client.chat.completions.create(
            model="glm-4-flash",
            messages=self.history,
            temperature=0.7
        )
        assistant_reply = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": assistant_reply})
        return assistant_reply
    
    def clear_memory(self):
        system_msg = self.history[0]
        self.history = [system_msg]
        return "记忆已清空"

def search_database(query):
    """预留：连接课程知识库"""
    pass

def run_code(code):
    """预留：执行代码"""
    pass
