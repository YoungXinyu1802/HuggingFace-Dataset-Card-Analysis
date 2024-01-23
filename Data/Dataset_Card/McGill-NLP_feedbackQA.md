---
license: apache-2.0
---

# Dataset Card for FeedbackQA

[📄 Read](https://arxiv.org/abs/2204.03025)<br>
[💾 Code](https://github.com/McGill-NLP/feedbackqa)<br>
[🔗 Webpage](https://mcgill-nlp.github.io/feedbackqa/)<br>
[💻 Demo](http://206.12.100.48:8080/)<br>
[🤗 Huggingface Dataset](https://huggingface.co/datasets/McGill-NLP/feedbackQA)<br>
[💬 Discussions](https://github.com/McGill-NLP/feedbackqa/discussions)

## Dataset Description

- **Homepage: https://mcgill-nlp.github.io/feedbackqa-data/**
- **Repository: https://github.com/McGill-NLP/feedbackqa-data/**
- **Paper:**
- **Leaderboard:**
- **Tasks: Question Answering**
### Dataset Summary

FeedbackQA is a retrieval-based QA dataset that contains interactive feedback from users. 
It has two parts: the first part contains a conventional RQA dataset, 
whilst this repo contains the second part, which contains feedback(ratings and natural language explanations) for QA pairs.

### Languages

English

## Dataset Creation
For each question-answer pair, we collected multiple feedback, each of which consists of a rating, selected
from excellent, good, could be improved, bad, and a natural language explanation 
elaborating on the strengths and/or weaknesses of the answer.

#### Initial Data Collection and Normalization
We scraped Covid-19-related content from official websites.


### Annotations


#### Who are the annotators?

Crowd-workers


### Licensing Information

Apache 2.0

### Contributions

[McGill-NLP](https://github.com/McGill-NLP)
