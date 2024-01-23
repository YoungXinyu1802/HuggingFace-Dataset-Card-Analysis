---
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets: []
---

# Dataset Card for quoteli3

## Dataset Description

- **Homepage:** https://nlp.stanford.edu/~muzny/quoteli.html
- **Repository:** https://nlp.stanford.edu/~muzny/quoteli.html
- **Paper:** Muzny, Grace, et al. "A two-stage sieve approach for quote attribution." Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 1, Long Papers. 2017.

### Dataset Summary 

This dataset is based on the quoteli3 dataset by Muzny et al. (2017). It contains annotated quotes for three pieces of literature: Chekhov\\\\\\\\\\\\'s The Steppe, Austen\\\\\\\\\\\\'s Emma and Pride and Prejudice.

### Languages

The text in the dataset is English.

## Dataset Structure

Training data: 
-Quotes (1575, 11)
-Characters (32, 6)

Test data:
-Quotes (1513, 11)
-Characters (145, 6)

### Data Splits
-Quotes:
  - train:
    - features: ['mention', 'oid', 'speaker', 'connection', 'id', 'answer', 'answer_mention {'answer', 'answer_start', 'answer_end', 'answer_in_context'}, 'question', 'context', 'large_context', 'book_title'],
    - num_rows: 1575
  - test:
    - features: ['mention', 'oid', 'speaker', 'connection', 'id', 'answer', 'answer_mention {'answer', 'answer_start', 'answer_end', 'answer_in_context'}, 'question', 'context', 'large_context', 'book_title'],
    - num_rows: 1513
-Characters:
  - train:
    - features: ['aliases', 'description', 'gender', 'name', 'id', 'book_title'],
    - num_rows: 32
  - test:
    - features: ['aliases', 'description', 'gender', 'name', 'id', 'book_title'],
    - num_rows: 146