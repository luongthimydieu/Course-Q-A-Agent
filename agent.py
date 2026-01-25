from zhipuai import ZhipuAI

class CourseAgent:
    """计算机专业课程助教智能体，基于智谱AI大模型"""
    
    def __init__(self, api_key):
        """
        初始化课程助教智能体
        
        参数:
            api_key (str): 智谱AI平台的API密钥
        """
        # 创建智谱AI客户端实例
        self.client = ZhipuAI(api_key=api_key)
        
        # 初始化对话历史，包含系统角色设定
        self.history = [
            {
                "role": "system", 
                "content": "你是计算机专业助教，回答简洁准确"  # 系统提示词，定义AI角色和行为
            }
        ]
    
    def chat(self, user_input):
        """
        与用户进行对话
        
        参数:
            user_input (str): 用户的输入文本
            
        返回:
            str: AI助教的回复内容
        """
        # 将用户输入添加到对话历史
        self.history.append({"role": "user", "content": user_input})
        
        # 调用智谱AI的聊天完成接口
        response = self.client.chat.completions.create(
            model="glm-4-flash",      # 使用GLM-4-Flash模型
            messages=self.history,     # 传入完整的对话历史
            temperature=0.7            # 控制回复随机性的参数(0.0-1.0)
        )
        
        # 提取AI的回复内容
        assistant_reply = response.choices[0].message.content
        
        # 将AI回复添加到对话历史，保持上下文连贯
        self.history.append({"role": "assistant", "content": assistant_reply})
        
        return assistant_reply
    
    def clear_memory(self):
        """
        清除对话历史，重置为初始状态
        
        返回:
            str: 操作确认信息
        """
        system_msg = self.history[0]  # 保留系统提示词
        self.history = [system_msg]   # 重置对话历史，只保留系统角色
        return "记忆已清空"             # 返回操作结果提示

    def search_database(query):
        """
        预留功能：连接课程知识库进行查询
        
        参数:
            query (str): 查询关键词或问题
        """
        # TODO: 实现与课程知识库的连接和查询逻辑
        pass

    def run_code(code):
        """
        预留功能：执行用户输入的代码
        
        参数:
            code (str): 需要执行的代码
        """
        # TODO: 实现代码安全执行环境
        # 注意：需要添加安全沙箱机制，防止恶意代码执行
        pass