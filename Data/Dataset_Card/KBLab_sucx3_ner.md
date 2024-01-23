---
annotations_creators:
- expert-generated
language_creators:
- other
language:
- sv
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- other
task_ids:
- named-entity-recognition
- part-of-speech
pretty_name: sucx3_ner
tags:
- structure-prediction
---
# Dataset Card for _SUCX 3.0 - NER_

## Dataset Description

- **Homepage:** [https://spraakbanken.gu.se/en/resources/suc3](https://spraakbanken.gu.se/en/resources/suc3)
- **Repository:** [https://github.com/kb-labb/sucx3_ner](https://github.com/kb-labb/sucx3_ner)
- **Paper:** [SUC 2.0 manual](http://spraakbanken.gu.se/parole/Docs/SUC2.0-manual.pdf)
- **Point of Contact:**

### Dataset Summary

The dataset is a conversion of the venerable SUC 3.0 dataset into the
huggingface ecosystem.
The original dataset does not contain an official train-dev-test split, which is
introduced here; the tag distribution for the NER tags between the three splits
is mostly the same.

The dataset has three different types of tagsets: manually annotated POS,
manually annotated NER, and automatically annotated NER.
For the automatically annotated NER tags, only sentences were chosen, where the
automatic and manual annotations would match (with their respective categories).

Additionally we provide remixes of the same data with some or all sentences
being lowercased.

### Supported Tasks and Leaderboards

- Part-of-Speech tagging
- Named-Entity-Recognition

### Languages

Swedish

## Dataset Structure

### Data Remixes

- `original_tags` contain the manual NER annotations
  - `lower` the whole dataset uncased
  - `lower_mix` some of the dataset uncased
  - `lower_both` every instance both cased and uncased
- `simple_tags` contain the automatic NER annotations
  - `lower` the whole dataset uncased
  - `lower_mix` some of the dataset uncased
  - `lower_both` every instance both cased and uncased

### Data Instances

For each instance, there is an `id`, with an optional `_lower` suffix to mark
that it has been modified, a `tokens` list of strings containing tokens, a
`pos_tags` list of strings containing POS-tags, and a `ner_tags` list of strings
containing NER-tags.

```json
{"id": "e24d782c-e2475603_lower",
"tokens": ["-", "dels", "har", "vi", "inget", "index", "att", "g\u00e5", "efter", ",", "vi", "kr\u00e4ver", "allts\u00e5", "ers\u00e4ttning", "i", "40-talets", "penningv\u00e4rde", "."],
"pos_tags": ["MID", "KN", "VB", "PN", "DT", "NN", "IE", "VB", "PP", "MID", "PN", "VB", "AB", "NN", "PP", "NN", "NN", "MAD"],
"ner_tags": ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]}
```

### Data Fields

- `id`: a string containing the sentence-id
- `tokens`: a list of strings containing the sentence's tokens
- `pos_tags`: a list of strings containing the tokens' POS annotations
- `ner_tags`: a list of strings containing the tokens' NER annotations

### Data Splits

| Dataset Split | Size Percentage of Total Dataset Size | Number of Instances for the Original Tags |
| ------------- | ------------------------------------- | ----------------------------------------- |
| train         | 64%                                   | 46\,026                                   |
| dev           | 16%                                   | 11\,506                                   |
| test          | 20%                                   | 14\,383                                   |

The `simple_tags` remix has fewer instances due to the requirement to match
tags.

## Dataset Creation

See the [original webpage](https://spraakbanken.gu.se/en/resources/suc3)

## Additional Information

### Dataset Curators

[Språkbanken](sb-info@svenska.gu.se)

### Licensing Information

CC BY 4.0 (attribution)

### Citation Information

[SUC 2.0 manual](http://spraakbanken.gu.se/parole/Docs/SUC2.0-manual.pdf)

### Contributions

Thanks to [@robinqrtz](https://github.com/robinqrtz) for adding this dataset.
