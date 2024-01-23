---
dataset_info:
  features:
  - name: shorturl
    dtype: string
  - name: title
    dtype: string
  - name: pubinfo
    dtype: string
  - name: preamble
    sequence: string
  - name: toc
    list:
    - name: content_title
      dtype: string
    - name: sub_toc
      sequence: string
  - name: main_text
    list:
    - name: main_content
      sequence: string
    - name: section_title
      dtype: string
    - name: subsections
      list:
      - name: content
        sequence: string
      - name: subsection_title
        dtype: string
  - name: bibliography
    sequence: string
  - name: related_entries
    list:
    - name: href
      dtype: string
    - name: text
      dtype: string
  splits:
  - name: train
    num_bytes: 160405734
    num_examples: 1776
  download_size: 90000475
  dataset_size: 160405734
---
# Dataset Card for "stanford_plato"

## Description

This is a collection of articles in the Stanford Encyclopedia of Philosophy (https://plato.stanford.edu/index.html).

This dataset includes 1776 articles, each explaining one philosophy term/people/topic. It has 8 features:

- shorturl: The shorturl for the article. For example, the shorturl 'abduction' correspond to the page https://plato.stanford.edu/entries/abduction/
- title: The title of the article.
- pubinfo: The publication information.
- **preamble**: The preface text of the article. The data is a list, each item of the list is a paragraph of the data. I choose not to break the paragraph structure. Certainly, you can merge them by, for example, ''.join(data['preamble'])
- toc: Table of contents. Also represented as list. Each item is a dictionary, the 'content_title' is the main content title, and the 'sub_toc' is a list of subcontent titles.
- **main_text**: The main text of the article.
  The data is also a list, each item represents a section of the article.
  Each item is a dictionary, 'section_title' is the title of the section, 'main_content' is a list of paragraphs before subsections,
  'subsections' is a list of subsections, each item is also a dictionary, has its own title 'subsection_title' and list of paragraphs 'content'.
- bibliography: list of bibliography.
- related_entries: list of entries related to the current entry.

## Copyright and license

See the information at the offical website: https://plato.stanford.edu/info.html#c
This is not an official release. May be deleted later if violates copyright. The responsibility of not abusing is on the user.
