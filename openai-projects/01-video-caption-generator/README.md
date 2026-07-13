# Video Caption Generator

This project is a simple Streamlit application that generates subtitles from video or audio files using the OpenAI API.

The app allows the user to upload a video or audio file, extract its audio, transcribe the content, and generate subtitles in `.srt` format.

## Features

- Upload video or audio files
- Extract audio from video files
- Generate transcriptions using OpenAI speech-to-text
- Export subtitles in `.srt` format
- Preview the generated subtitles
- Download the generated subtitle file
- Add a context prompt to improve transcription quality

## Technologies

- Python
- OpenAI API
- Whisper transcription model
- Streamlit
- Pydub
- Python-dotenv

## Project Structure

```text
01-video-caption-generator/
├── main.py
├── caption_generator.py
├── README.md
└── generated/
    ├── audio.mp3
    └── captions.srt
```

The `generated/` folder is created automatically when the app runs. It stores temporary audio and subtitle files.

## How It Works

The application follows this workflow:

```text
Uploaded video or audio
        ↓
Audio extraction with Pydub
        ↓
Audio transcription with OpenAI
        ↓
SRT subtitle generation
        ↓
Subtitle preview and download
```

## Setup

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install openai python-dotenv pydub streamlit
```

Update the requirements file:

```bash
python -m pip freeze > openai-projects/requirements.txt
```

Create a `.env` file in the repository root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the App

From the project folder, run:

```bash
cd openai-projects/01-video-caption-generator
streamlit run main.py
```

Then open the local URL displayed in the terminal.

## Usage

1. Open the Streamlit app.
2. Upload a video or audio file.
3. Add a short context prompt to help the model understand the content.
4. Generate the subtitles.
5. Preview the result in the app.
6. Download the `.srt` subtitle file.

## Example Context Prompt

```text
This is Portuguese content about software development.
```

The context prompt helps the transcription model understand the topic of the audio and can improve the quality of the generated subtitles.

## Notes

This project does not include example video or audio files in the repository.

Media files and generated subtitle files are ignored to avoid uploading course content, private files, or large files to GitHub.

Ignored files include:

```text
*.mp4
*.mov
*.avi
*.mkv
*.mp3
*.wav
*.m4a
*.srt
generated/
```

## Learning Goals

The main goals of this project are:

- Practice using the OpenAI API with Python
- Understand audio transcription workflows
- Convert video or audio input into subtitle files
- Build a simple user interface with Streamlit
- Apply good practices with environment variables, project structure, and documentation
