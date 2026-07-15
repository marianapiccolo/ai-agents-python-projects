# LangChain Projects

This folder contains practical projects developed during the LangChain module of my AI Agents with Python studies.

The goal of this module is to understand how to build AI applications using LangChain concepts such as chat models, prompt templates, output parsers, chains, memory, Streamlit interfaces, Hugging Face integration, OpenAI integration, and LangSmith tracing.

## Technologies

- Python
- LangChain
- LangChain OpenAI
- LangChain Hugging Face
- OpenAI API
- Hugging Face models
- Streamlit
- Pydantic
- Output parsers
- LangSmith
- Python-dotenv

## Project Structure

```text
langchain-projects/
├── 00-chat-openai/
│   ├── chat.py
│   ├── huggingface_model.py
│   ├── openai_model.py
│   └── README.md
│
├── 01-prompt-template/
│   ├── composed_prompt.py
│   ├── optimized_review_parser.py
│   ├── output_parser_model.py
│   ├── pydantic_output_parser.py
│   ├── string_output_parser.py
│   └── README.md
│
├── 02-review-analysis-chain/
│   ├── main.py
│   └── README.md
│
├── 03-python-chatbot/
│   ├── chat.py
│   ├── memory.py
│   ├── openai_model.py
│   └── README.md
│
├── requirements.txt
└── README.md
```

## Projects

### 00 - Chat with OpenAI and Hugging Face

This project introduces the basic use of chat models with LangChain.

It includes examples using:

- `ChatOpenAI` with OpenAI models;
- `HuggingFaceEndpoint` with Hugging Face models;
- `ChatHuggingFace`;
- LangChain message types;
- Streamlit chat interface.

Main concepts:

- `SystemMessage`
- `HumanMessage`
- `AIMessage`
- `ChatOpenAI`
- `HuggingFaceEndpoint`
- `ChatHuggingFace`
- Streamlit chat UI
- Session state for conversation history

This project shows how LangChain can work with different model providers using a similar structure.

---

### 01 - Prompt Templates and Output Parsers

This project explores how to create reusable prompts and standardize model responses.

It includes examples of:

- simple prompt templates;
- composed prompt templates;
- partial variables;
- chat prompt templates;
- string output parsing;
- comma-separated list parsing;
- JSON output parsing;
- Pydantic schemas;
- optimized model calls.

Main concepts:

- `PromptTemplate`
- `ChatPromptTemplate`
- `partial_variables`
- `StrOutputParser`
- `CommaSeparatedListOutputParser`
- `JsonOutputParser`
- `Pydantic`
- structured outputs

This project is important because real AI applications often need predictable and structured responses, not only free text.

---

### 02 - Review Analysis Chain

This project analyzes product reviews using LangChain chains.

It extracts structured information from reviews, saves intermediate results, and generates a final summary analysis.

Main concepts:

- creating chains with `prompt | model | parser`;
- combining multiple chains;
- using `JsonOutputParser`;
- using `StrOutputParser`;
- defining output schemas with Pydantic;
- saving results with a custom runnable;
- tracing the chain with LangSmith.

The workflow is:

```text
Product reviews
      ↓
PromptTemplate
      ↓
ChatOpenAI
      ↓
JsonOutputParser
      ↓
Structured review evaluations
      ↓
RunnableLambda
      ↓
Save results to file
      ↓
Summary chain
      ↓
Final text analysis
```

This project shows how LangChain can be used to create AI pipelines with multiple steps.

---

### 03 - Python Chatbot

This project is a Python-focused chatbot built with LangChain, OpenAI, Streamlit, and LangChain memory.

The chatbot answers questions about Python programming and keeps conversation history.

Main concepts:

- `ChatPromptTemplate`
- `MessagesPlaceholder`
- `RunnableWithMessageHistory`
- `InMemoryChatMessageHistory`
- Streamlit chat interface
- session-based memory
- topic-specific assistant behavior

The workflow is:

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

This project shows how to build a chatbot that keeps context during the conversation.

## Main Concepts Learned

## Chat Models

LangChain provides standard interfaces to work with different chat models.

Examples used in this module:

```python
model = ChatOpenAI()
```

and:

```python
llm = HuggingFaceEndpoint(...)
model = ChatHuggingFace(llm=llm)
```

This allows applications to switch or compare model providers more easily.

## Message Types

LangChain represents conversations using message objects.

The main message types used were:

- `SystemMessage`: defines assistant behavior;
- `HumanMessage`: represents the user input;
- `AIMessage`: represents the model response.

Example:

```python
messages = [
    SystemMessage(content="Answer briefly."),
    HumanMessage(content="What is Python?")
]
```

## Prompt Templates

Prompt templates make prompts reusable and dynamic.

