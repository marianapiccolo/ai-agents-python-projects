from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from the .env file
load_dotenv()


def summarize_text(text: str) -> str:
    """Summarize a text using a remote Hugging Face model."""

    client = InferenceClient()

    response = client.summarization(
        text,
        model="facebook/bart-large-cnn"
    )

    return response.summary_text