# HotpotQA-extended

> Version of the HotpotQA dataset with full Wikipedia articles.

The HotpotQA dataset consists of questions from crowd workers which require information from multiple Wikipedia  articles in order to answer,thus  testing  the  ability  for  models  to  perform  multi-hop question answering. The data is commonly presented as a list of paragraphs containing relevant information plus a setting where the addition of ’distractor paragraphs’ fully test the ability of the model to comprehend which information is relevant to the question asked.

In this dataset, we increase the length of the inputs by expanding each paragraph with its full Wikipedia page  as well as adding additional distractor articles from similar topics in order to meet the 10,000 token minimum length requirement for this benchmark.