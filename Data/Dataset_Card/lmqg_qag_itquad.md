---
license: cc-by-sa-4.0
pretty_name: SQuAD for question generation
language: it
multilinguality: monolingual
size_categories: 1k<n<10K
source_datasets: lmqg/qg_itquad
task_categories:
- text-generation
task_ids:
- language-modeling
tags:
- question-generation
---

# Dataset Card for "lmqg/qag_itquad"


## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is the question & answer generation dataset based on the ITQuAD.

### Supported Tasks and Leaderboards
* `question-answer-generation`: The dataset is assumed to be used to train a model for question & answer generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).

### Languages
Itallian (it)

## Dataset Structure
An example of 'train' looks as follows.
```
{
  "paragraph": ""4 Minuti" è uscito come primo singolo dell' album e ha raggiunto il terzo posto sulla Billboard Hot 100. E' stato il 37° top-ten di Madonna che ha spinto Madonna oltre Elvis Presley come l' artista con i più top-ten hit. Nel Regno Unito ha mantenuto il suo record per il più numero uno single per una artista femminile;"4 Minuti" diventando il suo tredicesimo. Al 23° Japan Gold Disc Awards, Madonna ha ricevuto il suo quinto trofeo Artista dell' anno dalla Recording Industry Association of Japan, la più importante per qualsiasi artista. Per promuovere ulteriormente l' album, Madonna ha intrapreso il Sticky & Sweet Tour, la sua prima grande avventura con Live Nation. Con un lordo di 280 milioni di dollari, è diventato il tour più incassato di un artista solista, superando il precedente record di Madonna stabilito con il Confessions Tour; è stato poi superato da The Wall Live di Roger Waters. E' stato esteso al prossimo anno, aggiungendo nuove date europee, e dopo la fine, il totale lordo totale era di 408 milioni di dollari.",
  "questions": [ "Qual è il nome del primo tour con Live Nation?", "4 minuti è diventato Madonna's che numero uno nel Regno Unito?", "Quanto ha incassato Stick e Sweet Tour?", "Madonna ha superato l' artista con i più alti dieci colpi?" ],
  "answers": [ "Sticky & Sweet Tour", "tredicesimo", "280 milioni di dollari,", "Elvis Presley" ],
  "questions_answers": "question: Qual è il nome del primo tour con Live Nation?, answer: Sticky & Sweet Tour | question: 4 minuti è diventato Madonna's che numero uno nel Regno Unito?, answer: tredicesimo | question: Quanto ha incassato Stick e Sweet Tour?, answer: 280 milioni di dollari, | question: Madonna ha superato l' artista con i più alti dieci colpi?, answer: Elvis Presley"
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
|16918 |     6280  | 1988|


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