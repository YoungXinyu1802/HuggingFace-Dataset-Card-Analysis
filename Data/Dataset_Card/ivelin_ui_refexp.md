---
license: cc-by-4.0
task_categories:
  - image-to-text
tags:
  - ui-referring-expression
  - ui-refexp
language:
  - en
pretty_name: UI understanding
size_categories:
  - 10K<n<100K
dataset_info:
  features:
    - name: screenshot
      dtype: image
    - name: prompt
      dtype: string
    - name: target_bounding_box
      dtype: string
  config_name: ui_refexp
  splits:
    - name: train
      num_bytes: 562037265
      num_examples: 15624
    - name: validation
      num_bytes: 60399225
      num_examples: 471
    - name: test
      num_bytes: 69073969
      num_examples: 565
  download_size: 6515012176
  dataset_size: 691510459
---

# Dataset Card for UIBert

## Dataset Description

- **Homepage:** https://github.com/google-research-datasets/uibert
- **Repository:** https://github.com/google-research-datasets/uibert
- **Paper:** https://arxiv.org/abs/2107.13731
- **Leaderboard:**
  - UIBert: https://arxiv.org/abs/2107.13731
  - Pix2Struct: https://arxiv.org/pdf/2210.03347

### Dataset Summary

This is a Hugging Face formatted dataset derived from the [Google UIBert dataset](https://github.com/google-research-datasets/uibert), which is in turn derived from the [RICO dataset](https://interactionmining.org/rico).

### Supported Tasks and Leaderboards

- UI Understanding
- UI Referring Expressions
- UI Action Automation

### Languages

- English

## Dataset Structure

- `screenshot`: blob of pixels.
- `prompt`: Prompt referring to a UI component with an optional action verb. For example "click on search button next to menu drawer."
- `target_bounding_box`: Bounding box of targeted UI components. `[xmin, ymin, xmax, ymax]`

### Data Splits

- train: 15K samples
- validation: 471 samples
- test: 565 samples

## Dataset Creation

### Curation Rationale

[More Information Needed]

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

[More Information Needed]
