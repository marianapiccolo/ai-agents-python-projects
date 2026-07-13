from pathlib import Path

import requests
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from the .env file
load_dotenv()

# Create an OpenAI client
client = OpenAI()

# Define the folder where generated files are stored
output_folder = Path(__file__).parent / "generated"
output_folder.mkdir(exist_ok=True)

# Define the original image path
original_image_path = output_folder / "generated_image.jpg"

# Open the original image and request image variations
with open(original_image_path, "rb") as image_file:
    response = client.images.create_variation(
        model="dall-e-2",
        n=3,
        image=image_file
    )

# Get the list of generated image variations
images = response.data

# Download and save each generated variation
for index, image in enumerate(images, start=1):
    image_url = image.url

    image_response = requests.get(image_url)

    variation_image_path = output_folder / f"image_variation_{index}.jpg"

    with open(variation_image_path, "wb") as variation_file:
        variation_file.write(image_response.content)

print("Image variations generated successfully.")