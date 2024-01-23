---
annotations_creators:
- crowdsourced
- expert-generated
language:
- en
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: P3
size_categories:
- 100M<n<1B
task_categories:
- other
---

# Dataset Card for P3

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://bigscience.huggingface.co/promptsource
- **Repository:** https://github.com/bigscience-workshop/promptsource/
- **Paper:** [Multitask Prompted Training Enables Zero-Shot Task Generalization](https://arxiv.org/abs/2110.08207)
- **Point of Contact:** [Victor Sanh](mailto:victor@huggingface.co)

### Dataset Summary

P3 (Public Pool of Prompts) is a collection of prompted English datasets covering a diverse set of NLP tasks. A prompt is the combination of an input template and a target template. The templates are functions mapping a data example into natural language for the input and target sequences. For example, in the case of an NLI dataset, the data example would include fields for *Premise, Hypothesis, Label*. An input template would be *If {Premise} is true, is it also true that {Hypothesis}?*, whereas a target template can be defined with the label choices *Choices[label]*. Here *Choices* is prompt-specific metadata that consists of the options *yes, maybe, no* corresponding to *label* being entailment (0), neutral (1) or contradiction (2).

Prompts are collected using [Promptsource](https://github.com/bigscience-workshop/promptsource), an interface to interactively write prompts on datasets, and collect prompt-specific metadata such as evaluation metrics. As of October 13th, there are 2'000 prompts collected for 270+ data(sub)sets. The collection of prompts of P3 is publicly available on [Promptsource](https://github.com/bigscience-workshop/promptsource).

To train [T0*](https://huggingface.co/bigscience/T0pp), we used a subset of the prompts available in Promptsource (see details [here](https://huggingface.co/bigscience/T0pp#training-data)). However, some of the prompts use `random.choice`, a method that selects uniformly at random an option in a list of valid possibilities. For reproducibility purposes, we release the collection of prompted examples used to train T0*. **The data available here are the materialized version of the prompted datasets used in [Multitask Prompted Training Enables Zero-Shot Task Generalization](https://arxiv.org/abs/2110.08207) which represent only a subset of the datasets for which there is at least one prompt in Promptsource.**

### Supported Tasks and Leaderboards

The tasks represented in P3 cover a diverse set of NLP tasks including multiple-choice QA, sentiment analysis or natural language inference. We detail the full list of datasets in [Source Data](#source-data).

### Languages

The data in P3 are in English (BCP-47 `en`).

## Dataset Structure

### Data Instances

An example of "train" looks as follows:
```bash
{
  'answer_choices': ['safe', 'trolley'],
  'inputs': [86, 8, 7142, 666, 6, 405, 8, 3, 834, 1518, 21, 1346, 42, 31682, 58, 37, 3, 929, 9, 3042, 63, 2765, 808, 8, 2045, 6448, 326, 13, 8, 31682, 11, 3, 24052, 135, 16, 8, 1346, 552, 8, 3, 834, 47, 6364, 5], 'inputs_pretokenized': 'In the sentence below, does the _ stand for safe or trolley?\nThe treasury workers took the gold bars off of the trolley and stacked them in the safe until the _ was empty.',
  'targets': [31682, 1],
  'targets_pretokenized': '\ntrolley'
}
```

In the case of rank classification (letting the model select its the prediction the option with the highest log-likelihood), an example looks as follows:
```bash
{
  'idx': [5, 0],
  'inputs': [86, 8, 7142, 666, 6, 405, 8, 3, 834, 1518, 21, 19454, 42, 22227, 58, 19454, 744, 31, 17, 2112, 4553, 17742, 7, 12, 1953, 6, 298, 22227, 966, 373, 405, 5, 3, 834, 19, 72, 952, 12, 619, 16, 3, 9, 17742, 3298, 5],
  'inputs_pretokenized': "In the sentence below, does the _ stand for Kyle or Logan?\nKyle doesn't wear leg warmers to bed, while Logan almost always does. _ is more likely to live in a warmer climate.",
  'is_correct': True,
  'targets': [19454, 1],
  'targets_pretokenized': 'Kyle',
  'weight': 1.0
}
```

To check all the prompted examples, you can use the [Promptsource hosted tool](http://bigscience.huggingface.co/promptsource) and choose the `Prompted dataset viewer` mode in the left panel.


### Data Fields

The data fields are the same among all splits:
- `answer_choices`: the choices (in natural language) available to the model
- `inputs_pretokenized`: the natural language input fed to the model
- `targets_pretokenized`: the natural language target that the model has to generate
- `inputs`: the tokenized input with [T5](https://huggingface.co/google/t5-v1_1-base)'s tokenizer
- `targets`: the tokenized target with [T5](https://huggingface.co/google/t5-v1_1-base)'s tokenizer
- `idx`: identifier of the (example, answer_option_id) in the case of rank classification
- `weight`: a weight for the example produced by seqio (always set to 1.0 in practise)
- `is_correct`: whether the (example, answer_option_id) is the correct one

### Data Splits

The list of data splits and their respective sizes is very long. You'll find the whole list in this [file](https://huggingface.co/datasets/bigscience/P3/blob/main/tasks_splits_and_features.py).

## Dataset Creation

### Curation Rationale

The Public Pool of Prompts relies on the Hugging Face Dataset library. Any public dataset in the Datasets library can be prompted. We select the datasets that have at least one subset in English and excluded datasets containing (predominantly) non-natural language examples.

We conservatively decided not to prompt datasets that contain potentially harmful content (for instance, datasets built on social media content). However, we sometimes prompt datasets that are purposefully built to measure bias and fairness of trained models, and reserve these prompted datasets (the validation or test sets) for evaluation purposes.

### Source Data

Here's the full list of the datasets present in the materialized version of P3:
- Multiple-Choice QA
  - CommonsenseQA
  - DREAM
  - QUAIL
  - QuaRTz
  - Social IQA
  - WiQA
  - Cosmos
  - QASC
  - Quarel
  - SciQ
  - Wiki Hop
  - ARC
  - OpenBookQA
  - MultiRC
  - PIQA
  - RACE
  - HellaSwag
  - BoolQ
- Extractive QA
  - Adversarial QA
  - Quoref
  - DuoRC
  - ROPES
  - SQuAD v2
  - ReCoRD
- Close-book QA
  - Hotpot QA
  - Wiki QA
  - Trivia QA
  - Web Questions
- Structure-to-text
  - Common Gen
  - Wiki Bio
- Sentiment
  - Amazon
  - App Reviews
  - IMDB
  - Rotten Tomatoes
  - Yelp
- Summarization
  - CNN Daily Mail
  - Gigaword
  - MultiNews
  - SamSum
  - XSum
- Topic Classification
  - AG News
  - DBPedia
  - TREC
- Paraphrase Identification
  - MRPC
  - PAWS
  - QQP
- Natural Language Inference
  - ANLI
  - CB
  - RTE
- Coreference Resolution
  - WSC
  - Winogrande
- Word Sense disambiguation
  - WiC
- Sentence Completion
  - COPA
  - HellaSwag
  - Story Cloze

### Annotations

The prompts available in Promptsource are collected as part of BigScience, one-year long research workshop on large multilingual models and datasets. 36 contributors affiliated with 24 institutions in 8 countries participated to the prompt collection. Contributors are in majority machine learning researchers or machine learning engineers.

The main annotation guideline was that prompts needed to be grammatical and understandable by a native English speaker with no prior experience of the tasks. Additionally, prompts that required explicit counting or numerical indexing were removed in favor of natural language variants, e.g., instead of predicting indices of a span to extract (e.g. in extractive question answering), the model was expected to copy the span's text instead. With these minimal constraints, prompt writers were encouraged to use both formal and creative prompts and various orderings of the data. Most of the prompts correspond directly to a version of the original proposed task, although we also allowed prompts that permuted the original task (for instance, generating a document from its summary) or allowed for ambiguous output (for instance, not indicating a list of available choices).

The full annotation given to the contributors can be found [here](https://github.com/bigscience-workshop/promptsource/blob/main/CONTRIBUTING.md). *Note to self: the link is currently being updated with the)

## Additional Information

### Licensing Information

The dataset is released under Apache 2.0.

### Citation Information

```bibtex
@misc{sanh2021multitask,
      title={Multitask Prompted Training Enables Zero-Shot Task Generalization},
      author={Victor Sanh and Albert Webson and Colin Raffel and Stephen H. Bach and Lintang Sutawika and Zaid Alyafeai and Antoine Chaffin and Arnaud Stiegler and Teven Le Scao and Arun Raja and Manan Dey and M Saiful Bari and Canwen Xu and Urmish Thakker and Shanya Sharma Sharma and Eliza Szczechla and Taewoon Kim and Gunjan Chhablani and Nihal Nayak and Debajyoti Datta and Jonathan Chang and Mike Tian-Jian Jiang and Han Wang and Matteo Manica and Sheng Shen and Zheng Xin Yong and Harshit Pandey and Rachel Bawden and Thomas Wang and Trishala Neeraj and Jos Rozen and Abheesht Sharma and Andrea Santilli and Thibault Fevry and Jason Alan Fries and Ryan Teehan and Stella Biderman and Leo Gao and Tali Bers and Thomas Wolf and Alexander M. Rush},
      year={2021},
      eprint={2110.08207},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```

### Contributions

Thanks to the contributors of [promptsource](https://github.com/bigscience-workshop/promptsource/graphs/contributors) for adding this dataset.
