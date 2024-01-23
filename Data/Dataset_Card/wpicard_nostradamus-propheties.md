---
annotations_creators:
- no-annotation
language_creators: []
language:
- en
language_bcp47:
- en-US
license:
- unknown
multilinguality:
- monolingual
pretty_name: nostradamus-propheties
size_categories:
- unknown
source_datasets: []
task_categories:
- sequence-modeling
task_ids:
- language-modeling
---
# Dataset Card for "nostradamus-propheties"

## Dataset Description

### Dataset Summary

The Nostradamus propheties dataset is a set of structured files containing the "Propheties" by Nostradamus, translated in modern English.

The original text consists of 10 "Centuries", every century containing 100 numbered quatrains.

In the dataset, every century is a separate file named `century**.json`. For instance, all the quatrains of Century I are in the file `century01.json`.

The century and the quantrain number are kept for every quatrain. Every quatrain has been split in four separate lines. For example, the second quatrain of Century I is stored in `century01.json` as follows:
```
{
  "century":1,
  "index":2,
  "line1":"The wand in the hand is placed in the middle of the tripod's legs.",
  "line2":"With water he sprinkles both the hem of his garment and his foot.",
  "line3":"A voice, fear: he trembles in his robes.",
  "line4":"Divine splendor; the God sits nearby."
}
```


