---
license: afl-3.0
---
## MEDIQUA2012-MAS task

source data is available [here](https://github.com/abachaa/MEDIQA2021/tree/main/Task2)

des:

1. data features

Multiple Answer Summarization with:

* key: key of each question
* question: question
* text: merge all text of all answers (if it is train-split, a merge of article and section part)
* sum\_abs: abstractive multiple answer summarization 
* sum\_ext: extractive multiple answer summarization 

2. train\_article /  train\_sec

Same structure with train, but:

* train: text: merge all text of all answers (if it is train-split, a merge of article and section part)
* train\_article: text is a merge of all subanswers 's articles
* train\_sec: text is a merge of all subanswers 's sections
