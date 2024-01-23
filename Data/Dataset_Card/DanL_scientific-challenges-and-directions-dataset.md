---
YAML tags:
annotations_creators:
- expert-generated
language_creators: []
language:
- en
license: []
multilinguality:
- monolingual
pretty_name: DanL/scientific-challenges-and-directions-dataset
source_datasets:
- CORD-19
task_categories:
- text-classification
task_ids:
- multi-label-classification
---

# Dataset Card for scientific-challenges-and-directions 

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description
- **Repository: [repo](https://github.com/Dan-La/scientific-challenges-and-directions)**
- **Paper: [A Search Engine for Discovery of Scientific Challenges and Directions](https://arxiv.org/abs/2108.13751)**
- **Point of Contact: lahav@mail.tau.ac.il,tomh@allenai.org**

### Dataset Summary

The scientific challenges and directions dataset is a collection of 2894 sentences and their surrounding contexts, from 1786 full-text papers in the [CORD-19](https://arxiv.org/abs/2004.10706) corpus, labeled for classification of _challenges_ and _directions_ by expert annotators with biomedical and bioNLP backgrounds.

At a high level, our labels are defined as follows:
* **Challenge**: A sentence mentioning a problem, difficulty, flaw, limitation, failure, lack of clarity, or knowledge gap.
* **Research direction**: A sentence mentioning suggestions or needs for further research, hypotheses, speculations, indications or hints that an issue is worthy of exploration.

The dataset was developed to help scientists and medical professionals discover challenges and potential directions across scientific literature. 


### Languages

The language in the dataset is English as written by authors of the scientific papers in the CORD-19 corpus.

## Dataset Structure

### Data Instances

For each instance, there is a unique id, a string for the text sentence, a string for the previous sentence, a string for the next sentence, and a list for the challenge and direction labels. 

```
{'id': 'PMC7152165_152',
 'label': [0.0, 0.0],
 'next_sent': 'The railways brought a new technology and vast engineering and architectural structures into Britain’s rural and urban landscapes.',
 'prev_sent': 'In Britain, improvements in coaching technologies and roads helped to increase stage coach speeds in the late eighteenth and early nineteenth centuries, while the railway construction boom of the 1830s and 1840s led to a massive reduction in journey times, and the emergence of distinctly new experiences and geographies.',
 'text': 'Britain’s railway companies were among the nation’s largest employers in the nineteenth century, and they facilitated the mobility of passengers and important commodities.'}
```

### Data Fields

* id: A string as a unique id for the instance. The id is composed of the unique PMC id of the paper, an underscore, and the index of the sentence within the paper. 
* next_sent_: A string of a sentence that is following the _text_ of the instance. If the text is the first in its paragraph the string is saved as '|'.
* prev_sent_: A string of a sentence that is preceding the _text_ of the instance. If the text is the first in its paragraph the string is saved as '|'.
* text: A string of the sentence we seek to classify. 
* label: A list of 2 values - the first is the label for _challenge_ and the last of _direction_. Each value may be either 0, indicating that the _text_ is **not** _challenge_ or _direction_, or 1, indicating that the the _text_ is _challenge_ or _direction_. Each instance can be a _challenge_, a _direction_, both, or neither.

### Data Splits

The scientific-challenges-and-directions dataset has 3 splits: _train_, _dev_, and _test_. Each instances shows up in only one split. The splits are stratified with no overlap in papers.

| Labels | Train | Dev | Test | All |
|:----------------------------:|:------:|:-----:|:----:|:----:|
| Not Challenge, Not Direction | 602    | 146   | 745  | 1493 |
| Not Challenge, Direction     | 106    | 25    | 122  | 253  |
| Challenge, Not Direction     | 288    | 73    | 382  | 743  |
| Challenge, Direction         | 155    | 40    | 210  | 405  |

## Dataset Creation

### Curation Rationale

The resource was developed to help scientists and medical professionals discover challenges and potential directions across scientific literature, focusing on a broad corpus pertaining to the COVID-19 pandemic and related historical research. 

### Source Data

#### Initial Data Collection and Normalization

See section 3.1 in our [paper](https://arxiv.org/abs/2108.13751).

#### Who are the source language producers?

The authors of the subset of full-text papers in the [CORD-19 dataset](https://arxiv.org/abs/2004.10706), which at the time of creating our dataset included roughly 180K documents.

### Annotations

#### Annotation process 

See section 3.1 in our [paper](https://arxiv.org/abs/2108.13751).

#### Who are the annotators?

Four expert annotators with biomedical and bioNLP backgrounds. For more details see section 3.1 in our [paper](https://arxiv.org/abs/2108.13751).

### Personal and Sensitive Information

The dataset does not contain any personal information about the authors or annotators.

## Considerations for Using the Data

### Social Impact of Dataset

As mentioned, the dataset was developed to help scientists and medical professionals discover challenges and potential directions across scientific literature, focusing on a broad corpus pertaining to the COVID-19 pandemic and related historical research. 
Studies were conducted to evaluate the utility of the dataset for researchers and medical professionals, in which a prototype based on the dataset was found to outperform other biomedical search tools. For more details see section 4 in our [paper](https://arxiv.org/abs/2108.13751).
This dataset was also developed for evaluating representational systems for scientific text classification and can be used as such. 

### Discussion of Biases

The source of the dataset is the full-text papers in the [CORD-19 dataset](https://arxiv.org/abs/2004.10706), so biases in CORD-19 may be replicated to our dataset.

### Other Known Limitations

N/A

## Additional Information

### Dataset Curators

The dataset was developed by Dan Lahav, Jon Saad Falcon, Bailey Kuehl, Sophie Johnson, Sravanthi Parasa, Noam Shomron, Duen Horng Chau, Diyi Yang, Eric Horvitz, Daniel S. Weld and Tom Hope as part of _Tel Aviv University_, the _Allen Institute for AI_, _University of Washington_, _Georgia Institute of Technology_, _Microsoft_ and _Swedish Medical Group_.

It was supported by the Edmond J. Safra Center for Bioinformatics at Tel-Aviv University, ONR  grant N00014-18-1-2193, NSF RAPID grant 2040196, the WR-F/Cable Professorship, and AI2.

### Licensing Information

[More Information Needed]

### Citation Information

If using our dataset and models, please cite:

```
@misc{lahav2021search,
      title={A Search Engine for Discovery of Scientific Challenges and Directions}, 
      author={Dan Lahav and Jon Saad Falcon and Bailey Kuehl and Sophie Johnson and Sravanthi Parasa and Noam Shomron and Duen Horng Chau and Diyi Yang and Eric Horvitz and Daniel S. Weld and Tom Hope},
      year={2021},
      eprint={2108.13751},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Contributions

Thanks to [@Dan-La](https://github.com/Dan-La) and [@tomhoper](https://github.com/tomhoper) for adding this dataset.
