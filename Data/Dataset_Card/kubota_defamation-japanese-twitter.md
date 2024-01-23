---
annotations_creators:
- crowdsourced
language:
- ja
language_creators:
- crowdsourced
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: defamation_japanese_twitter
size_categories:
- 1K<n<10K
source_datasets:
- original
tags: []
task_categories:
- text-classification
task_ids: []
dataset_info:
  features:
    - name: id
      dtype: string
    - name: target
      sequence: string
    - name: label
      sequence: string
    - name: user_id_list
      sequence: int32
---
# defamation_japanese_twitter
# Twitter日本語誹謗中傷検出データセット

<!-- ## Dataset Description

- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:** -->

## Dataset Summary

SNSにおける誹謗中傷検出のためのデータセットです．

5,000件の日本語のツイートに，それぞれ以下で定義している誹謗中傷の対象者と内容をアノテーションしています．アノテーションは，3人のクラウドワーカーにより行われています．2022年2月15日から2022年6月30日までのツイートです．
元のツイートは含まれていないため，Twitter APIを用いてデータセットを収集してください．


中傷対象(target)と中傷内容(label)の2項目がアノテーションされています．
- target ：テキストが話題にしている対象者の分類
- label ： targetで選択された対象者に対する誹謗中傷の種類の分類

文として成立しておらず意味の取れないものはラベルC(0)としています．

|  target  |  対象  | 例|
| ---- | ---- | ---- |
|  A1(1)  |  (人種・性別・職業・思想などを共通とする)グループ  |　(人種・性別・職業・思想などを共通とする)グループ
|  A2(2)  |  個人（著名人や知人など）  |　〇〇大統領，芸能人の〇〇さん，おまえ
|  A3(3)  |  対象がはっきりしないもの  |　
|  C(0)  |  文として成立しておらず意味が取れない |
　

|  label  |  誹謗中傷の種類  | 侵害されるもの　| 例
| ---- | ---- | ---- | ---- |
|  B1(1)  | 生命を脅かす，精神的・身体的な危害を加える  |　私生活の平穏　| • 殺害予告などの脅迫発言<br>• ◯◯なんていなくなればいいのにな
|  B2(2)  | 容姿，人格などをけなしている |　名誉感情| • 太っているくせにカッコいいと勘違いしている<br>• 田舎育ちだからファッション感覚がない
|  B3(3)  | 社会から客観的に受ける価値を低下させる |　名誉権| • ◯◯さんは過去に事件を起こして逮捕されたことがある<br>• ◯◯さんは会社の同僚と不倫をしている
|  B4(4)  | B1-B3のどれにも当てはまらず中傷性がない |　|
|  C(0)  |  文として成立しておらず意味が取れない |

## Data Fields
- `id` Twitter ID
- `target`: 3名のアノテータのカテゴリAの回答 values: C(0), A1(1), A2(2), A3(3)
- `label`: 3名のアノテータのカテゴリBの回答 values: C(0), B1(1), B2(2), B3(3), B4(4)
- `user_id_list`: 匿名化された回答者のID

## Example Using Twitter API
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kubotaissei/defamation_japanese_twitter/blob/master/notebooks/get_dataset_example.ipynb)
```python
# sample code from https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Tweet-Lookup/get_tweets_with_bearer_token.py
import requests
import os
import json
from datasets import load_dataset

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")


def create_url(ids: list):
    tweet_fields = "tweet.fields=created_at"
    ids = f"ids={','.join(ids)}"
    url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def get_text_data(examples):
    url = create_url(examples["id"])
    json_response = connect_to_endpoint(url)
    # print(json_response["data"])
    text_dict = {data["id"]: data["text"] for data in json_response["data"]}
    time_dict = {data["id"]: data["created_at"] for data in json_response["data"]}
    return {
        "text": [text_dict.get(id) for id in examples["id"]],
        "created_at": [time_dict.get(id) for id in examples["id"]],
    }


dataset = load_dataset("kubota/defamation-japanese-twitter")
dataset = dataset.map(get_text_data, batched=True, batch_size=100)
dataset["train"].to_pandas().head()

```

<!-- ## Data Splits

[More Information Needed]

## Dataset Creation

## Curation Rationale

[More Information Needed]

## Source Data

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

[More Information Needed]

### Citation Information

[More Information Needed] -->

## Contributions

Thanks to [@kubotaissei](https://github.com/kubotaissei) for adding this dataset.