---
dataset_info:
  features:
  - name: word
    dtype: string
  - name: domain
    dtype: string
  - name: domain_short
    dtype: string
  - name: freq
    dtype: int64
  - name: log_prob
    dtype: float64
  - name: log_prob_smoothed
    dtype: float64
  splits:
  - name: train
    num_bytes: 1232856541
    num_examples: 15326084
  download_size: 231790582
  dataset_size: 1232856541
language:
- da
tags:
- word frequencies
pretty_name: DAGW Word Frequencies (by domain)
---

# Dataset Card for DAGW Word Frequencies (by domain)

- **Paper:**  Derczynski, L., Ciosici, M. R., Baglini, R., Christiansen, M. H., Dalsgaard, J. A., Fusaroli, R., ... & Varab, D. (2021). The Danish Gigaword Corpus. In Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa) (pp. 413-421).
- **Point of Contact:** Kenneth Enevoldsen (Kennethcenevoldsen (at) gmail (dot) com )


This is a list of word frequencies derived from the Danish Gigaword (collected before 2022-22-01).
These word frequencies are derived from tokens from the Danish Gigaword Corpus, which have been tokenized using
the spacy pipeline for Danish `"da_core_news_lg"` using `spacy>=3.0.0,<3.4.0`.
See the notebook ["convert_to_hf_dataset.ipynb"](https://huggingface.co/datasets/chcaa/dagw-word-frequencies/blob/main/convert_to_hf_dataset.ipynb) and [wordfreq.py](https://huggingface.co/datasets/chcaa/dagw-word-frequencies/blob/main/wordfreq.py) for more information about how it was created.


# Dataset formats

This dataset have been created in four formats:

- [`chcaa/dagw-word-frequencies`](https://huggingface.co/datasets/chcaa/dagw-word-frequencies): Danish word frequencies from Danish Gigaword.
- [`chcaa/dagw-word-frequencies-by-domain`](https://huggingface.co/datasets/chcaa/dagw-word-frequencies-by-domain): word frequencies pr. domain.
- [`chcaa/dagw-word-frequencies-by-domain-with-pos-tags`](https://huggingface.co/datasets/chcaa/dagw-word-frequencies-by-domain-with-pos-tags): word frequencies pr. domain with their part-of-speech tags derived from the spacy pipeline for Danish `"da_core_news_lg"`.
- [`chcaa/dagw-word-frequencies-normalized-by-domain`](https://huggingface.co/datasets/chcaa/dagw-word-frequencies-normalized-by-domain): word frequencies pr. domain normalized by the top-level domain.


## Dataset Creation

### Curation Rationale

Word frequencies of large domains har often used to calculate metrics such as text entropy or word surprise. Word frequencies can also be used to to create stopword lists and similar.

### Source Data

The frequencies are derived from the Danish Gigaword. To read more about the Danish Gigaword and its content please check out the entry on [Danish language resources](https://sprogressource.digst.govcloud.dk/dataset/danish-gigaword), which also links to latest publications.


### Discussion of Biases

This dataset contains notably different distributions of the original domains; for instance, the legal domain is highly overrepresented within this corpus.
Please see the [normalized version](https://huggingface.co/datasets/chcaa/dagw-word-frequencies-normalized-by-domain) of this dataset if you wish to see word
frequencies which normalized across domains.

### Other Known Limitations

The news data within this corpus ("danavis") have altered the text, this is described further in the original version (v1) of [paper](https://arxiv.org/abs/2005.03521v1).


### Licensing Information

Below follows a brief overview of the sources in the corpus along with their individual license.

| Source            | License                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| adl               | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| botxt             | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cc                | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| danavis           | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| dannet            | [dannet license](https://cst.ku.dk/projekter/dannet/license.txt)                                                                                                                                                                                                                                                                                                                                                                                                                    |
| depbank           | Attribution-ShareAlike 4.0 International                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ep                | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ft                | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| gutenberg         | [gutenberg license](https://www.gutenberg.org/policy/license.html)                                                                                                                                                                                                                                                                                                                                                                                                                  |
| hest              | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jvj               | Attribution-ShareAlike 4.0 International                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| naat              | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| opensub           | The data set comes with the same license as the original sources. Please, check the information about the source that is given on http://opus.nlpl.eu/OpenSubtitles-v2018.php                                                                                                                                                                                                                                                                                                       |
| relig             | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| retsinformationdk | Danish Copyright law at https://www.retsinformation.dk/forms/r0710.aspx?id=164796 states "§ 9. Love, administrative forskrifter, retsafgørelser og lignende offentlige aktstykker er ikke genstand for ophavsret. Stk. 2. Bestemmelsen i stk. 1 gælder ikke for værker, der fremtræder som selvstændige bidrag i de i stk. 1 nævnte aktstykker. Sådanne værker må dog gengives i forbindelse med aktstykket. Retten til videre udnyttelse afhænger af de i øvrigt gældende regler." |
| retspraksis       | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| skat              | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| spont             | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| synne             | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| tv2r              | The owner of this content is TV2 Regionerne, Denmark. Creative Commons Attribution 4.0 International                                                                                                                                                                                                                                                                                                                                                                                |
| wiki              | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| wikibooks         | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| wikisource        | Creative Commons Legal Code 1.0 Universal      


### Contributions

Thanks to [@KennethEnevoldsen](https://github.com/KennethEnevoldsen) for adding this dataset.