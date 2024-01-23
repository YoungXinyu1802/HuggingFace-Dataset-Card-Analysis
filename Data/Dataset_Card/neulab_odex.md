---
license: cc-by-sa-4.0
task_categories:
- text2text-generation
- text-generation
language:
- en
- es
- ja
- ru
size_categories:
- n<1K
---

__ODEX__ is an Open-Domain EXecution-based NL-to-Code generation data benchmark. 
It contains 945 samples with a total of 1,707 human-written test cases, covering intents in four different natural languages --  439 in English, 90 in Spanish, 164 in Japanese, and 252 in Russian.


You can load the dataset by specifying a subset from *en, es, ja, ru* (by default the english subset *en* is loaded):
```python
from datasets import load_dataset

ds = load_dataset("neulab/odex", "ja", split="test")
```

If you find our dataset useful, please cite the paper

```
@article{wang2022execution,
  title={Execution-Based Evaluation for Open-Domain Code Generation},
  author={Zhiruo Wang, Shuyan Zhou, Daniel Fried, Graham Neubig},
  journal={arXiv preprint arXiv:2212.10481},
  year={2022}
}
```