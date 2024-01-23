---
pretty_name: WebGPT Comparisons
---
# Dataset Card for WebGPT Comparisons
## Dataset Description


In the [WebGPT paper](https://arxiv.org/abs/2112.09332), the authors trained a reward model from human feedback.
They used the reward model to train a long form question answering model to align with human preferences.
This is the dataset of all comparisons that were marked as suitable for reward modeling by the end of the WebGPT project.
There are 19,578 comparisons in total.

Each example in the dataset contains a pair of model answers for a question, and the associated metadata.
Each answer has a preference score from humans that can be used to determine which of the two answers are better.
Overall, an example has the following fields:

* `question`: The text of the question, together with the name of the dataset from which it was taken and a unique ID.
* `quotes_0`: The extracts that the model found while browsing for `answer_0`, together with the title of the page on which the extract was found, constructed from the HTML title and domain name of the page.
* `answer_0`: The final answer that the model composed using `quotes_0`.
* `tokens_0`: The prefix that would have been given to the model in the final step of the episode to create `answer_0`, and the completion given by the model or human. The prefix is made up of the question and the quotes, with some truncation, and the completion is simply the answer. Both are tokenized using the GPT-2 tokenizer. The concatenation of the prefix and completion is the input used for reward modeling.
* `score_0`: The strength of the preference for `answer_0` over `answer_1` as a number from −1 to 1. It sums to 0 with `score_1`, and an answer is preferred if and only if its score is positive. For reward modeling, we treat scores of 0 as soft 50% labels, and all other scores as hard labels (using only their sign).
* `quotes_1`: The counterpart to `quotes_0`.
* `answer_1`: The counterpart to `answer_0`.
* `tokens_1`: The counterpart to `tokens_0`.
* `score_1`: The counterpart to `score_0`.

This information was found in Appendix K of the WebGPT paper.

## Citation Information

[https://arxiv.org/abs/2112.09332](https://arxiv.org/abs/2112.09332)

```
@inproceedings{nakano2021webgpt,
  author = {Reiichiro Nakano and Jacob Hilton and Suchir Balaji and Jeff Wu and Long Ouyang and Christina Kim and Christopher Hesse and Shantanu Jain and Vineet Kosaraju and William Saunders and Xu Jiang and Karl Cobbe and Tyna Eloundou and Gretchen Krueger and Kevin Button and Matthew Knight and Benjamin Chess and John Schulman},
  title = {WebGPT: Browser-assisted question-answering with human feedback},
  booktitle = {arXiv},
  year = 2021,
}
```

Dataset added to the Hugging Face Hub by [@Tristan](https://huggingface.co/Tristan) and [@natolambert](https://huggingface.co/natolambert)