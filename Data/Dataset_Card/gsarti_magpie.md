---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
- text2text-generation
- translation
task_ids: []
pretty_name: magpie
tags:
- idiomaticity-classification
---

# Dataset Card for MAGPIE

## Table of Contents

- [Dataset Card for MAGPIE](#dataset-card-for-itacola)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Splits](#data-splits)
    - [Dataset Creation](#dataset-creation)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)

## Dataset Description

- **Original Repository:** [hslh/magpie-corpus](https://github.com/hslh/magpie-corpus)
- **Other Repository:** [vernadankers/mt_idioms](https://github.com/vernadankers/mt_idioms)
- **Original Paper:** [ACL Anthology](https://aclanthology.org/2020.lrec-1.35/)
- **Other Paper:** [ACL Anthology](https://aclanthology.org/2022.acl-long.252/)
- **Point of Contact:** [Hessel Haagsma, Verna Dankers](vernadankers@gmail.com)

### Dataset Summary

The MAGPIE corpus ([Haagsma et al. 2020](https://aclanthology.org/2020.lrec-1.35/)) is a large sense-annotated corpus of potentially idiomatic expressions (PIEs), based on the British National Corpus (BNC). Potentially idiomatic expressions are like idiomatic expressions, but the term also covers literal uses of idiomatic expressions, such as 'I leave work at the end of the day.' for the idiom 'at the end of the day'. This version of the dataset reflects the filtered subset used by [Dankers et al. (2022)](https://aclanthology.org/2022.acl-long.252/) in their investigation on how PIEs are represented by NMT models. Authors use 37k samples annotated as fully figurative or literal, for 1482 idioms that contain nouns, numerals or adjectives that are colors (which they refer to as keywords). Because idioms show syntactic and morphological variability, the focus is mostly put on nouns. PIEs and their context are separated using the original corpus’s word-level annotations.

### Languages

The language data in MAGPIE is in English (BCP-47 `en`)

## Dataset Structure

### Data Instances

The `magpie` configuration contains sentences with annotations for the presence, usage an type of potentially idiomatic expressions. An example from the `train` split of the `magpie` config (default) is provided below.

```json
{
    'sentence': 'There seems to be a dearth of good small tools across the board.',
    'annotation': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    'idiom': 'across the board',
    'usage': 'figurative',
    'variant': 'identical',
    'pos_tags': ['ADV', 'VERB', 'PART', 'VERB', 'DET', 'NOUN', 'ADP', 'ADJ', 'ADJ', 'NOUN', 'ADP', 'DET', 'NOUN']
}
```

The text is provided as-is, without further preprocessing or tokenization.

The fields are the following:

- `sentence`: The sentence containing a PIE.
- `annotation`: List of 0s and 1s of the same length of the whitespace-tokenized sentence, with 1s corresponding to the position of the idiomatic expression.
- `idiom`: The idiom contained in the sentence in its base form.
- `usage`: Either `figurative` or `literal`, depending on the usage of the PIE.
- `variant`: `identical` if the PIE matches the base form of the idiom, otherwise specifies the variation.
- `pos_tags`: List of POS tags associated with words in the sentence.

### Data Splits

|     config| train|
|----------:|-----:|
|`magpie`   | 44451 |

### Dataset Creation

Please refer to the original article [MAGPIE: A Large Corpus of Potentially Idiomatic Expressions](https://aclanthology.org/2020.lrec-1.35) for additional information on dataset creation, and to the article [Can Transformer be Too Compositional? Analysing Idiom Processing in Neural Machine Translation](https://aclanthology.org/2022.acl-long.252) for further information on the filtering of selected idioms.

## Additional Information

### Dataset Curators

The original authors are the curators of the original dataset. For problems or updates on this 🤗 Datasets version, please contact [gabriele.sarti996@gmail.com](mailto:gabriele.sarti996@gmail.com).

### Licensing Information

The dataset is licensed under [Creative Commons 4.0 license (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/)

### Citation Information

Please cite the authors if you use this corpus in your work:

```bibtex
@inproceedings{haagsma-etal-2020-magpie,
    title = "{MAGPIE}: A Large Corpus of Potentially Idiomatic Expressions",
    author = "Haagsma, Hessel  and
      Bos, Johan  and
      Nissim, Malvina",
    booktitle = "Proceedings of the 12th Language Resources and Evaluation Conference",
    month = may,
    year = "2020",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2020.lrec-1.35",
    pages = "279--287",
    language = "English",
    ISBN = "979-10-95546-34-4",
}
@inproceedings{dankers-etal-2022-transformer,
    title = "Can Transformer be Too Compositional? Analysing Idiom Processing in Neural Machine Translation",
    author = "Dankers, Verna  and
      Lucas, Christopher  and
      Titov, Ivan",
    booktitle = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.acl-long.252",
    doi = "10.18653/v1/2022.acl-long.252",
    pages = "3608--3626",
}
```
