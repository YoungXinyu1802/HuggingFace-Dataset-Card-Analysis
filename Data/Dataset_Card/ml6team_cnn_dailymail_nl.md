---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- nl
license:
- mit
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- https://github.com/huggingface/datasets/tree/master/datasets/cnn_dailymail
task_categories:
- conditional-text-generation
task_ids:
- summarization
---
# Dataset Card for Dutch CNN Dailymail Dataset

## Dataset Description

- **Repository:** [CNN / DailyMail Dataset NL repository](https://huggingface.co/datasets/ml6team/cnn_dailymail_nl)

### Dataset Summary

The Dutch CNN / DailyMail Dataset is a machine-translated version of the English CNN / Dailymail dataset containing just over 300k unique news aticles as written by journalists at CNN and the Daily Mail.

Most information about the dataset can be found on the [HuggingFace page](https://huggingface.co/datasets/cnn_dailymail) of the original English version.

These are the basic steps used to create this dataset (+ some chunking):
```
load_dataset("cnn_dailymail", '3.0.0')
```
And this is the HuggingFace translation pipeline:
```
pipeline(
    task='translation_en_to_nl',
    model='Helsinki-NLP/opus-mt-en-nl',
    tokenizer='Helsinki-NLP/opus-mt-en-nl')
```

### Data Fields

- `id`: a string containing the heximal formated SHA1 hash of the url where the story was retrieved from
- `article`: a string containing the body of the news article 
- `highlights`: a string containing the highlight of the article as written by the article author

### Data Splits

The Dutch CNN/DailyMail dataset follows the same splits as the original English version and has 3 splits: _train_, _validation_, and _test_.

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         | 287,113                                     |
| Validation    | 13,368                                      |
| Test          | 11,490                                      |

