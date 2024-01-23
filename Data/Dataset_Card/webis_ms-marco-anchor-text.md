# Webis MS MARCO Anchor Text 2022

The [Webis MS MARCO Anchor Text 2022 dataset](https://webis.de/data/webis-ms-marco-anchor-text-22.html) enriches Version 1 and 2 of the document collection of [MS MARCO](https://microsoft.github.io/msmarco/) with anchor text extracted from six [Common Crawl](https://commoncrawl.org/) snapshots. The six Common Crawl snapshots cover the years 2016 to 2021 (between 1.7-3.4 billion documents each). We sampled  1,000 anchor texts for documents with more than 1,000 anchor texts at random and all anchor texts for documents with less than 1,000 anchor texts (this sampling yields that all anchor text is included for 94% of the documents in Version 1 and 97% of documents for Version 2). Overall, the MS MARCO Anchor Text 2022 dataset enriches 1,703,834 documents for Version 1 and 4,821,244 documents for Version 2 with anchor text.

Cleaned versions of the MS MARCO Anchor Text 2022 dataset are available in [ir_datasets](https://github.com/allenai/ir_datasets/issues/154), [Zenodo](https://zenodo.org/record/5883456) and [Hugging Face](https://huggingface.co/datasets/webis/ms-marco-anchor-text). The raw dataset with additional information and all metadata for the extracted anchor texts (roughly 100GB) is available on [Hugging Face](https://huggingface.co/datasets/webis/ms-marco-anchor-text/tree/main/ms-marco-v1/anchor-text) and [files.webis.de](https://files.webis.de/data-in-progress/ecir22-anchor-text/anchor-text-samples/).

The details of the construction of the Webis MS MARCO Anchor Text 2022 dataset are described in the [associated paper](https://webis.de/publications.html#froebe_2022a). If you use this dataset, please cite
```
@InProceedings{froebe:2022a,
  address =               {Berlin Heidelberg New York},
  author =                {Maik Fr{\"o}be and Sebastian G{\"u}nther and Maximilian Probst and Martin Potthast and Matthias Hagen},
  booktitle =             {Advances in Information Retrieval. 44th European Conference on IR Research (ECIR 2022)},
  editor =                {Matthias Hagen and Suzan Verberne and Craig Macdonald and Christin Seifert and Krisztian Balog and Kjetil N{\o}rv\r{a}g and Vinay Setty},
  month =                 apr,
  publisher =             {Springer},
  series =                {Lecture Notes in Computer Science},
  site =                  {Stavanger, Norway},
  title =                 {{The Power of Anchor Text in the Neural Retrieval Era}},
  year =                  2022
}
```
