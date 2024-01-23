---
annotations_creators:
- machine-generated
language_creators:
- found
language:
- de
license:
- unknown
multilinguality:
- monolingual
size_categories:
- n>1M
source_datasets:
- original
task_categories:
- text-retrieval
- text-scoring
task_ids:
- semantic-similarity-scoring
- text-retrieval-other-example-based-retrieval
---

# Dataset Card for German Legal Sentences

## Table of Contents
- [Dataset Card for [Dataset Name]](#dataset-card-for-dataset-name)
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

- **Homepage:** https://lavis-nlp.github.io/german_legal_sentences/
- **Repository:** https://github.com/lavis-nlp/german_legal_sentences
- **Paper:** coming soon
- **Leaderboard:**
- **Point of Contact:** [Marco Wrzalik](mailto:marco.wrzalik@hs-rm.de)

### Dataset Summary

German Legal Sentences (GLS) is an automatically generated training dataset for semantic sentence matching and citation recommendation in the domain in german legal documents. It follows the concept of weak supervision, where imperfect labels are generated using multiple heuristics. For this purpose we use a combination of legal citation matching and BM25 similarity. The contained sentences and their citations are parsed from real judicial decisions provided by [Open Legal Data](http://openlegaldata.io/) (https://arxiv.org/abs/2005.13342).

### Supported Tasks and Leaderboards

The main associated task is *Semantic Similarity Ranking*. We propose to use the *Mean Reciprocal Rank* (MRR) cut at the tenth position as well as MAP and Recall on Rankings of size 200. As baselines we provide the follows: 

| Method                            | MRR@10   | MAP@200    | Recall@200  |
|-----------------------------------|---------:|-----------:|------------:|
| BM25 - default `(k1=1.2; b=0.75)` |     25.7 |       17.6 |        42.9 |
| BM25 - tuned `(k1=0.47; b=0.97)`  |     26.2 |       18.1 |        43.3 |
| [CoRT](https://arxiv.org/abs/2010.10252)             |     31.2 |       21.4 |        56.2 |
| [CoRT + BM25](https://arxiv.org/abs/2010.10252)      |     32.1 |       22.1 |        67.1 |

In addition, we want to support a *Citation Recommendation* task in the future.

If you wish to contribute evaluation measures or give any suggestion or critique, please write an [e-mail](mailto:marco.wrzalik@hs-rm.de).

### Languages

This dataset contains texts from the specific domain of German court decisions.

## Dataset Structure

### Data Instances

```
{'query.doc_id': 28860,
 'query.ref_ids': [6215, 248, 248],
 'query.sent_id': 304863,
 'query.text': 'Zudem ist zu berücksichtigen , dass die Vollverzinsung nach '
               '[REF] i. V. m. [REF] gleichermaßen zugunsten wie zulasten des '
               'Steuerpflichtigen wirkt , sodass bei einer Überzahlung durch '
               'den Steuerpflichtigen der Staat dem Steuerpflichtigen neben '
               'der Erstattung ebenfalls den entstandenen potentiellen Zins- '
               'und Liquiditätsnachteil in der pauschalierten Höhe des [REF] '
               'zu ersetzen hat , unabhängig davon , in welcher Höhe dem '
               'Berechtigten tatsächlich Zinsen entgangen sind .',
 'related.doc_id': 56348,
 'related.ref_ids': [248, 6215, 62375],
 'related.sent_id': 558646,
 'related.text': 'Ferner ist zu berücksichtigen , dass der Zinssatz des [REF] '
                 'im Rahmen des [REF] sowohl für Steuernachforderung wie auch '
                 'für Steuererstattungen und damit gleichermaßen zugunsten wie '
                 'zulasten des Steuerpflichtigen wirkt , Vgl. BVerfG , '
                 'Nichtannahmebeschluss vom [DATE] [REF] , juris , mit der '
                 'Folge , dass auch Erstattungsansprüche unabhängig davon , ob '
                 'und in welcher Höhe dem Berechtigten tatsächlich Zinsen '
                 'entgangen sind , mit monatlich 0,0 % verzinst werden .'}
```

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

The documents we take from [Open Legal Data](http://openlegaldata.io/) (https://arxiv.org/abs/2005.13342) are first preprocessed by removing line breaks, enumeration characters and headings. Afterwards we parse legal citations using hand-crafted regular expressions. Each citation is split into it components and normalized, thus different variants of the same citation are matched together. For instance, "§211 Absatz 1 des Strafgesetzbuches" is normalized to "§ 211 Abs. 1 StGB". Every time we discover an unknown citation, we assign an unique id to it. We use these ids to replace parsed citations in the document text with a simple reference tag containing this id (e.g `[REF321]`). At the same time we parse dates and replace them with the date tag `[DATE]`. Both remove dots which can may be confused with the end of a sentence, which makes the next stage easier.

We use [SoMaJo](https://github.com/tsproisl/SoMaJo) to perform sentence tokenizing on the pre-processed documents. Each sentence that does not contain at least one legal citation is discarded. For the rest we assign sentence ids, remove all reference ids from them as well as any contents in braces (braces often contain large enumerations of citations and their sources). At the same time we keep track of the corresponding document from which a sentence originates and which references occur in it. 

#### Who are the source language producers?

The source language originates in the context of German court proceedings.

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

The annotations are machine-generated.

### Personal and Sensitive Information

The source documents are already public and anonymized.

## Considerations for Using the Data

### Social Impact of Dataset

With this dataset, we strive towards better accessibility of court decisions to the general public by accelerating research on semantic search technologies. We hope that emerging search technologies will enable the layperson to find relevant information without knowing the specific terms used by lawyers.

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

Coming soon!

### Contributions

Thanks to [@mwrzalik](https://github.com/mwrzalik) for adding this dataset.