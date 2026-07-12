from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Create an OpenAI client
client = OpenAI()

# Get the audio file path based on the current script location
audio_file_path = Path(__file__).parent / "audio.mp3"

# Open the audio file and send it to the transcription model
with open(audio_file_path, "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        file=audio_file,
        model="whisper-1",
        language="pt"
    )

# Display the transcription result
print(transcription.text)