from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from the .env file
load_dotenv()


def complete_chat(messages: list[dict[str, str]]) -> list[dict[str, str]]:
    """Send the conversation history to the model and append the AI response."""

    client = InferenceClient(
        model="meta-llama/Llama-3.2-3B-Instruct"
    )

    response = client.chat_completion(messages)

    ai_response = response.choices[0]

    response_role = ai_response.message.role
    response_content = ai_response.message.content

    ai_message = {
        "role": response_role,
        "content": response_content
    }

    messages.append(ai_message)

    return messages