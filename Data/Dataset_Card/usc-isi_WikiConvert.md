---
language_creators:
- found
language:
- en
license:
- mit
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- extended|wikipedia
task_categories:
- fill-mask
- other
- text-generation
task_ids:
- language-modeling
- masked-language-modeling
pretty_name: Wiki-Convert
YAML tags:
- {}
- found
language_bcp47:
- en-US
tags:
- numeracy
- natural-language-understanding
- tokenization
---

# Dataset Card Creation Guide

## Table of Contents
- [Dataset Card Creation Guide](#dataset-card-creation-guide)
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
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
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

- **Repository:** [Github](https://github.com/avi-jit/numeracy-literacy)
- **Paper:** [Anthology](https://aclanthology.org/2021.emnlp-main.557)
- **Point of Contact:** [Avijit Thawani](mailto:thawani@isi.edu)

### Dataset Summary

Wiki-Convert is a 900,000+ sentences dataset of precise number annotations from English Wikipedia. It relies on Wiki contributors' annotations in the form of a [{{Convert}}](https://en.wikipedia.org/wiki/Template:Convert) template.

### Supported Tasks and Leaderboards

- `sequence-modeling`: The dataset can be used to train a model for [Language Mddeling], which consists in [TASK DESCRIPTION]. Success on this task is typically measured by achieving a low [perplexity](https://huggingface.co/transformers/perplexity.html).

### Languages

The dataset is extracted from English Wikipedia, hence overwhelmingly contains English text.

## Dataset Structure

### Data Instances

Each row in the json file contains metadata about the source Wikipedia sentence, along with annotations for a single number, e.g., `number: 10` in the below example. The annotations are inspired by Numeracy-600K and are in the form of `length` and `offset` from the beginning of the sentence.

```
{
  'id': 1080801, 'UNIQUE_STORY_INDEX': '1080801', 'offset': 83, 'length': 2, 'magnitude': 0, 'comment': "Like all Type UB III submarines, UB-117 carried 10 torpedoes and was armed with a  10 cms deck gun. ''", 'number': 10
}
```

Please refer to https://github.com/avi-jit/numeracy-literacy for more details.

### Data Splits

|                            | Tain   | Dev | Test |
| -----                      | :------: | :-----: | :----: |
| Input Sentences            |  739,583 | 92,447 | 92,449|

## License

Provided under MIT License.

## Citation

```
@inproceedings{thawani-etal-2021-numeracy,
    title = "Numeracy enhances the Literacy of Language Models",
    author = "Thawani, Avijit  and
      Pujara, Jay  and
      Ilievski, Filip",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-main.557",
    pages = "6960--6967",
    abstract = "Specialized number representations in NLP have shown improvements on numerical reasoning tasks like arithmetic word problems and masked number prediction. But humans also use numeracy to make better sense of world concepts, e.g., you can seat 5 people in your {`}room{'} but not 500. Does a better grasp of numbers improve a model{'}s understanding of other concepts and words? This paper studies the effect of using six different number encoders on the task of masked word prediction (MWP), as a proxy for evaluating literacy. To support this investigation, we develop Wiki-Convert, a 900,000 sentence dataset annotated with numbers and units, to avoid conflating nominal and ordinal number occurrences. We find a significant improvement in MWP for sentences containing numbers, that exponent embeddings are the best number encoders, yielding over 2 points jump in prediction accuracy over a BERT baseline, and that these enhanced literacy skills also generalize to contexts without annotated numbers. We release all code at https://git.io/JuZXn.",
}
```

Thanks to [@avi-jit](https://github.com/avi-jit) for adding this dataset.