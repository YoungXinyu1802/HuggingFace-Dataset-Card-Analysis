# SCP Text+ Embeddings

This dataset is adapted from the [SCP 1to 7 corpus from Kaggle](https://www.kaggle.com/datasets/czzzzzzz/scp1to7)

We concatenated the title, state, text, and image captions columns. We also removed any rows that contained a deleted page, which trims the results down from 6999 -> 6618. 

The embeddings were generated using [sentence-transformers/multi-qa-mpnet-base-dot-v1](https://huggingface.co/sentence-transformers/multi-qa-mpnet-base-cos-v1)

Feel free to use the dataset for semantic search or text generation tasks! 