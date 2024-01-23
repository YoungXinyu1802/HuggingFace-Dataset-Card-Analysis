---
dataset_info:
  features:
  - name: audio
    dtype: audio
  - name: transcription
    dtype: string
  splits:
  - name: train
    num_bytes: 117098145
    num_examples: 439
  download_size: 111238398
  dataset_size: 117098145
license: mit
language:
- en
pretty_name: Synthetic Compassion
size_categories:
- n<1K
---
# Dataset Card for "synthetic_compassion"
Synthetic compassion is a dataset consisting of generated compassionate speech for meditation and psychology advice. 
The dataset consists of unique voices as each audio file has its own synthetic voice.
The speech is generated with Tortoise TTS

## How to use
Here is how you can load the dataset
```python
from datasets import load_dataset
dataset = load_dataset("birgermoell/synthetic_compassion")
```