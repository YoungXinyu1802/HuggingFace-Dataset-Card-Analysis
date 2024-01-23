---
annotations_creators:
- machine-generated
language_creators:
- crowdsourced
language:
- '''en-US'''
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: Webis args.me argument corpus
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- text-retrieval
task_ids:
- document-retrieval
---
# Dataset Card for the args.me corpus

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Dataset Usage](#dataset-usage)
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

- **Homepage:** https://zenodo.org/record/4139439
- **Repository:** https://git.webis.de/code-research/arguana/args/args-framework
- **Paper:** [Building an Argument Search Engine for the Web](https://webis.de/downloads/publications/papers/wachsmuth_2017f.pdf)
- **Leaderboard:** https://touche.webis.de/
- **Point of Contact:** [Webis Group](https://webis.de/people.html)

### Dataset Summary

The args.me corpus (version 1.0, cleaned) comprises 382 545 arguments crawled from four debate portals in the middle of 2019. The debate portals are Debatewise, IDebate.org, Debatepedia, and Debate.org. The arguments are extracted using heuristics that are designed for each debate portal.

### Dataset Usage

```python
import datasets
args = datasets.load_dataset('cakiki/args_me', 'corpus', streaming=True)
args_iterator = iter(args)
for arg in args_iterator:
    print(args['conclusion'])
    print(args['id'])
    print(args['argument'])
    print(args['stance'])
    break
```

### Supported Tasks and Leaderboards

Document Retrieval, Argument Retrieval for Controversial Questions

### Languages

The args.me corpus is monolingual; it only includes English (mostly en-US) documents.

## Dataset Structure

### Data Instances

#### Corpus
```
{'conclusion': 'Science is the best!',
 'id': 'd6517702-2019-04-18T12:36:24Z-00000-000',
 'argument': 'Science is aright I guess, but Physical Education (P.E) is better. Think about it, you could sit in a classroom for and hour learning about molecular reconfiguration, or you could play football with your mates. Why would you want to learn about molecular reconfiguration anyway? I think the argument here would be based on, healthy mind or healthy body. With science being the healthy mind and P.E being the healthy body. To work this one out all you got to do is ask Steven Hawkins. Only 500 words',
 'stance': 'CON'}
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

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

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
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

### Citation Information

```
@dataset{yamen_ajjour_2020_4139439,
  author       = {Yamen Ajjour and
                  Henning Wachsmuth and
                  Johannes Kiesel and
                  Martin Potthast and
                  Matthias Hagen and
                  Benno Stein},
  title        = {args.me corpus},
  month        = oct,
  year         = 2020,
  publisher    = {Zenodo},
  version      = {1.0-cleaned},
  doi          = {10.5281/zenodo.4139439},
  url          = {https://doi.org/10.5281/zenodo.4139439}
}
```
