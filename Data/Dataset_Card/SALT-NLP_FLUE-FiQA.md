---
license: cc-by-3.0
---
## Dataset Summary
- **Homepage:** https://sites.google.com/view/salt-nlp-flang
- **Models:** https://huggingface.co/SALT-NLP/FLANG-BERT
- **Repository:** https://github.com/SALT-NLP/FLANG

## FLUE
FLUE (Financial Language Understanding Evaluation) is a comprehensive and heterogeneous benchmark that has been built from 5 diverse financial domain specific datasets.

Sentiment Classification: [Financial PhraseBank](https://huggingface.co/datasets/financial_phrasebank)\
Sentiment Analysis, Question Answering: [FiQA 2018](https://huggingface.co/datasets/SALT-NLP/FLUE-FiQA)\
New Headlines Classification: [Headlines](https://www.kaggle.com/datasets/daittan/gold-commodity-news-and-dimensions)\
Named Entity Recognition: [NER](https://huggingface.co/datasets/SALT-NLP/FLUE-NER)\
Structure Boundary Detection: [FinSBD3](https://sites.google.com/nlg.csie.ntu.edu.tw/finweb2021/shared-task-finsbd-3)

## Dataset Structure
The FiQA dataset has a corpus, queries and qrels (relevance judgments file). They are in the following format:
- `corpus` file: a `.jsonl` file (jsonlines) that contains a list of dictionaries, each with three fields `_id` with unique document identifier, `title` with document title (optional) and `text` with document paragraph or passage. For example: `{"_id": "doc1", "title": "Albert Einstein", "text": "Albert Einstein was a German-born...."}`
- `queries` file: a `.jsonl` file (jsonlines) that contains a list of dictionaries, each with two fields `_id` with unique query identifier and `text` with query text. For example: `{"_id": "q1", "text": "Who developed the mass-energy equivalence formula?"}`
- `qrels` file: a `.tsv` file (tab-seperated) that contains three columns, i.e. the `query-id`, `corpus-id` and `score` in this order. Keep 1st row as header. For example: `q1 doc1 1`

