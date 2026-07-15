from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# Load environment variables from the .env file
load_dotenv()

# Create a LangChain chat model connected to OpenAI
model = ChatOpenAI()

# Create a chat prompt template with a system instruction
chat_template = ChatPromptTemplate(
    [
        SystemMessage(
            content=(
                "Always answer the user in {language}, "
                "regardless of the language used in the question."
            )
        )
    ],
    partial_variables={
        "language": "Spanish"
    }
)

# Ask the user to type a message in the terminal
user_text = input("Type your message: ")

# Create a human message with the user input
user_message = HumanMessage(content=user_text)

# Add the user message to the chat template
chat_template.append(user_message)

# Generate the final prompt using the template
prompt = chat_template.invoke({})

# Send the prompt to the model
response = model.invoke(prompt)

# Create a parser that extracts only the text content from the model response
parser = StrOutputParser()

# Parse the model response into a plain string
parsed_response = parser.invoke(response)

# Display the final text response
print(parsed_response)