# Amazon Multilingual Counterfactual Dataset 

The dataset contains sentences from Amazon customer reviews (sampled from Amazon product review dataset) annotated for counterfactual detection (CFD) binary classification. Counterfactual statements describe events that did not or cannot take place. Counterfactual statements may be identified as statements of the form – If p was true, then q would be true (i.e. assertions whose antecedent (p) and consequent (q) are known or assumed to be false).

The key features of this dataset are:

* The dataset is multilingual and contains sentences in English, German, and Japanese.
* The labeling was done by professional linguists and high quality was ensured.
* The dataset is supplemented with the annotation guidelines and definitions, which were worked out by professional linguists. We also provide the clue word lists, which are typical for counterfactual sentences and were used for initial data filtering. The clue word lists were also compiled by professional linguists.

Please see the [paper](https://arxiv.org/abs/2104.06893) for the data statistics, detailed description of data collection and annotation.


GitHub repo URL: https://github.com/amazon-research/amazon-multilingual-counterfactual-dataset

## Usage

You can load each of the languages as follows:

```
from datasets import get_dataset_config_names

dataset_id = "SetFit/amazon_counterfactual"
# Returns ['de', 'en', 'en-ext', 'ja']
configs = get_dataset_config_names(dataset_id)
# Load English subset
dset = load_dataset(dataset_id, name="en")
```