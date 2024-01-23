---
language:
- en
task_categories:
- text-classification

---
# AutoTrain Dataset for project: honor

## Dataset Description

This dataset has been automatically processed by AutoTrain for project honor.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "\"Kimchi (kimchee) is a Korean dish which is well known throughout the world. It is a spicy, tangy and pungent food that contains pickled vegetables. The word \"Kimchi\" comes from the Korean \"Kim\" meaning \"turn\" and \"Chi\" meaning \"sauce\".\\n\\nKimchi consists of vegetables which are salted, fermented and seasoned. It is an important part of the Korean diet. The two main methods of preparing Kimchi are fermentation and salting. Fermented Kimchi is made by mixing cabbage, radish and other vegetables with a specific kind of salt and sugar. Salted Kimchi is made by mixing cabbage, radish and other vegetables with a specific amount of salt and some vinegar.\\n\\nThe standard vegetables used in preparing Kimchi include cabbage, radish, turnip and Chinese cabbage. However, there are many different variations of Kimchi. Some of the variations include Kimchi with beef, Kimchi with fish and Kimchi with soybean paste.\\n\\nThe preparation of Kimchi is considered to be an important part of Korean culture. It is prepared in a ritualistic manner. The Korean culture also consider it as a \"doorway\" to a family's hearth.",
    "target": 1,
    "feat_meta.pile_set_name": "GPT-3"
  },
  {
    "text": "So how did you survive the terrible British summer of 2015? (Mine was miserable. There were too many weekends at home in the garden, that's all I can say.) Well, it's a new year and a new season of Doctor Who, with Peter Capaldi as our time-travelling hero.\\n\\nHere's the first photo of Capaldi in costume:\\n\\nAnd here's how it all begins...\\n\\nThis story is called The Magician's Apprentice and features Missy (the Master, if you didn't know).\\n\\nAnd here's a trailer:\\n\\nAll we can say is: A spooky church? The Doctor having to answer questions about his mistakes? Yes, please! We can't wait to see more.\\n\\nDoctor Who series 9 begins on Saturday 19 September on BBC One.",
    "target": 1,
    "feat_meta.pile_set_name": "GPT-3"
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(names=['human', 'machine'], id=None)",
  "feat_meta.pile_set_name": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 3212 |
| valid        | 804 |
