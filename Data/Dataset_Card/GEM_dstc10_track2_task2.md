---
annotations_creators:
- none
language_creators:
- unknown
language:
- en
license:
- apache-2.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- conversational
task_ids: []
pretty_name: dstc10_track2_task2
tags:
- dialog-response-generation
---

# Dataset Card for GEM/dstc10_track2_task2

## Dataset Description

- **Homepage:** https://github.com/alexa/alexa-with-dstc10-track2-dataset
- **Repository:** https://github.com/alexa/alexa-with-dstc10-track2-dataset
- **Paper:** https://assets.amazon.science/54/a1/5282d47044179737b4289622c824/how-robust-are-you-evaluating-task-oriented-dialogue-systems-on-spoken-conversations.pdf
- **Leaderboard:** https://eval.ai/challenge/1663/overview
- **Point of Contact:** Seokhwan Kim

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/dstc10_track2_task2).

### Dataset Summary 

The DSTC10 Track2 Task 2 follows the DSTC9 Track1 task, where participants have to implement knowledge-grounded dialog systems.
The training dataset is inherited from the DSTC9 challenge and is in the written domain, while the test set is newly collected and consists of noisy ASR transcripts.
Hence, the dataset facilitates building models for grounded dialog response generation.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/dstc10_track2_task2')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/dstc10_track2_task2).

#### website
https://github.com/alexa/alexa-with-dstc10-track2-dataset

#### paper
https://assets.amazon.science/54/a1/5282d47044179737b4289622c824/how-robust-are-you-evaluating-task-oriented-dialogue-systems-on-spoken-conversations.pdf

#### authors
Seokhwan Kim, Yang Liu, Di Jin, Alexandros Papangelis, Karthik Gopalakrishnan, Behnam Hedayatnia, Dilek Hakkani-Tur (Amazon Alexa AI)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
https://github.com/alexa/alexa-with-dstc10-track2-dataset

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
https://github.com/alexa/alexa-with-dstc10-track2-dataset

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
https://assets.amazon.science/54/a1/5282d47044179737b4289622c824/how-robust-are-you-evaluating-task-oriented-dialogue-systems-on-spoken-conversations.pdf

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
@inproceedings{kim2021robust,
  title={" How Robust ru?": Evaluating Task-Oriented Dialogue Systems on Spoken Conversations},
  author={Kim, Seokhwan and Liu, Yang and Jin, Di and Papangelis, Alexandros and Gopalakrishnan, Karthik and Hedayatnia, Behnam and Hakkani-Tur, Dilek},
  journal={IEEE Automatic Speech Recognition and Understanding Workshop},
  year={2021}
}

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Seokhwan Kim

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
seokhwk@amazon.com

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
yes

#### Leaderboard Link

<!-- info: Provide a link to the leaderboard. -->
<!-- scope: periscope -->
https://eval.ai/challenge/1663/overview

#### Leaderboard Details

<!-- info: Briefly describe how the leaderboard evaluates models. -->
<!-- scope: microscope -->
It evaluates the models based on the automatic metrics defined in the task paper for the three tasks of detection, selection and generation.


### Languages and Intended Use

#### Multilingual?

<!-- quick -->
<!-- info: Is the dataset multilingual? -->
<!-- scope: telescope -->
no

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`En`

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
apache-2.0: Apache License 2.0

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
To conduct research on dialogue state tracking and knowledge-grounded response generation.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Dialog Response Generation

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
This dataset aims to explore the robustness of conversational models when trained on spoken data. It has two aspects, multi-domain dialogue state tracking and conversation modeling with access to unstructured knowledge.


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`industry`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Amazon

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Seokhwan Kim, Yang Liu, Di Jin, Alexandros Papangelis, Karthik Gopalakrishnan, Behnam Hedayatnia, Dilek Hakkani-Tur (Amazon Alexa AI)

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
Amazon

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Alexandros Papangelis (Amazon Alexa AI), Di Jin (Amazon Alexa AI), Nico Daheim (RWTH Aachen University)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
       features = datasets.Features(
            {
                "id": datasets.Value("string"),
                "gem_id": datasets.Value("string"),
                "turns": [
                    {
                        "speaker": datasets.Value("string"),
                        "text": datasets.Value("string"),
                        "nbest": [
                            {
                                "hyp": datasets.Value("string"),
                                "score": datasets.Value("float"),
                            }
                        ],
                    }
                ],
                "knowledge": {
                    "domain": datasets.Value("string"),
                    "entity_name": datasets.Value("string"),
                    "title": datasets.Value("string"),
                    "body": datasets.Value("string"),
                },
                "response": datasets.Value("string"),
                "source": datasets.Value("string"),
                "linearized_input": datasets.Value("string"),
                "target": datasets.Value("string"),
                "references": [datasets.Value("string")],
            }
        )

nbest contains an nbest list of outputs generated by an ASR system along with their scores.

knowledge defines the annotated grounding as well as its metadata

