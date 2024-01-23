---
license: cc-by-sa-4.0
---
annotations_creators:
- no-annotation
language:
- en
language_creators:
- expert-generated
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
paperswithcode_id: acronym-identification
pretty_name: Massive E-commerce Dataset for Retail and Insurance domain.
size_categories:
- n<1K
source_datasets:
- original
tags:
- chatbots
- e-commerce
- retail
- insurance
- consumer
- consumer goods

task_categories:
- question-answering
- text-retrieval
- text2text-generation
- other
- translation
- conversational

task_ids:
- extractive-qa
- closed-domain-qa
- utterance-retrieval
- document-retrieval
- closed-domain-qa
- open-book-qa
- closed-book-qa
train-eval-index:

- col_mapping:
    labels: tags
    tokens: tokens
  config: default
  splits:
    eval_split: test
  task: token-classification
  task_id: entity_extraction