---
annotations_creators:
- expert-generated
extended:
- original
language_creators:
- found
language:
- en
- bg
- zh
- hr
- da
- nl
- et
- fa
- ja
- ko
- it
- fr
- de
license:
- cc-by-nc-4.0
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- semantic-similarity-classification
---

# XL-WiC
Huggingface dataset for the XL-WiC paper [https://www.aclweb.org/anthology/2020.emnlp-main.584.pdf](https://www.aclweb.org/anthology/2020.emnlp-main.584.pdf).
Please refer to the official [website](https://pilehvar.github.io/xlwic/) for more information.


## Configurations
When loading one of the XL-WSD datasets one has to specify the training language and the target language (on which dev and test will be performed). 
Please refer to [Languages](#languages) section to see in which languages training data is available.
For example, we can load the dataset having English as training language and Italian as target language as follows:
```python
from datasets import load_dataset
dataset = load_dataset('pasinit/xlwic', 'en_it')
```

## Languages
**Training data**
- en (English)
- fr (French)
- de (German)
- it (Italian)

**Dev & Test data**
- fr (French)
- de (German)
- it (Italian)
- bg (Bulgarian)
- zh (Chinese)
- hr (Croatian)
- da (Danish)
- nl (Dutch)
- et (Estonian)
- fa (Farsi)
- ja (Japanesse)
- ko (Korean)
