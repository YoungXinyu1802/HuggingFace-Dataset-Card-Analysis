---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
pretty_name: ConceptNet with High Confidence
---
# Dataset Card for "relbert/conceptnet_high_confidence"
## Dataset Description
- **Repository:** [RelBERT](https://github.com/asahi417/relbert)
- **Paper:** [https://home.ttic.edu/~kgimpel/commonsense.html](https://home.ttic.edu/~kgimpel/commonsense.html)
- **Dataset:** High Confidence Subset of ConceptNet

### Dataset Summary
The selected subset of ConceptNet used in [this work](https://home.ttic.edu/~kgimpel/commonsense.html), which compiled 
to fine-tune [RelBERT](https://github.com/asahi417/relbert) model.

## Dataset Structure
### Data Instances
An example of `train` looks as follows.
```
{
    "relation_type": "AtLocation",
    "positives": [["fish", "water"], ["cloud", "sky"], ["child", "school"], ... ],
    "negatives": [["pen", "write"], ["sex", "fun"], ["soccer", "sport"], ["fish", "school"], ... ]
}
```

### Data Splits
|  name   |train|validation|
|---------|----:|---------:|
|conceptnet_high_confidence| 25 |      24|

### Number of Positive/Negative Word-pairs in each Split

| relation_type    |   positive (train) |   negative (train) |   positive (validation) |   negative (validation) |
|:-----------------|-------------------:|-------------------:|------------------------:|------------------------:|
| AtLocation       |                383 |               1768 |                      97 |                     578 |
| CapableOf        |                195 |               1790 |                      73 |                     600 |
| Causes           |                 71 |               1797 |                      26 |                     595 |
| CausesDesire     |                  9 |               1793 |                      11 |                     595 |
| CreatedBy        |                  2 |               1796 |                       0 |                       0 |
| DefinedAs        |                  0 |                  0 |                       2 |                     595 |
| Desires          |                 16 |               1794 |                      12 |                     595 |
| HasA             |                 67 |               1814 |                      17 |                     595 |
| HasFirstSubevent |                  2 |               1796 |                       0 |                       0 |
| HasLastSubevent  |                  2 |               1796 |                       3 |                     593 |
| HasPrerequisite  |                168 |               1803 |                      57 |                     592 |
| HasProperty      |                 94 |               1801 |                      39 |                     605 |
| HasSubevent      |                125 |               1798 |                      40 |                     609 |
| IsA              |                310 |               1764 |                      98 |                     603 |
| MadeOf           |                 17 |               1793 |                       7 |                     593 |
| MotivatedByGoal  |                 14 |               1796 |                      11 |                     595 |
| NotCapableOf     |                 15 |               1793 |                       0 |                       0 |
| NotDesires       |                  4 |               1795 |                       4 |                     592 |
| PartOf           |                 34 |               1801 |                       7 |                     593 |
| ReceivesAction   |                 18 |               1793 |                       8 |                     593 |
| SymbolOf         |                  0 |                  0 |                       2 |                     596 |
| UsedFor          |                249 |               1815 |                      81 |                     588 |
| SUM              |               1795 |              35896 |                     595 |                   11305 |

### Citation Information
```
@InProceedings{P16-1137,
  author = 	"Li, Xiang
		and Taheri, Aynaz
		and Tu, Lifu
		and Gimpel, Kevin",
  title = 	"Commonsense Knowledge Base Completion",
  booktitle = 	"Proceedings of the 54th Annual Meeting of the Association for      Computational Linguistics (Volume 1: Long Papers)    ",
  year = 	"2016",
  publisher = 	"Association for Computational Linguistics",
  pages = 	"1445--1455",
  location = 	"Berlin, Germany",
  doi = 	"10.18653/v1/P16-1137",
  url = 	"http://aclweb.org/anthology/P16-1137"
}
```