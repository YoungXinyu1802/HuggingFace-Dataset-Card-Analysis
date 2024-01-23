---
dataset_info:
  features:
  - name: _id
    dtype: int64
  - name: title
    dtype: string
  - name: author
    dtype: string
  - name: url
    dtype: string
  - name: summary
    dtype: string
  splits:
  - name: train
    num_bytes: 1881481
    num_examples: 3420
  download_size: 1080975
  dataset_size: 1881481
---
# Dataset Card for "poetry-summary"

This dataset contains scraped poem summarizations. Poems in this dataset also appear in [isaacrehg/poetry-detailed-analysis](https://huggingface.co/datasets/isaacrehg/poetry-detailed-analysis).

Each row contains the following data:

- _id: ID of this poem (for reference in [isaacrehg/poetry-detailed-analysis](https://huggingface.co/datasets/isaacrehg/poetry-detailed-analysis))
- title: The title of the poem
- author: The poem's author
- summary: The crawled summarization for this poem
