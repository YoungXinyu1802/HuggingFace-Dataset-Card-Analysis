---
task_categories:
- question-answering
language:
- en
pretty_name: LogiQA
size_categories:
- 1K<n<10K
paperswithcode_id: logiqa
dataset_info:
  features:
    - name: context
      dtype: string
    - name: query
      dtype: string
    - name: options
      sequence:
          dtype: string
    - name: correct_option
      dtype: string
  splits:
    - name: train
      num_examples: 7376
    - name: validation
      num_examples: 651
    - name: test
      num_examples: 651
---
# Dataset Card for LogiQA

## Dataset Description

- **Homepage:** 
- **Repository:** 
- **Paper:** 
- **Leaderboard:** 
- **Point of Contact:** 

### Dataset Summary

LogiQA is constructed from the logical comprehension problems from publically available questions of the National Civil Servants Examination of China, which are designed to test the civil servant candidates’ critical thinking and problem solving. This dataset includes the English versions only; the Chinese versions are available via the homepage/original source.


## Dataset Structure

### Data Instances

An example from `train` looks as follows:
```
{'context': 'Continuous exposure to indoor fluorescent lights is beneficial to the health of hamsters with heart disease. One group of hamsters exposed to continuous exposure to fluorescent lights has an average lifespan that is 2.5% longer than another one of the same species but living in a black wall.',
 'query': 'Which of the following questions was the initial motivation for conducting the above experiment?',
 'options': ['Can hospital light therapy be proved to promote patient recovery?',
  'Which one lives longer, the hamster living under the light or the hamster living in the dark?',
  'What kind of illness does the hamster have?',
  'Do some hamsters need a period of darkness?'],
 'correct_option': 0}
```

### Data Fields

- `context`: a `string` feature.
- `query`: a `string` feature.
- `answers`: a `list` feature containing `string` features.
- `correct_option`: a `string` feature.


### Data Splits

|train|validation|test|
|----:|---------:|---:|
| 7376|       651| 651|


## Additional Information

### Dataset Curators

The original LogiQA was produced by Jian Liu, Leyang Cui , Hanmeng Liu, Dandan Huang, Yile Wang, and Yue Zhang.

### Licensing Information

[More Information Needed]

### Citation Information

```
@article{liu2020logiqa,
  title={Logiqa: A challenge dataset for machine reading comprehension with logical reasoning},
  author={Liu, Jian and Cui, Leyang and Liu, Hanmeng and Huang, Dandan and Wang, Yile and Zhang, Yue},
  journal={arXiv preprint arXiv:2007.08124},
  year={2020}
}
```

### Contributions

[@lucasmccabe](https://github.com/lucasmccabe) added this dataset.