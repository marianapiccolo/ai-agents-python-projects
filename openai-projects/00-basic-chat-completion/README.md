# Basic Chat Completion

This project is a simple example of how to send a text prompt to an OpenAI model using Python.

The main goal is to understand the basic structure of an OpenAI API request and how to access the model response.

## Features

- Load environment variables from a `.env` file
- Create an OpenAI client
- Send a text prompt to a chat model
- Access the response message
- Print the response role and content

## Technologies

- Python
- OpenAI API
- Python-dotenv

## Project Structure

```text
00-basic-chat-completion/
├── main.py
└── README.md
```

## How It Works

The script follows a simple workflow:

```text
User prompt
    ↓
OpenAI chat completion request
    ↓
Model response
    ↓
Response role and content are printed
```

## Code Overview

The project creates an OpenAI client:

```python
client = OpenAI()
```

Then it sends a message to the model:

```python
response = client.chat.completions.create(
    model="gpt-5.5",
    messages=[
        {
            "role": "user",
            "content": "Why is Python a good programming language?"
        }
    ]
)
```

After that, it extracts the first response message:

```python
response_message = response.choices[0].message
```

And prints:

```python
print("Role:", message_role)
print("Content:", message_content)
```

## Setup

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r openai-projects/requirements.txt
```

Create a `.env` file in the repository root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Example

From the project folder:

```bash
cd openai-projects/00-basic-chat-completion
python main.py
```

## Learning Goals

The main goals of this project are:

- Understand how to initialize the OpenAI client
- Learn the basic structure of a chat completion request
- Understand the `messages` format with roles and content
- Access the model response from the API result
