---
language:
- en
- es
task_categories:
- translation
---
# AutoTrain Dataset for project: Rusynpannonianpure

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project Rusynpannonianpure.

### Languages

The BCP-47 code for the dataset's language is en2es.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "source": "\"I came to the region to meet with the leaders of the parties and discuss the progress in normalizin[...]",
    "target": "\"\u042f \u043f\u0440\u0438\u0448\u043e\u043b \u0434\u043e \u0440\u0435\u0491\u0438\u043e\u043d\u0443 \u043f\u0440\u0438\u0440\u0438\u0445\u0442\u0430\u0446 \u0448\u043b\u0457\u0434\u0443\u044e\u0446\u0438 \u0441\u0445\u043e\u0434 \u043b\u0438\u0434\u0435\u0440\u043e\u0445 \u0438 \u0431\u0435\u0448\u0435\u0434\u043e\u0432\u0430\u0446 \u043e \u043d\u0430\u043f\u0440\u0435\u0434\u043e\u0432\u0430\u043d\u044e \u0443 \u043d\u043e\u0440\u043c\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0457 \u043e\u0434\u043d\u043e\u0448\u0435[...]"
  },
  {
    "source": "\"We had a very good discussion yesterday evening about the situation and it is normal to look for a [...]",
    "target": "\"\u041c\u0430\u043b\u0438 \u0437\u043c\u0435 \u0454\u0434\u043d\u0443 \u043e\u0437\u0431\u0438\u043b\u044c\u043d\u0443 \u0440\u043e\u0437\u0433\u0432\u0430\u0440\u043a\u0443 \u0432\u0447\u0435\u0440\u0430 \u0432\u0435\u0447\u0430\u0440 \u043e \u0441\u0438\u0442\u0443\u0430\u0446\u0438\u0457 \u0438 \u043d\u043e\u0440\u043c\u0430\u043b\u043d\u043e \u0436\u0435 \u043f\u043e\u0442\u0440\u0435\u0431\u043d\u0435 \u0433\u043b\u0454\u0434\u0430\u0446 \u0440\u0438\u0448\u0435\u043d\u0454 \u043f\u0440\u0435\u0437 \u0434[...]"
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "source": "Value(dtype='string', id=None)",
  "target": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 3 |
| valid        | 1 |
