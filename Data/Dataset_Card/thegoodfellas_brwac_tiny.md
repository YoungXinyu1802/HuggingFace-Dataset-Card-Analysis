---
annotations_creators:
- no-annotation
language:
- pt
language_creators:
- found
license:
- mit
multilinguality:
- monolingual
pretty_name: brwac
size_categories:
- 10M<n<100M
source_datasets:
- original
tags:
- ufrgs
- nlp
- brazil
task_categories:
- fill-mask
task_ids:
- masked-language-modeling
---

# Dataset Card for BrWac

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Source Data](#source-data)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [BrWaC homepage](https://www.inf.ufrgs.br/pln/wiki/index.php?title=BrWaC)
- **Repository:** [BrWaC repository](https://www.inf.ufrgs.br/pln/wiki/index.php?title=BrWaC)
- **Paper:** [The brWaC Corpus: A New Open Resource for Brazilian Portuguese](https://www.aclweb.org/anthology/L18-1686/)
- **Point of Contact:** [Jorge A. Wagner Filho](mailto:jawfilho@inf.ufrgs.br)

### Dataset Summary

The BrWaC (Brazilian Portuguese Web as Corpus) is a large corpus constructed following the Wacky framework, 
which was made public for research purposes. The current corpus version, released in January 2017, is composed by 
3.53 million documents, 2.68 billion tokens and 5.79 million types. Please note that this resource is available 
solely for academic research purposes, and you agreed not to use it for any commercial applications.
Manually download at https://www.inf.ufrgs.br/pln/wiki/index.php?title=BrWaC

This is a Tiny version of the entire dataset for educational purposes. Please, refer to https://github.com/the-good-fellas/xlm-roberta-pt-br

### Supported Tasks and Leaderboards

Initially meant for fill-mask task.

### Languages

Brazilian Portuguese

## Dataset Creation

### Personal and Sensitive Information

All data were extracted from public sites.


### Licensing Information

MIT

### Citation Information

```
@inproceedings{wagner2018brwac,
  title={The brwac corpus: A new open resource for brazilian portuguese},
  author={Wagner Filho, Jorge A and Wilkens, Rodrigo and Idiart, Marco and Villavicencio, Aline},
  booktitle={Proceedings of the Eleventh International Conference on Language Resources and Evaluation 
  (LREC 2018)},
  year={2018}
}
```

### Contributions

Thanks to [@the-good-fellas](https://github.com/the-good-fellas) for adding this dataset as hf format.