# Hugging Face Projects

This folder contains practical projects developed during the Hugging Face module.

The goal is to understand how to work with Hugging Face datasets, local models, pipelines, diffusion models, and remote inference using the Hugging Face Inference Client.

## Folder Structure

```text
hugging-face-projects/
├── 00-hugging-face-datasets/
│   ├── main.py
│   └── README.md
│
├── 01-local-model-examples/
│   ├── text_generation.py
│   ├── text_summarization.py
│   ├── text_to_image.py
│   ├── text_to_speech.py
│   └── README.md
│
├── 02-inference-client/
│   ├── hfapi_chat_completion.py
│   ├── hfapi_summarization.py
│   ├── hfapi_text_generation.py
│   ├── main.py
│   └── README.md
│
└── requirements.txt
```

## Projects Overview

## 00 - Hugging Face Datasets

This project introduces how to work with datasets from the Hugging Face Hub.

It covers:

- Hugging Face datasets
- loading datasets with the `datasets` library
- reading dataset files with pandas
- using `hf://` paths
- basic dataset exploration

Example concepts:

```python
from datasets import load_dataset
```

and:

```python
import pandas as pd

df = pd.read_csv("hf://datasets/Anthropic/EconomicIndex/onet_task_mappings.csv")
```

This project uses the Anthropic Economic Index dataset as an example.

## 01 - Local Model Examples

This project explores how to run Hugging Face models locally or directly through Python libraries.

It includes examples for:

- text summarization
- text generation
- text-to-speech
- text-to-image

## Text Summarization

The `text_summarization.py` file uses a Hugging Face summarization pipeline.

Example task:

```text
Long text
  ↓
Summarization model
  ↓
Short summary
```

Main library:

```python
from transformers import pipeline
```

## Text Generation

The `text_generation.py` file uses a text generation model from Hugging Face.

Example task:

```text
Prompt
  ↓
Text generation model
  ↓
Generated text
```

This example introduces model limitations, especially when using smaller models locally.

## Text to Speech

The `text_to_speech.py` file uses a Hugging Face text-to-speech model.

It uses:

- `transformers`
- `datasets`
- `torch`
- `soundfile`
- speaker embeddings

Example task:

```text
Text
  ↓
Text-to-speech model
  ↓
Generated audio file
```

## Text to Image

The `text_to_image.py` file uses Stable Diffusion through the `diffusers` library.

It uses:

```python
from diffusers import StableDiffusionPipeline
```

Example task:

```text
Text prompt
  ↓
Stable Diffusion model
  ↓
Generated image
```

This project also introduces:

- `diffusers`
- `accelerate`
- Stable Diffusion
- local image generation
- device configuration

## 02 - Inference Client

This project shows how to use Hugging Face models without downloading them locally.

It uses the Hugging Face `InferenceClient`.

Main library:

```python
from huggingface_hub import InferenceClient
```

It includes:

- remote summarization
- remote text generation
- remote chat completion
- Streamlit interface

## Streamlit AI Tools App

The `main.py` file provides a visual interface with three tools:

```text
Generate Text
Summarize Text
Open Chat
```

The app uses Hugging Face remote models through the Inference Client.

Example flow:

```text
User prompt
  ↓
Streamlit interface
  ↓
InferenceClient
  ↓
Remote Hugging Face model
  ↓
AI response
```

## Main Concepts Learned

This module covers the following concepts:

- Hugging Face Hub
- datasets
- local model execution
- remote model inference
- Transformers pipelines
- Diffusers pipelines
- text generation
- text summarization
- text-to-speech
- text-to-image
- chat completion
- Streamlit interface
- API token management
- environment variables
- model limitations
- CUDA and device configuration

## Local Models vs Remote Inference

## Local Models

Local models are loaded with libraries such as `transformers` or `diffusers`.

Example:

```python
from transformers import pipeline

model = pipeline(
    task="summarization",
    model="google/pegasus-xsum"
)
```

This approach may download and run the model on the local machine.

Advantages:

- more control
- can work offline after downloading
- useful for experimentation

Limitations:

- requires local hardware resources
- may be slow on CPU
- large models can be heavy
- GPU configuration may be needed

## Remote Inference

Remote inference uses the Hugging Face API through `InferenceClient`.

Example:

```python
from huggingface_hub import InferenceClient

client = InferenceClient()
```

This approach uses hosted models without downloading them locally.

Advantages:

- no need to download large models
- simpler to run on lightweight machines
- useful for applications and prototypes

Limitations:

- requires internet connection
- may require an API token
- may have usage limits
- model availability can depend on Hugging Face settings

## CUDA Note

Some course examples use:

```python
device="cuda"
```

CUDA is a technology that allows PyTorch to use NVIDIA GPUs.

On macOS, CUDA is usually not available because it is specific to NVIDIA GPUs.

For better portability, some examples can be adapted to use:

```text
cuda
→ NVIDIA GPU

mps
→ Apple Silicon acceleration on macOS

cpu
→ fallback option
```

## Environment Variables

Some projects require a Hugging Face token.

The token should be stored in a `.env` file in the repository root:

```env
HF_TOKEN=your_hugging_face_token_here
```

or:

```env
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token_here
```

The `.env` file must never be committed to GitHub.

## Setup

From the repository root, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies from the Hugging Face requirements file:

```bash
python -m pip install -r hugging-face-projects/requirements.txt
```

If installing manually, the main libraries used in this module are:

```bash
python -m pip install transformers datasets pandas huggingface-hub python-dotenv streamlit diffusers accelerate soundfile torch torchvision
```

## Updating Requirements

After installing new libraries, update the requirements file:

```bash
python -m pip freeze > hugging-face-projects/requirements.txt
```

## Running the Projects

## Run dataset example

```bash
cd hugging-face-projects/00-hugging-face-datasets
python main.py
```

## Run local model examples

```bash
cd hugging-face-projects/01-local-model-examples
python text_summarization.py
python text_generation.py
python text_to_speech.py
python text_to_image.py
```

## Run inference client app

```bash
cd hugging-face-projects/02-inference-client
streamlit run main.py
```

## Generated Files

Some scripts may generate audio or image files.

Generated files should not be committed to GitHub.

Recommended `.gitignore` entries:

```gitignore
generated/
*.wav
*.mp3
*.m4a
*.png
*.jpg
*.jpeg
*.webp
.env
```

## Learning Goals

The main goals of this module are:

- Understand the Hugging Face ecosystem
- Load and explore datasets from the Hugging Face Hub
- Use local models with `transformers`
- Use diffusion models with `diffusers`
- Generate text, summaries, audio, and images
- Use hosted models with the Hugging Face Inference Client
- Build a visual AI application with Streamlit
- Manage API tokens safely
- Understand the difference between local inference and remote inference
- Prepare practical AI projects for a professional portfolio

## Status

Hugging Face module completed.
