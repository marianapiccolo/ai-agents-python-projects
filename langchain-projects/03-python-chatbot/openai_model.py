from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage
from langchain_core.prompts.chat import MessagesPlaceholder
from langchain_openai.chat_models import ChatOpenAI

# Load environment variables from the .env file
load_dotenv()

# Create a chat prompt template with a system instruction and a message history placeholder
chat_template = ChatPromptTemplate(
    [
        SystemMessage(
            content=(
                "Answer the user with direct and concise responses, "
                "but always answer the question clearly. "
                "The questions are about programming in {topic}. "
                "For any question outside this topic, answer only: "
                "'I am not an expert on this topic.'"
            )
        ),
        MessagesPlaceholder(variable_name="history")
    ],
    partial_variables={
        "topic": "Python"
    }
)

# Create a LangChain chat model connected to OpenAI
model = ChatOpenAI()

# Create the chain
chain = chat_template | model