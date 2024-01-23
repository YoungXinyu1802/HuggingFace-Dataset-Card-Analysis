---
license: mit
---

# diwank/silicone-merged

> Merged and simplified dialog act datasets from the [silicone collection](https://huggingface.co/datasets/silicone/)

All of the subsets of the original collection have been filtered (for errors and ambiguous classes), merged together and grouped into pairs of dialog turns. It is hypothesized that training dialog act classifier by including the previous utterance can help models pick up additional contextual cues and be better at inference esp if an utterance pair is provided.

## Example training script

```python
from datasets import load_dataset
from simpletransformers.classification import (
    ClassificationModel, ClassificationArgs
)

# Get data
silicone_merged = load_dataset("diwank/silicone-merged")

train_df = silicone_merged["train"]
eval_df = silicone_merged["validation"]

model_args = ClassificationArgs(
    num_train_epochs=8,
    model_type="deberta", 
    model_name="microsoft/deberta-large",
    use_multiprocessing=False,
    evaluate_during_training=True,
)

# Create a ClassificationModel
model = ClassificationModel("deberta", "microsoft/deberta-large", args=model_args, num_labels=11)  # 11 labels in this dataset

# Train model
model.train_model(train_df, eval_df=eval_df)
```

## Balanced variant of the training set

**Note**: This dataset is highly imbalanced and it is recommended to use a library like [imbalanced-learn](https://imbalanced-learn.org/stable/) before proceeding with training.

Since, balancing can be complicated and resource-intensive, we have shared a balanced variant of the train set that was created via oversampling using the _imbalanced-learn_ library. The balancing used the `SMOTEN` algorithm to deal with categorical data clustering and was resampled on a 16-core, 60GB RAM machine. You can access it using:

```load_dataset("diwank/silicone-merged", "balanced")```

## Feature description

- `text_a`: The utterance prior to the utterance being classified. (Say for dialog with turns 1-2-3, if we are trying to find the dialog act for 2, text_a is 1)
- `text_b`: The utterance to be classified
- `labels`: Dialog act label (as integer between 0-10, as mapped below)

## Labels map

```python
[
    (0, 'acknowledge')
    (1, 'answer')
    (2, 'backchannel')
    (3, 'reply_yes')
    (4, 'exclaim')
    (5, 'say')
    (6, 'reply_no')
    (7, 'hold')
    (8, 'ask')
    (9, 'intent')
    (10, 'ask_yes_no')
]
```

*****

## Appendix

### How the original datasets were mapped:

```python
mapping = {
    "acknowledge": {
        "swda": [
            "aap_am",
            "b",
            "bk"
        ],
        "mrda": [],
        "oasis": [
            "ackn",
            "accept",
            "complete"
        ],
        "maptask": [
            "acknowledge",
            "align"
        ],
        "dyda_da": [
            "commissive"
        ]
    },
    "answer": {
        "swda": [
            "bf",
        ],
        "mrda": [],
        "oasis": [
            "answ",
            "informCont",
            "inform",
            "answElab",
            "directElab",
            "refer"
        ],
        "maptask": [
            "reply_w",
            "explain"
        ],
        "dyda_da": [
            "inform"
        ]
    },
    "backchannel": {
        "swda": [
            "ad",
            "bh",
            "bd",
            "b^m"
        ],
        "mrda": [
            "b"
        ],
        "oasis": [
            "backch",
            "selfTalk",
            "init"
        ],
        "maptask": ["ready"],
        "dyda_da": []
    },
    "reply_yes": {
        "swda": [
            "na",
            "aa"
        ],
        "mrda": [],
        "oasis": [
            "confirm"
        ],
        "maptask": [
            "reply_y"
        ],
        "dyda_da": []
    },
    "exclaim": {
        "swda": [
            "ft",
            "fa",
            "fc",
            "fp"
        ],
        "mrda": [],
        "oasis": [
            "appreciate",
            "bye",
            "exclaim",
            "greet",
            "thank",
            "pardon",
            "thank-identitySelf",
            "expressRegret"
        ],
        "maptask": [],
        "dyda_da": []
    },
    "say": {
        "swda": [
            "qh",
            "sd"
        ],
        "mrda": ["s"],
        "oasis": [
            "expressPossibility",
            "expressOpinion",
            "suggest"
        ],
        "maptask": [],
        "dyda_da": []
    },
    "reply_no": {
        "swda": [
            "nn",
            "ng",
            "ar"
        ],
        "mrda": [],
        "oasis": [
            "refuse",
            "negate"
        ],
        "maptask": [
            "reply_n"
        ],
        "dyda_da": []
    },
    "hold": {
        "swda": [
            "^h",
            "t1"
        ],
        "mrda": [
            "f"
        ],
        "oasis": [
            "hold"
        ],
        "maptask": [],
        "dyda_da": []
    },
    "ask": {
        "swda": [
            "qw",
            "qo",
            "qw^d",
            "br",
            "qrr"
        ],
        "mrda": [
            "q"
        ],
        "oasis": [
            "reqInfo",
            "reqDirect",
            "offer"
        ],
        "maptask": [
            "query_w"
        ],
        "dyda_da": [
            "question"
        ]
    },
    "intent": {
        "swda": [],
        "mrda": [],
        "oasis": [
            "informIntent",
            "informIntent-hold",
            "expressWish",
            "direct",
            "raiseIssue",
            "correct"
        ],
        "maptask": [
            "instruct",
            "clarify"
        ],
        "dyda_da": [
            "directive"
        ]
    },
    "ask_yes_no": {
        "swda": [
            "qy^d",
            "^g"
        ],
        "mrda": [],
        "oasis": [
            "reqModal"
        ],
        "maptask": [
            "query_yn",
            "check"
        ],
        "dyda_da": []
    }
}
```