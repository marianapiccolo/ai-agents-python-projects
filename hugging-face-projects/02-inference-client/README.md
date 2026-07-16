# Hugging Face Inference Client

This project introduces how to use Hugging Face models through the Inference Client.

The main goal is to understand how to use models hosted on Hugging Face without downloading them locally.

## Technologies

- Python
- Hugging Face Hub
- InferenceClient
- Python-dotenv

## Project Structure

```text
02-inference-client/
├── hfapi_summarization.py
├── hfapi_text_generation.py
└── README.md
```

## How It Works

The project uses the Hugging Face `InferenceClient` to call a remote model.

```text
Text input
    ↓
InferenceClient
    ↓
Remote Hugging Face model
    ↓
Model response
```

## Local Models vs Inference Client

### Local models

Local models are loaded with libraries such as `transformers`.

Example:

```python
from transformers import pipeline

summarizer = pipeline(
    task="summarization",
    model="google/pegasus-xsum"
)
```

This approach may download and run the model locally.

### Inference Client

The Inference Client calls models through the Hugging Face API.

Example:

```python
from huggingface_hub import InferenceClient

client = InferenceClient()
```

This approach allows using models without downloading them locally.

## Summarization Example

This project uses the `facebook/bart-large-cnn` model for summarization.

Example:

```python
response = client.summarization(
    text,
    model="facebook/bart-large-cnn"
)
```

## Authentication

A Hugging Face token may be required.

Create a `.env` file in the repository root:

```env
HF_TOKEN=your_hugging_face_token_here
```

or:

```env
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token_here
```

The `.env` file is ignored by Git and should never be committed.

## Setup

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required libraries:

```bash
python -m pip install huggingface-hub python-dotenv
```

Update the requirements file:

```bash
python -m pip freeze > hugging-face-projects/requirements.txt
```

## Running the Example

From the project folder:

```bash
cd hugging-face-projects/02-inference-client
python hfapi_summarization.py
```

## Learning Goals

The main goals of this project are:

- Understand what the Hugging Face Inference API is
- Use `InferenceClient` to call remote models
- Run a summarization model without downloading it locally
- Understand the difference between local model execution and API-based inference
- Practice storing API tokens safely with environment variables

## Status

Project in progress as part of the Hugging Face module.

# Hugging Face Inference Client

This project introduces how to use Hugging Face models through the Inference Client.

The main goal is to understand how to use models hosted on Hugging Face without downloading them locally.

## Technologies

- Python
- Hugging Face Hub
- InferenceClient
- Python-dotenv

## Project Structure

```text
02-inference-client/
├── hfapi_summarization.py
├── hfapi_text_generation.py
└── README.md
```

## How It Works

The project uses the Hugging Face `InferenceClient` to call remote models through the Hugging Face API.

```text
Input
  ↓
InferenceClient
  ↓
Remote Hugging Face model
  ↓
Model response
```

This means the model does not need to be downloaded or executed locally.

## Local Models vs Inference Client

### Local models

Local models are loaded with libraries such as `transformers` or `diffusers`.

Example:

```python
from transformers import pipeline

summarizer = pipeline(
    task="summarization",
    model="google/pegasus-xsum"
)
```

This approach may download and run the model on the local machine.

### Inference Client

The Inference Client calls models through the Hugging Face API.

Example:

```python
from huggingface_hub import InferenceClient

client = InferenceClient()
```

This approach allows the project to use remote models without downloading them locally.

## Summarization Example

The `hfapi_summarization.py` file shows how to summarize text using a remote Hugging Face model.

It uses the `facebook/bart-large-cnn` model.

Example:

```python
response = client.summarization(
    text,
    model="facebook/bart-large-cnn"
)
```

Workflow:

```text
Long text
  ↓
InferenceClient
  ↓
Remote summarization model
  ↓
Summary
```

This is useful when the goal is to reduce a long text into a shorter version while keeping the main ideas.

## Text Generation Example

The `hfapi_text_generation.py` file shows how to generate text using a remote Hugging Face model through the Inference Client.

It uses the `meta-llama/Llama-3.2-3B-Instruct` model.

Example:

```python
client = InferenceClient(
    model="meta-llama/Llama-3.2-3B-Instruct"
)

response = client.text_generation(prompt)
```

Workflow:

```text
Prompt
  ↓
InferenceClient
  ↓
Remote text generation model
  ↓
Generated text
```

This is useful when the goal is to send a prompt and receive a generated answer from a hosted language model.

## Authentication

A Hugging Face token may be required to use the Inference API.

Create a `.env` file in the repository root:

```env
HF_TOKEN=your_hugging_face_token_here
```

or, depending on the configuration:

```env
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token_here
```

The `.env` file is ignored by Git and should never be committed.

## Setup

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required libraries:

```bash
python -m pip install huggingface-hub python-dotenv
```

Update the requirements file:

```bash
python -m pip freeze > hugging-face-projects/requirements.txt
```

## Running the Examples

From the project folder:

```bash
cd hugging-face-projects/02-inference-client
```

Run the summarization example:

```bash
python hfapi_summarization.py
```

Run the text generation example:

```bash
python hfapi_text_generation.py
```

## Requirements

The main dependencies used in this project are:

```text
huggingface-hub
python-dotenv
```

Some dependencies in `requirements.txt` may be installed automatically by these main packages.

## Important Usage Note

Using Hugging Face hosted models through the Inference API may have limits depending on the account, model, and provider configuration.

It is important to:

- keep the Hugging Face token private;
- avoid committing `.env` files;
- test with small prompts first;
- check model availability on Hugging Face;
- understand that some models may require permissions or gated access.

## Learning Goals

The main goals of this project are:

- Understand what the Hugging Face Inference API is
- Use `InferenceClient` to call remote models
- Run summarization without downloading the model locally
- Run text generation without downloading the model locally
- Understand the difference between local model execution and API-based inference
- Practice storing API tokens safely with environment variables
