---
annotations_creators:
- crowdsourced
language:
- en
license:
- mit
multilinguality:
- monolingual
size_categories:
- 10K<n<100k
task_categories:
- conversational
- text-generation
task_ids:
- dialogue-modeling
pretty_name: A Faithful Benchmark for Information-Seeking Dialogue
tags:
- faithful-dialogue-modeling
- trustworthy-dialogue-modeling
---

## Dataset Summary
FaithDial is a faithful knowledge-grounded dialogue benchmark, composed of **50,761** turns spanning **5649** conversations. It was curated through Amazon Mechanical Turk by asking annotators to amend hallucinated utterances in [Wizard of Wikipedia](https://parl.ai/projects/wizard_of_wikipedia/) (WoW). In our dialogue setting, we simulate interactions between two speakers: **an information seeker** and **a bot wizard**.  The seeker has a large degree of freedom as opposed to the wizard bot which is more restricted on what it can communicate. In fact, it must abide by the following rules: 
- **First**, it should be truthful by providing information that is attributable to the source knowledge *K*. 
- **Second**, it should provide information conversationally, i.e., use naturalistic phrasing of *K*, support follow-on discussion with questions, and prompt user's opinions. 
- **Third**, it should acknowledge its ignorance of the answer in those cases where *K* does not include it while still moving the conversation forward using *K*.

## Dataset Description

- **Homepage:** [FaithDial](https://mcgill-nlp.github.io/FaithDial/)
- **Repository:** [GitHub](https://github.com/McGill-NLP/FaithDial)
- **Point of Contact:** [Nouha Dziri](mailto:dziri@ualberta.ca)


## Language
English

## Data Instance

An example of 'train' looks as follows: 
```text
[
  {
    "utterances": [
      ... // prior utterances, 
      {
        "history": [
          "Have you ever been to a concert? They're so fun!",
          "No I cannot as a bot. However, have you been to Madonna's? Her 10th concert was used to help her 13th album called \"Rebel Heart\".",
          "Yeah I've heard of it but never went or what it was for. Can you tell me more about it?"
        ],
        "speaker": "Wizard",
        "knowledge": "It began on September 9, 2015, in Montreal, Canada, at the Bell Centre and concluded on March 20, 2016, in Sydney, Australia at Allphones Arena.",
        "original_response": "It started in September of 2015 and ran all the way through March of 2016. Can you imagine being on the road that long?",
        "response": "Sure. The concert started in September 9th of 2015 at Montreal, Canada. It continued till 20th of March of 2016, where it ended at Sydney, Australia.",
        "BEGIN": [
          "Hallucination",
          "Entailment"
        ],
        "VRM": [
          "Disclosure",
          "Question"
        ]
      }, 
      ... // more utterances
    ]
  }, 
  ... // more dialogues
]
```
If the `original_response` is empty, it means that the response is faithful to the source and we consider it as a FaithDial response. Faithful responses in WoW are also edited slightly if they are found to have some grammatical issues or typos. 
## Data Fields

 - `history`: `List[string]`. The dialogue history.
 - `knowledge`: `string`. The source knowkedge on which the bot wizard should ground its response.
 - `speaker`:  `string`.  The current speaker.
 - `original response`:  `string`.  The WoW original response before editing it.
 - `response`:   `string`.  The new Wizard response.
 - `BEGIN`:   `List[string]`. The BEGIN labels for the Wizard response.
 - `VRM`:  `List[string]`. The VRM labels for the wizard response.


## Data Splits

- `Train`: 36809 turns
- `Valid`: 6851 turns
- `Test`: 7101 turns

`Valid` includes both the `seen` and the `unseen` data splits from WoW. The same applies to `Test`. We also include those splits for FaithDial valid and test data. 

## Annotations
Following the guidelines for ethical crowdsourcing outlined in [Sheehan. 2018](https://www.tandfonline.com/doi/abs/10.1080/03637751.2017.1342043), 
we hire Amazon Mechanical Turk (AMT) workers to edit utterances in WoW dialogues that were found to exhibit unfaithful responses. To ensure clarity in the task definition, we provided detailed examples for our terminology. Moreover, we performed several staging rounds over the course of several months.

# Who are the annotators?

To be eligible for the task, workers have to be located in the United States and Canada and have to answer successfully 20 questions as part of a qualification test.  Before launching the main annotation task,  we perform a small pilot round (60 HITS) to check the performance of the workers. We email workers who commit errors, providing them with examples on how to fix their mistakes in future HITS. 

## Personal and Sensitive Information
Seeker utterances in FaithDial may contain personal and sensitive information. 

## Social Impact of Dataset
 In recent years, the conversational AI market has seen
a proliferation of a variety of applications—which are powered by large pre-trained LMs—that span
across a broad range of domains, such as customer
support, education, e-commerce, health, entertainment, etc. Ensuring that
these systems are trustworthy is key to deploy systems safely at a large scale in real-world application, especially in high-stake domain. FaithDial holds promise to encourage faithfulness in information-seeking dialogue and make virtual assistants both safer and more reliable. 

## Licensing Information

MIT

## Citation Information

```bibtex
@article{dziri2022faithdial,
  title={FaithDial: A Faithful Benchmark for Information-Seeking Dialogue},
  author={Dziri, Nouha and Kamalloo, Ehsan and Milton, Sivan and Zaiane, Osmar and Yu, Mo and Ponti, Edoardo and Reddy, Siva},
  journal={arXiv preprint, arXiv:2204.10757},
  year={2022},
  url={https://arxiv.org/abs/2204.10757}
}
```

