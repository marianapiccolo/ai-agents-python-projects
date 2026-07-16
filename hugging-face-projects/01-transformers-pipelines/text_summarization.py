from transformers import pipeline

# Create a summarization pipeline using a Hugging Face model
# If CUDA is available, device="cuda" can be used.
# On macOS, CUDA is usually not available because it is specific to NVIDIA GPUs.
summarizer = pipeline(
    task="summarization",
    model="google/pegasus-xsum"
    # device="cuda" - GPUs NVIDIA
)

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
Union. It is spoken by millions of people today.

Greek roots have been widely used for centuries and continue to be used to coin
new words in other languages. Greek and Latin are the predominant sources of
international scientific vocabulary.
"""

# Generate a summary from the input text
response = summarizer(
    text,
    max_length=140,
    min_length=30,
    do_sample=False
)

# Display the summary result
print(response)