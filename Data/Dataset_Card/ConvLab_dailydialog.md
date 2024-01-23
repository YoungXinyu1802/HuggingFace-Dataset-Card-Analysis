---
language:
- en
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
pretty_name: DailyDialog
size_categories:
- 10K<n<100K
task_categories:
- conversational
---

# Dataset Card for DailyDialog

- **Repository:** http://yanran.li/dailydialog
- **Paper:** https://arxiv.org/pdf/1710.03957.pdf
- **Leaderboard:** None
- **Who transforms the dataset:** Qi Zhu(zhuq96 at gmail dot com)

To use this dataset, you need to install [ConvLab-3](https://github.com/ConvLab/ConvLab-3) platform first. Then you can load the dataset via:
```
from convlab.util import load_dataset, load_ontology, load_database

dataset = load_dataset('dailydialog')
ontology = load_ontology('dailydialog')
database = load_database('dailydialog')
```
For more usage please refer to [here](https://github.com/ConvLab/ConvLab-3/tree/master/data/unified_datasets).

### Dataset Summary

DailyDialog is a high-quality multi-turn dialog dataset. It is intriguing in several aspects. The language is human-written and less noisy. The dialogues in the dataset reflect our daily communication way and cover various topics about our daily life. We also manually label the developed dataset with communication intention and emotion information.

- **How to get the transformed data from original data:** 
  - Download [ijcnlp_dailydialog.zip](http://yanran.li/files/ijcnlp_dailydialog.zip).
  - Run `python preprocess.py` in the current directory.
- **Main changes of the transformation:**
  - Use `topic` annotation as `domain`. If duplicated dialogs are annotated with different topics, use the most frequent one.
  - Use `intent` annotation as `binary` dialogue act.
  - Retain emotion annotation in the `emotion` field of each turn.
  - Use nltk to remove space before punctuation: `utt = ' '.join([detokenizer.detokenize(word_tokenize(s)) for s in sent_tokenize(utt)])`.
  - Replace `" ’ "` with `"'"`: `utt = utt.replace(' ’ ', "'")`.
  - Add space after full-stop
- **Annotations:**
  - intent, emotion

### Supported Tasks and Leaderboards

NLU, NLG

### Languages

English

### Data Splits

| split      |   dialogues |   utterances |   avg_utt |   avg_tokens |   avg_domains | cat slot match(state)   | cat slot match(goal)   | cat slot match(dialogue act)   | non-cat slot span(dialogue act)   |
|------------|-------------|--------------|-----------|--------------|---------------|-------------------------|------------------------|--------------------------------|-----------------------------------|
| train      |       11118 |        87170 |      7.84 |        11.22 |             1 | -                       | -                      | -                              | -                                 |
| validation |        1000 |         8069 |      8.07 |        11.16 |             1 | -                       | -                      | -                              | -                                 |
| test       |        1000 |         7740 |      7.74 |        11.36 |             1 | -                       | -                      | -                              | -                                 |
| all        |       13118 |       102979 |      7.85 |        11.22 |             1 | -                       | -                      | -                              | -                                 |

10 domains: ['Ordinary Life', 'School Life', 'Culture & Education', 'Attitude & Emotion', 'Relationship', 'Tourism', 'Health', 'Work', 'Politics', 'Finance']
- **cat slot match**: how many values of categorical slots are in the possible values of ontology in percentage.
- **non-cat slot span**: how many values of non-categorical slots have span annotation in percentage.


### Citation

```
@InProceedings{li2017dailydialog,
    author = {Li, Yanran and Su, Hui and Shen, Xiaoyu and Li, Wenjie and Cao, Ziqiang and Niu, Shuzi},
    title = {DailyDialog: A Manually Labelled Multi-turn Dialogue Dataset},
    booktitle = {Proceedings of The 8th International Joint Conference on Natural Language Processing (IJCNLP 2017)},
    year = {2017}
}
```

### Licensing Information

[**CC BY-NC-SA 4.0**](https://creativecommons.org/licenses/by-nc-sa/4.0/)