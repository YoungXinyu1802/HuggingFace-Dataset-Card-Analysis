---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name: CoNLL-2003
---

# Dataset Card for "tner/conll2003"

## Dataset Description

- **Repository:** [T-NER](https://github.com/asahi417/tner)
- **Paper:** [https://www.aclweb.org/anthology/W03-0419/](https://www.aclweb.org/anthology/W03-0419/)
- **Dataset:** CoNLL 2003
- **Domain:** News
- **Number of Entity:** 3


### Dataset Summary
CoNLL-2003 NER dataset formatted in a part of [TNER](https://github.com/asahi417/tner) project.
- Entity Types: `ORG`, `PER`, `LOC`, `MISC`
## Dataset Structure

### Data Instances
An example of `train` looks as follows.

```
{
  'tags': ['SOCCER','-', 'JAPAN', 'GET', 'LUCKY', 'WIN', ',', 'CHINA', 'IN', 'SURPRISE', 'DEFEAT', '.'],
  'tokens': [0, 0, 5, 0, 0, 0, 0, 3, 0, 0, 0, 0]
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/conll2003/raw/main/dataset/label.json).
```python
{
  "O": 0,
  "B-ORG": 1,
  "B-MISC": 2,
  "B-PER": 3,
  "I-PER": 4,
  "B-LOC": 5,
  "I-ORG": 6,
  "I-MISC": 7,
  "I-LOC": 8
}
```

### Data Splits

|  name   |train|validation|test|
|---------|----:|---------:|---:|
|conll2003|14041|      3250|3453|

### Licensing Information

From the [CoNLL2003 shared task](https://www.clips.uantwerpen.be/conll2003/ner/) page:

> The English data is a collection of news wire articles from the Reuters Corpus. The annotation has been done by people of the University of Antwerp. Because of copyright reasons we only make available the annotations. In order to build the complete data sets you will need access to the Reuters Corpus. It can be obtained for research purposes without any charge from NIST.

The copyrights are defined below, from the [Reuters Corpus page](https://trec.nist.gov/data/reuters/reuters.html):

> The stories in the Reuters Corpus are under the copyright of Reuters Ltd and/or Thomson Reuters, and their use is governed by the following agreements:
>
> [Organizational agreement](https://trec.nist.gov/data/reuters/org_appl_reuters_v4.html)
>
> This agreement must be signed by the person responsible for the data at your organization, and sent to NIST.
>
> [Individual agreement](https://trec.nist.gov/data/reuters/ind_appl_reuters_v4.html)
>
> This agreement must be signed by all researchers using the Reuters Corpus at your organization, and kept on file at your organization.

### Citation Information

```
@inproceedings{tjong-kim-sang-de-meulder-2003-introduction,
    title = "Introduction to the {C}o{NLL}-2003 Shared Task: Language-Independent Named Entity Recognition",
    author = "Tjong Kim Sang, Erik F. and De Meulder, Fien",
    booktitle = "Proceedings of the Seventh Conference on Natural Language Learning at {HLT}-{NAACL} 2003",
    year = "2003",
    url = "https://www.aclweb.org/anthology/W03-0419",
    pages = "142--147",
}
```