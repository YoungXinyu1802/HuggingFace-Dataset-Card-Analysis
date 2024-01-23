---
pretty_name: Non-Parallel MultiEURLEX (incl. Translations)
annotations_creators:
- found
language_creators:
- found
- machine-generated
language:
- en
- de 
- fr
- el
- sk
license:
- cc-by-sa-4.0
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
source_datasets:
- extended|multi_eurlex
task_categories:
- text-classification
task_ids:
- multi-label-classification
- topic-classification
---

# Dataset Card for "Non-Parallel MultiEURLEX (incl. Translations)"

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

- **Homepage:** https://github.com/nlpaueb/multi-eurlex/tree/realistic-zero-shot
- **Repository:** https://github.com/nlpaueb/multi-eurlex/tree/realistic-zero-shot
- **Paper:** TBA
- **Leaderboard:** N/A
- **Point of Contact:** [Ilias Chalkidis](mailto:ilias.chalkidis@di.ku.dk)

### Dataset Summary

**Documents**

MultiEURLEX of Chalkidis et al. (2021) comprises 65k EU laws in 23 official EU languages. Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU. Each EUROVOC label ID is associated with a *label descriptor*, e.g., [60, agri-foodstuffs],  [6006, plant product], [1115, fruit]. The descriptors are also available in the 23 languages. Chalkidis et al. (2019) published a monolingual (English) version of this dataset, called EUR-LEX, comprising 57k EU laws with the originally assigned gold labels.

In this new version, dubbed "Non-Parallel MultiEURLEX (incl. Translations)", MultiEURLEX comprises non-parallel documents across 5 languages (English, German, French, Greek, and Slovak), i.e., 11,000 different documents per language, including also translations from English to the rest of the 4 available languages.

### Supported Tasks and Leaderboards

MultiEURLEX can be used for legal topic classification, a multi-label classification task where legal documents need to be assigned concepts (in our case, from EUROVOC) reflecting their topics. Unlike EUR-LEX, however, MultiEURLEX supports labels from three different granularities (EUROVOC levels). More importantly, apart from monolingual (*one-to-one*) experiments, it can be used to study cross-lingual transfer scenarios, including *one-to-many* (systems trained in one language and used in other languages with no training data), and *many-to-one* or *many-to-many* (systems jointly trained in multiple languages and used in one or more other languages).

The dataset is not yet part of an established benchmark.

### Languages

