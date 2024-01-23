---
annotations_creators:
- unknown
language_creators:
- unknown
language:
- en
license: cc-by-4.0
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
pretty_name: Preprocessed SemEval-2010 Benchmark dataset 
---

# Preprocessed SemEval-2010 Benchmark dataset for Keyphrase Generation

## About

SemEval-2010 is a dataset for benchmarking keyphrase extraction and generation models.
The dataset is composed of 244 **full-text** scientific papers collected from the [ACM Digital Library](https://dl.acm.org/).
Keyphrases were annotated by readers and combined with those provided by the authors.
Details about the SemEval-2010 dataset can be found in the original paper [(kim et al., 2010)][kim-2010].

This version of the dataset was produced by [(Boudin et al., 2016)][boudin-2016] and provides four increasingly sophisticated levels of document preprocessing:

  * `lvl-1`: default text files provided by the SemEval-2010 organizers.

  * `lvl-2`: for each file, we manually retrieved the original PDF file from the ACM Digital Library.
    We then extract the enriched textual content of the PDF files using an Optical Character Recognition (OCR) system and perform document logical structure detection using ParsCit v110505.
    We use the detected logical structure to remove author-assigned keyphrases and select only relevant elements : title, headers, abstract, introduction, related work, body text and conclusion.
    We finally apply a systematic dehyphenation at line breaks.s

  * `lvl-3`: we further abridge the input text from level 2 preprocessed documents to the following: title, headers, abstract, introduction, related work, background and conclusion.

  * `lvl-4`: we abridge the input text from level 3 preprocessed documents using an unsupervised summarization technique.
    We keep the title and abstract and select the most content bearing sentences from the remaining contents.

Titles and abstracts, collected from the [SciCorefCorpus](https://github.com/melsk125/SciCorefCorpus), are also provided.
Details about how they were extracted and cleaned up can be found in [(Chaimongkol et al., 2014)][chaimongkol-2014]. 

Reference keyphrases are provided in stemmed form (because they were provided like this for the test split in the competition).
They are also categorized under the PRMU (<u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen) scheme as proposed in [(Boudin and Gallina, 2021)][boudin-2021].
Text pre-processing (tokenization) is carried out using `spacy` (`en_core_web_sm` model) with a special rule to avoid splitting words with hyphens (e.g. graph-based is kept as one token).
Stemming (Porter's stemmer implementation provided in `nltk`) is applied before reference keyphrases are matched against the source text.
Details about the process can be found in `prmu.py`.
The <u>P</u>resent reference keyphrases are also ordered by their order of apparition in the concatenation of title and text (lvl-1).

## Content and statistics

The dataset is divided into the following two splits:

| Split      | # documents | #words | # keyphrases | % Present | % Reordered | % Mixed | % Unseen |
| :--------- |------------:|-------:|-------------:|----------:|------------:|--------:|---------:|
| Train      |         144 |  184.6 |        15.44 |     42.16 |        7.36 |   26.85 |    23.63 |
| Test       |         100 |  203.1 |        14.66 |     40.11 |        8.34 |   27.12 |    24.43 |

Statistics (#words, PRMU distributions) are computed using the title/abstract and not the full text of scientific papers.

The following data fields are available :

- **id**: unique identifier of the document.
- **title**: title of the document.
- **abstract**: abstract of the document.
- **lvl-1**: content of the document with no text processing. 
- **lvl-2**: content of the document retrieved from original PDF files and cleaned up.
- **lvl-3**: content of the document further abridged to relevant sections.
- **lvl-4**: content of the document further abridged using an unsupervised summarization technique.
- **keyphrases**: list of reference keyphrases.
- **prmu**: list of <u>P</u>resent-<u>R</u>eordered-<u>M</u>ixed-<u>U</u>nseen categories for reference keyphrases.

## References

- (Kim et al., 2010) Su Nam Kim, Olena Medelyan, Min-Yen Kan, and Timothy Baldwin. 2010.
  [SemEval-2010 Task 5 : Automatic Keyphrase Extraction from Scientific Articles][kim-2010].
  In Proceedings of the 5th International Workshop on Semantic Evaluation, pages 21–26, Uppsala, Sweden. Association for Computational Linguistics.
- (Chaimongkol et al., 2014) Panot Chaimongkol, Akiko Aizawa, and Yuka Tateisi. 2014.
  [Corpus for Coreference Resolution on Scientific Papers][chaimongkol-2014].
  In Proceedings of the Ninth International Conference on Language Resources and Evaluation (LREC'14), pages 3187–3190, Reykjavik, Iceland. European Language Resources Association (ELRA).
- (Boudin et al., 2016) Florian Boudin, Hugo Mougard, and Damien Cram. 2016.
  [How Document Pre-processing affects Keyphrase Extraction Performance][boudin-2016].
  In Proceedings of the 2nd Workshop on Noisy User-generated Text (WNUT), pages 121–128, Osaka, Japan. The COLING 2016 Organizing Committee.
- (Boudin and Gallina, 2021) Florian Boudin and Ygor Gallina. 2021.
  [Redefining Absent Keyphrases and their Effect on Retrieval Effectiveness][boudin-2021]. 
  In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 4185–4193, Online. Association for Computational Linguistics.

[kim-2010]: https://aclanthology.org/S10-1004/
[chaimongkol-2014]: https://aclanthology.org/L14-1259/
[boudin-2016]: https://aclanthology.org/W16-3917/
[boudin-2021]: https://aclanthology.org/2021.naacl-main.330/
