---
dataset_info:
  features:
  - name: id
    dtype: uint32
  - name: language
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text_markdown
    dtype: string
  - name: text_html
    dtype: string
  - name: author
    dtype: string
  - name: original_author
    dtype: string
  - name: original_url
    dtype: string
  - name: lead_html
    dtype: string
  - name: lead_markdown
    dtype: string
  - name: type
    dtype: string
  - name: time_published
    dtype: uint64
  - name: statistics
    struct:
    - name: commentsCount
      dtype: uint32
    - name: favoritesCount
      dtype: uint32
    - name: readingCount
      dtype: uint32
    - name: score
      dtype: int32
    - name: votesCount
      dtype: int32
    - name: votesCountPlus
      dtype: int32
    - name: votesCountMinus
      dtype: int32
  - name: labels
    sequence: string
  - name: hubs
    sequence: string
  - name: flows
    sequence: string
  - name: tags
    sequence: string
  - name: reading_time
    dtype: uint32
  - name: format
    dtype: string
  - name: complexity
    dtype: string
  - name: comments
    sequence:
    - name: id
      dtype: uint64
    - name: parent_id
      dtype: uint64
    - name: level
      dtype: uint32
    - name: time_published
      dtype: uint64
    - name: score
      dtype: int32
    - name: votes
      dtype: uint32
    - name: message_html
      dtype: string
    - name: message_markdown
      dtype: string
    - name: author
      dtype: string
    - name: children
      sequence: uint64
  splits:
  - name: train
    num_bytes: 19968161329
    num_examples: 302049
  download_size: 3485570346
  dataset_size: 19968161329
task_categories:
- text-generation
language:
- ru
- en
size_categories:
- 100K<n<1M
---

# Habr dataset

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Description](#description)
- [Usage](#usage)
- [Data Instances](#data-instances)
- [Source Data](#source-data)
- [Personal and Sensitive Information](#personal-and-sensitive-information)

## Description

**Summary:** Dataset of posts and comments from [habr.com](https://habr.com/ru/all/), a Russian collaborative blog about IT, computer science and anything related to the Internet.

**Script:** [create_habr.py](https://github.com/IlyaGusev/rulm/blob/master/data_processing/create_habr.py)

**Point of Contact:** [Ilya Gusev](ilya.gusev@phystech.edu)

**Languages:** Russian, English, some programming code.


## Usage

Prerequisites:
```bash
pip install datasets zstandard jsonlines pysimdjson
```

Dataset iteration:
```python
from datasets import load_dataset
dataset = load_dataset('IlyaGusev/habr', split="train", streaming=True)
for example in dataset:
    print(example["text_markdown"])
```

## Data Instances

```
{
  "id": 12730,
  "language": "ru",
  "url": "https://habr.com/ru/post/12730/",
  "text_markdown": "...",
  "text_html": "...",
  "lead_markdown": "...",
  "lead_html": "...",
  "type": "article",
  "labels": [],
  "original_author": null,
  "original_url": null,
  "time_published": 1185962380,
  "author": "...",
  "title": "Хочешь в университет — сделай презентацию",
  "statistics": {
    "commentsCount": 23,
    "favoritesCount": 1,
    "readingCount": 1542,
    "score": 7,
    "votesCount": 15,
    "votesCountPlus": 11,
    "votesCountMinus": 4
  },
  "hubs": [
    "itcompanies"
  ],
  "flows": [
    "popsci"
  ],
  "tags": [
    "PowerPoint",
    "презентация",
    "абитуриенты",
  ],
  "reading_time": 1,
  "format": null,
  "complexity": null,
  "comments": {
    "id": [11653537, 11653541],
    "parent_id": [null, 11653537],
    "level": [0, 1],
    "time_published": [1185963192, 1185967886],
    "score": [-1, 0],
    "votes": [1, 0],
    "message_html": ["...", "..."],
    "author": ["...", "..."],
    "children": [[11653541], []]
  }
}
```

You can use this little helper to unflatten sequences:

```python
def revert_flattening(records):
    fixed_records = []
    for key, values in records.items():
        if not fixed_records:
            fixed_records = [{} for _ in range(len(values))]
        for i, value in enumerate(values):
            fixed_records[i][key] = value
    return fixed_records
```

The original JSONL is already unflattened.


## Source Data

* The data source is the [Habr](https://habr.com/) website.
* API call example: [post 709430](https://habr.com/kek/v2/articles/709430).
* Processing script is [here](https://github.com/IlyaGusev/rulm/blob/master/data_processing/create_habr.py). 

## Personal and Sensitive Information

The dataset is not anonymized, so individuals' names can be found in the dataset. Information about the original authors is included in the dataset where possible.
