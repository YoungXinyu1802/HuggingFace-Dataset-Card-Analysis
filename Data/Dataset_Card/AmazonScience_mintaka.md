---
annotations_creators:
- expert-generated
language_creators:
- found
license:
- cc-by-4.0
multilinguality:
- ar
- de
- ja
- hi
- pt
- en
- es
- it
- fr
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- open-domain-qa
paperswithcode_id: mintaka
pretty_name: Mintaka
language_bcp47:
- ar-SA
- de-DE
- ja-JP
- hi-HI
- pt-PT
- en-EN
- es-ES
- it-IT
- fr-FR
---

# Mintaka: A Complex, Natural, and Multilingual Dataset for End-to-End Question Answering

## Table of Contents
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
- **Homepage:** https://github.com/amazon-science/mintaka
- **Repository:** https://github.com/amazon-science/mintaka
- **Paper:** https://aclanthology.org/2022.coling-1.138/
- **Point of Contact:** [GitHub](https://github.com/amazon-science/mintaka)

### Dataset Summary

Mintaka is a complex, natural, and multilingual question answering (QA) dataset composed of 20,000 question-answer pairs elicited from MTurk workers and annotated with Wikidata question and answer entities. Full details on the Mintaka dataset can be found in our paper: https://aclanthology.org/2022.coling-1.138/

To build Mintaka, we explicitly collected questions in 8 complexity types, as well as generic questions:

- Count (e.g., Q: How many astronauts have been elected to Congress? A: 4)
- Comparative (e.g., Q: Is Mont Blanc taller than Mount Rainier? A: Yes)
- Superlative (e.g., Q: Who was the youngest tribute in the Hunger Games? A: Rue)
- Ordinal (e.g., Q: Who was the last Ptolemaic ruler of Egypt? A: Cleopatra)
- Multi-hop (e.g., Q: Who was the quarterback of the team that won Super Bowl 50? A: Peyton Manning)
- Intersection (e.g., Q: Which movie was directed by Denis Villeneuve and stars Timothee Chalamet? A: Dune)
- Difference (e.g., Q: Which Mario Kart game did Yoshi not appear in? A: Mario Kart Live: Home Circuit)
- Yes/No (e.g., Q: Has Lady Gaga ever made a song with Ariana Grande? A: Yes.)
- Generic (e.g., Q: Where was Michael Phelps born? A: Baltimore, Maryland)
- We collected questions about 8 categories: Movies, Music, Sports, Books, Geography, Politics, Video Games, and History

Mintaka is one of the first large-scale complex, natural, and multilingual datasets that can be used for end-to-end question-answering models.

### Supported Tasks and Leaderboards

The dataset can be used to train a model for question answering.
To ensure comparability, please refer to our evaluation script here: https://github.com/amazon-science/mintaka#evaluation

### Languages

All questions were written in English and translated into 8 additional languages: Arabic, French, German, Hindi, Italian, Japanese, Portuguese, and Spanish.

## Dataset Structure

### Data Instances

An example of 'train' looks as follows.

```json
{
  "id": "a9011ddf",
  "lang": "en",
  "question": "What is the seventh tallest mountain in North America?",
  "answerText": "Mount Lucania",
  "category": "geography",
  "complexityType": "ordinal",
  "questionEntity":
  [
      {
          "name": "Q49",
          "entityType": "entity",
          "label": "North America",
          "mention": "North America",
          "span": [40, 53]
      },
      {
          "name": 7,
          "entityType": "ordinal",
          "mention": "seventh",
          "span": [12, 19]
      }
  ],
  "answerEntity":
  [
      {
          "name": "Q1153188",
          "label": "Mount Lucania",
      }
  ],
}
```

### Data Fields

The data fields are the same among all splits.

`id`: a unique ID for the given sample.

`lang`: the language of the question. 

`question`: the original question elicited in the corresponding language.

`answerText`: the original answer text elicited in English.

`category`: the category of the question. Options are: geography, movies, history, books, politics, music, videogames, or sports

`complexityType`: the complexity type of the question. Options are: ordinal, intersection, count, superlative, yesno comparative, multihop, difference, or generic

`questionEntity`:  a list of annotated question entities identified by crowd workers.
```
{
     "name": The Wikidata Q-code or numerical value of the entity
     "entityType": The type of the entity. Options are:
             entity, cardinal, ordinal, date, time, percent, quantity, or money
     "label": The label of the Wikidata Q-code
     "mention": The entity as it appears in the English question text. Will be empty for non-English samples.
     "span": The start and end characters of the mention in the English question text. Will be empty for non-English samples.
}
```
`answerEntity`:  a list of annotated answer entities identified by crowd workers.
```
{
     "name": The Wikidata Q-code or numerical value of the entity
     "label": The label of the Wikidata Q-code
}
```

### Data Splits

For each language, we split into train (14,000 samples), dev (2,000 samples), and test (4,000 samples) sets.

### Personal and Sensitive Information

The corpora is free of personal or sensitive information.

## Considerations for Using the Data
### Social Impact of Dataset
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Discussion of Biases
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Other Known Limitations
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Additional Information

### Dataset Curators

Amazon Alexa AI.

### Licensing Information

This project is licensed under the CC-BY-4.0 License.

### Citation Information

Please cite the following papers when using this dataset.

```latex
@inproceedings{sen-etal-2022-mintaka,
    title = "Mintaka: A Complex, Natural, and Multilingual Dataset for End-to-End Question Answering",
    author = "Sen, Priyanka  and
      Aji, Alham Fikri  and
      Saffari, Amir",
    booktitle = "Proceedings of the 29th International Conference on Computational Linguistics",
    month = oct,
    year = "2022",
    address = "Gyeongju, Republic of Korea",
    publisher = "International Committee on Computational Linguistics",
    url = "https://aclanthology.org/2022.coling-1.138",
    pages = "1604--1619"
}
```

### Contributions

Thanks to [@afaji](https://github.com/afaji) for adding this dataset.