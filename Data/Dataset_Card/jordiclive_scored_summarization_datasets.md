# Dataset Card for "Scored-Summarization-datasets"
A collection of Text summarization datasets geared towards training a multi-purpose text summarizer.

Each dataset is a parquet file with the following features.

#### default
- `text`: a `string` feature. The `source` document
- `summary`: a `string` feature. The summary of the document
- `provenance`: a `string` feature. Information about the sub dataset.
- `t5_text_token_count`: a `int64` feature. The number of tokens the text is encoded in.
- `t5_summary_token_count `: a `int64` feature. The number of tokens the summary is encoded in.
- `contriever_cos`: a `float64` feature. The Cosine Similarity of the Contriever text embedding and Contriever summary embedding.

### Sub-datasets
- billsum
- cnn_dailymail/3.0.0
- multixscience
- newsroom
- samsum
- scitldr/AIC
- tldr-challenge
- wikihow
- xsum

Information about the Contriever model can be found here: https://github.com/facebookresearch/contriever.
