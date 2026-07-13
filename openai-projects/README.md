# OpenAI Projects

This folder contains practical projects developed during the OpenAI module of my AI Agents with Python studies.

The goal of this module is to explore how to use the OpenAI API in Python through small, practical projects involving text generation, audio transcription, subtitle generation, image generation, text-to-speech, and moderation.

## Official Documentation Used

- Text generation: https://developers.openai.com/api/docs/guides/text
- Speech to text: https://developers.openai.com/api/docs/guides/speech-to-text
- Text to speech: https://developers.openai.com/api/docs/guides/text-to-speech
- Image generation: https://developers.openai.com/api/docs/guides/image-generation
- Moderation: https://developers.openai.com/api/docs/guides/moderation

## Technologies

- Python
- OpenAI API
- Python-dotenv
- Streamlit
- Pydub
- Requests
- DALL·E
- Whisper transcription model
- OpenAI Moderation model

## Project Structure

```text
openai-projects/
├── 00-basic-chat-completion/
│   ├── main.py
│   └── README.md
│
├── 01-video-caption-generator/
│   ├── main.py
│   ├── caption_generator.py
│   └── README.md
│
├── 02-image-generation/
│   ├── image_generator.py
│   ├── image_variations.py
│   └── README.md
│
├── 03-audio-generation/
│   ├── main.py
│   └── README.md
│
├── 04-text-moderation/
│   ├── main.py
│   └── README.md
│
├── README.md
└── requirements.txt
```

## Projects

### 00 - Basic Chat Completion

A simple example that sends a text prompt to an OpenAI model and prints the response.

Main concepts:

- OpenAI client setup
- Environment variables
- Basic text generation
- Chat completion request
- API response structure

### 01 - Video Caption Generator

A Streamlit application that generates subtitles from video or audio files.

Main concepts:

- Audio extraction from video files
- Speech-to-text transcription
- SRT subtitle generation
- Streamlit interface
- File upload and download
- Context prompts for better transcription

### 02 - Image Generation

A project that explores image generation and image variations using the OpenAI API.

Main concepts:

- Image generation from text prompts
- Image variation generation
- Downloading generated images from URLs
- Saving generated files locally
- Working with generated outputs

### 03 - Audio Generation

A project that explores how to generate audio from text using the OpenAI API.

Main concepts:

- Text-to-speech generation
- Saving audio files locally
- Direct speech generation from text
- Alternative multimodal audio generation example

### 04 - Text Moderation

A project that explores how to classify and moderate text using the OpenAI Moderation API.

Main concepts:

- Text moderation
- Flagged content detection
- Moderation categories
- Conditional logic for safety rules
- Content filtering use cases

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

The `.env` file is ignored by Git and should never be committed.

## Requirements

The main dependencies used in this module are:

```text
openai
python-dotenv
streamlit
pydub
requests
```

Some dependencies in `requirements.txt` are subdependencies installed automatically by these main packages.

## Running the Projects

Each project has its own README with specific instructions.

General example:

```bash
cd openai-projects/00-basic-chat-completion
python main.py
```

For the Streamlit project:

```bash
cd openai-projects/01-video-caption-generator
streamlit run main.py
```

## Git Ignore Notes

Generated files and sensitive files are not included in this repository.

Ignored files include:

```text
.env
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

This prevents uploading API keys, course files, generated media files, and large outputs to GitHub.

## Important Cost Note

These projects use the OpenAI API and may generate costs.

Some operations, such as image generation, image variations, audio generation, and transcription, can count as API usage.

It is important to:

- test with small inputs;
- avoid running scripts repeatedly without checking the output;
- keep generated files ignored by Git;
- check OpenAI pricing before using the API extensively.

## Learning Goals

The main goals of this module are:

- Practice using the OpenAI API with Python
- Understand different OpenAI capabilities
- Work with text, audio, image, and moderation models
- Organize multiple small AI projects in a single repository
- Apply good practices with environment variables, `.gitignore`, modular code, and documentation
- Build a portfolio-ready GitHub structure

## Status

OpenAI module completed.
