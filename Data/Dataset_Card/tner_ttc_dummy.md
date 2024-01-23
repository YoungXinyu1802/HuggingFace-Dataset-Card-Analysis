---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- 1k<10K
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name: TTC
---

# Dataset Card for "tner/ttc" (Dummy)

***WARNING***: This is a dummy dataset for `ttc` and the correct one is [`tner/ttc`](https://huggingface.co/datasets/tner/ttc), which is private since **TTC dataset is not publicly released at this point**. We will grant you an access to the `tner/ttc` dataset, once you retained the original dataset from the authors (you need to send an inquiry to Shruti Rijhwani, `srijhwan@cs.cmu.edu`). See their repository for more detail [https://github.com/shrutirij/temporal-twitter-corpus](https://github.com/shrutirij/temporal-twitter-corpus).
Once you are granted access to the original TTC dataset by the author, please request the access at [here](https://huggingface.co/datasets/tner/ttc_dummy/discussions/1).

## Dataset Description

- **Repository:** [T-NER](https://github.com/asahi417/tner)
- **Paper:** [https://aclanthology.org/2020.acl-main.680/](https://aclanthology.org/2020.acl-main.680/)
- **Dataset:** Temporal Twitter Corpus
- **Domain:** Twitter
- **Number of Entity:** 3


### Dataset Summary
Broad Twitter Corpus NER dataset formatted in a part of [TNER](https://github.com/asahi417/tner) project.
- Entity Types: `LOC`, `ORG`, `PER`

## Dataset Structure

### Data Instances
An example of `train` looks as follows.

```
{
    'tokens': ['😝', 'lemme', 'ask', '$MENTION$', ',', 'Timb', '???', '"', '$MENTION$', ':', '$RESERVED$', '!!!', '"', '$MENTION$', ':', '$MENTION$', 'Nezzzz', '!!', 'How', "'", 'bout', 'do', 'a', 'duet', 'with', '$MENTION$', '??!', ';)', '"'],
    'tags': [6, 6, 6, 6, 6, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/btc/raw/main/dataset/label.json).
```python
{
    "B-LOC": 0,
    "B-ORG": 1,
    "B-PER": 2,
    "I-LOC": 3,
    "I-ORG": 4,
    "I-PER": 5,
    "O": 6
}
```

### Data Splits

|  name   |train|validation|test|
|---------|----:|---------:|---:|
|ttc      | 9995|       500|1477|

### Citation Information

```
@inproceedings{rijhwani-preotiuc-pietro-2020-temporally,
    title = "Temporally-Informed Analysis of Named Entity Recognition",
    author = "Rijhwani, Shruti  and
      Preotiuc-Pietro, Daniel",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.acl-main.680",
    doi = "10.18653/v1/2020.acl-main.680",
    pages = "7605--7617",
    abstract = "Natural language processing models often have to make predictions on text data that evolves over time as a result of changes in language use or the information described in the text. However, evaluation results on existing data sets are seldom reported by taking the timestamp of the document into account. We analyze and propose methods that make better use of temporally-diverse training data, with a focus on the task of named entity recognition. To support these experiments, we introduce a novel data set of English tweets annotated with named entities. We empirically demonstrate the effect of temporal drift on performance, and how the temporal information of documents can be used to obtain better models compared to those that disregard temporal information. Our analysis gives insights into why this information is useful, in the hope of informing potential avenues of improvement for named entity recognition as well as other NLP tasks under similar experimental setups.",
}
```