---
annotations_creators:
- expert-generated
language_creators:
- crowdsourced
language:
- en
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: 'probability_words_nli'
paperwithcoode_id: probability-words-nli
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
- multiple-choice
- question-answering
task_ids:
- open-domain-qa
- multiple-choice-qa
- natural-language-inference
- multi-input-text-classification
tags:
- wep
- words of estimative probability
- probability
- logical reasoning
- soft logic
- nli
- natural-language-inference
- reasoning
- logic
train-eval-index:
  - config: usnli
    task: text-classification
    task_id: multi-class-classification
    splits:
      train_split: train
      eval_split: validation
    col_mapping:
      sentence1: context
      sentence2: hypothesis
      label: label
    metrics:
      - type: accuracy
        name: Accuracy
      - type: f1
        name: F1 binary
  - config: reasoning-1hop
    task: text-classification
    task_id: multi-class-classification
    splits:
      train_split: train
      eval_split: validation
    col_mapping:
      sentence1: context
      sentence2: hypothesis
      label: label
    metrics:
      - type: accuracy
        name: Accuracy
      - type: f1
        name: F1 binary
  - config: reasoning-2hop
    task: text-classification
    task_id: multi-class-classification
    splits:
      train_split: train
      eval_split: validation
    col_mapping:
      sentence1: context
      sentence2: hypothesis
      label: label
    metrics:
      - type: accuracy
        name: Accuracy
      - type: f1
        name: F1 binary
---

# Dataset accompanying the "Probing neural language models for understanding of words of estimative probability" article

This dataset tests the capabilities of language models to correctly capture the meaning of words denoting probabilities (WEP), e.g. words like "probably", "maybe", "surely", "impossible".

We used probabilitic soft logic to combine probabilistic statements expressed with WEP (WEP-Reasoning) and we also used the UNLI dataset (https://nlp.jhu.edu/unli/) to directly check whether models can detect the WEP matching human-annotated probabilities.
The dataset can be used as natural langauge inference data (context, premise, label) or multiple choice question answering (context,valid_hypothesis, invalid_hypothesis).

```bib
@article{sileo2022probing,
  title={Probing neural language models for understanding of words of estimative probability},
  author={Sileo, Damien and Moens, Marie-Francine},
  journal={arXiv preprint arXiv:2211.03358},
  year={2022}
}
```