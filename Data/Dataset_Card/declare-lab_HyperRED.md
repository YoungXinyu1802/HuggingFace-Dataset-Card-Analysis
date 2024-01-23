---
license: cc-by-sa-3.0
---

# Dataset Card for HyperRED

## Description

- **Repository:** https://github.com/declare-lab/HyperRED
- **Paper (EMNLP 2022):** https://arxiv.org/abs/2211.10018

### Summary

HyperRED is a dataset for the new task of hyper-relational extraction, which extracts relation triplets together with qualifier information such as time, quantity or location. For example, the relation triplet (Leonard Parker, Educated At, Harvard University) can be factually enriched by including the qualifier (End Time, 1967). HyperRED contains 44k sentences with 62 relation types and 44 qualifier types.

### Languages

English.

## Dataset Structure

### Data Fields

- **tokens:** Sentence text tokens.
- **entities:** List of each entity span. The span indices correspond to each token in the space-separated text (inclusive-start and exclusive-end index)
- **relations:** List of each relationship label between the head and tail entity spans. Each relation contains a list of qualifiers where each qualifier has the value entity span and qualifier label.

### Data Instances

An example instance of the dataset is shown below:

```
{              
  "tokens": ['Acadia', 'University', 'is', 'a', 'predominantly', 'undergraduate', 'university', 'located', 'in', 'Wolfville', ',', 'Nova', 'Scotia', ',', 'Canada', 'with', 'some', 'graduate', 'programs', 'at', 'the', 'master', "'", 's', 'level', 'and', 'one', 'at', 'the', 'doctoral', 'level', '.'],
  "entities": [
    {'span': (0, 2), 'label': 'Entity'},
    {'span': (9, 13), 'label': 'Entity'},
    {'span': (14, 15), 'label': 'Entity'},
  ],
  "relations": [
    {
      "head": [0, 2],
      "tail": [9, 13],
      "label": "headquarters location",
      "qualifiers": [
        {"span": [14, 15], "label": "country"}
      ]
    }
  ], 
}
 ```

### Data Splits

The dataset contains 39,840 instances for training, 1,000 instances for validation and 4,000 instances for testing.

### Dataset Creation

The dataset is constructed from distant supervision between Wikipedia and Wikidata, and the human annotation process is detailed in the paper.

## Citation Information

```
@inproceedings{chia2022hyperred,
  title={A Dataset for Hyper-Relational Extraction and a Cube-Filling Approach},
  author={Yew Ken Chia, Lidong Bing, Sharifah Mahani Aljunied, Luo Si and Soujanya Poria},
  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
  year={2022}
}
```