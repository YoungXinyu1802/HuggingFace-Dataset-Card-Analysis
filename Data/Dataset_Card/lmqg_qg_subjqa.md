---
license: cc-by-4.0
pretty_name: SubjQA for question generation
language: en
multilinguality: monolingual
size_categories: 10K<n<100K
source_datasets: subjqa
task_categories:
- text-generation
task_ids:
- language-modeling
tags:
- question-generation
---

# Dataset Card for "lmqg/qg_subjqa"

## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is a subset of [QG-Bench](https://github.com/asahi417/lm-question-generation/blob/master/QG_BENCH.md#datasets), a unified question generation benchmark proposed in
 ["Generative Language Models for Paragraph-Level Question Generation: A Unified Benchmark and Evaluation, EMNLP 2022 main conference"](https://arxiv.org/abs/2210.03992).
Modified version of [SubjQA](https://github.com/megagonlabs/SubjQA) for question generation (QG) task.

### Supported Tasks and Leaderboards
* `question-generation`: The dataset can be used to train a model for question generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).

### Languages
English (en)

## Dataset Structure
An example of 'train' looks as follows.
```
{
  "question": "How is book?",
  "paragraph": "I am giving "Gone Girl" 3 stars, but only begrudgingly. In my mind, any book that takes me 3 months and 20 different tries to read is not worth 3 stars, especially a book written by an author I already respect. And I am not kidding, for me the first half of "Gone Girl" was a PURE TORTURE to read.Amy Dunn disappears on the day of her 5th wedding anniversary. All gradually uncovered evidence suggests that her husband, Nick, is somehow involved. Did he kill her? Was she kidnapped? What happened to Amy? One thing is clear, Nick and Amy's marriage wasn't as perfect as everybody thought.The first part of the novel is all about the investigation into Amy's disappearance, slow unraveling of Nick's dirty secrets, reminiscing about the troubled history of Nick and Amy's marriage as told in Amy's hidden diary. I strained and strained my brain trying to understand why this chunk of Gone Girl had no appeal to me whatsoever. The only answer I have is this: I am really not into reading about rich white people's problems. You want to whine to me about your dwindling trust fund? Losing your cushy New York job? Moving south and "only" renting a mansion there? Being unhappy because you have too much free time on your hands and you are used to only work as a hobby? You want to make fun of your lowly, un-posh neighbors and their casseroles? Well, I am not interested. I'd rather read about someone not necessarily likable, but at least worthy of my empathy, not waste my time on self-centered, spoiled, pathetic people who don't know what real problems are. Granted, characters in Flynn's previous novels ("Sharp Objects" and "Dark Places") are pretty pathetic and and at times revolting too, but I always felt some strange empathy towards them, not annoyance and boredom, like I felt reading about Amy and Nick's marriage voes.But then second part, with its wicked twist, changed everything. The story became much more exciting, dangerous and deranged. The main characters revealed sides to them that were quite shocking and VERY entertaining. I thought the Gillian Flynn I knew before finally unleashed her talent for writing utterly unlikable and crafty women. THEN I got invested in the story, THEN I cared.Was it too little too late though? I think it was. Something needed to be done to make "Gone Girl" a better read. Make it shorter? Cut out first part completely? I don't know. But because of my uneven experience with this novel I won't be able to recommend "Gone Girl" as readily as I did Flynn's earlier novels, even though I think this horror marriage story (it's not a true mystery, IMO) has some brilliantly written psycho goodness in it and an absolutely messed up ending that many loathed but I LOVED. I wish it didn't take so much time and patience to get to all of that...",
  "answer": "any book that takes me 3 months and 20 different tries to read is not worth 3 stars",
  "sentence": "In my mind, any book that takes me 3 months and 20 different tries to read is not worth 3 stars , especially a book written by an author I already respect.",
  "paragraph_sentence": "I am giving "Gone Girl" 3 stars, but only begrudgingly. <hl> In my mind, any book that takes me 3 months and 20 different tries to read is not worth 3 stars , especially a book written by an author I already respect. <hl> And I am not kidding, for me the first half of "Gone Girl" was a PURE TORTURE to read. Amy Dunn disappears on the day of her 5th wedding anniversary. All gradually uncovered evidence suggests that her husband, Nick, is somehow involved. Did he kill her? Was she kidnapped? What happened to Amy? One thing is clear, Nick and Amy's marriage wasn't as perfect as everybody thought. The first part of the novel is all about the investigation into Amy's disappearance, slow unraveling of Nick's dirty secrets, reminiscing about the troubled history of Nick and Amy's marriage as told in Amy's hidden diary. I strained and strained my brain trying to understand why this chunk of Gone Girl had no appeal to me whatsoever. The only answer I have is this: I am really not into reading about rich white people's problems. You want to whine to me about your dwindling trust fund? Losing your cushy New York job? Moving south and "only" renting a mansion there? Being unhappy because you have too much free time on your hands and you are used to only work as a hobby? You want to make fun of your lowly, un-posh neighbors and their casseroles? Well, I am not interested. I'd rather read about someone not necessarily likable, but at least worthy of my empathy, not waste my time on self-centered, spoiled, pathetic people who don't know what real problems are. Granted, characters in Flynn's previous novels ("Sharp Objects" and "Dark Places") are pretty pathetic and and at times revolting too, but I always felt some strange empathy towards them, not annoyance and boredom, like I felt reading about Amy and Nick's marriage voes. But then second part, with its wicked twist, changed everything. The story became much more exciting, dangerous and deranged. The main characters revealed sides to them that were quite shocking and VERY entertaining. I thought the Gillian Flynn I knew before finally unleashed her talent for writing utterly unlikable and crafty women. THEN I got invested in the story, THEN I cared. Was it too little too late though? I think it was. Something needed to be done to make "Gone Girl" a better read. Make it shorter? Cut out first part completely? I don't know. But because of my uneven experience with this novel I won't be able to recommend "Gone Girl" as readily as I did Flynn's earlier novels, even though I think this horror marriage story (it's not a true mystery, IMO) has some brilliantly written psycho goodness in it and an absolutely messed up ending that many loathed but I LOVED. I wish it didn't take so much time and patience to get to all of that...",
  "paragraph_answer": "I am giving "Gone Girl" 3 stars, but only begrudgingly. In my mind, <hl> any book that takes me 3 months and 20 different tries to read is not worth 3 stars <hl>, especially a book written by an author I already respect. And I am not kidding, for me the first half of "Gone Girl" was a PURE TORTURE to read.Amy Dunn disappears on the day of her 5th wedding anniversary. All gradually uncovered evidence suggests that her husband, Nick, is somehow involved. Did he kill her? Was she kidnapped? What happened to Amy? One thing is clear, Nick and Amy's marriage wasn't as perfect as everybody thought.The first part of the novel is all about the investigation into Amy's disappearance, slow unraveling of Nick's dirty secrets, reminiscing about the troubled history of Nick and Amy's marriage as told in Amy's hidden diary. I strained and strained my brain trying to understand why this chunk of Gone Girl had no appeal to me whatsoever. The only answer I have is this: I am really not into reading about rich white people's problems. You want to whine to me about your dwindling trust fund? Losing your cushy New York job? Moving south and "only" renting a mansion there? Being unhappy because you have too much free time on your hands and you are used to only work as a hobby? You want to make fun of your lowly, un-posh neighbors and their casseroles? Well, I am not interested. I'd rather read about someone not necessarily likable, but at least worthy of my empathy, not waste my time on self-centered, spoiled, pathetic people who don't know what real problems are. Granted, characters in Flynn's previous novels ("Sharp Objects" and "Dark Places") are pretty pathetic and and at times revolting too, but I always felt some strange empathy towards them, not annoyance and boredom, like I felt reading about Amy and Nick's marriage voes.But then second part, with its wicked twist, changed everything. The story became much more exciting, dangerous and deranged. The main characters revealed sides to them that were quite shocking and VERY entertaining. I thought the Gillian Flynn I knew before finally unleashed her talent for writing utterly unlikable and crafty women. THEN I got invested in the story, THEN I cared.Was it too little too late though? I think it was. Something needed to be done to make "Gone Girl" a better read. Make it shorter? Cut out first part completely? I don't know. But because of my uneven experience with this novel I won't be able to recommend "Gone Girl" as readily as I did Flynn's earlier novels, even though I think this horror marriage story (it's not a true mystery, IMO) has some brilliantly written psycho goodness in it and an absolutely messed up ending that many loathed but I LOVED. I wish it didn't take so much time and patience to get to all of that...",
  "sentence_answer": "In my mind, <hl> any book that takes me 3 months and 20 different tries to read is not worth 3 stars <hl> , especially a book written by an author I already respect.",
  "paragraph_id": "1b7cc3db9ec681edd253a41a2785b5a9",
  "question_subj_level": 1,
  "answer_subj_level": 1,
  "domain": "books"
}
```

The data fields are the same among all splits.
- `question`: a `string` feature. 
- `paragraph`: a `string` feature.
- `answer`: a `string` feature.
- `sentence`: a `string` feature.
- `paragraph_answer`: a `string` feature, which is same as the paragraph but the answer is highlighted by a special token `<hl>`.
- `paragraph_sentence`: a `string` feature, which is same as the paragraph but a sentence containing the answer is highlighted by a special token `<hl>`.
- `sentence_answer`: a `string` feature, which is same as the sentence but the answer is highlighted by a special token `<hl>`.

Each of `paragraph_answer`, `paragraph_sentence`, and `sentence_answer` feature is assumed to be used to train a question generation model,
but with different information. The `paragraph_answer` and `sentence_answer` features are for answer-aware question generation and 
`paragraph_sentence` feature is for sentence-aware question generation.

### Data Splits

|   name      |train|validation|test |
|-------------|----:|---------:|----:|
|default (all)|4437 |     659  |1489 |
| books       |636  |     91   |190  |
| electronics |696  |     98   |237  |
| movies      |723  |     100  |153  |
| grocery     |686  |     100  |378  |
| restaurants |822  |     128  |135  |
| tripadvisor |874  |     142  |396  |

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