---
dataset_info:
  features:
  - name: TEXT
    dtype: string
  - name: SOURCE
    dtype: string
  - name: META
    dtype: string
  splits:
  - name: train
    num_bytes: 3127637884
    num_examples: 7907
  download_size: 1911478917
  dataset_size: 3127637884
license: mit
task_categories:
- text-generation
language:
- es
- de
- fr
- nl
- it
- pt
- hu
tags:
- project gutenberg
- e-book
- gutenberg.org
pretty_name: Project Gutenberg eBooks in different languages
size_categories:
- 1K<n<10K
---
# Dataset Card for Project Gutenber - Multilanguage eBooks

A collection of non-english language eBooks (7907, about 75-80% of all the ES, DE, FR, NL, IT, PT, HU books available on the site) from the Project Gutenberg site with metadata removed. 

Originally colected for https://github.com/LAION-AI/Open-Assistant

| LANG | EBOOKS |
|----|----|
| ES | 717 |
| DE | 1735 |
| FR | 2863 |
| NL | 904 |
| IT | 692 |
| PT | 501 |
| HU | 495 |

The METADATA column contains catalogue meta information on each book as a serialized JSON:

| key | original column |
|----|----|
| language | - |
| text_id | Text# unique book identifier on Prject Gutenberg as *int* |
| title | Title of the book as *string* |
| issued | Issued date as *string* |
| authors | Authors as *string*, comma separated sometimes with dates |
| subjects | Subjects as *string*, various formats |
| locc | LoCC code as *string* |
| bookshelves | Bookshelves as *string*, optional |

## Source data

**How was the data generated?**

- A crawler (see Open-Assistant repository) downloaded the raw HTML code for 
  each eBook based on **Text#** id in the Gutenberg catalogue (if available)
- The metadata and the body of text are not clearly separated so an additional
  parser attempts to split them, then remove transcriber's notes and e-book 
  related information from the body of text (text clearly marked as copyrighted or 
  malformed was skipped and not collected)
- The body of cleaned TEXT as well as the catalogue METADATA is then saved as
  a parquet file, with all columns being strings

**Copyright notice:**

- Some of the books are copyrighted! The crawler ignored all books
  with an english copyright header by utilizing a regex expression, but make
  sure to check out the metadata for each book manually to ensure they are okay
  to use in your country! More information on copyright:
  https://www.gutenberg.org/help/copyright.html and
  https://www.gutenberg.org/policy/permission.html
- Project Gutenberg has the following requests when using books without
  metadata: _Books obtianed from the Project Gutenberg site should have the
  following legal note next to them: "This eBook is for the use of anyone
  anywhere in the United States and most other parts of the world at no cost and
  with almost" no restrictions whatsoever. You may copy it, give it away or
  re-use it under the terms of the Project Gutenberg License included with this
  eBook or online at www.gutenberg.org. If you are not located in the United
  States, you will have to check the laws of the country where you are located
  before using this eBook."_

