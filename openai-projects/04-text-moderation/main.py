from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from the .env file
load_dotenv()

# Create an OpenAI client
client = OpenAI()

# Text that will be analyzed by the moderation model
text_input = "This person is very rude and does not know anything about Python."

# Send the text to the moderation model
response = client.moderations.create(
    model="omni-moderation-latest",
    input=text_input
)

# Get the first moderation result
moderation_result = response.results[0]

# Check whether the content was flagged as potentially unsafe
print("Flagged:", moderation_result.flagged)

# Display the detected moderation categories
print("Categories:", moderation_result.categories.to_dict())