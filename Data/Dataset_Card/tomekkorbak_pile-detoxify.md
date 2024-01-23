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
pretty_name: pile-detoxify
size_categories:
- 1M<n<10M
source_datasets:
- extended|the_pile
tags:
- toxicity
- pretraining-with-human-feedback
task_categories:
- text-classification
- other
task_ids:
- acceptability-classification
- hate-speech-detection
- text-scoring
---

# Dataset Card for pile-pii-scrubadub

## Dataset Description

- **Repository: https://github.com/tomekkorbak/aligned-pretraining-objectives** 
- **Paper: Arxiv link to be added**

### Dataset Summary

This dataset contains text from [The Pile](https://huggingface.co/datasets/the_pile), annotated based on the toxicity of each sentence.
Each document (row in the dataset) is segmented into sentences, and each sentence is given a score: the toxicity predicted by the [Detoxify](https://github.com/unitaryai/detoxify).

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

This dataset is taken from [The Pile](https://huggingface.co/datasets/the_pile), which is English text.

## Dataset Structure

### Data Instances

1949977

### Data Fields

- texts (sequence): a list of the sentences in the document, segmented using SpaCy
- meta (dict): the section of [The Pile](https://huggingface.co/datasets/the_pile) from which it originated
- scores (sequence): a score for each sentence in the `texts` column indicating the toxicity predicted by [Detoxify](https://github.com/unitaryai/detoxify)
- avg_score (float64): the average of the scores listed in the `scores` column
- num_sents (int64): the number of sentences (and scores) in that document

### Data Splits

Training set only

## Dataset Creation

### Curation Rationale

This is labeled text from [The Pile](https://huggingface.co/datasets/the_pile), a large dataset of text in English. The text is scored for toxicity so that generative language models can be trained to avoid generating toxic text.

### Source Data

#### Initial Data Collection and Normalization

This is labeled text from [The Pile](https://huggingface.co/datasets/the_pile).

#### Who are the source language producers?

Please see [The Pile](https://huggingface.co/datasets/the_pile) for the source of the dataset.

### Annotations

#### Annotation process

Each sentence was scored using [Detoxify](https://github.com/unitaryai/detoxify), which is a toxic comment classifier.
We used the `unbiased` model which is based on the 124M parameter [RoBERTa](https://arxiv.org/abs/1907.11692) and trained on the [Jigsaw Unintended Bias in Toxicity Classification dataset](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification).

#### Who are the annotators?

[Detoxify](https://github.com/unitaryai/detoxify)

### Personal and Sensitive Information

This dataset contains all personal identifable information and toxic text that was originally contained in [The Pile](https://huggingface.co/datasets/the_pile).

## Considerations for Using the Data

### Social Impact of Dataset

This dataset contains examples of toxic text and personal identifiable information.
(A version of this datatset with personal identifiable information annotated is [available here](https://huggingface.co/datasets/tomekkorbak/pile-pii-scrubadub).)
Please take care to avoid misusing the toxic text or putting anybody in danger by publicizing their information.
This dataset is intended for research purposes only. We cannot guarantee that all toxic text has been detected, and we cannot guarantee that models trained using it will avoid generating toxic text.
We do not recommend deploying models trained on this data.

### Discussion of Biases

This dataset contains all biases from The Pile discussed in their paper: https://arxiv.org/abs/2101.00027

### Other Known Limitations

The toxic text in this dataset was detected using imperfect automated detection methods. We cannot guarantee that the labels are 100% accurate.

## Additional Information

### Dataset Curators

[The Pile](https://huggingface.co/datasets/the_pile)

### Licensing Information

From [The Pile](https://huggingface.co/datasets/the_pile): PubMed Central: [MIT License](https://github.com/EleutherAI/pile-pubmedcentral/blob/master/LICENSE)

### Citation Information

Paper information to be added

### Contributions

[The Pile](https://huggingface.co/datasets/the_pile)