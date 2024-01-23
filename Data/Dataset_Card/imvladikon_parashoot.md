---
task_categories:
- question-answering
language:
- he
---

# ParaShoot

[ParaShoot](https://github.com/omrikeren/ParaShoot): A Hebrew question and answering dataset in the style of [SQuAD](https://arxiv.org/abs/1606.05250), based on articles scraped from Wikipedia. The dataset contains a few thousand crowdsource-annotated pairs of questions and answers, in a setting suitable for few-shot learning.

For more details and quality analysis, see the [paper](https://arxiv.org/abs/2109.11314).

## Dataset Statistics

| **#Items** | **#Articles** | **#Paragraphs** |         |
| ---------- | ------------- | --------------- | ------- |
| Train      | 1792          | 295             | 565     |
| Dev        | 221           | 33              | 63      |
| Test       | 1025          | 165             | 319     |
| **Total**  | **3038**      | **493**         | **947** |


## Citing
If you use ParaShoot in your research, please cite the ParaShoot paper:
```bibtex
@inproceedings{keren2021parashoot,
  title={ParaShoot: A Hebrew Question Answering Dataset},
  author={Keren, Omri and Levy, Omer},
  booktitle={Proceedings of the 3rd Workshop on Machine Reading for Question Answering},
  pages={106--112},
  year={2021}
}
```