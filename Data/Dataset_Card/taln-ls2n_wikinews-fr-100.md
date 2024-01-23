---
annotations_creators:
- unknown
language_creators:
- unknown
language:
- fr
license:
- cc-by-4.0
multilinguality:
- monolingual
task_categories:
- text-mining
- text-generation
task_ids:
- keyphrase-generation
- keyphrase-extraction
size_categories:
- n<1K
pretty_name: Wikinews-fr-100
---

# Wikinews-fr-100 Benchmark Dataset for Keyphrase Generation

## About

Wikinews-fr-100 is a dataset for benchmarking keyphrase extraction and generation models.
The dataset is composed of 100 news articles in French collected from [wikinews](https://fr.wikinews.org/wiki/Accueil).
Keyphrases were annotated by readers (students in computer science) in an uncontrolled setting (that is, not limited to thesaurus entries).
Details about the dataset can be found in the original paper [(Bougouin et al., 2013)][bougouin-2013].

Reference (indexer-assigned) keyphrases are also categorized under the PRMU (<u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen) scheme as proposed in [(Boudin and Gallina, 2021)][boudin-2021]. Present reference keyphrases are also ordered by their order of apparition in the concatenation of title and abstract.

Text pre-processing (tokenization) is carried out using `spacy` (`fr_core_news_sm` model) with a special rule to avoid splitting words with hyphens (e.g. graph-based is kept as one token).
Stemming (Snowball stemmer implementation for french provided in `nltk`) is applied before reference keyphrases are matched against the source text.
Details about the process can be found in `prmu.py`.

## Content and statistics

The dataset contains the following test split:

| Split      | # documents | #words | # keyphrases | % Present | % Reordered | % Mixed | % Unseen |
| :--------- | ----------: | -----: | -----------: | --------: | ----------: | ------: | -------: |
| Test       | 100         | 306.9  |  9.64        | 95.91     | 1.40        | 0.85    | 1.84     |

The following data fields are available :

- **id**: unique identifier of the document.
- **title**: title of the document.
- **abstract**: abstract of the document.
- **keyphrases**: list of reference keyphrases.
- **prmu**: list of <u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen categories for reference keyphrases.

## References

- (Bougouin et al., 2013) Adrien Bougouin, Florian Boudin, and Béatrice Daille. 2013.
  [TopicRank: Graph-Based Topic Ranking for Keyphrase Extraction][bougouin-2013].
  In Proceedings of the Sixth International Joint Conference on Natural Language Processing, pages 543–551, Nagoya, Japan. Asian Federation of Natural Language Processing.
- (Boudin and Gallina, 2021) Florian Boudin and Ygor Gallina. 2021.
  [Redefining Absent Keyphrases and their Effect on Retrieval Effectiveness][boudin-2021]. 
  In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 4185–4193, Online. Association for Computational Linguistics.

[bougouin-2013]: https://aclanthology.org/I13-1062/
[boudin-2021]: https://aclanthology.org/2021.naacl-main.330/