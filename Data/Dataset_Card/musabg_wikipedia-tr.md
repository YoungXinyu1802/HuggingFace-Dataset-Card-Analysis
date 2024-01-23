---
annotations_creators:
- no-annotation
language:
- tr
language_creators:
- crowdsourced
license:
- cc-by-sa-3.0
- gfdl
multilinguality: []
pretty_name: Turkish February 2023
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- wikipedia, wiki,
task_categories:
- fill-mask
- text-generation
task_ids:
- masked-language-modeling
dataset_info:
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 935821219
    num_examples: 512377
  download_size: 518914544
  dataset_size: 935821219
---


# 📖 Wikipedia Turkish February 2023

Welcome to the Hugging Face dataset page for the Wikipedia Turkish February 2023 dataset! 
This dataset is a collection of articles from the Turkish Wikipedia and is designed to be used for masked language modeling and text generation tasks.

## 📚 Dataset Info

The dataset is organized into one split: "train". The "train" split contains 512,377 examples and has a size of 935,821,219 bytes. Each example in the dataset contains the following features: id, url, title, and text. The "id" feature is a string, while the "url", "title", and "text" features are all of dtype string.
Based on Wikipedia dump of "20230220"
Processed and cleaned using Huggingface wikipedia cleaner.

## 🗣️ Annotations

The articles in this dataset were not specifically annotated for any particular task, meaning that the dataset is unlabeled.

## 🌐 Language

This dataset is written in Turkish and was created using crowdsourcing methods by a team of volunteers.

## 📜 License

The Wikipedia Turkish February 2023 dataset is released under two licenses: CC-BY-SA 3.0 and GFDL. These licenses allow for the free use and distribution of the dataset with appropriate attribution.

## 🌍 Multilinguality

This dataset is not multilingual and is written solely in Turkish.

## 💻 Source Datasets

This dataset is an original dataset created from the Turkish Wikipedia.

## 📝 Task Categories and IDs

The Wikipedia Turkish February 2023 dataset is designed to be used for two main tasks: fill-mask and text-generation. The task IDs associated with this dataset are "masked-language-modeling".


## 💾 Download Size

The download size of the Wikipedia Turkish February 2023 dataset is 518,914,544 bytes.

Thank you for using the Wikipedia Turkish February 2023 dataset! We hope it is useful for your language modeling and text generation tasks.

