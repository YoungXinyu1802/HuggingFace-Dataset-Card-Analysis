---
annotations_creators: []
language_creators:
- crowdsourced
language: ["en","code"]
multilinguality:
- multilingual
size_categories:
- unknown
source_datasets: []
task_categories:
- text-generation
task_ids:
- language-modeling

---

## Dataset Description

A small subset in each dataset of `pile-v2`(~1000 samples) of [pile-v2]() dataset, each has 1,000 random samples from the original dataset. The dataset has 255MB of text (code and english).


## Languages
The dataset contains technical text on programming languages and natural language with the following subsets,
- Bible 
- TED2020
- PileOfLaw
- StackExchange
- GithubIssues
- Opensubtitles
- USPTO
- S2ORC
- DevDocs
- CodePileReddit2022
- USENET
- GNOME
- ASFPublicMail
- PileV2Reddit2020
- CodePilePosts
- Discourse
- Tanzil
- arXiv
- UbuntuIRC
- PubMed
- CodePileReddit2020
- CodePileReddit2021
- GlobalVoices
- FreeLaw_Options
- PileV2Posts

## Dataset Structure

```python
from datasets import load_dataset
load_dataset("CarperAI/pile-v2-small")
```
### How to use it
You can either load the whole dataset like above, or load a specific subset such as arxiv by specifying the folder directory:
```python
load_dataset("CarperAI/pile-v2-small", data_dir="data/arxiv")
```

