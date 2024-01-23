---
license: afl-3.0
---

# ParaDetox: Detoxification with Parallel Data

This repository contains information about Russian Paradetox dataset -- the first parallel corpus for the detoxification task -- as well as models for the detoxification of Russian texts.

## ParaDetox Collection Pipeline

The ParaDetox Dataset collection was done via [Yandex.Toloka](https://toloka.yandex.com/) crowdsource platform. The collection was done in three steps:
* *Task 1:* **Generation of Paraphrases**: The first crowdsourcing task asks users to eliminate toxicity in a given sentence while keeping the content.
* *Task 2:* **Content Preservation Check**:  We show users the generated paraphrases along with their original variants and ask them to indicate if they have close meanings.
* *Task 3:* **Toxicity Check**: Finally, we check if the workers succeeded in removing toxicity.

All these steps were done to ensure high quality of the data and make the process of collection automated. For more details please refer to the original paper.

## Detoxification model
**New SOTA** for detoxification task -- BART (base) model trained on ParaDetox dataset -- we released online in HuggingFace🤗 repository [here](https://huggingface.co/s-nlp/ruT5-base-detox).

You can also check out our [demo](https://detoxifier.nlp.zhores.net/junction/) and telegram [bot](https://t.me/rudetoxifierbot).

## Citation

```
@article{dementievarusse,
  title={RUSSE-2022: Findings of the First Russian Detoxification Shared Task Based on Parallel Corpora},
  author={Dementieva, Daryna and Logacheva, Varvara and Nikishina, Irina and Fenogenova, Alena and Dale, David and Krotova, Irina and Semenov, Nikita and Shavrina, Tatiana and Panchenko, Alexander}
}
```

## Contacts

If you find some issue, do not hesitate to add it to [Github Issues](https://github.com/s-nlp/russe_detox_2022).

For any questions, please contact: Daryna Dementieva (dardem96@gmail.com)