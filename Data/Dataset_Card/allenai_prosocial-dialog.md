---
annotations_creators:
- crowdsourced
language:
- en
language_creators:
- crowdsourced
- machine-generated
license: cc-by-4.0
multilinguality:
- monolingual
pretty_name: ProsocialDialog
size_categories:
- 10K<n<100K
- 100K<n<1M
source_datasets:
- original
- extended|social_bias_frames
tags:
- dialogue
- dialogue safety
- social norm
- rules-of-thumb
task_categories:
- conversational
- text-classification
task_ids:
- dialogue-generation
- multi-class-classification
---

# Dataset Card for ProsocialDialog Dataset

## Dataset Description
- **Repository:** [Dataset and Model](https://github.com/skywalker023/prosocial-dialog)
- **Paper:** [ProsocialDialog: A Prosocial Backbone for Conversational Agents](https://aclanthology.org/2022.emnlp-main.267/)
- **Point of Contact:** [Hyunwoo Kim](mailto:hyunwook@allenai.org)

## Dataset Summary
ProsocialDialog is the first large-scale multi-turn English dialogue dataset to teach conversational agents to respond to problematic content following social norms. Covering diverse unethical, problematic, biased, and toxic situations, ProsocialDialog contains responses that encourage prosocial behavior, grounded in commonsense social rules (i.e., rules-of-thumb, RoTs). Created via a human-AI collaborative framework, ProsocialDialog consists of 58K dialogues, with 331K utterances, 160K unique RoTs, and 497K dialogue safety labels accompanied by free-form rationales.


## Supported Tasks
* Dialogue response generation
* Dialogue safety prediction
* Rules-of-thumb generation

## Languages
English

## Dataset Structure

### Data Attributes
attribute | type | description
--- | ---  | ---
`context` | str | the potentially unsafe utterance
`response` | str | the guiding utterance grounded on rules-of-thumb (`rots`)
`rots` | list of str\|null | the relevant rules-of-thumb for `text` *not* labeled as \_\_casual\_\_
`safety_label` | str | the final verdict of the context according to `safety_annotations`: {\_\_casual\_\_, \_\_possibly\_needs\_caution\_\_, \_\_probably\_needs\_caution\_\_, \_\_needs\_caution\_\_, \_\_needs\_intervention\_\_}
`safety_annotations` | list of str | raw annotations from three workers: {casual, needs caution, needs intervention}
`safety_annotation_reasons` | list of str | the reasons behind the safety annotations in free-form text from each worker
`source` | str | the source of the seed text that was used to craft the first utterance of the dialogue: {socialchemistry, sbic, ethics_amt, ethics_reddit}
`etc` | str\|null | other information
`dialogue_id` | int | the dialogue index
`response_id` | int | the response index
`episode_done` | bool | an indicator of whether it is the end of the dialogue


## Dataset Creation

To create ProsocialDialog, we set up a human-AI collaborative data creation framework, where GPT-3 generates the potentially unsafe utterances, and crowdworkers provide prosocial responses to them. This approach allows us to circumvent two substantial challenges: (1) there are no available large-scale corpora of multiturn prosocial conversations between humans, and (2) asking humans to write unethical, toxic, or problematic utterances could result in psychological harms (Roberts, 2017; Steiger et al., 2021).

### Further Details, Social Impacts, and Limitations
Please refer to our [paper](https://arxiv.org/abs/2205.12688).


## Additional Information

### Citation

Please cite our work if you found the resources in this repository useful:
```
@inproceedings{kim2022prosocialdialog,
    title={ProsocialDialog: A Prosocial Backbone for Conversational Agents},
    author={Hyunwoo Kim and Youngjae Yu and Liwei Jiang and Ximing Lu and Daniel Khashabi and Gunhee Kim and Yejin Choi and Maarten Sap},
    booktitle={EMNLP},
    year=2022
}
```