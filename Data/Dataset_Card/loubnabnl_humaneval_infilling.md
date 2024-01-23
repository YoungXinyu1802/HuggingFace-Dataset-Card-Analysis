---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- code
license:
- mit
multilinguality:
- monolingual
source_datasets:
- original
task_categories:
- text2text-generation
task_ids: []
pretty_name: OpenAI HumanEval-Infilling
tags:
- code-generation
---

# HumanEval-Infilling


## Dataset Description

- **Repository:**  https://github.com/openai/human-eval-infilling
- **Paper:** https://arxiv.org/pdf/2207.14255

## Dataset Summary

[HumanEval-Infilling](https://github.com/openai/human-eval-infilling) is a benchmark for infilling tasks, derived from [HumanEval](https://huggingface.co/datasets/openai_humaneval) benchmark for the evaluation of code generation models.

## Dataset Structure
To load the dataset you need to specify a subset. By default `HumanEval-SingleLineInfilling` is loaded.

```python
from datasets import load_dataset
ds = load_dataset("humaneval_infilling", "HumanEval-RandomSpanInfilling")

DatasetDict({
    test: Dataset({
        features: ['task_id', 'entry_point', 'prompt', 'suffix', 'canonical_solution', 'test'],
        num_rows: 1640
    })
})
```

## Subsets

This dataset has 4 subsets: HumanEval-MultiLineInfilling, HumanEval-SingleLineInfilling, HumanEval-RandomSpanInfilling, HumanEval-RandomSpanInfillingLight.
The single-line, multi-line, random span infilling and its light version have 1033, 5815, 1640 and 164 tasks, respectively.

## Citation

```
@article{bavarian2022efficient,
  title={Efficient Training of Language Models to Fill in the Middle},
  author={Bavarian, Mohammad and Jun, Heewoo and Tezak, Nikolas and Schulman, John and McLeavey, Christine and Tworek, Jerry and Chen, Mark},
  journal={arXiv preprint arXiv:2207.14255},
  year={2022}
}
```