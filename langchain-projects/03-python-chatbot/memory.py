from langchain_core.chat_history import InMemoryChatMessageHistory

# Create an in-memory chat history
memory = InMemoryChatMessageHistory()

# Add example messages
memory.add_user_message("What is Python?")
memory.add_ai_message("Python is a programming language.")

# Display stored messages
print(memory.messages)