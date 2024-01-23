---
annotations_creators:
- none
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
- table-to-text
task_ids: []
pretty_name: viggo
tags:
- data-to-text
---

# Dataset Card for GEM/viggo

## Dataset Description

- **Homepage:** https://nlds.soe.ucsc.edu/viggo
- **Repository:** [Needs More Information]
- **Paper:** https://aclanthology.org/W19-8623/
- **Leaderboard:** N/A
- **Point of Contact:** Juraj Juraska

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/viggo).

### Dataset Summary 

ViGGO is an English data-to-text generation dataset in the video game domain, with target responses being more conversational than information-seeking, yet constrained to the information presented in a meaning representation. The dataset is relatively small with about 5,000 datasets but very clean, and can thus serve for evaluating transfer learning, low-resource, or few-shot capabilities of neural models.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/viggo')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/viggo).

#### website
[Wesbite](https://nlds.soe.ucsc.edu/viggo)

#### paper
[ACL Anthology](https://aclanthology.org/W19-8623/)

#### authors
Juraj Juraska, Kevin K. Bowden, Marilyn Walker

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Wesbite](https://nlds.soe.ucsc.edu/viggo)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://aclanthology.org/W19-8623/)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{juraska-etal-2019-viggo,
    title = "{V}i{GGO}: A Video Game Corpus for Data-To-Text Generation in Open-Domain Conversation",
    author = "Juraska, Juraj  and
      Bowden, Kevin  and
      Walker, Marilyn",
    booktitle = "Proceedings of the 12th International Conference on Natural Language Generation",
    month = oct # "{--}" # nov,
    year = "2019",
    address = "Tokyo, Japan",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W19-8623",
    doi = "10.18653/v1/W19-8623",
    pages = "164--172",
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Juraj Juraska

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
jjuraska@ucsc.edu

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

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-sa-4.0: Creative Commons Attribution Share Alike 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
ViGGO was designed for the task of data-to-text generation in chatbots (as opposed to task-oriented dialogue systems), with target responses being more conversational than information-seeking, yet constrained to the information presented in a meaning representation. The dataset, being relatively small and clean, can also serve for demonstrating transfer learning capabilities of neural models.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Data-to-Text


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
University of California, Santa Cruz

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Juraj Juraska, Kevin K. Bowden, Marilyn Walker

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Juraj Juraska


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
Each example in the dataset has the following two fields:

- `mr`: A meaning representation (MR) that, in a structured format, provides the information to convey, as well as the desired dialogue act (DA) type.
- `ref`: A reference output, i.e., a corresponding utterance realizing all the information in the MR.

Each MR is a flattened dictionary of attribute-and-value pairs, "wrapped" in the dialogue act type indication. This format was chosen primarily for its compactness, but also to allow for easy concatenation of multiple DAs (each with potentially different attributes) in a single MR.

Following is the list of all possible attributes (which are also refered to as "slots") in ViGGO along with their types/possible values:

- `name`: The name of a video game (e.g., Rise of the Tomb Raider).
- `release_year`: The year a video game was released in (e.g., 2015).
- `exp_release_date`: For a not-yet-released game, the date when it is expected to be released (e.g., February 22, 2019). *Note: This slot cannot appear together with `release_year` in the same dialogue act.*
- `developer`: The name of the studio/person that created the game (e.g., Crystal Dynamics).
- `genres`: A list of one or more genre labels from a set of possible values (e.g., action-adventure, shooter).
- `player_perspective`: A list of one or more perspectives from which the game is/can be played (possible values: first person, third person, side view, bird view).
- `platforms`: A list of one or more gaming platforms the game was officially released for (possible values: PC, PlayStation, Xbox, Nintendo, Nintendo Switch).
- `esrb`: A game's content rating as determined by the ESRB (possible values: E (for Everyone), E 10+ (for Everyone 10 and Older), T (for Teen), M (for Mature)).
- `rating`: Depending on the dialogue act this slot is used with, it is a categorical representation of either the game's average rating or the game's liking (possible values: excellent, good, average, poor).
- `has_multiplayer`: Indicates whether a game supports multiplayer or can only be played in single-player mode (possible values: yes, no).
- `available_on_steam`: Indicates whether a game can be purchased through the Steam digital distribution service (possible values: yes, no).
- `has_linux_release`: Indicates whether a game is supported on Linux operating systems (possible values: yes, no).
- `has_mac_release`: Indicates whether a game is supported on macOS (possible values: yes, no).
- `specifier`: A game specifier used by the `request` DA, typically an adjective (e.g., addictive, easiest, overrated, visually impressive).

Each MR in the dataset has 3 distinct reference utterances, which are represented as 3 separate examples with the same MR.

#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
The dataset structure mostly follows the format of the popular E2E dataset, however, with added dialogue act type indications, new list-type attributes introduced, and unified naming convention for multi-word attribute names.

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{
    "mr": "give_opinion(name[SpellForce 3], rating[poor], genres[real-time strategy, role-playing], player_perspective[bird view])",
    "ref": "I think that SpellForce 3 is one of the worst games I've ever played. Trying to combine the real-time strategy and role-playing genres just doesn't work, and the bird view perspective makes it near impossible to play."
}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
ViGGO is split into 3 partitions, with no MRs in common between the training set and either of the validation and the test set (and that *after* delexicalizing the `name` and `developer` slots). The ratio of examples in the partitions is approximately 7.5 : 1 : 1.5, with their exact sizes listed below:

- **Train:** 5,103 (1,675 unique MRs)
- **Validation:** 714 (238 unique MRs)
- **Test:** 1,083 (359 unique MRs)
- **TOTAL:** 6,900 (2,253 unique MRs)

*Note: The reason why the number of unique MRs is not exactly one third of all examples is that for each `request_attribute` DA (which only has one slot, and that without a value) 12 reference utterances were collected instead of 3.*

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
A similar MR length and slot distribution was preserved across the partitions. The distribution of DA types, on the other hand, is skewed slightly toward fewer `inform` DA instances (the most prevalent DA type) and a higher proportion of the less prevalent DAs in the validation and the test set.

#### 

<!-- info: What does an outlier of the dataset in terms of length/perplexity/embedding look like? -->
<!-- scope: microscope -->
```
{
    "mr": "request_attribute(player_perspective[])",
    "ref": "Is there a certain player perspective that you prefer over others in games you play?"
},
{
    "mr": "inform(name[FIFA 12], esrb[E (for Everyone)], genres[simulation, sport], player_perspective[bird view, side view], platforms[PlayStation, Xbox, Nintendo, PC], available_on_steam[no])",
    "ref": "Fifa 12 is a decent sports simulator. It's pretty cool how the game swaps from the bird's eye perspective down to a side view while you're playing. You can get the game for PlayStation, Xbox, Nintendo consoles, and PC, but unfortunately it's not on Steam. Of course, as a sports game there's not much objectionable content so it's rated E."
},
{
    "mr": "inform(name[Super Bomberman], release_year[1993], genres[action, strategy], has_multiplayer[no], platforms[Nintendo, PC], available_on_steam[no], has_linux_release[no], has_mac_release[no])",
    "ref": "Super Bomberman is one of my favorite Nintendo games, also available on PC, though not through Steam. It came out all the way back in 1993, and you can't get it for any modern consoles, unfortunately, so no online multiplayer, or of course Linux or Mac releases either. That said, it's still one of the most addicting action-strategy games out there."
}
```



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
ViGGO is a fairly small dataset but includes a greater variety of utterance types than most other datasets for NLG from structured meaning representations. This makes it more interesting from the perspective of model evaluation, since models have to learn to differentiate between various dialogue act types that share the same slots.

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
ViGGO's language is more casual and conversational -- as opposed to information-seeking -- which differentiates it from the majority of popular datasets for the same type of data-to-text task. Moreover, the video game domain is a rather uncommon one in the NLG community, despite being very well-suited for data-to-text generation, considering it offers entities with many attributes to talk about, which can be described in a structured format.


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

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
- [E2E NLG Challenge](http://www.macs.hw.ac.uk/InteractionLab/E2E/)

#### Technical Terms

<!-- info: Technical terms used in this card and the dataset and their definitions -->
<!-- scope: microscope -->
- MR = meaning representation
- DA = dialogue act



## Previous Results

### Previous Results

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`, `METEOR`, `ROUGE`, `BERT-Score`, `BLEURT`, `Other: Other Metrics`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
SER (slot error rate): Indicates the proportion of missing/incorrect/duplicate/hallucinated slot mentions in the utterances across a test set. The closer to zero a model scores in this metric, the more semantically accurate its outputs are. This metric is typically calculated either manually on a small sample of generated outputs, or heuristically using domain-specific regex rules and gazetteers.

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
- [Juraska et al., 2019. ViGGO: A Video Game Corpus for Data-To-Text Generation in Open-Domain Conversation.](https://aclanthology.org/W19-8623/)
- [Harkous et al., 2020. Have Your Text and Use It Too! End-to-End Neural Data-to-Text Generation with Semantic Fidelity.](https://aclanthology.org/2020.coling-main.218/)
- [Kedzie and McKeown, 2020. Controllable Meaning Representation to Text Generation: Linearization and Data Augmentation Strategies.](https://aclanthology.org/2020.emnlp-main.419/)
- [Juraska and Walker, 2021. Attention Is Indeed All You Need: Semantically Attention-Guided Decoding for Data-to-Text NLG.](https://aclanthology.org/2021.inlg-1.45/)



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
The primary motivation behind ViGGO was to create a data-to-text corpus in a new but conversational domain, and intended for use in open-domain chatbots rather than task-oriented dialogue systems. To this end, the dataset contains utterances of 9 generalizable and conversational dialogue act types, revolving around various aspects of video games. The idea is that similar, relatively small datasets could fairly easily be collected for other conversational domains -- especially other entertainment domains (such as music or books), but perhaps also topics like animals or food -- to support an open-domain conversational agent with controllable neural NLG.

Another desired quality of the ViGGO dataset was cleanliness (no typos and grammatical errors) and semantic accuracy, which has often not been the case with other crowdsourced data-to-text corpora. In general, for the data-to-text generation task, there is arguably no need to put the burden on the generation model to figure out the noise, since the noise would not be expected to be there in a real-world system whose dialogue manager that creates the input for the NLG module is usually configurable and tightly controlled.

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Produce a response from a structured meaning representation in the context of a conversation about video games. It can be a brief opinion or a description of a game, as well as a request for attribute (e.g., genre, player perspective, or platform) preference/confirmation or an inquiry about liking a particular type of games.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
no


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Crowdsourced`

#### Where was it crowdsourced?

<!-- info: If crowdsourced, where from? -->
<!-- scope: periscope -->
`Amazon Mechanical Turk`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
The paid crowdworkers who produced the reference utterances were from English-speaking countries, and they had at least 1,000 HITs approved and a HIT approval rate of 98% or more. Furthermore, in the instructions, crowdworkers were discouraged from taking on the task unless they considered themselves a gamer.

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
The dataset focuses on video games and their various aspects, and hence the language of the utterances may contain video game-specific jargon.

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by data curator

#### Data Preprocessing

<!-- info: How was the text data pre-processed? (Enter N/A if the text was not pre-processed) -->
<!-- scope: microscope -->
First, regular expressions were used to enforce several standardization policies regarding special characters, punctuation, and the correction of undesired abbreviations/misspellings of standard domain-specific terms (e.g., terms like "Play station" or "PS4" would be changed to the uniform "PlayStation"). At the same time, hyphens were removed or enforced uniformly in certain terms, for example, "single-player". Although phrases such as "first person" should correctly have a hyphen when used as adjective, the crowdworkers used this rule very inconsistently. In order to avoid model outputs being penalized during the evaluation by the arbitrary choice of a hyphen presence or absence in the reference utterances, the hyphen was removed in all such phrases regardless of the noun vs. adjective use.

Second, an extensive set of heuristics was developed to identify slot-related errors. This process revealed the vast majority of missing or incorrect slot mentions, which were subsequently fixed according to the corresponding MRs. This eventually led to the development of a robust, cross-domain, heuristic slot aligner that can be used for automatic slot error rate evaluation. For details, see the appendix in [Juraska and Walker, 2021](https://aclanthology.org/2021.inlg-1.45/).

Crowdworkers would sometimes also inject a piece of information which was not present in the MR, some of which is not even represented by any of the slots, e.g., plot or main characters. This unsolicited information was removed from the utterances so as to avoid confusing the neural model. Finally, any remaining typos and grammatical errors were resolved.

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
manually

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
Compliance with the indicated dialogue act type, semantic accuracy (i.e., all information in the corresponding MR mentioned and that correctly), and minimal extraneous information (e.g., personal experience/opinion). Whenever it was within a reasonable amount of effort, the utterances were manually fixed instead of being discarded/crowdsourced anew.


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
no


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
no PII

#### Justification for no PII

<!-- info: Provide a justification for selecting `no PII` above. -->
<!-- scope: periscope -->
Crowdworkers were instructed to only express the information in the provided meaning representation, which never prompted them to mention anything about themselves. Occasionally, they would still include a bit of personal experience (e.g., "I used to like the game as a kid.") or opinion, but these would be too general to be considered PII.


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



## Considerations for Using the Data

### PII Risks and Liability



### Licenses



### Known Technical Limitations

#### Technical Limitations

<!-- info: Describe any known technical limitations, such as spurrious correlations, train/test overlap, annotation biases, or mis-annotations, and cite the works that first identified these limitations when possible. -->
<!-- scope: microscope -->
The dataset is limited to a single domain: video games. One caveat of using a language generator trained on this dataset in a dialogue system as-is is that multiple subsequent turns discussing the same video game would be repeating its full name. ViGGO was designed for generation without context, and therefore it is up to the dialogue manager to ensure that pronouns are substituted for the names whenever it would sound more natural in a dialogue. Alternately, the dataset can easily be augmented with automatically constructed samples which omit the `name` slot in the MR and replace the name with a pronoun in the reference utterance.


