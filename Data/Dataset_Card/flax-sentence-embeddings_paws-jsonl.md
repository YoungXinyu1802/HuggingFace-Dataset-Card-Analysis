# Introduction
This dataset is a jsonl format for PAWS dataset from: https://github.com/google-research-datasets/paws. It only contains the `PAWS-Wiki Labeled (Final)` and 
`PAWS-Wiki Labeled (Swap-only)` training sections of the original PAWS dataset. Duplicates data are removed.

Each line contains a dict in the following format:

`{"guid": <id>, "texts": [anchor, positive]}` or 

`{"guid": <id>, "texts": [anchor, positive, negative]}`

positives_negatives.jsonl.gz: 24,723

positives_only.jsonl.gz: 13,487

**Total**: 38,210

## Dataset summary
[**PAWS: Paraphrase Adversaries from Word Scrambling**](https://github.com/google-research-datasets/paws)

This dataset contains 108,463 human-labeled and 656k noisily labeled pairs that feature the importance of modeling structure, context, and word order information for the problem of paraphrase identification. The dataset has two subsets, one based on Wikipedia and the other one based on the Quora Question Pairs (QQP) dataset.