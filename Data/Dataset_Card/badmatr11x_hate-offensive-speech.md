---
license: mit
language:
  - en
size_categories:
  - 10K<n<100K
source_dataset:
  - original
task_categories:
  - text-classification
task_ids:
  - multi-label-classification
dataset_info:
  features:
    - name: label
      dtype: int64
    - name: tweet
      dtype: string
  splits:
    - name: train
      num_bytes: 5045816.7990131285
      num_examples: 51070
    - name: test
      num_bytes: 280301.1995065645
      num_examples: 2837
    - name: validation
      num_bytes: 280400.0014803066
      num_examples: 2838
  download_size: 3879287
  dataset_size: 5606517.999999999
---

# **Dataset Card for Hate-Offensive Speech**

This is the original dataset created by the user [badmatr11x](https://www.huggingface.co/badmatr11x/). Datasets contains the annotated tweets classifying into the three categories; **hate-speech**, **offensive-speech** and **neither**.

# **Dataset Structure**

Database Structure as follows:

```
{
  "label": {
    0: "hate-speech",
    1: "offensive-speech",
    2: "neither"
  },
  "tweet": <string>
}
```

### **Dataset Instances**

Examples from the datasets as follows:

Lable-0 (Hate Speech)

```
{
  "label": 0,
  "tweet": "@user @user @user we were? maybe you are-but don't you dare demonize innocent infants born with white skin, "
}
```

Label-1 (Offensive Speech)

```
{
  "label": 1,
  "tweet": "...and I'm goin back to school.. only for the hoes and a class or two"
}
```

Label-2 (Neither)

```
{
  "label": 2,
  "tweet": "@user @user are you guys going to take forever to bring the new gmc?"
}
```

# **Data Fields**

- `label`: a int64 value
- `tweet`: a string

# **Data Splits**

- Datasets splits into the three parts; train, validation and test.
- Training datasets contains 90% tweeets, validation contains 5% and rest of 5% assigned to test datasets.
