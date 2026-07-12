from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Create an OpenAI client
client = OpenAI()

# Define the project folder based on the current file location
project_folder = Path(__file__).parent

# Define input and output file paths
audio_file_path = project_folder / "audio.mp3"
subtitle_file_path = project_folder / "captions.srt"

# Add context to help the model understand the audio content better
context_prompt = "The audio contains Portuguese content about software development."

# Open the audio file and send it to the transcription model
with open(audio_file_path, "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        file=audio_file,
        model="whisper-1",
        language="pt",
        response_format="srt",
        prompt=context_prompt
    )

# Display the generated subtitles in the terminal
print(transcription)

# Save the transcription as an SRT subtitle file
with open(subtitle_file_path, "w", encoding="utf-8") as subtitle_file:
    subtitle_file.write(transcription)