---
dataset_info:
  features:
  - name: audio
    dtype: audio
  - name: transcription
    dtype: string
  splits:
  - name: train
    num_bytes: 308051793.096
    num_examples: 1722
  download_size: 302072835
  dataset_size: 308051793.096
---
# Dataset Card for "synthetic_compassion_wav"
Synthetic compassion is a dataset consisting of generated compassionate speech for meditation and psychology advice. 
The dataset consists of unique voices as each audio file has its own synthetic voice.
The speech is generated with Tortoise TTS

## How to use
Here is how you can load the dataset
```python
from datasets import load_dataset
dataset = load_dataset("birgermoell/synthetic_compassion_wav")
```