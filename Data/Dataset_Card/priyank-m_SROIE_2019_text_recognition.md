---
annotations_creators: []
language:
- en
language_creators: []
license: []
multilinguality:
- monolingual
pretty_name: SROIE_2019_text_recognition
size_categories:
- 10K<n<100K
source_datasets: []
tags:
- text-recognition
- recognition
task_categories:
- image-to-text
task_ids:
- image-captioning
---
This dataset we prepared using the Scanned receipts OCR and information extraction(SROIE) dataset.
The SROIE dataset contains 973 scanned receipts in English language.
Cropping the bounding boxes from each of the receipts to generate this text-recognition dataset resulted in 33626 images for train set and 18704 images for the test set.
The text annotations for all the images inside a split are stored in a metadata.jsonl file.

usage: 

from dataset import load_dataset

data = load_dataset("priyank-m/SROIE_2019_text_recognition")

source of raw SROIE dataset:
https://www.kaggle.com/datasets/urbikn/sroie-datasetv2