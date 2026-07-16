# AI Agents Python Projects

This repository contains practical Python projects focused on Artificial Intelligence, Large Language Models, Generative AI, and AI-powered applications.

The projects were developed as part of my studies in a course from Hashtag Treinamentos and reorganized into a professional portfolio structure by technology area:

- OpenAI
- LangChain
- Hugging Face

The repository is also designed to be expanded in the future with new AI agent projects, experiments, integrations, and production-oriented examples.

## Repository Structure

```text
ai-agents-python-projects/
├── openai-projects/
│   ├── 00-basic-chat-completion/
│   ├── 01-video-caption-generator/
│   ├── 02-image-generation/
│   ├── 03-audio-generation/
│   ├── 04-text-moderation/
│   ├── README.md
│   └── requirements.txt
│
├── langchain-projects/
│   ├── 00-chat-openai/
│   ├── 01-prompt-template/
│   ├── 02-review-analysis-chain/
│   ├── 03-python-chatbot/
│   ├── README.md
│   └── requirements.txt
│
├── hugging-face-projects/
│   ├── 00-hugging-face-datasets/
│   ├── 01-local-model-examples/
│   ├── 02-inference-client/
│   ├── README.md
│   └── requirements.txt
│
├── .gitignore
├── settings.json
└── README.md
```

## Project Goals

The main goals of this repository are:

- practice Python applied to AI projects;
- understand how to use LLM APIs and AI model providers;
- build small but practical Generative AI applications;
- organize AI projects in a clean portfolio structure;
- explore OpenAI, LangChain, and Hugging Face tools;
- prepare a foundation for future AI agents projects.

## Main Topics Covered

This repository includes projects related to:

- chat completions
- prompt engineering
- text generation
- text summarization
- text moderation
- speech-to-text
- text-to-speech
- image generation
- video caption generation
- Hugging Face datasets
- local model execution
- remote inference APIs
- Streamlit interfaces
- LangChain chains
- memory and chat history
- output parsers
- structured outputs
- AI application architecture

## OpenAI Projects

The `openai-projects` folder contains projects using the OpenAI API.

These projects explore different OpenAI capabilities, including text, audio, image, moderation, and transcription.

## Projects

```text
openai-projects/
├── 00-basic-chat-completion/
├── 01-video-caption-generator/
├── 02-image-generation/
├── 03-audio-generation/
├── 04-text-moderation/
├── README.md
└── requirements.txt
```

## Main Concepts

The OpenAI module covers:

- chat completions
- message roles
- API client configuration
- video transcription
- subtitle generation
- image generation
- image variations
- text-to-speech
- audio generation
- content moderation
- safe API key usage

## Example Applications

### Basic Chat Completion

A simple example showing how to send messages to an OpenAI model and receive a response.

### Video Caption Generator

A project that extracts or processes audio from a video and generates subtitles using speech-to-text.

### Image Generation

A project that generates images from prompts and creates image variations.

### Audio Generation

A project that converts text into generated audio.

### Text Moderation

A project that checks whether a text violates moderation categories.

## LangChain Projects

The `langchain-projects` folder contains projects focused on LangChain concepts and LLM application workflows.

LangChain is used to structure prompts, chains, parsers, memory, and chatbot behavior.

## Projects

```text
langchain-projects/
├── 00-chat-openai/
├── 01-prompt-template/
├── 02-review-analysis-chain/
├── 03-python-chatbot/
├── README.md
└── requirements.txt
```

## Main Concepts

The LangChain module covers:

- ChatOpenAI
- Hugging Face models with LangChain
- message types
- prompt templates
- composed prompts
- partial variables
- output parsers
- structured JSON outputs
- Pydantic models
- chains
- RunnableLambda
- LangSmith tracing
- Streamlit chat interfaces
- memory and conversation history

## Example Applications

### Chat with OpenAI and Hugging Face

A basic chat application using LangChain with OpenAI and Hugging Face models.

### Prompt Templates and Output Parsers

Examples showing how to create reusable prompts and parse model outputs into strings, lists, JSON, and structured Pydantic objects.

### Review Analysis Chain

A chain that analyzes product reviews, extracts structured information, saves intermediate data, and generates a summary.

### Python Learning Chatbot

