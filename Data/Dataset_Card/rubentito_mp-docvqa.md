---
pretty_name: MP-DocVQA (Multipage Document Visual Question Answering)
license: mit
task_categories:
- question-answering
- document-question-answering
- document-visual-question-answering
language:
- en
multilinguality:
- monolingual
source_datasets:
- Single Page Document Visual Question Answering
---

# Dataset Card for Multipage Document Visual Question Answering (MP-DocVQA)

## Dataset Description

- **Homepage: [Robust Reading Competition Portal](https://rrc.cvc.uab.es/?ch=17&com=introduction)** 
- **Repository: [Robust Reading Competition Portal](https://rrc.cvc.uab.es/?ch=17&com=downloads)** 
- **Paper: [Hierarchical multimodal transformers for Multi-Page DocVQA](https://arxiv.org/abs/2212.05935.pdf])** 
- **Leaderboard: [Task 4 of DocVQA on the Robust Reading Competition Portal](https://rrc.cvc.uab.es/?ch=17&com=evaluation&task=4)**

### Dataset Summary

The dataset is aimed to perform Visual Question Answering on multipage industry scanned documents. The questions and answers are reused from Single Page DocVQA (SP-DocVQA) dataset. The images also corresponds to the same in original dataset with previous and posterior pages with a limit of up to 20 pages per document.

### Download the Dataset

The dataset is not integrated with Huggingface yet. But you can download it from the [DocVQA Challenge](https://rrc.cvc.uab.es/?ch=17) in the RRC Portal, [Downloads section](https://rrc.cvc.uab.es/?ch=17&com=downloads).

### Leaderboard

You can also check the live leaderboard at the [RRC Portal](https://rrc.cvc.uab.es/?ch=17&com=evaluation&task=4)


## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

|          | Train | Validation | Test | Total |
|----------|:-----:|:-----------:|:------:|:-------:|
|**Questions** |36230 |   5187     |5019  | 46436 |
|**Documents** |5131 |   927     |959  | 5929 |
|**Pages / Images**     |37269 |   6510     |6223  | 47952 |

Note that some documents might appear in both validation and test set. But they are never seen during training.

### Citation Information

```tex
@article{tito2022hierarchical,
  title={Hierarchical multimodal transformers for Multi-Page DocVQA},
  author={Tito, Rub{\`e}n and Karatzas, Dimosthenis and Valveny, Ernest},
  journal={arXiv preprint arXiv:2212.05935},
  year={2022}
}
```

