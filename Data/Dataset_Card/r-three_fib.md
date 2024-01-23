
# Dataset Card for FIB

## Dataset Summary

The FIB benchmark consists of 3579 examples for evaluating the factual inconsistency of large language models. Each example consists of a document and a pair of summaries: a factually consistent one and a factually inconsistent one. It is based on documents and summaries from XSum and CNN/DM.
Since this dataset is intended to evaluate the factual inconsistency of large language models, there is only a test split.  

Accuracies should be reported separately for examples from XSum and for examples from CNN/DM. This is because the behavior of models on XSum and CNN/DM are expected to be very different. The factually inconsistent summaries are model-extracted from the document for CNN/DM but are model-generated for XSum. 

### Citation Information

```
@article{tam2022fib,
  title={Evaluating the Factual Consistency of Large Language Models Through Summarization},
  author={Tam, Derek and Mascarenhas, Anisha and Zhang, Shiyue and Kwan, Sarah and Bansal, Mohit and Raffel, Colin},
  journal={arXiv preprint arXiv:2211.08412},
  year={2022}
}
```
### Licensing Information

license: cc-by-4.0