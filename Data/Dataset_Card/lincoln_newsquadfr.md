---
annotations_creators:
- private
language_creators: null
language:
- fr-FR
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
- newspaper
- online
task_categories:
- question-answering
task_ids:
- extractive-qa
- open-domain-qa
paperswithcode_id: null
---

# Dataset Card for newsquadfr

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** [lincoln.fr](https://www.lincoln.fr/)
- **Repository:** [github/Lincoln-France](https://github.com/Lincoln-France)
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [email](labinnovation@mel.lincoln.fr)

### Dataset Summary

newsquadfr is a small dataset created for Question Answering task. Contexts are paragraphs of articles extracted from nine online french newspaper during year 2020/2021. newsquadfr stands for Newspaper question answering dataset in french. inspired by Piaf and Squad dataset. 2 520 triplets context - question - answer.

```py
from datasets import load_dataset

ds_name = 'lincoln/newsquadfr'

# exemple 1
ds_newsquad = load_dataset(ds_name)

# exemple 2
data_files = {'train': 'train.json', 'test': 'test.json', 'valid': 'valid.json'}
ds_newsquad = load_dataset(ds_name, data_files=data_files)

# exemple 3
ds_newsquad = load_dataset(ds_name, data_files=data_files, split="valid+test")
```

(train set)

| website       | Nb  |
|---------------|-----|
| cnews         | 20  |
| francetvinfo  | 40  |
| la-croix      | 375 |
| lefigaro      | 160 |
| lemonde       | 325 |
| lesnumeriques | 70  |
| numerama      | 140 |
| sudouest      | 475 |
| usinenouvelle | 45  |



### Supported Tasks and Leaderboards

- extractive-qa
- open-domain-qa

### Languages

Fr-fr

## Dataset Structure

### Data Instances

```json
{'answers': {'answer_start': [53], 'text': ['manSuvre "agressive']},
 'article_id': 34138,
 'article_title': 'Caricatures, Libye, Haut-Karabakh... Les six dossiers qui '
                  'opposent Emmanuel Macron et Recep Tayyip Erdogan.',
 'article_url': 'https://www.francetvinfo.fr/monde/turquie/caricatures-libye-haut-karabakh-les-six-dossiers-qui-opposent-emmanuel-macron-et-recep-tayyip-erdogan_4155611.html#xtor=RSS-3-[france]',
 'context': 'Dans ce contexte déjà tendu, la France a dénoncé une manSuvre '
            '"agressive" de la part de frégates turques à l\'encontre de l\'un '
            "de ses navires engagés dans une mission de l'Otan, le 10 juin. "
            'Selon Paris, la frégate Le Courbet cherchait à identifier un '
            'cargo suspecté de transporter des armes vers la Libye quand elle '
            'a été illuminée à trois reprises par le radar de conduite de tir '
            "de l'escorte turque.",
 'id': '2261',
 'paragraph_id': 201225,
 'question': "Qu'est ce que la France reproche à la Turquie?",
 'website': 'francetvinfo'}
```

### Data Fields

- `answers`: a dictionary feature containing:
  - `text`: a `string` feature.
  - `answer_start`: a `int64` feature.
- `article_id`: a `int64` feature. 
- `article_title`: a string feature.
- `article_url`: a string feature.
- `context`: a `string` feature.
- `id`: a `string` feature.
- `paragraph_id`: a `int64` feature.
- `question`: a `string` feature.
- `website`: a `string` feature.


### Data Splits

| Split | Nb |
|-------|----|
| train |1650|
| test  |415 |
| valid |455 |

## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

Paragraphs were chosen according to theses rules:
- parent article must have more than 71% ASCII characters
- paragraphs size must be between 170 and 670 characters
- paragraphs shouldn't contain "A LIRE" or "A VOIR AUSSI"

Then, we stratified our original dataset to create this dataset according to :
- website
- number of named entities
- paragraph size



#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

Using Piaf annotation tools. Three different persons mostly.

#### Who are the annotators?

Lincoln

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

- Annotation is not well controlled
- asking question on news is biaised
 

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr

### Citation Information

[Needs More Information]