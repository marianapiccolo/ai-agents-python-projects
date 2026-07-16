# Summarization Model with Hugging Face

This project introduces how to use Hugging Face models with the `transformers` library.

The main goal is to understand how to load a pre-trained summarization model and use it to summarize long text.

## Official Model Pages

- facebook/bart-large-cnn: https://huggingface.co/facebook/bart-large-cnn
- google/pegasus-xsum: https://huggingface.co/google/pegasus-xsum

## Technologies

- Python
- Hugging Face
- Transformers
- PyTorch

## Project Structure

```text
01-summarization-model/
├── main.py
└── README.md
```

## How It Works

The project uses a Hugging Face pipeline for text summarization.

```text
Long text
    ↓
Hugging Face summarization pipeline
    ↓
Pre-trained model
    ↓
Short summary
```

## Transformers Pipeline

The `pipeline` function is a high-level API from Hugging Face Transformers.

It allows developers to use pre-trained models for common tasks with little code.

Example:

```python
from transformers import pipeline

summarizer = pipeline(
    task="summarization",
    model="google/pegasus-xsum"
)
```

The task defines what the model should do.

The model defines which pre-trained model should be used.

## Summarization

Summarization is the task of reducing a long text into a shorter version while keeping the main ideas.

In this project, the model receives a long text about the Greek language and generates a summary.

Example:

```python
response = summarizer(
    text,
    max_length=140,
    min_length=30,
    do_sample=False
)
```

## Parameters

### `max_length`

Defines the maximum length of the generated summary.

### `min_length`

Defines the minimum length of the generated summary.

### `do_sample=False`

Makes the output more deterministic.  
This means the model is less random and more consistent across executions.

## CUDA Note

The course example used:

```python
device="cuda"
```

CUDA is a technology that allows PyTorch to use NVIDIA GPUs for faster processing.

On macOS, CUDA is usually not available because it is specific to NVIDIA GPUs.

For this reason, the project code does not force CUDA by default.

If running on a machine with a compatible NVIDIA GPU, the pipeline can be configured with:

```python
summarizer = pipeline(
    task="summarization",
    model="google/pegasus-xsum",
    device="cuda"
)
```

## Setup

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required libraries:

```bash
python -m pip install transformers torch torchvision
```

Update the requirements file:

```bash
python -m pip freeze > hugging-face-projects/requirements.txt
```

## Running the Example

From the project folder:

```bash
cd hugging-face-projects/01-summarization-model
python main.py
```

## Requirements

The main dependencies used in this project are:

```text
transformers
torch
torchvision
```

Some dependencies in `requirements.txt` are installed automatically by these main packages.

## Learning Goals

The main goals of this project are:

- Understand what Hugging Face models are
- Learn how to use the `transformers` library
- Use a pre-trained model with `pipeline`
- Run a summarization model locally
- Understand basic summarization parameters
- Understand when CUDA can be used for acceleration
