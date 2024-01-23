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
pretty_name: VilaQuAD
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- extractive-qa
---

# Dataset Card for VilaQuAD

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

- **Homepage:** https://doi.org/10.5281/zenodo.4562337
- **Paper:** [Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? A Comprehensive Assessment for Catalan](https://arxiv.org/abs/2107.07903)
- **Point of Contact:** [Carlos Rodríguez-Penagos](mailto:carlos.rodriguez1@bsc.es) and [Carme Armentano-Oller](mailto:carme.armentano@bsc.es)

### Dataset Summary

VilaQuAD, An extractive QA dataset for Catalan, from [VilaWeb](https://www.vilaweb.cat/) newswire text.

This dataset contains 2095 of Catalan language news articles along with 1 to 5 questions referring to each fragment (or context).

VilaQuad articles are extracted from the daily [VilaWeb](https://www.vilaweb.cat/) and used under [CC-by-nc-sa-nd](https://creativecommons.org/licenses/by-nc-nd/3.0/deed.ca) licence. 

This dataset can be used to build extractive-QA and Language Models.

### Supported Tasks and Leaderboards

Extractive-QA, Language Model.

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

### Data Instances

```
{
  'id': 'P_556_C_556_Q1',
  'title': "El Macba posa en qüestió l'eufòria amnèsica dels anys vuitanta a l'estat espanyol",
  'context': "El Macba ha obert una nova exposició, 'Gelatina dura. Històries escamotejades dels 80', dedicada a revisar el discurs hegemònic que es va instaurar en aquella dècada a l'estat espanyol, concretament des del començament de la transició, el 1977, fins a la fita de Barcelona 92. És una mirada en clau espanyola, però també centralista, perquè més enllà dels esdeveniments ocorreguts a Catalunya i els artistes que els van combatre, pràcticament només s'hi mostren fets polítics i culturals generats des de Madrid. No es parla del País Basc, per exemple. Però, dit això, l'exposició revisa aquesta dècada de la història recent tot qüestionant un triomfalisme homogeneïtzador, que ja se sap que va arrasar una gran quantitat de sectors crítics i radicals de l'àmbit social, polític i cultural. Com diu la comissària, Teresa Grandas, de l'equip del Macba: 'El relat oficial dels anys vuitanta a l'estat espanyol va prioritzar la necessitat per damunt de la raó i va consolidar una mirada que privilegiava el futur abans que l'anàlisi del passat recent, obviant qualsevol consideració crítica respecte de la filiació amb el poder franquista.",
  'question': 'Com es diu la nova exposició que ha obert el Macba?',
  'answers': [
    {
      'text': "'Gelatina dura. Històries escamotejades dels 80'",
      'answer_start': 38
    }
  ]
}
```

### Data Fields

Follows [Rajpurkar, Pranav et al., (2016)](http://arxiv.org/abs/1606.05250) for SQuAD v1 datasets.

- `id` (str): Unique ID assigned to the question.
- `title` (str): Title of the VilaWeb article.
- `context` (str): VilaWeb section text.
- `question` (str): Question.
- `answers` (list): List of answers to the question, each containing:
  - `text` (str): Span text answering to the question.
  - `answer_start` Starting offset of the span text answering to the question.

### Data Splits

- train.json: 1295 contexts, 3882 questions
- dev.json: 400 contexts, 1200 questions
- test.json: 400 contexts, 1200 questions

## Dataset Creation

### Curation Rationale

We created this dataset to contribute to the development of language models in Catalan, a low-resource language.


### Source Data

- [VilaWeb site](https://www.vilaweb.cat/)

#### Initial Data Collection and Normalization

The source data are scraped articles from archives of Catalan newspaper website [Vilaweb](https://www.vilaweb.cat). 

From a the online edition of the newspaper [VilaWeb](https://www.vilaweb.cat), 2095 articles were randomnly selected. These headlines were also used to create a Textual Entailment dataset. For the extractive QA dataset, creation of between 1 and 5 questions for each news context was commissioned, following an adaptation of the guidelines from SQuAD 1.0 ([Rajpurkar, Pranav et al. (2016)](http://arxiv.org/abs/1606.05250)). In total, 6282 pairs of a question and an extracted fragment that contains the answer were created.

For compatibility with similar datasets in other languages, we followed as close as possible existing curation guidelines. We also created [another QA dataset with wikipedia](https://huggingface.co/datasets/projecte-aina/viquiquad) to ensure thematic and stylistic variety.

#### Who are the source language producers?

Professional journalists from the Catalan newspaper [VilaWeb](https://www.vilaweb.cat/).

### Annotations

#### Annotation process

We comissioned the creation of 1 to 5 questions for each context, following an adaptation of the guidelines from SQuAD 1.0 ([Rajpurkar, Pranav et al. (2016)](http://arxiv.org/abs/1606.05250)).

#### Who are the annotators?

Annotation was commissioned to an specialized company that hired a team of native language speakers.

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

We hope this dataset contributes to the development of language models in Catalan, a low-resource language.

### Discussion of Biases

[N/A]

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/en/inici/index.html) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina/).

### Licensing Information

This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">Attribution-ShareAlike 4.0 International License</a>.

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

[DOI](https://doi.org/10.5281/zenodo.4562337)


### Contributions

[N/A]