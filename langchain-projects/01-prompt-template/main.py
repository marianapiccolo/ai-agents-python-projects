from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

# Load environment variables from the .env file
load_dotenv()

# Create an OpenAI model through LangChain
model = OpenAI()

# -------------------------------------------------------------------
# Option 1: Single prompt template
# -------------------------------------------------------------------
# This example creates one complete prompt template with dynamic variables.
# The variables "length" and "language" are already defined as partial variables.
#
# prompt_template = PromptTemplate.from_template(
#     """
#     Answer the user in a maximum of {length} characters.
#     Answer in {language}, regardless of the language used by the user.
#
#     User question: {message}
#     """,
#     partial_variables={
#         "length": 140,
#         "language": "Spanish"
#     }
# )


# -------------------------------------------------------------------
# Option 2: Composed prompt template
# -------------------------------------------------------------------
# This approach creates smaller prompt templates and combines them
# into one final prompt template.

tone_template = PromptTemplate.from_template(
    "Answer the user in a polite but informal way, as if you were a friend talking to them. "
)

length_template = PromptTemplate.from_template(
    "Your answer must always have a maximum of {length} characters. ",
    partial_variables={
        "length": 140
    }
)

language_template = PromptTemplate.from_template(
    "Answer in {language}, regardless of the language used by the user. ",
    partial_variables={
        "language": "Spanish"
    }
)

message_template = PromptTemplate.from_template(
    "User message: {message}"
)

# Combine all prompt templates into one final template
final_template = (
    tone_template
    + length_template
    + language_template
    + message_template
)

# Fill only the remaining variable: "message"
prompt = final_template.invoke(
    {
        "message": "Is Python worth learning for someone who knows nothing about programming?"
    }
)

# Display the final formatted prompt
print(prompt)

# Send the prompt to the model
response = model.invoke(prompt)

# Display the model response
print(response)