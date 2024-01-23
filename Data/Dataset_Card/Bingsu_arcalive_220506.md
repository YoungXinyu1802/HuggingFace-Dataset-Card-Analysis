---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
language:
- ko
license:
- cc0-1.0
multilinguality:
- monolingual
paperswithcode_id: null
pretty_name: arcalive_210816_220506
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- fill-mask
- text-generation
task_ids:
- masked-language-modeling
- language-modeling
---

# Dataset Card for Bingsu/arcalive_220506

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)

## Dataset Description

- **Homepage:** https://huggingface.co/datasets/Bingsu/arcalive_220506
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

[아카라이브 베스트 라이브 채널](https://arca.live/b/live)의 2021년 8월 16일부터 2022년 5월 6일까지의 데이터를 수집하여, 댓글만 골라낸 데이터입니다.

커뮤니티 특성상, 민감한 데이터들도 많으므로 사용에 주의가 필요합니다.

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

ko

## Dataset Structure

### Data Instances

- Size of downloaded dataset files: 21.3 MB

### Data Fields

- text: `string`

### Data Splits

|            | train  |
| ---------- | ------ |
| # of texts | 195323 |

```pycon
>>> from datasets import load_dataset
>>>
>>> data = load_dataset("Bingsu/arcalive_220506")
>>> data["train"].features
{'text': Value(dtype='string', id=None)}
```

```pycon
>>> data["train"][0]
{'text': '오오오오...'}
```
