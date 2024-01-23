---
language:
- en
size_categories:
- 1K<n<10K
---
# Dataset Card for KGEditor

## Dataset Description

- **Homepage:**
- **Repository:** 
- **Paper:** [https://arxiv.org/abs/2301.10405](https://arxiv.org/abs/2301.10405)
- **Leaderboard:** [https://zjunlp.github.io/project/KGE_Editing/](https://zjunlp.github.io/project/KGE_Editing/)
- **Point of Contact:** 

### Supported Tasks and Leaderboards

The purpose of the KGE Edit task is to modify the erroneous knowledge in the KGE model and to inject new knowledge into the KGE model. Thus, in response to the task objectives, we design two subtasks (EDIT & ADD). For the EDIT sub-task, we edit the wrong fact knowledge that is stored in the KG embeddings. Also, for the ADD sub-task, we add brand-new knowledge into the model without re-training the whole model.

### Dataset Summary

We build four datasets for the sub-task of EDIT and ADD based on two benchmark datasets FB15k-237, and WN18RR. Firstly, we train KG embedding models with language models. For EDIT task, we sample some hard triples as candidates following the procedure below. For the ADD sub-task, we leverage the original training set of FB15k-237 and WN18RR to build the pre-train dataset (original pre-train data) and use the data from the standard inductive setting as they are not seen before.

## Dataset Structure

### Data Instances

An example of E-FB15k237:
(Note that we have converted the ID to text for easier understanding)

```
{
  "ori": ["Jennifer Connelly", "type of union", "Marriage"],
  "cor": ["Stephen Sondheim", "type of union", "Marriage"],
  "process": ["[MASK]", "type of union", "Marriage"],
  "label": "Jennifer Connelly"
}
```

An example of A-FB15k237:

```
{
  "triples": ["Darryl F. Zanuck", "place of death", "Palm Springs"],
  "label": "Palm Springs",
  "head": 0
}
```

### Data Fields

The data fields are the same among all splits.
For EDIT sub-task:

- ori: the fact in the pre-train dataset.
- cor: corrupted triple.
- process: the triple after replacing the wrong entity with the [MASK] token.
- label: a classification label, the scope is the entire set of entities.

For ADD sub-task:

- triples: the knowledge that needs to be injected into the model.
- label: a classification label, the scope is the entire set of entities.
- head: the head or tail entity that does not appear in pre-train.
### Data Splits

<table>
  <tr>
    <th></th>
    <td>Pre-trained</td>
    <th>Train</th>
    <th>Test</th>
    <th>L-Test</th>
  </tr>
  <tr>
    <th>E-FB15k237</th>
    <td>310,117</td>
    <td>3,087</td>
    <td>3,087</td>
    <td>7,051</td>
  </tr>
  <tr>
    <th>A-FB15k237</th>
    <td>215,082</td>
    <td>2,000</td>
    <td>-</td>
    <td>16,872</td>
  </tr>
  <tr>
    <th>E-WN18RR</th>
    <td>93,003</td>
    <td>1,491</td>
    <td>1,401</td>
    <td>5,003</td>
  </tr>
  <tr>
    <th>A-WN18RR</th>
    <td>69,721</td>
    <td>2,000</td>
    <td>-</td>
    <td>10,000</td>
  </tr>
</table>

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

For the EDIT subtask, our data(E-FB15k237 and E-WN18RR) is based on the [FB15k237](https://paperswithcode.com/dataset/fb15k-237) and [WN18RR](https://paperswithcode.com/dataset/wn18rr).

For the ADD subtask, our data(A-FB15k237 and E-WN18RR) remain the same as the inductive settings in [paper](https://arxiv.org/abs/2010.03496).

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

```
@article{DBLP:journals/corr/abs-2301-10405,
  author    = {Siyuan Cheng and
               Ningyu Zhang and
               Bozhong Tian and
               Zelin Dai and
               Feiyu Xiong and
               Wei Guo and
               Huajun Chen},
  title     = {Editing Language Model-based Knowledge Graph Embeddings},
  journal   = {CoRR},
  volume    = {abs/2301.10405},
  year      = {2023},
  url       = {https://doi.org/10.48550/arXiv.2301.10405},
  doi       = {10.48550/arXiv.2301.10405},
  eprinttype = {arXiv},
  eprint    = {2301.10405},
  timestamp = {Thu, 26 Jan 2023 17:49:16 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2301-10405.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

### Contributions

[More Information Needed]