#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
It was kept compatible with MultiWox 2.X data.

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
{'id': '0',
 'gem_id': 'GEM-dstc10_track2_task2-test-0',
 'turns': [{'speaker': 'U',
   'text': "hi uh i'm looking for restaurant in lower ha",
   'nbest': [{'hyp': "hi uh i'm looking for restaurant in lower ha",
     'score': -25.625450134277344},
    {'hyp': "hi uh i'm looking for restaurant in lower hai",
     'score': -25.969446182250977},
    {'hyp': "hi uh i'm looking for restaurant in lower haig",
     'score': -32.816890716552734},
    {'hyp': "hi uh i'm looking for restaurant in lower haigh",
     'score': -32.84316635131836},
    {'hyp': "hi uh i'm looking for restaurant in lower hag",
     'score': -32.8637580871582},
    {'hyp': "hi uh i'm looking for restaurant in lower hah",
     'score': -33.1048698425293},
    {'hyp': "hi uh i'm looking for restaurant in lower hait",
     'score': -33.96509552001953},
    {'hyp': "hi um i'm looking for restaurant in lower hai",
     'score': -33.97885513305664},
    {'hyp': "hi um i'm looking for restaurant in lower haig",
     'score': -34.56083679199219},
    {'hyp': "hi um i'm looking for restaurant in lower haigh",
     'score': -34.58711242675781}]},
  {'speaker': 'S',
   'text': 'yeah definitely i can go ahead and help you with that ummm what kind of option in a restaurant are you looking for',
   'nbest': []},
  {'speaker': 'U',
   'text': 'yeah umm am looking for an expensive restaurant',
   'nbest': [{'hyp': 'yeah umm am looking for an expensive restaurant',
     'score': -21.272899627685547},
    {'hyp': 'yeah umm m looking for an expensive restaurant',
     'score': -21.444047927856445},
    {'hyp': 'yeah umm a m looking for an expensive restaurant',
     'score': -21.565458297729492},
    {'hyp': 'yeah ummm am looking for an expensive restaurant',
     'score': -21.68832778930664},
    {'hyp': 'yeah ummm m looking for an expensive restaurant',
     'score': -21.85947608947754},
    {'hyp': 'yeah ummm a m looking for an expensive restaurant',
     'score': -21.980886459350586},
    {'hyp': "yeah umm a'm looking for an expensive restaurant",
     'score': -22.613924026489258},
    {'hyp': "yeah ummm a'm looking for an expensive restaurant",
     'score': -23.02935218811035},
    {'hyp': 'yeah um am looking for an expensive restaurant',
     'score': -23.11180305480957},
    {'hyp': 'yeah um m looking for an expensive restaurant',
     'score': -23.28295135498047}]},
  {'speaker': 'S',
   'text': "lemme go ahead and see what i can find for you ok great so i do ummm actually no i'm sorry is there something else i can help you find i don't see anything expensive",
   'nbest': []},
  {'speaker': 'U',
   'text': "sure ummm maybe if you don't have anything expensive how about something in the moderate price range",
   'nbest': [{'hyp': "sure ummm maybe if you don't have anything expensive how about something in the moderate price range",
     'score': -27.492507934570312},
    {'hyp': "sure umm maybe if you don't have anything expensive how about something in the moderate price range",
     'score': -27.75853729248047},
    {'hyp': "sure ummm maybe if you don't have anything expensive how about something in the moderate price rang",
     'score': -29.44410514831543},
    {'hyp': "sure umm maybe if you don't have anything expensive how about something in the moderate price rang",
     'score': -29.710134506225586},
    {'hyp': "sure um maybe if you don't have anything expensive how about something in the moderate price range",
     'score': -31.136560440063477},
    {'hyp': "sure um maybe if you don't have anything expensive how about something in the moderate price rang",
     'score': -33.088157653808594},
    {'hyp': "sure ummm maybe i you don't have anything expensive how about something in the moderate price range",
     'score': -36.127620697021484},
    {'hyp': "sure umm maybe i you don't have anything expensive how about something in the moderate price range",
     'score': -36.39365005493164},
    {'hyp': "sure ummm maybe if yo don't have anything expensive how about something in the moderate price range",
     'score': -36.43605041503906},
    {'hyp': "sure umm maybe if yo don't have anything expensive how about something in the moderate price range",
     'score': -36.70207977294922}]},
  {'speaker': 'S',
   'text': 'ok moderate lemme go ahead and check to see what i can find for moderate ok great i do have several options coming up how does the view lounge sound',
   'nbest': []},
  {'speaker': 'U',
   'text': 'that sounds good ummm do they have any sort of happy hour special',
   'nbest': [{'hyp': 'that sounds good ummm do they have any sort of happy hour special',
     'score': -30.316478729248047},
    {'hyp': 'that sounds good umm do they have any sort of happy hour special',
     'score': -30.958009719848633},
    {'hyp': 'that sounds good um do they have any sort of happy hour special',
     'score': -34.463165283203125},
    {'hyp': 'that sounds good ummm do they have any sirt of happy hour special',
     'score': -34.48350143432617},
    {'hyp': 'that sounds good umm do they have any sirt of happy hour special',
     'score': -35.12503433227539},
    {'hyp': 'that sounds good ummm do they have any sord of happy hour special',
     'score': -35.61939239501953},
    {'hyp': 'that sounds good umm do they have any sord of happy hour special',
     'score': -36.26092529296875},
    {'hyp': 'that sounds good ummm do they have any sont of happy hour special',
     'score': -37.697105407714844},
    {'hyp': 'that sounds good umm do they have any sont of happy hour special',
     'score': -38.33863830566406},
    {'hyp': 'that sounds good um do they have any sirt of happy hour special',
     'score': -38.630191802978516}]}],
 'knowledge': {'domain': 'restaurant',
  'entity_name': 'The View Lounge',
  'title': 'Does The View Lounge offer happy hour?',
  'body': 'The View Lounge offers happy hour.'},
 'response': 'uhhh great question lemme go ahead and check that out for you ok fantastic so it looks like they do offer happy hour',
 'source': 'sf_spoken',
 'linearized_input': "<U> hi uh i'm looking for restaurant in lower ha <S> yeah definitely i can go ahead and help you with that ummm what kind of option in a restaurant are you looking for <U> yeah umm am looking for an expensive restaurant <S> lemme go ahead and see what i can find for you ok great so i do ummm actually no i'm sorry is there something else i can help you find i don't see anything expensive <U> sure ummm maybe if you don't have anything expensive how about something in the moderate price range <S> ok moderate lemme go ahead and check to see what i can find for moderate ok great i do have several options coming up how does the view lounge sound <U> that sounds good ummm do they have any sort of happy hour special || knowledge domain: restaurant, entity: The View Lounge, title: Does The View Lounge offer happy hour?, information: The View Lounge offers happy hour.",
 'target': 'uhhh great question lemme go ahead and check that out for you ok fantastic so it looks like they do offer happy hour',
 'references': ['uhhh great question lemme go ahead and check that out for you ok fantastic so it looks like they do offer happy hour']}

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
train: training set, val: validation set, test: test set

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The track dataset originally only consists of a validation and test set in the spoken domain with noisy ASR transcripts.
The training set is taken from the predecessor task DSTC9 Track 1 and contains written conversations.



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
This dataset can be used to evaluate conversational models on spoken inputs (using ASR hypotheses). In particular, we can evaluate the models’ ability to understand language by tracking the dialogue state, and their ability to generate knowledge-grounded responses.

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
yes

