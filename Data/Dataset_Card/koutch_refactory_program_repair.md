---
dataset_info:
  features:
  - name: submission_id
    dtype: int64
  - name: assignment_id
    dtype: int64
  - name: func_code
    dtype: string
  - name: func_name
    dtype: string
  - name: test
    dtype: string
  - name: description
    dtype: string
  - name: annotation
    dtype: string
  - name: comments
    dtype: string
  - name: __index_level_0__
    dtype: float64
  splits:
  - name: train
    num_bytes: 962
    num_examples: 1
  download_size: 0
  dataset_size: 962
---
# Dataset Card for "refactory_program_repair"

## Dataset Description

- **Paper: coming soon** 

### Dataset Summary

The "refactory_program_repair" dataset is a subset of the [refactory_programming_data](https://huggingface.co/datasets/koutch/refactory_programming_data) 
augmented with educators' annotations on the corrections to the buggy programs and comments on the reason for the solution not working.

### Supported Tasks and Leaderboards

This dataset can be used for the task of program repair. In [Computing Education Research (CER)](https://faculty.washington.edu/ajko/cer/), 
methods for automatically repairing student programs are used to provide students with feedback and help them debug their code. 

### Languages

The assignments were written in Python - English 

## Dataset Structure

### Data Fields

* submission_id: a unique number identifying the submission
* func_code: the cleaned code submitted
* func_name: the name of the function that had to be implemented
* assingment_id: the unique (string) identifier of the assignment that had to be completed
* description: the assignment description
* test: a humaneval style string which can be used to execute the submitted solution on the provided test cases
* annotation: the annotators correction to buggy program
* comments: annotators' short comment on why the type of bug in the solution


## Dataset Creation

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

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

### Citation Information

[Coming soon]