---
license: cc-by-nc-4.0
---

# Dataset Card for CLARA-MeD

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
- [Dataset Creation](#dataset-creation)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [https://clara-nlp.uned.es/home/med/](https://clara-nlp.uned.es/home/med/)
- **Repository:** [https://github.com/lcampillos/CLARA-MeD](https://github.com/lcampillos/CLARA-MeD)
- **Paper:** [http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/6439](http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/6439)
- **DOI:** [https://doi.org/10.20350/digitalCSIC/14644](https://doi.org/10.20350/digitalCSIC/14644)
- **Point of Contact:** [Leonardo Campillos-Llanos](leonardo.campillos@csic.es)

### Dataset Summary

A parallel corpus with a subset of 3800 sentence pairs of professional and laymen variants (149 862 tokens) as a benchmark for medical text simplification. This dataset was collected in the CLARA-MeD project, with the goal of simplifying medical texts in the Spanish language and reducing the language barrier to patient's informed decision making.

### Supported Tasks and Leaderboards

Medical text simplification

### Languages

Spanish

## Dataset Structure

### Data Instances

For each instance, there is a string for the source text (professional version), and a string for the target text (simplified version).

```
{'SOURCE': 'adenocarcinoma ductal de páncreas'
 'TARGET': 'Cáncer de páncreas'}
```

### Data Fields

- `SOURCE`: a string containing the professional version. 
- `TARGET`: a string containing the simplified version. 

## Dataset Creation

### Source Data

#### Who are the source language producers?

1. Drug leaflets and summaries of product characteristics from [CIMA](https://cima.aemps.es)
2. Cancer-related information summaries from the [National Cancer Institute](https://www.cancer.gov/)
3. Clinical trials announcements from [EudraCT](https://www.clinicaltrialsregister.eu/)

### Annotations

#### Annotation process

Semi-automatic alignment of technical and patient versions of medical sentences. Inter-annotator agreement measured with Cohen's Kappa (average Kappa = 0.839 +- 0.076; very high agreement).

#### Who are the annotators?

Leonardo Campillos-Llanos
Adrián Capllonch-Carriónb
Ana Rosa Terroba-Reinares
Ana Valverde-Mateos
Sofía Zakhir-Puig

### Personal and Sensitive Information

No personal and sensitive information was used.

### Licensing Information

These data are aimed at research and educational purposes, and released under a Creative Commons Non-Commercial Attribution (CC-BY-NC-A) 4.0 International License.

### Citation Information

Campillos Llanos, L., Terroba Reinares, A. R., Zakhir Puig, S., Valverde, A., & Capllonch-Carrión, A. (2022). Building a comparable corpus and a benchmark for Spanish medical text simplification. *Procesamiento del lenguaje natural*, 69, pp. 189--196. 

### Contributions

Thanks to [Jónathan Heras from Universidad de La Rioja](http://www.unirioja.es/cu/joheras) ([@joheras](https://github.com/joheras)) for formatting this dataset for Hugging Face.
