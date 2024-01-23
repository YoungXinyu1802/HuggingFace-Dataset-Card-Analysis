---
annotations_creators:
- other
language_creators:
- other
language:
- sk
language_bcp47:
- sk-SK
license:
- unknown
multilinguality:
- monolingual
pretty_name: stsb-sk
size_categories:
- 1K<n<10K
source_datasets:
- extended|stsb_multi_mt
task_categories:
- text-scoring
task_ids:
- semantic-similarity-scoring
---

Retrieving the 50th example from the train set:

```
> print(dataset['train']['sentence1'][0][50])
Muž hrá na gitare.

> print(dataset['train']['sentence2'][0][50])
Chlapec hrá na gitare.

> print(dataset['train']['similarity_score'][0][50])
3.200000047683716
```

For score explanation see [stsb_multi_mt](https://huggingface.co/datasets/stsb_multi_mt).
