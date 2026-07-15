# Review Analysis Chain

This project analyzes product reviews using LangChain, OpenAI, Pydantic, output parsers, LangSmith, and custom runnables.

The main goal is to understand how to build a LangChain pipeline that extracts structured information from product reviews, saves intermediate results, and generates a final summary analysis.

## Features

- Analyze multiple product reviews
- Extract structured information from review text
- Identify whether each review is positive or negative
- Identify whether the product is worth buying
- Extract positive and negative points
- Use Pydantic to define the expected response schema
- Use JsonOutputParser to parse model responses
- Use StrOutputParser to generate a final text summary
- Create chains with `prompt | model | parser`
- Combine multiple chains into a larger workflow
- Add a custom Python function inside the chain with RunnableLambda
- Save structured results to a local file
- Trace the pipeline with LangSmith

## Technologies

- Python
- LangChain
- LangChain OpenAI
- OpenAI API
- Pydantic
- JsonOutputParser
- StrOutputParser
- RunnableLambda
- LangSmith
- Python-dotenv

## Project Structure

```text
02-review-analysis-chain/
├── main.py
├── README.md
└── generated/
    └── reviews.txt
```

The `generated/` folder is created automatically when the script runs and is ignored by Git.

## How It Works

The project follows this workflow:

```text
Product reviews
      ↓
PromptTemplate
      ↓
ChatOpenAI
      ↓
JsonOutputParser
      ↓
Structured review evaluations
      ↓
RunnableLambda
      ↓
Save results to file
      ↓
Summary chain
      ↓
Final text analysis
```

## Review Evaluation Schema

The project uses Pydantic classes to define the expected output structure.

Each review evaluation contains:

- `positive_review`: whether the review is positive
- `worth_buying`: whether the review says the product is worth buying
- `positive_points`: main positive points from the review
- `negative_points`: main negative points from the review

The final structured output contains a list of review evaluations.

## Creating a Chain

The first chain extracts structured information from the product reviews:

```python
review_analysis_chain = review_template | model | review_parser
```

This connects three steps:

```text
PromptTemplate → ChatOpenAI → JsonOutputParser
```

The prompt template receives the input reviews and creates the final prompt.

The model receives the prompt and generates a response.

The parser converts the model response into structured data.

## Combining Chains

The project also combines multiple chains into a larger workflow.

The first chain extracts structured information from the reviews:

```python
review_analysis_chain = review_template | model | review_parser
```

The second chain receives the structured evaluations and generates a final text analysis:

```python
summary_chain = summary_template | model | text_parser
```

Then both chains are combined:

```python
global_chain = review_analysis_chain | summary_chain
```

This creates a complete pipeline:

```text
Product reviews
      ↓
Structured review evaluation
      ↓
Final summary analysis
```

This approach is useful for building more complex AI workflows where each step has a clear responsibility.

## Custom Runnable with RunnableLambda

This project also uses `RunnableLambda` to add a custom Python function inside the LangChain pipeline.

The custom function saves the structured review evaluations to a local file:

```python
save_reviews_runnable = RunnableLambda(save_reviews_to_file)
```

Then it is added to the global chain:

```python
global_chain = review_analysis_chain | save_reviews_runnable | summary_chain
```

The full workflow becomes:

```text
Product reviews
      ↓
Structured review evaluation
      ↓
Save results to file
      ↓
Final summary analysis
```

The custom function returns the same data it receives so the next chain can continue processing.

## LangSmith Tracing

This project uses LangSmith to trace and monitor the LangChain pipeline.

LangSmith helps inspect:

- chain inputs;
- generated prompts;
- model responses;
- intermediate chain steps;
- execution time;
- errors and debugging information.

To enable LangSmith tracing, the following environment variables are used in the `.env` file:

```env
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGSMITH_PROJECT=your_project_name_here
```

The `.env` file is ignored by Git and should never be committed.

## Output

The script saves the structured review evaluations in:

```text
generated/reviews.txt
```

Example output:

```text
{'positive_review': True, 'worth_buying': True, 'positive_points': ['good quality'], 'negative_points': []}
{'positive_review': False, 'worth_buying': False, 'positive_points': ['presentation'], 'negative_points': ['size']}
```

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

LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGSMITH_PROJECT=your_project_name_here
```

## Running the Project

From the project folder:

```bash
cd langchain-projects/02-review-analysis-chain
python main.py
```

The output file will be created inside the `generated/` folder.

## Important Cost Note

This project uses the OpenAI API and may generate costs.

Each model call can count as API usage. For this reason, it is important to:

- test with small inputs;
- avoid running the script repeatedly without checking the output;
- group similar inputs when appropriate;
- check OpenAI pricing before using the API extensively.

## Learning Goals

The main goals of this project are:

- Understand how to create a LangChain chain
- Learn how to connect prompt templates, models, and parsers
- Use JsonOutputParser with a Pydantic schema
- Process multiple reviews in a single model call
- Combine multiple chains into a larger workflow
- Add custom Python functions to a chain with RunnableLambda
- Save intermediate results to a local file
- Use LangSmith to trace and debug LangChain executions
- Apply a pipeline-style workflow with LangChain
