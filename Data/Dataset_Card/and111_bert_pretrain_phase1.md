### Dataset Summary

Input data for the **first** phase of BERT pretraining (sequence length 128). All text is tokenized with [bert-base-uncased](https://huggingface.co/bert-base-uncased) tokenizer. 
Data is obtained by concatenating and shuffling [wikipedia](https://huggingface.co/datasets/wikipedia) (split: `20220301.en`) and [bookcorpusopen](https://huggingface.co/datasets/bookcorpusopen) datasets and running [reference BERT data preprocessor](https://github.com/google-research/bert/blob/master/create_pretraining_data.py) without masking and input duplication (`dupe_factor = 1`). Documents are split into sentences with the [NLTK](https://www.nltk.org/) sentence tokenizer (`nltk.tokenize.sent_tokenize`).

See the dataset for the **second** phase of pretraining: [bert_pretrain_phase2](https://huggingface.co/datasets/and111/bert_pretrain_phase2).