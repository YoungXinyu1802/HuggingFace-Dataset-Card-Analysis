---
task_categories:
- text-classification
---

Original source: https://github.com/openai/generating-reviews-discovering-sentiment

This dataset is different from the dataset distributed by GLUE, which means the metric **shouldn't be compared with the SST2 performance in GLUE**.

The description of SST2 dataset in the paper is the following.

> The Stanford Sentiment Treebank (SST)(Socher  et  al.,  2013) was created specifically to evaluate more complex compositional models of language. It is de-rived from the same base dataset as MR but was relabeledvia Amazon Mechanical and includes dense labeling of thephrases of parse trees computed for all sentences.  For thebinary  subtask,  this  amounts  to  76961  total  labels  com-pared to the 6920 sentence level labels. As a demonstrationof the capability of unsupervised representation learning tosimplify  data  collection  and  remove  preprocessing  steps,our reported results ignore these dense labels and computedparse trees, using only the raw text and sentence level la-bels
