from transformers import pipeline

# Create a text generation pipeline using a Hugging Face model
# If CUDA is available, device="cuda" can be used.
# On macOS, CUDA is usually not available because it is specific to NVIDIA GPUs.
text_generator = pipeline(
    task="text-generation",
    model="ahxt/LiteLlama-460M-1T"
    # device="cuda"
)

# Prompt used as input for the model
prompt = "What is the Python programming language?"

# Generate text from the prompt
response = text_generator(
    prompt,
    max_new_tokens=80,
    do_sample=True,
    temperature=0.7
)

# Display the generated text
print(response)