---
task_categories:
- summarization

---
# AutoTrain Dataset for project: exacts

## Dataset Description

This dataset has been automatically processed by AutoTrain for project exacts.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "How do plants adapt to different environments?",
    "target": "Plants adapt to different environments through a variety of mechanisms. Some examples include developing deep roots to access water in dry regions, growing smaller leaves to reduce water loss in hot regions, or producing chemicals to deter herbivores in regions with high herbivore populations."
  },
  {
    "text": "How do volcanoes erupt?",
    "target": "Volcanoes erupt when pressure from molten rock, ash, and gas inside the volcano builds up and eventually forces its way to the surface. This can happen through a volcano's central vent or through fissures on its slopes."
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
| train        | 156 |
| valid        | 39 |
