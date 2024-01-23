---
annotations_creators:
- machine-generated
language:
- en
language_creators:
- found
license:
- mit
multilinguality:
- monolingual
pretty_name: pile-pii-scrubadub
size_categories:
- 1M<n<10M
source_datasets:
- extended|the_pile
tags:
- pii
- personal
- identifiable
- information
- pretraining-with-human-feedback
task_categories:
- text-classification
- other
task_ids:
- acceptability-classification
- text-scoring
---

# Dataset Card for pile-pii-scrubadub

## Dataset Description

- **Repository: https://github.com/tomekkorbak/aligned-pretraining-objectives** 
- **Paper: Arxiv link to be added**

### Dataset Summary

This dataset contains text from [The Pile](https://huggingface.co/datasets/the_pile), annotated based on the personal idenfitiable information (PII) in each sentence.
Each document (row in the dataset) is segmented into sentences, and each sentence is given a score: the percentage of words in it that are classified as PII by [Scrubadub](https://scrubadub.readthedocs.io/en/stable/).

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

This dataset is taken from [The Pile](https://huggingface.co/datasets/the_pile), which is English text.

## Dataset Structure

### Data Instances

1949977

### Data Fields

- texts (sequence): a list of the sentences in the document (segmented using [SpaCy](https://spacy.io/))
- meta (dict): the section of [The Pile](https://huggingface.co/datasets/the_pile) from which it originated
- scores (sequence): a score for each sentence in the `texts` column indicating the percent of words that are detected as PII by [Scrubadub](https://scrubadub.readthedocs.io/en/stable/)
- avg_score (float64): the average of the scores listed in the `scores` column
- num_sents (int64): the number of sentences (and scores) in that document

### Data Splits

Training set only

## Dataset Creation

### Curation Rationale

This is labeled text from [The Pile](https://huggingface.co/datasets/the_pile), a large dataset of text in English. The PII is labeled so that generative language models can be trained to avoid generating PII.

### Source Data

#### Initial Data Collection and Normalization

This is labeled text from [The Pile](https://huggingface.co/datasets/the_pile).

#### Who are the source language producers?

Please see [The Pile](https://huggingface.co/datasets/the_pile) for the source of the dataset.

### Annotations

#### Annotation process

For each sentence, [Scrubadub](https://scrubadub.readthedocs.io/en/stable/) was used to detect:

- email addresses
- addresses and postal codes
- phone numbers
- credit card numbers
- US social security numbers
- vehicle plates numbers
- dates of birth
- URLs
- login credentials

#### Who are the annotators?

[Scrubadub](https://scrubadub.readthedocs.io/en/stable/)

### Personal and Sensitive Information

This dataset contains all PII that was originally contained in [The Pile](https://huggingface.co/datasets/the_pile), with all detected PII annotated.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset contains examples of real PII (conveniently annotated in the text!). Please take care to avoid misusing it or putting anybody in danger by publicizing their information.
This dataset is intended for research purposes only. We cannot guarantee that all PII has been detected, and we cannot guarantee that models trained using it will avoid generating PII.
We do not recommend deploying models trained on this data.

### Discussion of Biases

This dataset contains all biases from The Pile discussed in their paper: https://arxiv.org/abs/2101.00027

### Other Known Limitations

The PII in this dataset was detected using imperfect automated detection methods. We cannot guarantee that the labels are 100% accurate.

## Additional Information

### Dataset Curators

[The Pile](https://huggingface.co/datasets/the_pile)

### Licensing Information

From [The Pile](https://huggingface.co/datasets/the_pile): PubMed Central: [MIT License](https://github.com/EleutherAI/pile-pubmedcentral/blob/master/LICENSE)

### Citation Information

Paper information to be added

### Contributions

[The Pile](https://huggingface.co/datasets/the_pile)