---
task_categories:
- conditional-text-generation

---
# AutoTrain Dataset for project: dippatel_summarizer

## Dataset Description

This dataset has been automatically processed by AutoTrain for project dippatel_summarizer.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "feat_id": "13864393",
    "text": "Peter: So have you gone to see the wedding?\nHolly: of course, it was so exciting\nRuby: I really don't understand what's so exciting about it\nAngela: me neither\nHolly: because it's the first person of colour in any Western royal family\nRuby: is she?\nPeter: it's not true\nHolly: no?\nPeter: there is a princess in Liechtenstein\nPeter: I think a few years ago a prince of Liechtenstein married a woman from Africa\nPeter: and it was the first case of this kind among European ruling dynasties\nHolly: what? I've never heard of it\nPeter: wait, I'll google it\nRuby: interesting\nPeter: here: <file_other>\nPeter: Princess Angela von Liechtenstein, born Angela Gisela Brown\nPeter: sorry, she's from Panama, but anyway of African descent\nRuby: right! but who cares about Liechtenstein?!\nPeter: lol, I just noticed that it's not true, what you wrote\nRuby: I'm excited anyway, she's the first in the UK for sure",
    "target": "Holly went to see the royal wedding. Prince of Liechtenstein married a Panamanian woman of African descent."
  },
  {
    "feat_id": "13716378",
    "text": "Max: I'm so sorry Lucas. I don't know what got into me.\nLucas: .......\nLucas: I don't know either.\nMason: that was really fucked up Max\nMax: I know. I'm so sorry :(.\nLucas: I don't know, man.\nMason: what were you thinking??\nMax: I wasn't.\nMason: yea\nMax: Can we please meet and talk this through? Please.\nLucas: Ok. I'll think about it and let you know.\nMax: Thanks...",
    "target": "Max is sorry about his behaviour so wants to meet up with Lucas and Mason. Lucas will let him know. "
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "feat_id": "Value(dtype='string', id=None)",
  "text": "Value(dtype='string', id=None)",
  "target": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 2400 |
| valid        | 600 |
