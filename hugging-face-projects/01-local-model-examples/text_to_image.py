from pathlib import Path

import torch
from diffusers import StableDiffusionPipeline

# Model used for text-to-image generation
model_id = "sd-legacy/stable-diffusion-v1-5"

# Select the best available device
# - CUDA: NVIDIA GPUs
# - MPS: Apple Silicon acceleration on macOS
# - CPU: fallback option
if torch.cuda.is_available():
    device = "cuda"
    torch_dtype = torch.float16
elif torch.backends.mps.is_available():
    device = "mps"
    torch_dtype = torch.float32
else:
    device = "cpu"
    torch_dtype = torch.float32

# Load the Stable Diffusion pipeline
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch_dtype
)

# Move the model to the selected device
pipe = pipe.to(device)

# Prompt used to generate the image
prompt = "A purple cow with a big smile"

# Generate the image
response = pipe(prompt)

# Get the first generated image
image = response.images[0]

# Create a folder to store generated files
output_folder = Path(__file__).parent / "generated"
output_folder.mkdir(exist_ok=True)

# Save the generated image
image_path = output_folder / "generated_image.png"
image.save(image_path)

print("Image generated successfully.")
print(f"Image saved at: {image_path}")