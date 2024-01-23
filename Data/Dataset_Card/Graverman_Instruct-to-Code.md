---
license: apache-2.0
language:
- en
tags:
- code
- instuction
size_categories:
- 100K<n<1M
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: original ds
    dtype: string
  - name: id
    dtype: int64
  splits:
  - name: train
    num_bytes: 563327497
    num_examples: 700000
  download_size: 246890997
  dataset_size: 563327497
---
Dataset with different instructions and the code that should be generated after those instructions.
Made for main dataset of Open Assistant.

If you want to contribute, message me on discord (Graverman#0804), here are some types of intructions left to be done:

- Write a python funtion based on these instructions

- What would be a description above on jupyter notebook for this code ✅

- Given description that is above in a jupyter notebook, what could be the code ✅

- Given the docstring, create instructions for the code 

- Given code, create some instructions for that code

- Rewrite the following code ✅

- Explain this snippet of code ✅

- Solve the following problem in python ✅

id is an index in the original dataset that the code was taken from

The dataset will have ~700k examples (in progress)