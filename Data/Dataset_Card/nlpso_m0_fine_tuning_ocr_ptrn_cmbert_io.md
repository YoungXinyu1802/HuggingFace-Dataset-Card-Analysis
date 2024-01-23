---
language:
- fr
multilinguality:
- monolingual
task_categories:
- token-classification
---

# m0_fine_tuning_ocr_ptrn_cmbert_io

## Introduction

This dataset was used to fine-tuned [HueyNemud/das22-10-camembert_pretrained](https://huggingface.co/HueyNemud/das22-10-camembert_pretrained) for **flat NER task** using Flat NER approach [M0]. 
It contains 19th-century Paris trade directories' entries.

## Dataset parameters

* Approach : M0
* Dataset type : noisy (Pero OCR)
* Tokenizer : [HueyNemud/das22-10-camembert_pretrained](https://huggingface.co/HueyNemud/das22-10-camembert_pretrained)
* Tagging format : IO
* Counts : 
    * Train : 6084
    * Dev : 676
    * Test : 1685
* Associated fine-tuned model : [nlpso/m0_flat_ner_ocr_ptrn_cmbert_io](https://huggingface.co/nlpso/m0_flat_ner_ocr_ptrn_cmbert_io)
    
## Entity types

Abbreviation|Description
-|-
O |Outside of a named entity
PER |Person or company name
ACT |Person or company professional activity
TITRE |Distinction
LOC |Street name
CARDINAL |Street number
FT |Geographical feature

## How to use this dataset

```python
from datasets import load_dataset

train_dev_test = load_dataset("nlpso/m0_fine_tuning_ocr_ptrn_cmbert_io")
