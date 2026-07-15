# Prompt Templates and Output Parsers

This project explores how to use LangChain prompt templates and output parsers to create reusable prompts and structured model responses.

The main goal is to understand how prompts can be customized, composed, reused, and connected to parsers that standardize the output of language models.

## Features

- Create reusable prompt templates
- Use dynamic variables inside prompts
- Use partial variables to predefine prompt values
- Compose smaller prompt templates into a final prompt
- Use chat prompt templates with system and human messages
- Parse model responses into plain strings
- Parse model responses into comma-separated lists
- Parse model responses into structured JSON
- Use Pydantic models to define response schemas
- Optimize model calls by processing multiple reviews in one request

## Technologies

- Python
- LangChain
- LangChain OpenAI
- OpenAI API
- PromptTemplate
- ChatPromptTemplate
- StrOutputParser
- CommaSeparatedListOutputParser
- JsonOutputParser
- Pydantic
- Python-dotenv

## Project Structure

```text
01-prompt-template/
├── composed_prompt.py
├── output_parser_model.py
├── string_output_parser.py
├── pydantic_output_parser.py
├── optimized_review_parser.py
└── README.md
```

## Files

### `composed_prompt.py`

This file shows how to create reusable prompt templates and combine them into a final prompt.

It includes examples of:

- tone instructions;
- response length instructions;
- response language instructions;
- user message input;
- `partial_variables`.

Example concept:

```python
final_template = (
    tone_template
    + length_template
    + language_template
    + message_template
)
```

This makes the prompt easier to maintain because each part has a clear responsibility.

### `output_parser_model.py`

This file shows how to use `CommaSeparatedListOutputParser`.

The goal is to ask the model for a list and parse the response into a Python list.

Example concept:

```python
parser = CommaSeparatedListOutputParser()
parsed_response = parser.invoke(response)
```

This is useful when the application needs a simple structured list instead of free text.

### `string_output_parser.py`

This file shows how to use `StrOutputParser`.

The goal is to extract only the text content from the model response.

Example concept:

```python
parser = StrOutputParser()
parsed_response = parser.invoke(response)
```

This is useful when the model returns an object such as an `AIMessage`, but the application only needs the final text.

### `pydantic_output_parser.py`

This file shows how to use `JsonOutputParser` with a Pydantic model.

The goal is to define the expected response format using a schema.

Example concept:

```python
class ReviewEvaluation(BaseModel):
    positive_review: bool
    worth_buying: bool
    positive_points: list[str]
    negative_points: list[str]
```

This helps the model return structured data that can be used in application logic.

### `optimized_review_parser.py`

This file improves the previous review analysis example by sending multiple reviews in a single model call.

Instead of calling the model once per review, it sends the full list of reviews at once and expects a structured list of evaluations.

This can reduce:

- number of API calls;
- execution time;
- cost;
- repeated prompt processing.

## How It Works

The project starts with simple prompt customization and evolves into structured output parsing.

General workflow:

```text
User input or review data
        ↓
PromptTemplate or ChatPromptTemplate
        ↓
Language model
        ↓
OutputParser
        ↓
Structured or cleaned response
```

## PromptTemplate

`PromptTemplate` is used to create reusable prompts with dynamic variables.

Example:

```python
prompt_template = PromptTemplate.from_template(
    "Answer in {language}. User message: {message}"
)
```

Then the variables can be filled later:

```python
prompt = prompt_template.invoke(
    {
        "language": "Spanish",
        "message": "Is Python worth learning?"
    }
)
```

This is useful because the same prompt structure can be reused with different inputs.

## Partial Variables

Partial variables are values that are already fixed inside the prompt template.

Example:

```python
length_template = PromptTemplate.from_template(
    "Your answer must always have a maximum of {length} characters.",
    partial_variables={
        "length": 140
    }
)
```

Later, it is not necessary to provide `length` again.

