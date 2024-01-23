Sentence representation plays a crucial role in NLP downstream tasks such as NLI, text classification, and STS. Recent sentence representation training techniques require NLI or STS datasets. However, there are no equivalent Thai NLI or STS datasets for sentence representation training.
To address this problem we provide the Thai sentence vector benchmark. We evaluate the Spearman correlation score of the sentence representations’ performance on Thai STS-B (translated version of [STS-B](https://github.com/facebookresearch/SentEval)).

# Thai semantic textual similarity benchmark
- We use [STS-B translated ver.](https://github.com/mrpeerat/Thai-Sentence-Vector-Benchmark/blob/main/sts-test_th.csv) in which we translate STS-B from [SentEval](https://github.com/facebookresearch/SentEval) by using google-translate.
- How to evaluate sentence representation: [SentEval.ipynb](https://github.com/mrpeerat/Thai-Sentence-Vector-Benchmark/blob/main/SentEval.ipynb) 
- How to evaluate sentence representation on Google Colab: https://colab.research.google.com/github/mrpeerat/Thai-Sentence-Vector-Benchmark/blob/main/SentEval.ipynb

| Base Model  | Spearman's Correlation (*100) | Supervised? |
| ------------- | :-------------: | :-------------: |
| [simcse-model-distil-m-bert](https://huggingface.co/mrp/simcse-model-distil-m-bert)  | 38.84  |
| [simcse-model-m-bert-thai-cased](https://huggingface.co/mrp/simcse-model-m-bert-thai-cased)  | 39.26  | 
| [simcse-model-roberta-base-thai](https://huggingface.co/mrp/simcse-model-roberta-base-thai)  | 62.60  | 
| [distiluse-base-multilingual-cased-v2](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v2)  | 63.50  | ✓
| [paraphrase-multilingual-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2)  | 80.11  | ✓