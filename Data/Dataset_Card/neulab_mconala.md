---
license: cc-by-sa-4.0
task_categories:
- text-generation
- translation
language:
- es
- ja
- ru
tags:
- code generation
pretty_name: mconala
size_categories:
- n<1K
---
# Dataset Card for MCoNaLa

## Dataset Description

- **Homepage:** https://github.com/zorazrw/multilingual-conala
- **Repository:** https://github.com/zorazrw/multilingual-conala
- **Paper:** https://arxiv.org/pdf/2203.08388.pdf
- **Leaderboard:** https://explainaboard.inspiredco.ai/leaderboards?show_mine=false&sort_dir=desc&sort_field=created_at&dataset=mconala

### Dataset Summary

MCoNaLa is a Multilingual Code/Natural Language Challenge dataset with 896 NL-Code pairs in three languages: Spanish, Japanese, and Russian. 

### Languages

Spanish, Japanese, Russian; Python

## Dataset Structure

### How to Use

```bash
from datasets import load_dataset

# Spanish subset
load_dataset("neulab/mconala", "es")
DatasetDict({
    test: Dataset({
        features: ['question_id', 'intent', 'rewritten_intent', 'snippet'],
        num_rows: 341
    })
})

# Japanese subset
load_dataset("neulab/mconala", "ja")
DatasetDict({
    test: Dataset({
        features: ['question_id', 'intent', 'rewritten_intent', 'snippet'],
        num_rows: 210
    })
})

# Russian subset
load_dataset("neulab/mconala", "ru")
DatasetDict({
    test: Dataset({
        features: ['question_id', 'intent', 'rewritten_intent', 'snippet'],
        num_rows: 345
    })
})
```

### Data Fields

|Field|Type|Description|
|---|---|---|
|question_id|int|StackOverflow post id of the sample|
|intent|string|Title of the Stackoverflow post as the initial NL intent|
|rewritten_intent|string|nl intent rewritten by human annotators|
|snippet|string|Python code solution to the NL intent|


### Data Splits

The dataset contains  341, 210, and 345 samples in Spanish, Japanese, and Russian.


### Citation Information

```
@article{wang2022mconala,
  title={MCoNaLa: A Benchmark for Code Generation from Multiple Natural Languages},
  author={Zhiruo Wang, Grace Cuenca, Shuyan Zhou, Frank F. Xu, Graham Neubig},
  journal={arXiv preprint arXiv:2203.08388},
  year={2022}
}
```