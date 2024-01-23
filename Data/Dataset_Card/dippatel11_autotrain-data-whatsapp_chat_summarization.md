---
language:
- en
task_categories:
- conditional-text-generation

---
# AutoTrain Dataset for project: whatsapp_chat_summarization

## Dataset Description

This dataset has been automatically processed by AutoTrain for project whatsapp_chat_summarization.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "feat_id": "13682435",
    "text": "Ella: Hi, did you get my text?\nJesse: Hey, yeah sorry- It's been crazy here. I'll collect Owen, don't worry about it :)\nElla: Oh thank you!! You're a lifesaver!\nJesse: It's not problem ;) Good luck with your meeting!!\nElla: Thanks again! :)",
    "target": "Jesse will collect Owen so that Ella can go for a meeting."
  },
  {
    "feat_id": "13728090",
    "text": "William: Hey. Today i saw you were arguing with Blackett.\nWilliam: Are you guys fine?\nElizabeth: Hi. Sorry you had to see us argue.\nElizabeth: It was just a small misunderstanding but we will solve it.\nWilliam: Hope so\nWilliam: You think I should to talk to him about it?\nElizabeth: No don't\nElizabeth: He won't like it that we talked after the argument.\nWilliam: Ok. But if you need any help, don't hesitate to call me\nElizabeth: Definitely",
    "target": "Elizabeth had an argument with Blackett today, but she doesn't want William to intermeddle."
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "feat_id": "Value(dtype='string', id=None)",
  "text": "Value(dtype='string', id=None)",
  "target": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 1600 |
| valid        | 400 |
