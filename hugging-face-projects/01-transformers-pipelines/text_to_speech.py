from pathlib import Path

import soundfile as sf
import torch
from datasets import load_dataset
from transformers import pipeline

# Create a text-to-speech pipeline using a Hugging Face model
# The course uses device="cuda", but CUDA is only available with compatible NVIDIA GPUs.
# On macOS, it is better to run without forcing CUDA.
text_to_speech = pipeline(
    task="text-to-speech",
    model="microsoft/speecht5_tts"
    # device="cuda"
)

# Load speaker embeddings used by the SpeechT5 model
# Speaker embeddings help define the voice characteristics of the generated audio.
embeddings_dataset = load_dataset(
    "Matthijs/cmu-arctic-xvectors",
    split="validation"
)

# Select one speaker embedding from the dataset
speaker_embedding = torch.tensor(
    embeddings_dataset[0]["xvector"]
).unsqueeze(0)

# Text that will be converted into speech
text_input = (
    "Python is a powerful programming language for automation, "
    "data analysis, web development, and artificial intelligence."
)

# Generate speech from text
speech = text_to_speech(
    text_input,
    forward_params={
        "speaker_embeddings": speaker_embedding
    }
)

# Create a folder to store generated files
output_folder = Path(__file__).parent / "generated"
output_folder.mkdir(exist_ok=True)

# Define the output audio file path
audio_file_path = output_folder / "speech.wav"

# Save the generated speech as a WAV file
sf.write(
    audio_file_path,
    speech["audio"],
    samplerate=speech["sampling_rate"]
)

print("Audio generated successfully.")
print(f"Audio saved at: {audio_file_path}")