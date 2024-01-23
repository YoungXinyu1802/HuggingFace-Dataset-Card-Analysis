---
license: apache-2.0
language:
- en
task_categories:
- summarization
- text2text-generation
tags:
- summarization
- long-document
pretty_name: SQuALITY v1.3
size_categories:
- n<1K
---


# SQuALITY - v1.3

> Original paper [here](https://arxiv.org/abs/2205.11465)

This is v1.3, the 'text' edition `.jsonl` files. See description from the [original repo](https://github.com/nyu-mll/SQuALITY):

> v1.3 fixes some bugs in v1.2. In v1.2, 10 out of 127 articles (each ~5k-word-long) are missing a few hundreds words each, so summaries may not be fully contained in the article. To fix this issue, we have updated the 10 articles.

## contents 

> again, this is taken from the repo

Each data file ({train/dev/test}.jsonl) is formatted as a JSON lines file. Each row in the data file is a JSON dictionary with the following fields:

- metadata: the Gutenberg story ID, an internal UID, and the Project Gutenberg license
- document: the Gutenberg story
questions: a list of questions and accompanying responses
  - question text
  - question number: the order in which that question was answered by the writers
  - responses: list of worker's response, where each response is a dictionary containing the (anonymized) worker ID, an internal UID, and their response to the question
 

### dataset contents


```python
DatasetDict({
    train: Dataset({
        features: ['metadata', 'document', 'questions'],
        num_rows: 50
    })
    test: Dataset({
        features: ['metadata', 'document', 'questions'],
        num_rows: 52
    })
    validation: Dataset({
        features: ['metadata', 'document', 'questions'],
        num_rows: 25
    })
})
```

