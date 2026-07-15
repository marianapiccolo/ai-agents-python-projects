from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts.chat import MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai.chat_models import ChatOpenAI

# Load environment variables from the .env file
load_dotenv()

# Dictionary used to store conversations by session ID
conversations = {}


def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    """
    Return the chat history for a given session.

    If the session does not exist yet, create a new in-memory history.
    """

    if session_id not in conversations:
        conversations[session_id] = InMemoryChatMessageHistory()

    return conversations[session_id]


# Create a chat prompt template with a system instruction and memory placeholder
chat_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            (
                "Answer the user with direct and concise responses, "
                "but always answer the question clearly. "
                "The questions are about programming in {topic}. "
                "For any question outside this topic, answer only: "
                "'I am not an expert on this topic.'"
            )
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{message}")
    ]
).partial(topic="Python")

# Create a LangChain chat model connected to OpenAI
model = ChatOpenAI()

# Create the basic chain
chain = chat_template | model

# Add message history support to the chain
chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history=get_session_history,
    input_messages_key="message",
    history_messages_key="history"
)