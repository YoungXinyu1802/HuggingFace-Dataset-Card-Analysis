---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- he
license:
- other
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- extended|other-reuters-corpus
task_categories:
- token-classification
task_ids:
- named-entity-recognition
train-eval-index:
- config: bmc
  task: token-classification
  task_id: entity_extraction
  splits:
    train_split: train
    eval_split: validation
    test_split: test
  col_mapping:
    tokens: tokens
    ner_tags: tags
  metrics:
    - type: seqeval
      name: seqeval
---


# Splits for the Ben-Mordecai and Elhadad Hebrew NER Corpus (BMC)

In order to evaluate performance in accordance with the original Ben-Mordecai and Elhadad (2005) work, we provide three 75%-25% random splits. 
* Only the 7 entity categories viable for evaluation were kept (DATE, LOC, MONEY, ORG, PER, PERCENT, TIME) --- all MISC entities were filtered out.
* Sequence label scheme was changed from IOB to BIOES
* The dev sets are 10% taken out of the 75%


## Citation

If you use use the BMC corpus, please cite the original paper as well as our paper which describes the splits:

* Ben-Mordecai and Elhadad (2005):
```console
@mastersthesis{naama,
  title={Hebrew Named Entity Recognition},
  author={Ben-Mordecai, Naama},
  advisor={Elhadad, Michael},
  year={2005},
  url="https://www.cs.bgu.ac.il/~elhadad/nlpproj/naama/",
  institution={Department of Computer Science, Ben-Gurion University},
  school={Department of Computer Science, Ben-Gurion University},
}
```

* Bareket and Tsarfaty (2020)
```console
@misc{bareket2020neural,
      title={Neural Modeling for Named Entities and Morphology (NEMO^2)}, 
      author={Dan Bareket and Reut Tsarfaty},
      year={2020},
      eprint={2007.15620},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

