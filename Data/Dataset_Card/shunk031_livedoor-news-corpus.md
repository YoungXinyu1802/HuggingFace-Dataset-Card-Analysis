# Dataset Card for Livedoor News Corpus

[![CI](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus/actions/workflows/ci.yaml/badge.svg)](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus/actions/workflows/ci.yaml)

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** http://www.rondhuit.com/download.html#ldcc
- **Repository:** https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus

### Dataset Summary

> 本コーパスは、NHN Japan 株式会社が運営する「livedoor ニュース」のうち、下記のクリエイティブ・コモンズライセンスが適用されるニュース記事を収集し、可能な限り HTML タグを取り除いて作成したものです。

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

```python
from datasets import load_dataset

dataset = load_dataset(
    "shunk031/livedoor-news-corpus", 
    train_ratio=0.8,
    val_ratio=0.1,
    test_ratio=0.1,
    random_state=42, 
    shuffle=True,
)

print(dataset)
# DatasetDict({
#     train: Dataset({
#         features: ['url', 'date', 'title', 'content', 'category'],
#         num_rows: 5894
#     })
#     validation: Dataset({
#         features: ['url', 'date', 'title', 'content', 'category'],
#         num_rows: 737
#     })
#     test: Dataset({
#         features: ['url', 'date', 'title', 'content', 'category'],
#         num_rows: 736
#     })
# })
```

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

> 各記事ファイルにはクリエイティブ・コモンズライセンス「表示 – 改変禁止」が適用されます。 クレジット表示についてはニュースカテゴリにより異なるため、ダウンロードしたファイルを展開したサブディレクトリにあるそれぞれの LICENSE.txt をご覧ください。 livedoor は NHN Japan 株式会社の登録商標です。

### Citation Information

[More Information Needed]

### Contributions

Thanks to [RONDHUIT Co., Ltd.](https://www.rondhuit.com/) for creating this dataset.
