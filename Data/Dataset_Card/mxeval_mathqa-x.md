---
license: apache-2.0
task_categories:
- text-generation
language:
- en
tags:
- mathqa-x
- mathqa
- mxeval
pretty_name: mbxp
size_categories:
- 1K<n<10K
---
# MBXP

## Table of Contents
- [MathQA-X](#MathQA-X)
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

# MathQA-X

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
get_dataset_config_names("mxeval/mathqa-x")
['python', 'java', 'javascript']
```
To load a specific dataset and language
```python
from datasets import load_dataset
load_dataset("mxeval/mathqa-x", "python")
DatasetDict({
    test: Dataset({
        features: ['task_id', 'language', 'prompt', 'test', 'entry_point', 'canonical_solution'],
        num_rows: 1883
    })
})
```

### Data Instances

An example of a dataset instance:

```python
{
  "task_id": "MathQA/0",
  "language": "python",
  "prompt": "def problem():\n    \"\"\"\n    a shopkeeper sold an article offering a discount of 5 % and earned a profit of 31.1 % . what would have been the percentage of profit earned if no discount had been offered ? n0 = 5.0 n1 = 31.1\n    \"\"\"\n",
  "test": "import math\ndef compare(x, y):\n    return math.fabs(x-y)<1e-8\ncandidate = problem\nassert compare(candidate(), 38.0)\ndef check(x): pass\n",
  "entry_point": "problem",
  "canonical_solution": "    n0 = 5.0\n    n1 = 31.1\n    t0 = n1 + 100.0\n    t1 = 100.0 - n0\n    t2 = t0 * 100.0\n    t3 = t2 / t1\n    answer = t3 - 100.0\n    return answer\n"
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

 - MathQA-X
   - Python
   - Java
   - Javascript

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
>>> mathqa_python = load_dataset("mxeval/mathqa-x", "python", split="test")
>>> example_problem = mathqa_python[0]
>>> check_correctness(example_problem, example_problem["canonical_solution"], timeout=20.0)
{'task_id': 'MathQA/0', 'passed': True, 'result': 'passed', 'completion_id': None, 'time_elapsed': 9.673357009887695}
```

### Considerations for Using the Data
Make sure to sandbox the execution environment.

### Dataset Curators
AWS AI Labs

### Licensing Information

[LICENSE](https://huggingface.co/datasets/mxeval/mathqa-x/blob/main/mathqa-x-LICENSE) <br>
[THIRD PARTY LICENSES](https://huggingface.co/datasets/mxeval/mathqa-x/blob/main/THIRD_PARTY_LICENSES)

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