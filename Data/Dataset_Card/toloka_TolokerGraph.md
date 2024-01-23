---
license: cc-by-4.0
tags:
- toloka
- graph
- node-classification
pretty_name: Graph of Crowd Annotators
size_categories:
- 10K<n<100K
task_categories:
- graph-ml
dataset_info:
  features:
  - name: id
    dtype: int32
  - name: approved_rate
    dtype: float
  - name: skipped_rate
    dtype: float
  - name: expired_rate
    dtype: float
  - name: rejected_rate
    dtype: float
  - name: education
    dtype: string
  - name: english_profile
    dtype: bool
  - name: english_tested
    dtype: bool
  - name: banned
    dtype: bool
---
# Toloker Graph: Interaction of Crowd Annotators

## Dataset Description

- **Repository:** https://github.com/Toloka/TolokerGraph
- **Point of Contact:** research@toloka.ai

### Dataset Summary

This repository contains a graph representing interactions between crowd annotators on a project labeled on the [Toloka](https://toloka.ai/) crowdsourcing platform (see the [Toloka overview](https://toloka.ai/en/docs/guide/concepts/overview) for the details on the used terminology).

The graph contains 11,758 nodes and 519,000 edges. Each node represents an individual annotator; nodes are provided with four numerical and three categorical features. An edge is drawn between a pair of annotators if they annotated the same task. Also, each node is provided with a label showing whether the annotator was banned on this project, or not.

### Nodes

Nodes are stored in the [nodes.tsv](nodes.tsv) file in the TSV format of the following structure:

- `id`: unique identifier of the annotator
- `approved_rate`: percentage of the approved labels of this annotator
- `skipped_rate`: percentage of the skipped tasks of this annotator
- `expired_rate`: percentage of the expired tasks of this annotator
- `rejected_rate`: percentage of the rejected labels of this annotator
- `education`: level of education as self-reported by this annotator (`none`, `basic`, `middle`, `high`)
- `english_profile`: knowledge of English as self-reported by this annotator (`0` for no, `1` for yes)
- `english_tested`: whether the annotator passed the Toloka language test for English (`0` for no, `1` for yes)
- `banned`: whether the annotator was banned on this project (`0` for no, `1` for yes)

The `*_rate` attributes should sum up to 1.

### Edges

Edges are stored in the [edges.tsv](edges.tsv) file in the TSV format of the following structure:

- `source`: source identifier of the annotator
- `target`: target identifier of the annotator

As the graph is undirected, `source` and `target` can be interchanged for the given pair of nodes.

### Citation

* Likhobaba, D., Pavlichenko, N., Ustalov, D. (2023). [Toloker Graph: Interaction of Crowd Annotators](https://doi.org/10.5281/zenodo.7620795). Zenodo. <https://doi.org/10.5281/zenodo.7620795>

```bibtex
@dataset{Tolokers,
  author     = {Likhobaba, Daniil and Pavlichenko, Nikita and Ustalov, Dmitry},
  title      = {{Toloker Graph: Interaction of Crowd Annotators}},
  year       = {2023},
  publisher  = {Zenodo},
  doi        = {10.5281/zenodo.7620795},
  url        = {https://github.com/Toloka/TolokerGraph},
  language   = {english},
}
```

### Copyright

Licensed under the Creative Commons Attribution 4.0 License. See LICENSE file for more details.
