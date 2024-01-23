---
language:
- en
paperswithcode_id: 
pretty_name: SumPubmed
train-eval-index:
- config: Blaise-g--SumPubmed
  task: summarization
  task_id: summarization
  splits:
    eval_split: test
  col_mapping:
    text: text
    abstract: target
---

# Dataset Card for "SumPubmed"

## Original Dataset Description

- **Repository:** [https://github.com/vgupta123/sumpubmed](https://github.com/vgupta123/sumpubmed) 
- **Paper:** [More Information Needed](https://vgupta123.github.io/docs/121_paper.pdf)

## Description of dataset processing
5 rows were dropped from the original dataset taken from KAGGLE as they were missing the respective 'shorter_abstract' entries.

The 'line_text' and 'filename_text' columns were left untouched while the remaining ones were processed to remove the '\n' (many repetitions of those present in the original dataset), '\<dig\>', '\<cit\>', 'BACKGROUND', 'RESULTS' and 'CONCLUSIONS' matching strings which were deemed not necessary for the purpose of summarization. Additionally, extra spaces were removed and spacing around punctuations was fixed.

