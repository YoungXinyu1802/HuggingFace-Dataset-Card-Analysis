---
annotations_creators:
- machine-generated
language:
- de
- nl
- en
- fr
- es
language_creators:
- expert-generated
license:
- cc-by-4.0
multilinguality:
- multilingual
pretty_name: Berlin State Library OCR
size_categories:
- 1M<n<10M
source_datasets: []
tags:
- ocr
- library
task_categories:
- fill-mask
- text-generation
task_ids:
- masked-language-modeling
- language-modeling
---

# Dataset Card for Berlin State Library OCR data

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

- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

> The digital collections of the SBB contain 153,942 digitized works from the time period of 1470 to 1945.

> At the time of publication, 28,909 works have been OCR-processed resulting in 4,988,099 full-text pages.
For each page with OCR text, the language has been determined by langid (Lui/Baldwin 2012).

### Supported Tasks and Leaderboards

- `language-modeling`: this dataset has the potential to be used for training language models on historical/OCR'd text. Since it contains OCR confidence, language and date information for many examples, it is also possible to filter this dataset to more closely match the requirements for training data. 
-  

### Languages

The collection includes material across a large number of languages. The languages of the OCR text have been detected using [langid.py: An Off-the-shelf Language Identification Tool](https://aclanthology.org/P12-3005) (Lui & Baldwin, ACL 2012). The dataset includes a confidence score for the language prediction. **Note:** not all examples may have been successfully matched to the language prediction table from the original data. 

The frequency of the top ten languages in the dataset is shown below: 

|    |        frequency |
|----|------------------|
| de |      3.20963e+06 |
| nl | 491322           |
| en | 473496           |
| fr | 216210           |
| es |  68869           |
| lb |  33625           |
| la |  27397           |
| pl |  17458           |
| it |  16012           |
| zh |  11971           |

[More Information Needed]

## Dataset Structure

### Data Instances

Each example represents a single page of OCR'd text. 

A single example of the dataset is as follows:

```python
{'aut': 'Doré, Henri',
 'date': '1912',
 'file name': '00000218.xml',
 'language': 'fr',
 'language_confidence': 1.0,
 'place': 'Chang-hai',
 'ppn': '646426230',
 'publisher': 'Imprimerie de la Mission Catholique',
 'text': "— 338 — Cela fait, on enterre la statuette qu’on vient d’outrager, atten dant la réalisation sur la personne elle-même. C’est l’outrage en effigie. Un deuxième moyen, c’est de représenter l’Esprit Vengeur sous la figure d’un fier-à-bras, armé d’un sabre, ou d’une pique, et de lui confier tout le soin de sa vengeance. On multiplie les incantations et les offrandes en son honneur, pour le porter au paroxysme de la fureur, et inspirer à l’Esprit malin l’idée de l’exécution de ses désirs : en un mot, on fait tout pour faire passer en son cœur la rage de vengeance qui consume le sien propre. C’est une invention diabolique imaginée pour assouvir sa haine sur l’ennemi qu’on a en horreur. Ailleurs, ce n’est qu’une figurine en bois ou en papier, qui est lancée contre l’ennemi; elle se dissimule, ou prend des formes fantastiques pour acomplir son œuvre de vengeance. Qu’on se rappelle la panique qui régna dans la ville de Nan- king ifâ ffl, et ailleurs, l’année où de méchantes gens répandirent le bruit que des hommes de papier volaient en l’air et coupaient les tresses de cheveux des Chinois. Ce fut une véritable terreur, tous étaient affolés, et il y eut à cette occasion de vrais actes de sauvagerie. Voir historiettes sur les envoûtements : Wieger Folk-Lore, N os 50, 128, 157, 158, 159. Corollaire. Les Tao-niu jift fx ou femmes “ Tao-clie'’. A cette super stition peut se rapporter la pratique des magiciennes du Kiang- sou ■n: m, dans les environs de Chang-hai ± m, par exemple. Ces femmes portent constamment avec- elles une statue réputée merveilleuse : elle n’a que quatre ou cinq pouces de hauteur ordinairement. A force de prières, d’incantations, elles finissent par la rendre illuminée, vivante et parlante, ou plutôt piaillarde, car elle ne répond que par des petits cris aigus et répétés aux demandes qu’on lui adressé; elle paraît comme animée, sautille,",
 'title': 'Les pratiques superstitieuses',
 'wc': [1.0,
  0.7266666889,
  1.0,
  0.9950000048,
  0.7059999704,
  0.5799999833,
  0.7142857313,
  0.7250000238,
  0.9855555296,
  0.6880000234,
  0.7099999785,
  0.7054545283,
  1.0,
  0.8125,
  0.7950000167,
  0.5681818128,
  0.5500000119,
  0.7900000215,
  0.7662500143,
  0.8830000162,
  0.9359999895,
  0.7411110997,
  0.7950000167,
  0.7962499857,
  0.6949999928,
  0.8937500119,
  0.6299999952,
  0.8820000291,
  1.0,
  0.6781818271,
  0.7649999857,
  0.437142849,
  1.0,
  1.0,
  0.7416666746,
  0.6474999785,
  0.8166666627,
  0.6825000048,
  0.75,
  0.7033333182,
  0.7599999905,
  0.7639999986,
  0.7516666651,
  1.0,
  1.0,
  0.5466666818,
  0.7571428418,
  0.8450000286,
  1.0,
  0.9350000024,
  1.0,
  1.0,
  0.7099999785,
  0.7250000238,
  0.8588888645,
  0.8366666436,
  0.7966666818,
  1.0,
  0.9066666961,
  0.7288888693,
  1.0,
  0.8333333135,
  0.8787500262,
  0.6949999928,
  0.8849999905,
  0.5816666484,
  0.5899999738,
  0.7922222018,
  1.0,
  1.0,
  0.6657142639,
  0.8650000095,
  0.7674999833,
  0.6000000238,
  0.9737499952,
  0.8140000105,
  0.978333354,
  1.0,
  0.7799999714,
  0.6650000215,
  1.0,
  0.823333323,
  1.0,
  0.9599999785,
  0.6349999905,
  1.0,
  0.9599999785,
  0.6025000215,
  0.8525000215,
  0.4875000119,
  0.675999999,
  0.8833333254,
  0.6650000215,
  0.7566666603,
  0.6200000048,
  0.5049999952,
  0.4524999857,
  1.0,
  0.7711111307,
  0.6666666865,
  0.7128571272,
  1.0,
  0.8700000048,
  0.6728571653,
  1.0,
  0.6800000072,
  0.6499999762,
  0.8259999752,
  0.7662500143,
  0.6725000143,
  0.8362500072,
  1.0,
  0.6600000262,
  0.6299999952,
  0.6825000048,
  0.7220000029,
  1.0,
  1.0,
  0.6587499976,
  0.6822222471,
  1.0,
  0.8339999914,
  0.6449999809,
  0.7062500119,
  0.9150000215,
  0.8824999928,
  0.6700000167,
  0.7250000238,
  0.8285714388,
  0.5400000215,
  1.0,
  0.7966666818,
  0.7350000143,
  0.6188889146,
  0.6499999762,
  1.0,
  0.7459999919,
  0.5799999833,
  0.7480000257,
  1.0,
  0.9333333373,
  0.790833354,
  0.5550000072,
  0.6700000167,
  0.7766666412,
  0.8280000091,
  0.7250000238,
  0.8669999838,
  0.5899999738,
  1.0,
  0.7562500238,
  1.0,
  0.7799999714,
  0.8500000238,
  0.4819999933,
  0.9350000024,
  1.0,
  0.8399999738,
  0.7950000167,
  1.0,
  0.9474999905,
  0.453333348,
  0.6575000286,
  0.9399999976,
  0.6733333468,
  0.8042857051,
  0.7599999905,
  1.0,
  0.7355555296,
  0.6499999762,
  0.7118181586,
  1.0,
  0.621999979,
  0.7200000286,
  1.0,
  0.853333354,
  0.6650000215,
  0.75,
  0.7787500024,
  1.0,
  0.8840000033,
  1.0,
  0.851111114,
  1.0,
  0.9142857194,
  1.0,
  0.8899999857,
  1.0,
  0.9024999738,
  1.0,
  0.6166666746,
  0.7533333302,
  0.7766666412,
  0.6637499928,
  1.0,
  0.8471428752,
  0.7012500167,
  0.6600000262,
  0.8199999928,
  1.0,
  0.7766666412,
  0.3899999857,
  0.7960000038,
  0.8050000072,
  1.0,
  0.8000000119,
  0.7620000243,
  1.0,
  0.7163636088,
  0.5699999928,
  0.8849999905,
  0.6166666746,
  0.8799999952,
  0.9058333039,
  1.0,
  0.6866666675,
  0.7810000181,
  0.3400000036,
  0.2599999905,
  0.6333333254,
  0.6524999738,
  0.4875000119,
  0.7425000072,
  0.75,
  0.6863636374,
  1.0,
  0.8742856979,
  0.137500003,
  0.2099999934,
  0.4199999869,
  0.8216666579,
  1.0,
  0.7563636303,
  0.3000000119,
  0.8579999804,
  0.6679999828,
  0.7099999785,
  0.7875000238,
  0.9499999881,
  0.5799999833,
  0.9150000215,
  0.6600000262,
  0.8066666722,
  0.729090929,
  0.6999999881,
  0.7400000095,
  0.8066666722,
  0.2866666615,
  0.6700000167,
  0.9225000143,
  1.0,
  0.7599999905,
  0.75,
  0.6899999976,
  0.3600000143,
  0.224999994,
  0.5799999833,
  0.8874999881,
  1.0,
  0.8066666722,
  0.8985714316,
  0.8827272654,
  0.8460000157,
  0.8880000114,
  0.9533333182,
  0.7966666818,
  0.75,
  0.8941666484,
  1.0,
  0.8450000286,
  0.8666666746,
  0.9533333182,
  0.5883333087,
  0.5799999833,
  0.6549999714,
  0.8600000143,
  1.0,
  0.7585714459,
  0.7114285827,
  1.0,
  0.8519999981,
  0.7250000238,
  0.7437499762,
  0.6639999747,
  0.8939999938,
  0.8877778053,
  0.7300000191,
  1.0,
  0.8766666651,
  0.8019999862,
  0.8928571343,
  1.0,
  0.853333354,
  0.5049999952,
  0.5416666865,
  0.7963636518,
  0.5600000024,
  0.8774999976,
  0.6299999952,
  0.5749999881,
  0.8199999928,
  0.7766666412,
  1.0,
  0.9850000143,
  0.5674999952,
  0.6240000129,
  1.0,
  0.9485714436,
  1.0,
  0.8174999952,
  0.7919999957,
  0.6266666651,
  0.7887499928,
  0.7825000286,
  0.5366666913,
  0.65200001,
  0.832857132,
  0.7488889098]}
  ```
  

### Data Fields

- 'file name': filename of the original XML file 
- 'text': OCR'd text for that page of the item
- 'wc': the word confidence for each token predicted by the OCR engine 
- 'ppn': 'Pica production numbers' an internal ID used by the library.  See [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2702544.svg)](https://doi.org/10.5281/zenodo.2702544) for more details. 
 'language': language predicted by `langid.py` (see above for more details) 
 -'language_confidence': confidence score given by `langid.py`
- publisher: publisher of the item in which the text appears
- place: place of publication of the item in which the text appears
- date: date of the item in which the text appears
- title: title of the item in which the text appears
- aut: author of the item in which the text appears

[More Information Needed]

### Data Splits

This dataset contains only a single split `train`. 

## Dataset Creation

The dataset is created from [OCR fulltexts of the Digital Collections of the Berlin State Library (DC-SBB)](https://doi.org/10.5281/zenodo.3257041) hosted on Zenodo.  

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

The dataset is created from [OCR fulltexts of the Digital Collections of the Berlin State Library (DC-SBB)](https://doi.org/10.5281/zenodo.3257041) hosted on Zenodo.  This dataset includes text content produced through running Optical Character Recognition across 153,942 digitized works held by the Berlin State Library. 

The [dataprep.ipynb](https://huggingface.co/datasets/biglam/berlin_state_library_ocr/blob/main/dataprep.ipynb) was used to create this dataset. 

To make the dataset more useful for training language models, the following steps were carried out:
- the CSV `xml2csv_alto.csv`, which contains the full text corpus per document page (incl.OCR word confidences) was loaded using the `datasets` library
- this CSV was augmented with language information from `corpus-language.pkl` **note** some examples don't find a match for this. Sometimes this is because a text is blank, but some actual text may be missing predicted language information
- the CSV was further augmented by trying to map the PPN to fields in a metadata download created using [https://github.com/elektrobohemian/StabiHacks/blob/master/oai-analyzer/oai-analyzer.py](https://github.com/elektrobohemian/StabiHacks/blob/master/oai-analyzer/oai-analyzer.py). **note** not all examples are successfully matched to this metadata download. 


#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

This dataset contains machine-produced annotations for:

- the confidence scores the OCR engines used to produce the full-text materials. 
- the predicted languages and associated confidence scores produced by `langid.py`

The dataset also contains metadata for the following fields:

- author
- publisher
- the place of publication 
- title 


#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

This dataset contains historical material, potentially including names, addresses etc., but these are not likely to refer to living individuals. 

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

As with any historical material, the views and attitudes expressed in some texts will likely diverge from contemporary beliefs. One should consider carefully how this potential bias may become reflected in language models trained on this data.  

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

Initial data created by: Labusch, Kai; Zellhöfer, David

### Licensing Information

[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode)

### Citation Information

```
@dataset{labusch_kai_2019_3257041,
  author       = {Labusch, Kai and
                  Zellhöfer, David},
  title        = {{OCR fulltexts of the Digital Collections of the 
                   Berlin State Library (DC-SBB)}},
  month        = jun,
  year         = 2019,
  publisher    = {Zenodo},
  version      = {1.0},
  doi          = {10.5281/zenodo.3257041},
  url          = {https://doi.org/10.5281/zenodo.3257041}
}
```

### Contributions

Thanks to [@davanstrien](https://github.com/davanstrien) for adding this dataset.
