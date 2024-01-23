---
tags:
- Tutorial
size_categories:
- n<1K
---

## Zero to One: Label Studio Tutorial Dataset

This dataset is used in the [Label Studio Zero to One Tutorial](https://hubs.ly/Q01CNlyy0). This dataset was originally provided by [Andrew Maas](https://ai.stanford.edu/~amaas/)([ref](https://ai.stanford.edu/~amaas/papers/wvSent_acl2011.bib)). This is an open and well-known dataset. The original dataset did have over 100,000 reviews.

### Parsing down 100,000 reviews to 100 reviews

To parse this dataset down to 100 reviews, (Chris Hoge)[https://huggingface.co/hogepodge] and myself((Erin Mikail Staples)[https://huggingface.co/erinmikail]) took the following steps.

It started by (writing a script)[https://s3.amazonaws.com/labelstud.io/datasets/IMDB_collect.py] that walked the directory structure to capture the data and metadata as rows of data. The data was written in randomized batches with rows corresponding to:

- 0 - 25,000: Labeled training data, with positive and negative sentiment mixed.
- 25,001 - 75000: Unlabeled training data.
- 75001 - 100,000: Labeled testing data, with positive and negative sentiment mixed.

These batches were also written out as separate files for convenience. Finally, the first 100 rows of each batch were written out as separate files to support faster loading for a streamlined learning experience.

Our thanks to Andrew Maas for having provided this free data set from their research.

## Did you try your hand at this tutorial?

We'd love to hear you share your results and how it worked out for you! 

Did you build something else with the data? 

Let us know! Join us in the (Label Studio Slack Community)[https://hubs.ly/Q01CNprb0] or drop us an (email)[mailto:community@labelstud.io]

## Enjoy what we're working on?

Drop us a star on (GitHub!)[https://hubs.ly/Q01CNp4W0]

