---
dataset_info:
  features:
  - name: submission_id
    dtype: int64
  - name: func_code
    dtype: string
  - name: correct
    dtype: bool
  - name: assignment_id
    dtype: int64
  - name: func_name
    dtype: string
  - name: test
    dtype: string
  - name: description
    dtype: string
  splits:
  - name: train
    num_bytes: 5129686
    num_examples: 4394
  download_size: 269066
  dataset_size: 5129686
license: lgpl
language:
- en
size_categories:
- 1K<n<10K
---
# Dataset Card for "refactory_programming_data"

---
license: lgpl-3.0
size_categories:
- 1K<n<10K
---

# Dataset Card for Refactory Programming Data

## Dataset Description

- **Repository:** [GitHub](https://github.com/githubhuyang/refactory)
- **Paper:** [Re-Factoring Based Program Repair Applied to Programming Assignments](https://ieeexplore.ieee.org/abstract/document/8952522)

### Dataset Summary

The data.zip archive contains 2442 correct and 1783 buggy program attempts by 361 undergraduate students crediting an introduction to Python programming course 
at NUS (National University of Singapore). 

### Tasks

This dataset can be used for the task of repairing student buggy programs.

### Languages

The programs were written in the Python programming language. 

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

* func_code: the cleaned code submitted by the student
* correct: whether the program successfully passed all tests
* question: unique id of the question/assignment to be solved
* func_name: the name of the function to implement
* test: a humaneval-style string which can be used to execute the submitted solution on the provided test cases
* description: the assignment description (i.e. the problem that the students had to solve)

## Dataset Creation

Details about the dataset curation can be found in the release paper. 

## Additional Information

### Licensing Information

The data was released under a [GNU Lesser General Public License v3.0](https://github.com/githubhuyang/refactory/blob/master/LICENSE) license

### Citation Information

All credits must be attributed to the original authors and contributors of the dataset

```
@inproceedings{yang2019refactory,
    title={Re-factoring based Program Repair applied to Programming Assignments},
    author={Hu, Yang and Ahmed, Umair Z. and Mechtaev, Sergey and Leong, Ben and Roychoudhury, Abhik},
    booktitle={2019 34th IEEE/ACM International Conference on Automated Software Engineering (ASE)},
    pages={388--398},
    year={2019},
    organization={IEEE/ACM}
}
```