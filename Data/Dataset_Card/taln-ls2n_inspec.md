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
task_categories:
- text-mining
- text-generation
task_ids:
- keyphrase-generation
- keyphrase-extraction
size_categories:
- 1K<n<10K
pretty_name: Inspec
---

# Inspec Benchmark Dataset for Keyphrase Generation

## About

Inspec is a dataset for benchmarking keyphrase extraction and generation models.
The dataset is composed of 2,000 abstracts of scientific papers collected from the [Inspec database](https://www.theiet.org/resources/inspec/).
Keyphrases were annotated by professional indexers in an uncontrolled setting (that is, not limited to thesaurus entries).
Details about the inspec dataset can be found in the original paper [(Hulth, 2003)][hulth-2003].
 

Reference (indexer-assigned) keyphrases are also categorized under the PRMU (<u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen) scheme as proposed in [(Boudin and Gallina, 2021)][boudin-2021].

Text pre-processing (tokenization) is carried out using `spacy` (`en_core_web_sm` model) with a special rule to avoid splitting words with hyphens (e.g. graph-based is kept as one token).
Stemming (Porter's stemmer implementation provided in `nltk`) is applied before reference keyphrases are matched against the source text.
Details about the process can be found in `prmu.py`.

## Content and statistics

The dataset is divided into the following three splits:

| Split      | # documents | #words | # keyphrases | % Present | % Reordered | % Mixed | % Unseen |
| :--------- | ----------: | -----: | -----------: | --------: | ----------: | ------: | -------: |
| Train      | 1,000       | 141.7  | 9.79         | 78.00     | 9.85        | 6.22    | 5.93     |
| Validation | 500         | 132.2  | 9.15         | 77.96     | 9.82        | 6.75    | 5.47     |
| Test       | 500         | 134.8  | 9.83         | 78.70     | 9.92        | 6.48    | 4.91     |

The following data fields are available :

- **id**: unique identifier of the document.
- **title**: title of the document.
- **abstract**: abstract of the document.
- **keyphrases**: list of reference keyphrases.
- **prmu**: list of <u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen categories for reference keyphrases.

## References

- (Hulth, 2003) Anette Hulth. 2003.
  [Improved automatic keyword extraction given more linguistic knowledge](https://aclanthology.org/W03-1028). 
  In Proceedings of the 2003 Conference on Empirical Methods in Natural Language Processing, pages 216-223.
- (Boudin and Gallina, 2021) Florian Boudin and Ygor Gallina. 2021.
  [Redefining Absent Keyphrases and their Effect on Retrieval Effectiveness](https://aclanthology.org/2021.naacl-main.330/). 
  In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 4185–4193, Online. Association for Computational Linguistics.

[hulth-2003]: https://aclanthology.org/W03-1028/
[boudin-2021]: https://aclanthology.org/2021.naacl-main.330/