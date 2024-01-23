---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- en
license:
- other
multilinguality:
- monolingual
pretty_name: RiddleSense
size_categories:
- 1K<n<10K
source_datasets:
- riddle_sense
tags:
- riddles
- riddler
- non-commercial
---
# _RiddleSense_ ++: Evaluating LLMs' Riddling abilities

Some cleaning and other modifications to make [the riddle_sense dataset](https://huggingface.co/datasets/riddle_sense) more suitable for training language models to generate riddles via standard `text generation`

## Notable changes

- reformatting to use special tags indicating the question and answer components
- normalization: whitespace normalization, etc with `clean-text`
- **spell correction** the original dataset has numerous spelling errors; these are fixed using `BertChecker` from the `neuspell` library **for the questions only**. The answers were left as-is as there is some specific terminology/puns that get changed by SC.

## Notes & Gotchas

- the original dataset has a non-commercial clause, so this does too.
