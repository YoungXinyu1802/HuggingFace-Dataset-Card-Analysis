## Convert conversational QA into statements.

This dataset is a variation on the dataset presented by [Demszky et al](https://arxiv.org/abs/1809.02922).
The main purpose of this work is to convert a series of questions and answers into a full statement representing the last answer. The items in this set are texts as in the following:

```bash
Q: Who built the famous decorated havelis in Rajasthan?
A: Rajput kings
Q: Jaipur is also known as what city?
A: the Pink City
Q: What are the notable houses in it made from?
A: a type of sandstone dominated by a pink hue

Statement:
Notable houses in Jaipur made from a type of sandstone dominated by a pink hue
```

The dataset has been created by limiting the set of [Demszky et al](https://arxiv.org/abs/1809.02922) to the SQUAD items. These questions and answers are made to appear as a conversation by artificially substituting some random entities (chosen from PERSON, GPE, ORG) with the relevant pronoun. For example, in the text above the last question contains "it" to indicate the city of Jaipur.