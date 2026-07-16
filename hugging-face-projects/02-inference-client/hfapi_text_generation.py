from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from the .env file
# The Hugging Face token should be stored there
load_dotenv()

# Create a Hugging Face Inference Client using a text generation model
client = InferenceClient(
    model="meta-llama/Llama-3.2-3B-Instruct"
)

# Prompt sent to the model
prompt = "What is the Python programming language?"

# Generate text from the prompt using the remote model
response = client.text_generation(prompt)

# Display the generated response
print(response)