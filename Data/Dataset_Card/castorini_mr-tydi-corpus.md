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

This dataset stores documents of Mr. TyDi. To access the queries and judgments, please refer to [castorini/mr-tydi](https://huggingface.co/datasets/castorini/mr-tydi).

# Dataset Structure
The only configuration here is the `language`. As all three folds (train, dev and test) share the same corpus, there is only one fold 'train' under each language, unlike [castorini/mr-tydi](https://huggingface.co/datasets/castorini/mr-tydi).

An example of document data entry looks as follows:
```
{
  'docid': '25#0', 
  'title': 'Autism', 
  'text': 'Autism is a developmental disorder characterized by difficulties with social interaction and communication, ...'
}
```

# Load Dataset
An example to load the dataset:
```
language = 'english'
dataset = load_dataset('castorini/mr-tydi-corpus', language, 'train')
```

# Citation Information
```
@article{mrtydi,
      title={{Mr. TyDi}: A Multi-lingual Benchmark for Dense Retrieval}, 
      author={Xinyu Zhang and Xueguang Ma and Peng Shi and Jimmy Lin},
      year={2021},
      journal={arXiv:2108.08787},
}
```