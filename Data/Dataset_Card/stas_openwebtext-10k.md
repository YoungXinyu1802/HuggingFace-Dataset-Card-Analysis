10K slice of OpenWebText - An open-source replication of the WebText dataset from OpenAI.

This is a small subset representing the first 10K records from the original dataset - created for testing.

The full 8M-record dataset is [here](https://huggingface.co/datasets/openwebtext).

```
$ python -c "from datasets import load_dataset; ds=load_dataset('stas/openwebtext-10k'); print(ds)"
DatasetDict({
    train: Dataset({
        features: ['text'],
        num_rows: 10000
    })
})
```

* Records: 10,000
* compressed size: ~15MB
* uncompressed size: 50MB

To convert to jsonlines:

```
from datasets import load_dataset
dataset_name = "stas/openwebtext-10k"
name = dataset_name.split('/')[-1]
ds = load_dataset(dataset_name, split='train')
ds.to_json(f"{name}.jsonl", orient="records", lines=True)
```

To see how this subset was created, here is the [instructions file](https://huggingface.co/datasets/stas/openwebtext-10k/blob/main/process.txt).
