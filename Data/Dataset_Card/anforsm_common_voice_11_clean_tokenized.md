---
license: cc0-1.0
language:
- en
task_categories:
- text-to-speech
- text-generation
pretty_name: Common Voice 11 (en) Cleaned and Tokenized
size_categories:
- 10K<n<100K
dataset_info:
  features:
  - name: input_ids
    sequence: int32
  - name: attention_mask
    sequence: int8
  - name: labels
    sequence: int64
  splits:
  - name: train
    num_bytes: 1109542776
    num_examples: 83274
  - name: validation
    num_bytes: 17374496
    num_examples: 1304
  download_size: 197852035
  dataset_size: 1126917272
---

A cleaned and tokenized version of the English data from [Mozilla Common Voice 11 dataset](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0/tree/main).

Cleaning steps:
* Filtered on samples with >2 upvotes and <1 downvotes]
* Removed non voice audio at start and end through pytorch VAD

Tokenization:
* Audio tokenized through [EnCodec by Meta](https://github.com/facebookresearch/encodec)
  * Using 24khz pre-trained model, and target bandwidth of 1.5
  * Represented in text as audio_token_0 - audio_token_1023
* Prompts constructed as "text: \<common voice transcript\>\naudio: \<audio tokens\>"
* Prompts tokenized with GPT tokenizer with added vocab of audio tokens.
* Tokenized prompts padded to size 1024 with eos_token.

Each sample has 3 properties: input_ids, attention_mask and labels. input_ids and labels are the tokenized prompts and attention_mask is the attention mask.