The EU has 24 official languages. When new members join the EU, the set of official languages usually expands, except the languages are already included. MultiEURLEX covers 23 languages from seven language families (Germanic, Romance, Slavic, Uralic, Baltic, Semitic, Hellenic). EU laws are published in all official languages, except Irish, for resource-related reasons (Read more at https://europa.eu/european-union/about-eu/eu-languages_en). This wide coverage makes MultiEURLEX a valuable testbed for cross-lingual transfer. All languages use the Latin script, except for Bulgarian (Cyrillic script) and Greek. Several other languages are also spoken in EU countries. The EU is home to over 60 additional indigenous regional or minority languages, e.g., Basque, Catalan, Frisian, Saami, and Yiddish, among others, spoken by approx. 40 million people, but these additional languages are not considered official (in terms of EU), and EU laws are not translated to them.

This version of MultiEURLEX covers 5 EU languages (English, German, French, Greek, and Slovak). It also includes machine-translated versions of the documents using the EasyNMT framework (https://github.com/UKPLab/EasyNMT) utilizing the many-to-many M2M_100_418M model of Fan et al. (2020) for el-to-en and el-to-de pairs and the OPUS-MT (Tiedemann et al., 2020) models for the rest.

## Dataset Structure

### Data Instances

**Multilingual use of the dataset**

When the dataset is used in a multilingual setting selecting the the 'all_languages' flag:

```python
from datasets import load_dataset
dataset = load_dataset('nlpaueb/multi_eurlex', 'all_languages')
```

```json
{
  "celex_id": "31979D0509",
  "text": {"en": "COUNCIL DECISION  of 24 May 1979  on financial aid from the Community for the eradication of African swine fever in Spain  (79/509/EEC)\nTHE COUNCIL OF THE EUROPEAN COMMUNITIES\nHaving regard to the Treaty establishing the European Economic Community, and in particular Article 43 thereof,\nHaving regard to the proposal from the Commission (1),\nHaving regard to the opinion of the European Parliament (2),\nWhereas the Community should take all appropriate measures to protect itself against the appearance of African swine fever on its territory;\nWhereas to this end the Community has undertaken, and continues to undertake, action designed to contain outbreaks of this type of disease far from its frontiers by helping countries affected to reinforce their preventive measures ; whereas for this purpose Community subsidies have already been granted to Spain;\nWhereas these measures have unquestionably made an effective contribution to the protection of Community livestock, especially through the creation and maintenance of a buffer zone north of the river Ebro;\nWhereas, however, in the opinion of the Spanish authorities themselves, the measures so far implemented must be reinforced if the fundamental objective of eradicating the disease from the entire country is to be achieved;\nWhereas the Spanish authorities have asked the Community to contribute to the expenses necessary for the efficient implementation of a total eradication programme;\nWhereas a favourable response should be given to this request by granting aid to Spain, having regard to the undertaking given by that country to protect the Community against African swine fever and to eliminate completely this disease by the end of a five-year eradication plan;\nWhereas this eradication plan must include certain measures which guarantee the effectiveness of the action taken, and it must be possible to adapt these measures to developments in the situation by means of a procedure establishing close cooperation between the Member States and the Commission;\nWhereas it is necessary to keep the Member States regularly informed as to the progress of the action undertaken,",
           "en2fr": "DU CONSEIL du 24 mai 1979 concernant l'aide financiere de la Communaute e l'eradication de la peste porcine africaine en Espagne (79/509/CEE)\nLE CONSEIL DES COMMUNAUTAS EUROPENNES ...",
           "en2de": "...",
           "en2el": "...",
           "en2sk": "..."
  },
  "labels": [
    1,
    13,
    47
  ]
}
```

**Monolingual use of the dataset**

When the dataset is used in a monolingual setting selecting the ISO language code for one of the 5 supported languages, or supported translation pairs in the form src2trg, where src and trg are ISO language codes, e.g., en2fr for English translated to French. For example:

```python
from datasets import load_dataset
dataset = load_dataset('nlpaueb/multi_eurlex', 'en2fr')
```

```json
{
  "celex_id": "31979D0509", 
  "text": "DU CONSEIL du 24 mai 1979 concernant l'aide financiere de la Communaute e l'eradication de la peste porcine africaine en Espagne (79/509/CEE)\nLE CONSEIL DES COMMUNAUTAS EUROPENNES ...",
  "labels": [
    1,
    13,
    47
  ]
}
```

### Data Fields

**Multilingual use of the dataset**

The following data fields are provided for documents (`train`, `dev`, `test`):

`celex_id`: (**str**)  The official ID of the document. The CELEX number is the unique identifier for all publications in both Eur-Lex and CELLAR.\
`text`: (dict[**str**])  A dictionary with the 23 languages as keys and the full content of each document as values.\
`labels`: (**List[int]**) The relevant EUROVOC concepts (labels).


**Monolingual use of the dataset**

The following data fields are provided for documents (`train`, `dev`, `test`):

`celex_id`: (**str**)  The official ID of the document. The CELEX number is the unique identifier for all publications in both Eur-Lex and CELLAR.\
`text`: (**str**)  The full content of each document across languages.\
`labels`: (**List[int]**) The relevant EUROVOC concepts (labels).


If you want to use the descriptors of the EUROVOC concepts, similar to [Chalkidis et al. (2020)](https://aclanthology.org/2020.emnlp-main.607/), please download the relevant JSON file [here](https://raw.githubusercontent.com/nlpaueb/multi-eurlex/master/data/eurovoc_descriptors.json).
Then you may load it and use it:
```python
import json
from datasets import load_dataset

# Load the English part of the dataset
dataset = load_dataset('nlpaueb/multi_eurlex', 'en', split='train')

# Load (label_id, descriptor) mapping 
with open('./eurovoc_descriptors.json') as jsonl_file:
    eurovoc_concepts =  json.load(jsonl_file)

# Get feature map info
classlabel = dataset.features["labels"].feature

# Retrieve IDs and descriptors from dataset
for sample in dataset:
  print(f'DOCUMENT: {sample["celex_id"]}')
  # DOCUMENT: 32006D0213
  for label_id in sample['labels']:
    print(f'LABEL: id:{label_id}, eurovoc_id: {classlabel.int2str(label_id)}, \
            eurovoc_desc:{eurovoc_concepts[classlabel.int2str(label_id)]}')
    # LABEL: id: 1, eurovoc_id: '100160', eurovoc_desc: 'industry'
```

### Data Splits
<table>
<tr><td> Language </td> <td>   ISO code </td> <td>  Member Countries where official </td> <td>  EU Speakers [1] </td> <td>   Number of Documents [2] </td> </tr> 
<tr><td> English     </td> <td> <b>en</b>   </td> <td>  United Kingdom (1973-2020), Ireland (1973), Malta (2004)   </td> <td> 13/ 51% </td> <td>  11,000 / 1,000 / 5,000 </td> </tr> 
<tr><td> German    </td> <td>  <b>de</b>   </td> <td> Germany (1958), Belgium (1958), Luxembourg (1958)  </td> <td> 16/32% </td> <td> 11,000 / 1,000 / 5,000 </td> </tr> 
<tr><td> French    </td> <td>  <b>fr</b>   </td> <td> France (1958), Belgium(1958), Luxembourg (1958)  </td> <td> 12/26% </td> <td> 11,000 / 1,000 / 5,000 </td> </tr> 
<tr><td> Greek       </td> <td>  <b>el</b>   </td> <td> Greece (1981), Cyprus (2008) </td> <td>  3/4% </td> <td>  11,000 / 1,000 / 5,000 </td> </tr>  
<tr><td> Slovak      </td> <td>  <b>sk</b>   </td> <td> Slovakia (2004)  </td> <td>  1/1% </td> <td>  11,000 / 1,000 / 5,000 </td> </tr>  
</table>

[1] Native and Total EU speakers percentage (%) \
[2] Training / Development / Test Splits 

## Dataset Creation

### Curation Rationale

The original dataset was curated by Chalkidis et al. (2021).\
The new version of the dataset was curated by Xenouleas et al. (2022).\
The documents have been annotated by the Publications Office of EU (https://publications.europa.eu/en).

### Source Data

#### Initial Data Collection and Normalization

The original data are available at the EUR-LEX portal (https://eur-lex.europa.eu) in unprocessed formats (HTML, XML, RDF). The documents were downloaded from the EUR-LEX portal in HTML. The relevant EUROVOC concepts were downloaded from the SPARQL endpoint of the Publications Office of EU (http://publications.europa.eu/webapi/rdf/sparql). 
Chalkidis et al. (2021) stripped HTML mark-up to provide the documents in plain text format and inferred the labels for EUROVOC levels 1--3, by backtracking the EUROVOC hierarchy branches, from the originally assigned labels to their ancestors in levels 1--3, respectively.

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

All the documents of the dataset have been annotated by the Publications Office of EU (https://publications.europa.eu/en) with multiple concepts from EUROVOC (http://eurovoc.europa.eu/). EUROVOC has eight levels of concepts. Each document is assigned one or more concepts (labels). If a document is assigned a concept, the ancestors and descendants of that concept are typically not assigned to the same document. The documents were originally annotated with concepts from levels 3 to 8.
Chalkidis et al. (2021)augmented the annotation with three alternative sets of labels per document, replacing each assigned concept by its ancestor from level 1, 2, or 3, respectively. 
Thus, Chalkidis et al. (2021) provide four sets of gold labels per document, one for each of the first three levels of the hierarchy, plus the original sparse label assignment.Levels 4 to 8 cannot be used independently, as many documents have gold concepts from the third level; thus many documents will be mislabeled, if we discard level 3.


#### Who are the annotators?

Publications Office of EU (https://publications.europa.eu/en)

### Personal and Sensitive Information

The dataset contains publicly available EU laws that do not include personal or sensitive information with the exception of trivial information presented by consent, e.g., the names of the current presidents of the European Parliament and European Council, and other administration bodies.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

Xenouleas et al. (2021)

### Licensing Information

We provide MultiEURLEX with the same licensing as the original EU data (CC-BY-4.0):

© European Union, 1998-2021

The Commission’s document reuse policy is based on Decision 2011/833/EU. Unless otherwise specified, you can re-use the legal documents published in EUR-Lex for commercial or non-commercial purposes.

The copyright for the editorial content of this website, the summaries of EU legislation and the consolidated texts, which is owned by the EU, is licensed under the Creative Commons Attribution 4.0 International licence. This means that you can re-use the content provided you acknowledge the source and indicate any changes you have made.

Source: https://eur-lex.europa.eu/content/legal-notice/legal-notice.html \
Read more:  https://eur-lex.europa.eu/content/help/faq/reuse-contents-eurlex.html

### Citation Information

*Stratos Xenouleas, Alexia Tsoukara, Giannis Panagiotakis Ilias Chalkidis, and Ion Androutsopoulos.*
*Realistic Zero-Shot Cross-Lingual Transfer in Legal Topic Classification.*
*Proceedings of 12th Hellenic Conference on Artificial Intelligence (SETN 2022). Corfu, Greece. 2022*
```
@InProceedings{xenouleas-etal-2022-realistic-multieurlex,
  author = {Xenouleas, Stratos
                and Tsoukara, Alexia
                and Panagiotakis, Giannis
                and Chalkidis, Ilias
                and Androutsopoulos, Ion},
  title = {Realistic Zero-Shot Cross-Lingual Transfer in Legal Topic Classification},
  booktitle = {Proceedings of 12th Hellenic Conference on Artificial Intelligence (SETN 2022)},
  year = {2022},
  publisher = {Association for Computer Machinery},
  location = {Corfu, Greece},
}
```

### Contributions

Thanks to [@iliaschalkidis](https://github.com/iliaschalkidis) for adding this dataset.