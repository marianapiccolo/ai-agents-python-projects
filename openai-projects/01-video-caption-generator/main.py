from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from pydub import AudioSegment

# Load environment variables from the .env file
load_dotenv()

# Create an OpenAI client
client = OpenAI()

# Define the project folder based on the current file location
project_folder = Path(__file__).parent

# Define input and output file paths
video_file_path = project_folder / "video.mp4"
audio_file_path = project_folder / "audio.mp3"
subtitle_file_path = project_folder / "captions.srt"

# Get the video file extension without the dot. ex: mp4
video_file_extension = video_file_path.suffix.replace(".", "")

# Load the video file and extract its audio
audio = AudioSegment.from_file(
    file=video_file_path,
    format=video_file_extension
)

# Export the extracted audio as an MP3 file
audio.export(audio_file_path, format="mp3")

# Add context to help the transcription model understand the audio better
context_prompt = "The audio contains Portuguese content about software development."

# Open the extracted audio file and send it to the transcription model
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