import pandas as pd

# -------------------------------------------------------------------
# Option 1: Loading a Hugging Face dataset with the datasets library
# -------------------------------------------------------------------
# This example was not used because the dataset is large.
#
# from datasets import load_dataset
#
# dataset = load_dataset("facebook/natural_reasoning", split="train")
#
# print(dataset["question"])


# -------------------------------------------------------------------
# Option 2: Loading a Hugging Face dataset file with pandas
# -------------------------------------------------------------------
# This example loads a CSV file directly from a Hugging Face dataset repository.
# Some datasets may require authentication with the Hugging Face CLI.

dataset_path = "hf://datasets/Anthropic/EconomicIndex/onet_task_mappings.csv"

dataframe = pd.read_csv(dataset_path)

print(dataframe)