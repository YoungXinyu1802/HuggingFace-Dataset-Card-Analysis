# WMT16 English-Romanian Translation Data w/ further preprocessing

The original instructions are [here](https://github.com/rsennrich/wmt16-scripts/tree/master/sample).

This pre-processed dataset was created by running:

```
git clone https://github.com/rsennrich/wmt16-scripts
cd wmt16-scripts
cd sample
./download_files.sh
./preprocess.sh
```

It was originally used by  `transformers` [`finetune_trainer.py`](https://github.com/huggingface/transformers/blob/641f418e102218c4bf16fcd3124bfebed6217ef6/examples/seq2seq/finetune_trainer.py)

The data itself resides at https://cdn-datasets.huggingface.co/translation/wmt_en_ro.tar.gz

If you would like to convert it to jsonlines I've included a small script `convert-to-jsonlines.py` that will do it for you. But if you're using the `datasets` API, it will be done on the fly.
