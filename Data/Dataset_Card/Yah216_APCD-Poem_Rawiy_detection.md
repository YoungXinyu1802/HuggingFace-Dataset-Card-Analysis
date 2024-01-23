---
language:
- ar
task_categories:
- text-classification
---
# AutoTrain Dataset for project: Poem_Rawiy_detection

## Dataset Descritpion

We used the APCD dataset cited hereafter for pretraining the model. The dataset has been cleaned and only the main text and the Qafiyah columns were kept:
```
@Article{Yousef2019LearningMetersArabicEnglish-arxiv,
  author =       {Yousef, Waleed A. and Ibrahime, Omar M. and Madbouly, Taha M. and Mahmoud,
                  Moustafa A.},
  title =        {Learning Meters of Arabic and English Poems With Recurrent Neural Networks: a Step
                  Forward for Language Understanding and Synthesis},
  journal =      {arXiv preprint arXiv:1905.05700},
  year =         2019,
  url =          {https://github.com/hci-lab/LearningMetersPoems}
}
```

### Languages

The BCP-47 code for the dataset's language is ar.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "\u0643\u0644\u0651\u064c \u064a\u064e\u0632\u0648\u0644\u064f \u0633\u064e\u0631\u064a\u0639\u0627\u064b \u0644\u0627 \u062b\u064e\u0628\u0627\u062a\u064e \u0644\u0647\u064f    \u0641\u0643\u064f\u0646 \u0644\u0650\u0648\u064e\u0642\u062a\u0643\u064e \u064a\u0627 \u0645\u0650\u0633\u0643\u064a\u0646\u064f \u0645\u064f\u063a\u062a\u064e\u0646\u0650\u0645\u0627",
    "target": 27
  },
  {
    "text": "\u0648\u0642\u062f \u0623\u0628\u0631\u0632\u064e \u0627\u0644\u0631\u0651\u064f\u0645\u0651\u064e\u0627\u0646\u064f \u0644\u0644\u0637\u0631\u0641\u0650 \u063a\u064f\u0635\u0652\u0646\u064e\u0647\u064f    \u0646\u0647\u0648\u062f\u0627\u064b \u062a\u064f\u0635\u0627\u0646\u064f \u0627\u0644\u0644\u0645\u0633\u064e \u0639\u0646 \u0643\u0641\u0651\u0650 \u0623\u062d\u0645\u0642\u0650",
    "target": 23
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=35, names=['\u0621', '\u0624', '\u0627', '\u0628', '\u062a', '\u062b', '\u062c', '\u062d', '\u062e', '\u062f', '\u0630', '\u0631', '\u0632', '\u0633', '\u0634', '\u0635', '\u0636', '\u0637', '\u0637\u0646', '\u0638', '\u0639', '\u063a', '\u0641', '\u0642', '\u0643', '\u0644', '\u0644\u0627', '\u0645', '\u0646', '\u0647', '\u0647\u0640', '\u0647\u0646', '\u0648', '\u0649', '\u064a'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 1347718 |
| valid        | 336950 |
