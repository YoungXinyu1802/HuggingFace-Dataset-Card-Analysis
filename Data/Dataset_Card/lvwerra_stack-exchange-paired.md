---
task_categories:
- text-generation
- question-answering
language:
- en
pretty_name: StackExchange Paired
size_categories:
- 10M<n<100M
---

# StackExchange Paired

This is a processed version of the [`HuggingFaceH4/stack-exchange-preferences`](https://huggingface.co/datasets/HuggingFaceH4/stack-exchange-preferences). The following steps were applied:

- Parse HTML to Markdown with `markdownify`
- Create pairs `(response_j, response_k)` where j was rated better than k
- Sample at most 10 pairs per question
- Shuffle the dataset globally

This dataset is designed to be used for preference learning. The processing notebook is in [the repository](https://huggingface.co/datasets/lvwerra/stack-exchange-paired/tree/main) as well.
