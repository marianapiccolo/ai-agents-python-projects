from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

# Load environment variables from the .env file
load_dotenv()

# Create an OpenAI model through LangChain
model = OpenAI()

# Create a reusable prompt template with dynamic variables
prompt_template = PromptTemplate.from_template(
    """
    Answer the user in a maximum of {length} characters.
    Answer in {language}, regardless of the language used by the user.

    User question: {message}
    """
)

# Fill the template with specific values
prompt = prompt_template.invoke(
    {
        "length": 140,
        "language": "Spanish",
        "message": "Is Python worth learning for someone who knows nothing about programming?"
    }
)

# Send the formatted prompt to the model
response = model.invoke(prompt)

# Display the model response
print(response)