---
annotations_creators:
- other
language_creators:
- found
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 10M<n<100M
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- parsing
pretty_name: Annotated Reference Strings
---

# Dataset Card for annotated_reference_strings

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

- **Homepage:** [https://www.github.com/kylase](https://www.github.com/kylase)
- **Repository:** [https://www.github.com/kylase](https://www.github.com/kylase)
- **Point of Contact:** [Yuan Chuan Kee](https://www.github.com/kylase) 

### Dataset Summary

The `annotated_reference_strings` dataset comprises millions of the annotated reference strings, i.e. each token of the strings have an associated label such as author, title, year, etc.

These strings are synthesized using citation processor on millions of citations obtained from various sources, spanning different scientific domains.

### Supported Tasks

This dataset can be used for structure prediction.

### Languages

The dataset is composed of reference strings that are in English.

## Dataset Structure

### Data Instances

```json
{
  "source": "pubmed",
  "lang": "en",
  "entry_type": "article",
  "doi_prefix": "pubmed19n0001",
  "csl_style": "annual-reviews",
  "content": "<citation-number>8.</citation-number> <author>Mohr W.</author> <year>1977.</year> <title>[Morphology of bone tumors. 2. Morphology of benign bone tumors].</title> <container-title>Aktuelle Probleme in Chirurgie und Orthopadie.</container-title> <volume>5:</volume> <page>29–42</page>"
}
```

#### Important Note 

1. Each citation is rendered to _at most_ **17** CSL styles. Therefore, there will be near duplicates.
2. All characters (including punctuations) of a segment (**a segment consists of 1 or more token**) are enclosed by tag(s). 
   1. Only tokens that act as "conjunctions" are not enclosed in tags. These tokens will be labelled as `other`.
3. There will be instances which a segment can be enclosed by more than one tag e.g. `<issued><year>2021</year></issued>`. This depends on how the styles' author(s).

### Data Fields

- `source`: Describe the source of the citation. `{pubmed, jstor, crossref}`
- `lang`: Describe the language of the citation. `{en}`
- `entry_type`: Describe the BibTeX entry type. `{article, book, inbook, misc, techreport, phdthesis, incollection, inproceedings}`
- `doi_prefix`: For JSTOR and CrossRef, it is the prefix of the DOI. For PubMed, it is the directory (e.g. `pubmed19nXXXX` where `XXXX` is 4 digits) of which the citation is generated from.
- `csl_style`: The CSL style which the citation is rendered as.
- `content`: The rendered citation of a specific style with each segment enclosed by tags named after the CSL variables

### Data Splits

Data splits are not available yet.

## Dataset Creation

### Source Data

#### Initial Data Collection and Normalization

The citations that are used to generate these reference strings are obtained from 3 main sources:

- [PubMed](https://www.nlm.nih.gov/databases/download/pubmed_medline.html) (2019 Baseline)
- CrossRef via [Open Academic Graph v2](https://www.microsoft.com/en-us/research/project/open-academic-graph/)
- JSTOR Sample Datasets (not available online as of publication date)

If the citation is not in BibTeX format, [bibutils](https://sourceforge.net/p/bibutils/home/Bibutils/) is used to convert it to BibTeX.

#### Who are the source language producers?

The manner which the citations are rendered as reference strings are based on rules/specifications dictated by the publisher.
[Citation Style Language](https://citationstyles.org/) (CSL) is an established standard which such specifications are prescribed. 
Thousands of citation styles are available.

### Annotations

#### Annotation process

The annotation process involves 2 main interventions:
1. Modification of the styles' CSL specification to inject the CSL variable names as part of the render process
2. Sanitization of the rendered strings using regular expressions to ensure all tokens and characters are enclosed in the tags

#### Who are the annotators?

The original CSL specification are available on [GitHub](https://github.com/citation-style-language/styles).

The modification of the styles and the sanitization process are done by the author of this work.

## Additional Information

### Licensing Information

This dataset is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

### Citation Information

This dataset is a product of a Master Project done in the National University of Singapore. 

If you are using it, please cite the following: 

```bibtex
@techreport{kee2021,
    author = {Yuan Chuan Kee},
    title = {Synthesis of a large dataset of annotated reference strings for developing citation parsers},
    institution = {National University of Singapore},
    year = {2021}
}
```

### Contributions

Thanks to [@kylase](https://github.com/kylase) for adding this dataset.
