# A More Natural PersonaChat

## Dataset Summary

This dataset is a true-cased version of the PersonaChat dataset by Zhang et al. (2018).
The original PersonaChat dataset is all lower case, and has extra space around each
clause/sentence separating punctuation mark. This version of the dataset has more of a
natural language look, with sentence capitalization, proper noun capitalization, and
normalized whitespace. Also, each dialogue turn includes a pool of distractor
candidate responses, which can be used by a multiple choice regularization loss during
training.

As an example, here is an utterance from the original PersonaChat dataset:

```
"i really like celine dion . what about you ?"
```

In this dataset, that example is:

```
"I really like Celine Dion. What about you?"
```

## Languages

The text in the dataset is in English (**en**).

## Data Fields

Each instance of the dataset represents a conversational utterance that a
crowdworker made, while pretending to have a certain personality. Each instance has
these fields:

| Field Name    | Datatype       | Description                                                                                                                                                                                                                 |
|---------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `conv_id`       | int            | A unique identifier for the instance's conversation.                                                                                                                                                                        |
| `utterance_idx` | int            | The index of the instance in the conversation.                                                                                                                                                                              |
| `personality`   | list of string | Sentences describing the personality of the current speaker.                                                                                                                                                                |
| `history`       | list of string | The conversation's utterances so far, alternating between speakers with one utterance per speaker.                                                                                                                          |
| `candidates`    | list of string | A list of utterances including distractor utterances as well as the true utterance the speaker gave, given their personality and the conversation history thus far. The true utterance is always the last utterance in this list. |

## Dataset Curation

The dataset was sourced from HuggingFace's version of the dataset used in the code for their
ConvAI 2018 submission, which was described in their [blog article](https://medium.com/huggingface/how-to-build-a-state-of-the-art-conversational-ai-with-transfer-learning-2d818ac26313)
on that submission. This version of the dataset has had extra white spaces removed,
and a StanfordNLP [stanza](https://stanfordnlp.github.io/stanza/) NLP pipeline was
used to conduct part-of-speech tagging to identify proper nouns, which were then
capitalized. The pipeline was also used to conduct sentence segmentation, allowing
the beginning of sentences to then be capitalized. Finally, all instances of the
pronoun "I" were capitalized, along with its contractions.

## Citation Information

For the PersonaChat dataset, please cite:

```
@article{zhang2018personalizing,
  title={Personalizing dialogue agents: I have a dog, do you have pets too?},
  author={Zhang, Saizheng and Dinan, Emily and Urbanek, Jack and Szlam, Arthur and Kiela, Douwe and Weston, Jason},
  journal={arXiv preprint arXiv:1801.07243},
  year={2018}
}
```
