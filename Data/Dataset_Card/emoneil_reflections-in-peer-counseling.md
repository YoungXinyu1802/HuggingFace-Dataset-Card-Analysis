---
annotations_creators:
- expert-generated
language: []
language_creators: []
license: []
pretty_name: Reflections in Peer Counseling
size_categories:
- 1K<n<10K
source_datasets: []
tags:
- gpt3
- natural language processing
- natural language generation
- peer counseling
task_categories:
- summarization
- text-generation
- conversational
task_ids:
- dialogue-generation
---

# Dataset Card for Reflections in Peer Counseling

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
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
  - [Contributions](#contributions)

## Dataset Description
- **Homepage:**
- **Repository:**
- **Paper: Automatic Reflection Generation for Peer-to-Peer Counseling**
- **Point of Contact: emoneil@sas.upenn.edu**

### Dataset Summary

The dataset derives from conversations between clients and counselors on a large peer-to-peer online counseling service. There are a total of 1061 observations across training and testing datasets, with 50 additional randomly sampled examples used in defining the few-shot learning prompt or for validation purposes in tuning hyperparameters, thus totaling 1111 observations across these sets. These observations were sourced from a larger dataset consisting of annotations of several different clinical counseling skills. We thus focus on the annotations of counselor reflections. The counselor reflections were annotated at utterance level with counselor verbal behaviors using the Motivational Interviewing Treatment Integrity 4.2 (MITI) and the Motivational Interviewing Skill Code 2.5 (MISC) manuals. Thus, the entire dataset consists of conversational context-counselor reflection pairs.

### Supported Tasks and Leaderboards

The dataset was used for conditioning and tuning generative models for generating reflection statements in the domain of peer-to-peer counseling.

### Languages

The language in the dataset is English.

## Dataset Structure

### Data Instances

Each instance consists of the chat room id of the conversation in which the dialogue occurred, the prompt which is the conversational context that immediately precedes the counselor reflection (including previous utterances from either the client or counselor up until and including the most recent prior client message that immediately followed a counselor’s message), and the completion which is the counselor reflection.

```
{
  'chat_id': "1234567",
  'prompt': "Client: I'm 19, he's 25. He's not very considerate of how I feel but says he cares about me and loves me.\nCounselor:",
  'completion': " The words are easy, actions are needed. Guys who are 25 just desire to have different experiences.\n\n",
}
```

### Data Fields

* `chat_id`: an integer defining the chat id of the conversation
* `prompt`: a string corresponding to the conversational context preceding the counselor reflection with the messages separated by new line characters and each utterance prepended by 'Client:' or 'Counselor:'. The string ends with 'Counselor:' to indicate that it is followed by the counselor completion described below.
* `completion`: a string corresponding to the counselor reflection

### Data Splits

The dataset is split into training, testing, and a small set of 50 examples used either for designing the few-shot learning prompt or tuning hyperparameters. 911 examples were used for training. 350 of these examples also constitute a reduced training set used in comparative experiments. 150 examples were used for testing. 50 of these testing examples (randomly selected) were used in the human evaluation. We ensured that the chat identifiers for messages in the test set uniquely differed from those included in the training set.

## Dataset Creation

### Curation Rationale

Reflective listening is a critical skill in peer-to-peer counseling that is only effective when tailored to the context. Thus, we wanted to home in on this particular skill and explore the potential of state-of-the-art language models for text generation in this domain.

### Source Data

#### Initial Data Collection and Normalization

The dataset was created by filtering the larger dataset of utterances annotated for many different counseling skills to only those counselor messages annotated as reflections. Then, the prompt instances were created by identifying the preceding messages for each of these counselor reflection instances. After the prompts were initially created, prompts with less than or equal to five words were removed.

The author created reference reflections for each of the 350 training example prompts in the reduced training set and each of the 150 testing example prompts. In creating a reference reflection given each conversational context, the author intended to simulate responding to the client in roughly the same time a counselor would as if this turn was embedded in a conversation the client was having with the author. This gauging of time is based on the author’s experience in volunteering as a counselor at crisis hotlines. It is possible that the reference reflections were created in roughly even less time than an average counselor response given that there were hundreds of conversational contexts for which reflections needed to be created.

#### Who are the source language producers?

The 'client' messages are utterances of those seeking mental health support on a large online counseling service platform. The 'counselor' messages are utterances of minimally-trained peer counselors of this large online counseling service.

For each of the 350 training example prompts in the reduced training set and each of the 150 testing example prompts, a reference reflection was also created by the author.

### Annotations

#### Annotation process

The human evaluation examined text of generative models fine-tuned on the full training set, a reduced training set, and reference reflections; a few-shot learning model; the actual counselor; and the reference reflection.

We administered a survey through Amazon Mechanical Turk Developer Sandbox. 50 of the testing prompts were provided along with the corresponding six response sources. Provided with the conversational context, the annotators evaluated responses based on three criteria: fluency, resemblance of reflection, and overall preference. Thus, for each context, evaluators measured the fluency, reflection resemblance, and overall preference for all six candidate responses. 

We used a variation of Efficient Annotation of Scalar Labels (EASL), a hybrid approach between direct assessment and online pairwise ranking aggregation and rank-based magnitude estimation. Evaluators saw all six responses at once (without knowledge of each response’s origin) and used a sliding scale from 1 to 5 to rate the responses based on each of the three dimensions. The order of the model responses for each conversational context was randomized. We provided examples of response ratings for ratings of 1 and 5 on the overall fluency and reflection resemblance dimensions. However, we did not include an example for overall preference, noting its subjectivity. The order of the model responses for each conversational context was randomized. We provided examples of response ratings for ratings of 1 and 5 on the overall fluency and reflection resemblance dimensions. However, we did not include an example for overall preference, noting its subjectivity.

Fluency refers to the response's overall fluency and human-likeness. In the instructions, we noted non-capitalized words and colloquial language are acceptable and not to be considered fluency errors. Reflection resemblance refers to whether the response captures and returns to the client something the client has said. Overall preference refers to the extent to which the evaluator likes the response.

Using Krippendorff’s alpha, we measured inter-annotator agreement, obtaining alpha values of -0.0369, 0.557, and 0.358 for overall fluency, reflection resemblance, and overall preference, respectively. Although these agreement values are low, the 0.557 inter-annotator agreement we obtained for reflection resemblance is notably higher than the inter-annotator agreement obtained for reflection likeness in the most relevant prior work.

#### Who are the annotators?

The three annotators recruited for the human evaluation were familiar with counseling reflections. All three annotators have worked with this large online counseling service dataset with IRB approval. They are quite familiar with motivational interviewing codes, annotating messages and using large language models for mass labeling.

### Personal and Sensitive Information

Due to the sensitive nature of this dataset and privacy concerns, we are unable to publicly share the data.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset of reflections in peer-to-peer counseling can be used as a reference point in understanding and evaluating counselor clinical skills and furthering the potential of language technology to be applied in this space. Given the sensitive nature of the mental health care context and the minimal training of these counselors, the use of such data requires care in understanding the limitations of technology defined based on this language.

### Discussion of Biases

Much of the language of conversations on this online counseling service platform is very informal and some client and counselor utterances may also contain pejorative language. 

As for the generated text assessed in the human evaluation of this work, it is important to note that GPT-3 was trained on over 45 terabytes of data from the internet and books, and large volumes of data collected from online sources will inevitably contain biases that may be captured. There may thus be inadvertent discrimination against subclasses of particular protected groups. Using generated responses as a source of guidance rather than using generative systems as the counselors themselves may be able to balance the benefits and risks of using artificial intelligence in delicate mental health settings. It is imperative that such systems are not misused by companies seeking to maximize efficiency and minimize cost.

The reference reflections in this work were created by the author, whose experience with counseling and motivational interviewing derives from over one hundred hours of training at a teen-to-teen crisis hotline and textline service and experience through a research fellowship developing and user testing a platform for nurses to practice and grow their motivational interviewing skills. Therefore, the reference reflections may not be as clinically precise as are possible from a medical professional, and the diversity of reflections is inherently limited.

### Other Known Limitations


## Additional Information

### Dataset Curators

Developed by Emma O'Neil, João Sedoc, Diyi Yang, Haiyi Zhu, Lyle Ungar.

### Licensing Information


### Citation Information


### Contributions

Thanks to [@emoneil](https://github.com/emoneil) for adding this dataset.