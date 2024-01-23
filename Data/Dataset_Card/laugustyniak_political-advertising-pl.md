---
annotations_creators:
- hired_annotators
language_creators:
- found
language:
- pl
license:
- other
multilinguality:
- monolingual
size_categories:
- 10<n<10K
task_categories:
- token-classification
task_ids:
- named-entity-recognition
- part-of-speech
pretty_name: Polish-Political-Advertising
---

# Polish-Political-Advertising

## Info

Political campaigns are full of political ads posted by candidates on social media. Political advertisement constitute a basic form of campaigning, subjected to various social requirements. We present the first publicly open dataset for detecting specific text chunks and categories of political advertising in the Polish language. It contains 1,705 human-annotated tweets tagged with nine categories, which constitute campaigning under Polish electoral law.

> We achieved a 0.65 inter-annotator agreement (Cohen's kappa score). An additional annotator resolved the mismatches between the first two annotators improving the consistency and complexity of the annotation process.

## Tasks (input, output and metrics)

Political Advertising Detection

**Input** ('*tokens'* column): sequence of tokens

**Output** ('tags*'* column):  sequence of tags 

**Domain**: politics

**Measurements**: F1-Score (seqeval)

**Example:**

Input: `['@k_mizera', '@rdrozd', 'Problemem', 'jest', 'mała', 'produkcja', 'dlatego', 'takie', 'ceny', '.', '10', '000', 'mikrofirm', 'zamknęło', 'się', 'w', 'poprzednim', 'tygodniu', 'w', 'obawie', 'przed', 'ZUS', 'a', 'wystarczyło', 'zlecić', 'tym', 'co', 'chcą', 'np', '.', 'szycie', 'masek', 'czy', 'drukowanie', 'przyłbic', 'to', 'nie', 'wymaga', 'super', 'sprzętu', ',', 'umiejętności', '.', 'nie', 'będzie', 'pit', ',', 'vat', 'i', 'zus', 'będą', 'bezrobotni']`

Input (translated by DeepL): `@k_mizera @rdrozd The problem is small production that's why such prices . 10,000 micro businesses closed down last week for fear of ZUS and all they had to do was outsource to those who want e.g . sewing masks or printing visors it doesn't require super equipment , skills . there will be no pit , vat and zus will be unemployed`

Output: `['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-WELFARE', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-WELFARE', 'O', 'B-WELFARE', 'O', 'B-WELFARE', 'O', 'B-WELFARE']`


## Data splits

| Subset     |   Cardinality |
|:-----------|--------------:|
| train      |          1020 |
| test       |           341 |
| validation |           340 |

## Class distribution

| Class                           |   train |   validation |   test |
|:--------------------------------|--------:|-------------:|-------:|
| B-HEALHCARE                     |   0.237 |        0.226 |  0.233 |
| B-WELFARE                       |   0.210 |        0.232 |  0.183 |
| B-SOCIETY                       |   0.156 |        0.153 |  0.149 |
| B-POLITICAL_AND_LEGAL_SYSTEM    |   0.137 |        0.143 |  0.149 |
| B-INFRASTRUCTURE_AND_ENVIROMENT |   0.110 |        0.104 |  0.133 |
| B-EDUCATION                     |   0.062 |        0.060 |  0.080 |
| B-FOREIGN_POLICY                |   0.040 |        0.039 |  0.028 |
| B-IMMIGRATION                   |   0.028 |        0.017 |  0.018 |
| B-DEFENSE_AND_SECURITY          |   0.020 |        0.025 |  0.028 |

## License

[Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Links

[HuggingFace](https://huggingface.co/datasets/laugustyniak/political-advertising-pl)

[Paper](https://aclanthology.org/2020.winlp-1.28/)

## Citing

> ACL WiNLP 2020 Paper

```bibtex
@inproceedings{augustyniak-etal-2020-political,
    title = "Political Advertising Dataset: the use case of the Polish 2020 Presidential Elections",
    author = "Augustyniak, Lukasz and Rajda, Krzysztof and Kajdanowicz, Tomasz and Bernaczyk, Micha{\l}",
    booktitle = "Proceedings of the The Fourth Widening Natural Language Processing Workshop",
    month = jul,
    year = "2020",
    address = "Seattle, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.winlp-1.28",
    pages = "110--114"
}
```