A chatbot focused on answering Python programming questions, using chat history and LangChain memory concepts.

## Hugging Face Projects

The `hugging-face-projects` folder contains projects focused on Hugging Face datasets, models, pipelines, and remote inference.

It includes examples with both local model execution and API-based inference.

## Projects

```text
hugging-face-projects/
├── 00-hugging-face-datasets/
├── 01-local-model-examples/
├── 02-inference-client/
├── README.md
└── requirements.txt
```

## Main Concepts

The Hugging Face module covers:

- Hugging Face Hub
- datasets
- pandas with Hugging Face files
- Transformers pipelines
- local model execution
- text summarization
- text generation
- text-to-speech
- text-to-image
- Stable Diffusion
- Diffusers
- Accelerate
- InferenceClient
- Streamlit AI tools app
- API token management

## Example Applications

### Hugging Face Datasets

A basic project showing how to load and explore datasets from the Hugging Face Hub.

### Local Model Examples

Examples using local Hugging Face models for:

- text summarization
- text generation
- text-to-speech
- text-to-image

### Inference Client App

A Streamlit application that uses Hugging Face remote models through the Inference Client.

The app includes:

- text generation
- text summarization
- chat completion

## Local Models vs Remote Inference

This repository includes both local and remote model examples.

## Local Models

Local models are loaded and executed on the local machine.

Examples use libraries such as:

- `transformers`
- `diffusers`
- `torch`

Advantages:

- more control over execution;
- useful for experimentation;
- can work offline after downloading models.

Limitations:

- may require strong hardware;
- can be slow on CPU;
- large models may require GPU acceleration.

## Remote Inference

Remote inference uses APIs to call hosted models.

Examples use:

- OpenAI API
- Hugging Face Inference Client

Advantages:

- no need to download large models;
- easier to run on lightweight machines;
- useful for prototypes and applications.

Limitations:

- requires internet connection;
- may require API keys or tokens;
- may have rate limits or costs.

## Environment Variables

Some projects require API keys or tokens.

Create a `.env` file in the repository root when needed.

Example:

```env
OPENAI_API_KEY=your_openai_api_key_here
HF_TOKEN=your_hugging_face_token_here
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token_here
```

The `.env` file must never be committed to GitHub.

Make sure `.env` is included in `.gitignore`.

## Setup

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Each main folder has its own `requirements.txt`.

Install dependencies for OpenAI projects:

```bash
python -m pip install -r openai-projects/requirements.txt
```

Install dependencies for LangChain projects:

```bash
python -m pip install -r langchain-projects/requirements.txt
```

Install dependencies for Hugging Face projects:

```bash
python -m pip install -r hugging-face-projects/requirements.txt
```

## Running the Projects

Each project folder includes its own README with specific instructions.

In general, Python scripts can be executed with:

```bash
python filename.py
```

Streamlit applications can be executed with:

```bash
streamlit run main.py
```

Example:

```bash
cd hugging-face-projects/02-inference-client
streamlit run main.py
```

## Generated Files

Some projects generate files such as:

- audio files
- image files
- subtitle files
- temporary outputs

These files should not be committed to GitHub.

Recommended `.gitignore` entries:

```gitignore
.venv/
venv/
.env
__pycache__/
*.py[cod]
.DS_Store
generated/
*.mp3
*.wav
*.m4a
*.mp4
*.mov
*.avi
*.mkv
*.srt
*.png
*.jpg
*.jpeg
*.webp
```

## Future Improvements

This repository is structured to support future AI agent projects.

Possible future additions include:

- autonomous AI agents
- tool-calling agents
- RAG applications
- vector databases
- document question-answering
- multi-agent workflows
- AI assistants with memory
- backend APIs for AI applications
- deployment examples
- cloud integrations

## Learning Outcomes

Through these projects, I practiced:

- using AI APIs in Python;
- building AI-powered applications;
- working with LLMs and multimodal models;
- organizing code into reusable functions;
- creating Streamlit interfaces;
- managing environment variables safely;
- structuring projects for a technical portfolio;
- understanding the differences between OpenAI, LangChain, and Hugging Face.

## Status

This repository is in progress and will continue to be expanded with new AI, LLM, and AI agent projects.
