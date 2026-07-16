from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from the .env file
load_dotenv()


def generate_text(prompt: str) -> str:
    """Generate text using a remote Hugging Face model."""

    client = InferenceClient(
        model="meta-llama/Llama-3.2-3B-Instruct"
    )

    response = client.text_generation(prompt)

    return response