---
annotations_creators:
- unknown
language_creators:
- unknown
language:
- fr
- en
license:
- cc-by-4.0
multilinguality:
- multilingual
task_categories:
- text-mining
- text-generation
task_ids:
- keyphrase-generation
- keyphrase-extraction
size_categories:
- 1K<n<10K
pretty_name: TALN-Archives
---

# TALN-Archives Benchmark Dataset for Keyphrase Generation

## About

TALN-Archives is a dataset for benchmarking keyphrase extraction and generation models.
The dataset is composed of 1207 abstracts of scientific papers in French collected from the [TALN Archives](http://talnarchives.atala.org/). 
Keyphrases were annotated by authors in an uncontrolled setting (that is, not limited to thesaurus entries).
English translations of title/abstract/keyphrases are also available for a subset of the documents (456 fully- and 719 partially-translated documents), allowing to experiment with cross-lingual / multilingual keyphrase generation.
Details about the dataset can be found in the original paper [(Boudin, 2013)][boudin-2013].

Reference (indexer-assigned) keyphrases are also categorized under the PRMU (<u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen) scheme as proposed in [(Boudin and Gallina, 2021)][boudin-2021]. <u>P</u>resent reference keyphrases are also ordered by their order of apparition in the concatenation of title and abstract.


Text pre-processing (tokenization) is carried out using `spacy` (`fr_core_news_sm` model) with a special rule to avoid splitting words with hyphens (e.g. graph-based is kept as one token).
Stemming (Snowball stemmer implementation for french provided in `nltk`) is applied before reference keyphrases are matched against the source text.
Details about the process can be found in `prmu.py`.

## Content and statistics

The dataset contains the following test split:

| Split      | # documents | #words | # keyphrases | % Present | % Reordered | % Mixed | % Unseen |
| :--------- | ----------: | -----: | -----------: | --------: | ----------: | ------: | -------: |
| Test       | 1207        | 138.3  | 4.12         | 53.83     | 12.32       | 21.69   | 12.16    |

The following data fields are available :

- **id**: unique identifier of the document.
- **title**: title of the document.
- **abstract**: abstract of the document.
- **keyphrases**: list of reference keyphrases.
- **prmu**: list of <u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen categories for reference keyphrases.
- **translation**: translations of title, abstract and keyphrases in English if available.

## References

- (Boudin, 2013) Florian Boudin. 2013.
  [TALN Archives : a digital archive of French research articles in Natural Language Processing (TALN Archives : une archive numérique francophone des articles de recherche en Traitement Automatique de la Langue) [in French]][boudin-2013].
  In Proceedings of TALN 2013 (Volume 2: Short Papers), pages 507–514, Les Sables d’Olonne, France. ATALA.
- (Boudin and Gallina, 2021) Florian Boudin and Ygor Gallina. 2021.
  [Redefining Absent Keyphrases and their Effect on Retrieval Effectiveness][boudin-2021]. 
  In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 4185–4193, Online. Association for Computational Linguistics.

[boudin-2013]: https://aclanthology.org/F13-2001/
[boudin-2021]: https://aclanthology.org/2021.naacl-main.330/