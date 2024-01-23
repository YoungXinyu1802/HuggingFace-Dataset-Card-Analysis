---
language:
- fr
multilinguality:
- monolingual
task_categories:
- token-classification
---

# m2m3_fine_tuning_ocr_ptrn_cmbert_io

## Introduction

This dataset was used to fine-tuned [HueyNemud/das22-10-camembert_pretrained](https://huggingface.co/HueyNemud/das22-10-camembert_pretrained) for **nested NER task** using Independant NER layers approach [M1]. 
It contains Paris trade directories entries from the 19th century.

## Dataset parameters

* Approachrd : M2 and M3
* Dataset type : noisy (Pero OCR)
* Tokenizer : [HueyNemud/das22-10-camembert_pretrained](https://huggingface.co/HueyNemud/das22-10-camembert_pretrained)
* Tagging format : IO
* Counts : 
    * Train : 6084
    * Dev : 676
    * Test : 1685
* Associated fine-tuned models :
    * M2 : [nlpso/m2_joint_label_ocr_ptrn_cmbert_io](https://huggingface.co/nlpso/m2_joint_label_ocr_ptrn_cmbert_io)
    * M3 : [nlpso/m3_hierarchical_ner_ocr_ptrn_cmbert_io](https://huggingface.co/nlpso/m3_hierarchical_ner_ocr_ptrn_cmbert_io)
    
## Entity types

Abbreviation|Entity group (level)|Description
-|-|-
O |1 & 2|Outside of a named entity
PER |1|Person or company name
ACT |1 & 2|Person or company professional activity
TITREH |2|Military or civil distinction
DESC |1|Entry full description
TITREP |2|Professionnal reward
SPAT |1|Address
LOC |2|Street name
CARDINAL |2|Street number
FT |2|Geographical feature

## How to use this dataset

```python
from datasets import load_dataset

train_dev_test = load_dataset("nlpso/m2m3_fine_tuning_ocr_ptrn_cmbert_io")
