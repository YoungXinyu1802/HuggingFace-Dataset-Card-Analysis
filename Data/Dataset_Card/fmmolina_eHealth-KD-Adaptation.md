---
license: afl-3.0
---

## Description

An adaptation of [eHealth-KD Challenge 2020 dataset](https://knowledge-learning.github.io/ehealthkd-2020/), filtered only for the task of NER. Some adaptation of the original dataset have been made:

- BIO annotations
- Errors fixing
- Overlapped entities has been processed as an unique entity

## Dataset loading

datasets = load_dataset('json', data_files={'train': ['@YOUR_PATH@/training_anns_bio.json'], 'testing': ['@YOUR_PATH@/testing_anns_bio.json'], 'validation': ['@YOUR_PATH@/development_anns_bio.json']})