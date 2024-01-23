---
license: gpl-3.0
---
## Dataset Description

- **Homepage:** https://www.darrow.ai/
- **Repository:** https://github.com/darrow-labs/ClassActionPrediction
- **Paper:** https://arxiv.org/abs/2211.00582
- **Leaderboard:** N/A
- **Point of Contact:** [Gila Hayat](mailto:gila@darrow.ai)

### Dataset Summary

USClassActions is an English dataset of 200 complaints from the US Federal Court with the respective binarized judgment outcome (Win/Lose). The dataset poses a challenging text classification task. We are happy to share this dataset in order to promote robustness and fairness studies on the critical area of legal NLP. The data was annotated using  Darrow.ai proprietary tool.


### Data Instances
```python
from datasets import load_dataset
dataset = load_dataset('darrow-ai/USClassActionOutcomes_ExpertsAnnotations')
```
### Data Fields
`id`: (**int**) a unique identifier of the document \
`origin_label `: (**str**) the outcome of the case \
`target_text`: (**str**) the facts of the case \
`annotator_prediction `: (**str**) annotators predictions of the case outcome based on the target_text \
`annotator_confidence `: (**str**) the annotator's level of confidence in his outcome prediction \

### Curation Rationale

The dataset was curated by Darrow.ai (2022).

### Citation Information

*Gil Semo, Dor Bernsohn, Ben Hagag, Gila Hayat, and Joel Niklaus*
*ClassActionPrediction: A Challenging Benchmark for Legal Judgment Prediction of Class Action Cases in the US*
*Proceedings of the 2022 Natural Legal Language Processing Workshop. Abu Dhabi. 2022*
```
@InProceedings{darrow-niklaus-2022-uscp,
  author = {Semo, Gil
                and Bernsohn, Dor
                and Hagag, Ben
                and Hayat, Gila
                and Niklaus, Joel},
  title = {ClassActionPrediction: A Challenging Benchmark for Legal Judgment Prediction of Class Action Cases in the US},
  booktitle = {Proceedings of the 2022 Natural Legal Language Processing Workshop},
  year = {2022},
  location = {Abu Dhabi},
}
```
