---
license: cc-by-sa-4.0
pretty_name: SQuAD for question generation
language: de
multilinguality: monolingual
size_categories: 1k<n<10K
source_datasets: lmqg/qg_dequad
task_categories:
- text-generation
task_ids:
- language-modeling
tags:
- question-generation
---

# Dataset Card for "lmqg/qag_dequad"


## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is the question & answer generation dataset based on the DEQuAD.

### Supported Tasks and Leaderboards
* `question-answer-generation`: The dataset is assumed to be used to train a model for question & answer generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).

### Languages
German (de)

## Dataset Structure
An example of 'train' looks as follows.
```
{
  "paragraph": "51._Bundesstaat === District of Columbia === Der District of Columbia gilt neben Puerto Rico als einer der aussichtsreichen Kandidaten für die Anerkennung als Bundesstaat in naher Zukunft. Die Einwohner des Bundesdistrikts gelten als größte Befürworter dieser Entscheidung, die jedoch einer Verfassungsänderung bedürfte. Die Anhänger nutzen das Motto des Unabhängigkeitskrieges in abgewandelter Form – „Taxation without representation“ –, um auf die mangelnde Repräsentation im Kongress hinzuweisen. Das Motto wird heute auf die Nummernschilder neu zugelassener Autos gedruckt (wobei der Fahrer alternativ die Internet-Adresse des D.C. wählen kann). Bill Clintons Präsidenten-Limousine hatte ein solches Nummernschild kurz vor Ende seiner Amtszeit. George W. Bush ließ diese Nummernschilder nach seinem Amtsantritt wieder entfernen. Die kleine ''D.C. Statehood Party'' vertrat diese Ansicht und vereinte sich mit den Grünen zur ''D.C. Statehood Green Party''. 1978 kamen sie ihrem Ziel am nächsten, als der Kongress das ''District of Columbia Voting Rights Amendment'' verabschiedete. Zwei Jahre später beriefen lokale Bürger mit einer Initiative eine konstitutionelle Versammlung für einen neuen Bundesstaat. 1982 ratifizierten die Wähler die Verfassung des Bundesstaates, der ''New Columbia'' heißen sollte. 1985 wurde der Plan jedoch gestoppt, als das Amendment scheiterte, weil es nicht von genug Staaten innerhalb von sieben Jahren ratifiziert wurde. Eine andere Möglichkeit wäre die Rückgliederung des Gebietes in den Bundesstaat Maryland. Damit würden die Einwohner des D.C. in den Genuss der Vorteile kommen, in einem Bundesstaat zu leben, ohne dass ein 51. Bundesstaat geschaffen werden müsste. Am 26. Juni 2020 stimmte das US-Repräsentantenhaus mit 232 zu 180 Stimmen dafür, den District of Columbia als 51. Bundesstaat anzuerkennen. Ein positives Votum des durch die Republikaner dominierten US-Senats gilt als unwahrscheinlich. Außerdem kündigte Präsident Trump sein Veto gegen ein solches, potenzielles Vorhaben an. Dennoch war es das erste positive Votum einer der beiden Kammern des US-Kongresses für eine Anerkennung als Bundesstaat.",
  "questions": [ "Was ist das Motto der Befürworter der Anerkennung von District of Columbia als neuer US-Bundesstaat?", "Warum hat die Anerkennung von District of Columbia zu einem neuen US-Bundesstaat 1985 nicht geklappt?", "Was war der potenzielle Name für den neuen US-Bundesstaat anstelle von District of Columbia?", "Aus welchen ehemaligen Parteien bestand die D.C. Statehood Green Party?" ],
  "answers": [ "das Motto des Unabhängigkeitskrieges in abgewandelter Form – „Taxation without representation“ ", "weil es nicht von genug Staaten innerhalb von sieben Jahren ratifiziert wurde", " ''New Columbia'' ", "Die kleine ''D.C. Statehood Party'' vertrat diese Ansicht und vereinte sich mit den Grünen" ],
  "questions_answers": "question: Was ist das Motto der Befürworter der Anerkennung von District of Columbia als neuer US-Bundesstaat?, answer: das Motto des Unabhängigkeitskrieges in abgewandelter Form – „Taxation without representation“ | question: Warum hat die Anerkennung von District of Columbia zu einem neuen US-Bundesstaat 1985 nicht geklappt?, answer: weil es nicht von genug Staaten innerhalb von sieben Jahren ratifiziert wurde | question: Was war der potenzielle Name für den neuen US-Bundesstaat anstelle von District of Columbia?, answer: ''New Columbia'' | question: Aus welchen ehemaligen Parteien bestand die D.C. Statehood Green Party?, answer: Die kleine ''D.C. Statehood Party'' vertrat diese Ansicht und vereinte sich mit den Grünen"
}
```
The data fields are the same among all splits.
- `questions`: a `list` of `string` features. 
- `answers`: a `list` of `string` features.
- `paragraph`: a `string` feature.
- `questions_answers`: a `string` feature.

## Data Splits

|train|validation|test |
|----:|---------:|----:|
|2489 |     1476 | 474 |


## Citation Information

```
@inproceedings{ushio-etal-2022-generative,
    title = "{G}enerative {L}anguage {M}odels for {P}aragraph-{L}evel {Q}uestion {G}eneration",
    author = "Ushio, Asahi  and
        Alva-Manchego, Fernando  and
        Camacho-Collados, Jose",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, U.A.E.",
    publisher = "Association for Computational Linguistics",
}
```