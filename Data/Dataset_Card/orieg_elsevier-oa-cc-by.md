---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: Elsevier OA CC-By
paperswithcode_id: elsevier-oa-cc-by
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- fill-mask
- summarization
- text-classification
task_ids:
- masked-language-modeling
- news-articles-summarization
- news-articles-headline-generation
---

# Dataset Card for Elsevier OA CC-By

## Table of Contents
- [Dataset Card for Elsevier OA CC-By](#dataset-card-for-elsevier-oa-cc-by)
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
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
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

- **Homepage:** https://elsevier.digitalcommonsdata.com/datasets/zm33cdndxs
- **Repository:** https://elsevier.digitalcommonsdata.com/datasets/zm33cdndxs
- **Paper:** https://arxiv.org/abs/2008.00774
- **Leaderboard:**
- **Point of Contact:** [@orieg](https://huggingface.co/orieg)

### Dataset Summary

Elsevier OA CC-By: This is a corpus of 40k (40,091) open access (OA) CC-BY articles from across Elsevier’s journals
representing a large scale, cross-discipline set of research data to support NLP and ML research. The corpus include full-text
articles published in 2014 to 2020 and are categorized in 27 Mid Level ASJC Code (subject classification).

***Distribution of Publication Years***

| Publication Year | Number of Articles |
| :---: | :---: |
| 2014 | 3018 |
| 2015 | 4438 |
| 2016 | 5913 |
| 2017 | 6419 |
| 2018 | 8016 |
| 2019 | 10135 |
| 2020 | 2159 |

***Distribution of Articles Per Mid Level ASJC Code. Each article can belong to multiple ASJC codes.***

| Discipline | Count |
| --- | ---: |
| General | 3847 |
| Agricultural and Biological Sciences | 4840 |
| Arts and Humanities | 982 |
| Biochemistry, Genetics and Molecular Biology | 8356 |
| Business, Management and Accounting | 937 |
| Chemical Engineering | 1878 |
| Chemistry | 2490 |
| Computer Science | 2039 |
| Decision Sciences | 406 |
| Earth and Planetary Sciences | 2393 |
| Economics, Econometrics and Finance | 976 |
| Energy | 2730 |
| Engineering | 4778 |
| Environmental Science | 6049 |
| Immunology and Microbiology | 3211 |
| Materials Science | 3477 |
| Mathematics | 538 |
| Medicine | 7273 |
| Neuroscience | 3669 |
| Nursing | 308 |
| Pharmacology, Toxicology and Pharmaceutics | 2405 |
| Physics and Astronomy | 2404 |
| Psychology | 1760 |
| Social Sciences | 3540 |
| Veterinary | 991 |
| Dentistry | 40 |
| Health Professions | 821 |

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

English (`en`).

## Dataset Structure
    
### Data Instances

The original dataset was published with the following json structure:
```
{
    "docId": <str>,
    "metadata":{
        "title": <str>,
        "authors": [
            {
                "first": <str>,
                "initial": <str>,
                "last": <str>,
                "email": <str>
            },
            ...
        ],
        "issn": <str>,
        "volume": <str>,
        "firstpage": <str>,
        "lastpage": <str>,
        "pub_year": <int>,
        "doi": <str>,
        "pmid": <str>,
        "openaccess": "Full",
        "subjareas": [<str>],
        "keywords": [<str>],
        "asjc": [<int>],
    },
    "abstract":[
        {
          "sentence": <str>,
          "startOffset": <int>,
          "endOffset": <int>
        },
        ...
    ],
    "bib_entries":{
        "BIBREF0":{
            "title":<str>,
            "authors":[
                {
                "last":<str>,
                "initial":<str>,
                "first":<str>
                },
                ...
            ],
            "issn": <str>,
            "volume": <str>,
            "firstpage": <str>,
            "lastpage": <str>,
            "pub_year": <int>,
            "doi": <str>,
            "pmid": <str>
        },
        ...
    },
    "body_text":[
        {
        "sentence": <str>,
        "secId": <str>,
        "startOffset": <int>,
        "endOffset": <int>,
        "title": <str>,
        "refoffsets": {
            <str>:{
                "endOffset":<int>,
                "startOffset":<int>
                }
            },
        "parents": [
            {
            "id": <str>,
            "title": <str>
            },
            ...
        ]
    },
    ...
    ]
}
```

***docId*** The docID is the identifier of the document. This is unique to the document, and can be resolved into a URL
for the document through the addition of `https//www.sciencedirect.com/science/pii/<docId>`

***abstract*** This is the author provided abstract for the document

***body_text*** The full text for the document. The text has been split on sentence boundaries, thus making it easier to
use across research projects. Each sentence has the title (and ID) of the section which it is from, along with titles (and
IDs) of the parent section. The highest-level section takes index 0 in the parents array. If the array is empty then the
title of the section for the sentence is the highest level section title. This will allow for the reconstruction of the article
structure. References have been extracted from the sentences. The IDs of the extracted reference and their respective
offset within the sentence can be found in the “refoffsets” field. The complete list of references are can be found in
the “bib_entry” field along with the references’ respective metadata. Some will be missing as we only keep ‘clean’
sentences,

***bib_entities*** All the references from within the document can be found in this section. If the meta data for the
reference is available, it has been added against the key for the reference. Where possible information such as the
document titles, authors, and relevant identifiers (DOI and PMID) are included. The keys for each reference can be
found in the sentence where the reference is used with the start and end offset of where in the sentence that reference
was used.

***metadata*** Meta data includes additional information about the article, such as list of authors, relevant IDs (DOI and
PMID). Along with a number of classification schemes such as ASJC and Subject Classification.

***author_highlights*** Author highlights were included in the corpus where the author(s) have provided them. The
coverage is 61% of all articles. The author highlights, consisting of 4 to 6 sentences, is provided by the author with
the aim of summarising the core findings and results in the article.

### Data Fields

* ***title***: This is the author provided title for the document. 100% coverage.
* ***abstract***: This is the author provided abstract for the document. 99.25% coverage.
* ***keywords***: This is the author and publisher provided keywords for the document. 100% coverage.
* ***asjc***: This is the disciplines for the document as represented by 334 ASJC (All Science Journal Classification) codes. 100% coverage.
* ***subjareas***: This is the Subject Classification for the document as represented by 27 ASJC top-level subject classifications. 100% coverage.
* ***body_text***: The full text for the document. 100% coverage.
* ***author_highlights***: This is the author provided highlights for the document. 61.31% coverage.

### Data Splits

***Distribution of Publication Years***

|  | Train | Test | Validation |
| --- | :---: | :---: | :---: |
| All Articles | 32072 | 4009 | 4008 |
| With Author Highlights | 19644 | 2420 | 2514 |

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

Date the data was collected:	2020-06-25T11:00:00.000Z

See the [original paper](https://doi.org/10.48550/arXiv.2008.00774) for more detail on the data collection process.

#### Who are the source language producers?

See `3.1 Data Sampling` in the [original paper](https://doi.org/10.48550/arXiv.2008.00774).

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

### Citation Information

```
@article{Kershaw2020ElsevierOC,
  title     = {Elsevier OA CC-By Corpus},
  author    = {Daniel James Kershaw and R. Koeling},
  journal   = {ArXiv},
  year      = {2020},
  volume    = {abs/2008.00774},
  doi       = {https://doi.org/10.48550/arXiv.2008.00774},
  url       = {https://elsevier.digitalcommonsdata.com/datasets/zm33cdndxs},
  keywords  = {Science, Natural Language Processing, Machine Learning, Open Dataset},
  abstract  = {We introduce the Elsevier OA CC-BY corpus. This is the first open
               corpus of Scientific Research papers which has a representative sample
               from across scientific disciplines. This corpus not only includes the
               full text of the article, but also the metadata of the documents, 
               along with the bibliographic information for each reference.}
}
```

```
@dataset{https://10.17632/zm33cdndxs.3,
  doi       = {10.17632/zm33cdndxs.2},
  url       = {https://data.mendeley.com/datasets/zm33cdndxs/3},
  author    = "Daniel Kershaw and Rob Koeling",
  keywords  = {Science, Natural Language Processing, Machine Learning, Open Dataset},
  title     = {Elsevier OA CC-BY Corpus},
  publisher = {Mendeley},
  year      = {2020},
  month     = {sep}
}
```

### Contributions

Thanks to [@orieg](https://github.com/orieg) for adding this dataset.