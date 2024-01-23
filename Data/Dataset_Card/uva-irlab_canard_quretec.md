# Preprocessed CANARD
Voskarides et al. have trained a Query Resolution Term Classification (QuReTec) model using the CANARD data set.

CANARD is a dataset for question-in-context rewriting that consists of questions each given in a dialog context together with a context-independent rewriting of the question. The context of each question is the dialog utterences that precede the question. CANARD can be used to evaluate question rewriting models that handle important linguistic phenomena such as coreference and ellipsis resolution.

QuReTeC is trained to label the relevant terms in the conversation history for the current contextless question. The relevant terms are the terms that occur in both the rewritten question and the history. For example:

**History:** \
Where was Bennett born?\
Bennett was born Michael Bennett DiFiglia in Buffalo, New York. When  was he born? CANNOTANSWER \
**Current question**: \
Who are his parents? \
**Rewritten question**: \
Who are Michael Bennett's parents?

The **gold/relevant terms** from the question history are: michael, bennett

## Data subsets
This repository contains the following subsets:
- gold_supervision (default): \
  the gold terms are the overlapping terms between the question history from the rewritten question. 
- distant_supervision: \
  the gold terms are the overlapping terms between the question history and the passage in which the answer to question can be found.

## Data structure
Each entry contains the following keys:
```
prev_questions: string
  e.g.: Where was Bennett born? Bennett was born Michael Bennett DiFiglia in Buffalo, New York. When  was he born? CANNOTANSWER.
cur_question: string
  e.g.: Who are his parents?
gold_terms: string[]
  e.g.: ["michael", "bennett"]
bert_ner_overlap: 2-dimensional array. The first entry lists all the terms and the second end lists the labels for those terms.
  e.g.: [
  ["where", "was", "bennett", "born", "?", "bennett", "was", "born", "michael", "bennett", "difiglia", "in", "buffalo", ",", "new", "york", ".", "when", "was", "he", "born", "?", "cannotanswer", ".", "[SEP]", "who", "are", "his", "parents", "?"],
  ["O", "O", "REL", "O", "O", "REL", "O", "O", "REL", "REL", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "[SEP]", "O", "O", "O", "O", "O"]
  ]
answer_text_with_window: string.
  For the 'gold_supervision' subset this field contains the rewritten question, e.g.: Who are Michael Bennett's parents?
  For the 'distant_supervision' subset this field contains the relevant passage to the question: e.g.: Bennett was born Michael Bennett DiFiglia in Buffalo, New York, the son of Helen (nee Ternoff), a secretary, and Salvatore Joseph DiFiglia, a factory worker. Michael Bennett (theater)'s father was Roman Catholic and Italian American and Michael Bennett (theater)'s mother was Jewish. Michael Bennett (theater) studied dance and 
 ```

# Original authors

QuReTeC model from the published SIGIR 2020 paper: Query Resolution for Conversational Search with Limited Supervision by N. Voskarides, D. Li, P. Ren, E. Kanoulas and M. de Rijke. [[pdf]](https://arxiv.org/abs/2005.11723). 

# Contributions

Uploaded by G. Scheuer ([website](https://giguruscheuer.com))