# WMT14 English-German Translation Data w/ further preprocessing

The original pre-processing script is [here](https://github.com/pytorch/fairseq/blob/master/examples/translation/prepare-wmt14en2de.sh).

This pre-processed dataset was created by running:

```
git clone https://github.com/pytorch/fairseq
cd fairseq
cd examples/translation/
./prepare-wmt14en2de.sh
```

It was originally used by  `transformers` [`finetune_trainer.py`](https://github.com/huggingface/transformers/blob/641f418e102218c4bf16fcd3124bfebed6217ef6/examples/seq2seq/finetune_trainer.py)

The data itself resides at https://cdn-datasets.huggingface.co/translation/wmt_en_de.tgz
