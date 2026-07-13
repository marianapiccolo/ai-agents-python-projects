# Image Generation with OpenAI API

This project explores how to generate images and create image variations using the OpenAI API with Python.

The main goal is to understand how image generation works from text prompts and how to generate variations from an existing image.

## Official Documentation

- Image generation: https://developers.openai.com/api/docs/guides/image-generation

## Features

- Generate an image from a text prompt
- Download the generated image from the returned URL
- Save generated images locally
- Create image variations from an existing image
- Organize generated files in a dedicated output folder

## Technologies

- Python
- OpenAI API
- DALL·E
- Requests
- Python-dotenv

## Project Structure

```text
02-image-generation/
├── image_generator.py
├── image_variations.py
├── README.md
└── generated/
    ├── generated_image.jpg
    ├── image_variation_1.jpg
    ├── image_variation_2.jpg
    └── image_variation_3.jpg
```

The `generated/` folder stores generated images and is ignored by Git.

## How It Works

### Image generation from prompt

The first script sends a text prompt to the OpenAI image generation API.

```text
Text prompt
    ↓
OpenAI image generation API
    ↓
Generated image URL
    ↓
Image download with requests
    ↓
Local image file
```

### Image variations

The second script uses an existing image as input and asks the API to generate new image variations.

```text
Original image
    ↓
OpenAI image variation API
    ↓
Generated variation URLs
    ↓
Image download with requests
    ↓
Local variation files
```

## Setup

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install openai python-dotenv requests
```

Update the requirements file:

```bash
python -m pip freeze > openai-projects/requirements.txt
```

Create a `.env` file in the repository root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Examples

From the project folder:

```bash
cd openai-projects/02-image-generation
```

To generate an image from a prompt:

```bash
python image_generator.py
```

To generate image variations:

```bash
python image_variations.py
```

## Important Cost Note

Image generation uses the OpenAI API and may generate costs.

Each generated image or image variation can count as API usage. For this reason, it is important to:

- test with a small number of images;
- avoid running scripts repeatedly without checking the output;
- keep generated files ignored by Git;
- check the official OpenAI pricing page before using the API extensively.

## Git Ignore Notes

Generated images are not included in this repository.

The following files and folders should be ignored:

```text
generated/
*.png
*.jpg
*.jpeg
*.webp
```

## Learning Goals

The main goals of this project are:

- Practice image generation with the OpenAI API
- Understand how prompts influence generated images
- Learn how to download files from generated URLs
- Generate image variations from an existing image
- Organize generated outputs safely
- Apply good practices with environment variables, file structure, and documentation
