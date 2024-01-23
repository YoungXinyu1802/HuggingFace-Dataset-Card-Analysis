---
license: openrail
task_categories:
- text2text-generation
language:
- en
size_categories:
- 100K<n<1M
---
This is a dataset of paraphrases created by ChatGPT.

**We used this prompt to generate paraphrases:**                         
Generate 5 similar paraphrases for this question, show it like a numbered list without commentaries: *{text}*

This dataset is based on the [Quora paraphrase question](https://www.kaggle.com/competitions/quora-question-pairs), texts from the [SQUAD 2.0](https://huggingface.co/datasets/squad_v2) and the [CNN news dataset](https://huggingface.co/datasets/cnn_dailymail).

We generated 5 paraphrases for each sample, totally this dataset has almost 400k data rows. You can make 30 rows of a row 
from each sample. In this way you can make 12 millions train pairs (400k rows with 5 paraphrases -> 6x5x400000 = 12 millions of bidirected or 6x5x400000/2 = 6 millions of unique pairs).

**We used:**
- 292652 questions from the Quora dataset 
- 92113 texts from the Squad 2.0 dataset
- 15438 texts from the CNN news dataset

**Structure of the dataset:**
- text column - an original sentence or question from the datasets
- paraphrases - a list of 5 paraphrases
- category - question / sentence
- source - quora / squad_2 / cnn_news