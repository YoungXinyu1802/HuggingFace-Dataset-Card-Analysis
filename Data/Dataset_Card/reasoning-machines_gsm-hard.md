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
- gsm8k (https://huggingface.co/datasets/gsm8k)
task_categories:
- text2text-generation
task_ids: []
pretty_name: gsm-hard
tags:
- math_reasoning
- symbolic_reasoning
---

## Dataset Description
- **Repository:** https://reasonwithpal.com/
- **Paper:** [PaL: Program-Aided Language Model](https://arxiv.org/abs/2211.10435)

### Dataset Summary
This is the harder version of gsm8k math reasoning dataset (https://huggingface.co/datasets/gsm8k).
We construct this dataset by replacing the numbers in the questions of GSM8K with larger numbers that are less common.


### Supported Tasks and Leaderboards
This dataset is used to evaluate math reasoning

### Languages
English - Numbers

## Dataset Structure
```python
dataset = load_dataset("reasoning-machines/gsm-hard")
DatasetDict({
    train: Dataset({
        features: ['input', 'code', 'target'],
        num_rows: 1319
    })
})
```

### Data Fields
train/dev/test:
- input: The question
- code: The corresponding code solution to the question
- target: The answer

### Citation Information

```
@article{gao2022pal,
  title={PAL: Program-aided Language Models},
  author={Gao, Luyu and Madaan, Aman and Zhou, Shuyan and Alon, Uri and Liu, Pengfei and Yang, Yiming and Callan, Jamie and Neubig, Graham},
  journal={arXiv preprint arXiv:2211.10435},
  year={2022}
}
```