---
language:
- hr
license:
- cc-by-sa-4.0
task_categories:
- text-classification
task_ids:
- natural-language-inference
tags:
- causal-reasoning
- textual-entailment
- commonsense-reasoning
---
The COPA-HR dataset (Choice of plausible alternatives in Croatian) is a translation 
of the English COPA dataset (https://people.ict.usc.edu/~gordon/copa.html) by following the 
XCOPA dataset translation methodology (https://arxiv.org/abs/2005.00333). The dataset consists of 1000 premises 
(My body cast a shadow over the grass), each given a question (What is the cause?), and two choices 
(The sun was rising; The grass was cut), with a label encoding which of the choices is more plausible 
given the annotator or translator (The sun was rising).

The dataset is split into 400 training samples, 100 validation samples, and 500 test samples. It includes the 
following features: 'premise', 'choice1', 'choice2', 'label', 'question', 'changed' (boolean).

If you use the dataset in your work, please cite
```
@article{DBLP:journals/corr/abs-2104-09243,
 author    = {Nikola Ljube\\\\v{s}i\\\\'{c} and
              Davor Lauc},
 title     = {BERTi{\\\\'{c}} - The Transformer Language Model for Bosnian, Croatian,
               Montenegrin and Serbian},
 journal   = {CoRR},
 volume    = {abs/2104.09243},
 year      = {2021},
 url       = {https://arxiv.org/abs/2104.09243},
 archivePrefix = {arXiv},
}
```