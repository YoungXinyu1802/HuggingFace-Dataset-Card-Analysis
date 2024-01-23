---
annotations_creators: []
language:
- en
language_creators: []
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: MetaQA Agents' Predictions
size_categories: []
source_datasets:
- mrqa
- duorc
- qamr
- boolq
- commonsense_qa
- hellaswag
- social_i_qa
- narrativeqa
tags:
- multi-agent question answering
- multi-agent QA
- predictions
task_categories:
- question-answering
task_ids: []
paperswithcode_id: metaqa-combining-expert-agents-for-multi
---
# Dataset Card for MetaQA Agents' Predictions

## Dataset Description
- **Repository:** [MetaQA's Repository](https://github.com/UKPLab/MetaQA)
- **Paper:** [MetaQA: Combining Expert Agents for Multi-Skill Question Answering](https://arxiv.org/abs/2112.01922)
- **Point of Contact:** [Haritz Puerto](mailto:puerto@ukp.informatik.tu-darmstadt.de)

## Dataset Summary
This dataset contains the answer predictions of the QA agents for the [QA datasets](https://huggingface.co/datasets/haritzpuerto/MetaQA_Datasets) used in [MetaQA paper](https://arxiv.org/abs/2112.01922). In particular, it contains the following QA agents' predictions:
### Span-Extraction Agents
- Agent: Span-BERT Large (Joshi et al.,2020) trained on SQuAD. Predictions for:
  - SQuAD
  - NewsQA
  - HotpotQA
  - SearchQA
  - Natural Questions
  - TriviaQA-web
  - QAMR
  - DuoRC
  - DROP
- Agent: Span-BERT Large (Joshi et al.,2020) trained on NewsQA. Predictions for:
  - SQuAD
  - NewsQA
  - HotpotQA
  - SearchQA
  - Natural Questions
  - TriviaQA-web
  - QAMR
  - DuoRC
  - DROP
- Agent: Span-BERT Large (Joshi et al.,2020) trained on HotpotQA. Predictions for:
  - SQuAD
  - NewsQA
  - HotpotQA
  - SearchQA
  - Natural Questions
  - TriviaQA-web
  - QAMR
  - DuoRC
  - DROP
- Agent: Span-BERT Large (Joshi et al.,2020) trained on SearchQA. Predictions for:
  - SQuAD
  - NewsQA
  - HotpotQA
  - SearchQA
  - Natural Questions
  - TriviaQA-web
  - QAMR
  - DuoRC
  - DROP
- Agent: Span-BERT Large (Joshi et al.,2020) trained on Natural Questions. Predictions for:
  - SQuAD
  - NewsQA
  - HotpotQA
  - SearchQA
  - Natural Questions
  - TriviaQA-web
  - QAMR
  - DuoRC
  - DROP
- Agent: Span-BERT Large (Joshi et al.,2020) trained on TriviaQA-web. Predictions for:
  - SQuAD
  - NewsQA
  - HotpotQA
  - SearchQA
  - Natural Questions
  - TriviaQA-web
  - QAMR
  - DuoRC
  - DROP
- Agent: Span-BERT Large (Joshi et al.,2020) trained on QAMR. Predictions for:
  - SQuAD
  - NewsQA
  - HotpotQA
  - SearchQA
  - Natural Questions
  - TriviaQA-web
  - QAMR
  - DuoRC
  - DROP
- Agent: Span-BERT Large (Joshi et al.,2020) trained on DuoRC. Predictions for:
  - SQuAD
  - NewsQA
  - HotpotQA
  - SearchQA
  - Natural Questions
  - TriviaQA-web
  - QAMR
  - DuoRC
  - DROP
- Agent: Span-BERT Large (Joshi et al.,2020) trained on DROP. Predictions for:
  - SQuAD
  - NewsQA
  - HotpotQA
  - SearchQA
  - Natural Questions
  - TriviaQA-web
  - QAMR
  - DuoRC
  - DROP

### Multiple-Choice Agents
- Agent: RoBERTa Large (Liu et al., 2019) trained on RACE. Predictions for:
  - RACE
  - Commonsense QA
  - BoolQ
  - HellaSWAG
  - Social IQA

- Agent: RoBERTa Large (Liu et al., 2019) trained on HellaSWAG. Predictions for:
  - RACE
  - Commonsense QA
  - BoolQ
  - HellaSWAG
  - Social IQA

- Agent: AlBERT xxlarge-v2 (Lan et al., 2020) trained on Commonsense QA. Predictions for:
  - RACE
  - Commonsense QA
  - BoolQ
  - HellaSWAG
  - Social IQA

- Agent: BERT Large-wwm (Devlin et al., 2019) trained on BoolQ. Predictions for:
  - BoolQ

### Abstractive Agents
- Agent: TASE (Segal et al., 2020) trained on DROP. Predictions for:
  - DROP

- Agent: BART Large with Adapters (Pfeiffer et al., 2020) trained on NarrativeQA. Predictions for:
  - NarrativeQA

### Multimodal Agents
- Agent: Hybrider (Chen et al., 2020) trained on HybridQA. Predictions for:
  - HybridQA

### Languages
All the QA datasets used English and thus, the Agents's predictions are also in English.
## Dataset Structure
Each agent has a folder. Inside, there is a folder for each dataset containing four files:
- predict_nbest_predictions.json
- predict_predictions.json / predictions.json
- predict_results.json (for span-extraction agents)

### Structure of predict_nbest_predictions.json 
```
{id: [{"start_logit": ...,
       "end_logit": ...,
       "text": ...,
       "probability": ... }]}
```
### Structure of predict_predictions.json 
```
{id: answer_text}
```
### Data Splits
All the QA datasets have 3 splits: train, validation, and test. The splits (Question-Context pairs) are provided in https://huggingface.co/datasets/haritzpuerto/MetaQA_Datasets



## Considerations for Using the Data
### Social Impact of Dataset
The purpose of this dataset is to help developing new multi-agent models and analyzing the predictions of QA models.
### Discussion of Biases
The QA models used to create this predictions may not be perfect, generate false data, and contain biases. The release of these predictions may help to identify these flaws in the models.

## Additional Information

### License
The MetaQA Agents' prediction dataset version is released under the [Apache-2.0 License](http://www.apache.org/licenses/LICENSE-2.0). 
### Citation
```
@article{Puerto2021MetaQACE,
  title={MetaQA: Combining Expert Agents for Multi-Skill Question Answering},
  author={Haritz Puerto and Gozde Gul cSahin and Iryna Gurevych},
  journal={ArXiv},
  year={2021},
  volume={abs/2112.01922}
}
```