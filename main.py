from agent import Agent

math_agent = Agent("MathAgent", "Solve math problems and equations.")
knowledge_agent = Agent("KnowledgeAgent", "Answer general knowledge questions.")
manager_agent = Agent("ManagerAgent", "Delegate the task to MathAgent or KnowledgeAgent.")

task = input("Enter your question: ")

# Manager decides which agent to assign
decision = manager_agent.think(f"This is the task: {task}. Which agent should solve it?")
print(f"Manager decided: {decision}")

if "math" in decision.lower():
    result = math_agent.think(task)
elif "knowledge" in decision.lower():
    result = knowledge_agent.think(task)
else:
    result = "Manager is confused!"

print("Final Answer:", result)
