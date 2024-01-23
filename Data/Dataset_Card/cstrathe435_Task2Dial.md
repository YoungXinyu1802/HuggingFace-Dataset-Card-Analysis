# Dataset Card for Task2Dial

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Acknowledgements] (#funding-information)

## Dataset Description

- **Homepage:** [Needs More Information]
- **Repository:** [Needs More Information]
- **Paper:** https://aclanthology.org/2021.icnlsp-1.28/
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

The Task2Dial dataset includes (1) a set of recipe documents with 353 individual dialogues; and (2) conversations between an IG and an IF, which are grounded in the associated recipe documents. Presents sample utterances from a dialogue along with the associated recipe. It demonstrates some important features of the dataset, such as mentioning entities not present in the recipe document; re-composition of the original text to focus on the important steps and the breakdown of the recipe into manageable and appropriate steps. Following recent efforts in the field to standardise NLG research, we have made the dataset freely available.

### Supported Tasks and Leaderboards

We demonstrate the task of implementing the Task2Dial in a conversational agent called chefbot in the following git repo: https://github.com/carlstrath/ChefBot

### Languages

English

### Data Fields

Dataset.1: Task2Dial main, 353 cooking recipes modelled on real conversations between an IF and IG.

Dataset. 2: A list of alternative ingredients for every swappable ingredient in the Task2Dial dataset.

Dataset. 3. A list of objects and utensils with explanations, comparisons, handling and common storage location information.

## Dataset Creation

The proposed task considers the recipe-following scenario with an information giver
(IG) and an information follower (IF), where the IG has access to the recipe and gives
instructions to the IF. The IG might choose to omit irrelevant information, simplify
the content of a recipe or provide it as is. The IF will either follow the task or ask
for further information. The IG might have to rely on information outside the given
document (i.e. commonsense) to enhance understanding and success of the task. In
addition, the IG decides on how to present the recipe steps, i.e. split them into sub-
steps or merge them together, often diverging from the original number of recipe steps.
The task is regarded as successful when the IG has successfully followed/understood
the recipe. Hence, other dialogue-focused metrics, such as the number of turns, are
not appropriate here. Formally, Task2Dial can be defined as follows: Given a recipe
𝑅𝑖 from 𝑅 =𝑅1, 𝑅2, 𝑅3,..., 𝑅𝑛, an ontology or ontologies 𝑂𝑖 =𝑂11,𝑂2,...,𝑂𝑛 of
cooking-related concepts, a history of the conversation ℎ, predict the response 𝑟 of
the IG.

### Curation Rationale

Text selection was dependent on the quality of the information
provided in the existing recipes. Too little information and the transcription and
interpretation of the text became diffused with missing or incorrect knowledge.
Conversely, providing too much information in the text resulted in a lack of creativity
and commonsense reasoning by the data curators. Thus, the goal of the curation was
to identify text that contained all the relevant information to complete the cooking
task (tools, ingredients, weights, timings, servings) but not in such detail that it
subtracted from the creativity, commonsense and imagination of the annotators.

### Source Data

#### Initial Data Collection and Normalization

Three open-source and creative commons licensed
cookery websites6 were identified for data extraction, which permits any use or non-
commercial use of data for research purposes. As content submission to the
cooking websites was unrestricted, data appropriateness was ratified by the ratings
and reviews given to each recipe by the public, highly rated recipes with a positive
feedback were given preference over recipes with low scores and poor reviews [38].
From this, a list of 353 recipes was compiled and divided amongst the annotators
for the data collection. As mentioned earlier, annotators were asked to take on the
roles of both IF and IG, rather than a multi-turn WoZ approach, to allow flexibility
in the utterances. This approach allowed the annotators additional time to formulate
detailed and concise responses.

#### Who are the source language producers?

Undergraduate RAs were recruited through email.
The participants were paid an hourly rate based on a university pay scale which is
above the living wage and corresponds to the real living wage, following ethical
guidelines for responsible innovation. The annotation team was composed of
two males and one female data curators, under the age of 25 of mixed ethnicity’s with
experience in AI and computing. This minimised the gender bias that is frequently
observed in crowdsourcing platforms.

#### Annotation process

Each annotator was provided with a detailed list of instructions, an example dialogue and an IF/IG template (see Appendix A). The annotators were asked to read both the example dialogue and the original recipe to understand the text, context, composition, translation and annotation. The instructions included information handling and storage of data, text formatting, metadata and examples of high-quality and poor dialogues. An administrator was on hand throughout the data collection to support and guide the annotators. This approach reduced the number of low-quality dialogues associated with large crowdsourcing platforms that are often discarded post evaluation, as demonstrated in the data collection of the Doc2Dial dataset.

#### Who are the annotators?

Research assistants (RAs) from the School of Computing were employed on temporary contracts to construct and format the dataset. After an initial meeting to discuss the job role and determine suitability, the RAs were asked to complete a paid trial, this was evaluated and further advice was given on how to write dialogues and format the data to ensure high quality. After the successful completion of the trial, the RAs were permitted to continue with the remainder of the data collection. To ensure the high quality of the dataset, samples of the dialogues were often reviewed and further feedback was provided. 

### Personal and Sensitive Information

An ethics request was submitted for review by the board of ethics at our university. No personal or other data that may be used to identify an individual was collected in this study. 

## Considerations for Using the Data

The Task2Dial dataset is currently only for the cooking domain, but using the methodologies provided other tasks can be modelled for example, furniture assembly and maintenance tasks.

### Social Impact of Dataset

Our proposed task aims to motivate research for modern dialogue systems that
address the following challenges. Firstly, modern dialogue systems should be flexible
and allow for "off-script" scenarios in order to emulate real-world phenomena, such
as the ones present in human-human communication. This will require new ways
of encoding user intents and new approaches to dialogue management in general.
Secondly, as dialogue systems find different domain applications, the complexity
of the dialogues might increase as well as the reliance on domain knowledge that
can be encoded in structured or unstructured ways, such as documents, databases
etc. Many applications, might require access to different domain knowledge sources
in a course of a dialogue, and in such context, selection might prove beneficial in
choosing "what to say".

### Discussion of Biases

Prior to data collection, we performed three pilot studies.
In the first, two participants assumed the roles of IG and IF respectively, where the
IG had access to a recipe and provided recipe instructions to the IF (who did not have
access to the recipe) over the phone, recording the session and then transcribing it.
Next, we repeated the process with text-based dialogue through an online platform
following a similar setup, however, the interaction was solely chat-based. The final
study used self-dialogue, with one member of the team writing entire dialogues
assuming both the IF and IG roles. We found that self-dialogue results were proximal
to the results of two-person studies. However, time and cost were higher for producing
two-person dialogues, with the additional time needed for transcribing and correction,
thus, we opted to use self-dialogue.

## Additional Information

Video: https://www.youtube.com/watch?v=zISkwn95RXs&ab_channel=ICNLSPConference

### Dataset Curators

The recipes are composed by people of a different races
/ ethnicity, nationalities, socioeconomic status, abilities, age, gender and language
with significant variation in pronunciations, structure, language and grammar. This
provided the annotators with unique linguistic content for each recipe to interpret
the data and configure the text into an IF/IG format. To help preserve sociolinguistic
patterns in speech, the data curators retained the underlying language when para-
phrasing, to intercede social and regional dialects with their own interpretation of
the data to enhance the lexical richness.

### Licensing Information

CC

### Citation Information

https://aclanthology.org/2021.icnlsp-1.28/

### Acknowledgements

The research is supported under the EPSRC projects CiViL (EP/T014598/1) and
NLG for low-resource domains (EP/T024917/1).