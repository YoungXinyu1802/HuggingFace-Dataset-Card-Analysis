---
dataset_info:
  features:
  - name: task_id
    dtype: string
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: test
    dtype: string
  - name: entry_point
    dtype: string
  splits:
  - name: multi-humaneval_python
    num_bytes: 165716
    num_examples: 164
  download_size: 67983
  dataset_size: 165716
license: apache-2.0
task_categories:
- text-generation
tags:
- mxeval
- code-generation
- multi-humaneval
- humaneval
pretty_name: multi-humaneval
language:
- en
---
# Multi-HumanEval

## Table of Contents
- [multi-humaneval](#multi-humaneval)
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

# multi-humaneval

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
get_dataset_config_names("mxeval/multi-humaneval")
['python', 'csharp', 'go', 'java', 'javascript', 'kotlin', 'perl', 'php', 'ruby', 'scala', 'swift', 'typescript']

```
To load a specific dataset and language
```python
from datasets import load_dataset
load_dataset("mxeval/multi-humaneval", "python")
DatasetDict({
    test: Dataset({
        features: ['task_id', 'language', 'prompt', 'test', 'entry_point', 'canonical_solution', 'description'],
        num_rows: 164
    })
})
```

### Data Instances

An example of a dataset instance:

```python
{
  "task_id": "HumanEval/0",
  "language": "python",
  "prompt": "from typing import List\n\n\ndef has_close_elements(numbers: List[float], threshold: float) -> bool:\n    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than\n    given threshold.\n    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)\n    False\n    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)\n    True\n    \"\"\"\n",
  "test": "\n\nMETADATA = {\n    \"author\": \"jt\",\n    \"dataset\": \"test\"\n}\n\n\ndef check(candidate):\n    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True\n    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False\n    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True\n    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False\n    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True\n    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True\n    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False\n\n",
  "entry_point": "has_close_elements",
  "canonical_solution": "    for idx, elem in enumerate(numbers):\n        for idx2, elem2 in enumerate(numbers):\n            if idx != idx2:\n                distance = abs(elem - elem2)\n                if distance < threshold:\n                    return True\n\n    return False\n",
  "description": "Check if in given list of numbers, are any two numbers closer to each other than\n    given threshold.\n    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)\n    False\n    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)\n    True"
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

 - HumanXEval
   - Python
   - Csharp
   - Go
   - Java
   - Javascript
   - Kotlin
   - Perl
   - Php
   - Ruby
   - Scala
   - Swift
   - Typescript

## Dataset Creation

### Curation Rationale

Since code generation models are often trained on dumps of GitHub a dataset not included in the dump was necessary to properly evaluate the model. However, since this dataset was published on GitHub it is likely to be included in future dumps.

### Personal and Sensitive Information

None.

### Social Impact of Dataset
With this dataset code generating models can be better evaluated which leads to fewer issues introduced when using such models.

## Execution

### Execution Example
Install the repo [mbxp-exec-eval](https://github.com/amazon-science/mbxp-exec-eval) to execute generations or canonical solutions for the prompts from this dataset.

```python
>>> from datasets import load_dataset
>>> from mxeval.execution import check_correctness
>>> humaneval_python = load_dataset("mxeval/multi-humaneval", "python", split="test")
>>> example_problem = humaneval_python[0]
>>> check_correctness(example_problem, example_problem["canonical_solution"], timeout=20.0)
{'task_id': 'HumanEval/0', 'passed': True, 'result': 'passed', 'completion_id': None, 'time_elapsed': 9.636878967285156}
```

### Considerations for Using the Data
Make sure to sandbox the execution environment.

### Dataset Curators
AWS AI Labs

### Licensing Information

[LICENSE](https://huggingface.co/datasets/mxeval/multi-humaneval/blob/main/multi-humaneval-LICENSE) <br>
[THIRD PARTY LICENSES](https://huggingface.co/datasets/mxeval/multi-humaneval/blob/main/THIRD_PARTY_LICENSES)

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