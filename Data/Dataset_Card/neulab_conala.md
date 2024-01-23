---
annotations_creators: []
language_creators:
- crowdsourced
- expert-generated
language:
- code
license:
- mit
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- text2text-generation
task_ids: []
pretty_name: CoNaLa
tags:
- code-generation
---

## Dataset Description
- **Repository:** https://conala-corpus.github.io/
- **Paper:** [Learning to Mine Aligned Code and Natural Language Pairs from Stack Overflow](https://arxiv.org/pdf/1805.08949.pdf)

### Dataset Summary
[CoNaLa](https://conala-corpus.github.io/) is a benchmark of code and natural language pairs, for the evaluation of code generation tasks. The dataset was crawled from Stack Overflow, automatically filtered, then curated by annotators, split into 2,379 training and 500 test examples. The automatically mined dataset is also available with almost 600k examples.


### Supported Tasks and Leaderboards
This dataset is used to evaluate code generations.

### Languages
English - Python code.

## Dataset Structure
```python
dataset_curated = load_dataset("neulab/conala")
DatasetDict({
    train: Dataset({
        features: ['question_id', 'intent', 'rewritten_intent', 'snippet'],
        num_rows: 2379
    })
    test: Dataset({
        features: ['question_id', 'intent', 'rewritten_intent', 'snippet'],
        num_rows: 500
    })
})

dataset_mined = load_dataset("neulab/conala", "mined")
DatasetDict({
    train: Dataset({
        features: ['question_id', 'parent_answer_post_id', 'prob', 'snippet', 'intent', 'id'],
        num_rows: 593891
    })
})
```
### Data Instances

#### CoNaLa - curated
This is the curated dataset by annotators
```
{
    'question_id': 41067960,
    'intent': 'How to convert a list of multiple integers into a single integer?',
    'rewritten_intent': "Concatenate elements of a list 'x' of multiple integers to a single integer",
    'snippet': 'sum(d * 10 ** i for i, d in enumerate(x[::-1]))'
}
```

#### CoNaLa - mined
This is the automatically mined dataset before curation
```
{
    'question_id': 34705205,
     'parent_answer_post_id': 34705233,
     'prob': 0.8690001442846342,
     'snippet': 'sorted(l, key=lambda x: (-int(x[1]), x[0]))',
     'intent': 'Sort a nested list by two elements',
     'id': '34705205_34705233_0'
}
```

### Data Fields
Curated:

|Field|Type|Description|
|---|---|---|
|question_id|int64|Id of the Stack Overflow question|
|intent|string|Natural Language intent (i.e., the title of a Stack Overflow question)|
|rewritten_intent|string|Crowdsourced revised intents that try to better reflect the full meaning of the code|
|snippet|string| Code snippet that implements the intent|

Mined:

|Field|Type|Description|
|---|---|---|
|question_id|int64|Id of the Stack Overflow question|
|parent_answer_post_id|int64|Id of the answer post from which the candidate snippet is extracted|
|intent|string|Natural Language intent (i.e., the title of a Stack Overflow question)|
|snippet|string| Code snippet that implements the intent|
|id|string|Unique id for this intent/snippet pair|
|prob|float64|Probability given by the mining model|

### Data Splits
There are two version of the dataset (curated and mined), mined only has a train split and curated has two splits: train and test.

## Dataset Creation
The dataset was crawled from Stack Overflow, automatically filtered, then curated by annotators. For more details, please refer to the original [paper](https://arxiv.org/pdf/1805.08949.pdf)

### Citation Information

```
@inproceedings{yin2018learning,
  title={Learning to mine aligned code and natural language pairs from stack overflow},
  author={Yin, Pengcheng and Deng, Bowen and Chen, Edgar and Vasilescu, Bogdan and Neubig, Graham},
  booktitle={2018 IEEE/ACM 15th international conference on mining software repositories (MSR)},
  pages={476--486},
  year={2018},
  organization={IEEE}
}
``` 