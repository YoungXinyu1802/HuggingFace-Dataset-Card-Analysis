---
annotations_creators:
  - no-annotation
language_creators:
  - found
language:
  - id
  - ms
source_datasets:
  - original
task_categories:
  - text2text-generation
task_ids:
  - g2p
paperswithcode_id: null
pretty_name: ID Word2Phoneme
---

# Dataset Card for ID Word2Phoneme

## Table of Contents

- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** [Github](https://github.com/open-dict-data/ipa-dict/blob/master/data/ma.txt)
- **Repository:** [Github](https://github.com/open-dict-data/ipa-dict/blob/master/data/ma.txt)
- **Point of Contact:**
- **Size of downloaded dataset files:**
- **Size of the generated dataset:**
- **Total amount of disk used:**

### Dataset Summary

Originally a [Malay/Indonesian Lexicon](https://github.com/open-dict-data/ipa-dict/blob/master/data/ma.txt) retrieved from [ipa-dict](https://github.com/open-dict-data/ipa-dict). We removed the accented letters (because Indonesian graphemes do not use accents), separated homographs, and removed backslashes in phonemes -- resulting in a word-to-phoneme dataset.

### Languages

- Indonesian
- Malay

## Dataset Structure

### Data Instances

| word  | phoneme |
| ----- | ------- |
| aba   | aba     |
| ab    | ab      |
| ab’ad | abʔad   |
| abad  | abad    |
| abadi | abadi   |
| ...   | ...     |

### Data Fields

- `word`: Word (grapheme) as a string.
- `phoneme`: Phoneme (IPA) as a string.

### Data Splits

| train |
| ----- |
| 27553 |

## Additional Information

### Citation Information

```
@misc{open-dict-data-no-date,
	author = {{Open-Dict-Data}},
	title = {{GitHub - open-dict-data/ipa-dict: Monolingual wordlists with pronunciation information in IPA}},
	url = {https://github.com/open-dict-data/ipa-dict},
}
```
