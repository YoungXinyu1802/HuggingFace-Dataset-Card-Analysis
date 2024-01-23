---
language:
- sl
license:
- cc-by-sa-4.0
task_categories:
- token-classification
task_ids:
- lemmatization
- named-entity-recognition
- parsing
- part-of-speech
tags:
- structure-prediction
- tokenization
- dependency-parsing
---
The dataset contains 7432 training samples, 1164 validation samples and 893 test samples. 
Each sample represents a sentence and includes the following features: sentence ID ('sent\_id'), 
list of tokens ('tokens'), list of lemmas ('lemmas'), 
list of Multext-East tags ('xpos\_tags), list of UPOS tags ('upos\_tags'), list of morphological features ('feats'), 
list of IOB tags ('iob\_tags'), and list of universal dependency tags ('uds'). Three dataset configurations are
available, where the corresponding features are encoded as class labels: 'ner', 'upos', and 'ud'.