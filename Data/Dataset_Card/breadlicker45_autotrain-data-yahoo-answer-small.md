---
task_categories:
- summarization

---
# AutoTrain Dataset for project: yahoo-answer-small

## Dataset Description

This dataset has been automatically processed by AutoTrain for project yahoo-answer-small.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "how do you get a girl to like you? and how can you make her your girlfriend?",
    "target": "Be yourself.  It's the oldest and best advice.  She may still not like you, but that's the risk, and you keep your manliness and dignity.  Never, never forget this."
  },
  {
    "text": "how long is a bacterium's life?",
    "target": "It depends on the bacterium. For E. coli (common lab bacteria) 20-30 minutes is an average doubling time, but different strains vary.\\n\\nI heard something somewhere about a weird form of bacteria that lives miles underground in granite formations and only divides once every ten thousand years, or something crazy like that. I can't give you a source, it's just a freaky thing off the top of my head that I haven't gone to the trouble to confirm. My contention is that if reincarnation is true, that would be the *worst* thing to come back as. So mind your karma.\\n\\nPart of the reason it would be the worst is that bacteria reproduce by one cell dividing into two, so as long as there are any of that strain still alive, it hasn't really died.\\n\\nThey can die though. In a liquid culture you can tell because of a lot of turbidity (cloudiness) some of which is from cells and some from debris from dead cells. Or, you could have agar plates that get really nasty and dried up, and most of those bacteria are probably dead. Or you could tell because they look really crappy under a microscope. If you try to streak it and grow it on a plate and it doesn't grow, it's probably dead."
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 2399 |
| valid        | 600 |
