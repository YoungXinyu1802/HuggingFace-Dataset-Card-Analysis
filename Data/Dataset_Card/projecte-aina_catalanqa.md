---

annotations_creators:
- expert-generated
language_creators:
- found
language:
- ca
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: catalanqa
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- extractive-qa

---
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

# Dataset Card for CatalanQA
    
## Dataset Description
- **Homepage:** https://github.com/projecte-aina
- **Point of Contact:** [Carlos Rodríguez-Penagos](mailto:carlos.rodriguez1@bsc.es) and [Carme Armentano-Oller](mailto:carme.armentano@bsc.es)

### Dataset Summary

This dataset can be used to build extractive-QA and Language Models. It is an aggregation and balancing of 2 previous datasets: [VilaQuAD](https://huggingface.co/datasets/projecte-aina/vilaquad) and [ViquiQuAD](https://huggingface.co/datasets/projecte-aina/viquiquad).

Splits have been balanced by kind of question, and unlike other datasets like [SQuAD](http://arxiv.org/abs/1606.05250), it only contains, per record, one question and one answer for each context, although the contexts can repeat multiple times.

This dataset was developed by [BSC TeMU](https://temu.bsc.es/) as part of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina/), to enrich the [Catalan Language Understanding Benchmark (CLUB)](https://club.aina.bsc.es/).

### Supported Tasks and Leaderboards
Extractive-QA, Language Model.

### Languages
The dataset is in Catalan (`ca-CA`).

## Dataset Structure
### Data Instances
```
    {
      "title": "Els 521 policies espanyols amb més mala nota a les oposicions seran enviats a Catalunya",
      "paragraphs": [
        {
          "context": "El Ministeri d'Interior espanyol enviarà a Catalunya els 521 policies espanyols que han obtingut més mala nota a les oposicions. Segons que explica El País, hi havia mig miler de places vacants que s'havien de cobrir, però els agents amb més bones puntuacions han elegit destinacions diferents. En total van aprovar les oposicions 2.600 aspirants. D'aquests, en seran destinats al Principat 521 dels 560 amb més mala nota. Per l'altra banda, entre els 500 agents amb més bona nota, només 8 han triat Catalunya. Fonts de la policia espanyola que esmenta el diari ho atribueixen al procés d'independència, al Primer d'Octubre i a la 'situació social' que se'n deriva.",
          "qas": [
            {
              "question": "Quants policies enviaran a Catalunya?",
              "id": "0.5961700408283691",
              "answers": [
                {
                  "text": "521",
                  "answer_start": 57
                }
              ]
            }
          ]
        }
      ]
    },
```

### Data Fields
Follows [(Rajpurkar, Pranav et al., 2016)](http://arxiv.org/abs/1606.05250) for SQuAD v1 datasets:

- `id` (str): Unique ID assigned to the question.
- `title` (str): Title of the article.
- `context` (str): Article text.
- `question` (str): Question.
- `answers` (list): Answer to the question, containing:
  - `text` (str): Span text answering to the question.
  - `answer_start` Starting offset of the span text answering to the question.
  
### Data Splits
- train.json: 17135 question/answer pairs
- dev.json: 2157 question/answer pairs
- test.json: 2135 question/answer pairs

## Dataset Creation
### Curation Rationale

We created this corpus to contribute to the development of language models in Catalan, a low-resource language.

### Source Data
- [VilaWeb](https://www.vilaweb.cat/) and [Catalan Wikipedia](https://ca.wikipedia.org).

#### Initial Data Collection and Normalization
This dataset is a balanced aggregation from [ViquiQuAD](https://huggingface.co/datasets/projecte-aina/viquiquad) and [VilaQuAD](https://huggingface.co/datasets/projecte-aina/vilaquad) datasets.

#### Who are the source language producers?
Volunteers from [Catalan Wikipedia](https://ca.wikipedia.org) and professional journalists from [VilaWeb](https://www.vilaweb.cat/).

### Annotations
#### Annotation process
We did an aggregation and balancing from [ViquiQuAD](https://huggingface.co/datasets/projecte-aina/viquiquad) and [VilaQuAD](https://huggingface.co/datasets/projecte-aina/vilaquad) datasets.

To annotate those datasets, we commissioned the creation of 1 to 5 questions for each context, following an adaptation of the guidelines from SQuAD 1.0 [(Rajpurkar, Pranav et al., 2016)](http://arxiv.org/abs/1606.05250).

For compatibility with similar datasets in other languages, we followed as close as possible existing curation guidelines. 

#### Who are the annotators?
Annotation was commissioned by a specialized company that hired a team of native language speakers.

### Personal and Sensitive Information
No personal or sensitive information is included.

## Considerations for Using the Data
### Social Impact of Dataset
We hope this corpus contributes to the development of language models in Catalan, a low-resource language.

### Discussion of Biases
[N/A]

### Other Known Limitations
[N/A]

## Additional Information
### Dataset Curators
Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).

### Licensing Information
This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">Attribution-ShareAlike 4.0 International License</a>.

### Contributions

[N/A]