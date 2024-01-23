---
annotations_creators:
- crowd-sourced
language_creators:
- unknown
language:
- en
license:
- cc-by-sa-4.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- conversational
task_ids: []
pretty_name: schema_guided_dialog
tags:
- dialog-response-generation
---

# Dataset Card for GEM/schema_guided_dialog

## Dataset Description

- **Homepage:** n/a
- **Repository:** [Github[(https://github.com/google-research-datasets/dstc8-schema-guided-dialogue)
- **Paper:** https://arxiv.org/abs/1909.05855
- **Leaderboard:** N/A
- **Point of Contact:** Abhinav Rastogi

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/schema_guided_dialog).

### Dataset Summary 

The GEM version of this dataset functions as a response generation dataset. The input specifies dialog acts that a model needs to verbalize. The Schema-Guided Dialog dataset is challenging since it comprises multiple domains from hotel and travel to restaurants, and a wide range of dialog acts. The context of each conversation is provided as well. 

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/schema_guided_dialog')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/schema_guided_dialog).

#### website
n/a

#### paper
[Arxiv](https://arxiv.org/abs/1909.05855)

#### authors
Abhinav Rastogi, Xiaoxue Zang, Srinivas Sunkara, Raghav Gupta, Pranav Khaitan, Amir Fayazi, Maria Wang, and Guan-Lin Chao

## Dataset Overview

### Where to find the Data and its Documentation

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github[(https://github.com/google-research-datasets/dstc8-schema-guided-dialogue)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[Arxiv](https://arxiv.org/abs/1909.05855)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
{
@inproceedings{rastogi2020towards,
  title={Towards scalable multi-domain conversational agents: The schema-guided dialogue dataset},
  author={Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={34},
  number={05},
  pages={8689--8696},
  year={2020}
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Abhinav Rastogi

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
schema-guided-dst@google.com

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
no


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
`English`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
The language structure is machine-generated, and the language realizations are produced by crowd workers.
The dataset paper does not provide demographic information for the crowd workers.


#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-sa-4.0: Creative Commons Attribution Share Alike 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
The Schema-Guided Dialogue (SGD) dataset contains 18K multi-domain task-oriented dialogues between a human and a virtual assistant, which covers 17 domains ranging from banks and events to media, calendar, travel, and weather.
The language presents in the datset is only English.
The SGD dataset provides a challenging testbed for a number of tasks in task-oriented dialogue, including language understanding, slot filling, dialogue state tracking and response generation.
For the creation of the SGD dataset, they developed a multi-domain dialogue simulator that generates dialogue outlines over an arbitrary combination of APIs, dialogue states and system actions. Then, they used a crowd-sourcing procedure to paraphrase these outlines to natural language utterances.
This novel crowd-sourcing procedure preserves all annotations obtained from the simulator and does not require any extra annotations after dialogue collection.


#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Dialog Response Generation

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
The goal of a speaker who generates the target utterance is to help users accomplish tasks including but not limited to finding flights, booking restaurants, searching for nearby events and movies.



### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`industry`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Google

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Abhinav Rastogi, Xiaoxue Zang, Srinivas Sunkara, Raghav Gupta, Pranav Khaitan, Amir Fayazi, Maria Wang, and Guan-Lin Chao

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
Google

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Wanyu Du wrote the initial data card and Yacine Jernite the data loader. Simon Mille updated the data card with the additional splits. Sebastian Gehrmann migrated the data card and loader to the v2 version and extended the missing information.


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
Each dialog instance has the following fields:

* `dialogue_id`: A unique identifier for a dialogue.
* `services`: A list of services present in the dialogue.
* `turns`: A list of annotated system or user utterances. Each turn consists of the following fields:
	* `speaker`: The speaker for the turn, either `USER` or `SYSTEM`.
	* `utterance`: A string containing the natural language utterance.
	* `frames`: A list of frames, each frame containing annotations for a single service and consists of the following fields:
		* `service`: The name of the service corresponding to the frame. The slots and intents used in the following fields are taken from the schema of this service.
		* `slots`: A list of slot spans in the utterance, only provided for non-categorical slots. Each slot span contains the following fields:
			* `slot`: The name of the slot.
			* `start`: The index of the starting character in the utterance corresponding to the slot value.
			* `exclusive_end`: The index of the character just after the last character corresponding to the slot value in the utterance.
		* `actions`: A list of actions corresponding to the system. Each action has the following fields:
			* `act`: The type of action.
			* `slot`: (optional) A slot argument for some of the actions.
			* `values`: (optional) A list of values assigned to the slot. If the values list is non-empty, then the slot must be present.
			* `canonical_values`: (optional) The values in their canonicalized form as used by the service. It is a list of strings of the same length as values.
		* `service_call`: (system turns only, optional) The request sent to the service. It consists of the following fields:
			* `method`: The name of the intent or function of the service or API being executed.
			* `parameters`: A pair of lists of the same lengths: `parameter_slot_name` contains slot names and `parameter_canonical_value` contains the corresponding values in their canonicalized form.
		* `service_results`: (system turns only, optional) A list of entities containing the results obtained from the service. It is only available for turns in which a service call is made. Each entity is represented as a pair of lists of the same length: `service_slot_name` contains slot names and `service_canonical_value` contains the corresponding canonical values.
		* `state`: (user turns only) The dialogue state corresponding to the service. It consists of the following fields:
			* `active_intent`: The intent corresponding to the service of the frame which is currently being fulfilled by the system. It takes the value "NONE" if none of the intents are active.
			* `requested_slots`: A list of slots requested by the user in the current turn.
			* `slot_values`: A pair of lists of the same lengths: `slot_name` contains slot names and `slot_value_list` contains the corresponding lists of strings. For categorical slots, this list contains a single value assigned to the slot. For non-categorical slots, all the values in this list are spoken variations of each other and are equivalent (e.g, "6 pm", "six in the evening", "evening at 6" etc.).



#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{'dialogue_id': '1_00000',
 'services': ['Restaurants_1'],
 'turns':
 {'frames':
 	[{'actions': [{'act': [6],
      'canonical_values': [['FindRestaurants']],
      'slot': ['intent'],
      'values': [['FindRestaurants']]}],
      'service': ['Restaurants_1'],
      'service_call': [{'method': '',
      'parameters': {'parameter_canonical_value': [],
       'parameter_slot_name': []}}],
      'service_results': [{'service_results_list': []}],
      'slots': [{'exclusive_end': [], 'slot': [], 'start': []}],
      'state': [{'active_intent': 'FindRestaurants',
      			 'requested_slots': [],
      			 'slot_values': {'slot_name': [], 'slot_value_list': []}}]},
     {'actions': [{'act': [13],
      'canonical_values': [[]],
      'slot': ['city'],
      'values': [[]]}],
      'service': ['Restaurants_1'],
      'service_call': [{'method': '',
      'parameters': {'parameter_canonical_value': [],
       'parameter_slot_name': []}}],
      'service_results': [{'service_results_list': []}],
      'slots': [{'exclusive_end': [], 'slot': [], 'start': []}],
      'state': [{'active_intent': '',
      		   'requested_slots': [],
      		   'slot_values': {'slot_name': [], 'slot_value_list': []}}]},
    ...,]}
 'speaker': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
 'utterance': [
   'I am feeling hungry so I would like to find a place to eat.',
   'Do you have a specific which you want the eating place to be located at?',
   'I would like for it to be in San Jose.',
   'Is there a specific cuisine type you enjoy, such as Mexican, Italian or something else?',
   'I usually like eating the American type of food.',
   'I see that at 71 Saint Peter there is a good restaurant which is in San Jose.',
   'Can you give me the address of this restaurant.',
   'If you want to go to this restaurant you can find it at 71 North San Pedro Street.',
   'Can you give me the phone number that I can contact them with?',
   'If you want to phone them you can at 408-971-8523.',
   'Is there some other restaurant which you can suggest?',
   'How would you like Bazille restaurant which is situated in San Jose.',
   'Do you have another restaurant matching my needs? For example a restaurant which is economical and is located in Palo Alto.',
   'I see that 7 restaurants suit to what you requested. Bird Dog seems as a good restaurant and is located in Palo Alto.',
   'Alright, that seems good. I would like to make a booking at this restaurant.',
   'For which time do you want the booking to be?',
   'I will be eating there at 11:30 am so make it for then.',
   'Can you please confirm that you want to book a table for 2 at 11:30 am at the Bird Dog restaurant in Palo Alto for today.',
   'That suits me well. Can you tell me if they feature live music?',
   'Your booking has been made without errors, but unfortunately they do not have live music.',
   'Will I be able to find liquor there? Can you give me the address of their location?',
   'The restaurant is located at 420 Ramona Street. Unfortunately they do not serve alcohol at the restaurant.',
   'I appreciate it very much. That would be all.',
   'Have a good time!'
 ]}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
The dataset is split into a train, validation, and test set with the following sizes:

| | Train | Validation | Test |
| --- | --- | --- | --- |
| \# of dialogues | 16142 | 2482 | 4201 |
| \# of turns | 48426 | 7446 | 12603 |

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The data is generally split i.i.d, but some topics only appear in training and some only for testing. For example, the domains Messaging, Payment, and Train are test-only. 



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
This dataset comprises a wide range of dialog capabilities and thus enables the evaluation of many more generation capabilities of comparable datasets. Its collection methodology ensures a high diversity but also high quality of the data. 

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
The domains a lot more diverse than other datasets. 

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
surface realization, compositionality.


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
yes

#### GEM Modifications

<!-- info: What changes have been made to he original dataset? -->
<!-- scope: periscope -->
`data points modified`

#### Modification Details

<!-- info: For each of these changes, described them in more details and provided the intended purpose of the modification -->
<!-- scope: microscope -->
We are focusing on the response-generation part of the dataset and thus reformatted the dataset to treat the service agent utterances as the targets to be generated and the previous customer utterance and the agent's dialog act as the input. We additionally reformat the dialog acts to directly conform to the format described in this [paper](https://arxiv.org/abs/2004.15006).


#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
yes

#### Split Information

<!-- info: Describe how the new splits were created -->
<!-- scope: periscope -->
9 challenge sets for Schema-Guided Dialog were added to the GEM evaluation suite.

1. We created subsets of the training and development sets of 500 randomly selected inputs each.
2. We applied 5 transformations to respectively 5 sets of 500 randomly selected inputs: (i) back-translation, (ii)-(iii) introduction of typographical errors, using Butterfingers with two thresholds (0.02 and 0.05), resulting in two sets with different amounts of typos introduced (there are more typos with the 0.05 threshold than with the 0.02 one), (iv) removal of final punctuations (when any), and (v) input scrambling, for which the order of the dialogue acts was randomly reassigned.
3. For the input size, we created subpopulations based on the number of dialogue acts in the input.

| DA number     | Frequency English |
|---------------|-------------------|
| 1             |              5049 |
| 2             |              2517 |
| 3             |              1328 |
| 4             |               469 |
| 5             |               335 |
| 6             |               256 |
| 7             |                46 |

We also split the test data according to the type of dialogue act, represented by cardinal numbers in the dataset.

| DA type      | Frequency English |
|--------------|-------------------|
| 2            |              1397 |
| 3            |               983 |
| 4            |              1027 |
| 5            |               958 |
| 9            |                72 |
| 10           |              1024 |
| 11           |              1246 |
| 12           |               500 |
| 13           |              2078 |
| 15           |               715 |


#### Split Motivation

<!-- info: What aspects of the model's generation capacities were the splits created to test? -->
<!-- scope: periscope -->
Generalization and Robustness.


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
* [Paper for dataset and DST baseline](https://arxiv.org/pdf/1909.05855.pdf)
* [DSTC8 overview paper](https://arxiv.org/pdf/2002.01359.pdf)
* [Code for DST baseline](https://github.com/google-research/google-research/tree/master/schema_guided_dst)
* [Natural language generation baseline paper](https://arxiv.org/pdf/2004.15006.pdf)
* [Blog post announcing the dataset](https://ai.googleblog.com/2019/10/introducing-schema-guided-dialogue.html)




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Surface realization and compositionally. 

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEURT`, `BLEU`, `ROUGE`

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
The original paper focused on the task of dialog state prediction instead of response generation and thus did not suggest any set of metrics. 

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
no



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
Previous multi-domain task-oriented dialogue datsets do not sufficiently capture the real-world challenges in virtual assistants, since they cover few domains and assume a single static ontology per domain.
The SGD datset is created to cover 17 domains with over 16K dialogues, and contain multiple different APIs in most domains, many of which have overlapping functionalities but different interfaces, which reflects common real-world scenarios.
The wide range of available annotations can be used for intent prediction, slot filling, dialogue state tracking, policy imitation learning, language generation, user simulation learning, among other tasks in large-scale virtual assistants.


#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
The goal of a speaker who generates the target utterance is to help users accomplish tasks including but not limited to finding flights, booking restaurants, searching for nearby events and movies.


#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
no


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Machine-generated`

#### Generation Method Link

<!-- info: If text was machine-generated for the dataset, provide a link to the generation method if available (N/A otherwise). -->
<!-- scope: periscope -->
[Github](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue)

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
The dialogue outlines are first generated by a simulator. The dialogue simulator interacts with the services to generate dialogue outlines. It consists of two agents playing the roles of the user and the system, interacting with each other using a finite set of actions specified through dialogue acts over a probabilistic automaton designed to capture varied dialogue trajectories. It is worth noting that the simulation automaton does not include any domain-specific constraints: all domain-specific constraints are encoded in the schema and scenario.

The dialogue paraphrasing framework then converts the outlines generated by the simulator into a natural conversation. Users may refer to the slot values in the dialogue acts in various different ways during the conversation, e.g., “los angeles” may be referred to as “LA” or “LAX”. To introduce these natural variations in the slot values, different slot values are replaced with a randomly selected variation while being kept consistent across user turns in a dialogue. The actions are then converted to pseudo-natural language utterances using a set of manually defined action-to-text templates, and the resulting utterances for the different actions in a turn are concatenated together.


#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
The dataset covers the following domains: Alarm, Banks, Buses, Calendar, Events, Flights, Homes, Hotels, Media, Messaging, Movies, Music, Payment, RentalCars, Restaurants, RideSharing, Services, Train, Travel, and Weather. The domain ‘Service’ includes salons, dentists, doctors etc. The ‘Alarm’, ‘Messaging’, ‘Payment’ and ‘Train’ domains are only present in the dev or test sets.
to test generalization to new domains.

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
crowd-sourced

#### Number of Raters

<!-- info: What is the number of raters -->
<!-- scope: telescope -->
unknown

#### Raters per Training Example

<!-- info: How many annotators saw each training example? -->
<!-- scope: periscope -->
0

#### Raters per Test Example

<!-- info: How many annotators saw each test example? -->
<!-- scope: periscope -->
0

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
unknown

#### Annotation Values

<!-- info: Purpose and values for each annotation -->
<!-- scope: microscope -->
The dialogue transformed by these steps is sent to the crowd workers to be reformulated into more natural language. One crowd worker is tasked with paraphrasing all utterances of a dialogue to ensure naturalness and coherence. The crowd workers are asked to exactly repeat the slot values in their paraphrases so that the span indices for the slots can be recovered via string matching.


#### Any Quality Control?

<!-- info: Quality control measures? -->
<!-- scope: telescope -->
none


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
no

#### Justification for Using the Data

<!-- info: If not, what is the justification for reusing the data? -->
<!-- scope: microscope -->
While no policy is reported, we assume that one was in place for the collection.


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
no PII

#### Justification for no PII

<!-- info: Provide a justification for selecting `no PII` above. -->
<!-- scope: periscope -->
The SGD dataset does not use identity categories and does not contain sensitive data.



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
no

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
Due to the combination of the automatic generation and crowd rater paraphasing, the language can be very formulaic. While this may be acceptable for the model part (i.e., we may actually desire an automated agent to form formulaic responses), the input utterances of the simulated customers likely do not cover the entire spectrum of the English language. 



## Considerations for Using the Data

### PII Risks and Liability



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

#### Technical Limitations

<!-- info: Describe any known technical limitations, such as spurrious correlations, train/test overlap, annotation biases, or mis-annotations, and cite the works that first identified these limitations when possible. -->
<!-- scope: microscope -->
The dialogues under each domain distributed unevenly, where the flights domain has 3644 dialogues while the payment domain only contains 222 dialogues.
Besides, all dialogues are paraphrased by crowd-workers, and it is possible that crow-workers with different culture backgrounds will exhibit biased opinions.


#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
Since the initial data was automatically generated, the coverage of entity names is necessarily biased. An agent thus needs to be evaluated in a more realistic environment. 


