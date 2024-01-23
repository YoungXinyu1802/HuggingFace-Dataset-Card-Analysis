---
annotations_creators:
- unknown
language_creators:
- unknown
language:
- en
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
- 100K<n<1M
pretty_name: KPTimes
---

# KPTimes Benchmark Dataset for Keyphrase Generation

## About

KPTimes is a dataset for benchmarking keyphrase extraction and generation models.
The dataset is composed of 290K news articles in English collected from the [New York Times](https://www.nytimes.com/) and the [Japan
Times](https://www.japantimes.co.jp/).
Keyphrases were annotated by editors in a semi-automated manner (that is, editors revise a set of keyphrases proposed by an algorithm and provide additional keyphrases).
Details about the dataset can be found in the original paper [(Gallina et al., 2019)][gallina-2019].

Reference (indexer-assigned) keyphrases are also categorized under the PRMU (<u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen) scheme as proposed in [(Boudin and Gallina, 2021)][boudin-2021].

Text pre-processing (tokenization) is carried out using `spacy` (`en_core_web_sm` model) with a special rule to avoid splitting words with hyphens (e.g. graph-based is kept as one token).
Stemming (Porter's stemmer implementation provided in `nltk`) is applied before reference keyphrases are matched against the source text.
Details about the process can be found in `prmu.py`. <u>P</u>resent keyphrases are ordered according to their first occurrence position in the text.

## Content and statistics

The dataset contains the following test split:

| Split      | # documents | #words | # keyphrases | % Present | % Reordered | % Mixed | % Unseen |
| :--------- | ----------: | -----: | -----------: | --------: | ----------: | ------: | -------: |
| Train      | 259,923     | 921  | 5.03         | 45.61     | 15.57        | 29.63    | 9.19     |
| Validation | 10,000      | 921  | 5.02         | 45.22    | 15.78        | 29.60    | 9.41     |
| Test       | 20,000      | 648  | 5.03        | 60.64    | 8.90       | 18.95    | 11.51     |

The following data fields are available :

- **id**: unique identifier of the document.
- **title**: title of the document.
- **abstract**: abstract of the document.
- **keyphrases**: list of reference keyphrases.
- **prmu**: list of <u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen categories for reference keyphrases.
- **date**: publishing date (YYYY/MM/DD)
- **categories**: categories of the article (1 or 2 categories)

## References

- (Gallina et al., 2019) Ygor Gallina, Florian Boudin, and Beatrice Daille. 2019.
  [KPTimes: A Large-Scale Dataset for Keyphrase Generation on News Documents][gallina-2019].
  In Proceedings of the 12th International Conference on Natural Language Generation, pages 130–135, Tokyo, Japan. Association for Computational Linguistics.
- (Boudin and Gallina, 2021) Florian Boudin and Ygor Gallina. 2021.
  [Redefining Absent Keyphrases and their Effect on Retrieval Effectiveness][boudin-2021]. 
  In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 4185–4193, Online. Association for Computational Linguistics.

[gallina-2019]: https://aclanthology.org/W19-8617/
[boudin-2021]: https://aclanthology.org/2021.naacl-main.330/