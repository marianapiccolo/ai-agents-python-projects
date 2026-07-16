# Hugging Face Datasets

This project introduces the basic use of Hugging Face datasets with Python.

The main goal is to understand how datasets can be loaded from the Hugging Face Hub and used in Python projects.

## Topics Covered

- Basic PyTorch installation
- CUDA concept
- Hugging Face datasets
- Loading datasets with the `datasets` library
- Loading dataset files with pandas
- Reading CSV files directly from Hugging Face Hub

## Technologies

- Python
- PyTorch
- Torchvision
- Hugging Face Hub
- Hugging Face Datasets
- Pandas

## Project Structure

```text
00-hugging-face-datasets/
├── main.py
└── README.md
```

## PyTorch and CUDA

PyTorch is a popular library used in Machine Learning and Deep Learning projects.

It is commonly used by Hugging Face models for tensor operations and neural network execution.

CUDA is a technology from NVIDIA that allows compatible GPUs to accelerate deep learning workloads.

In simple terms:

```text
CPU
→ general-purpose processor

GPU
→ faster for many machine learning operations

CUDA
→ technology that allows PyTorch to use NVIDIA GPUs
```

On some machines, CUDA may not be available. For example, macOS computers usually do not use CUDA because CUDA is specific to NVIDIA GPUs.

## Hugging Face Datasets

Hugging Face provides a large collection of datasets through the Hugging Face Hub.

Datasets can be loaded in different ways.

### Option 1 - Using the datasets library

Example:

```python
from datasets import load_dataset

dataset = load_dataset("facebook/natural_reasoning", split="train")

print(dataset["question"])
```

This approach uses the Hugging Face `datasets` library.

It is useful when working with datasets directly in the Hugging Face format.

In this project, this dataset was kept as a commented example because it was too large for the course exercise.

### Option 2 - Using pandas with a Hugging Face file path

Example:

```python
import pandas as pd

dataset_path = "hf://datasets/Anthropic/EconomicIndex/onet_task_mappings.csv"

dataframe = pd.read_csv(dataset_path)

print(dataframe)
```

This approach reads a CSV file directly from a Hugging Face dataset repository.

It is useful when the dataset contains files that can be loaded as regular tabular data.

## Dataset Used

This project uses the following dataset file:

```text
Anthropic/EconomicIndex/onet_task_mappings.csv
```

The file is loaded directly with pandas using the `hf://` path.

## Authentication Note

Some Hugging Face datasets may require authentication.

In those cases, it may be necessary to log in with:

```bash
huggingface-cli login
```

or configure a Hugging Face token in the environment.

Example:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

The `.env` file should never be committed to GitHub.

## Setup

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required libraries:

```bash
python -m pip install torch torchvision datasets pandas
```

Update the requirements file:

```bash
python -m pip freeze > hugging-face-projects/requirements.txt
```

## Running the Example

From the project folder:

```bash
cd hugging-face-projects/00-hugging-face-datasets
python main.py
```

## Requirements

The main dependencies used in this project are:

```text
torch
torchvision
datasets
pandas
huggingface-hub
```

Some dependencies in `requirements.txt` are installed automatically by these main packages.

## Learning Goals

The main goals of this project are:

- Understand what PyTorch is used for
- Understand the basic idea of CUDA
- Learn how Hugging Face datasets are organized
- Load datasets using the `datasets` library
- Load dataset files directly with pandas
- Practice working with external AI/ML datasets in Python
