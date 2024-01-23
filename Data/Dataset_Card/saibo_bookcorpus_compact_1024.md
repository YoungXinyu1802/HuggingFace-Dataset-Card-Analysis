---
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2753205189
    num_examples: 616051
  download_size: 1603181006
  dataset_size: 2753205189
size_categories:
- 100K<n<1M
---
# Dataset Card for "bookcorpus_compact_1024"

Num samples: 616,051

The number of tokens for each sequence is not exactly 1024, but all slightly shorter than 1024.
The sequences were built by merging sentences to the maximal length shorter than 1024 tokens.
Therefore, padding is necessary for batch processing.

```python
import time
from typing import List

from datasets import load_dataset, Dataset
from tqdm import tqdm
from transformers import AutoTokenizer


def batch_tokenize(texts: List[str], tokenizer, batch_size=1000):
    start = time.time()
    """Tokenize the texts in batch"""
    assert tokenizer.is_fast, "tokenizer must be fast tokenizer"
    tokenized_texts = []
    for i in tqdm(range(0, len(texts), batch_size)):
        batch = texts[i:i + batch_size]
        batch_encoding = tokenizer(batch)
        tokenized_texts.extend(batch_encoding["input_ids"])
    print(f"batch_tokenize time with bs={batch_size}: {time.time() - start}")
    return tokenized_texts


class CompactText:
    def __init__(self, tokenizer="gpt2", split="test", block_size=512):

        self.block_size = block_size
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer)

    def compact_load(self, dataset_name: str, split: str):
        dataset = load_dataset(dataset_name)[split]

        batch_encoding = batch_tokenize(dataset["text"], self.tokenizer, batch_size=10000)
        compact_texts = []
        texts = dataset["text"]

        total_num_tok = 0
        tracker = []
        i = 0
        for j in tqdm(range(len(batch_encoding))):
            total_num_tok += len(batch_encoding[j])
            if total_num_tok >= self.block_size:
                batch_sents = texts[i:j]
                big_sent = " ".join(batch_sents)
                compact_texts.append(big_sent)
                tracker.append((i, j))
                i = j
                total_num_tok = 0
                print(tracker)
        # self.examples = compact_texts
        compact_ds = Dataset.from_dict({"text": compact_texts})
        return compact_ds


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--block-size", type=int, default=512)
    args = parser.parse_args()
    compactifier = CompactText(block_size=args.block_size)
    dataset = compactifier.compact_load(dataset_name="saibo/bookcorpus_deduplicated", split="train")
    dataset.push_to_hub(f"saibo/bookcorpus_compact_{args.block_size}")

```


[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)