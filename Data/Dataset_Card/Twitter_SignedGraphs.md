---
license: cc-by-4.0
---
# Learning Stance Embeddings from Signed Social Graphs
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg?style=flat-square)](http://makeapullrequest.com)
[![arXiv](https://img.shields.io/badge/arXiv-2201.11675-b31b1b.svg)](https://arxiv.org/abs/2201.11675)

This repo contains the datasets from our paper [Learning Stance Embeddings from Signed Social Graphs](https://arxiv.org/abs/2201.11675). <br />
[[PDF]](https://arxiv.org/pdf/2201.11675.pdf)
[[HuggingFace Datasets]](https://huggingface.co/Twitter)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Overview
A key challenge in social network analysis is understanding the position, or stance, of people in the graph on a large set of topics. In such social graphs, modeling (dis)agreement patterns across a range of correlated topics may be beneficial. For example, disagreement on one topic may make disagreement (or agreement) more likely for related topics. 

We open source **two Twitter signed, topical graph datasets**. One dataset, **TwitterSG**, labels (dis)agreements using engagements between users via tweets to derive topic-informed, signed edges. The other, **BirdwatchSG**,leverages community reports on misinformation and misleading content.

## Datasets

### TwitterSG

Twitter Signed Graph, or TwitterSG, is a signed, directed, edge-attributed graph of users, drawn from Twitter interactions. TwitterSG contains 753,944 nodes (users), 200 topics and 12,848,093 edges. It is the largest publicly available user-to-user signed social graph (∼6x larger than the Epinions graph).

A positive edge exists from user 𝐴 to user 𝐵 if user 𝐴 liked a tweet posted by user 𝐵. A negative edge exists from user 𝐴 to user 𝐵 if user 𝐴 expressed opposition towards user 𝐵’s tweet, e.g., by replying *I disagree with you*. The full list of opposition keywords is specified [here](https://github.com/lejohnyjohn/learning-stance-embeddings-from-signed-social-graphs/tree/main/datasets). The topic of an edge from user 𝐴 to user 𝐵 is determined by the topic of user 𝐵’s tweet. 

Tweets' topics were inferred with a topic classifier used in production by Twitter. The topics provided in the dataset are all related to sports (e.g., sports teams, players, managers, or events), and the tweets related to these interactions were published between 20th May (Ice Hockey World Championships) and 8th August 2021 (closing date of the 2020 Tokyo Olympic Games). 

9.6\% of edges are negative (opposition) and 90.4\% are positive. There may be several edges between two nodes (several interactions, several topics). The data format is displayed below.

| source_idx | target_idx | topic_idx | topic | rating |
| ------------- | ------------- | ---------- | ------ | ---- |
| 1   | 6 | 19 | Copa America | +1 |
| 1   | 6 | 97 | NFL | -1 |
| 4   | 5 | 23 |Kylian Mbappe | +1 |

### BirdwatchSG

Birdwatch Signed Graph, or BirdwatchSG, is a signed, directed, edge-attributed graph of users, drawn from note ratings on the Birdwatch pilot. The graph contains 2,987 nodes (users), 1,020 topics and 441,986 edges. 

[Birdwatch pilot](https://blog.twitter.com/en_us/topics/product/2021/introducing-birdwatch-a-community-based-approach-to-misinformation) was launched by Twitter in January 2021 in the USA to address misleading information on the platform, in a community-driven fashion: the Birdwatch participants can identify information they believe is misleading in tweets and write notes that provide informative context. They can also rate the helpfulness (either *helpful*, *somewhat helpful*, or *not helpful*) of notes added by other contributors. All Birdwatch contributions are publicly available on the [Birdwatch site](https://twitter.github.io/birdwatch/) for anyone in the USA.

Using Birdwatch data from January to July 2021, a positive (negative) edge is created from participant 𝑈1 to 𝑈2 if participant 𝑈1 rated a note written by participant 𝑈2 as *helpful* (*not helpful*). The *somewhat helpful* ratings were filtered out. The topic associated with an edge is the topic inferred from the tweet the note refers to.

36.9% of edges are negative (opposition) and 63.1% are positive. There may be several edges between two nodes (several interactions, several topics).

| source_idx | target_idx | topic_idx | topic | rating |
| ------------- | ------------- | ---------- | ------ | ---- |
| 10   | 6 | 443 | US Politics | +1 |
| 7   | 14 | 12 | Ted Cruz | -1 |
| 1   | 11 | 1003 | COVID-19 | +1 |

## Citation
If you use our datasets in your work, please cite the following:
```bib
@article{pougue2022learning,
  title={Learning Stance Embeddings from Signed Social Graphs},
  author={Pougu{\'e}-Biyong, John and Gupta, Akshay and Haghighi, Aria and El-Kishky, Ahmed},
  journal={arXiv preprint arXiv:2201.11675},
  year={2022}
}
```