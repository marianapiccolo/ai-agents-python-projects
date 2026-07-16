from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from the .env file
# The Hugging Face token should be stored there
load_dotenv()

# Create a Hugging Face Inference Client
client = InferenceClient()

# Example long text to summarize
text = """
Greek is an Indo-European language, constituting an independent Hellenic branch
within the Indo-European language family. It is native to Greece, Cyprus, Italy,
southern Albania, and other regions of the Balkans, Caucasus, the Black Sea coast,
Asia Minor, and the Eastern Mediterranean. It has the longest documented history
of any Indo-European language, spanning at least 3,400 years of written records.
Its writing system is the Greek alphabet, which has been used for approximately
2,800 years.

The Greek language holds a very important place in the history of the Western
world. Beginning with the epics of Homer, ancient Greek literature includes many
works of lasting importance in the European canon. Greek is also the language in
which many foundational texts in science and philosophy were originally composed.
The New Testament of the Christian Bible was also originally written in Greek.

During antiquity, Greek was by far the most widely spoken lingua franca in the
Mediterranean world. It eventually became the official language of the Byzantine
Empire and developed into Medieval Greek. In its modern form, Greek is the official
language of Greece and Cyprus and one of the 24 official languages of the European
Union.

Greek roots have been widely used for centuries and continue to be used to coin
new words in other languages. Greek and Latin are the predominant sources of
international scientific vocabulary.
"""

# Send the text to a remote summarization model through the Inference API
response = client.summarization(
    text,
    model="facebook/bart-large-cnn"
)

# Display the generated summary
print(response)