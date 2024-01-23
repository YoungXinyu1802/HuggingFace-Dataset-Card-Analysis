---
annotations_creators:
- unknown
language_creators:
- unknown
language:
- fr
license: cc-by-4.0
multilinguality:
- multilingual
task_categories:
- text-mining
- text-generation
task_ids:
- keyphrase-generation
- keyphrase-extraction
size_categories:
- n<1K
pretty_name: TermITH-Eval
---

# TermITH-Eval Benchmark Dataset for Keyphrase Generation

## About

TermITH-Eval is a dataset for benchmarking keyphrase extraction and generation models.
The dataset is composed of 400 abstracts of scientific papers in French collected from the FRANCIS and PASCAL databases of the French [Institute for Scientific and Technical Information (Inist)](https://www.inist.fr/).
Keyphrases were annotated by professional indexers in an uncontrolled setting (that is, not limited to thesaurus entries).
Details about the dataset can be found in the original paper [(Bougouin et al., 2016)][bougouin-2016].

Reference (indexer-assigned) keyphrases are also categorized under the PRMU (<u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen) scheme as proposed in [(Boudin and Gallina, 2021)][boudin-2021]. Present reference keyphrases are also ordered by their order of apparition in the concatenation of title and abstract.

Text pre-processing (tokenization) is carried out using `spacy` (`fr_core_news_sm` model) with a special rule to avoid splitting words with hyphens (e.g. graph-based is kept as one token).
Stemming (Snowball stemmer implementation for french provided in `nltk`) is applied before reference keyphrases are matched against the source text.
Details about the process can be found in `prmu.py`.

## Content and statistics

The dataset contains the following test split:

| Split      | # documents |     #words | # keyphrases | % Present | % Reordered | % Mixed | % Unseen |
| :--------- |------------:|-----------:|-------------:|----------:|------------:|--------:|---------:|
| Test       |         399 |      156.9 |        11.81 |     40.60 |        7.32 |   19.28 |    32.80 |

The following data fields are available :

- **id**: unique identifier of the document.
- **title**: title of the document.
- **abstract**: abstract of the document.
- **keyphrases**: list of reference keyphrases.
- **prmu**: list of <u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen categories for reference keyphrases.
- **category**: category of the document, i.e. chimie (chemistry), archeologie (archeology), linguistique (linguistics) and scienceInfo (information sciences).

## References

- (Bougouin et al., 2016) Adrien Bougouin, Sabine Barreaux, Laurent Romary, Florian Boudin, and Béatrice Daille. 2016.
  [TermITH-Eval: a French Standard-Based Resource for Keyphrase Extraction Evaluation][bougouin-2016]. 
  In Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC'16), pages 1924–1927, Portorož, Slovenia. European Language Resources Association (ELRA).Language Processing, pages 543–551, Nagoya, Japan. Asian Federation of Natural Language Processing.
- (Boudin and Gallina, 2021) Florian Boudin and Ygor Gallina. 2021.
  [Redefining Absent Keyphrases and their Effect on Retrieval Effectiveness][boudin-2021]. 
  In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 4185–4193, Online. Association for Computational Linguistics.

[bougouin-2016]: https://aclanthology.org/L16-1304/
[boudin-2021]: https://aclanthology.org/2021.naacl-main.330/