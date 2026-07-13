# Text Moderation with OpenAI API

This project explores how to moderate and classify text using the OpenAI Moderation API with Python.

The main goal is to understand how to detect potentially harmful, offensive, or unsafe content in text inputs.

## Official Documentation

- Moderation: https://developers.openai.com/api/docs/guides/moderation

## Features

- Analyze text content with the OpenAI Moderation API
- Check whether a text input is flagged as potentially unsafe
- Inspect moderation categories
- Use moderation results to support content filtering decisions
- Explore how moderation can be integrated into larger applications

## Technologies

- Python
- OpenAI API
- OpenAI Moderation model
- Python-dotenv

## Project Structure

```text
04-text-moderation/
├── main.py
└── README.md
```

## How It Works

The script sends a text input to the moderation model.

```text
Text input
    ↓
OpenAI Moderation API
    ↓
Moderation result
    ↓
Flagged status and category scores
```

The API response includes a `flagged` value and a list of moderation categories.

The `flagged` value indicates whether the content was considered potentially unsafe.

The categories show what type of content may have been detected, such as harassment, hate, self-harm, sexual content, or violence.

## Example

```python
response = client.moderations.create(
    model="omni-moderation-latest",
    input=text_input
)
```

Then the result can be inspected:

```python
moderation_result = response.results[0]

print(moderation_result.flagged)
print(moderation_result.categories.to_dict())
```

## Possible Use Cases

Moderation can be used in many types of applications, for example:

- comment moderation;
- chat moderation;
- forum content filtering;
- user-generated content review;
- automatic warning systems;
- blocking offensive messages;
- sending risky content to manual review;
- applying different rules depending on the detected category.

For example, an application could apply different actions depending on the category:

```text
If harassment is detected
    → hide the message or warn the user

If hate content is detected
    → block the message

If self-harm content is detected
    → show a safety message or escalate the case

If violence is detected
    → review, block, or flag the content
```

The moderation result does not need to be used only as `True` or `False`.  
It can support more detailed business rules using conditional logic.

## Setup

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install openai python-dotenv
```

Update the requirements file:

```bash
python -m pip freeze > openai-projects/requirements.txt
```

Create a `.env` file in the repository root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Example

From the project folder:

```bash
cd openai-projects/04-text-moderation
python text_moderation.py
```

## Important Note

Moderation models are useful for identifying potentially unsafe content, but they should be used as part of a broader safety strategy.

In real applications, moderation logic can be combined with:

- business rules;
- manual review;
- user warnings;
- logging;
- escalation flows;
- different actions depending on the category.

## Learning Goals

The main goals of this project are:

- Understand how moderation models classify text
- Learn how to detect potentially unsafe content
- Inspect flagged results and moderation categories
- Think about how moderation can support product safety
- Apply conditional logic based on different moderation categories
