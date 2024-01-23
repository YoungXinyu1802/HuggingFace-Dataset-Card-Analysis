---
dataset_info:
  features:
  - name: label
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 74489242
    num_examples: 478389
  - name: test
    num_bytes: 12922409
    num_examples: 81957
  download_size: 56815784
  dataset_size: 87411651
---
# Dataset Card for "kaggle-mbti-cleaned-augmented"
This dataset is built upon [Shunian/kaggle-mbti-cleaned](https://huggingface.co/datasets/Shunian/kaggle-mbti-cleaned) to address the sample imbalance problem.

Thanks to the [Parrot Paraphraser](https://github.com/PrithivirajDamodaran/Parrot_Paraphraser) and [NLP AUG](https://github.com/makcedward/nlpaug), some of the skewness issue are addressed in the training data, make it grows from 328,660 samples to 478,389 samples in total.

View [GitHub](https://github.com/nogibjj/MBTI-Personality-Test) for more information