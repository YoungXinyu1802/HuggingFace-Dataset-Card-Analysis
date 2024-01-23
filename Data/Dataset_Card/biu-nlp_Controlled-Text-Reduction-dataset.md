# Controlled Text Reduction

This dataset contains Controlled Text Reduction triplets - document-summary pairs, and the spans in the document that cover the summary.
The task input is consists of a document with pre-selected spans in it ("highlights"). The output is a text covering all and only the highlighted content.

The script downloads the data from the original [GitHub repository](https://github.com/lovodkin93/Controlled_Text_Reduction). 

### Format

The dataset contains the following important features:
 
* `doc_text` - the input text. 
* `summary_text` - the output text. 
* `highlight_spans` - the spans in the input text (the doc_text) that lead to the output text (the summary_text). 

```json
{'doc_text': 'The motion picture industry\'s most coveted award...with 32.',
  'summary_text': 'The Oscar, created 60 years ago by MGM...awarded person (32).',
  'highlight_spans':'[[0, 48], [50, 55], [57, 81], [184, 247], ..., [953, 975], [1033, 1081]]'}
```
where for each document-summary pair, we save the spans in the input document that lead to the summary. 

Notice that the dataset consists of two subsets:
1. `DUC-2001-2002` - which is further divided into 3 splits (train, validation and test).
2. `CNN-DM` - which has a single split.

Citation
========
If you find the Controlled Text Reduction dataset useful in your research, please cite the following paper:
```
@misc{https://doi.org/10.48550/arxiv.2210.13449,
  doi = {10.48550/ARXIV.2210.13449},
  url = {https://arxiv.org/abs/2210.13449},
  author = {Slobodkin, Aviv and Roit, Paul and Hirsch, Eran and Ernst, Ori and Dagan, Ido},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Controlled Text Reduction},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Zero v1.0 Universal}
}

```