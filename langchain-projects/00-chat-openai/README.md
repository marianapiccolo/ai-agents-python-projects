# LangChain Chat with OpenAI and Hugging Face

This project is a simple chatbot built with LangChain and Streamlit.

The main goal is to understand how LangChain works with chat models and how to connect different model providers, such as OpenAI and Hugging Face, using a similar message structure.

## Features

- Create a basic chat model with LangChain
- Use OpenAI through `ChatOpenAI`
- Use Hugging Face models through `HuggingFaceEndpoint`
- Build a simple chat interface with Streamlit
- Store the conversation history with Streamlit session state
- Work with LangChain message types such as `SystemMessage`, `HumanMessage`, and `AIMessage`
- Handle reasoning model outputs that include `<think>` sections

## Technologies

- Python
- LangChain
- LangChain OpenAI
- LangChain Hugging Face
- OpenAI API
- Hugging Face Inference Endpoint
- Streamlit
- Python-dotenv
- Torch

## Project Structure

```text
00-chat-openai/
├── chat.py
├── openai_model.py
├── huggingface_model.py
└── README.md
```

## How It Works

The project uses LangChain message objects to structure the conversation.

```text
System message
      ↓
User message
      ↓
LangChain chat model
      ↓
AI response
      ↓
Streamlit chat interface
```

## OpenAI Model

The OpenAI version uses `ChatOpenAI`.

```python
model = ChatOpenAI()
```

This connects LangChain to an OpenAI chat model.

The model receives a list of messages and returns an AI response:

```python
response = model.invoke(messages)
```

## Hugging Face Model

The Hugging Face version uses `HuggingFaceEndpoint` and `ChatHuggingFace`.

```python
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B"
)

model = ChatHuggingFace(llm=llm)
```

This allows a Hugging Face model to be used through the LangChain chat interface.

## Streamlit Interface

The `chat.py` file creates a simple web chat interface.

The conversation is stored with:

```python
st.session_state["messages"]
```

This is important because Streamlit reruns the script after each user interaction.  
Using `session_state` keeps the chat history while the app is open.

## Message Types

LangChain uses different message types to represent a conversation.

### SystemMessage

Defines the assistant behavior.

Example:

```python
SystemMessage(
    content="Answer the questions in a short way."
)
```

### HumanMessage

Represents the user message.

Example:

```python
HumanMessage(content=prompt)
```

### AIMessage

Represents the model response.

Example:

```python
AIMessage(content=final_answer)
```

## Handling Reasoning Output

Some reasoning models may return internal thinking sections using tags such as:

```text
<think>
...
</think>
```

In this project, the chat interface checks if the response contains `</think>` and displays only the final answer after that tag.

This keeps the interface cleaner for the user.

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
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

Depending on the Hugging Face configuration, the token may also be named:

```env
HF_TOKEN=your_huggingface_token_here
```

## Running the App

From the project folder:

```bash
cd langchain-projects/00-chat-openai
streamlit run chat.py
```

## Learning Goals

The main goals of this project are:

- Understand the basic LangChain chat model structure
- Learn how to use `ChatOpenAI`
- Learn how to use Hugging Face models with LangChain
- Understand LangChain message types
- Build a simple chatbot interface with Streamlit
- Store conversation history with Streamlit session state
- Compare different model providers inside the same LangChain workflow
