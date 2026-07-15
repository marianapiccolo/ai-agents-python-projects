# Python Chatbot with LangChain

This project is a Python-focused chatbot built with LangChain, OpenAI, Streamlit, and LangChain message history.

The main goal is to create a chatbot specialized in answering questions about Python programming while keeping the conversation history.

## Features

- Build a chatbot interface with Streamlit
- Use LangChain to connect a prompt template to an OpenAI chat model
- Use `ChatPromptTemplate` to define the assistant behavior
- Use `MessagesPlaceholder` to inject conversation history into the prompt
- Restrict the chatbot topic to Python programming
- Return a default answer for questions outside the defined topic
- Store visual chat messages with Streamlit session state
- Store model conversation history with `InMemoryChatMessageHistory`
- Use `RunnableWithMessageHistory` to add memory to the chain

## Technologies

- Python
- LangChain
- LangChain OpenAI
- OpenAI API
- Streamlit
- RunnableWithMessageHistory
- InMemoryChatMessageHistory
- Python-dotenv

## Project Structure

```text
03-python-chatbot/
├── chat.py
├── openai_model.py
├── memory.py
└── README.md
```

## How It Works

The project follows this workflow:

```text
User message
      ↓
Streamlit chat input
      ↓
RunnableWithMessageHistory
      ↓
InMemoryChatMessageHistory
      ↓
ChatPromptTemplate
      ↓
ChatOpenAI
      ↓
AI response
      ↓
Streamlit chat interface
```

## Prompt Template

The chatbot uses a system message to define its behavior.

The assistant is instructed to:

- answer directly and concisely;
- answer only questions about Python programming;
- refuse questions outside the topic with a default response.

Example concept:

```python
(
    "system",
    "Answer the user with direct and concise responses. The questions are about programming in {topic}."
)
```

The topic is defined as a partial variable:

```python
chat_template.partial(topic="Python")
```

This means the chatbot is configured as a Python programming assistant.

## MessagesPlaceholder

The project uses `MessagesPlaceholder` to insert previous conversation messages into the prompt.

```python
MessagesPlaceholder(variable_name="history")
```

This allows the model to receive the conversation history before answering the next user message.

## Chain with Memory

The basic chain connects the chat prompt template to the model:

```python
chain = chat_template | model
```

Then memory support is added with:

```python
chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history=get_session_history,
    input_messages_key="message",
    history_messages_key="history"
)
```

This creates a chain that can remember previous messages during the session.

## In-Memory Chat History

The project uses `InMemoryChatMessageHistory` to store conversation messages.

```python
conversations = {}

def get_session_history(session_id):
    if session_id not in conversations:
        conversations[session_id] = InMemoryChatMessageHistory()

    return conversations[session_id]
```

Each conversation is stored by `session_id`.

## Streamlit Session State

Streamlit session state is used to keep the messages visible in the chat interface.

```python
st.session_state["messages"]
```

This is useful because Streamlit reruns the script after each user interaction.

## Difference Between Streamlit State and LangChain Memory

`st.session_state` is used for the user interface.

`InMemoryChatMessageHistory` is used by LangChain to provide conversation history to the model.

```text
st.session_state
→ keeps messages visible in the Streamlit app.

InMemoryChatMessageHistory
→ keeps messages available to the LangChain chain.
```

## Setup

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r langchain-projects/requirements.txt
```

Create a `.env` file in the repository root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

The `.env` file is ignored by Git and should never be committed.

## Running the App

From the project folder:

```bash
cd langchain-projects/03-python-chatbot
streamlit run chat.py
```

Then open the local URL displayed in the terminal.

## Important Cost Note

This project uses the OpenAI API and may generate costs.

Each message sent to the chatbot can count as API usage. For this reason, it is important to:

- test with short messages;
- avoid sending repeated unnecessary requests;
- check OpenAI pricing before using the API extensively.

## Learning Goals

The main goals of this project are:

- Build a chatbot interface with Streamlit
- Understand how to use `ChatPromptTemplate`
- Understand how to use `MessagesPlaceholder`
- Create a topic-specific chatbot
- Connect a LangChain prompt to an OpenAI chat model
- Use Streamlit session state to display conversation history
- Use `RunnableWithMessageHistory` to add memory to a chain
- Use `InMemoryChatMessageHistory` to store messages in memory
- Understand the difference between UI history and model memory
