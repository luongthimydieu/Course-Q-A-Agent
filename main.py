from agent import CourseAgent
import os

API_KEY = os.getenv("ZHIPU_API_KEY") or input("请输入API Key: ")

print("=" * 50)
print("🎓 计算机专业智能答疑助手")
print("=" * 50)
print("💡 输入'清空记忆'清除对话历史")
print("🚪 输入'退出'结束对话\n")

agent = CourseAgent(api_key=API_KEY)

while True:
    user_input = input("你: ").strip()
    if not user_input: continue
    
    if user_input == "退出":
        print("\n👋 感谢使用，再见！")
        break
    
    if user_input == "清空记忆":
        print(f"\n🤖 助手: {agent.clear_memory()}")
        continue
    
    try:
        reply = agent.chat(user_input)
        print(f"\n🤖 助手: {reply}\n")
    except Exception as e:
        print(f"\n❌ 错误: {str(e)}")
