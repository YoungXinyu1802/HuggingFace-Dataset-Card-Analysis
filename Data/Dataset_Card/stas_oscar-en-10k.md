---
language:
  - en
license: apache-2.0
---

# OSCAR EN 10K for testing

This is a small subset representing the 10K records from the original OSCAR dataset, "unshuffled_deduplicated_en" subset - created for testing. The records were extracted after having been shuffled.

The full 1TB+ dataset is at https://huggingface.co/datasets/oscar.

```
$ python -c "from datasets import load_dataset; ds=load_dataset('stas/oscar-en-10k'); print(ds)"
DatasetDict({
    train: Dataset({
        features: ['text'],
        num_rows: 10000
    })
})
```

* Records: 10,000
* compressed size: ~37MB
* uncompressed size: 131MB

To convert to jsonlines:

```
from datasets import load_dataset
dataset_name = "stas/oscar-en-10k"
name = dataset_name.split('/')[-1]
ds = load_dataset(dataset_name, split='train')
ds.to_json(f"{name}.jsonl", orient="records", lines=True)
```

To see how this subset was created, here is the [instructions file](https://huggingface.co/datasets/stas/oscar-en-10k/blob/main/process.txt).
