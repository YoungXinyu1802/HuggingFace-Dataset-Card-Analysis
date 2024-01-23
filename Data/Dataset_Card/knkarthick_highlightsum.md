---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- mit
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- summarization
task_ids: []
pretty_name: HighlightSum Corpus
---
# Dataset Card for HighlightSum Corpus [Single Dataset Comprising of AMI, SamSUM & DialogSUM for Brief Summarization of Text]
## Dataset Description
### Links
- **AMI:** https://huggingface.co/datasets/knkarthick/AMI
- **DialogSUM:** https://github.com/cylnlp/dialogsum
- **SamSUM:** https://huggingface.co/datasets/knkarthick/samsum
- **Point of Contact:** https://huggingface.co/knkarthick

### Dataset Summary
HighlightSUM is collection of large-scale dialogue summarization dataset from AMI, SamSUM & DialogSUM, consisting of 31,108 dialogues with corresponding manually labeled summaries.
### Languages
English

## Dataset Structure
### Data Instances
HighlightSum is a large-scale dialogue summarization dataset collection, consisting of 31,108 dialogues split into train, test and validation.

The first instance in the training set:
{'id': 'train_0', 
'summary': "Mr. Smith's getting a check-up, and Doctor Hawkins advises him to have one every year. Hawkins'll give some information about their classes and medications to help Mr. Smith quit smoking.", 
'dialogue': "#Person1#: Hi, Mr. Smith. I'm Doctor Hawkins. Why are you here today?\n#Person2#: I found it would be a good idea to get a check-up.\n#Person1#: Yes, well, you haven't had one for 5 years. You should have one every year.\n#Person2#: I know. I figure as long as there is nothing wrong, why go see the doctor?\n#Person1#: Well, the best way to avoid serious illnesses is to find out about them early. So try to come at least once a year for your own good.\n#Person2#: Ok.\n#Person1#: Let me see here. Your eyes and ears look fine. Take a deep breath, please. Do you smoke, Mr. Smith?\n#Person2#: Yes.\n#Person1#: Smoking is the leading cause of lung cancer and heart disease, you know. You really should quit.\n#Person2#: I've tried hundreds of times, but I just can't seem to kick the habit.\n#Person1#: Well, we have classes and some medications that might help. I'll give you more information before you leave.\n#Person2#: Ok, thanks doctor."}

### Data Fields
- dialogue: text of dialogue.
- summary: human written summary of the dialogue.
- id: unique file id of an example.

### Data Splits
- train: 27401
- val: 1360
- test: 2347

## Dataset Creation
### Curation Rationale
Collection of AMI, SamSUM & DialogSUM Datasets.
### Who are the source language producers?
linguists
### Who are the annotators?
language experts

## Licensing Information
non-commercial licence: MIT
## Citation Information
Refer the above links for Credits & Citations.