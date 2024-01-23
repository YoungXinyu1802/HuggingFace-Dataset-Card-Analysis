---
language: 
  - ar
  - bn
  - en
  - fi
  - id
  - fi
  - ja
  - ko
  - ru
  - sw
  - te
  - th

    
multilinguality:
- multilingual    

task_categories:
- text-retrieval

license: apache-2.0
---

# Dataset Summary
Mr. TyDi is a multi-lingual benchmark dataset built on TyDi, covering eleven typologically diverse languages. It is designed for monolingual retrieval, specifically to evaluate ranking with learned dense representations.

This dataset stores the queries, judgements, and example training data of Mr. TyDi. To access the corpus, please refer to [castorini/mr-tydi-corpus](https://huggingface.co/datasets/castorini/mr-tydi-corpus).

# Dataset Structure
The only configuration here is the `language`, 
For each language, there are three splits: `train`, `dev`, and `test`.
The negative examples from training set are sampled from the top-30 BM25 runfiles on each language.
Specifically, we combine the **training** data for all languages under the `combined` configuration.

An example of `train` set looks as follows:
```
{
  'query_id': '1', 
  'query': 'When was quantum field theory developed?', 
  'positive_passages': [
    {
      'docid': '25267#12', 
      'title': 'Quantum field theory', 
      'text': 'Quantum field theory naturally began with the study of electromagnetic interactions, as the electromagnetic field was the only known classical field as of the 1920s.'
    },
    ...
    ]
  'negative_passages': [
    {
      'docid': '346489#8', 
      'title': 'Local quantum field theory', 
      'text': 'More recently, the approach has been further implemented to include an algebraic version of quantum field ...'
    },
    ...
  ],
}
```

An example of `dev` and `test` set looks as follows. We only provide the docid of positive passages here to save the space. 
Also no candidate passages are provided at this point. 
Note that to perform the retrieval, it need to be used together with [castorini/mr-tydi-corpus](https://huggingface.co/datasets/castorini/mr-tydi-corpus)
```
{
  'query_id': '0', 
  'query': 'Is Creole a pidgin of French?', 
  'positive_passages': [
    {
      'docid': '3716905#1',
      'title': '', 
      'text': ''
    },
    ...
   ]
}
```

# Load Dataset

An example to load the dataset:
```
language = 'english'

# to load all train, dev and test sets
dataset = load_dataset('castorini/mr-tydi', language)

# or to load a specific set:
set_name = 'train'
dataset = load_dataset('castorini/mr-tydi', language, set_name)
```
Note that the 'combined' option has only the 'train' set.


# Citation Information
```
@article{mrtydi,
      title={{Mr. TyDi}: A Multi-lingual Benchmark for Dense Retrieval}, 
      author={Xinyu Zhang and Xueguang Ma and Peng Shi and Jimmy Lin},
      year={2021},
      journal={arXiv:2108.08787},
}
```

