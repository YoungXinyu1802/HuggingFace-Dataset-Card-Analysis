---
annotations_creators:
- machine-generated
language_creators:
- machine-generated
language:
- da
license:
- apache-2.0
multilinguality:
- translation
pretty_name: machine_translated_cnn_dailymail_da_small
size_categories:
- 1K<n<10K
source_datasets: []
task_categories:
- summarization
task_ids:
- news-articles-summarization
---

# Dataset Card for machine_translated_cnn_dailymail_da_small

### Dataset Summary

This dataset is a machine translated subset of the [CNN Dailymail Dataset](https://huggingface.co/datasets/ccdv/cnn_dailymail) into Danish. The dataset is translated using the [Helsinki-NLP/opus-mt-en-da](https://huggingface.co/Helsinki-NLP/opus-mt-en-da)-model. The dataset consists of 2872 articles with summaries with intended usage for Danish text summarisation.

## Dataset Structure

Machine translated articles (`article`) with corresponding summaries (`highlights`).
```
{
  'article': Value(dtype='string', id=None),
  'highlights': Value(dtype='string', id=None),
  'id': Value(dtype='string', id=None)
}
```

### Licensing Information
The dataset is released under the [Apache-2.0 License](http://www.apache.org/licenses/LICENSE-2.0). 