---
language:
- it
multilinguality:
- monolingual
size_categories:
- 8k<n<10k
task_categories:
- question-answering
task_ids:
- extractive-qa
---

# Squad-it
This dataset is an adapted version of that [squad-it](https://github.com/crux82/squad-it) to train on HuggingFace models.

It contains:
- train samples: 87599
- test samples : 10570

This dataset is for question answering and his format is the following:
```
[
  {
    "answers": [
      {
        "answer_start": [1],
        "text": ["Questo è un testo"]
      },
    ],
    "context": "Questo è un testo relativo al contesto.",
    "id": "1",
    "question": "Questo è un testo?",
    "title": "train test"
  }
]
```

It can be used to train many models like T5, Bert, Distilbert...