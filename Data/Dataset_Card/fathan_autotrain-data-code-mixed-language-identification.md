---
task_categories:
- token-classification

---
# AutoTrain Dataset for project: code-mixed-language-identification

## Dataset Description

This dataset has been automatically processed by AutoTrain for project code-mixed-language-identification.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "feat_Unnamed: 0": 1104,
    "tokens": [
      "@user",
      "salah",
      "satu",
      "dari",
      "4",
      "anak",
      "dr",
      "sunardi",
      "ada",
      "yg",
      "berprofesi",
      "sbg",
      "dokter",
      "juga",
      ",",
      "lulusan",
      "unair",
      ",",
      "sudah",
      "selesai",
      "koas",
      "dan",
      "intern",
      "tolong",
      "disupport",
      "pak",
      "anak",
      "beliau"
    ],
    "tags": [
      6,
      1,
      1,
      1,
      6,
      1,
      6,
      6,
      1,
      1,
      1,
      1,
      1,
      1,
      6,
      1,
      6,
      6,
      1,
      1,
      1,
      1,
      0,
      1,
      3,
      1,
      1,
      1
    ]
  },
  {
    "feat_Unnamed: 0": 239,
    "tokens": [
      "@user",
      "kamu",
      "pake",
      "apa",
      "toh",
      "?",
      "aku",
      "pake",
      "xl",
      "banter",
      "lho",
      "di",
      "apartemen",
      "pun",
      "bisa",
      "download",
      "yutub"
    ],
    "tags": [
      6,
      1,
      1,
      1,
      1,
      6,
      1,
      1,
      6,
      1,
      1,
      1,
      1,
      1,
      1,
      0,
      6
    ]
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "feat_Unnamed: 0": "Value(dtype='int64', id=None)",
  "tokens": "Sequence(feature=Value(dtype='string', id=None), length=-1, id=None)",
  "tags": "Sequence(feature=ClassLabel(names=['EN', 'ID', 'JV', 'MIX_ID_EN', 'MIX_ID_JV', 'MIX_JV_EN', 'OTH'], id=None), length=-1, id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 1105 |
| valid        | 438 |
