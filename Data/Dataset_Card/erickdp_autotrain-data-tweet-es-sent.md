---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: tweet-es-sent

## Dataset Description

This dataset has been automatically processed by AutoTrain for project tweet-es-sent.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "target": 1,
    "text": "1sola vuelta! arauz presidente! 1sola vuelta! todo 1 1sola la 1 es ecdor! por ti!1 por 1 los tuyos!1 por nosotros juntos1 mas de 45 d apoyo popular el 7 se vota 1por la vida por el futuro,por la esperanza guayaquil ec dor es 1"
  },
  {
    "target": 1,
    "text": "excelente decisi\u00f3n , las mujeres son importantes y por esa raz\u00f3n, a productos de primera necesidad hay que quitarles el iva "
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "target": "ClassLabel(num_classes=3, names=['0', '1', '2'], id=None)",
  "text": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 12400 |
| valid        | 3685 |
