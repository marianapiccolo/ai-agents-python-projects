from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
# import base64

# Load environment variables from the .env file
load_dotenv()

# Create an OpenAI client
client = OpenAI()

# Define the project folder based on the current file location
project_folder = Path(__file__).parent

# Create a folder to store generated files
output_folder = project_folder / "generated"
output_folder.mkdir(exist_ok=True)

# Define the output audio file path
audio_file_path = output_folder / "generated_audio.wav"


# -------------------------------------------------------------------
# Option 1: Generate audio directly from a text input
# -------------------------------------------------------------------
# This is the simplest way to create speech from text.
# The model receives a text and returns an audio file.

text_input = (
    "If you want to learn Python from scratch, this audio introduces "
    "a practical learning path with real projects and hands-on exercises."
)

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    response_format="wav",
    input=text_input
)

# Save the generated audio file locally
response.write_to_file(audio_file_path)

print("Audio generated successfully.")
print(f"Audio saved at: {audio_file_path}")


# -------------------------------------------------------------------
# Option 2: Generate text and audio together from a prompt
# -------------------------------------------------------------------
# This example uses a multimodal model that can return both text and audio.
# It is useful when the model needs to create the message content first
# and then return it as speech.
#
# This code is commented because it is only an alternative example.
# To use it, uncomment the block below.

# response = client.chat.completions.create(
#     model="gpt-4o-audio-preview",
#     modalities=["text", "audio"],
#     audio={
#         "format": "wav",
#         "voice": "alloy"
#     },
#     messages=[
#         {
#             "role": "user",
#             "content": (
#                 "Create a short audio message inviting beginners to learn Python "
#                 "through a practical learning path with real projects and hands-on exercises."
#             )
#         }
#     ]
# )
#
# audio_data = response.choices[0].message.audio.data
# audio_bytes = base64.b64decode(audio_data)
#
# multimodal_audio_file_path = output_folder / "multimodal_generated_audio.wav"
#
# with open(multimodal_audio_file_path, "wb") as audio_file:
#     audio_file.write(audio_bytes)
#
# print("Multimodal audio generated successfully.")
# print(f"Audio saved at: {multimodal_audio_file_path}")