---
license: unknown
---

This sentiment dataset was used in the paper: John Blitzer, Mark Dredze, Fernando Pereira. Biographies, Bollywood, Boom-boxes and Blenders: Domain Adaptation for Sentiment Classification. Association of Computational Linguistics (ACL), 2007.

The author asks, if you use this data for your research or a publication, to cite the above paper as the reference for the data, and to inform him about the reuse.

The Multi-Domain Sentiment Dataset contains product reviews taken from Amazon.com from 4 product types (domains): Kitchen, Books, DVDs, and Electronics. Each domain has several thousand reviews, but the exact number varies by domain. Reviews contain star ratings (1 to 5 stars) that can be converted into binary labels if needed.

The directory contains 3 files called positive.review, negative.review and unlabeled.review. While the positive and negative files contain positive and negative reviews, these aren't necessarily the splits the authors used in the experiments. They randomly drew from the three files ignoring the file names. Each file contains a pseudo XML scheme for encoding the reviews. Most of the fields are self explanatory. The reviews have a "unique ID" field that isn't very unique. If it has two unique id fields, ignore the one containing only a number.