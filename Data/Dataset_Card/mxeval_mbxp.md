---
license: apache-2.0
task_categories:
- text-generation
language:
- en
tags:
- mxeval
- mbxp
- mbpp
- code-generation
- mxeval
pretty_name: mbxp
size_categories:
- 10K<n<100K
---
# MBXP

## Table of Contents
- [MBXP](#MBXP)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#related-tasks-and-leaderboards)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Executional Correctness](#execution)
    - [Execution Example](#execution-example)
    - [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Personal and Sensitive Information](#personal-and-sensitive-information)
    - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

# MBXP

## Dataset Description

- **Repository:** [GitHub Repository](https://github.com/amazon-science/mbxp-exec-eval)
- **Paper:** [Multi-lingual Evaluation of Code Generation Models](https://openreview.net/forum?id=Bo7eeXm6An8)

### Dataset Summary

This repository contains data and code to perform execution-based multi-lingual evaluation of code generation capabilities and the corresponding data,
namely, a multi-lingual benchmark MBXP, multi-lingual MathQA and multi-lingual HumanEval.
<br>Results and findings can be found in the paper ["Multi-lingual Evaluation of Code Generation Models"](https://arxiv.org/abs/2210.14868).


### Related Tasks and Leaderboards
* [Multi-HumanEval](https://huggingface.co/datasets/mxeval/multi-humaneval)
* [MBXP](https://huggingface.co/datasets/mxeval/mbxp)
* [MathQA-X](https://huggingface.co/datasets/mxeval/mathqa-x)

### Languages
The programming problems are written in multiple programming languages and contain English natural text in comments and docstrings.


## Dataset Structure
To lookup currently supported datasets
```python
from datasets import get_dataset_config_names
get_dataset_config_names("mxeval/mbxp")
['python', 'csharp', 'go', 'java', 'javascript', 'kotlin', 'perl', 'php', 'ruby', 'scala', 'swift', 'typescript']
```
To load a specific dataset and language
```python
from datasets import load_dataset
load_dataset("mxeval/mbxp", "python")
DatasetDict({
    test: Dataset({
        features: ['task_id', 'language', 'prompt', 'test', 'entry_point', 'canonical_solution', 'description'],
        num_rows: 974
    })
})
```

### Data Instances

An example of a dataset instance:

```python
{
  "task_id": "MBPP/1",
  "language": "python",
  "prompt": "\n\ndef min_cost(cost, m, n):\n\t\"\"\"\n\tWrite a function to find the minimum cost path to reach (m, n) from (0, 0) for the given cost matrix cost[][] and a position (m, n) in cost[][].\n\t>>> min_cost([[1, 2, 3], [4, 8, 2], [1, 5, 3]], 2, 2)\n\t8\n\t>>> min_cost([[2, 3, 4], [5, 9, 3], [2, 6, 4]], 2, 2)\n\t12\n\t>>> min_cost([[3, 4, 5], [6, 10, 4], [3, 7, 5]], 2, 2)\n\t16\n\t\"\"\"\n",
  "test": "\n\nMETADATA = {}\n\n\ndef check(candidate):\n    assert candidate([[1, 2, 3], [4, 8, 2], [1, 5, 3]], 2, 2) == 8\n    assert candidate([[2, 3, 4], [5, 9, 3], [2, 6, 4]], 2, 2) == 12\n    assert candidate([[3, 4, 5], [6, 10, 4], [3, 7, 5]], 2, 2) == 16\n\n",
  "entry_point": "min_cost",
  "canonical_solution": "\tR = 3\n\tC = 3\n\t \n\ttc = [[0 for x in range(C)] for x in range(R)] \n\ttc[0][0] = cost[0][0] \n\tfor i in range(1, m+1): \n\t\ttc[i][0] = tc[i-1][0] + cost[i][0] \n\tfor j in range(1, n+1): \n\t\ttc[0][j] = tc[0][j-1] + cost[0][j] \n\tfor i in range(1, m+1): \n\t\tfor j in range(1, n+1): \n\t\t\ttc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j] \n\treturn tc[m][n]",
  "description": "Write a function to find the minimum cost path to reach (m, n) from (0, 0) for the given cost matrix cost[][] and a position (m, n) in cost[][]."
}
```

### Data Fields

- `task_id`: identifier for the data sample
- `prompt`: input for the model containing function header and docstrings
- `canonical_solution`: solution for the problem in the `prompt`
- `description`: task description
- `test`: contains function to test generated code for correctness
- `entry_point`: entry point for test
- `language`: programming lanuage identifier to call the appropriate subprocess call for program execution


### Data Splits

 - MBXP
   - Python
   - Java
   - Javascript
   - Typescript
   - Kotlin
   - Ruby
   - Php
   - Cpp
   - Csharp
   - Go
   - Perl
   - Scala
   - Swift

## Dataset Creation

### Curation Rationale

Since code generation models are often trained on dumps of GitHub a dataset not included in the dump was necessary to properly evaluate the model. However, since this dataset was published on GitHub it is likely to be included in future dumps.

### Personal and Sensitive Information

None.

### Social Impact of Dataset
With this dataset code generating models can be better evaluated which leads to fewer issues introduced when using such models.

### Dataset Curators
AWS AI Labs

## Execution

### Execution Example
Install the repo [mbxp-exec-eval](https://github.com/amazon-science/mbxp-exec-eval) to execute generations or canonical solutions for the prompts from this dataset.

```python
>>> from datasets import load_dataset
>>> from mxeval.execution import check_correctness
>>> mbxp_python = load_dataset("mxeval/mbxp", "python", split="test")
>>> example_problem = mbxp_python[0]
>>> check_correctness(example_problem, example_problem["canonical_solution"], timeout=20.0)
{'task_id': 'MBPP/1', 'passed': True, 'result': 'passed', 'completion_id': None, 'time_elapsed': 10.314226150512695}
```

### Considerations for Using the Data
Make sure to sandbox the execution environment.

### Licensing Information

[LICENSE](https://huggingface.co/datasets/mxeval/mbxp/blob/main/mbxp-LICENSE) <br>
[THIRD PARTY LICENSES](https://huggingface.co/datasets/mxeval/mbxp/blob/main/THIRD_PARTY_LICENSES)

### Citation Information
```
@inproceedings{
athiwaratkun2023multilingual,
title={Multi-lingual Evaluation of Code Generation Models},
author={Ben Athiwaratkun and Sanjay Krishna Gouda and Zijian Wang and Xiaopeng Li and Yuchen Tian and Ming Tan and Wasi Uddin Ahmad and Shiqi Wang and Qing Sun and Mingyue Shang and Sujan Kumar Gonugondla and Hantian Ding and Varun Kumar and Nathan Fulton and Arash Farahani and Siddhartha Jain and Robert Giaquinto and Haifeng Qian and Murali Krishna Ramanathan and Ramesh Nallapati and Baishakhi Ray and Parminder Bhatia and Sudipta Sengupta and Dan Roth and Bing Xiang},
booktitle={The Eleventh International Conference on Learning Representations },
year={2023},
url={https://openreview.net/forum?id=Bo7eeXm6An8}
}
```

### Contributions

[skgouda@](https://github.com/sk-g) [benathi@](https://github.com/benathi)