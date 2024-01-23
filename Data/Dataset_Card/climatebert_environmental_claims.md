---
license: cc-by-nc-sa-4.0
annotations_creators:
- expert-generated
language_creators:
- found
language:
- en
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- text-classification
pretty_name: EnvironmentalClaims
---

# Dataset Card for environmental_claims

## Dataset Description

- **Homepage:** [climatebert.ai](https://climatebert.ai)
- **Repository:**
- **Paper:** [arxiv.org/abs/2209.00507](https://arxiv.org/abs/2209.00507)
- **Leaderboard:**
- **Point of Contact:** [Dominik Stammbach](mailto:dominsta@ethz.ch)

### Dataset Summary

We introduce an expert-annotated dataset for detecting real-world environmental claims made by listed companies.

### Supported Tasks and Leaderboards

The dataset supports a binary classification task of whether a given sentence is an environmental claim or not.

### Languages

The text in the dataset is in English.

## Dataset Structure

### Data Instances

```
{
    "text": "It will enable E.ON to acquire and leverage a comprehensive understanding of the transfor- mation of the energy system and the interplay between the individual submarkets in regional and local energy supply sys- tems.",
    "label": 0
}
```

### Data Fields

- text: a sentence extracted from corporate annual reports, sustainability reports and earning calls transcripts
- label: the label (0 -> no environmental claim, 1 -> environmental claim)

### Data Splits

The dataset is split into:
- train: 2,400
- validation: 300
- test: 300

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

Our dataset contains environmental claims by firms, often in the financial domain. We collect text from corporate annual reports, sustainability reports, and earning calls transcripts.

For more information regarding our sample selection, please refer to Appendix B of our paper, which is provided for [citation](#citation-information).

#### Who are the source language producers?

Mainly large listed companies.

### Annotations

#### Annotation process

For more information on our annotation process and annotation guidelines, please refer to Appendix C of our paper, which is provided for [citation](#citation-information).

#### Who are the annotators?

The authors and students at University of Zurich with majors in finance and sustainable finance.

### Personal and Sensitive Information

Since our text sources contain public information, no personal and sensitive information should be included.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

- Dominik Stammbach
- Nicolas Webersinke
- Julia Anna Bingler
- Mathias Kraus
- Markus Leippold

### Licensing Information

This dataset is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license (cc-by-nc-sa-4.0). To view a copy of this license, visit [creativecommons.org/licenses/by-nc-sa/4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

If you are interested in commercial use of the dataset, please contact the ClimateBert team at [hello@climatebert.ai](mailto:hello@climatebert.ai).

### Citation Information

```bibtex
@misc{stammbach2022environmentalclaims,
  title = {A Dataset for Detecting Real-World Environmental Claims},
  author = {Stammbach, Dominik and Webersinke, Nicolas and Bingler, Julia Anna and Kraus, Mathias and Leippold, Markus},
  year = {2022},
  doi = {10.48550/ARXIV.2209.00507},
  url = {https://arxiv.org/abs/2209.00507},
  publisher = {arXiv},
}
```

### Contributions

Thanks to [@webersni](https://github.com/webersni) for adding this dataset.