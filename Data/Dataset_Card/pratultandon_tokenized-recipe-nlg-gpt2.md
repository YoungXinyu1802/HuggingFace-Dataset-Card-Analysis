---
dataset_info:
  features:
  - name: input_ids
    sequence: int32
  - name: attention_mask
    sequence: int8
  splits:
  - name: test
    num_bytes: 135944246
    num_examples: 106202
  - name: train
    num_bytes: 2582090838
    num_examples: 2022671
  download_size: 805955428
  dataset_size: 2718035084
---
# Dataset Card for "tokenized-recipe-nlg-gpt2"

This a tokenized version of the recipe-nlg database from https://recipenlg.cs.put.poznan.pl/. 
The preprocessing on the original csv was done using the methodology of the original paper (best as I could interpret) along with a similar 0.05 percent train test split. The tokenizer used has some special tokens, but all these parameters are accessible in https://huggingface.co/pratultandon/recipe-nlg-gpt2 if you want to recreate. This dataset will save you a lot of time getting started if you want to experiment with training GPT2 on the data yourself. 

