---
license: cc-by-nc-nd-4.0
language:
- es
multilinguality:
- monolingual
size_categories:
- 100M<n<1B
source_datasets:
- original
task_categories:
  - text-generation
  - fill-mask
task_ids:
  - language-modeling
  - masked-language-modeling
---


# esCorpius: A Massive Spanish Crawling Corpus

## Introduction
In the recent years, Transformer-based models have lead to significant advances in language modelling for natural language processing. However, they require a vast amount of data to be (pre-)trained and there is a lack of corpora in languages other than English. Recently, several initiatives have presented multilingual datasets obtained from automatic web crawling. However, the results in Spanish present important shortcomings, as they are either too small in comparison with other languages, or present a low quality derived from sub-optimal cleaning and deduplication. In this work, we introduce esCorpius, a Spanish crawling corpus obtained from near 1 Pb of Common Crawl data. It is the most extensive corpus in Spanish with this level of quality in the extraction, purification and deduplication of web textual content. Our data curation process involves a novel highly parallel cleaning pipeline and encompasses a series of deduplication mechanisms that together ensure the integrity of both document and paragraph boundaries. Additionally, we maintain both the source web page URL and the WARC shard origin URL in order to complain with EU regulations. esCorpius has been released under CC BY-NC-ND 4.0 license.

## Statistics
| **Corpus**              | OSCAR<br>22.01 | mC4          | CC-100          | ParaCrawl<br>v9 | esCorpius<br>(ours) |
|-------------------------|----------------|--------------|-----------------|-----------------|-------------------------|
| **Size (ES)**           | 381.9 GB       | 1,600.0 GB   | 53.3 GB         | 24.0 GB         | 322.5 GB                |
| **Docs (ES)**           | 51M            | 416M         | -               | -               | 104M                    |
| **Words (ES)**          | 42,829M        | 433,000M     | 9,374M          | 4,374M          | 50,773M                 |
| **Lang.<br>identifier** | fastText       | CLD3         | fastText        | CLD2            | CLD2 + fastText         |
| **Elements**            | Document       | Document     | Document        | Sentence        | Document and paragraph  |
| **Parsing quality**     | Medium         | Low          | Medium          | High            | High                    |
| **Cleaning quality**    | Low            | No cleaning  | Low             | High            | High                    |
| **Deduplication**       | No             | No           | No              | Bicleaner       | dLHF                    |
| **Language**            | Multilingual   | Multilingual | Multilingual    | Multilingual    | Spanish                 |
| **License**             | CC-BY-4.0      | ODC-By-v1.0  | Common<br>Crawl | CC0             | CC-BY-NC-ND             |


## Citation
Link to the paper: https://www.isca-speech.org/archive/pdfs/iberspeech_2022/gutierrezfandino22_iberspeech.pdf / https://arxiv.org/abs/2206.15147

Cite this work:
```
@inproceedings{gutierrezfandino22_iberspeech,
  author={Asier Gutiérrez-Fandiño and David Pérez-Fernández and Jordi Armengol-Estapé and David Griol and Zoraida Callejas},
  title={{esCorpius: A Massive Spanish Crawling Corpus}},
  year=2022,
  booktitle={Proc. IberSPEECH 2022},
  pages={126--130},
  doi={10.21437/IberSPEECH.2022-26}
}
```
## Disclaimer
We did not perform any kind of filtering and/or censorship to the corpus. We expect users to do so applying their own methods. We are not liable for any misuse of the corpus.