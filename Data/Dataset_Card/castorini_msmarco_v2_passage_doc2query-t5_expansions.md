---
language: 
  - English
    
license: "Apache License 2.0"
---
# Dataset Summary
The repo provides queries generated for the MS MARCO v2 passage corpus with docTTTTTquery (sometimes written as docT5query or doc2query-T5), the latest version of the doc2query family of document expansion models. The basic idea is to train a model, that when given an input document, generates questions that the document might answer (or more broadly, queries for which the document might be relevant). These predicted questions (or queries) are then appended to the original documents, which are then indexed as before. The docTTTTTquery model gets its name from the use of T5 as the expansion model.

# Dataset Structure

All three folds (train, dev and test) share the same corpus. The queries are generated from this corpus.

An example data entry looks as follows:
```
{   "id": "msmarco_passage_22_0", 
    "predicted_queries": ["in drug combat does a zombie take more damage or die", "is the health bar the same as smash bros", "is brawlhalla health bar", "icpri league brawlhalla", "what is a battle brawlhalla", "is smash bros minecraft brawlhalla zombies", "what are the health bars on brawlhalla", "does smash bros have health bars", "is brawlhalla a health bar", "what is brawlhalla", "what is brwlhalla", "how many health bars is in brawlhalla", "is there health bar in brawlhalla", "what is boiledhalla?", "what is a good health bar in brawlhalla", "what is skills brawlhalla", "how many gobs in a brawlhalla", "is smash bros. an nsb game", "how many health bars are there in the brawlhalla", "what is brawlhalla"]
}
```
# Load Dataset
An example to load the dataset:
```
dataset = load_dataset('castorini/msmarco_v2_passage_doc2query-t5_expansions', data_files='d2q/d2q.jsonl???.gz')
```
# Citation Information
```

@article{docTTTTTquery,
  title={From doc2query to {docTTTTTquery}},
  author={Nogueira, Rodrigo and Lin, Jimmy},
  year={2019}
}

@article{emdt5,
   author={Ronak Pradeep and Rodrigo Nogueira and Jimmy Lin},
   title={The Expando-Mono-Duo Design Pattern for Text Ranking with Pretrained Sequence-to-Sequence Models},
   journal={arXiv:2101.05667},
   year={2021},
}

