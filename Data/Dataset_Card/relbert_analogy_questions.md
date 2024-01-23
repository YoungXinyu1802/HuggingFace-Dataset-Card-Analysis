---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- n<1K
pretty_name: Analogy Question
---

# Dataset Card for "relbert/analogy_questions"
## Dataset Description
- **Repository:** [RelBERT](https://github.com/asahi417/relbert)
- **Paper:** [https://aclanthology.org/2021.acl-long.280/](https://aclanthology.org/2021.acl-long.280/)
- **Dataset:** Analogy Questions

### Dataset Summary
This dataset contains 5 different word analogy questions used in [Analogy Language Model](https://aclanthology.org/2021.acl-long.280/).

- original analogy questions

| name      | Size (valid/test) | Num of choice | Num of relation group | Original Reference                                                         |
|-----------|------------------:|--------------:|----------------------:|:--------------------------------------------------------------------------:|
| `sat_full`| -/374             | 5             | 2                     | [Turney (2005)](https://arxiv.org/pdf/cs/0508053.pdf)                      |
| `sat`     | 37/337            | 5             | 2                     | [Turney (2005)](https://arxiv.org/pdf/cs/0508053.pdf)                      |
| `u2`      | 24/228            | 5,4,3         | 9                     | [EnglishForEveryone](https://englishforeveryone.org/Topics/Analogies.html) |
| `u4`      | 48/432            | 5,4,3         | 5                     | [EnglishForEveryone](https://englishforeveryone.org/Topics/Analogies.html) |
| `google`  | 50/500            | 4             | 2                     | [Mikolov et al., (2013)](https://www.aclweb.org/anthology/N13-1090.pdf)    |
| `bats`    | 199/1799          | 4             | 3                     | [Gladkova et al., (2016)](https://www.aclweb.org/anthology/N18-2017.pdf)   |

- extra analogy questions

| name                                | Size (valid/test)   | Num of choice (valid/test)   | Num of relation group (valid/test)   | Original Reference                                                                                                     |
|:------------------------------------|:--------------------|:-----------------------------|:-------------------------------------|:-----------------------------------------------------------------------------------------------------------------------|
| `semeval2012_relational_similarity` | 79/-                | 3/-                          | 79/-                                 | [relbert/semeval2012_relational_similarity](https://huggingface.co/datasets/relbert/semeval2012_relational_similarity) |
| `t_rex_relational_similarity`       | 496/183             | 74/48                        | 60/19                                | [relbert/t_rex_relational_similarity](https://huggingface.co/datasets/relbert/t_rex_relational_similarity)             |
| `conceptnet_relational_similarity`  | 1112/1192           | 19/17                        | 18/16                                | [relbert/conceptnet_relational_similarity](https://huggingface.co/datasets/relbert/conceptnet_relational_similarity)   |
| `nell_relational_similarity`        | 400/600             | 5/7                          | 4/6                                  | [relbert/nell_relational_similarity](https://huggingface.co/datasets/relbert/nell_relational_similarity)               |
| `scan` | 178/1616            | 3,36,136,10,45,78,15,21,55,120,153,91,28/3,36,136,10,45,78,15,21,55,120,153,91,28 | 2/2                                  | [relbert/scientific_and_creative_analogy](https://huggingface.co/datasets/relbert/scientific_and_creative_analogy) |


## Dataset Structure
### Data Instances
An example of `test` looks as follows.
```
{
    "stem": ["raphael", "painter"],
    "answer": 2,
    "choice": [["andersen", "plato"],
                ["reading", "berkshire"],
                ["marx", "philosopher"],
                ["tolstoi", "edison"]]
}
```
The `stem` is the query word pair, `choice` has word pair candidates,
and `answer` indicates the index of correct candidate which starts from `0`.
All data is lowercased except Google dataset.

### Citation Information
```
@inproceedings{ushio-etal-2021-bert-is,
    title ={{BERT} is to {NLP} what {A}lex{N}et is to {CV}: {C}an {P}re-{T}rained {L}anguage {M}odels {I}dentify {A}nalogies?},
    author={Ushio, Asahi and
            Espinosa-Anke, Luis and
            Schockaert, Steven and
            Camacho-Collados, Jose},
    booktitle={Proceedings of the {ACL}-{IJCNLP} 2021 Main Conference},
    year={2021},
    publisher={Association for Computational Linguistics}
}
```

### LICENSE
The LICENSE of all the resources are under [CC-BY-NC-4.0](./LICENSE). Thus, they are freely available for academic purpose or individual research, but restricted for commercial use.
