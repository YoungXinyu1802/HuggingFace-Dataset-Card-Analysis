---
annotations_creators:
- crowdsourced
- expert-generated
- machine-generated
language_creators:
- crowdsourced
- expert-generated
- machine-generated
- other
language:
- en
license:
- apache-2.0
multilinguality:
- multilingual
- monolingual
pretty_name: bigbench
size_categories:
- unknown
source_datasets:
- original
task_categories:
- multiple-choice
- question-answering
- text-classification
- text-generation
- zero-shot-classification
task_ids:
- multiple-choice-qa
- extractive-qa
- open-domain-qa
- closed-domain-qa
- fact-checking
- acceptability-classification
- intent-classification
- multi-class-classification
- multi-label-classification
- text-scoring
- hate-speech-detection
- language-modeling
---
BIG-Bench but it doesn't require the hellish dependencies (tensorflow, pypi-bigbench, protobuf) of the official version.
```python
dataset = load_dataset("tasksource/bigbench",'movie_recommendation')
```
Code to reproduce:
https://colab.research.google.com/drive/1MKdLdF7oqrSQCeavAcsEnPdI85kD0LzU?usp=sharing

Datasets are capped to 50k examples to keep things light.
I also removed the default split when train was available also to save space, as default=train+val.

```bibtex
@article{srivastava2022beyond,
  title={Beyond the imitation game: Quantifying and extrapolating the capabilities of language models},
  author={Srivastava, Aarohi and Rastogi, Abhinav and Rao, Abhishek and Shoeb, Abu Awal Md and Abid, Abubakar and Fisch, Adam and Brown, Adam R and Santoro, Adam and Gupta, Aditya and Garriga-Alonso, Adri{\`a} and others},
  journal={arXiv preprint arXiv:2206.04615},
  year={2022}
}
```