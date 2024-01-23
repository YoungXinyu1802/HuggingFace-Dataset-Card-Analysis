---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name: MIT Movie
---

# Dataset Card for "tner/mit_movie_trivia"

## Dataset Description

- **Repository:** [T-NER](https://github.com/asahi417/tner)
- **Dataset:** MIT Movie
- **Domain:** Movie
- **Number of Entity:** 12

### Dataset Summary
MIT Movie NER dataset formatted in a part of [TNER](https://github.com/asahi417/tner) project.

- Entity Types: `Actor`, `Plot`, `Opinion`, `Award`, `Year`, `Genre`, `Origin`, `Director`, `Soundtrack`, `Relationship`, `Character_Name`, `Quote`

## Dataset Structure

### Data Instances
An example of `train` looks as follows.

```
{
    'tags': [0, 13, 14, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4],
    'tokens': ['a', 'steven', 'spielberg', 'film', 'featuring', 'a', 'bluff', 'called', 'devil', 's', 'tower', 'and', 'a', 'spectacular', 'mothership']
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/mit_movie_trivia/raw/main/dataset/label.json).
```python
{
    "O": 0,
    "B-Actor": 1,
    "I-Actor": 2,
    "B-Plot": 3,
    "I-Plot": 4,
    "B-Opinion": 5,
    "I-Opinion": 6,
    "B-Award": 7,
    "I-Award": 8,
    "B-Year": 9,
    "B-Genre": 10,
    "B-Origin": 11,
    "I-Origin": 12,
    "B-Director": 13,
    "I-Director": 14,
    "I-Genre": 15,
    "I-Year": 16,
    "B-Soundtrack": 17,
    "I-Soundtrack": 18,
    "B-Relationship": 19,
    "I-Relationship": 20,
    "B-Character_Name": 21,
    "I-Character_Name": 22,
    "B-Quote": 23,
    "I-Quote": 24
}
```

### Data Splits

|  name   |train|validation|test|
|---------|----:|---------:|---:|
|mit_movie_trivia      |6816  |       1000| 1953|