Example:

```python
prompt_template = PromptTemplate.from_template(
    "Answer in {language}. User message: {message}"
)
```

This is useful when prompts need variables such as:

- language;
- tone;
- response length;
- user message;
- business rules;
- output format.

## ChatPromptTemplate

`ChatPromptTemplate` is used to create prompts in chat format.

It works well with messages such as system, human, and AI messages.

Example:

```python
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "Answer questions about {topic}."),
        ("human", "{message}")
    ]
)
```

## Output Parsers

Output parsers standardize model responses.

This module used:

- `StrOutputParser`;
- `CommaSeparatedListOutputParser`;
- `JsonOutputParser`.

Parsers are useful because language models can respond in different formats, but applications often need predictable data.

## Pydantic Schemas

Pydantic was used to define structured response formats.

Example:

```python
class ReviewEvaluation(BaseModel):
    positive_review: bool
    worth_buying: bool
    positive_points: list[str]
    negative_points: list[str]
```

This helps guide the model to return structured data that can be used in application logic.

## Chains

Chains connect multiple LangChain components into a pipeline.

Example:

```python
chain = prompt_template | model | parser
```

This means:

```text
PromptTemplate → Model → Parser
```

Chains make the workflow cleaner and easier to extend.

## Combining Chains

Multiple chains can be combined to create larger workflows.

Example:

```python
global_chain = review_analysis_chain | summary_chain
```

This allows one chain output to become the next chain input.

## RunnableLambda

`RunnableLambda` allows regular Python functions to be added inside a LangChain chain.

Example:

```python
save_reviews_runnable = RunnableLambda(save_reviews_to_file)
```

This is useful when a pipeline needs custom logic, such as:

- saving files;
- transforming data;
- logging;
- validating information;
- calling external services.

## Memory

The chatbot project used memory with:

```python
RunnableWithMessageHistory
```

and:

```python
InMemoryChatMessageHistory
```

This allows the chain to keep conversation history and answer with context.

## LangSmith

LangSmith was used to trace and monitor LangChain executions.

It helps inspect:

- chain inputs;
- generated prompts;
- model responses;
- intermediate steps;
- execution time;
- errors and debugging information.

Environment variables used for LangSmith:

```env
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGSMITH_PROJECT=your_project_name_here
```

The `.env` file is ignored by Git and should never be committed.

## Setup

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the LangChain module dependencies:

```bash
python -m pip install -r langchain-projects/requirements.txt
```

Create a `.env` file in the repository root:

```env
OPENAI_API_KEY=your_openai_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here

LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGSMITH_PROJECT=your_project_name_here
```

Depending on the Hugging Face configuration, the token may also be named:

```env
HF_TOKEN=your_huggingface_token_here
```

## Running the Projects

Each project has its own README with specific instructions.

Examples:

```bash
cd langchain-projects/00-chat-openai
streamlit run chat.py
```

```bash
cd langchain-projects/01-prompt-template
python composed_prompt.py
```

```bash
cd langchain-projects/02-review-analysis-chain
python main.py
```

```bash
cd langchain-projects/03-python-chatbot
streamlit run chat.py
```

## Requirements

The main dependencies used in this module are:

```text
langchain
langchain-core
langchain-openai
langchain-huggingface
langsmith
openai
streamlit
python-dotenv
pydantic
torch
transformers
huggingface-hub
```

Some dependencies in `requirements.txt` are subdependencies installed automatically by these main packages.

## Git Ignore Notes

The repository should not include:

- `.env` files;
- API keys;
- generated files;
- temporary outputs;
- virtual environments;
- cache folders.

Important ignored files and folders include:

```text
.env
.venv/
__pycache__/
generated/
```

## Important Cost Note

These projects use APIs that may generate costs.

OpenAI API calls, model invocations, and repeated chatbot messages can count as usage.

It is important to:

- test with small inputs;
- avoid unnecessary repeated executions;
- check generated outputs before running again;
- monitor usage in OpenAI, Hugging Face, and LangSmith dashboards when applicable.

## Learning Goals

The main goals of this module were:

- Understand the role of LangChain in AI applications
- Use chat models through LangChain
- Compare OpenAI and Hugging Face integrations
- Create reusable prompts with `PromptTemplate`
- Use `ChatPromptTemplate` for chat-based applications
- Standardize model outputs with output parsers
- Use Pydantic to define structured response formats
- Build chains using LangChain Expression Language
- Combine chains into larger AI workflows
- Add custom Python functions with `RunnableLambda`
- Trace and debug chains with LangSmith
- Build a chatbot with memory using LangChain and Streamlit
- Organize LangChain projects for a GitHub portfolio

## Status

LangChain module completed.
