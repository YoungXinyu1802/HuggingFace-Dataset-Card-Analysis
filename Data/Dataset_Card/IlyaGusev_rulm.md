---
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 44765634773
    num_examples: 11558373
  - name: test
    num_bytes: 225645511
    num_examples: 58638
  - name: validation
    num_bytes: 227568446
    num_examples: 58013
  download_size: 14178680811
  dataset_size: 45218848730
task_categories:
- text-generation
language:
- ru
size_categories:
- 10M<n<100M
---

# Dataset for training Russian language models

Overall: 44G

Scripts: https://github.com/IlyaGusev/rulm/tree/hf/data_processing

Contents:
- Librusec, 15%: 18G
- stihi.ru: 8.9G
- Wikipedia, 7.5G
- [News](https://github.com/buriy/russian-nlp-datasets/releases/tag/r4): 6.5G
- OpenSubtitles: 2.0G
- [DM math](https://github.com/mannefedov/mathematics_dataset_russian): 1.3G
- StackOverflow: 318M
- https://huggingface.co/datasets/IlyaGusev/gazeta
- https://huggingface.co/datasets/Tatyana/ru_sentiment_dataset
- https://huggingface.co/datasets/blinoff/medical_qa_ru_data