This is useful for rules that should remain constant, such as:

- response language;
- maximum answer length;
- tone;
- output format;
- business rules.

## ChatPromptTemplate

`ChatPromptTemplate` is used to create prompts in chat format.

It works with messages such as:

- `SystemMessage`
- `HumanMessage`
- `AIMessage`

Example:

```python
chat_template = ChatPromptTemplate(
    [
        SystemMessage(
            content="Always answer in {language}."
        )
    ],
    partial_variables={
        "language": "Spanish"
    }
)
```

This is useful when working with chat models because it follows the same structure used in conversations.

## Output Parsers

Output parsers help standardize model responses.

Without a parser, the model may return different formats for similar requests.

With a parser, the application can guide and process the response more reliably.

## Parser Types Used

### StrOutputParser

Returns only the text content of the model response.

```text
AIMessage(content="Sí, Python vale la pena.")
        ↓
"Sí, Python vale la pena."
```

### CommaSeparatedListOutputParser

Parses a comma-separated response into a Python list.

```text
Juan, María, Carlos
        ↓
["Juan", "María", "Carlos"]
```

### JsonOutputParser with Pydantic

Parses the model response into structured JSON based on a schema.

Example output:

```python
{
    "positive_review": True,
    "worth_buying": True,
    "positive_points": ["good quality", "easy to use"],
    "negative_points": []
}
```

## Pydantic

Pydantic is used to define the expected data structure.

In this project, it defines what information should be extracted from product reviews.

Example:

```python
class ReviewEvaluation(BaseModel):
    positive_review: bool = Field(
        description="Is this review positive or negative?"
    )

    worth_buying: bool = Field(
        description="Does this review say the product is worth buying?"
    )
```

The field descriptions help the model understand what each output field means.

## Review Analysis Example

The review analysis examples simulate a practical use case: extracting structured information from product reviews.

The model analyzes reviews and returns:

- whether the review is positive;
- whether the product is worth buying;
- main positive points;
- main negative points.

This kind of workflow can be useful for:

- e-commerce review analysis;
- customer feedback classification;
- product insights;
- CRM systems;
- dashboards;
- automated reports.

## Optimization Example

The optimized review parser sends multiple reviews in a single model call.

Instead of:

```text
Review 1 → model call
Review 2 → model call
Review 3 → model call
Review 4 → model call
```

It uses:

```text
All reviews → one model call
```

This can be more efficient, but it is important to consider the model context limit when processing large amounts of text.

## Setup

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r langchain-projects/requirements.txt
```

Create a `.env` file in the repository root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

The `.env` file is ignored by Git and should never be committed.

## Running the Examples

From the project folder:

```bash
cd langchain-projects/01-prompt-template
```

Run the composed prompt example:

```bash
python composed_prompt.py
```

Run the comma-separated list parser example:

```bash
python output_parser_model.py
```

Run the string output parser example:

```bash
python string_output_parser.py
```

Run the Pydantic JSON parser example:

```bash
python pydantic_output_parser.py
```

Run the optimized review parser example:

```bash
python optimized_review_parser.py
```

## Important Cost Note

These examples use the OpenAI API and may generate costs.

Each model call can count as API usage. For this reason, it is important to:

- test with small inputs;
- avoid running scripts repeatedly without checking the output;
- group similar inputs when appropriate;
- check OpenAI pricing before using the API extensively.

## Learning Goals

The main goals of this project are:

- Understand how to create reusable prompts with LangChain
- Learn how to use dynamic variables in prompts
- Use partial variables to predefine prompt rules
- Compose smaller prompts into a final prompt
- Understand the difference between `PromptTemplate` and `ChatPromptTemplate`
- Learn how output parsers standardize model responses
- Convert model responses into strings, lists, or structured JSON
- Use Pydantic schemas to define expected outputs
- Optimize model calls by processing multiple inputs together
- Build more reliable AI workflows for real applications

#
