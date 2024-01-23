---
language:
- de
---

# Germeval Task 2017: Shared Task on Aspect-based Sentiment in Social Media Customer Feedback

In the connected, modern world, customer feedback is a valuable source for insights on the quality of products or services. This feedback allows other customers to benefit from the experiences of others and enables businesses to react on requests, complaints or recommendations. However, the more people use a product or service, the more feedback is generated, which results in the major challenge of analyzing huge amounts of feedback in an efficient, but still meaningful way.

Thus, we propose a shared task on automatically analyzing customer reviews about “Deutsche Bahn” - the german public train operator with about two billion passengers each year.

Example: 

> “RT @XXX: Da hört jemand in der Bahn so laut ‘700 Main Street’ durch seine Kopfhörer, dass ich mithören kann. :( :( :(“

As shown in the example, insights from reviews can be derived on different granularities. The review contains a general evaluation of the travel (The customer disliked the travel). Furthermore, the review evaluates a dedicated aspect of the train travel (“laut” → customer did not like the noise level).

Consequently, we frame the task as aspect-based sentiment analysis with four sub tasks:

## Data format

```
ID <tab> Text <tab> Relevance <tab> Sentiment <tab> Aspect:Polarity (whitespace separated)
```

## Links

- http://ltdata1.informatik.uni-hamburg.de/germeval2017/
- https://sites.google.com/view/germeval2017-absa/

## How to cite

```bibtex
@inproceedings{germevaltask2017,
title = {{GermEval 2017: Shared Task on Aspect-based Sentiment in Social Media Customer Feedback}},
author = {Michael Wojatzki and Eugen Ruppert and Sarah Holschneider and Torsten Zesch and Chris Biemann},
year = {2017},
booktitle = {Proceedings of the GermEval 2017 – Shared Task on Aspect-based Sentiment in Social Media Customer Feedback},
address={Berlin, Germany},
pages={1--12}
}
```