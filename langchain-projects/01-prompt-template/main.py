from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_openai import OpenAI

# Load environment variables from the .env file
load_dotenv()

# Create an OpenAI model through LangChain
model = OpenAI()

# Create an output parser that expects a comma-separated list
parser = CommaSeparatedListOutputParser()

# Template that tells the model which response format it should follow
format_template = PromptTemplate.from_template(
    "Response format: {format_instructions}. ",
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

# Template that defines the response language
language_template = PromptTemplate.from_template(
    "The texts in your response must be in {language}. ",
    partial_variables={
        "language": "Spanish"
    }
)

# Template that contains the user request
message_template = PromptTemplate.from_template(
    "User message: {message}"
)

# Combine all templates into one final prompt
final_template = (
    format_template
    + language_template
    + message_template
)

# Fill the prompt with the user message
prompt = final_template.invoke(
    {
        "message": "Generate a list with the names of 10 customers."
    }
)

# Send the prompt to the model
response = model.invoke(prompt)

# Parse the model response into a Python list
parsed_response = parser.invoke(response)

# Display the parsed result
print(parsed_response)