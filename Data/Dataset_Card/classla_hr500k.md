---
language:
- hr
license:
- cc-by-sa-4.0
task_categories:
- other
task_ids:
- lemmatization
- named-entity-recognition
- part-of-speech
tags:
- structure-prediction
- normalization
- tokenization
---

The hr500k training corpus contains 506,457 Croatian tokens manually annotated on the levels of tokenisation, sentence segmentation, morphosyntactic tagging, lemmatisation, named entities and dependency syntax.

On the sentence level, the dataset contains 20159 training samples, 1963 validation samples and 2672 test samples 
across the respective data splits. Each sample represents a sentence and includes the following features:
sentence ID ('sent\_id'), sentence text ('text'), list of tokens ('tokens'), list of lemmas ('lemmas'), 
list of MULTEXT-East tags ('xpos\_tags), list of UPOS tags ('upos\_tags'), list of morphological features ('feats'), 
and list of IOB tags ('iob\_tags'). A subset of the data also contains universal dependencies ('ud') and consists of
7498 training samples, 649 validation samples, and 742 test samples.

Three dataset configurations are available, namely 'ner', 'upos', and 'ud', with the corresponding features
encoded as class labels. If the configuration is not specified, it defaults to 'ner'.

If you use this dataset in your research, please cite the following paper:

```
Bibtex	@InProceedings{LJUBEI16.340,
  author = {Nikola Ljubešić and Filip Klubička and Željko Agić and Ivo-Pavao Jazbec},
  title = {New Inflectional Lexicons and Training Corpora for Improved Morphosyntactic Annotation of Croatian and Serbian},
  booktitle = {Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC 2016)},
  year = {2016},
  month = {may},
  date = {23-28},
  location = {Portorož, Slovenia},
  editor = {Nicoletta Calzolari (Conference Chair) and Khalid Choukri and Thierry Declerck and Sara Goggi and Marko Grobelnik and Bente Maegaard and Joseph Mariani and Helene Mazo and Asuncion Moreno and Jan Odijk and Stelios Piperidis},
  publisher = {European Language Resources Association (ELRA)},
  address = {Paris, France},
  isbn = {978-2-9517408-9-1},
  language = {english}
 }
```