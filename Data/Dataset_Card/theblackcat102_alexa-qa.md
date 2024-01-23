---
license: mit
task_categories:
- question-answering
language:
- en
pretty_name: Alexa Question Answering dataset
tags:
- alexa
size_categories:
- 10K<n<100K
---
# Alexa Answers from [alexaanswers.amazon.com](https://alexaanswers.amazon.com/)

The Alexa Answers community helps to improve Alexa’s knowledge and answer questions asked by Alexa users. Which contains some very quirky and hard question like

Q: what percent of the population has blackhair

A: The most common hair color in the world is black and its found in wide array of background and ethnicities. About 75 to 85% of the global population has either black hair or the deepest brown shade.

Q: what was the world population during world war two

A: 2.3 billion

However, with unusual questions there are unsual answers.

Q: what is nascar poem

A: Roses are red; Violets are blue; For Blaney's new ride; Switch the 1 and the 2.

there's no official nascar poem

# Dataset stats

Total dataset size are 136039 and splitted into train-test-validation via 7-2-1 ratio. The split are same as [alexa-qa-with-rank](https://huggingface.co/datasets/theblackcat102/alexa-qa-with-rank), so no train question in alexa-qa can be found in validation and test splits in alex-qa-with-rank.

Train : 95,227

Test : 27,208

Validation : 13,604

Do note that similar repharses of question does exist between splits and I will leave the study to others.


# Last update

19/02/2023
