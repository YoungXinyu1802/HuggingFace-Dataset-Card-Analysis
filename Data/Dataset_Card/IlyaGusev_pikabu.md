---
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: title
    dtype: string
  - name: text_markdown
    dtype: string
  - name: timestamp
    dtype: uint64
  - name: author_id
    dtype: int64
  - name: username
    dtype: string
  - name: rating
    dtype: int64
  - name: pluses
    dtype: int64
  - name: minuses
    dtype: int64
  - name: url
    dtype: string
  - name: tags
    sequence: string
  - name: blocks
    sequence:
    - name: data
      dtype: string
    - name: type
      dtype: string
  - name: comments
    sequence:
    - name: id
      dtype: int64
    - name: timestamp
      dtype: uint64
    - name: parent_id
      dtype: int64
    - name: text_markdown
      dtype: string
    - name: text_html
      dtype: string
    - name: images
      sequence: string
    - name: rating
      dtype: int64
    - name: pluses
      dtype: int64
    - name: minuses
      dtype: int64
    - name: author_id
      dtype: int64
    - name: username
      dtype: string
  splits:
  - name: train
    num_bytes: 96105803658
    num_examples: 6907622
  download_size: 20196853689
  dataset_size: 96105803658
task_categories:
- text-generation
language:
- ru
size_categories:
- 1M<n<10M
---


# Pikabu dataset

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Description](#description)
- [Usage](#usage)
- [Data Instances](#data-instances)
- [Source Data](#source-data)
- [Personal and Sensitive Information](#personal-and-sensitive-information)

## Description

**Summary:** Dataset of posts and comments from [pikabu.ru](https://pikabu.ru/), a website that is Russian Reddit/9gag.

**Script:** [convert_pikabu.py](https://github.com/IlyaGusev/rulm/blob/master/data_processing/convert_pikabu.py)

**Point of Contact:** [Ilya Gusev](ilya.gusev@phystech.edu)

**Languages:** Mostly Russian.


## Usage

Prerequisites:
```bash
pip install datasets zstandard jsonlines pysimdjson
```

Dataset iteration:
```python
from datasets import load_dataset
dataset = load_dataset('IlyaGusev/pikabu', split="train", streaming=True)
for example in dataset:
    print(example["text_markdown"])
```

## Data Instances

```
{
  "id": 69911642,
  "title": "Что можно купить в Китае за цену нового iPhone 11 Pro",
  "text_markdown": "...",
  "timestamp": 1571221527,
  "author_id": 2900955,
  "username": "chinatoday.ru",
  "rating": -4,
  "pluses": 9,
  "minuses": 13,
  "url": "...",
  "tags": ["Китай", "AliExpress", "Бизнес"],
  "blocks": {"data": ["...", "..."], "type": ["text", "text"]},
  "comments": {
    "id": [152116588, 152116426],
    "text_markdown": ["...", "..."],
    "text_html": ["...", "..."],
    "images": [[], []],
    "rating": [2, 0],
    "pluses": [2, 0],
    "minuses": [0, 0],
    "author_id": [2104711, 2900955],
    "username": ["FlyZombieFly", "chinatoday.ru"]
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


## Source Data

* The data source is the [Pikabu](https://pikabu.ru/) website.
* An original dump can be found here: [pikastat](https://pikastat.d3d.info/)
* Processing script is [here](https://github.com/IlyaGusev/rulm/blob/master/data_processing/convert_pikabu.py). 

## Personal and Sensitive Information

The dataset is not anonymized, so individuals' names can be found in the dataset. Information about the original authors is included in the dataset where possible.
