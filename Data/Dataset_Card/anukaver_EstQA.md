---
language: et
---

# Estonian Question Answering dataset

* Dataset for extractive question answering in Estonian. It is based on Wikipedia articles, pre-filtered via PageRank. Annotation was done by one person.
* Train set includes 776 context-question-answer triplets. There are several possible answers per question, each in a separate triplet. Number of different questions is 512.
* Test set includes 603 samples. Each sample contains one or more golden answers. Altogether there are 892 golden ansewrs.

### Change log
Test set v1.1 adds some more golden answers.

### Reference
If you use this dataset for research, please cite the following paper:

```
@mastersthesis{mastersthesis,
  author       = {Anu Käver}, 
  title        = {Extractive Question Answering for Estonian Language},
  school       = {Tallinn University of Technology (TalTech)},
  year         = 2021
}
```