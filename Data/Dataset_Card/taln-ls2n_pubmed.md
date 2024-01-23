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
- 1k<n<10k
task_categories:
- text-generation
task_ids: []
pretty_name: PubMed
tags:
- keyphrase-generation
- keyphrase-extraction
- text-mining
---
# Schutz 2008 PubMed dataset for keyphrase extraction
## About
  
This dataset is made of 1320 articles with full text and author assigned keyphrases.

Details about the dataset can be found in the original paper:
Keyphrase extraction from single documents in the open domain exploiting linguistic and statistical methods. Alexander Thorsten Schutz. Master's thesis, National University of Ireland (2008).

  
Reference (indexer-assigned) keyphrases are also categorized under the PRMU (<u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen) scheme as proposed in the following paper:
 - Florian Boudin and Ygor Gallina. 2021.
   [Redefining Absent Keyphrases and their Effect on Retrieval Effectiveness](https://aclanthology.org/2021.naacl-main.330/). 
   In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 4185–4193, Online. Association for Computational Linguistics.
   
Text pre-processing (tokenization) is carried out using spacy (en_core_web_sm model) with a special rule to avoid splitting words with hyphens (e.g. graph-based is kept as one token). Stemming (Porter's stemmer implementation provided in nltk) is applied before reference keyphrases are matched against the source text.   
  
## Content

The details of the dataset are in the table below:

| Split      | # documents | # keyphrases by document (average) | % Present | % Reordered | % Mixed | % Unseen |
| :--------- | ----------: | -----------:                       | --------: | ----------: | ------: | -------: |
| Test       | 1320        |                5.40                |   84.54   | 9.14        | 3.84    |   2.47   |



The following data fields are available:
- **id**: unique identifier of the document.
- **title**: title of the document.
- **text**: full article minus the title.
- **keyphrases**: list of reference keyphrases.
- **prmu**: list of <u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen categories for reference keyphrases.

**NB**: The present keyphrases (represented by the "P" label in the PRMU column) are sorted by their apparition order in the text (title + text).

