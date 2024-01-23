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
  - name: multilingual-humaneval_python
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
- mbxp
- multi-humaneval
- mathqax
pretty_name: mxeval
language:
- en
---
# MxEval

## Table of Contents
- [MxEval](#MxEval)
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
    - [Personal and Sensitive Information](#personal-and-sensitive-information)
    - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Executional Correctness](#execution)
    - [Execution Example](#execution-example)
    - [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Repository:** [GitHub Repository](https://github.com/amazon-science/mbxp-exec-eval)
- **Paper:** [Multi-lingual Evaluation of Code Generation Models](https://openreview.net/forum?id=Bo7eeXm6An8)

### Dataset Summary

This repository contains data and code to perform execution-based multi-lingual evaluation of code generation capabilities and the corresponding data,
namely, a multi-lingual benchmark MBXP, multi-lingual MathQA and multi-lingual HumanEval.
<br>Results and findings can be found in the paper ["Multi-lingual Evaluation of Code Generation Models"](https://arxiv.org/abs/2210.14868).


### Supported Tasks and Leaderboards
* [MBXP](https://huggingface.co/datasets/mxeval/mbxp)
* [Multi-HumanEval](https://huggingface.co/datasets/mxeval/multi-humaneval)
* [MathQA-X](https://huggingface.co/datasets/mxeval/mathqa-x)

### Languages
The programming problems are written in multiple programming languages and contain English natural text in comments and docstrings.


## Dataset Structure
To lookup currently supported datasets
```python
get_dataset_config_names("mxeval/mxeval")
['mathqa-x', 'mbxp', 'multi-humaneval']
```
To load a specific dataset and language
```python
from datasets import load_dataset
load_dataset("mxeval/mxeval", "mbxp", split="python")
Dataset({
    features: ['task_id', 'language', 'prompt', 'test', 'entry_point', 'description', 'canonical_solution'],
    num_rows: 974
})
```

### Data Instances

An example of a dataset instance:

```python
{
  "task_id": "MBSCP/6",
  "language": "scala",
  "prompt": "object Main extends App {\n    /**\n     * You are an expert Scala programmer, and here is your task.\n     * * Write a Scala function to check whether the two numbers differ at one bit position only or not.\n     *\n     * >>> differAtOneBitPos(13, 9)\n     * true\n     * >>> differAtOneBitPos(15, 8)\n     * false\n     * >>> differAtOneBitPos(2, 4)\n     * false\n     */\n    def differAtOneBitPos(a : Int, b : Int) : Boolean = {\n",
  "test": "\n\n    var arg00 : Int = 13\n    var arg01 : Int = 9\n    var x0 : Boolean = differAtOneBitPos(arg00, arg01)\n    var v0 : Boolean = true\n    assert(x0 == v0, \"Exception -- test case 0 did not pass. x0 = \" + x0)\n\n    var arg10 : Int = 15\n    var arg11 : Int = 8\n    var x1 : Boolean = differAtOneBitPos(arg10, arg11)\n    var v1 : Boolean = false\n    assert(x1 == v1, \"Exception -- test case 1 did not pass. x1 = \" + x1)\n\n    var arg20 : Int = 2\n    var arg21 : Int = 4\n    var x2 : Boolean = differAtOneBitPos(arg20, arg21)\n    var v2 : Boolean = false\n    assert(x2 == v2, \"Exception -- test case 2 did not pass. x2 = \" + x2)\n\n\n}\n",
  "entry_point": "differAtOneBitPos",
  "description": "Write a Scala function to check whether the two numbers differ at one bit position only or not."
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
   - Java 
   - JavaScript
   - Csharp
   - CPP
   - Go
   - Kotlin
   - PHP
   - Perl
   - Ruby
   - Swift
   - Scala
 - MBXP
   - Python
   - Java
   - JavaScript
   - TypeScript
   - Csharp
   - CPP
   - Go
   - Kotlin
   - PHP
   - Perl
   - Ruby
   - Swift
   - Scala
 - MathQA
   - Python
   - Java
   - JavaScript


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
>>> mbxp_python = load_dataset("mxeval/mxeval", "mbxp", split="python")
>>> example_problem = mbxp_python[0]
>>> check_correctness(example_problem, example_problem["canonical_solution"], timeout=20.0)
{'task_id': 'MBPP/1', 'passed': True, 'result': 'passed', 'completion_id': None, 'time_elapsed': 10.582208633422852}
```
### Considerations for Using the Data
Make sure to sandbox the execution environment since generated code samples can be harmful.


### Licensing Information

[LICENSE](https://huggingface.co/datasets/mxeval/mxeval/blob/main/LICENSE) <br>
[THIRD PARTY LICENSES](https://huggingface.co/datasets/mxeval/mxeval/blob/main/THIRD_PARTY_LICENSES)

# Citation Information
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

# Contributions

[skgouda@](https://github.com/sk-g) [benathi@](https://github.com/benathi)