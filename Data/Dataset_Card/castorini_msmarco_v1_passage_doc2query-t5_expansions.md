---
language:
  - English

license: "Apache License 2.0"
---
# Dataset Summary
The repo provides queries generated for the MS MARCO V1 passage corpus with docTTTTTquery (sometimes written as docT5query or doc2query-T5), the latest version of the doc2query family of document expansion models. The basic idea is to train a model, that when given an input document, generates questions that the document might answer (or more broadly, queries for which the document might be relevant). These predicted questions (or queries) are then appended to the original documents, which are then indexed as before. The docTTTTTquery model gets its name from the use of T5 as the expansion model.

# Dataset Structure

All three folds (train, dev and test) share the same corpus. The queries are generated from this corpus.

An example data entry looks as follows:
```
{  
    "id": "0", 
    "predicted_queries": ["what was important to the success of the manhattan project", "why was the manhattan project important?", "what was important about the manhattan project", "why was the success of the manhattan project so important?", "who was the manhattan project a scientific project for", "what was the manhattan project important for", "why was the manhattan project a success", "how was the success of the manhattan project", "why was the manhattan project important to the success of the project?", "what is the importance of communication amongst scientific minds", "what was the importance of scientific communication for the success of the manhattan project", "what was the purpose of the manhattan project", "why was the manhattan project significant?", "why was the manhattan project important", "why did scientists believe in atomic power", "why did scientists and engineers have to communicate?", "why was the manhattan project a success", "what was the purpose of the manhattan project", "why did scientists and engineers want to be involved in the manhattan project", "why are the scientists so valuable", "which of the following was an important outcome of the manhattan project?", "why was the manhattan project successful", "why was the manhattan project an important scientific achievement", "what was the success of manhattan", "what was the result of the manhattan project", "why was communications important to the success of the manhattan project?", "why the manhattan project was important", "why is it important to know who is the manhattan project", "what was the most important accomplishment to the success of the manhattan project?", "why was the manhattan project an important achievement?", "why was the manhattan project important to the success of the atomic bomb", "how did the manhattan project impact scientists?", "what were the effects of the manhattan project", "what were the results of the manhattan project and how did they affect the public", "what was the manhattan project", "why did scientists contribute to the success of the manhattan project", "why was communication important in the manhattan project", "what was the effect of the manhattan project on the world", "what was the importance of communication in the success of the manhattan project?", "why was communications important to the success of the manhattan project?", "why was the manhattan project important", "what was the manhattan project", "why was the success of the manhattan project important", "why was manhattan project a success", "what was important about the manhattan project", "what benefited from the success of the new york nuclear bomb", "what was the significance to the success of the manhattan project?", "why is communication important", "why was the manhattan project an important achievement", "why did the manhattan project work", "what was the manhattan project's success", "what was the significance of the manhattan experiment", "how important was communication to the success of the manhattan project", "why is communication important to the success of the manhattan project?", "what was the importance of the manhattan project", "why did scientists believe the manhattan project had the greatest impact on science?", "what was a critical effect of the manhattan project?", "why did the manhattan project succeed", "what was the importance of the manhattan project", "why was the manhattan project important", "why was the manhattan project a success?", "what was the importance of communication and communication during the manhattan project", "why was the manhattan project significant?", "what was the importance of communication in the manhattan project?", "why was communication important to the success of the manhattan project?", "why was the manhattan project an important achievement", "what was important about the manhattan project", "why was the manhattan project a success", "why were the scientists at the manhattan project so successful?", "why did the manhattan project really work", "what was the success of the manhattan project", "what is the importance of communication during the manhattan project", "why was the manhattan project important", "why was communication important?", "what was the importance of communication in the success of the manhattan project?", "why was the manhattan project successful?", "which statement reflects the success of the manhattan project?", "why did the manhattan project succeed", "why was the manhattan project a great success", "why was the manhattan project important"]
}
```
# Load Dataset
An example to load the dataset:
```
dataset = load_dataset('castorini/msmarco_v1_passage_doc2query-t5_expansions', data_files='d2q.jsonl.gz')
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
