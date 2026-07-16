from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from the .env file
# The Hugging Face token should be stored there
load_dotenv()

# Create a Hugging Face Inference Client using a chat model
client = InferenceClient(
    model="meta-llama/Llama-3.2-3B-Instruct"
)

# Initial conversation history with a system message
messages = [
    {
        "role": "system",
        "content": "Answer the questions correctly and accurately."
    }
]

# Start an infinite chat loop in the terminal
while True:
    # Read the user message from the terminal
    user_prompt = input("Type your message: ")

    # Create the user message in chat format
    user_message = {
        "role": "user",
        "content": user_prompt
    }

    # Add the user message to the conversation history
    messages.append(user_message)

    # Send the full conversation history to the model
    response = client.chat_completion(messages)

    # Access the first response choice
    ai_response = response.choices[0]

    # Extract the AI response role and content
    response_role = ai_response.message.role
    response_content = ai_response.message.content

    # Create the AI message in chat format
    ai_message = {
        "role": response_role,
        "content": response_content
    }

    # Add the AI response to the conversation history
    messages.append(ai_message)

    # Display the AI response
    print("AI:", response_content)