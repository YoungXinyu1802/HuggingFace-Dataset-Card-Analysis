---
annotations_creators: []
language_creators: []
language:
- de
- en
- fr
- ru
- zh
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
- multilingual
pretty_name: MTEB Benchmark
---

# Dataset Card for MTEB Benchmark

## Dataset Description

- **Homepage:** https://github.com/embeddings-benchmark/mteb-draft
- **Repository:** https://github.com/embeddings-benchmark/mteb-draft
- **Paper:** soon
- **Leaderboard:** https://docs.google.com/spreadsheets/d/14P8bdEzsIgTGGlp9oOlMw-THrQbn2fYfZEkZV4NUBos
- **Point of Contact:** nouamane@huggingface.co

### Dataset Summary

MTEB is a heterogeneous benchmark that has been built from diverse tasks:
* BitextMining: [BUCC](https://comparable.limsi.fr/bucc2018/bucc2018-task.html), [Tatoeba](https://github.com/facebookresearch/LASER/tree/main/data/tatoeba/v1)
* Classification: [AmazonCounterfactualClassification](https://arxiv.org/abs/2104.06893), [AmazonPolarityClassification](https://dl.acm.org/doi/10.1145/2507157.2507163), [AmazonReviewsClassification](https://arxiv.org/abs/2010.02573), [Banking77Classification](https://arxiv.org/abs/2003.04807), [EmotionClassification](https://www.aclweb.org/anthology/D18-1404), [ImdbClassification](http://www.aclweb.org/anthology/P11-1015), [MassiveIntentClassification](https://arxiv.org/abs/2204.08582#:~:text=MASSIVE%20contains%201M%20realistic%2C%20parallel,diverse%20languages%20from%2029%20genera.), [MassiveScenarioClassification](https://arxiv.org/abs/2204.08582#:~:text=MASSIVE%20contains%201M%20realistic%2C%20parallel,diverse%20languages%20from%2029%20genera.), [MTOPDomainClassification](https://arxiv.org/pdf/2008.09335.pdf), [MTOPIntentClassification](https://arxiv.org/pdf/2008.09335.pdf), [ToxicConversationsClassification](https://www.kaggle.com/competitions/jigsaw-unintended-bias-in-toxicity-classification/overview), [TweetSentimentExtractionClassification](https://www.kaggle.com/competitions/tweet-sentiment-extraction/overview)
* Clustering: [ArxivClusteringP2P](https://www.kaggle.com/Cornell-University/arxiv), [ArxivClusteringS2S](https://www.kaggle.com/Cornell-University/arxiv), [BiorxivClusteringP2P](https://api.biorxiv.org/), [BiorxivClusteringS2S](https://api.biorxiv.org/), [MedrxivClusteringP2P](https://api.biorxiv.org/), [MedrxivClusteringS2S](https://api.biorxiv.org/), [RedditClustering](https://arxiv.org/abs/2104.07081), [RedditClusteringP2P](https://huggingface.co/datasets/sentence-transformers/reddit-title-body), [StackExchangeClustering](https://arxiv.org/abs/2104.07081), [StackExchangeClusteringP2P](https://huggingface.co/datasets/flax-sentence-embeddings/stackexchange_title_body_jsonl), [TwentyNewsgroupsClustering](https://scikit-learn.org/0.19/datasets/twenty_newsgroups.html)
* Pair Classification: [SprintDuplicateQuestions](https://www.aclweb.org/anthology/D18-1131/), [TwitterSemEval2015](https://alt.qcri.org/semeval2015/task1/), [TwitterURLCorpus](https://languagenet.github.io/)
* Reranking: [AskUbuntuDupQuestions](https://github.com/taolei87/askubuntu), [MindSmallReranking](https://www.microsoft.com/en-us/research/uploads/prod/2019/03/nl4se18LinkSO.pdf), [SciDocs](https://allenai.org/data/scidocs), [StackOverflowDupQuestions](https://www.microsoft.com/en-us/research/uploads/prod/2019/03/nl4se18LinkSO.pdf)
* Retrieval: [ArguAna](http://argumentation.bplaced.net/arguana/data), [ClimateFEVER](https://www.sustainablefinance.uzh.ch/en/research/climate-fever.html), [CQADupstackRetrieval](http://nlp.cis.unimelb.edu.au/resources/cqadupstack/), [DBPedia](https://github.com/iai-group/DBpedia-Entity/), [FEVER](https://fever.ai/), [FiQA2018](https://sites.google.com/view/fiqa/), [HotpotQA](https://hotpotqa.github.io/), [MSMARCO](https://microsoft.github.io/msmarco/), [MSMARCOv2](https://microsoft.github.io/msmarco/TREC-Deep-Learning.html), [NFCorpus](https://www.cl.uni-heidelberg.de/statnlpgroup/nfcorpus/), [NQ](https://ai.google.com/research/NaturalQuestions/), [QuoraRetrieval](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs), [SCIDOCS](https://allenai.org/data/scidocs), [SciFact](https://github.com/allenai/scifact), [Touche2020](https://webis.de/events/touche-20/shared-task-1.html), [TRECCOVID](https://ir.nist.gov/covidSubmit/index.html)
* STS: [BIOSSES](https://tabilab.cmpe.boun.edu.tr/BIOSSES/DataSet.html), [SICK-R](https://www.aclweb.org/anthology/S14-2001.pdf), [STS12](https://www.aclweb.org/anthology/S12-1051.pdf), [STS13](https://www.aclweb.org/anthology/S13-1004/), [STS14](http://alt.qcri.org/semeval2014/task10/), [STS15](http://alt.qcri.org/semeval2015/task2/), [STS16](http://alt.qcri.org/semeval2016/task1/), [STS17](http://alt.qcri.org/semeval2016/task1/), [STS22](https://competitions.codalab.org/competitions/33835), [STSBenchmark](http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark)
* Summarization: [SummEval](https://tabilab.cmpe.boun.edu.tr/BIOSSES/DataSet.html)

All these datasets have been preprocessed and can be used for your experiments.