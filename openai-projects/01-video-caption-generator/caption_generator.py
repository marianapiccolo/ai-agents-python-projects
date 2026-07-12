from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from pydub import AudioSegment


def generate_captions(uploaded_file, context_prompt: str = "") -> str:
    """
    Generate SRT captions from an uploaded video or audio file.

    The function extracts the audio, sends it to the OpenAI transcription model,
    and saves the generated subtitles in SRT format.
    """

    # Load environment variables from the .env file
    load_dotenv()

    # Create an OpenAI client
    client = OpenAI()

    # Define the project folder based on the current file location
    project_folder = Path(__file__).parent

    # Create a folder to store generated files
    output_folder = project_folder / "generated"
    output_folder.mkdir(exist_ok=True)

    # Define output file paths
    audio_file_path = output_folder / "audio.mp3"
    subtitle_file_path = output_folder / "captions.srt"

    # Get the uploaded file extension without the dot
    file_extension = Path(uploaded_file.name).suffix.replace(".", "")

    # Make sure the file pointer is at the beginning
    uploaded_file.seek(0)

    # Load the uploaded video or audio file
    audio = AudioSegment.from_file(
        file=uploaded_file,
        format=file_extension
    )

    # Export the extracted audio as an MP3 file
    audio.export(audio_file_path, format="mp3")

    # Open the audio file and send it to the transcription model
    with open(audio_file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-1",
            language="pt",
            response_format="srt",
            prompt=context_prompt
        )

    # Save the transcription as an SRT subtitle file
    with open(subtitle_file_path, "w", encoding="utf-8") as subtitle_file:
        subtitle_file.write(transcription)

    return transcription