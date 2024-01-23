---
language:
- tr
size_categories:
- 100K<n<1M
source_datasets:
- nli_tr
task_categories:
- text-classification
task_ids:
- semantic-similarity-scoring
- text-scoring
---
# NLI-TR for Supervised SimCSE

This dataset is a modified version of [NLI-TR](https://huggingface.co/datasets/nli_tr) dataset. Its intended use is to train Supervised [SimCSE](https://github.com/princeton-nlp/SimCSE) models for sentence-embeddings. Steps followed to produce this dataset are listed below:
1. Merge train split of snli_tr and multinli_tr subsets.
2. Find every premise that has an entailment hypothesis **and** a contradiction hypothesis.
3. Write found triplets into sent0 (premise), sent1 (entailment hypothesis), hard_neg (contradiction hypothesis) format.

See this [Colab Notebook](https://colab.research.google.com/drive/1Ysq1SpFOa7n1X79x2HxyWjfKzuR_gDQV?usp=sharing) for training and evaluation on Turkish sentences.