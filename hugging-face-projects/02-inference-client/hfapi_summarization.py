from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from the .env file
load_dotenv()

# Create a Hugging Face Inference Client
client = InferenceClient()


def summarize_text(text: str) -> str:
    """Summarize a text using a remote Hugging Face model."""

    response = client.summarization(
        text,
        model="facebook/bart-large-cnn"
    )

    return response.summary_text


if __name__ == "__main__":
    example_text = """
    Greek is an Indo-European language, constituting an independent Hellenic branch
    within the Indo-European language family. It has the longest documented history
    of any Indo-European language, spanning at least 3,400 years of written records.
    Greek also holds a very important place in the history of the Western world.
    """

    summary = summarize_text(example_text)
    print(summary)