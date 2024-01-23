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

## The interesting part

The user rating, alexa score (probably the times called by alexa) available as well as different answers provided by different users. These attributes make it possible to train a human preference model (Reward model in RLHF) by ranking answer with higher score better than lower score counterpart. 

Each question-answers are formatted as below:

The answers are in list of text-score pairs. If you want to train a reward model, you will have to handle the tie answers yourself.

```
{
  "question": "what did don cherry say to get him fired",
  "answers": [
    [
      "Cherry, 85, was fired by Sportsnet after saying Nov. ... He went on Fox News to say he believed he was fired because he used the words \"you people\" instead of \"everybody.\" Hall of Famer Bobby Orr, who was coached by Cherry, was among those who supported him, calling the firing \"disgraceful.\"",
      7.0
    ],
    [
      "Don Cherry, Canada's most polarizing, flamboyant and opinionated hockey commentator, was fired Monday for calling immigrants \"you people\" in a television rant in which he said new immigrants are not honoring the country's fallen soldiers.",
      0.0
    ],
    [
      "Don Cherry, the flamboyant hockey commentator, was fired from his employment for an anti-immigrant rant. ",
      0.0
    ]
  ],
  "topics": "film and tv"
}
```

# Dataset stats

The split is same as [alexa-qa](https://huggingface.co/datasets/theblackcat102/alexa-qa) but only questions with more than 1 answers. The total dataset size is 70,483

Train : 49,368

Test : 14,075

Validation : 7,040


# Last update

19/02/2023
