---
annotations_creators: []
language:
- code
license:
- other
multilinguality:
- monolingual
size_categories:
- unknown
task_categories:
- text-generation
task_ids:
- language-modeling
pretty_name: github-jupyter-text-code-pairs
---

This is a parsed version of [github-jupyter-parsed](https://huggingface.co/datasets/codeparrot/github-jupyter-parsed), with markdown and code pairs. We provide the preprocessing script in [preprocessing.py](https://huggingface.co/datasets/codeparrot/github-jupyter-parsed-v2/blob/main/preprocessing.py). The data is deduplicated and consists of 451662 examples. 

For similar datasets with text and Python code, there is [CoNaLa](https://huggingface.co/datasets/neulab/conala) benchmark from StackOverflow, with some samples curated by annotators.