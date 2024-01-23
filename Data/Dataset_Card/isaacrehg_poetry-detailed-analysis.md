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
  - name: stanza_index
    dtype: int64
  - name: stanza_header
    dtype: string
  - name: content
    dtype: string
  - name: analysis
    dtype: string
  splits:
  - name: train
    num_bytes: 18347594
    num_examples: 14507
  download_size: 9751592
  dataset_size: 18347594
---
# Dataset Card for "poetry-detailed-analysis"

This dataset contains scraped per-stanza analyses. Poems in this dataset also appear in [isaacrehg/poetry-summary](https://huggingface.co/datasets/isaacrehg/poetry-summary).

Each row contains the following data:

- _id: ID of the poem (for reference in [isaacrehg/poetry-summary](https://huggingface.co/datasets/isaacrehg/poetry-summary))
- title: The title of the poem
- author: The poem's author
- url: URL scraped from analysis content where the full poem can be found (may be missing or incorrect)
- stanza_index: index for the section of the poem that this record pertains to
- stanza_header: natural language description of the pertinant stanza (ie. "Stanza One" or "Lines 10-16")
- content: poem content for this stanza (may be missing or partially ommited, ie. "Curling its coral feet, (…) Men long dead.")
- analysis: analysis of this stanza