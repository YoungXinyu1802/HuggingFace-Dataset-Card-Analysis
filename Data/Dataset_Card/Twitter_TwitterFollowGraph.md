---
license: cc-by-4.0
---


# kNN-Embed: Locally Smoothed Embedding Mixtures For Multi-interest Candidate Retrieval
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg?style=flat-square)](http://makeapullrequest.com)
[![arXiv](https://img.shields.io/badge/arXiv-2201.11675-b31b1b.svg)](https://arxiv.org/pdf/2205.06205.pdf)

This repo contains the TwitterFaveGraph dataset from our paper [kNN-Embed: Locally Smoothed Embedding Mixtures For Multi-interest Candidate Retrieval](https://arxiv.org/pdf/2205.06205.pdf). <br />
[[PDF]]()
[[HuggingFace Datasets]](https://huggingface.co/Twitter)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## TwitterFollowGraph

TwitterFollowGraph is a bipartite directed graph of users (consumer) nodes to author (producer) nodes where an edge represents a user "following" an author engagement. Each edge is binned into predetermined time chunks which are denoted with ordinals. These ordinals are contiguous and respect time ordering of engagements. In total TwitterFollowGraph has 261𝑀 edges and 15.5𝑀 vertices, with a max-degree of 900𝐾 and a min-degree of 5.

The data format is displayed below.

| user_index | author_index | time_chunk |
| ------------- | ------------- |  ---- |
| 1   | 2 | 1 |
| 2   | 1 | 2 |
| 3   | 3 | 2 |

## Citation
If you use TwitterFollowGraph in your work, please cite the following:
```bib
@article{el2022knn,
  title={kNN-Embed: Locally Smoothed Embedding Mixtures For Multi-interest Candidate Retrieval},
  author={El-Kishky, Ahmed and Markovich, Thomas and Leung, Kenny and Portman, Frank and Haghighi, Aria and Xiao, Ying},
  journal={arXiv preprint arXiv:2205.06205},
  year={2022}
}
```