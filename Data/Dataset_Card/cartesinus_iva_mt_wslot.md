---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: locale
    dtype: string
  - name: origin
    dtype: string
  - name: partition
    dtype: string
  - name: translation_utt
    dtype:
      translation:
        languages:
        - en
        - pl
  - name: translation_xml
    dtype:
      translation:
        languages:
        - en
        - pl
  - name: src_bio
    dtype: string
  - name: tgt_bio
    dtype: string
  splits:
  - name: train
    num_bytes: 6187206
    num_examples: 20362
  - name: validation
    num_bytes: 1115480
    num_examples: 3681
  - name: test
    num_bytes: 1587613
    num_examples: 5394
  download_size: 3851892
  dataset_size: 8890299
task_categories:
- translation
language:
- en
- pl
tags:
- machine translation
- nlu
- natural-language-understanding
- virtual assistant
pretty_name: Machine translation for NLU with slot transfer
size_categories:
- 10K<n<100K
license: cc-by-4.0
---
# Machine translation dataset for NLU (Virual Assistant) with slot transfer between languages
## Dataset Summary

Disclaimer: This is Work-In-Progress and for research purposes only.

IVA_MT is machine translation dataset that can be used to train, adapt and evaluate MT models used in Virtual Assistant NLU context (e.g. to translate trainig corpus of NLU).

## Dataset Composition (en-pl)
| Corpus                                                               | Train  | Dev   | Test  |
|----------------------------------------------------------------------|--------|-------|-------|
| [Massive 1.1](https://huggingface.co/datasets/AmazonScience/massive) | 11514  | 2033  | 2974  |
| [Leyzer 0.2.0](https://github.com/cartesinus/leyzer/tree/0.2.0)      | 3974   | 701   | 1380  |
| [OpenSubtitles from OPUS](https://opus.nlpl.eu/OpenSubtitles-v1.php) | 2329   | 411   | 500   |
| [KDE from OPUS](https://opus.nlpl.eu/KDE4.php)                       | 1154   | 241   | 241   |
| [CCMatrix from Opus](https://opus.nlpl.eu/CCMatrix.php)              | 1096   | 232   | 237   |
| [Ubuntu from OPUS](https://opus.nlpl.eu/Ubuntu.php)                  | 281    | 60    | 59    |
| [Gnome from OPUS](https://opus.nlpl.eu/GNOME.php)                    | 14     | 3     | 3     |
| *total*                                                              | 20362  | 3681  | 5394  |

## Tools
Scripts used to generate this dataset can be found on [github](https://github.com/cartesinus/iva_mt).