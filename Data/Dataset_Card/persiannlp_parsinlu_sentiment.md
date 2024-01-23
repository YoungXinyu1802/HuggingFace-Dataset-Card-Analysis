---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- fa
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- extended|translated|mnli
task_categories:
- sentiment-analysis
task_ids:
- sentiment-analysis
---

# Dataset Card for PersiNLU (Textual Entailment)

## Table of Contents
- [Dataset Card for PersiNLU (Sentiment Analysis)](#dataset-card-for-persi_sentiment)
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

- **Homepage:** [Github](https://github.com/persiannlp/parsinlu/)
- **Repository:** [Github](https://github.com/persiannlp/parsinlu/)
- **Paper:** [Arxiv](https://arxiv.org/abs/2012.06154)
- **Leaderboard:** 
- **Point of Contact:** d.khashabi@gmail.com

### Dataset Summary

A Persian sentiment analysis dataset.  

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

The text dataset is in Persian (`fa`).

## Dataset Structure

### Data Instances

Here is an example from the dataset: 
```json 
{
  "review": "خوب بود ولی خیلی گرون شده دیگه...فک نکنم به این قیمت ارزش خرید داشته باشد",
  "review_id": "1538",
  "example_id": "4",
  "excel_id": "food_194",
  "question": "نظر شما در مورد بسته بندی و نگهداری این حلوا شکری، ارده و کنجد چیست؟",
  "category": "حلوا شکری، ارده و کنجد",
  "aspect": "بسته بندی",
  "label": "-3",
  "guid": "food-dev-r1538-e4"
}
```

### Data Fields
- `review`: the review text.
- `review_id`: a unique id associated with the review.
- `example_id`: a unique id associated with a particular attribute being addressed about the review.
- `question`: a natural language question about a particular attribute.
- `category`: the subject discussed in the review.
- `aspect`: the aspect mentioned in the input question. 
- `label`: the overall sentiment towards this particular subject, in the context of the mentioned aspect. Here are the definition of the labels: 
```
    '-3': 'no sentiment expressed',
    '-2': 'very negative',
    '-1': 'negative',
    '0': 'neutral',
    '1': 'positive',
    '2': 'very positive',
    '3': 'mixed',
```
     

### Data Splits

See the data. 

## Dataset Creation

### Curation Rationale

For details, check [the corresponding draft](https://arxiv.org/abs/2012.06154).

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

CC BY-NC-SA 4.0 License 

### Citation Information
```bibtex 
@article{huggingface:dataset,
    title = {ParsiNLU: A Suite of Language Understanding Challenges for Persian},
    authors = {Khashabi, Daniel and Cohan, Arman and Shakeri, Siamak and Hosseini, Pedram and Pezeshkpour, Pouya and Alikhani, Malihe and Aminnaseri, Moin and Bitaab, Marzieh and Brahman, Faeze and Ghazarian, Sarik and others},
    year={2020}
    journal = {arXiv e-prints},
    eprint = {2012.06154},    
}
```

### Contributions

Thanks to [@danyaljj](https://github.com/danyaljj) for adding this dataset.
