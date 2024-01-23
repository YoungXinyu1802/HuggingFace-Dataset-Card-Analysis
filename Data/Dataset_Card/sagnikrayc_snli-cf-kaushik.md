---
annotations_creators:
  - crowdsourced
language_creators:
  - crowdsourced 
language:
  - en 
license:
  - cc-by-4.0 
multilinguality:
  - monolingual 
size_categories:
  - 1K<n<10K 
source_datasets:
  - extended|snli 
task_categories:
  - text-classification 
task_ids:
  - natural-language-inference
  - multi-input-text-classification 
pretty_name: Counterfactual Instances for Stanford Natural Language Inference 
dataset_info:
  features:
    - name: premise
      dtype: string
    - name: hypothesis
      dtype: string
    - name: label
      dtype: string
  splits:
    - name: train
      num_bytes: 1771712
      num_examples: 8300
    - name: validation
      num_bytes: 217479
      num_examples: 1000
    - name: test
      num_bytes: 437468
      num_examples: 2000
---
# Dataset Card for Counterfactually Augmented SNLI

## Table of Contents
- [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)

## Dataset Description

- **Repository:** [Learning the Difference that Makes a Difference with Counterfactually-Augmented Data](https://github.com/acmi-lab/counterfactually-augmented-data)
- **Paper:** [Learning the Difference that Makes a Difference with Counterfactually-Augmented Data](https://openreview.net/forum?id=Sklgs0NFvr)
- **Point of Contact:** [Sagnik Ray Choudhury](mailto:sagnikrayc@gmail.com)

### Dataset Summary

The SNLI corpus (version 1.0) is a collection of 570k human-written English sentence pairs manually labeled for balanced classification with the labels entailment, contradiction, and neutral, supporting the task of natural language inference (NLI), also known as recognizing textual entailment (RTE). In the ICLR 2020 paper [Learning the Difference that Makes a Difference with Counterfactually-Augmented Data](https://openreview.net/forum?id=Sklgs0NFvr), Kaushik et. al. provided a dataset with counterfactual perturbations on the SNLI and IMDB data. This repository contains the original and counterfactual perturbations for the SNLI data, which was generated after processing the original data from [here](https://github.com/acmi-lab/counterfactually-augmented-data).

### Languages

The language in the dataset is English as spoken by users of the website Flickr and as spoken by crowdworkers from Amazon Mechanical Turk. The BCP-47 code for English is en.

## Dataset Structure

### Data Instances

For each instance, there is: 
- a string for the premise, 
- a string for the hypothesis,
- a label: (entailment, contradiction, neutral) 
- a type: this tells whether the data point is the original SNLI data point or a counterfactual perturbation.
- an idx. The ids correspond to the original id in the SNLI data. For example, if the original SNLI instance was `4626192243.jpg#3r1e`, there wil be 5 data points as follows:

```json lines
{
  "idx": "4626192243.jpg#3r1e-orig",
  "premise": "A man with a beard is talking on the cellphone and standing next to someone who is lying down on the street.",
  "hypothesis": "A man is prone on the street while another man stands next to him.",
  "label": "entailment",
  "type": "original"
}
{
  "idx": "4626192243.jpg#3r1e-cf-0",
  "premise": "A man with a beard is talking on the cellphone and standing next to someone who is lying down on the street.",
  "hypothesis": "A man is talking to his wife on the cellphone.",
  "label": "neutral",
  "type": "cf"
}
{
  "idx": "4626192243.jpg#3r1e-cf-1",
  "premise": "A man with a beard is talking on the cellphone and standing next to someone who is on the street.",
  "hypothesis": "A man is prone on the street while another man stands next to him.",
  "label": "neutral",
  "type": "cf"
}
{
  "idx": "4626192243.jpg#3r1e-cf-2",
  "premise": "A man with a beard is talking on the cellphone and standing next to someone who is sitting on the street.",
  "hypothesis": "A man is prone on the street while another man stands next to him.",
  "label": "contradiction",
  "_type": "cf"
}
{
  "idx": "4626192243.jpg#3r1e-cf-3",
  "premise": "A man with a beard is talking on the cellphone and standing next to someone who is lying down on the street.",
  "hypothesis": "A man is alone on the street.",
  "label": "contradiction",
  "type": "cf"
}
```

### Data Splits

Following SNLI, this dataset also has 3 splits: _train_, _validation_, and _test_. The original paper says this:
```aidl 
RP and RH, each comprised of 3332 pairs in train, 400 in validation, and 800 in test, leading to a total of 6664 pairs in train, 800 in validation, and 1600 in test in the revised dataset.
```
This means for _train_, there are 1666 original SNLI instances, and each has 4 counterfactual perturbations (from premise and hypothesis edit), leading to a total of 1666*5 = 8330 _train_ data points in this dataset. Similarly, _validation_ and _test_ has 200 and 400 original SNLI instances respectively, consequently 1000 and 2000 instances in total. 

| Dataset Split | Number of Instances in Split |
|---------------|------------------------------|
| Train         | 8,330                        |
| Validation    | 1,000                        |
| Test          | 2,000                        |

