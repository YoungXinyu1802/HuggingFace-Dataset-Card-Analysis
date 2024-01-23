---
annotations_creators:
- machine-generated
- expert-generated
language_creators:
- found
language:
- en
- it
license:
- other
multilinguality:
- translation
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- translation
pretty_name: iknlp22-pestyle
---

# Dataset Card for IK-NLP-22 Project 1: A Study in Post-Editing Stylometry

## Table of Contents

- [Dataset Card for IK-NLP-22 Project 1: A Study in Post-Editing Stylometry](#dataset-card-for-ik-nlp-22-project-1-a-study-in-post-editing-stylometry)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
      - [Train Split](#train-split)
      - [Test splits](#test-splits)
    - [Dataset Creation](#dataset-creation)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)

## Dataset Description

- **Source:** [FLORES-101](https://huggingface.co/datasets/gsarti/flores_101)
- **Point of Contact:** [Gabriele Sarti](mailto:ik-nlp-course@rug.nl)

### Dataset Summary

This dataset contains a sample of sentences taken from the [FLORES-101](https://huggingface.co/datasets/gsarti/flores_101) dataset that were either translated from scratch or post-edited from an existing automatic translation by three human translators. Translation were performed for the English-Italian language pair, and translators' behavioral data (keystrokes, pauses, editing times) were collected using the [PET](https://github.com/wilkeraziz/PET) platform.

This dataset is made available for final projects of the 2022 edition of the Natural Language Processing course at the [Information Science Master's Degree](https://www.rug.nl/masters/information-science/?lang=en) at the University of Groningen, taught by [Arianna Bisazza](https://research.rug.nl/en/persons/arianna-bisazza) and [Gabriele Sarti](https://research.rug.nl/en/persons/gabriele-sarti) with the assistance of [Anjali Nair](https://nl.linkedin.com/in/anjalinair012).

**Disclaimer**: *This repository is provided without direct data access due to currently unpublished results.* _**For this reason, it is strictly forbidden to share or publish all the data associated to this repository**_. *Students will be provided with a compressed folder containing the data upon choosing a project based on this dataset. To load the dataset using 🤗 Datasets, download and unzip the provided folder and pass it to the* `load_dataset` *method as:* `datasets.load_dataset('GroNLP/ik-nlp-22_pestyle', 'full', data_dir='path/to/unzipped/folder')`

### Languages

The language data of is in English (BCP-47 `en`) and Italian (BCP-47 `it`)

## Dataset Structure

### Data Instances

The dataset contains four configurations: `full`, `test_mask_subject`, `test_mask_modality`, `test_mask_time`. `full` contains the main `train` split in which all fields are available. The other three, `test_mask_subject`, `test_mask_modality`, `test_mask_time`, contain a `test` split each with different fields removed to avoid information leaking during evaluation. See more details in the [Data Splits](#data-splits) section.

### Data Fields

The following fields are contained in the training set:

|Field|Description|
|-----|-----------|
|`item_id`   | The sentence identifier. The first digits of the number represent the document containing the sentence, while the last digit of the number represents the sentence position inside the document. Documents can contain from 3 to 5 semantically-related sentences each. |
|`subject_id`   | The identifier for the translator performing the translation from scratch or post-editing task. Values: `t1`, `t2` or `t3`. |
|`modality`   | The modality of the translation task. Values: `ht` (translation from scratch), `pe1` (post-editing Google Translate translations), `pe2` (post-editing [mBART](https://huggingface.co/facebook/mbart-large-50-one-to-many-mmt) translations). |
|`src_text`   | The original source sentence extracted from Wikinews, wikibooks or wikivoyage. |
|`mt_text`   | Missing if tasktype is `ht`. Otherwise, contains the automatically-translated sentence before post-editing. |
|`tgt_text`   | Final sentence produced by the translator (either via translation from scratch of `sl_text` or post-editing `mt_text`) |
|`edit_time`   | Total editing time for the translation in seconds. |
|`k_total`   | Total number of keystrokes for the translation. |
|`k_letter`   | Total number of letter keystrokes for the translation. |
|`k_digit`   | Total number of digit keystrokes for the translation. |
|`k_white`   | Total number of whitespace keystrokes for the translation. |
|`k_symbol`   | Total number of symbol (punctuation, etc.) keystrokes for the translation. |
|`k_nav`   | Total number of navigation keystrokes (left-right arrows, mouse clicks) for the translation. |
|`k_erase`   | Total number of erase keystrokes (backspace, cancel) for the translation. |
|`k_copy`   | Total number of copy (Ctrl + C) actions during the translation. |
|`k_cut`   | Total number of cut (Ctrl + X) actions during the translation. |
|`k_paste`   | Total number of paste (Ctrl + V) actions during the translation. |
|`n_pause_geq_300`   | Number of pauses of 300ms or more during the translation. |
|`len_pause_geq_300`   | Total duration of pauses of 300ms or more, in milliseconds. |
|`n_pause_geq_1000`   | Number of pauses of 1s or more during the translation. |
|`len_pause_geq_1000`   | Total duration of pauses of 1000ms or more, in milliseconds. |
|`num_annotations` | Number of times the translator focused the texbox for performing the translation of the sentence during the translation session. E.g. 1 means the translation was performed once and never revised. |
|`n_insert`   | Number of post-editing insertions (empty for modality `ht`) computed using the [tercom](https://github.com/jhclark/tercom) library. |
|`n_delete`   | Number of post-editing deletions (empty for modality `ht`) computed using the [tercom](https://github.com/jhclark/tercom) library. |
|`n_substitute`   | Number of post-editing substitutions (empty for modality `ht`) computed using the [tercom](https://github.com/jhclark/tercom) library. |
|`n_shift`   | Number of post-editing shifts (empty for modality `ht`) computed using the [tercom](https://github.com/jhclark/tercom) library. |
|`bleu`   | Sentence-level BLEU score between MT and post-edited fields (empty for modality `ht`) computed using the [SacreBLEU](https://github.com/mjpost/sacrebleu) library with default parameters. |
|`chrf`   | Sentence-level chrF score between MT and post-edited fields (empty for modality `ht`) computed using the [SacreBLEU](https://github.com/mjpost/sacrebleu) library with default parameters. |
|`ter`   | Sentence-level TER score between MT and post-edited fields (empty for modality `ht`) computed using the [tercom](https://github.com/jhclark/tercom) library. |
|`aligned_edit`   | Aligned visual representation of REF (`mt_text`), HYP (`tl_text`) and edit operations (I = Insertion, D = Deletion, S = Substitution) performed on the field. Replace `\\n` with `\n` to show the three aligned rows.|

### Data Splits

| config| train| test|
|------:|-----:|----:|
|`main` | 1170 | 120 |

#### Train Split

The `train` split contains a total of 1170 triplets (or pairs, when translation from scratch is performed) annotated with behavioral data produced during the translation. The following is an example of the subject `t3` post-editing a machine translation produced by system 2 (tasktype `pe2`) taken from the `train` split. The field `aligned_edit` is showed over three lines to provide a visual understanding of its contents.

```json
{
    "item_id": 1072,
    "subject_id": "t3",
    "tasktype": "pe2",
    "src_text": "At the beginning dress was heavily influenced by the Byzantine culture in the east.",
    "mt_text": "All'inizio il vestito era fortemente influenzato dalla cultura bizantina dell'est.",
    "tgt+text": "Inizialmente, l'abbigliamento era fortemente influenzato dalla cultura bizantina orientale.",
    "edit_time": 45.687,
    "k_total": 51,
    "k_letter": 31,
    "k_digit": 0,
    "k_white": 2,
    "k_symbol": 3,
    "k_nav": 7,
    "k_erase": 3,
    "k_copy": 0,
    "k_cut": 0,
    "k_paste": 0,
    "n_pause_geq_300": 9,
    "len_pause_geq_300": 40032,
    "n_pause_geq_1000": 5,
    "len_pause_geq_1000": 38392,
    "num_annotations": 1,
    "n_insert": 0.0,
    "n_delete": 1.0,
    "n_substitute": 3.0,
    "n_shift": 0.0,
    "bleu": 47.99,
    "chrf": 62.05,
    "ter": 40.0,
    "aligned_edit: "REF:  all'inizio il            vestito         era fortemente influenzato dalla cultura bizantina dell'est.\\n
                    HYP:  ********** inizialmente, l'abbigliamento era fortemente influenzato dalla cultura bizantina orientale.\\n 
                    EVAL: D          S             S                                                                  S"
}
```

The text is provided as-is, without further preprocessing or tokenization.

#### Test splits

The three `test` splits (one per configuration) contain the same 120 entries each, following the same structure as `train`. Each test split omit some of the fields to prevent leakage of information:

- In `test_mask_subject` the `subject_id` is absent, for the main task of post-editor stylometry.

- In `test_mask_modality` the following fields are absent for the modality prediction extra task: `modality`, `mt_text`, `n_insert`, `n_delete`, `n_substitute`, `n_shift`, `ter`, `bleu`, `chrf`, `aligned_edit`.

- In `test_mask_time` the following fields are absent for the time and pause prediction extra task: `edit_time`, `n_pause_geq_300`, `len_pause_geq_300`, `n_pause_geq_1000`, and `len_pause_geq_1000`.

### Dataset Creation

The dataset was parsed from PET XML files into CSV format using a script adapted from the one by [Antonio Toral](https://research.rug.nl/en/persons/antonio-toral-ruiz) found at the following link: [https://github.com/antot/postediting_novel_frontiers](https://github.com/antot/postediting_novel_frontiers)

## Additional Information

### Dataset Curators

For problems related to this 🤗 Datasets version, please contact us at [ik-nlp-course@rug.nl](mailto:ik-nlp-course@rug.nl).

### Licensing Information

It is forbidden to share or publish the data associated with this 🤗 Dataset version.

### Citation Information

No citation information is provided for this dataset.