---
pretty_name: SQuAD2.0 Dutch
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- nl
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- open-domain-qa
- extractive-qa
paperswithcode_id: squad_v2_dutch
dataset_info:
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: title_en
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: text
      dtype: string
    - name: text_en
      dtype: string
    - name: answer_start_en
      dtype: int32
---

# Dataset Card for "squad_v2_dutch"

## Dataset Description

- **Homepage:** [https://rajpurkar.github.io/SQuAD-explorer/](https://rajpurkar.github.io/SQuAD-explorer/)

## Dataset Summary

The squad_v2_dutch dataset is a machine-translated version of the SQuAD v2 dataset from English to Dutch.
The SQuAD v2 dataset combines the 100,000 questions in SQuAD1.1 with over 50,000 unanswerable questions written adversarially by crowdworkers
to look similar to answerable ones. To do well on SQuAD2.0, systems must not only answer questions when possible, but
also determine when no answer is supported by the paragraph and abstain from answering.

## Challenges and Solutions
One of the main challenges in translating the SQuAD v2 dataset to Dutch was accurately translating the answers, which are often short phrases or single words.
Translating the answers individually would result in obvious mistakes. Examples are

* Destiny's Child -> Het kind van Destiny
* Dangerously in Love -> Gevaarlijk in de liefde
* Imagine -> Stel je voor
* Men in Black -> Mannen in zwart
* Hottest Female Singer of All Time -> De heetste vrouwelijke zanger aller tijden

The correct translation of these phrases often depends on the context in which they are used.
To address this, the title, question, answers, and context were concatenated as a single sequence, separated by the newline character.
When the translated version had the correct number of newlines and did not contain any apparent mixups of the answers with the question and title, it was used.
Otherwise, the one-by-one context-less translation was used as a fallback.

Most examples where translated with the context-rich translation: ~95%.
* train split: context: 123898,  no context: 6406
* validation split: context: 10196, no context: 1644

### Data Fields

The data fields are the same among all splits.

#### squad_v2
- `id`: a `string` feature.
- `title`: a `string` feature.
- `title_en`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `text`: a list of `string` feature.
  - `text_en`: a list of `string` feature.
  - `answer_start_en`: a `int32` feature.

### Citation Information

```
@article{2016arXiv160605250R,
       author = {{Rajpurkar}, Pranav and {Zhang}, Jian and {Lopyrev},
                 Konstantin and {Liang}, Percy},
        title = "{SQuAD: 100,000+ Questions for Machine Comprehension of Text}",
      journal = {arXiv e-prints},
         year = 2016,
          eid = {arXiv:1606.05250},
        pages = {arXiv:1606.05250},
archivePrefix = {arXiv},
       eprint = {1606.05250},
}

```

### Contributions

Thanks to [@lewtun](https://github.com/lewtun), [@albertvillanova](https://github.com/albertvillanova), [@patrickvonplaten](https://github.com/patrickvonplaten),
[@thomwolf](https://github.com/thomwolf) for adding the https://huggingface.co/datasets/squad_v2 dataset.
This project would not have been possible without compute generously provided by Google through the
[TPU Research Cloud](https://sites.research.google/trc/).

Created by [Yeb Havinga](https://www.linkedin.com/in/yeb-havinga-86530825/)



