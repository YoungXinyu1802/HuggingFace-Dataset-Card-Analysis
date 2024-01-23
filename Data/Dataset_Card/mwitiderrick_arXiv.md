---
license: cc0-1.0
---
About Dataset

This is a subset of the ArXiv dataset from Kaggle 

https://www.kaggle.com/datasets/Cornell-University/arxiv

About ArXiv

For nearly 30 years, ArXiv has served the public and research communities by providing open access to scholarly articles, from the vast branches of physics to the many subdisciplines of computer science to everything in between, including math, statistics, electrical engineering, quantitative biology, and economics. This rich corpus of information offers significant, but sometimes overwhelming depth.

In these times of unique global challenges, efficient extraction of insights from data is essential. To help make the arXiv more accessible, we present a free, open pipeline on Kaggle to the machine-readable arXiv dataset: a repository of 1.7 million articles, with relevant features such as article titles, authors, categories, abstracts, full text PDFs, and more.

Our hope is to empower new use cases that can lead to the exploration of richer machine learning techniques that combine multi-modal features towards applications like trend analysis, paper recommender engines, category prediction, co-citation networks, knowledge graph construction and semantic search interfaces.

The dataset is freely available via Google Cloud Storage buckets (more info here). Stay tuned for weekly updates to the dataset!

ArXiv is a collaboratively funded, community-supported resource founded by Paul Ginsparg in 1991 and maintained and operated by Cornell University.

The release of this dataset was featured further in a Kaggle blog post here.


See here for more information.

ArXiv On Kaggle

Metadata

This dataset is a mirror of the original ArXiv data. Because the full dataset is rather large (1.1TB and growing), this dataset provides only a metadata file in the json format. This file contains an entry for each paper, containing:

id: ArXiv ID (can be used to access the paper, see below)
submitter: Who submitted the paper
authors: Authors of the paper
title: Title of the paper
comments: Additional info, such as number of pages and figures
journal-ref: Information about the journal the paper was published in
doi: [https://www.doi.org](Digital Object Identifier)
abstract: The abstract of the paper
categories: Categories / tags in the ArXiv system
versions: A version history

You can access each paper directly on ArXiv using these links:

https://arxiv.org/abs/{id}: Page for this paper including its abstract and further links
https://arxiv.org/pdf/{id}: Direct link to download the PDF
License
Creative Commons CC0 1.0 Universal Public Domain Dedication applies to the metadata in this dataset. See https://arxiv.org/help/license for further details and licensing on individual papers.

Acknowledgements

The original data is maintained by ArXiv, huge thanks to the team for building and maintaining this dataset.

We're using https://github.com/mattbierbaum/arxiv-public-datasets to pull the original data, thanks to Matt Bierbaum for providing this tool.