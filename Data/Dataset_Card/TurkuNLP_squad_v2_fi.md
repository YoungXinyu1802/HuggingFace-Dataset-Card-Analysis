---
license: cc-by-sa-4.0
task_categories:
- question-answering
language:
- fi
---

### Dataset Summary

This dataset is a DeepL -based machine translation of the English SQuAD2.0 dataset which combines the 100,000 questions in 
SQuAD1.1 with over 50,000 unanswerable questions written adversarially by crowdworkers to look similar to answerable ones. 
To do well on SQuAD2.0, systems must not only answer questions when possible, but also determine when no answer is supported 
by the paragraph and abstain from answering.

### Data Fields

The data fields are the same among all splits.

#### Example Data

```
{
    "title": "Victoria_(Australia)",
    "paragraphs": [
      {
        "qas": [
          {
            "question": "Millainen talous Victoriassa on?",
            "id": "570d2417fed7b91900d45c3d",
            "answers": [
              {
                "text": "monipuolinen",
                "answer_start": 26,
                "texts": [
                  "monipuolinen"
                ],
                "starts": [
                  26
                ]
              },
              {
                "text": "hyvin monipuolinen",
                "answer_start": 20,
                "texts": [
                  "hyvin ",
                  "monipuolinen"
                ],
                "starts": [
                  20,
                  26
                ]
              },
              {
                "text": "hyvin monipuolinen",
                "answer_start": 20,
                "texts": [
                  "hyvin ",
                  "monipuolinen"
                ],
                "starts": [
                  20,
                  26
                ]
              }
            ],
            "is_impossible": false
          }
        ],
        "context": "Victorian talous on hyvin monipuolinen: palvelualat, kuten rahoitus- ja kiinteistöpalvelut, terveydenhuolto, koulutus, tukkukauppa, vähittäiskauppa, majoitus- ja ravitsemistoiminta ja teollisuus muodostavat suurimman osan työllisyydestä. Victorian osavaltion bruttokansantuote on Australian toiseksi suurin, vaikka Victoria on asukaskohtaisen bruttokansantuotteen osalta neljäntenä, koska sen kaivostoiminta on vähäistä. Kulttuurin alalla Melbournessa on useita museoita, taidegallerioita ja teattereita, ja sitä kutsutaan myös \"Australian urheilupääkaupungiksi\". Melbournen krikettikenttä (Melbourne Cricket Ground) on Australian suurin stadion, ja siellä järjestettiin vuoden 1956 kesäolympialaiset ja vuoden 2006 Kansainyhteisön kisat. Kenttää pidetään myös australialaisen kriketin ja australialaisen jalkapallon \"henkisenä kotina\", ja se isännöi vuosittain Australian jalkapalloliigan (AFL) suurta loppuottelua, johon osallistuu yleensä yli 95 000 ihmistä. Victoriaan kuuluu kahdeksan julkista yliopistoa, joista vanhin, Melbournen yliopisto, on perustettu vuonna 1853."
      }
    ]
}
```

#### squad_v2

- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `text`: a `string` feature.
  - `answer_start`: a `int32` feature.
  - `texts`: a `string` feature.
  - `starts`: a `int32` feature.

### Data Splits

| name     |  train | validation |
| -------- | -----: | ---------: |
| squad_v2 | 130319 |      11873 |

### Evaluation Results

Results from fine-tuning [TurkuNLP/bert-base-finnish-cased-v1](ttps://huggingface.co/TurkuNLP/bert-base-finnish-cased-v1) for extractive question answering.

| dataset              | F1    |
| -------------------- | ----: |
| TurkuNLP/squad_v2_fi | 73.66 |
| ilmariky/SQuAD_v2_fi | 61.87 |

### Considerations for Using the Data

Due to DeepL terms and conditions, this dataset **must not be used for any machine translation work**, namely machine translation 
system development and evaluation of any kind. In general, we wish you do not pair the original English data with the translations 
except when working on research unrelated to machine translation, so as not to infringe on the terms and conditions.

### Licensing Information

Contents of this repository are distributed under the 
[Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/). 
Copyright of the dataset contents belongs to the original copyright holders.