# RAFT Submission Template

Welcome to the [RAFT benchmark](https://raft.elicit.org/)! RAFT is a few-shot classification benchmark that tests language models:

- across multiple domains (lit review, tweets, customer interaction, etc.)
- on economically valuable classification tasks (someone inherently cares about the task)
- in a setting that mirrors deployment (50 examples per task, info retrieval allowed, hidden test set)

This repository can be used to generate a template so you can submit your predictions for evaluation on [the leaderboard](https://huggingface.co/spaces/ought/raft-leaderboard).

## Quickstart

### 1. Create an account on the Hugging Face Hub

First create an account on the Hugging Face Hub and you can sign up [here](https://huggingface.co/join) if you haven't already!

### 2. Create a template repository on your machine

The next step is to create a template repository on your local machine that contains various files and a CLI to help you validate and submit your predictions. The Hugging Face Hub uses [Git Large File Storage (LFS)](https://git-lfs.github.com) to manage large files, so first install it if you don't have it already. For example, on macOS you can run:

```bash
brew install git-lfs
git lfs install
```

Next, run the following commands to create the repository. We recommend creating a Python virtual environment for the project, e.g. with Anaconda:

```bash
# Create and activate a virtual environment
conda create -n raft python=3.8 && conda activate raft
# Install the following libraries
pip install cookiecutter huggingface-hub==0.0.16
# Create the template repository
cookiecutter git+https://huggingface.co/datasets/ought/raft-submission
```

This will ask you to specify your Hugging Face Hub username, password, and the name of the repository:

```
hf_hub_username [<huggingface>]:
hf_hub_password [<password>]:
repo_name [<my-raft-submissions>]:
```

This will trigger the following steps:

1. Create a private dataset repository on the Hugging Face Hub under `{hf_hub_username}/{repo_name}`
2. Clone the repository to your local machine
3. Add various template files and commit them locally to the repository

The resulting repository should have the following structure:

```
my-raft-submission
├── LICENSE
├── README.md               <- The README with submission instructions
├── cli.py                  <- The CLI for validating predictions etc
├── data                    <- The predictions for each task
├── my-raft-submission.py   <- Script to load predictions. Do not edit!
└── requirements.txt        <- The requirements file for the submissions
```

### 3. Install the dependencies

The final step is to install the project's dependencies:

```bash
# Navigate to the template repository
cd my-raft-submissions
# Install dependencies
python -m pip install -r requirements.txt
```

That's it! You're now all set to start generating predictions - see the instructions below on how to submit them to the Hub.

## Submitting to the leaderboard

To make a submission to the [leaderboard](https://huggingface.co/spaces/ought/raft-leaderboard), there are three main steps:

1. Generate predictions on the unlabeled test set of each task
2. Validate the predictions are compatible with the evaluation framework
3. Push the predictions to the Hub!

See the instructions below for more details.

### Rules

1. To prevent overfitting to the public leaderboard, we only evaluate **one submission per week**. You can push predictions to the Hub as many times as you wish, but we will only evaluate the most recent commit in a given week. Submissions are evaluated **every Sunday at 12:00 UTC.**
2. Transfer or meta-learning using other datasets, including further pre-training on other corpora, is allowed.
3. Use of unlabeled test data is allowed, as is it always available in the applied setting. For example, further pre-training using the unlabeled data for a task would be permitted.
4. Systems may be augmented with information retrieved from the internet, e.g. via automated web searches.


### Submission file format

For each task in RAFT, you should create a CSV file called `predictions.csv` with your model's predictions on the unlabeled test set. Each file should have exactly 2 columns:

* ID (int)
* Label (string)

See the dummy predictions in the `data` folder for examples with the expected format. Here is a simple example that creates a majority-class baseline:

```python
from pathlib import Path
import pandas as pd
from collections import Counter
from datasets import load_dataset, get_dataset_config_names

tasks = get_dataset_config_names("ought/raft")

for task in tasks:
    # Load dataset
    raft_subset = load_dataset("ought/raft", task)
    # Compute majority class over training set
    counter = Counter(raft_subset["train"]["Label"])
    majority_class = counter.most_common(1)[0][0]
    # Load predictions file
    preds = pd.read_csv(f"data/{task}/predictions.csv")
    # Convert label IDs to label names
    preds["Label"] = raft_subset["train"].features["Label"].int2str(majority_class)
    # Save predictions
    preds.to_csv(f"data/{task}/predictions.csv", index=False)
```

As you can see in the example, each `predictions.csv` file should be stored in the task's subfolder in `data` and at the end you should have something like the following:

```
data
├── ade_corpus_v2
│   ├── predictions.csv             <- A CSV file of the predictions with `ID` and `Label` columns
│   └── task.json                   <- Configuration file for loading the predictions. Do not edit!
├── banking_77
│   ├── predictions.csv
│   └── task.json
├── neurips_impact_statement_risks
│   ├── predictions.csv
│   └── task.json
├── one_stop_english
│   ├── predictions.csv
│   └── task.json
├── overruling
│   ├── predictions.csv
│   └── task.json
├── semiconductor_org_types
│   ├── predictions.csv
│   └── task.json
├── systematic_review_inclusion
│   ├── predictions.csv
│   └── task.json
├── tai_safety_research
│   ├── predictions.csv
│   └── task.json
├── terms_of_service
│   ├── predictions.csv
│   └── task.json
├── tweet_eval_hate
│   ├── predictions.csv
│   └── task.json
└── twitter_complaints
    ├── predictions.csv
    └── task.json
```

### Validate your submission

To ensure that your submission files are correctly formatted, run the following command from the root of the repository:

```
python cli.py validate
```

If everything is correct, you should see the following message:

```
All submission files validated! ✨ 🚀 ✨
Now you can make a submission 🤗
```

### Push your submission to the Hugging Face Hub!

The final step is to commit your files and push them to the Hub:

```
python cli.py submit
```

If there are no errors, you should see the following message:

```
Submission successful! 🎉 🥳 🎉
Your submission will be evaluated on Sunday 05 September 2021 at 12:00 UTC ⏳
```

where the evaluation is run every Sunday and your results will be visible on the leaderboard.