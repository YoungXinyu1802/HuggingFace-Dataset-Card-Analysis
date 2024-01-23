---
annotations_creators:
- expert-generated
language_creators:
- crowdsourced
language:
- en
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: 'movie_recommendation'
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- multiple-choice
- question-answering
task_ids:
- multiple-choice-qa
- open-domain-qa
tags:
- movie-recommendation
- collaborative-filtering
- movielens
- film
---


# Dataset for evaluation of (zero-shot) recommendation with language models

This is the BIG-Bench version of our language-based movie recommendation dataset.

<https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/movie_recommendation>

GPT-2 has a 48.8% accuracy, chance is 25%.
Human accuracy is 60.4%.

# Citation
```
@InProceedings{sileodreclm22,
    author="Sileo, Damien
    and Vossen, Wout
    and Raymaekers, Robbe",
    editor="Hagen, Matthias
    and Verberne, Suzan
    and Macdonald, Craig
    and Seifert, Christin
    and Balog, Krisztian
    and N{\o}rv{\aa}g, Kjetil
    and Setty, Vinay",
    title="Zero-Shot Recommendation as Language Modeling",
    booktitle="Advances in Information Retrieval",
    year="2022",
    publisher="Springer International Publishing",
    address="Cham",
    pages="223--230",
    isbn="978-3-030-99739-7"
}
```