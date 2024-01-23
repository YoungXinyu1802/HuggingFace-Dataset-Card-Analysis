---
tags:
- python
- code
---

# CodeParrot 🦜 Dataset

## What is it?

This is the full CodeParrot dataset. It contains Python files used to train the code generation model in Chapter 10: Training Transformers from Scratch in the [NLP with Transformers book](https://learning.oreilly.com/library/view/natural-language-processing/9781098103231/). You can find the full code in the accompanying [Github repository](https://github.com/nlp-with-transformers/notebooks/blob/main/10_transformers-from-scratch.ipynb).

## Creation

It was created with the GitHub dataset available via Google's BigQuery. It contains approximately 22 million Python files and is 180 GB (50 GB compressed) big. The SQL query to create the dataset is the following:

```sql
SELECT
  f.repo_name, f.path, c.copies, c.size, c.content, l.license
FROM
  `bigquery-public-data.github_repos.files` AS f
JOIN
  `bigquery-public-data.github_repos.contents` AS c
ON
  f.id = c.id
JOIN
  `bigquery-public-data.github_repos.licenses` AS l
ON
  f.repo_name = l.repo_name 
WHERE
  NOT c.binary
    AND ((f.path LIKE '%.py')
      AND (c.size BETWEEN 1024 AND 1048575))
```

## Duplication
Note that about 70% of the dataset is duplicated. If you use the dataset make sure to deal with them appropriately. See [codeparrot-clean](https://huggingface.co/datasets/lvwerra/codeparrot-clean) for a deduplicated version of this dataset.