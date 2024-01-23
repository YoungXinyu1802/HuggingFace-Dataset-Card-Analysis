---
annotations_creators:
- no-annotation
language:
- en
language_creators:
- machine-generated
license:
- odc-by
multilinguality:
- monolingual
pretty_name: C4-FAQs
size_categories:
- 100K<n<1M
source_datasets:
- extended|c4
tags:
- question-generation
- question_generation
- open-domain-qg
- qg
task_categories:
- text2text-generation
- text-generation
- question-answering
task_ids:
- text-simplification
- language-modeling
- open-domain-qa
---

# Dataset Card for [Dataset Name]

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
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Point of Contact:** [Vishal Burman](mailto:vishal.a.burman23@gmail.com)

### Dataset Summary

This dataset comprises of open-domain question-answer pairs obtained from extracting 150K FAQ URLs from C4 dataset. Please refer to the original [`paper`](https://arxiv.org/abs/1910.10683) and [`dataset card`](https://huggingface.co/datasets/c4) for more details.

You can load C4-FAQs as follows:
```python
from datasets import load_dataset
c4_faqs_dataset = load_dataset("vishal-burman/c4-faqs")
```

### Supported Tasks and Leaderboards

C4-FAQs is mainly intended for open-domain end-to-end question generation. It can also be used for open-domain question answering.

### Languages

C4-FAQs only supports English language.

## Dataset Structure

### Data Instances

An example of a single dataset point:
```python
{'url': 'https://www.brusselsghosts.com/things-to-do-brussels/faq.html', 'faq_pairs': [{'question': 'What should I bring for the tour?', 'answer': 'Nothing special, just be ready to walk for bit and potentially something to protect you from poltergeists and rain. Any kind of amulet or protection stone is also welcome.'}, {'question': 'Can kids join too ?', 'answer': 'Yes, we accept kids from 6 years old and on! We also have a family discount, if you book for 2 adults and 2 kids!'}, {'question': 'Where is the meeting point ?', 'answer': 'Brussels has many paved roads and those are hardly accessible with a wheelchair, for that reason we have to unfortunately label our tour as not wheelchair accessible.'}]}
```

### Data Fields

The data have several fields:

- `url`: URL of the webpage containing the FAQs
- `faq_pairs`: A list of question-answer pairs extracted from the webpage
  - `question`: A single question as a string
  - `answer`: A single answer to the above question as a string 

### Data Splits

| subset | total |
|:-------|:------|
| train  | 150K  |

## Dataset Creation

### Curation Rationale

The dataset was curated to create end-to-end Question Generation pipelines. A large amount of open-source models use [`SQuAD`](https://huggingface.co/datasets/squad) dataset to create answer-agnostic question generation models. While the questions are valid, they often are short factoid in nature. This dataset is curated from FAQs of websites, which are generally hand-crafted and can be used to further improve generated question quality.

## Additional Information

### Dataset Curators

Original data by [Common Crawl](https://commoncrawl.org/).

### Licensing Information

The original dataset was released under the terms of ODC-BY. By using this, you are also bound by the Common Crawl terms of use in respect of the content contained in the dataset.

### Citation Information

If you use this dataset, I would love to hear about it! Reach out on GitHub, twitter or shoot me an email.

To cite the original `c4` dataset:
```bibtex
@article{2019t5,
    author = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},
    title = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
    journal = {arXiv e-prints},
    year = {2019},
    archivePrefix = {arXiv},
    eprint = {1910.10683},
}
```
