# ❤️‍🩹 Sensai: Toxic Chat Dataset

Sensai is a toxic chat dataset consists of live chats from Virtual YouTubers' live streams.

Download the dataset from [Kaggle Datasets](https://www.kaggle.com/uetchy/sensai) and join `#livechat-dataset` channel on [holodata Discord](https://holodata.org/discord) for discussions.

## Provenance

- **Source:** YouTube Live Chat events (all streams covered by [Holodex](https://holodex.net), including Hololive, Nijisanji, 774inc, etc)
- **Temporal Coverage:** From 2021-01-15T05:15:33Z
- **Update Frequency:** At least once per month

## Research Ideas

- Toxic Chat Classification
- Spam Detection
- Sentence Transformer for Live Chats

See [public notebooks](https://www.kaggle.com/uetchy/sensai/code) for ideas.

## Files

| filename                  | summary                                                        | size     |
| ------------------------- | -------------------------------------------------------------- | -------- |
| `chats_flagged_%Y-%m.csv` | Chats flagged as either deleted or banned by mods (3,100,000+) | ~ 400 MB |
| `chats_nonflag_%Y-%m.csv` | Non-flagged chats (3,100,000+)                                 | ~ 300 MB |

To make it a balanced dataset, the number of `chats_nonflags` is adjusted (randomly sampled) to be the same as `chats_flagged`.
Ban and deletion are equivalent to `markChatItemsByAuthorAsDeletedAction` and `markChatItemAsDeletedAction` respectively.

## Dataset Breakdown

### Chats (`chats_%Y-%m.csv`)

| column          | type   | description                  |
| --------------- | ------ | ---------------------------- |
| body            | string | chat message                 |
| membership      | string | membership status            |
| authorChannelId | string | anonymized author channel id |
| channelId       | string | source channel id            |

#### Membership status

| value             | duration                  |
| ----------------- | ------------------------- |
| unknown           | Indistinguishable         |
| non-member        | 0                         |
| less than 1 month | < 1 month                 |
| 1 month           | >= 1 month, < 2 months    |
| 2 months          | >= 2 months, < 6 months   |
| 6 months          | >= 6 months, < 12 months  |
| 1 year            | >= 12 months, < 24 months |
| 2 years           | >= 24 months              |

#### Pandas usage

Set `keep_default_na` to `False` and `na_values` to `''` in `read_csv`. Otherwise, chat message like `NA` would incorrectly be treated as NaN value.

```python
import pandas as pd
from glob import iglob

flagged = pd.concat([
    pd.read_csv(f,
                na_values='',
                keep_default_na=False)
    for f in iglob('../input/sensai/chats_flagged_*.csv')
],
               ignore_index=True)
```

## Consideration

### Anonymization

`authorChannelId` are anonymized by SHA-1 hashing algorithm with a pinch of undisclosed salt.

### Handling Custom Emojis

All custom emojis are replaced with a Unicode replacement character `U+FFFD`.

## Citation

```latex
@misc{sensai-dataset,
 author={Yasuaki Uechi},
 title={Sensai: Toxic Chat Dataset},
 year={2021},
 month={8},
 version={31},
 url={https://github.com/holodata/sensai-dataset}
}
```

## License

- Code: [MIT License](https://github.com/holodata/sensai-dataset/blob/master/LICENSE)
- Dataset: [ODC Public Domain Dedication and Licence (PDDL)](https://opendatacommons.org/licenses/pddl/1-0/index.html)
