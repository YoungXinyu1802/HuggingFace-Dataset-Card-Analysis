---
license: apache-2.0
tags:
- human-feedback
pretty_name: Helpful Instructions
---

# Dataset Card for Helpful Instructions

## Dataset Description

- **Homepage:** 
- **Repository:** 
- **Paper:** 
- **Leaderboard:** 
- **Point of Contact: Lewis Tunstall** 

### Dataset Summary

Helpful Instructions is a dataset of `(instruction, demonstration)` pairs that are derived from public datasets. As the name suggests, it focuses on instructions that are "helpful", i.e. the kind of questions or tasks a human user might instruct an AI assistant to perform. You can load the dataset as follows:

```python
from datasets import load_dataset

# Load all subsets
helpful_instructions = load_dataset("HuggingFaceH4/helpful_instructions")

# Load a single subset
helpful_instructions_subset = load_dataset("HuggingFaceH4/helpful_instructions", data_dir="data/helpful-anthropic-raw")
```


### Supported Tasks and Leaderboards

This dataset can be used to fine-tune pretrained language models to follow instructions.

### Languages

English

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

[More Information Needed]