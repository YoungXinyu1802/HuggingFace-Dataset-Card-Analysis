---
task_categories:
- text-classification
language:
- tr
- en
size_categories:
- 1K<n<10K
---
# AutoTrain Dataset for project: thycomments

## Dataset Description

This dataset has been automatically processed by HuggingFace AutoTrain for project tktktk.

### Languages

Turkish and English

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "@TK_TR 21 dk beklemem gerekti\u011fi s\u00f6yleniyor, m\u00fc\u015fteri temsilcisi ba\u011flanm\u0131yorum . \u0130nternet sitesinden de i\u015flem yap\u0131lam\u0131yor nas\u0131l \u00e7\u00f6z\u00fcm bulaca\u011f\u0131m ?",
    "target": 0
  },
  {
    "text": "@yhyustun Sevgili Yahya Bey Allah Rizasi icin bari sen bir aciklama yaparsan sevinirim.Konu su:Danimarkadan Turkiyeye ucuslar sistemde yok gorunuyor tum Mart ayi icin.1 Mart icin ucusum vardi fakat birkac gun once cagri merkeziyle gorustum ucuslar satisa kapanmis ancak bizim bir haberimiz",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(names=['negative', 'neutral', 'positive'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 2398 |
| valid        | 601 |