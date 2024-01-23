---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- crowdsourced
license: []
multilinguality:
- monolingual
pretty_name: 'TRIP: Tiered Reasoning for Intuitive Physics'
size_categories:
- 1K<n<10K
source_datasets:
- original
tags: []
task_categories:
- text-classification
task_ids:
- natural-language-inference
---
# [TRIP - Tiered Reasoning for Intuitive Physics](https://aclanthology.org/2021.findings-emnlp.422/)
Official dataset for [Tiered Reasoning for Intuitive Physics: Toward Verifiable Commonsense Language Understanding](https://aclanthology.org/2021.findings-emnlp.422/). Shane Storks, Qiaozi Gao, Yichi Zhang, Joyce Chai. EMNLP Findings, 2021.

For our official model and experiment code, please check [GitHub](https://github.com/sled-group/Verifiable-Coherent-NLU).

## Overview
![image](trip_sample.png)
We introduce Tiered Reasoning for Intuitive Physics (TRIP), a novel commonsense reasoning dataset with dense annotations that enable multi-tiered evaluation of machines’ reasoning process.

It includes dense annotations for each story capturing multiple tiers of reasoning beyond the end task. From these annotations, we propose a tiered evaluation, where given a pair of highly similar stories (differing only by one sentence which makes one of the stories implausible), systems must jointly identify (1) the plausible story, (2) a pair of conflicting sentences in the implausible story, and (3) the underlying physical states in those sentences causing the conflict. The goal of TRIP is to enable a systematic evaluation of machine coherence toward the end task prediction of plausibility. In particular, we evaluate whether a high-level plausibility prediction can be verified based on lower-level understanding, for example, physical state changes that would support the prediction.

## Download
```python
from datasets import load_dataset
dataset = load_dataset("sled-umich/TRIP")
```
* [HuggingFace-Dataset](https://huggingface.co/datasets/sled-umich/TRIP)
* [GitHub](https://github.com/sled-group/Verifiable-Coherent-NLU)

## Cite
```bibtex
@misc{storks2021tiered,
      title={Tiered Reasoning for Intuitive Physics: Toward Verifiable Commonsense Language Understanding}, 
      author={Shane Storks and Qiaozi Gao and Yichi Zhang and Joyce Chai},
      year={2021},
      booktitle={Findings of the Association for Computational Linguistics: EMNLP 2021},
      location={Punta Cana, Dominican Republic},
      publisher={Association for Computational Linguistics},
}
```
