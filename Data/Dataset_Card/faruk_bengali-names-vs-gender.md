---
license: afl-3.0
---

# Bengali Female VS Male Names Dataset
An NLP dataset that contains 2030 data samples of Bengali names and corresponding gender both for female and male. This is a very small and simple toy dataset that can be used by NLP starters to practice sequence classification problem and other NLP problems like gender recognition from names.

# Background
In Bengali language, name of a person is dependent largely on their gender. Normally, name of a female ends with certain type of suffix "A", "I", "EE" ["আ", "ই", "ঈ"]. And the names of male are significantly different from female in terms of phoneme patterns and ending suffix. So, In my observation there is a significant possibility that these difference in patterns can be used for gender classification based on names.


Find the full documentation here:
[Documentation and dataset specifications](https://github.com/faruk-ahmad/bengali-female-vs-male-names)

## Dataset Format
The dataset is in CSV format. There are two columns- namely 
1. Name
2. Gender

Each row has two attributes. First one is name, second one is the gender. The name attribute is in ```utf-8``` encoding. And the second attribute i.e. the gender attribute has been signified by 0 and 1 as 

|   |   |
|---|---|
|male| 0|
|female| 1|
|   |   |

## Dataset Statistics
The number of samples per class is as bellow-

|   |   |
|---|---|
|male| 1029|
|female| 1001|
|   |   |

## Possible Use Cases
1. Sequence Classification using RNN, LSTM etc
2. Sequence modeling using other type of machine learning algorithms
3. Gender recognition based on names

## Disclaimer
The names were collected from internet using different sources like wikipedia, baby name suggestion websites, blogs etc. If someones name is in the dataset, that is totally unintentional.