---
annotations_creators:
- no-annotation
language:
- en
language_creators:
- found
license:
- cc0-1.0
multilinguality:
- monolingual
pretty_name: Gutenberg Poetry Corpus
size_categories:
- 1M<n<10M
source_datasets: []
tags:
- poetry
- stylistics
- poems
- gutenberg
task_categories:
- text-generation
task_ids:
- language-modeling
---

# Allison Parrish's Gutenberg Poetry Corpus

This corpus was originally published under the CC0 license by [Allison Parrish](https://www.decontextualize.com/). Please visit Allison's fantastic [accompanying GitHub repository](https://github.com/aparrish/gutenberg-poetry-corpus) for usage inspiration as well as more information on how the data was mined, how to create your own version of the corpus, and examples of projects using it.

This dataset contains 3,085,117 lines of poetry from hundreds of Project Gutenberg books. Each line has a corresponding `gutenberg_id` (1191 unique values) from project Gutenberg.

```python
Dataset({
    features: ['line', 'gutenberg_id'],
    num_rows: 3085117
})
```
A row of data looks like this:
```python
{'line': 'And retreated, baffled, beaten,', 'gutenberg_id': 19}
```
