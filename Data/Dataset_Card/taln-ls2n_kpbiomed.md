---
annotations_creators:
- unknown
language_creators:
- unknown
language:
- en
license:
- cc-by-nc-4.0
multilinguality:
- monolingual
task_categories:
- text-mining
- text-generation
task_ids:
- keyphrase-generation
- keyphrase-extraction
size_categories:
- 100K<n<1M
pretty_name: KP-Biomed
---

# KPBiomed, A Large-Scale Dataset for keyphrase generation
## About
  
This dataset is made of 5.6 million abstracts with author assigned keyphrases.

Details about the dataset can be found in the original paper:
Maël Houbre, Florian Boudin and Béatrice Daille. 2022. [A Large-Scale Dataset for Biomedical Keyphrase Generation](https://arxiv.org/abs/2211.12124). In Proceedings of the 13th International Workshop on Health Text Mining and Information Analysis (LOUHI 2022).

  
Reference (author-assigned) keyphrases are also categorized under the PRMU (<u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen) scheme as proposed in the following paper:
 - Florian Boudin and Ygor Gallina. 2021.
   [Redefining Absent Keyphrases and their Effect on Retrieval Effectiveness](https://aclanthology.org/2021.naacl-main.330/). 
   In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 4185–4193, Online. Association for Computational Linguistics.
   
Text pre-processing (tokenization) is carried out using spacy (en_core_web_sm model) with a special rule to avoid splitting words with hyphens (e.g. graph-based is kept as one token). Stemming (Porter's stemmer implementation provided in nltk) is applied before reference keyphrases are matched against the source text.   
  
## Content

The details of the dataset are in the table below:

| Split        | # documents | # keyphrases by document (average) | % Present | % Reordered | % Mixed | % Unseen |
| :----------- | ----------: | ---------------------------------: | --------: | ----------: | ------: | -------: |
| Train small  |    500k     |               5.24                 |   66.31   |    7.16     |  12.60  |  13.93   |
| Train medium |    2M       |               5.24                 |   66.30   |    7.18     |  12.57  |  13.95   |
| Train large  |    5.6M     |               5.23                 |   66.32   |    7.18     |  12.55  |  13.95   |
| Validation   |    20k      |               5.25                 |   66.44   |    7.07     |  12.45  |  14.05   |
| Test         |    20k      |               5.22                 |   66.59   |    7.22     |  12.44  |  13.75   |



The following data fields are available:
- **id**: unique identifier of the document.
- **title**: title of the document.
- **abstract**: abstract of the document.
- **keyphrases**: list of reference keyphrases.
- **mesh terms**: list of indexer assigned MeSH terms if available (around 68% of the articles)
- **prmu**: list of <u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen categories for reference keyphrases.
- **authors**: list of the article's authors
- **year**: publication year

**NB**: The present keyphrases (represented by the "P" label in the PRMU column) are sorted by their apparition order in the text (title + text).


