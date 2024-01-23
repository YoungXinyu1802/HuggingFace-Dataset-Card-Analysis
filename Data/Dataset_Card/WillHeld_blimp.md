---
dataset_info:
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: two_prefix_prefix_good
    dtype: string
  - name: two_prefix_prefix_bad
    dtype: string
  - name: two_prefix_word
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pairID
    dtype: string
  - name: feature_name
    dtype: string
  splits:
  - name: train
    num_bytes: 15550503
    num_examples: 67000
  download_size: 4374212
  dataset_size: 15550503
---
# Dataset Card for "blimp"

HuggingFace Hub Upload of BLiMP: The Benchmark of Linguistic Minimal Pairs from https://github.com/alexwarstadt/blimp

If you use this dataset in your work, please cite the original authors and paper.

```
@article{warstadt2020blimp,
    author = {Warstadt, Alex and Parrish, Alicia and Liu, Haokun and Mohananey, Anhad and Peng, Wei and Wang, Sheng-Fu and Bowman, Samuel R.},
    title = {BLiMP: The Benchmark of Linguistic Minimal Pairs for English},
    journal = {Transactions of the Association for Computational Linguistics},
    volume = {8},
    number = {},
    pages = {377-392},
    year = {2020},
    doi = {10.1162/tacl\_a\_00321},
    URL = {https://doi.org/10.1162/tacl_a_00321},
    eprint = {https://doi.org/10.1162/tacl_a_00321},
    abstract = { We introduce The Benchmark of Linguistic Minimal Pairs (BLiMP),1 a challenge set for evaluating the linguistic knowledge of language models (LMs) on major grammatical phenomena in English. BLiMP consists of 67 individual datasets, each containing 1,000 minimal pairs—that is, pairs of minimally different sentences that contrast in grammatical acceptability and isolate specific phenomenon in syntax, morphology, or semantics. We generate the data according to linguist-crafted grammar templates, and human aggregate agreement with the labels is 96.4\%. We evaluate n-gram, LSTM, and Transformer (GPT-2 and Transformer-XL) LMs by observing whether they assign a higher probability to the acceptable sentence in each minimal pair. We find that state-of-the-art models identify morphological contrasts related to agreement reliably, but they struggle with some subtle semantic and syntactic phenomena, such as negative polarity items and extraction islands. }
}
```