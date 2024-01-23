---
annotations_creators:
- expert-generated
language:
- 'no'
- 'nob'
- 'en'
language_creators:
- machine-generated
- expert-generated
license:
- apache-2.0
multilinguality:
- multilingual
pretty_name: MNLI Norwegian
size_categories:
- 100K<n<1M
source_datasets: []
tags:
- norwegian
- simcse
- mnli
- nli
- sentence
task_categories:
- sentence-similarity
- text-classification
task_ids:
- natural-language-inference
- semantic-similarity-classification
---

# MNLI Norwegian
The Multi-Genre Natural Language Inference (MultiNLI) corpus is a crowd-sourced collection of 433k sentence pairs annotated with textual entailment information. The corpus is modeled on the SNLI corpus, but differs in that it covers a range of genres of spoken and written text, and supports a distinctive cross-genre generalisation evaluation. There is also a [HuggingFace version](https://huggingface.co/datasets/multi_nli) of the dataset available. 

This dataset is machine translated using Google Translate. From this translation different version of the dataset where created. Included in the repo is a version that is specifically suited for training sentence-BERT-models. This version include the triplet: base-entailment-contradiction. It also includes a version that mixes English and Norwegian, as well as both csv and json-verions. The script for generating the datasets are included in this repo. 

Please note that there is no test dataset for MNLI, since this is closed. The authors of MNLI informs us that they selected 7500 new contexts in the same way as the original MNLI contexts. That means the English part of the XNLI test sets is highly comparable. For each genre, the text is generally in-domain with the original MNLI test set (it's from the same source and selected by me in the same way). In most cases the XNLI test set can therefore be used. 

### The following datasets are available in the repo:

* mnli_no_en_for_simcse.csv
* mnli_no_en_small_for_simcse.csv
* mnli_no_for_simcse.csv
* multinli_1.0_dev_matched_no_mt.jsonl
* multinli_1.0_dev_mismatched_no_mt.jsonl
* multinli_1.0_train_no_mt.jsonl
* nli_for_simcse.csv
* xnli_dev_no_mt.jsonl
* xnli_test_no_mt.jsonl


### Licensing Information
The majority of the corpus is released under the OANC’s license, which allows all content to be freely used, modified, and shared under permissive terms. The data in the FICTION section falls under several permissive licenses; Seven Swords is available under a Creative Commons Share-Alike 3.0 Unported License, and with the explicit permission of the author, Living History and Password Incorrect are available under Creative Commons Attribution 3.0 Unported Licenses; the remaining works of fiction are in the public domain in the United States (but may be licensed differently elsewhere). The translation and compilation of the Norwegian part is released under the Creative Commons Attribution 3.0 Unported Licenses.


### Citation Information
The datasets are compiled and machine translated by the AiLab at the Norwegian National Library. However, the vast majority of the work related to this dataset is compiling the English version. We therefore suggest that you also cite the original work:

```
@InProceedings{N18-1101,
  author = "Williams, Adina
            and Nangia, Nikita
            and Bowman, Samuel",
  title = "A Broad-Coverage Challenge Corpus for
           Sentence Understanding through Inference",
  booktitle = "Proceedings of the 2018 Conference of
               the North American Chapter of the
               Association for Computational Linguistics:
               Human Language Technologies, Volume 1 (Long
               Papers)",
  year = "2018",
  publisher = "Association for Computational Linguistics",
  pages = "1112--1122",
  location = "New Orleans, Louisiana",
  url = "http://aclweb.org/anthology/N18-1101"
}