#### Unique Language Coverage

<!-- info: Does this dataset cover other languages than other datasets for the same task? -->
<!-- scope: periscope -->
no

#### Difference from other GEM datasets

<!-- info: What else sets this dataset apart from other similar datasets in GEM? -->
<!-- scope: microscope -->
This dataset contains transcribed spoken interactions.

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
We can measure the model’s ability to understand language and to generate knowledge-grounded responses.


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
no

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
no


### Getting Started with the Task




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
This dataset can be used to evaluate conversational models on spoken inputs (using ASR hypotheses). In particular, we can evaluate the models’ ability to generate knowledge-grounded responses.

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`Other: Other Metrics`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
BLEU-1, BLEU-2, BLEU-3, BLEU-4, METEOR, ROGUE-1, ROGUE-2, ROGUE-L

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
no



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
We want to explore how conversational models perform on spoken data. 

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
This dataset aims to explore the robustness of conversational models when evaluated on spoken data. It has two aspects, multi-domain dialogue state tracking and conversation modeling with access to unstructured knowledge.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
no


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Other`

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
The conversations revolve around 5 domains (or topics): hotels, restaurants, attractions, taxi, train.

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
not validated

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
not filtered


### Structured Annotations

#### Additional Annotations?

<!-- quick -->
<!-- info: Does the dataset have additional annotations for each instance? -->
<!-- scope: telescope -->
none

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
no


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
yes


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
no PII

#### Justification for no PII

<!-- info: Provide a justification for selecting `no PII` above. -->
<!-- scope: periscope -->
The subjects were instructed to conduct fictional conversations about booking restaurants or requesting fictional information.


### Maintenance

#### Any Maintenance Plan?

<!-- info: Does the original dataset have a maintenance plan? -->
<!-- scope: telescope -->
no



## Broader Social Context

### Previous Work on the Social Impact of the Dataset

#### Usage of Models based on the Data

<!-- info: Are you aware of cases where models trained on the task featured in this dataset ore related tasks have been used in automated systems? -->
<!-- scope: telescope -->
no


### Impact on Under-Served Communities

#### Addresses needs of underserved Communities?

<!-- info: Does this dataset address the needs of communities that are traditionally underserved in language technology, and particularly language generation technology? Communities may be underserved for exemple because their language, language variety, or social or geographical context is underepresented in NLP and NLG resources (datasets and models). -->
<!-- scope: telescope -->
no


### Discussion of Biases

#### Any Documented Social Biases?

<!-- info: Are there documented social biases in the dataset? Biases in this context are variations in the ways members of different social categories are represented that can have harmful downstream consequences for members of the more disadvantaged group. -->
<!-- scope: telescope -->
unsure



## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
There should be no risk related to PII as the subjects conduct fictional conversations.


### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`open license - commercial use allowed`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`open license - commercial use allowed`


### Known Technical Limitations



