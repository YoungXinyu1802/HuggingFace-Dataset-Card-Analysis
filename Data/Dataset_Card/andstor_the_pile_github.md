---
annotations_creators:
- no-annotation
language:
- en
language_creators:
- found
license:
- other
multilinguality:
- monolingual
pretty_name: The Pile GitHub
size_categories: []
source_datasets:
- original
tags: []
task_categories:
- text-generation
- fill-mask
- text-classification
task_ids: []
---

# Dataset Card for The Pile GitHub

## Table of Contents
- [Dataset Card for Smart Contracts](#dataset-card-for-the-pile-github)
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
  - [Additional Information](#additional-information)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [ElutherAI](https://pile.eleuther.ai)
- **Repository:** [GitHub](https://github.com/andstor/the-pile-github)
- **Paper:** [arXiv](https://arxiv.org/abs/2101.00027)
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

This is the GitHub subset of EleutherAi/The Pile dataset and contains GitHub repositories. The programming languages are identified using the [guesslang library](https://github.com/yoeo/guesslang). A total of 54 programming languages are included in the dataset.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages
The following languages are covered by the dataset:
```
'Assembly', 'Batchfile', 'C', 'C#', 'C++', 'CMake', 'COBOL', 'CSS', 'CSV', 'Clojure', 'CoffeeScript', 'DM', 'Dart', 'Dockerfile', 'Elixir', 'Erlang', 'Fortran', 'Go', 'Groovy', 'HTML', 'Haskell', 'INI', 'JSON', 'Java', 'JavaScript', 'Julia', 'Kotlin', 'Lisp', 'Lua', 'Makefile', 'Markdown', 'Matlab', 'None', 'OCaml', 'Objective-C', 'PHP', 'Pascal', 'Perl', 'PowerShell', 'Prolog', 'Python', 'R', 'Ruby', 'Rust', 'SQL', 'Scala', 'Shell', 'Swift', 'TOML', 'TeX', 'TypeScript', 'Verilog', 'Visual Basic', 'XML', 'YAML'
```

The [guesslang library](https://github.com/yoeo/guesslang) is used to identify the programming languages. It has a guessing accuracy of above 90%. Hence, there will be some misclassifications in the language identification.

## Dataset Structure

### Data Instances

[More Information Needed]

```
{
  'text': ...,
  'meta': {'language': ...}
}
```

### Data Fields

- `text` (`string`): the source code.
- `meta` (`dict`): the metadata of the source code.
  - `language` (`string`): the programming language of the source code.

### Data Splits

[More Information Needed]

|                         | train | validation | test |
|-------------------------|------:|-----------:|-----:|
| Input Sentences         |       |            |      |
| Average Sentence Length |       |            |      |

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

The data is purely a subset of the [EleutherAI/The Pile dataset](https://huggingface.co/datasets/the_pile). See the original [dataset](https://arxiv.org/abs/2201.07311) for more details.

## Additional Information

### Licensing Information

The Pile dataset was released on January 1st, 2021. It is licensed under the MIT License. See the [dataset](https://arxiv.org/abs/2201.07311) for more details.

### Citation Information

Provide the [BibTex](http://www.bibtex.org/)-formatted reference for the dataset. For example:
```
@article{pile,
    title={The {P}ile: An 800GB Dataset of Diverse Text for Language Modeling},
    author={Gao, Leo and Biderman, Stella and Black, Sid and Golding, Laurence and Hoppe, Travis and Foster, Charles and Phang, Jason and He, Horace and Thite, Anish and Nabeshima, Noa and Presser, Shawn and Leahy, Connor},
    journal={arXiv preprint arXiv:2101.00027},
    year={2020}
}
```

### Contributions

Thanks to [@andstor](https://github.com/andstor) for adding this dataset.