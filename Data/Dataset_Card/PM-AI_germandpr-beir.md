---
annotations_creators: []
language:
- de
language_creators: []
license: []
multilinguality:
- monolingual
pretty_name: germandpr-beir
size_categories:
- 10K<n<100K
source_datasets: []
tags:
- information retrieval
- ir
- documents retrieval
- passage retrieval
- beir
- benchmark
- qrel
- sts
- semantic search
task_categories:
- sentence-similarity
- feature-extraction
- text-retrieval
- question-answering
- other
task_ids:
- document-retrieval
- open-domain-qa
- closed-domain-qa
viewer: true
---

# Dataset Card for germanDPR-beir

## Dataset Summary

This dataset can be used for [BEIR](https://arxiv.org/abs/2104.08663) evaluation based on [deepset/germanDPR](https://huggingface.co/datasets/deepset/germandpr).
It already has been used to evaluate a newly trained [bi-encoder model](https://huggingface.co/PM-AI/bi-encoder_msmarco_bert-base_german).
The benchmark framework requires a particular dataset structure by default which has been created locally and uploaded here.

Acknowledgement: The dataset was initially created as "[germanDPR](https://www.deepset.ai/germanquad)" by Timo Möller, Julian Risch, Malte Pietsch, Julian Gutsch, Tom Hersperger, Luise Köhler, Iuliia Mozhina, and Justus Peter, during work done at deepset.ai.
## Dataset Creation
First, the original dataset [deepset/germanDPR](https://huggingface.co/datasets/deepset/germandpr) was converted into three files for BEIR compatibility:
 - The first file is `queries.jsonl` and contains an ID and a question in each line.
 - The second file, `corpus.jsonl`, contains in each line an ID, a title, a text and some metadata.
 - In the `qrel` folder is the third file. It connects every question from `queries.json` (via `q_id`) with a relevant text/answer from `corpus.jsonl` (via `c_id`)
 
This process has been done for `train` and `test` split separately based on the original germanDPR dataset.
Approaching the dataset creation like that is necessary because queries AND corpus both differ in deepset's germanDPR dataset
and it might be confusion changing this specific split.
In conclusion, queries and corpus differ between train and test split and not only qrels data!
Note: If you want one big corpus use `datasets.concatenate_datasets()`.

In the original dataset, there is one passage containing the answer and three "wrong" passages for each question.
During the creation of this customized dataset, all four passages are added, but only if they are not already present (... meaning they have been deduplicated).

It should be noted, that BEIR is combining `title` + `text` in `corpus.jsonl` to a new string which may produce odd results:
The original germanDPR dataset does not always contain "classical" titles (i.e. short), but sometimes consists of whole sentences, which are also present in the "text" field.
This results in very long passages as well as duplications.
In addition, both title and text contain specially formatted content.
For example, the words used in titles are often connected with underscores:

> `Apple_Magic_Mouse`

And texts begin with special characters to distinguish headings and subheadings:

> `Wirtschaft_der_Vereinigten_Staaten\n\n== Verschuldung ==\nEin durchschnittlicher Haushalt (...)`

Line breaks are also frequently found, as you can see.

Of course, it depends on the application whether these things become a problem or not.
However, it was decided to release two variants of the original dataset:
- The `original` variant leaves the titles and texts as they are. There are no modifications.
- The `processed` variant removes the title completely and simplifies the texts by removing the special formatting.

The creation of both variants can be viewed in [create_dataset.py](https://huggingface.co/datasets/PM-AI/germandpr-beir/resolve/main/create_dataset.py).
In particular, the following parameters were used:
- `original`: `SPLIT=test/train, TEXT_PREPROCESSING=False, KEEP_TITLE=True`
- `processed`: `SPLIT=test/Train, TEXT_PREPROCESSING=True, KEEP_TITLE=False`

One final thing to mention: The IDs for queries and the corpus should not match!!!
During the evaluation using BEIR, it was found that if these IDs match, the result for that entry is completely removed. 
This means some of the results are missing.
A correct calculation of the overall result is no longer possible.
Have a look into [BEIR's evaluation.py](https://github.com/beir-cellar/beir/blob/c3334fd5b336dba03c5e3e605a82fcfb1bdf667d/beir/retrieval/evaluation.py#L49) for further understanding.

## Dataset Usage
As earlier mentioned, this dataset is intended to be used with the BEIR benchmark framework.
The file and data structure required for BEIR can only be used to a limited extent with Huggingface Datasets or it is necessary to define multiple dataset repositories at once.
To make it easier, the [dl_dataset.py](https://huggingface.co/datasets/PM-AI/germandpr-beir/tree/main/dl_dataset.py) script is provided to download the dataset and to ensure the correct file and folder structure.

```python
# dl_dataset.py
import json
import os

import datasets
from beir.datasets.data_loader import GenericDataLoader

# ----------------------------------------
# This scripts downloads the BEIR compatible deepsetDPR dataset from "Huggingface Datasets" to your local machine.
# Please see dataset's description/readme to learn more about how the dataset was created.
# If you want to use deepset/germandpr without any changes, use TYPE "original"
# If you want to reproduce PM-AI/bi-encoder_msmarco_bert-base_german, use TYPE "processed"
# ----------------------------------------


TYPE = "processed"  # or "original"
SPLIT = "train"  # or "train"
DOWNLOAD_DIR = "germandpr-beir-dataset"
DOWNLOAD_DIR = os.path.join(DOWNLOAD_DIR, f'{TYPE}/{SPLIT}')
DOWNLOAD_QREL_DIR = os.path.join(DOWNLOAD_DIR, f'qrels/')

os.makedirs(DOWNLOAD_QREL_DIR, exist_ok=True)

# for BEIR compatibility we need queries, corpus and qrels all together
# ensure to always load these three based on the same type (all "processed" or all "original")
for subset_name in ["queries", "corpus", "qrels"]:
    subset = datasets.load_dataset("PM-AI/germandpr-beir", f'{TYPE}-{subset_name}', split=SPLIT)
    if subset_name == "qrels":
        out_path = os.path.join(DOWNLOAD_QREL_DIR, f'{SPLIT}.tsv')
        subset.to_csv(out_path, sep="\t", index=False)
    else:
        if subset_name == "queries":
            _row_to_json = lambda row: json.dumps({"_id": row["_id"], "text": row["text"]}, ensure_ascii=False)
        else:
            _row_to_json = lambda row: json.dumps({"_id": row["_id"], "title": row["title"], "text": row["text"]}, ensure_ascii=False)

        with open(os.path.join(DOWNLOAD_DIR, f'{subset_name}.jsonl'), "w", encoding="utf-8") as out_file:
            for row in subset:
                out_file.write(_row_to_json(row) + "\n")


# GenericDataLoader is part of BEIR. If everything is working correctly we can now load the dataset
corpus, queries, qrels = GenericDataLoader(data_folder=DOWNLOAD_DIR).load(SPLIT)
print(f'{SPLIT} corpus size: {len(corpus)}\n'
      f'{SPLIT} queries size: {len(queries)}\n'
      f'{SPLIT} qrels: {len(qrels)}\n')

print("--------------------------------------------------------------------------------------------------------------\n"
      "Now you can use the downloaded files in BEIR framework\n"
      "Example: https://github.com/beir-cellar/beir/blob/v1.0.1/examples/retrieval/evaluation/dense/evaluate_sbert.py\n"
      "--------------------------------------------------------------------------------------------------------------")
```

Alternatively, the data sets can be downloaded directly:
- https://huggingface.co/datasets/PM-AI/germandpr-beir/resolve/main/data/original.tar.gz
- https://huggingface.co/datasets/PM-AI/germandpr-beir/resolve/main/data/processed.tar.gz

Now you can use the downloaded files in BEIR framework:
- For Example: [evaluate_sbert.py](https://github.com/beir-cellar/beir/blob/v1.0.1/examples/retrieval/evaluation/dense/evaluate_sbert.py)
- Just set variable `"dataset"` to `"germandpr-beir-dataset/processed/test"` or `"germandpr-beir-dataset/original/test"`.
- Same goes for `"train"`.

## Dataset Sizes
- Original **train** `corpus` size, `queries` size and `qrels` size: `24009`, `9275` and `9275`
- Original **test** `corpus` size, `queries` size and `qrels` size: `2876`, `1025` and `1025`

- Processed **train** `corpus` size, `queries` size and `qrels` size: `23993`, `9275` and `9275`
- Processed **test** `corpus` size, `queries` size and `qrels` size: `2875` and `1025` and `1025`

## Languages

This dataset only supports german (aka. de, DE).

## Acknowledgment

The dataset was initially created as "[deepset/germanDPR](https://www.deepset.ai/germanquad)" by Timo Möller, Julian Risch, Malte Pietsch, Julian Gutsch, Tom Hersperger, Luise Köhler, Iuliia Mozhina, and Justus Peter, during work done at [deepset.ai](https://www.deepset.ai/).

This work is a collaboration between [Technical University of Applied Sciences Wildau (TH Wildau)](https://en.th-wildau.de/) and [sense.ai.tion GmbH](https://senseaition.com/).
You can contact us via:
* [Philipp Müller (M.Eng.)](https://www.linkedin.com/in/herrphilipps); Author
* [Prof. Dr. Janett Mohnke](mailto:icampus@th-wildau.de); TH Wildau
* [Dr. Matthias Boldt, Jörg Oehmichen](mailto:info@senseaition.com); sense.AI.tion GmbH 

This work was funded by the European Regional Development Fund (EFRE) and the State of Brandenburg. Project/Vorhaben: "ProFIT: Natürlichsprachliche Dialogassistenten in der Pflege".

<div style="display:flex">
     <div style="padding-left:20px;">
          <a href="https://efre.brandenburg.de/efre/de/"><img src="https://huggingface.co/datasets/PM-AI/germandpr-beir/resolve/main/res/EFRE-Logo_rechts_oweb_en_rgb.jpeg" alt="Logo of European Regional Development Fund (EFRE)" width="200"/></a>
     </div>
     <div style="padding-left:20px;">
          <a href="https://www.senseaition.com"><img src="https://senseaition.com/wp-content/uploads/thegem-logos/logo_c847aaa8f42141c4055d4a8665eb208d_3x.png" alt="Logo of senseaition GmbH" width="200"/></a>
     </div>
     <div style="padding-left:20px;">
          <a href="https://www.th-wildau.de"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/TH_Wildau_Logo.png/640px-TH_Wildau_Logo.png" alt="Logo of TH Wildau" width="180"/></a>
     </div>
</div>