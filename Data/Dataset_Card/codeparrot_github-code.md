---
annotations_creators: []
language_creators:
- crowdsourced
- expert-generated
language:
- code
license:
- other
multilinguality:
- multilingual
pretty_name: github-code
size_categories:
- unknown
source_datasets: []
task_categories:
- text-generation
task_ids:
- language-modeling
---

# GitHub Code Dataset

## Dataset Description
The GitHub Code dataset consists of 115M code files from GitHub in 32 programming languages with 60 extensions totaling in 1TB of data. The dataset was created from the public GitHub dataset on Google BiqQuery.

### How to use it

The GitHub Code dataset is a very large dataset so for most use cases it is recommended to make use of the streaming API of `datasets`. You can load and iterate through the dataset with the following two lines of code:

```python
from datasets import load_dataset

ds = load_dataset("codeparrot/github-code", streaming=True, split="train")
print(next(iter(ds)))

#OUTPUT:
{
 'code': "import mod189 from './mod189';\nvar value=mod189+1;\nexport default value;\n",
 'repo_name': 'MirekSz/webpack-es6-ts',
 'path': 'app/mods/mod190.js',
 'language': 'JavaScript',
 'license': 'isc',
 'size': 73
}
```

You can see that besides the code, repo name, and path also the programming language, license, and the size of the file are part of the dataset. You can also filter the dataset for any subset of the 30 included languages (see the full list below) in the dataset. Just pass the list of languages as a list. E.g. if your dream is to build a Codex model for Dockerfiles use the following configuration:

```python
ds = load_dataset("codeparrot/github-code", streaming=True, split="train", languages=["Dockerfile"])
print(next(iter(ds))["code"])

#OUTPUT:
"""\
FROM rockyluke/ubuntu:precise

ENV DEBIAN_FRONTEND="noninteractive" \
    TZ="Europe/Amsterdam"
...
"""
```

We also have access to the license of the origin repo of a file so we can filter for licenses in the same way we filtered for languages:
 
```python
ds = load_dataset("codeparrot/github-code", streaming=True, split="train", licenses=["mit", "isc"])

licenses = []
for element in iter(ds).take(10_000):
    licenses.append(element["license"])
print(Counter(licenses))

#OUTPUT:
Counter({'mit': 9896, 'isc': 104})
```

Naturally, you can also download the full dataset. Note that this will download ~300GB compressed text data and the uncompressed dataset will take up ~1TB of storage:
```python
ds = load_dataset("codeparrot/github-code", split="train")
```

## Data Structure

### Data Instances

```python
{
 'code': "import mod189 from './mod189';\nvar value=mod189+1;\nexport default value;\n",
 'repo_name': 'MirekSz/webpack-es6-ts',
 'path': 'app/mods/mod190.js',
 'language': 'JavaScript',
 'license': 'isc',
 'size': 73
}
```

### Data Fields

|Field|Type|Description|
|---|---|---|
|code|string|content of source file|
|repo_name|string|name of the GitHub repository|
|path|string|path of file in GitHub repository|
|language|string|programming language as inferred by extension|
|license|string|license of GitHub repository|
|size|int|size of source file in bytes|

### Data Splits

The dataset only contains a train split.

## Languages

The dataset contains 30 programming languages with over 60 extensions:

```python
{
    "Assembly": [".asm"],
    "Batchfile": [".bat", ".cmd"],
    "C": [".c", ".h"],
    "C#": [".cs"],
    "C++": [".cpp", ".hpp", ".c++", ".h++", ".cc", ".hh", ".C", ".H"],
    "CMake": [".cmake"],
    "CSS": [".css"],
    "Dockerfile": [".dockerfile", "Dockerfile"],
    "FORTRAN": ['.f90', '.f', '.f03', '.f08', '.f77', '.f95', '.for', '.fpp'],
    "GO": [".go"],
    "Haskell": [".hs"],
    "HTML":[".html"],
    "Java": [".java"],
    "JavaScript": [".js"],
    "Julia": [".jl"],
    "Lua": [".lua"],
    "Makefile": ["Makefile"],
    "Markdown": [".md", ".markdown"],
    "PHP": [".php", ".php3", ".php4", ".php5", ".phps", ".phpt"],
    "Perl": [".pl", ".pm", ".pod", ".perl"],
    "PowerShell": ['.ps1', '.psd1', '.psm1'],
    "Python": [".py"],
    "Ruby": [".rb"],
    "Rust": [".rs"],
    "SQL": [".sql"],
    "Scala": [".scala"],
    "Shell": [".sh", ".bash", ".command", ".zsh"],
    "TypeScript": [".ts", ".tsx"],
    "TeX": [".tex"],
    "Visual Basic": [".vb"]
}
```

