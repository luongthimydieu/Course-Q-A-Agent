# 导入课程助教智能体类
from agent import CourseAgent
import os  # 导入操作系统模块，用于环境变量管理

# 获取API密钥：优先从环境变量读取，如果不存在则要求用户输入
API_KEY = os.getenv("ZHIPU_API_KEY") or input("请输入API Key: ")

# 打印程序标题和欢迎信息
print("=" * 50)  # 打印分隔线
print("🎓 计算机专业智能答疑助手")  # 程序标题
print("=" * 50)  # 打印分隔线

# 打印使用说明和命令提示
print("💡 输入'清空记忆'清除对话历史")  # 清空记忆命令提示
print("🚪 输入'退出'结束对话\n")  # 退出命令提示，\n表示换行

# 创建课程助教智能体实例
agent = CourseAgent(api_key=API_KEY)

# 主循环：持续与用户交互直到退出
while True:
    # 获取用户输入并去除首尾空白字符
    user_input = input("你: ").strip()
    
    # 如果用户输入为空，跳过本次循环继续等待输入
    if not user_input:
        continue
    
    # 处理退出命令
    if user_input == "退出":
        print("\n👋 感谢使用，再见！")  # 退出提示信息
        break  # 退出while循环，结束程序
    
    # 处理清空记忆命令
    if user_input == "清空记忆":
        # 调用智能体的清空记忆方法，并打印返回的确认信息
        print(f"\n🤖 助手: {agent.clear_memory()}")
        continue  # 继续下一次循环
    
    # 处理普通对话请求
    try:
        # 调用智能体的聊天方法获取回复
        reply = agent.chat(user_input)
        # 格式化输出助手的回复
        print(f"\n🤖 助手: {reply}\n")  # \n用于在回复前后添加空行
    except Exception as e:
        # 异常处理：打印错误信息
        print(f"\n❌ 错误: {str(e)}")  # 将异常转换为字符串显示