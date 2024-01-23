---
license: cc-by-4.0
pretty_name: Harvesting QA paris from Wikipedia.
language: en
multilinguality: monolingual
size_categories: 1M<
source_datasets:
- extended|wikipedia
task_categories:
- question-answering
task_ids:
- extractive-qa
---

# Dataset Card for "lmqg/qa_harvesting_from_wikipedia"

## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://aclanthology.org/P18-1177/](https://aclanthology.org/P18-1177/)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is the QA dataset collected by [Harvesting Paragraph-level Question-Answer Pairs from Wikipedia](https://aclanthology.org/P18-1177) (Du & Cardie, ACL 2018).


### Supported Tasks and Leaderboards
* `question-answering`

### Languages
English (en)

## Dataset Structure

### Data Fields
The data fields are the same among all splits.

#### plain_text

- `id`: a `string` feature of id
- `title`: a `string` feature of title of the paragraph 
- `context`: a `string` feature of paragraph 
- `question`: a `string` feature of question
- `answers`: a `json` feature of answers

### Data Splits

|train    |validation|test    |
|--------:|---------:|-------:|
|1,204,925|    30,293|  24,473|

## Citation Information

```
@inproceedings{du-cardie-2018-harvesting,
    title = "Harvesting Paragraph-level Question-Answer Pairs from {W}ikipedia",
    author = "Du, Xinya  and
      Cardie, Claire",
    booktitle = "Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2018",
    address = "Melbourne, Australia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P18-1177",
    doi = "10.18653/v1/P18-1177",
    pages = "1907--1917",
    abstract = "We study the task of generating from Wikipedia articles question-answer pairs that cover content beyond a single sentence. We propose a neural network approach that incorporates coreference knowledge via a novel gating mechanism. As compared to models that only take into account sentence-level information (Heilman and Smith, 2010; Du et al., 2017; Zhou et al., 2017), we find that the linguistic knowledge introduced by the coreference representation aids question generation significantly, producing models that outperform the current state-of-the-art. We apply our system (composed of an answer span extraction system and the passage-level QG system) to the 10,000 top ranking Wikipedia articles and create a corpus of over one million question-answer pairs. We provide qualitative analysis for the this large-scale generated corpus from Wikipedia.",
}
```