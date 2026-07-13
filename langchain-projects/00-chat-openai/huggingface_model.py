import torch
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace

# Fix for a Streamlit + Torch compatibility warning/error
torch.classes.__path__ = []

# Load environment variables from the .env file
load_dotenv()

# Define the initial system message that controls the assistant behavior
messages = [
    SystemMessage(
        content=(
            "Answer the questions in a short way, but not too short. "
            "Use a maximum of 140 characters."
        )
    )
]

# Create a Hugging Face endpoint using an open-source model
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B"
)

# Wrap the Hugging Face endpoint as a LangChain chat model
model = ChatHuggingFace(llm=llm)


if __name__ == "__main__":
    # Simple terminal test
    user_message = input("Type your message: ")

    messages.append(HumanMessage(content=user_message))

    response = model.invoke(messages)

    print(response)
    print(type(response))
    print(response.content)
    print(response.type)