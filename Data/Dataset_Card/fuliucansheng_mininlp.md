
# Dataset Card for "MiniNLP"


## Dataset Description

### Dataset Summary

This is a mini-nlp dataset for unitorch package.

### Data Instances

#### plain_text

An example of 'train' looks as follows.
```
{
    "id": 1,
    "num": 3,
    "query": "Is this a test?",
    "doc": "train test",
    "label": "Good",
    "score": 0.882
}
```

### Data Fields

The data fields are the same among all splits.

#### plain_text
- `id`: a `int32` feature.
- `num`: a `int32` feature.
- `query`: a `string` feature.
- `doc`: a `string` feature.
- `label`: a `string` feature.
- `score`: a `float32` feature.


### Data Splits Sample Size

|   name   |train|validation|test|
|----------|----:|---------:|---:|
|plain_text|15000|     1000 |1000|
