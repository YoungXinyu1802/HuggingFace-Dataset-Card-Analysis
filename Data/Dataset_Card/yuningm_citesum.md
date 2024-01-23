---
language:
- en
license: cc-by-nc-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- summarization
paperswithcode_id: citesum
---

# CiteSum

## Description

CiteSum: Citation Text-guided Scientific Extreme Summarization and Low-resource Domain Adaptation.  

CiteSum contains TLDR summaries for scientific papers from their citation texts without human annotation, making it around 30 times larger than the previous human-curated dataset SciTLDR.
## Homepage
https://github.com/morningmoni/CiteSum

## Paper
https://arxiv.org/abs/2205.06207

## Authors

### Yuning Mao, Ming Zhong, Jiawei Han
#### University of Illinois Urbana-Champaign  
{yuningm2, mingz5, hanj}@illinois.edu


## Dataset size

Train: 83304  
Validation: 4721  
Test: 4921  

## Data details

- src (string): source text. long description of paper
- tgt (string): target text. tldr of paper
- paper_id (string): unique id for the paper
- title (string): title of the paper
- discipline (dict): 
  - venue (string): Where the paper was published (conference)
  - journal (string): Journal in which the paper was published
  - mag_field_of_study (list[str]): scientific fields that the paper falls under.

Example:

```
{
    'src': 'We describe a convolutional neural network that learns feature representations for short textual posts using hashtags as a supervised signal. The proposed approach is trained on up to 5.5 billion words predicting 100,000 possible hashtags. As well as strong performance on the hashtag prediction task itself, we show that its learned representation of text (ignoring the hashtag labels) is useful for other tasks as well. To that end, we present results on a document recommendation task, where it also outperforms a number of baselines.',

    'tgt': 'A convolutional neural network model for predicting hashtags was proposed in REF .',

    'paper_id': '14697143',

    'title': '#TagSpace: Semantic Embeddings from Hashtags',

    'discipline': {
        'venue': 'EMNLP',
        'journal': None,
        'mag_field_of_study': ['Computer Science']
        }
}
  ```


## Using the dataset

```python
from datasets import load_dataset

ds = load_dataset("yuningm/citesum")
```

## Data location
https://drive.google.com/file/d/1ndHCREXGSPnDUNllladh9qCtayqbXAfJ/view
