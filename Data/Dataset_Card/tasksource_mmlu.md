---
license: apache-2.0
task_categories:
- text-classification
- multiple-choice
task_ids:
- multiple-choice-qa
- open-domain-qa
- closed-domain-qa
language:
- en
tags:
- multi-task
- multitask
- mmlu
- hendrycks_test
pretty_name: mmlu
---

MMLU (`hendrycks_test` on huggingface) without auxiliary train. It is much lighter (7MB vs 162MB) and faster than the original implementation, in which auxiliary train is loaded (+ duplicated!) by default for all the configs in the original version, making it quite heavy.

We use this version in [tasksource](https://huggingface.co/tasksource). 

Reference to original dataset:
Measuring Massive Multitask Language Understanding - https://github.com/hendrycks/test
```
@article{hendryckstest2021,
  title={Measuring Massive Multitask Language Understanding},
  author={Dan Hendrycks and Collin Burns and Steven Basart and Andy Zou and Mantas Mazeika and Dawn Song and Jacob Steinhardt},
  journal={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2021}
}
```