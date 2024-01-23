---
language:
- pt
multilinguality:
- monolingual
task_ids:
- language-modeling
paperswithcode_id: lener-br
pretty_name: LeNER-Br language modeling
datasets:
- lener_br
tags:
- lener_br
---

# Dataset Card for "LeNER-Br language modeling"

## Dataset Summary

The LeNER-Br language modeling dataset is a collection of legal texts in Portuguese from the [LeNER-Br](https://huggingface.co/datasets/lener_br) dataset ([official site](https://cic.unb.br/~teodecampos/LeNER-Br/)).
 
The legal texts were downloaded from this [link](https://cic.unb.br/~teodecampos/LeNER-Br/LeNER-Br.zip) (93.6MB) and processed to create a `DatasetDict` with train and validation dataset (20%).

The LeNER-Br language modeling dataset allows the finetuning of language models as BERTimbau [base](https://huggingface.co/neuralmind/bert-base-portuguese-cased) and [large](https://huggingface.co/neuralmind/bert-large-portuguese-cased).

## Language

Portuguese from Brazil.

## Blog post

[NLP | Modelos e Web App para Reconhecimento de Entidade Nomeada (NER) no domínio jurídico brasileiro](https://medium.com/@pierre_guillou/nlp-modelos-e-web-app-para-reconhecimento-de-entidade-nomeada-ner-no-dom%C3%ADnio-jur%C3%ADdico-b658db55edfb) (29/12/2021)

## Dataset structure

```
DatasetDict({
    validation: Dataset({
        features: ['text'],
        num_rows: 3813
    })
    train: Dataset({
        features: ['text'],
        num_rows: 15252
    })
})
```

## Use

```
!pip install datasets
from datasets import load_dataset

dataset = load_dataset("pierreguillou/lener_br_finetuning_language_model")
```