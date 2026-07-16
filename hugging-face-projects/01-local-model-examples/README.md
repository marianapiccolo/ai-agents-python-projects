# Local Model Examples with Hugging Face

This project explores different Hugging Face model tasks executed locally with Python.

The main goal is to understand how to use local or directly loaded Hugging Face models for different AI tasks such as summarization, text generation, text-to-speech, and text-to-image generation.

## Technologies

- Python
- Hugging Face
- Transformers
- Diffusers
- PyTorch
- Datasets
- SoundFile

## Project Structure

```text
01-local-model-examples/
├── text_summarization.py
├── text_generation.py
├── text_to_speech.py
├── text_to_image.py
└── README.md
```

## Files

### `text_summarization.py`

This file shows how to summarize long text with a Hugging Face summarization pipeline.

Main concepts:

- `pipeline("summarization")`
- pre-trained summarization model
- `max_length`
- `min_length`

### `text_generation.py`

This file shows how to generate text from a prompt.

Main concepts:

- `pipeline("text-generation")`
- prompt-based generation
- `max_new_tokens`
- `temperature`
- model limitations

### `text_to_speech.py`

This file shows how to convert text into audio using the `microsoft/speecht5_tts` model.

Main concepts:

- `pipeline("text-to-speech")`
- speaker embeddings
- `datasets`
- `soundfile`
- WAV file generation

### `text_to_image.py`

This file shows how to generate an image from a text prompt using Stable Diffusion.

Main concepts:

- `StableDiffusionPipeline`
- `diffusers`
- text-to-image generation
- local image generation
- saving generated images

## Tasks Covered

This project includes examples of:

- text summarization
- text generation
- text-to-speech
- text-to-image

## Device Handling

Some course examples use:

```python
device="cuda"
```

CUDA is specific to NVIDIA GPUs.

In this project, the code is adapted to support different environments:

- `cuda` for NVIDIA GPUs
- `mps` for Apple Silicon
- `cpu` as fallback

This makes the examples more portable.

## Setup

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the main libraries:

```bash
python -m pip install transformers diffusers accelerate datasets pandas soundfile torch torchvision
```

Update the requirements file:

```bash
python -m pip freeze > hugging-face-projects/requirements.txt
```

## Running the Examples

Text summarization:

```bash
cd hugging-face-projects/01-local-model-examples
python text_summarization.py
```

Text generation:

```bash
cd hugging-face-projects/01-local-model-examples
python text_generation.py
```

Text to speech:

```bash
cd hugging-face-projects/01-local-model-examples
python text_to_speech.py
```

Text to image:

```bash
cd hugging-face-projects/01-local-model-examples
python text_to_image.py
```

## Generated Files

Some scripts create generated outputs, such as:

- audio files
- image files

These outputs should be stored in a `generated/` folder and ignored by Git.

## Learning Goals

The main goals of this project are:

- Understand how to load Hugging Face models locally
- Learn the difference between `transformers` and `diffusers`
- Practice common AI tasks with ready-to-use pipelines
- Work with text, audio, and image generation
- Understand device configuration for local execution
- Build a strong practical foundation before moving to inference APIs and the final project

## Status

Project completed as part of the Hugging Face module examples.
