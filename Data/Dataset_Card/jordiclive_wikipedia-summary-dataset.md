
## Dataset Description

- **Repository:** https://github.com/tscheepers/Wikipedia-Summary-Dataset


### Dataset Summary

This is a dataset that can be used for research into machine learning and natural language processing. It contains all titles and summaries (or introductions) of English Wikipedia articles, extracted in September of 2017.

The dataset is different from the regular Wikipedia dump and different from the datasets that can be created by gensim because ours contains the extracted summaries and not the entire unprocessed page body. This could be useful if one wants to use the smaller, more concise, and more definitional summaries in their research. Or if one just wants to use a smaller but still diverse dataset for efficient training with resource constraints.

A summary or introduction of an article is everything starting from the page title up to the content outline.

### Citation Information

```
@mastersthesis{scheepers2017compositionality,
  author  = {Scheepers, Thijs}, 
  title   = {Improving the Compositionality of Word Embeddings},
  school  = {Universiteit van Amsterdam},
  year    = {2017},
  month   = {11},
  address = {Science Park 904, Amsterdam, Netherlands}
}
```