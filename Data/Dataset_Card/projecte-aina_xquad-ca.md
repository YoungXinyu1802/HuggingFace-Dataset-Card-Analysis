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
pretty_name: xquad-ca
size_categories:
- unknown
source_datasets: []
task_categories:
- question-answering
task_ids:
- extractive-qa
---

# Dataset Card for XQuAD-Ca

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
- **Homepage:** https://zenodo.org/record/6669801
- **Paper:** [Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? A Comprehensive Assessment for Catalan](https://arxiv.org/abs/2107.07903)
- **Point of Contact:** [Carlos Rodríguez-Penagos](carlos.rodriguez1@bsc.es) and [Carme Armentano-Oller](carme.armentano@bsc.es)

### Dataset Summary

Professional translation into Catalan of [XQuAD dataset](https://github.com/deepmind/xquad).

XQuAD (Cross-lingual Question Answering Dataset) is a benchmark dataset for evaluating cross-lingual question answering performance. The dataset consists of a subset of 240 paragraphs and 1190 question-answer pairs from the development set of SQuAD v1.1 ([Rajpurkar, Pranav et al., 2016](http://arxiv.org/abs/1606.05250)) together with their professional translations into ten language: Spanish, German, Greek, Russian, Turkish, Arabic, Vietnamese, Thai, Chinese, and Hindi. Rumanian was added later. We added the 13th language to the corpus using also professional native Catalan translators.

XQuAD and XQuAD-Ca datasets are released under [CC-by-sa](https://creativecommons.org/licenses/by-sa/3.0/legalcode) licence. 

### Supported Tasks and Leaderboards

Cross-lingual-QA, Extractive-QA, Language Model

### Languages

The dataset is in Catalan (`ca-CA`)

## Dataset Structure

### Data Instances

One json file.

1189 examples.

<pre>

{
  "data": [
    {
          "context": "Al llarg de la seva existència, Varsòvia ha estat una ciutat multicultural. Segons el cens del 1901, de 711.988 habitants, el 56,2 % eren catòlics, el 35,7 % jueus, el 5 % cristians ortodoxos grecs i el 2,8 % protestants. Vuit anys després, el 1909, hi havia 281.754 jueus (36,9 %), 18.189 protestants (2,4 %) i 2.818 mariavites (0,4 %). Això va provocar que es construïssin centenars de llocs de culte religiós a totes les parts de la ciutat. La majoria d’ells es van destruir després de la insurrecció de Varsòvia del 1944. Després de la guerra, les noves autoritats comunistes de Polònia van apocar la construcció d’esglésies i només se’n va construir un petit nombre.",
          "qas": [
            {
              "answers": [
                {
                  "text": "711.988",
                  "answer_start": 104
                }
              ],
              "id": "57338007d058e614000b5bdb",
              "question": "Quina era la població de Varsòvia l’any 1901?"
            },
            {
              "answers": [
                {
                  "text": "56,2 %",
                  "answer_start": 126
                }
              ],
              "id": "57338007d058e614000b5bdc",
              "question": "Dels habitants de Varsòvia l’any 1901, quin percentatge era catòlic?"
            },
            ...
          ]
        }
      ]
    }, 
    ...

   ]
} 

</pre>

### Data Fields

Follows [Rajpurkar, Pranav et al., 2016](http://arxiv.org/abs/1606.05250) for SQuAD v1 datasets.

- `id` (str): Unique ID assigned to the question.
- `title` (str): Title of the Wikipedia article.
- `context` (str): Wikipedia section text.
- `question` (str): Question.
- `answers` (list): List of answers to the question, each containing:
  - `text` (str): Span text answering to the question.
  - `answer_start` Starting offset of the span text answering to the question.

### Data Splits

- test.json: 1189 examples.


## Dataset Creation

### Curation Rationale

We created this dataset to contribute to the development of language models in Catalan, a low-resource language, and for compatibility with similar datasets in other languages, and to allow inter-lingual comparisons. 

### Source Data

- [XQuAD's webpage](https://github.com/deepmind/xquad).

#### Initial Data Collection and Normalization

This dataset is a professional translation of [XQuAD](https://github.com/deepmind/xquad) into Catalan, commissioned by [BSC TeMU](https://temu.bsc.es/) within [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina/). 

For more information on how XQuAD was created, refer to the paper, On the [Cross-lingual Transferability of Monolingual Representations](https://arxiv.org/abs/1910.11856), or visit the [XQuAD's webpage](https://github.com/deepmind/xquad).

#### Who are the source language producers?

For more information on how XQuAD was created, refer to the paper, [On the Cross-lingual Transferability of Monolingual Representations   ](https://arxiv.org/abs/1910.11856), or visit the [XQuAD's webpage](https://github.com/deepmind/xquad).

### Annotations

This is a professional translation of the XQuAD corpus and its annotations.

#### Annotation process

[N/A]

#### Who are the annotators?

Translation was commissioned to a professional translation company.

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset contributes to the development of language models in Catalan, a low-resource language.

### Discussion of Biases

[N/A]

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

Carlos Rodríguez-Penagos (carlos.rodriguez1@bsc.es) and Carme Armentano-Oller (carme.armentano@bsc.es) from [BSC-CNS](https://www.bsc.es/).


This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).


### Licensing Information

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

### Citation Information

```

@inproceedings{armengol-estape-etal-2021-multilingual,
    title = "Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? {A} Comprehensive Assessment for {C}atalan",
    author = "Armengol-Estap{\'e}, Jordi  and
      Carrino, Casimiro Pio  and
      Rodriguez-Penagos, Carlos  and
      de Gibert Bonet, Ona  and
      Armentano-Oller, Carme  and
      Gonzalez-Agirre, Aitor  and
      Melero, Maite  and
      Villegas, Marta",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.437",
    doi = "10.18653/v1/2021.findings-acl.437",
    pages = "4933--4946",
}

```


[DOI](https://doi.org/10.5281/zenodo.4526223)



### Contributions

[N/A]