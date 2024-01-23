---
license: cc-by-4.0
---

# MiCRO: Multi-interest Candidate Retrieval Online
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg?style=flat-square)](http://makeapullrequest.com)
[![arXiv](https://img.shields.io/badge/arXiv-2201.11675-b31b1b.svg)](https://arxiv.org/abs/2210.16271)

This repo contains the TwitterFaveGraph dataset from our paper [MiCRO: Multi-interest Candidate Retrieval Online](). <br />
[[PDF]](https://arxiv.org/pdf/2210.16271.pdf)
[[HuggingFace Datasets]](https://huggingface.co/Twitter)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## TwitterFaveGraph

TwitterFaveGraph is a bipartite directed graph of user nodes to Tweet nodes where an edge represents a "fave" engagement. Each edge is binned into predetermined time chunks which are assigned as ordinals. These ordinals are contiguous and respect time ordering. In total TwitterFaveGraph has 6.7M user nodes, 13M Tweet nodes, and 283M edges. The maximum degree for users is 100 and the minimum degree for users is 1. The maximum
degree for Tweets is 280k and the minimum degree for Tweets is 5.

The data format is displayed below.

| user_index | tweet_index | time_chunk |
| ------------- | ------------- |  ---- |
| 1   | 2 | 1 |
| 2   | 1 | 1 |
| 3   | 3 | 2 |

## Citation
If you use TwitterFaveGraph in your work, please cite the following:
```bib
@article{portman2022micro,
  title={MiCRO: Multi-interest Candidate Retrieval Online},
  author={Portman, Frank and Ragain, Stephen and El-Kishky, Ahmed},
  journal={arXiv preprint arXiv:2210.16271},
  year={2022}
}
```