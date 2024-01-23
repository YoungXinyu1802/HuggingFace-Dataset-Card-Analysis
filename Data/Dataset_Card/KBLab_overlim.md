---
annotations_creators:
- other
language_creators:
- other
language:
- sv
- da
- nb
license:
- cc-by-4.0
multilinguality:
- translation
size_categories:
- unknown
source_datasets:
- extended|glue
- extended|super_glue
task_categories:
- text-classification
task_ids:
- natural-language-inference
- semantic-similarity-classification
- sentiment-classification
- text-scoring
pretty_name: overlim
tags:
- qa-nli
- paraphrase-identification
---

# Dataset Card for OverLim

## Dataset Description

- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

The _OverLim_ dataset contains some of the GLUE and SuperGLUE tasks automatically
translated to Swedish, Danish, and Norwegian (bokmål), using the OpusMT models
for MarianMT.

The translation quality was not manually checked and may thus be faulty.
Results on these datasets should thus be interpreted carefully.

If you want to have an easy script to train and evaluate your models have a look [here](https://github.com/kb-labb/overlim_eval)


### Supported Tasks and Leaderboards

The data contains the following tasks from GLUE and SuperGLUE:

- GLUE
  - `mnli`
  - `mrpc`
  - `qnli`
  - `qqp`
  - `rte`
  - `sst`
  - `stsb`
  - `wnli`
- SuperGLUE
  - `boolq`
  - `cb`
  - `copa`
  - `rte`

### Languages

- Swedish
- Danish
- Norwegian (bokmål)

## Dataset Structure

### Data Instances

Every task has their own set of features, but all share an `idx` and `label`.

- GLUE
  - `mnli`
    - `premise`, `hypothesis`
  - `mrpc`
    - `text_a`, `text_b`
  - `qnli`
    - `premise`, `hypothesis`
  - `qqp`
    - `text_a`, `text_b`
  - `sst`
    - `text`
  - `stsb`
    - `text_a`, `text_b`
  - `wnli`
    - `premise`, `hypothesis`
- SuperGLUE
  - `boolq`
    - `question`, `passage`
  - `cb`
    - `premise`, `hypothesis`
  - `copa`
    - `premise`, `choice1`, `choice2`, `question`
  - `rte`
    - `premise`, `hypothesis`

### Data Splits

In order to have test-split, we repurpose the original validation-split as
test-split, and split the training-split into a new training- and
validation-split, with an 80-20 distribution.

## Dataset Creation

For more information about the individual tasks see (https://gluebenchmark.com) and (https://super.gluebenchmark.com).

### Curation Rationale

Training non-English models is easy, but there is a lack of evaluation datasets to compare their actual performance.

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@kb-labb](https://github.com/kb-labb) for adding this dataset.