## Licenses
Each example is also annotated with the license of the associated repository. There are in total 15 licenses:
```python
[
  'mit',
  'apache-2.0',
  'gpl-3.0',
  'gpl-2.0',
  'bsd-3-clause',
  'agpl-3.0',
  'lgpl-3.0',
  'lgpl-2.1',
  'bsd-2-clause',
  'cc0-1.0',
  'epl-1.0',
  'mpl-2.0',
  'unlicense',
  'isc',
  'artistic-2.0'
 ]
```

## Dataset Statistics

The dataset contains 115M files and the sum of all the source code file sizes is 873 GB (note that the size of the dataset is larger due to the extra fields). A breakdown per language is given in the plot and table below:

![dataset-statistics](https://huggingface.co/datasets/codeparrot/github-code/resolve/main/github-code-stats-alpha.png)

|    | Language     |File Count| Size (GB)|
|---:|:-------------|---------:|-------:|
|  0 | Java         | 19548190 | 107.70 |
|  1 | C            | 14143113 | 183.83 |
|  2 | JavaScript   | 11839883 |  87.82 |
|  3 | HTML         | 11178557 | 118.12 |
|  4 | PHP          | 11177610 |  61.41 |
|  5 | Markdown     |  8464626 |  23.09 |
|  6 | C++          |  7380520 |  87.73 |
|  7 | Python       |  7226626 |  52.03 |
|  8 | C#           |  6811652 |  36.83 |
|  9 | Ruby         |  4473331 |  10.95 |
| 10 | GO           |  2265436 |  19.28 |
| 11 | TypeScript   |  1940406 |  24.59 |
| 12 | CSS          |  1734406 |  22.67 |
| 13 | Shell        |  1385648 |   3.01 |
| 14 | Scala        |   835755 |   3.87 |
| 15 | Makefile     |   679430 |   2.92 |
| 16 | SQL          |   656671 |   5.67 |
| 17 | Lua          |   578554 |   2.81 |
| 18 | Perl         |   497949 |   4.70 |
| 19 | Dockerfile   |   366505 |   0.71 |
| 20 | Haskell      |   340623 |   1.85 |
| 21 | Rust         |   322431 |   2.68 |
| 22 | TeX          |   251015 |   2.15 |
| 23 | Batchfile    |   236945 |   0.70 |
| 24 | CMake        |   175282 |   0.54 |
| 25 | Visual Basic |   155652 |   1.91 |
| 26 | FORTRAN      |   142038 |   1.62 |
| 27 | PowerShell   |   136846 |   0.69 |
| 28 | Assembly     |    82905 |   0.78 |
| 29 | Julia        |    58317 |   0.29 |


## Dataset Creation

The dataset was created in two steps:
1. Files of with the extensions given in the list above were retrieved from the GitHub dataset on BigQuery (full query [here](https://huggingface.co/datasets/codeparrot/github-code/blob/main/query.sql)). The query was executed on _Mar 16, 2022, 6:23:39 PM UTC+1_.
2. Files with lines longer than 1000 characters and duplicates (exact duplicates ignoring whitespaces) were dropped (full preprocessing script [here](https://huggingface.co/datasets/codeparrot/github-code/blob/main/github_preprocessing.py)).

## Considerations for Using the Data

The dataset consists of source code from a wide range of repositories. As such they can potentially include harmful or biased code as well as sensitive information like passwords or usernames.

## Releases

You can load any older version of the dataset with the `revision` argument:

```Python
ds = load_dataset("codeparrot/github-code", revision="v1.0")
```

### v1.0
- Initial release of dataset
- The query was executed on _Feb 14, 2022, 12:03:16 PM UTC+1_

### v1.1
- Fix missing Scala/TypeScript
- Fix deduplication issue with inconsistent Python `hash`
- The query was executed on _Mar 16, 2022, 6:23:39 PM UTC+1_
