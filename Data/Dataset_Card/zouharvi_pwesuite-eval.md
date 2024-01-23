---
language:
- en
- am
- bn
- sw
- uz
- es
- pl
- fr
- de
multilinguality:
- multilingual
tags:
- words
- word
- embedding
- phonetic
- phonological
- cognates
- rhyme
- analogy
pretty_name: 'PWESuite Evaluation v1'
size_categories:
- 100K<n<1M
dataset_info:
  features:
  - name: token_ort
    dtype: string
  - name: token_ipa
    dtype: string
  - name: token_arp
    dtype: string
  - name: lang
    dtype: string
  - name: purpose
    dtype: string
  splits:
  - name: train
    num_examples: 1330692
---

# PWESuite-Eval

Dataset composed of multiple smaller datasets used for the evaluation of phonetic word embeddings.
Further description, usage and paper link TODO.

Used datasets:
- [CMU Pronunciation dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict)
- [CC-100](https://data.statmt.org/cc-100/)
- [CogNet v0](https://aclanthology.org/P19-1302/)
- [Vitz and Winkler (1973)](https://www.sciencedirect.com/science/article/pii/S0022537173800167)

Authors:
- Vilém Zouhar (ETH Zürich, [contact](mailto:vzouhar@ethz.ch))
- Kalvin Chang (CMU LTI, [contact](mailto:kalvinc@cs.cmu.edu))
- Chenxuan Cui (CMU LTI, [contact](mailto:cxcui@cs.cmu.edu))
- Nathaniel Robinson (CMU LTI, [contact](mailto:nrrobins@cs.cmu.edu))
- Nathaniel Carlson (BYU, [contact](mailto:natec18@byu.edu))
- David Mortensen (CMU LTI, [contact](mailto:dmortens@cs.cmu.edu))
