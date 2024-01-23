---
language:
- en
source_datasets:
- allenai/c4
task_categories:
- text-generation
pretty_name: C4 200M Grammatical Error Correction Dataset
tags:
- grammatical-error-correction
---
# C4 200M
# Dataset Summary


C4 200M Sample Dataset adopted from https://huggingface.co/datasets/liweili/c4_200m 

C4_200m is a collection of 185 million sentence pairs generated from the cleaned English dataset from C4. This dataset can be used in grammatical error correction (GEC) tasks.

The corruption edits and scripts used to synthesize this dataset is referenced from: [C4_200M Synthetic Dataset](https://github.com/google-research-datasets/C4_200M-synthetic-dataset-for-grammatical-error-correction)

# Description
As discussed before, this dataset contains 185 million sentence pairs. Each article has these two attributes: `input` and `output`. Here is a sample of dataset:
```
{
  "input": "Bitcoin is for $7,094 this morning, which CoinDesk says."
  "output": "Bitcoin goes for $7,094 this morning, according to CoinDesk."
}
```