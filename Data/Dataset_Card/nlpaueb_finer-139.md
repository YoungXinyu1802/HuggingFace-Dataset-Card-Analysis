---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: FiNER-139
size_categories:
- 1M<n<10M
source_datasets: []
task_categories:
- structure-prediction
- named-entity-recognition
- entity-extraction
task_ids:
- named-entity-recognition
---

# Dataset Card for FiNER-139

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks)
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
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
- [SEC-BERT](#sec-bert)
- [About Us](#about-us)

## Dataset Description

- **Homepage:** [FiNER](https://github.com/nlpaueb/finer)
- **Repository:** [FiNER](https://github.com/nlpaueb/finer)
- **Paper:** [FiNER, Loukas et al. (2022)](https://arxiv.org/abs/2203.06482)
- **Point of Contact:** [Manos Fergadiotis](mailto:fergadiotis@aueb.gr)

### Dataset Summary

<div style="text-align: justify">
<strong>FiNER-139</strong> is comprised of 1.1M sentences annotated with <strong>eXtensive Business Reporting Language (XBRL)</strong> tags extracted from annual and quarterly reports of publicly-traded companies in the US. 
Unlike other entity extraction tasks, like named entity recognition (NER) or contract element extraction, which typically require identifying entities of a small set of common types (e.g., persons, organizations), FiNER-139 uses a much larger label set of <strong>139 entity types</strong>. 
Another important difference from typical entity extraction is that FiNER focuses on numeric tokens, with the correct tag depending mostly on context, not the token itself.
</div>

### Supported Tasks

<div style="text-align: justify">
To promote transparency among shareholders and potential investors, publicly traded companies are required to file periodic financial reports annotated with tags from the eXtensive Business Reporting Language (XBRL), an XML-based language, to facilitate the processing of financial information. 
However, manually tagging reports with XBRL tags is tedious and resource-intensive. 
We, therefore, introduce <strong>XBRL tagging</strong> as a <strong>new entity extraction task</strong> for the <strong>financial domain</strong> and study how financial reports can be automatically enriched with XBRL tags. 
To facilitate research towards automated XBRL tagging we release FiNER-139.
</div>

### Languages

**FiNER-139** is compiled from approximately 10k annual and quarterly **English** reports

## Dataset Structure

### Data Instances

This is a "train" split example:

```json
{
	'id': 40
	'tokens': ['In', 'March', '2014', ',', 'the', 'Rialto', 'segment', 'issued', 'an', 'additional', '$', '100', 'million', 'of', 'the', '7.00', '%', 'Senior', 'Notes', ',', 'at', 'a', 'price', 'of', '102.25', '%', 'of', 'their', 'face', 'value', 'in', 'a', 'private', 'placement', '.']
	'ner_tags': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 37, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
```

### Data Fields

**id**: ID of the example <br>
**tokens**: List of tokens for the specific example. <br>
**ner_tags**: List of tags for each token in the example. Tags are provided as integer classes.<br>

If you want to use the class names you can access them as follows:

```python
import datasets

finer_train = datasets.load_dataset("nlpaueb/finer-139", split="train")

finer_tag_names = finer_train.features["ner_tags"].feature.names
```

**finer_tag_names** contains a list of class names corresponding to the integer classes e.g.
```
0 -> "O"
1 -> "B-AccrualForEnvironmentalLossContingencies"
```

### Data Splits

| Training | Validation | Test
| -------- | ---------- | -------
| 900,384 | 112,494 | 108,378

## Dataset Creation

### Curation Rationale

The dataset was curated by [Loukas et al. (2022)](https://arxiv.org/abs/2203.06482) <br>

### Source Data

#### Initial Data Collection and Normalization

<div style="text-align: justify">

FiNER-139 is compiled from approximately 10k annual and quarterly English reports (filings) of publicly traded companies downloaded from the [US Securities
and Exchange Commission's (SEC)](https://www.sec.gov/) [Electronic Data Gathering, Analysis, and Retrieval (EDGAR)](https://www.sec.gov/edgar.shtml) system.
The reports span a 5-year period, from 2016 to 2020. They are annotated with XBRL tags by professional auditors and describe the performance and projections of the companies. XBRL defines approximately 6k entity types from the US-GAAP taxonomy. FiNER-139 is annotated with the 139 most frequent XBRL entity types with at least 1,000 appearances.
We used regular expressions to extract the text notes from the Financial Statements Item of each filing, which is the primary source of XBRL tags in annual and quarterly reports. We used the <strong>IOB2</strong> annotation scheme to distinguish tokens at the beginning, inside, or outside of tagged expressions, which leads to 279 possible token labels.
</div>

### Annotations

#### Annotation process

<div style="text-align: justify">

All the examples were annotated by professional auditors as required by the Securities & Exchange Commission (SEC) legislation.
Even though the gold XBRL tags come from professional auditors there are still some discrepancies. Consult [Loukas et al. (2022)](https://arxiv.org/abs/2203.06482), (Section 9.4) for more details
</div>

#### Who are the annotators?

Professional auditors

### Personal and Sensitive Information

The dataset contains publicly available annual and quarterly reports (filings)

## Additional Information

### Dataset Curators

[Loukas et al. (2022)](https://arxiv.org/abs/2203.06482)

### Licensing Information

<div style="text-align: justify">
Access to SEC's EDGAR public database is free, allowing research of public companies' financial information and operations by reviewing the filings the companies makes with the SEC.
</div>

### Citation Information

If you use this dataset cite the following

```
@inproceedings{loukas-etal-2022-finer,
    title = {FiNER: Financial Numeric Entity Recognition for XBRL Tagging},
    author = {Loukas, Lefteris and
      Fergadiotis, Manos and
      Chalkidis, Ilias and
      Spyropoulou, Eirini and
      Malakasiotis, Prodromos and
      Androutsopoulos, Ion and
      Paliouras George},
    booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL 2022)},
    publisher = {Association for Computational Linguistics},
    location = {Dublin, Republic of Ireland},
    year = {2022},
    url = {https://arxiv.org/abs/2203.06482}
}
```

## SEC-BERT
<img align="center" src="https://i.ibb.co/0yz81K9/sec-bert-logo.png" alt="SEC-BERT" width="400"/>

<div style="text-align: justify">
We also pre-train our own BERT models (<strong>SEC-BERT</strong>) for the financial domain, intended to assist financial NLP research and FinTech applications. <br>
<strong>SEC-BERT</strong> consists of the following models:

* [**SEC-BERT-BASE**](https://huggingface.co/nlpaueb/sec-bert-base): Same architecture as BERT-BASE trained on financial documents.
* [**SEC-BERT-NUM**](https://huggingface.co/nlpaueb/sec-bert-num): Same as SEC-BERT-BASE but we replace every number token with a [NUM] pseudo-token handling all numeric expressions in a uniform manner, disallowing their fragmentation
* [**SEC-BERT-SHAPE**](https://huggingface.co/nlpaueb/sec-bert-shape): Same as SEC-BERT-BASE but we replace numbers with pseudo-tokens that represent the number’s shape, so numeric expressions (of known shapes) are no longer fragmented, e.g., '53.2' becomes '[XX.X]' and '40,200.5' becomes '[XX,XXX.X]'.

These models were pre-trained on 260,773 10-K filings (annual reports) from 1993-2019, publicly available at [U.S. Securities and Exchange Commission (SEC)](https://www.sec.gov/)
</div>

## About Us
<div style="text-align: justify">

[**AUEB's Natural Language Processing Group**](http://nlp.cs.aueb.gr) develops algorithms, models, and systems that allow computers to process and generate natural language texts.

The group's current research interests include:
* question answering systems for databases, ontologies, document collections, and the Web, especially biomedical question answering,
* natural language generation from databases and ontologies, especially Semantic Web ontologies,
text classification, including filtering spam and abusive content,
* information extraction and opinion mining, including legal text analytics and sentiment analysis,
* natural language processing tools for Greek, for example parsers and named-entity recognizers,
machine learning in natural language processing, especially deep learning.

The group is part of the Information Processing Laboratory of the Department of Informatics of the Athens University of Economics and Business.
</div>

[Manos Fergadiotis](https://manosfer.github.io) on behalf of [AUEB's Natural Language Processing Group](http://nlp.cs.aueb.gr)