---
pretty_name: Summarize from Feedback
---
# Dataset Card for Summarize from Feedback
## Dataset Description


In the [Learning to Summarize from Human Feedback paper](https://arxiv.org/abs/2009.01325), a reward model was trained from human feedback.
The reward model was then used to train a summarization model to align with human preferences. This is the dataset of human feedback that was released for reward modelling.
There are two parts of this dataset: `comparisons` and `axis`. In the `comparisons` part, human annotators were asked to choose the best out of two summaries.
In the `axis` part, human annotators gave scores on a likert scale for the quality of a summary.
The `comparisons` part only has a train and validation split, and the `axis` part only has a test and validation split.

The summaries used for training the reward model in the paper come from the TL;DR dataset.
Additional validation and test data come from the TL;DR dataset, CNN articles, and Daily Mail articles.

For more information, see the repo [here](https://github.com/openai/summarize-from-feedback#human-feedback-data).

## Citation Information

[https://arxiv.org/abs/2009.01325](https://arxiv.org/abs/2009.01325)

```
@inproceedings{stienon2020learning,
  author = {Nisan Stiennon and Long Ouyang and Jeff Wu and Daniel M. Ziegler and Ryan Lowe and Chelsea Voss and Alec Radford and Dario Amodei and Paul Christiano},
  title = {Learning to summarize from human feedback},
  booktitle = {NeurIPS},
  year = 2020,
}
```

Dataset added to the Hugging Face Hub with help from [@Tristan](https://huggingface.co/Tristan)