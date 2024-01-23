---
annotations_creators:
- unknown
language_creators:
- unknown
language:
- en
license:
- unknown
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
task_categories:
- text-generation
task_ids: []
pretty_name: KP20k
tags:
- keyphrase-generation
- keyphrase-extraction
- text-mining
---

# KP20k Benchmark Dataset for Keyphrase Generation

## About

KP20k is a dataset for benchmarking keyphrase extraction and generation models.
The data is composed of 570 809 abstracts and their associated titles from scientific articles.

Details about the dataset can be found in the original paper:
- Meng et al 2017.
  [Deep keyphrase Generation](https://aclanthology.org/P17-1054.pdf)
  Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics, pages 582–592
  
Reference (indexer-assigned) keyphrases are also categorized under the PRMU (<u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen) scheme as proposed in the following paper:
 - Florian Boudin and Ygor Gallina. 2021.
   [Redefining Absent Keyphrases and their Effect on Retrieval Effectiveness](https://aclanthology.org/2021.naacl-main.330/). 
   In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 4185–4193, Online. Association for Computational Linguistics.
   
Text pre-processing (tokenization) is carried out using spacy (en_core_web_sm model) with a special rule to avoid splitting words with hyphens (e.g. graph-based is kept as one token). Stemming (Porter's stemmer implementation provided in nltk) is applied before reference keyphrases are matched against the source text.   
  
## Content

The dataset is divided into the following three splits:

| Split      | # documents | # keyphrases by document (average) | % Present | % Reordered | % Mixed | % Unseen |
| :--------- | ----------: | -----------:                       | --------: | ----------: | ------: | -------: |
| Train      | 530 809     |                5.29                |   58.19   | 10.93       | 17.36   |   13.52  |
| Test       | 20 000      |                5.28                |   58.40   | 10.84       | 17.20   |   13.56  |
| Validation | 20 000      |                5.27                |   58.20   | 10.94       | 17.26   |   13.61  |


The following data fields are available:
- **id**: unique identifier of the document. **NB** There were no ids in the original dataset. The ids were generated using the python module shortuuid (https://pypi.org/project/shortuuid/)
- **title**: title of the document.
- **abstract**: abstract of the document.
- **keyphrases**: list of reference keyphrases.
- **prmu**: list of <u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen categories for reference keyphrases.

**NB**: The present keyphrases (represented by the "P" label in the PRMU column) are sorted by their apparition order in the text (title + abstract).