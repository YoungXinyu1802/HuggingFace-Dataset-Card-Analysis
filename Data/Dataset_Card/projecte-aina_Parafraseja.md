---
annotations_creators:
- CLiC-UB
language_creators:
- found
language:
- ca
license:
- cc-by-nc-nd-4.0
multilinguality:
- monolingual
pretty_name: Parafraseja
size_categories:
- ?
task_categories:
- text-classification
task_ids:
- multi-input-text-classification
---

# Dataset Card for Parafraseja

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

- **Point of Contact:** [blanca.calvo@bsc.es](blanca.calvo@bsc.es)

### Dataset Summary

Parafraseja is a dataset of 21,984 pairs of sentences with a label that indicates if they are paraphrases or not. The original sentences were collected from [TE-ca](https://huggingface.co/datasets/projecte-aina/teca) and [STS-ca](https://huggingface.co/datasets/projecte-aina/sts-ca). For each sentence, an annotator wrote a sentence that was a paraphrase and another that was not. The guidelines of this annotation are available. 

### Supported Tasks and Leaderboards

This dataset is mainly intended to train models for paraphrase detection.

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

The dataset consists of pairs of sentences labelled with "Parafrasis" or "No Parafrasis" in a jsonl format.

### Data Instances

<pre>
  {
    "id": "te1_14977_1", 
    "source": "teca", 
    "original": "La 2a part consta de 23 cap\u00edtols, cadascun dels quals descriu un ocell diferent.", 
    "new": "La segona part consisteix en vint-i-tres cap\u00edtols, cada un dels quals descriu un ocell diferent.", 
    "label": "Parafrasis"
   }
</pre>

### Data Fields
- original: original sentence
- new: new sentence, which could be a paraphrase or a non-paraphrase
- label: relation between original and new

### Data Splits

* dev.json: 2,000 examples
* test.json: 4,000 examples
* train.json: 15,984 examples

## Dataset Creation

### Curation Rationale

We created this corpus to contribute to the development of language models in Catalan, a low-resource language. 

### Source Data

The original sentences of this dataset came from the [STS-ca](https://huggingface.co/datasets/projecte-aina/sts-ca) and the [TE-ca](https://huggingface.co/datasets/projecte-aina/teca).

#### Initial Data Collection and Normalization

11,543 of the original sentences came from TE-ca, and 10,441 came from STS-ca.

#### Who are the source language producers?

TE-ca and STS-ca come from the [Catalan Textual Corpus](https://zenodo.org/record/4519349#.Y1Zs__uxXJF), which consists of several corpora gathered from web crawling and public corpora, and [Vilaweb](https://www.vilaweb.cat), a Catalan newswire.

### Annotations

The dataset is annotated with the label "Parafrasis" or "No Parafrasis" for each pair of sentences.

#### Annotation process

The annotation process was done by a single annotator and reviewed by another. 

#### Who are the annotators?

The annotators were Catalan native speakers, with a background on linguistics.

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

We hope this corpus contributes to the development of language models in Catalan, a low-resource language.

### Discussion of Biases

We are aware that this data might contain biases. We have not applied any steps to reduce their impact.

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)


This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).

### Licensing Information

[Creative Commons Attribution Non-commercial No-Derivatives 4.0 International](https://creativecommons.org/licenses/by-nc-nd/4.0/).



### Contributions

[N/A]
