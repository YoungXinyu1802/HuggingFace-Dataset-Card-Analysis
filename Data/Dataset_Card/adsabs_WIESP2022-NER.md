---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: 'WIESP2022-NER'
size_categories:
- 1K<n<10K
source_datasets: []
task_categories:
- token-classification
task_ids:
- named-entity-recognition
---
# Dataset for the first <a href="https://ui.adsabs.harvard.edu/WIESP/" style="color:blue">Workshop on Information Extraction from Scientific Publications (WIESP/2022)</a>.


## Dataset Description
Datasets with text fragments from astrophysics papers, provided by the [NASA Astrophysical Data System](https://ui.adsabs.harvard.edu/) with manually tagged astronomical facilities and other entities of interest (e.g., celestial objects).  
Datasets are in JSON Lines format (each line is a json dictionary).  
The datasets are formatted similarly to the CONLL2003 format. Each token is associated with an NER tag. The tags follow the "B-" and "I-" convention from the [IOB2 syntax]("https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)")

Each entry consists of a dictionary with the following keys:
- `"unique_id"`: a unique identifier for this data sample. Must be included in the predictions.
- `"tokens"`: the list of tokens (strings) that form the text of this sample. Must be included in the predictions.
- `"ner_tags"`: the list of NER tags (in IOB2 format)

The following keys are not strictly needed by the participants:
- `"ner_ids"`: the pre-computed list of ids corresponding ner_tags, as given by the dictionary in ner_tags.json
- `"label_studio_id"`, `"section"`, `"bibcode"`: references for internal NASA/ADS use.

## Instructions for Workshop participants:
How to load the data using the Huggingface library:
 ```python
from datasets import load_dataset
dataset = load_dataset("adsabs/WIESP2022-NER")
 ```

How to load the data if you cloned the repository locally:  
(assuming `./WIESP2022-NER-DEV.jsonl` is in the current directory, change as needed)
- python (as list of dictionaries):
```python
import json
with open("./WIESP2022-NER-DEV.jsonl", 'r') as f:
    wiesp_dev_json = [json.loads(l) for l in list(f)]
```
 - into Huggingface (as a Huggingface Dataset):
```python
from datasets import Dataset
wiesp_dev_from_json = Dataset.from_json(path_or_paths="./WIESP2022-NER-DEV.jsonl")
```


How to compute your scores on the training data:
1. format your predictions as a list of dictionaries, each with the same `"unique_id"` and `"tokens"` keys from the dataset, as well as the list of predicted NER tags under the `"pred_ner_tags"` key (see `WIESP2022-NER-DEV-sample-predictions.jsonl` for an example).
2. pass the references and predictions datasets to the `compute_MCC()` and `compute_seqeval()` functions (from the `.py` files with the same names).

Requirement to run the scoring scripts:  
[NumPy](https://numpy.org/install/)  
[scikit-learn](https://scikit-learn.org/stable/install.html)  
[seqeval](https://github.com/chakki-works/seqeval#installation)

To get scores on the validation data, zip your predictions file (a single `.jsonl' file formatted following the same instructions as above) and upload the `.zip` file to the [Codalabs](https://codalab.lisn.upsaclay.fr/competitions/5062) competition.

## File list
```
├── WIESP2022-NER-TRAINING.jsonl : 1753 samples for training.
├── WIESP2022-NER-DEV.jsonl : 20 samples for development.
├── WIESP2022-NER-DEV-sample-predictions.jsonl : an example file with properly formatted predictions on the development data.
├── WIESP2022-NER-VALIDATION-NO-LABELS.jsonl : 1366 samples for validation without the NER labels. Used for the WIESP2022 workshop.
├── WIESP2022-NER-VALIDATION.jsonl : 1366 samples for validation
├── WIESP2022-NER-TESTING-NO-LABELS.jsonl : 2505 samples for testing without the NER labels. Used for the WIESP2022 workshop.
├── WIESP2022-NER-TESTING.jsonl : 2505 samples for testing
├── README.MD : this file.
├── tag_definitions.md : short descriptions and examples of the tags used in the task.
└── scoring-scripts/ : scripts used to evaluate submissions.
    ├── compute_MCC.py : computes the Matthews correlation coefficient between two datasets.
    └── compute_seqeval.py : computes the seqeval scores (precision, recall, f1, overall and for each class) between two datasets.
```