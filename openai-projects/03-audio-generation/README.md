# Audio Generation with OpenAI API

This project explores how to generate audio from text using the OpenAI API with Python.

The main goal is to understand how text-to-speech works and how to save generated audio files locally.

## Official Documentation

- Text to speech: https://developers.openai.com/api/docs/guides/text-to-speech

## Features

- Generate speech from a text input
- Save generated audio files locally
- Explore a direct text-to-speech workflow
- Keep an alternative multimodal audio generation example as reference
- Organize generated files in a dedicated output folder

## Technologies

- Python
- OpenAI API
- Text-to-speech
- Python-dotenv

## Project Structure

```text
03-audio-generation/
├── audio_generator.py
├── main.py
├── README.md
└── generated/
    └── generated_audio.wav
```

The `generated/` folder stores generated audio files and is ignored by Git.

## How It Works

### Option 1 - Text to speech

This approach receives a predefined text and converts it into an audio file.

```text
Text input
    ↓
OpenAI text-to-speech API
    ↓
Generated audio
    ↓
Local audio file
```

### Option 2 - Multimodal response with text and audio

This alternative approach uses a model that can generate both text and audio from a prompt.

```text
Prompt
    ↓
Model generates the message
    ↓
Model returns text and audio
    ↓
Audio file is saved locally
```

In this project, the multimodal example is kept commented as a reference.

## Setup

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install openai python-dotenv
```

Update the requirements file:

```bash
python -m pip freeze > openai-projects/requirements.txt
```

Create a `.env` file in the repository root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Example

From the project folder:

```bash
cd openai-projects/03-audio-generation
python audio_generator.py
```

The generated audio file will be saved inside the `generated/` folder.

## Important Cost Note

Audio generation uses the OpenAI API and may generate costs.

Each request can count as API usage. For this reason, it is important to:

- test with short texts;
- avoid running the script repeatedly without checking the output;
- keep generated files ignored by Git;
- check the official OpenAI pricing page before using the API extensively.

## Git Ignore Notes

Generated audio files are not included in this repository.

The following files and folders should be ignored:

```text
generated/
*.mp3
*.wav
*.m4a
```

## Learning Goals

The main goals of this project are:

- Practice text-to-speech generation with the OpenAI API
- Understand how to save generated audio files locally
- Compare direct text-to-speech with multimodal audio generation
- Apply good practices with environment variables, file structure, and documentation
