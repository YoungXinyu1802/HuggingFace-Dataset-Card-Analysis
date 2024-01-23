
---
annotations_creators:
- crowdsourced
language:
- en
language_creators:
- found
- crowdsourced
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: condaqa
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- negation
- reading comprehension
task_categories:
- question-answering
task_ids: []
---

# Dataset Card for CondaQA: A Contrastive Reading Comprehension Dataset for Reasoning about Negation

## Dataset Description

- **Repository:** [https://github.com/AbhilashaRavichander/CondaQA](https://github.com/AbhilashaRavichander/CondaQA)
- **Paper:** [https://arxiv.org/abs/2211.00295](https://arxiv.org/abs/2211.00295) 
- **Point of Contact:** aravicha@andrew.cmu.edu

## Dataset Summary

Data from the EMNLP 2022 paper by Ravichander et al.: "CondaQA: A Contrastive Reading Comprehension Dataset for Reasoning about Negation". 

If you use this dataset, we would appreciate you citing our work:
    
```
@inproceedings{ravichander-et-al-2022-condaqa,
  title={CONDAQA: A Contrastive Reading Comprehension Dataset for Reasoning about Negation},
  author={‪Ravichander‬, Abhilasha and Gardner, Matt and Marasovi\'{c}, Ana},
  proceedings={EMNLP 2022},
  year={2022}
}
```
      
From the paper: "We introduce CondaQA to facilitate the future development of models that can process negation effectively. This is the first English reading comprehension dataset which requires reasoning about the implications of negated statements in paragraphs. We collect paragraphs with diverse negation cues, then have crowdworkers ask questions about the _implications_ of the negated statement in the passage.  We also have workers make three kinds of edits to the passage---paraphrasing the negated statement, changing the scope of the negation, and reversing the negation---resulting in clusters of question-answer pairs that are difficult for models to answer with spurious shortcuts. CondaQA features 14,182 question-answer pairs with over 200 unique negation cues." 

### Supported Tasks and Leaderboards 

The task is to answer a question given a Wikipedia passage that includes something being negated. There is no official leaderboard.

### Language 
English

## Dataset Structure

### Data Instances
Here's an example instance:

```
{"QuestionID": "q10", 
"original cue": "rarely", 
"PassageEditID": 0, 
"original passage": "Drug possession is the crime of having one or more illegal drugs in one's possession, either for personal use, distribution, sale or otherwise. Illegal drugs fall into different categories and sentences vary depending on the amount, type of drug, circumstances, and jurisdiction. In the U.S., the penalty for illegal drug possession and sale can vary from a small fine to a prison sentence. In some states, marijuana possession is considered to be a petty offense, with the penalty being comparable to that of a speeding violation. In some municipalities, possessing a small quantity of marijuana in one's own home is not punishable at all. Generally, however, drug possession is an arrestable offense, although first-time offenders rarely serve jail time. Federal law makes even possession of \"soft drugs\", such as cannabis, illegal, though some local governments have laws contradicting federal laws.", 
"SampleID": 5294, 
"label": "YES", 
"original sentence": "Generally, however, drug possession is an arrestable offense, although first-time offenders rarely serve jail time.", 
"sentence2": "If a drug addict is caught with marijuana, is there a chance he will be jailed?", 
"PassageID": 444, 
"sentence1": "Drug possession is the crime of having one or more illegal drugs in one's possession, either for personal use, distribution, sale or otherwise. Illegal drugs fall into different categories and sentences vary depending on the amount, type of drug, circumstances, and jurisdiction. In the U.S., the penalty for illegal drug possession and sale can vary from a small fine to a prison sentence. In some states, marijuana possession is considered to be a petty offense, with the penalty being comparable to that of a speeding violation. In some municipalities, possessing a small quantity of marijuana in one's own home is not punishable at all. Generally, however, drug possession is an arrestable offense, although first-time offenders rarely serve jail time. Federal law makes even possession of \"soft drugs\", such as cannabis, illegal, though some local governments have laws contradicting federal laws."
}

```

### Data Fields

* `QuestionID`: unique ID for this question (might be asked for multiple passages)
* `original cue`: Negation cue that was used to select this passage from Wikipedia
* `PassageEditID`: 0 = original passage, 1 = paraphrase-edit passage, 2 = scope-edit passage, 3 = affirmative-edit passage
* `original passage`: Original Wikipedia passage the passage is based on (note that the passage might either be the original Wikipedia passage itself, or an edit based on it)
* `SampleID`: unique ID for this passage-question pair
* `label`: answer 
* `original sentence`: Sentence that contains the negated statement
* `sentence2`: question
* `PassageID`: unique ID for the Wikipedia passage
* `sentence1`: passage 

### Data Splits

Data splits can be accessed as:
```
from datasets import load_dataset
train_set = load_dataset("condaqa", "train")
dev_set = load_dataset("condaqa", "dev")
test_set = load_dataset("condaqa", "test")
```

## Dataset Creation

Full details are in the paper.


### Curation Rationale

From the paper: "Our goal is to evaluate models on their ability to process the contextual implications of negation. We have the following desiderata for our question-answering dataset:
1. The dataset should include a wide variety of negation cues, not just negative particles. 
2. Questions should be targeted towards the _implications_ of a negated statement, rather than the factual content of what was or wasn't negated, to remove common sources of spurious cues in QA datasets (Kaushik and Lipton, 2018; Naik et al., 2018; McCoy et al., 2019).
3. Questions should come in closely-related, contrastive groups, to further reduce the possibility of models' reliance on spurious cues in the data (Gardner et al., 2020). This will result in sets of passages that are similar to each other in terms of the words that they contain, but that may admit different answers to questions.
4. Questions should probe the extent to which models are sensitive to how the negation is expressed. In order to do this, there should be contrasting passages that differ only in their negation cue or its scope."

### Source Data

From the paper: "To construct CondaQA, we first collected passages from a July 2021 version of English Wikipedia that contained negation cues, including single- and multi-word negation phrases, as well as affixal negation."

"We use negation cues from [Morante et al. (2011)](https://aclanthology.org/L12-1077/) and [van Son et al. (2016)](https://aclanthology.org/W16-5007/) as a starting point which we extend." 

#### Initial Data Collection and Normalization

We show ten passages to crowdworkers and allow them to choose a passage they would like to work on.

#### Who are the source language producers?

Original passages come from volunteers who contribute to Wikipedia. Passage edits, questions, and answers are produced by crowdworkers. 

### Annotations

#### Annotation process

From the paper: "In the first stage of the task, crowdworkers made three types of modifications to the original passage: (1) they paraphrased the negated statement, (2) they modified the scope of the negated statement (while retaining the negation cue), and (3) they undid the negation. In the second stage, we instruct crowdworkers to ask challenging questions about the implications of the negated statement. The crowdworkers then answered the questions they wrote previously for the original and edited passages."

Full details are in the paper. 

#### Who are the annotators?

From the paper: "Candidates took a qualification exam which consisted of 12 multiple-choice questions that evaluated comprehension of the instructions. We recruit crowdworkers who answer >70% of the questions correctly for the next stage of the dataset construction task." We use the CrowdAQ platform for the exam and Amazon Mechanical Turk for annotations. 

### Personal and Sensitive Information

We expect that such information has already been redacted from Wikipedia. 

## Considerations for Using the Data

### Social Impact of Dataset

A model that solves this dataset might be (mis-)represented as an evidence that the model understands the entirety of English language and consequently deployed where it will have immediate and/or downstream impact on stakeholders. 

### Discussion of Biases

We are not aware of societal biases that are exhibited in this dataset.  

### Other Known Limitations

From the paper: "Though CondaQA currently represents the largest NLU dataset that evaluates a model’s ability to process the implications of negation statements, it is possible to construct a larger dataset, with more examples spanning different answer types. Further CONDAQA is an English dataset, and it would be useful to extend our data collection procedures to build high-quality resources in other languages. Finally, while we attempt to extensively measure and control for artifacts in our dataset, it is possible that our dataset has hidden artifacts that we did not study."

## Additional Information

### Dataset Curators

From the paper: "In order to estimate human performance, and to construct a high-quality evaluation with fewer ambiguous examples, we have five verifiers provide answers for each question in the development and test sets." The first author has been manually checking the annotations throughout the entire data collection process that took ~7 months.

### Licensing Information

license: apache-2.0

### Citation Information

```
@inproceedings{ravichander-et-al-2022-condaqa,
  title={CONDAQA: A Contrastive Reading Comprehension Dataset for Reasoning about Negation},
  author={‪Ravichander‬, Abhilasha and Gardner, Matt and Marasovi\'{c}, Ana},
  proceedings={EMNLP 2022},
  year={2022}
}
```