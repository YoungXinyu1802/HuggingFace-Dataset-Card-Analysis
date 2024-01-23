---
annotations_creators: []
language_creators:
- crowdsourced
- expert-generated
language:
- code
license:
- other
multilinguality:
- muonolingual
size_categories:
- unknown
source_datasets: []
task_categories:
- text-generation
task_ids:
- language-modeling
---

# GitHub Jupyter Dataset

## Dataset Description
This is a parsed and preprocessed version of [GitHub-Jupyter Dataset](https://huggingface.co/datasets/codeparrot/github-jupyter), a dataset extracted from Jupyter Notebooks on BigQuery. We only keep markdown and python cells and convert the markdown to text. Some heuristics are also applied to filter notebooks with little data and very long or very short cells. 


## Licenses
Each example has the license of its associated repository. There are in total 15 licenses:
```python
[
  'mit',
  'apache-2.0',
  'gpl-3.0',
  'gpl-2.0',
  'bsd-3-clause',
  'agpl-3.0',
  'lgpl-3.0',
  'lgpl-2.1',
  'bsd-2-clause',
  'cc0-1.0',
  'epl-1.0',
  'mpl-2.0',
  'unlicense',
  'isc',
  'artistic-2.0'
 ]
```
