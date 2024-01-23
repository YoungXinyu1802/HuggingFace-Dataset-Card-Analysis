---
annotations_creators:
- crowdsourced
language:
- eng
language_creators:
- crowdsourced
license: []
multilinguality:
- monolingual
pretty_name: Action-Effect-Prediction
size_categories:
- 1K<n<10K
source_datasets:
- original
tags: []
task_categories:
- image-classification
- image-to-text
task_ids: []
---
# Physical-Action-Effect-Prediction

Official dataset for ["What Action Causes This? Towards Naive Physical Action-Effect Prediction"](https://aclanthology.org/P18-1086/), ACL 2018.

![What Action Causes This? Towards Naive Physical Action-Effect Prediction](https://sled.eecs.umich.edu/media/datasets/action-effect-pred.png)



## Overview

Despite recent advances in knowledge representation, automated reasoning, and machine learning, artificial agents still lack the ability to understand basic action-effect relations regarding the physical world, for example, the action of cutting a cucumber most likely leads to the state where the cucumber is broken apart into smaller pieces. If artificial agents (e.g., robots) ever become our partners in joint tasks, it is critical to empower them with such action-effect understanding so that they can reason about the state of the world and plan for actions. Towards this goal, this paper introduces a new task on naive physical action-effect prediction, which addresses the relations between concrete actions (expressed in the form of verb-noun pairs) and their effects on the state of the physical world as depicted by images. We collected a dataset for this task and developed an approach that harnesses web image data through distant supervision to facilitate learning for action-effect prediction. Our empirical results have shown that web data can be used to complement a small number of seed examples (e.g., three examples for each action) for model learning. This opens up possibilities for agents to learn physical action-effect relations for tasks at hand through communication with humans with a few examples.

### Datasets

- This dataset contains action-effect information for 140 verb-noun pairs. It has two parts: effects described by natural language, and effects depicted in images.
- The language data contains verb-noun pairs and their effects described in natural language. For each verb-noun pair, its possible effects are described by 10 different annotators. The format for each line is `verb noun, effect_sentence, [effect_phrase_1, effect_phrase_2, effect_phrase_3, ...]`. Effect_phrases were automatically extracted from their corresponding effect_sentences. 
- The image data contains images depicting action effects. For each verb-noun pair, an average of 15 positive images and 15 negative images were collected. Positive images are those deemed to capture the resulting world state of the action. And negative images are those deemed to capture some state of the related object (*i.e.*, the nouns in the verb-noun pairs), but are not the resulting state of the corresponding action.

### Download
```python
from datasets import load_dataset

dataset = load_dataset("sled-umich/Action-Effect")
```
* [HuggingFace](https://huggingface.co/datasets/sled-umich/Action-Effect)
* [Google Drive](https://drive.google.com/drive/folders/1P1_xWdCUoA9bHGlyfiimYAWy605tdXlN?usp=sharing)
* Dropbox:
  * [Language Data](https://www.dropbox.com/s/pi1ckzjipbqxyrw/action_effect_sentence_phrase.txt?dl=0)
  * [Image Data](https://www.dropbox.com/s/ilmfrqzqcbdf22k/action_effect_image_rs.tar.gz?dl=0)

### Cite

[What Action Causes This? Towards Naïve Physical Action-Effect Prediction](https://sled.eecs.umich.edu/publication/dblp-confacl-vanderwende-cyg-18/). *Qiaozi Gao, Shaohua Yang, Joyce Chai, Lucy Vanderwende*. ACL, 2018. [[Paper]](https://aclanthology.org/P18-1086/) [[Slides]](https://aclanthology.org/attachments/P18-1086.Presentation.pdf)

```tex
@inproceedings{gao-etal-2018-action,
    title = "What Action Causes This? Towards Naive Physical Action-Effect Prediction",
    author = "Gao, Qiaozi  and
      Yang, Shaohua  and
      Chai, Joyce  and
      Vanderwende, Lucy",
    booktitle = "Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2018",
    address = "Melbourne, Australia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P18-1086",
    doi = "10.18653/v1/P18-1086",
    pages = "934--945",
    abstract = "Despite recent advances in knowledge representation, automated reasoning, and machine learning, artificial agents still lack the ability to understand basic action-effect relations regarding the physical world, for example, the action of cutting a cucumber most likely leads to the state where the cucumber is broken apart into smaller pieces. If artificial agents (e.g., robots) ever become our partners in joint tasks, it is critical to empower them with such action-effect understanding so that they can reason about the state of the world and plan for actions. Towards this goal, this paper introduces a new task on naive physical action-effect prediction, which addresses the relations between concrete actions (expressed in the form of verb-noun pairs) and their effects on the state of the physical world as depicted by images. We collected a dataset for this task and developed an approach that harnesses web image data through distant supervision to facilitate learning for action-effect prediction. Our empirical results have shown that web data can be used to complement a small number of seed examples (e.g., three examples for each action) for model learning. This opens up possibilities for agents to learn physical action-effect relations for tasks at hand through communication with humans with a few examples.",
}
```

