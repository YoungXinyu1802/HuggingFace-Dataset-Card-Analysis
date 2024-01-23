---
language:
  - English

license: "Apache License 2.0"
---
# Dataset Summary
The repo provides queries generated for the MS MARCO V1 document segmented corpus with docTTTTTquery (sometimes written as docT5query or doc2query-T5), the latest version of the doc2query family of document expansion models. The basic idea is to train a model, that when given an input document, generates questions that the document might answer (or more broadly, queries for which the document might be relevant). These predicted questions (or queries) are then appended to the original documents, which are then indexed as before. The docTTTTTquery model gets its name from the use of T5 as the expansion model.

# Dataset Structure

All three folds (train, dev and test) share the same corpus.
An example data entry looks as follows:
```
{
    "id": "D1555982#0", "predicted_queries": ["when find radius of star r", "what is r radius", "how to find out radius of star", "what is radius r", "what is radius of r", "how do you find radius of star igel", "which law states that radiation is proportional to radiation?", "what is the radius of a spherical star", "what is the radius of the star", "what is radius of star"]
}
```
# Load Dataset
An example to load the dataset:
```
dataset = load_dataset('castorini/msmarco_v1_doc_segmented_doc2query-t5_expansions')
```
# Citation Information
```

@article{docTTTTTquery,
  title={From doc2query to {docTTTTTquery}},
  author={Nogueira, Rodrigo and Lin, Jimmy},
  year={2019}
}

@article{emdt5,
   author = "Ronak Pradeep and Rodrigo Nogueira and Jimmy Lin",
   title = "The Expando-Mono-Duo Design Pattern for Text Ranking with Pretrained Sequence-to-Sequence Models",
   journal = "arXiv:2101.05667",
   year = 2021,
}
