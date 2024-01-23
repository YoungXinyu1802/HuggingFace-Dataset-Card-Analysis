---
language:
- de
multilinguality:
- monolingual
source_datasets:
- original
task_categories:
- question-answering
- text-retrieval
task_ids:
- extractive-qa
- closed-domain-qa
thumbnail: https://thumb.tildacdn.com/tild3433-3637-4830-a533-353833613061/-/resize/720x/-/format/webp/germanquad.jpg
---

![bert_image](https://thumb.tildacdn.com/tild3433-3637-4830-a533-353833613061/-/resize/720x/-/format/webp/germanquad.jpg)
# Dataset Card for germandpr

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://deepset.ai/germanquad
- **Repository:** https://github.com/deepset-ai/haystack
- **Paper:** https://arxiv.org/abs/2104.12741

### Dataset Summary

We take GermanQuAD as a starting point and add hard negatives from a dump of the full German Wikipedia following the approach of the DPR authors (Karpukhin et al., 2020). The format of the dataset also resembles the one of DPR. GermanDPR comprises 9275 question/answerpairs in the training set and 1025 pairs in the test set. For eachpair, there are one positive context and three hard negative contexts.

### Supported Tasks and Leaderboards

- `open-domain-qa`, `text-retrieval`: This dataset is intended to be used for `open-domain-qa` and text retrieval tasks.

### Languages

The sentences in the dataset are in German (de).

## Dataset Structure

### Data Instances

A sample from the training set is provided below:

```
{
    "question": "Wie viele christlichen Menschen in Deutschland glauben an einen Gott?",
    "answers": [
        "75 % der befragten Katholiken sowie 67 % der Protestanten glaubten an einen Gott (2005: 85 % und 79 %)"
    ],
    "positive_ctxs": [
        {
            "title": "Gott",
            "text": "Gott\
=== Demografie ===
Eine Zusammenfassung von Umfrageergebnissen aus verschiedenen Staaten ergab im Jahr 2007, dass es weltweit zwischen 505 und 749 Millionen Atheisten und Agnostiker gibt. Laut der Encyclopædia Britannica gab es 2009 weltweit 640 Mio. Nichtreligiöse und Agnostiker (9,4 %), und weitere 139 Mio. Atheisten (2,0 %), hauptsächlich in der Volksrepublik China.\\\\\\\\
Bei einer Eurobarometer-Umfrage im Jahr 2005 wurde festgestellt, dass 52 % der damaligen EU-Bevölkerung glaubt, dass es einen Gott gibt. Eine vagere Frage nach dem Glauben an „eine andere spirituelle Kraft oder Lebenskraft“ wurde von weiteren 27 % positiv beantwortet. Bezüglich der Gottgläubigkeit bestanden große Unterschiede zwischen den einzelnen europäischen Staaten. Die Umfrage ergab, dass der Glaube an Gott in Staaten mit starkem kirchlichen Einfluss am stärksten verbreitet ist, dass mehr Frauen (58 %) als Männer (45 %) an einen Gott glauben und dass der Gottglaube mit höherem Alter, geringerer Bildung und politisch rechtsgerichteten Ansichten korreliert.\\\\\\\\
Laut einer Befragung von 1003 Personen in Deutschland im März 2019 glauben 55 % an einen Gott; 2005 waren es 66 % gewesen. 75 % der befragten Katholiken sowie 67 % der Protestanten glaubten an einen Gott (2005: 85 % und 79 %). Unter Konfessionslosen ging die Glaubensquote von 28 auf 20 % zurück. Unter Frauen (60 %) war der Glauben 2019 stärker ausgeprägt als unter Männern (50 %), in Westdeutschland (63 %) weiter verbreitet als in Ostdeutschland (26 %).",
            "passage_id": ""
        }
    ],
    "negative_ctxs": [],
    "hard_negative_ctxs": [
        {
            "title": "Christentum",
            "text": "Christentum\
\
=== Ursprung und Einflüsse ===\
Die ersten Christen waren Juden, die zum Glauben an Jesus Christus fanden. In ihm erkannten sie den bereits durch die biblische Prophetie verheißenen Messias (hebräisch: ''maschiach'', griechisch: ''Christos'', latinisiert ''Christus''), auf dessen Kommen die Juden bis heute warten. Die Urchristen übernahmen aus der jüdischen Tradition sämtliche heiligen Schriften (den Tanach), wie auch den Glauben an einen Messias oder Christus (''christos'': Gesalbter). Von den Juden übernommen wurden die Art der Gottesverehrung, das Gebet der Psalmen u. v. a. m. Eine weitere Gemeinsamkeit mit dem Judentum besteht in der Anbetung desselben Schöpfergottes. Jedoch sehen fast alle Christen Gott als ''einen'' dreieinigen Gott an: den Vater, den Sohn (Christus) und den Heiligen Geist. Darüber, wie der dreieinige Gott konkret gedacht werden kann, gibt es unter den christlichen Konfessionen und Gruppierungen unterschiedliche Auffassungen bis hin zur Ablehnung der Dreieinigkeit Gottes (Antitrinitarier). Der Glaube an Jesus Christus führte zu Spannungen und schließlich zur Trennung zwischen Juden, die diesen Glauben annahmen, und Juden, die dies nicht taten, da diese es unter anderem ablehnten, einen Menschen anzubeten, denn sie sahen in Jesus Christus nicht den verheißenen Messias und erst recht nicht den Sohn Gottes. Die heutige Zeitrechnung wird von der Geburt Christi aus gezählt. Anno Domini (A. D.) bedeutet „im Jahr des Herrn“.",
            "passage_id": ""
        },
        {
            "title": "Noachidische_Gebote",
            "text": "Noachidische_Gebote\
\
=== Die kommende Welt ===\
Der Glaube an eine ''Kommende Welt'' (Olam Haba) bzw. an eine ''Welt des ewigen Lebens'' ist ein Grundprinzip des Judentums. Dieser jüdische Glaube ist von dem christlichen Glauben an das ''Ewige Leben'' fundamental unterschieden. Die jüdische Lehre spricht niemandem das Heil dieser kommenden Welt ab, droht aber auch nicht mit Höllenstrafen im Jenseits. Juden glauben schlicht, dass allen Menschen ein Anteil der kommenden Welt zuteilwerden kann. Es gibt zwar viele Vorstellungen der kommenden Welt, aber keine kanonische Festlegung ihrer Beschaffenheit; d. h., das Judentum kennt keine eindeutige Antwort darauf, was nach dem Tod mit uns geschieht. Die Frage nach dem Leben nach dem Tod wird auch als weniger wesentlich angesehen, als Fragen, die das Leben des Menschen auf Erden und in der Gesellschaft betreffen.\
Der jüdische Glaube an eine kommende Welt bedeutet nicht, dass Menschen, die nie von der Tora gehört haben, böse oder sonst minderwertige Menschen sind. Das Judentum lehrt den Glauben, dass alle Menschen mit Gott verbunden sind. Es gibt im Judentum daher keinen Grund, zu missionieren. Das Judentum lehrt auch, dass alle Menschen sich darin gleichen, dass sie weder prinzipiell gut noch böse sind, sondern eine Neigung zum Guten wie zum Bösen haben. Während des irdischen Lebens sollte sich der Mensch immer wieder für das Gute entscheiden.",
            "passage_id": ""
        },
        {
            "title": "Figuren_und_Schauplätze_der_Scheibenwelt-Romane",
            "text": "Figuren_und_Schauplätze_der_Scheibenwelt-Romane\
\
=== Herkunft ===\
Es gibt unzählig viele Götter auf der Scheibenwelt, die so genannten „geringen Götter“, die überall sind, aber keine Macht haben. Erst wenn sie durch irgendein Ereignis Gläubige gewinnen, werden sie mächtiger. Je mehr Glauben, desto mehr Macht. Dabei nehmen sie die Gestalt an, die die Menschen ihnen geben (zum Beispiel Offler). Wenn ein Gott mächtig genug ist, erhält er Einlass in den Cori Celesti, den Berg der Götter, der sich in der Mitte der Scheibenwelt erhebt. Da Menschen wankelmütig sind, kann es auch geschehen, dass sie den Glauben verlieren und einen Gott damit entmachten (s. „Einfach Göttlich“).",
            "passage_id": ""
        }
    ]
},
```

### Data Fields

- `positive_ctxs`: a dictionary feature containing:
  - `title`: a `string` feature.
  - `text`: a `string` feature.
  - `passage_id`: a `string` feature.
- `negative_ctxs`: a dictionary feature containing:
  - `title`: a `string` feature.
  - `text`: a `string` feature.
  - `passage_id`: a `string` feature.
- `hard_negative_ctxs`: a dictionary feature containing:
  - `title`: a `string` feature.
  - `text`: a `string` feature.
  - `passage_id`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a list feature containing:
  - a `string` feature.
  
### Data Splits

The dataset is split into a training set and a test set.
The final GermanDPR dataset comprises 9275
question/answer pairs in the training set and 1025
pairs in the test set. For each pair, there are one
positive context and three hard negative contexts.

|      |questions|answers|positive contexts|hard negative contexts|
|------|--------:|------:|----------------:|---------------------:|
|train|9275|     9275|9275|27825|
|test|1025|     1025|1025|3075|

## Additional Information

### Dataset Curators

The dataset was initially created by Timo Möller, Julian Risch, Malte Pietsch, Julian Gutsch, Tom Hersperger, Luise Köhler, Iuliia Mozhina, and Justus Peter, during work done at deepset.ai

### Citation Information

```
@misc{möller2021germanquad,
      title={GermanQuAD and GermanDPR: Improving Non-English Question Answering and Passage Retrieval}, 
      author={Timo Möller and Julian Risch and Malte Pietsch},
      year={2021},
      eprint={2104.12741},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```