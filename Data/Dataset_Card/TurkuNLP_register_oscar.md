# Dataset Card for register_oscar

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
 
### Dataset Summary

The Register Oscar dataset is a multilingual dataset, containing languaegs from the Oscar dataset that have been tagged with register information. 

8 main-level registers:
* Narrative (NA)
* Informational Description (IN)
* Opinion (OP)
* Interactive Discussion (ID)
* How-to/Instruction (HI)
* Informational Persuasion (IP)
* Lyrical (LY)
* Spoken (SP)

For further description of the labels, see (Douglas Biber and Jesse Egbert. 2018. Register variation online)

Code used to tag Register Oscar can be found at https://github.com/TurkuNLP/register-labeling

### Languages

Currently contains the following languages: Arabic, Bengali, Catalan, English, Spanish, Basque, French, Hindi, Indonesian, Portuguese, Swahili, Urdu, Vietnamese and Chinese.

For further information on the languages and data, see https://huggingface.co/datasets/oscar

## Dataset Structure

### Data Instances

```
{"id": "0", "labels": ["NA"], "text": "Zarif: Iran inajua mpango wa Saudia wa kufanya mauaji ya kigaidi dhidi ya maafisa wa ngazi za juu wa Iran\n"}
```

### Data Fields

* id: unique id of the document (from the Oscar dataset)
* labels: the list of labels assigned to the text
* text: the original text of the document (as appears in the Oscar dataset)