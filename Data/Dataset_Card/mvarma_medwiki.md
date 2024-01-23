---
YAML tags:
annotations_creators:
- machine-generated
language_creators:
- crowdsourced
language:
- en-US
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: medwiki
size_categories:
- unknown
source_datasets:
- extended|wikipedia
task_categories:
- text-retrieval
task_ids:
- entity-linking-retrieval
---

# Dataset Card for MedWiki

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
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

- **Repository:** [Github](https://github.com/HazyResearch/medical-ned-integration)
- **Paper:** [Cross-Domain Data Integration for Named Entity Disambiguation in Biomedical Text](https://arxiv.org/abs/2110.08228)
- **Point of Contact:** [Maya Varma](mailto:mvarma2@stanford.edu)

### Dataset Summary

MedWiki is a large sentence dataset collected from a medically-relevant subset of Wikipedia and annotated with biomedical entities in the Unified Medical Language System (UMLS) knowledge base. For each entity, we include a rich set of types sourced from both UMLS and WikiData. Consisting of over 13 million sentences and 17 million entity annotations, MedWiki can be utilized as a pretraining resource for language models and can improve performance of medical named entity recognition and disambiguation systems, especially on rare entities. 

Here, we include two configurations of MedWiki (further details in [Dataset Creation](#dataset-creation)):
- `MedWiki-Full` is a large sentence dataset with UMLS medical entity annotations generated through the following two steps: (1) a weak labeling proecedure to annotate WikiData entities in sentences and (2) a data integration approach that maps WikiData entities to their counterparts in UMLS.
- `MedWiki-HQ` is a subset of MedWiki-Full with higher quality labels designed to limit noise that arises from the annotation procedure listed above.

### Languages

The text in the dataset is in English and was obtained from English Wikipedia.

## Dataset Structure

### Data Instances

A typical data point includes a sentence collected from Wikipedia annotated with UMLS medical entities and associated titles and types. 

An example from the MedWiki test set looks as follows:
```
{'sent_idx_unq': 57000409,
 'sentence': "The hair , teeth , and skeletal side effects of TDO are lifelong , and treatment is used to manage those effects .",
 'mentions': ['tdo'],
 'entities': ['C2931236'],
 'entity_titles': ['Tricho-dento-osseous syndrome 1'],
 'types': [['Disease or Syndrome', 'disease', 'rare disease', 'developmental defect during embryogenesis', 'malformation syndrome with odontal and/or periodontal component', 'primary bone dysplasia with increased bone density', 'syndromic hair shaft abnormality']],
 'spans': [[10, 11]]}
```

### Data Fields

- `sent_idx_unq`: a unique integer identifier for the data instance
- `sentence`: a string sentence collected from English Wikipedia. Punctuation is separated from words, and the sentence can be tokenized into word-pieces with the .split() method.
- `mentions`: list of medical mentions in the sentence.
- `entities`: list of UMLS medical entity identifiers corresponding to mentions. There is exactly one entity for each mention, and the length of the `entities` list is equal to the length of the `mentions` list.
- `entity_titles`: List of English titles collected from UMLS that describe each entity. The length of the `entity_titles` list is equal to the length of the `entities` list.
- `types`: List of category types associated with each entity, including types collected from UMLS and WikiData.
- `spans`: List of integer pairs representing the word span of each mention in the sentence.

### Data Splits

MedWiki includes two configurations: MedWiki-Full and MedWiki-HQ (described further in [Dataset Creation](#dataset-creation)). For each configuration, data is split into training, development, and test sets. The split sizes are as follow:

|                             | Train | Dev | Test |
| -----                       | ------ | ----- | ---- |
| MedWiki-Full Sentences      |11,784,235 | 649,132 | 648,608 |
| MedWiki-Full Mentions       |15,981,347 | 876,586 | 877,090 |
| MedWiki-Full Unique Entities | 230,871 | 55,002 | 54,772 |
| MedWiki-HQ Sentences        | 2,962,089 | 165,941 | 164,193 |
| MedWiki-HQ Mentions         | 3,366,108 | 188,957 | 186,622 |
| MedWiki-HQ Unique Entities      | 118,572 | 19,725 | 19,437 |

## Dataset Creation

### Curation Rationale

Existing medical text datasets are generally limited in scope, often obtaining low coverage over the entities and structural resources in the UMLS medical knowledge base. When language models are trained across such datasets, the lack of adequate examples may prevent models from learning the complex reasoning patterns that are necessary for performing effective entity linking or disambiguation, especially for rare entities as shown in prior work by [Orr et al.](http://cidrdb.org/cidr2021/papers/cidr2021_paper13.pdf). Wikipedia, which is often utilized as a rich knowledge source in general text settings, contains references to medical terms and can help address this issue. Here, we curate the MedWiki dataset, which is a large-scale, weakly-labeled dataset that consists of sentences from Wikipedia annotated with medical entities in the UMLS knowledge base. MedWiki can serve as a pretraining dataset for language models and holds potential for improving performance on medical named entity recognition tasks, especially on rare entities. 

### Source Data

#### Initial Data Collection and Normalization

MedWiki consists of sentences obtained from the November 2019 dump of English Wikipedia. We split pages into an 80/10/10 train/dev/test split and then segment each page at the sentence-level. This ensures that all sentences associated with a single Wikipedia page are placed in the same split. 

#### Who are the source language producers?

The source language producers are editors on English Wikipedia. 

### Annotations

#### Annotation process

We create two configurations of our dataset: MedWiki-Full and MedWiki-HQ. We label MedWiki-Full by first annotating all English Wikipedia articles with textual mentions and corresponding WikiData entities; we do so by obtaining gold entity labels from internal page links as well as generating weak labels based on pronouns and alternative entity names (see [Orr et al. 2020](http://cidrdb.org/cidr2021/papers/cidr2021_paper13.pdf) for additional information).  Then, we use the off-the-shelf entity linker [Bootleg](https://github.com/HazyResearch/bootleg) to map entities in WikiData to their counterparts in the 2017AA release of the Unified Medical Language System (UMLS), a standard knowledge base for biomedical entities (additional implementation details in forthcoming publication). Any sentence containing at least one UMLS entity is included in MedWiki-Full. We also include types associated with each entity, which are collected from both WikiData and UMLS using the generated UMLS-Wikidata mapping. It is important to note that types obtained from WikiData are filtered according to methods described in [Orr et al. 2020](http://cidrdb.org/cidr2021/papers/cidr2021_paper13.pdf). 

Since our labeling procedure introduces some noise into annotations, we also release the MedWiki-HQ dataset configuration with higher-quality labels. To generate MedWiki-HQ, we filtered the UMLS-Wikidata mappings to only include pairs of UMLS medical entities and WikiData items that share a high textual overlap between titles. MedWiki-HQ is a subset of MedWiki-Full.

To evaluate the quality of our UMLS-Wikidata mappings, we find that WikiData includes a small set of "true" labeled mappings between UMLS entities and WikiData items. (Note that we only include WikiData items associated with linked Wikipedia pages.) This set comprises approximately 9.3k UMLS entities in the original UMLS-Wikidata mapping (used for MedWiki-Full) and 5.6k entities in the filtered UMLS-Wikidata mapping (used for MedWiki-HQ). Using these labeled sets, we find that our mapping accuracy is 80.2% for the original UMLS-Wikidata mapping and 94.5% for the filtered UMLS-Wikidata mapping. We also evaluate integration performance on this segment as the proportion of mapped WikiData entities that share a WikiData type with the true entity, suggesting the predicted mapping adds relevant structural resources. Integration performance is 85.4% for the original UMLS-Wikidata mapping and 95.9% for the filtered UMLS-Wikidata mapping. The remainder of items in UMLS have no “true” mappings to WikiData.

#### Who are the annotators?

The dataset was labeled using weak-labeling techniques as described above.

### Personal and Sensitive Information

No personal or sensitive information is included in MedWiki.

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of this dataset is to enable the creation of better named entity recognition systems for biomedical text. MedWiki encompasses a large set of entities in the UMLS knowledge base and includes a rich set of types associated with each entity, which can enable the creation of models that achieve high performance on named entity recognition tasks, especially on rare or unpopular entities. Such systems hold potential for improving automated parsing and information retrieval from large quantities of biomedical text.

### Discussion of Biases

The data included in MedWiki comes from English Wikipedia. Generally, Wikipedia articles are neutral in point of view and aim to avoid bias. However, some [prior work](https://www.hbs.edu/ris/Publication%20Files/15-023_e044cf50-f621-4759-a827-e9a3bf8920c0.pdf) has shown that ideological biases may exist within some Wikipedia articles, especially those that are focused on political issues or those that are written by fewer authors. We anticipate that such biases are rare for medical articles, which are typically comprised of scientific facts. However, it is important to note that bias encoded in Wikipedia is likely to be reflected by MedWiki.

### Other Known Limitations

Since MedWiki was annotated using weak labeling techniques, there is likely some noise in entity annotations. (Note that to address this, we include the MedWiki-HQ configuration, which is a subset of MedWiki-Full with higher quality labels. Additional details in [Dataset Creation](#dataset-creation)). 

## Additional Information

### Dataset Curators

MedWiki was curated by Maya Varma, Laurel Orr, Sen Wu, Megan Leszczynski, Xiao Ling, and Chris Ré. 

### Licensing Information

Dataset licensed under CC BY 4.0.

### Citation Information

```
@inproceedings{varma-etal-2021-cross-domain,
    title = "Cross-Domain Data Integration for Named Entity Disambiguation in Biomedical Text",
    author = "Varma, Maya  and
      Orr, Laurel  and
      Wu, Sen  and
      Leszczynski, Megan  and
      Ling, Xiao  and
      R{\'e}, Christopher",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-emnlp.388",
    pages = "4566--4575",
}
```

### Contributions

Thanks to [@maya124](https://github.com/maya124) for adding this dataset.
