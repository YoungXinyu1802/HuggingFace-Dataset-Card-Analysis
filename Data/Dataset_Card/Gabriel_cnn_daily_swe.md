---
language:
- sv
license:
- mit
size_categories:
- 100K<n<1M
source_datasets:
- https://github.com/huggingface/datasets/tree/master/datasets/cnn_dailymail
task_categories:
- summarization
- text2text-generation
task_ids: []
tags:
- conditional-text-generation
---

# Dataset Card for Swedish CNN Dailymail Dataset
The Swedish CNN/DailyMail dataset has only been machine-translated to improve downstream fine-tuning on Swedish summarization tasks.

## Dataset Summary
Read about the full details at original English version: https://huggingface.co/datasets/cnn_dailymail
### Data Fields
- `id`: a string containing the heximal formated SHA1 hash of the url where the story was retrieved from
- `article`: a string containing the body of the news article 
- `highlights`: a string containing the highlight of the article as written by the article author

### Data Splits
The Swedish CNN/DailyMail dataset follows the same splits as the original English version and has 3 splits: _train_, _validation_, and _test_.

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         | 287,113                                     |
| Validation    | 13,368                                      |
| Test          | 11,490                                      |
