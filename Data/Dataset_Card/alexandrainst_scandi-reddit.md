---
pretty_name: ScandiReddit
language:
- da
- sv
- no
- is
license:
- cc-by-4.0
multilinguality:
- multilingual
size_categories:
- 10M<n<100M
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
---

# Dataset Card for ScandiReddit

## Dataset Description

- **Repository:** <https://github.com/alexandrainst/ScandiReddit>
- **Point of Contact:** [Dan Saattrup Nielsen](mailto:dan.nielsen@alexandra.dk)
- **Size of downloaded dataset files:** 2341 MB
- **Size of the generated dataset:** 3594 MB
- **Total amount of disk used:** 5935 MB

### Dataset Summary

ScandiReddit is a filtered and post-processed corpus consisting of comments from [Reddit](https://reddit.com/).

All Reddit comments from December 2005 up until October 2022 were downloaded through [PushShift](https://files.pushshift.io/reddit/comments/), after which these were filtered based on the FastText language detection model. Any comment which was classified as Danish (`da`), Norwegian (`no`), Swedish (`sv`) or Icelandic (`is`) with a confidence score above 70% was kept.

The resulting comments were then deduplicated, removing roughly 438,000 comments. 5,000 comments written by Reddit bots were removed, and roughly 189,000 comments belonging to inappropriate subreddits (explicit and drug-related) were also removed.

Lastly, we remove roughly 40,000 near-duplicate comments from the resulting corpus, where near-duplicate here means that the comments have more than 80% of their word 5-grams in common.


### Supported Tasks and Leaderboards

Training language models is the intended task for this dataset. No leaderboard is active at this point.


### Languages

The dataset is available in Danish (`da`), Swedish (`sv`), Norwegian (`no`) and Icelandic (`is`).


## Dataset Structure

### Data Instances

- **Size of downloaded dataset files:** 2341 MB
- **Size of the generated dataset:** 3594 MB
- **Total amount of disk used:** 5935 MB

An example from the dataset looks as follows.
```
{
    'doc': 'Bergen er ødelagt. Det er ikke moro mer.',
    'subreddit': 'Norway',
    'language': 'da',
    'language_confidence': 0.7472341656684875
}
```

### Data Fields

The data fields are the same among all splits.

- `doc`: a `string` feature.
- `subreddit`: a `string` feature.
- `language`: a `string` feature.
- `language_confidence`: a `float64` feature.

### Language Distribution

|   name   |  count   |
|----------|---------:|
| sv       | 6,967,420  |
| da       | 4,965,195  |
| no       | 1,340,470  |
| is       | 206,689    |
| total    | 13,479,774 |

### Top-50 Subreddit Distribution

|   name   |  count  |
|----------|--------:|
|sweden                  |4,881,483|
|Denmark                 |3,579,178|
|norge                   |1,281,655|
|svenskpolitik           | 771,960|
|InfluencergossipDK      | 649,910|
|swedishproblems         | 339,683|
|Iceland                 | 183,488|
|dkfinance               | 113,860|
|unket                   |  81,077|
|DanishEnts              |  69,055|
|dankmark                |  62,928|
|swedents                |  58,576|
|scandinavia             |  57,136|
|Allsvenskan             |  56,006|
|Gothenburg              |  54,395|
|stockholm               |  51,016|
|ISKbets                 |  47,944|
|Sverige                 |  39,552|
|SWARJE                  |  34,691|
|GossipDK                |  29,332|
|NorskFotball            |  28,571|
|Superligaen             |  23,641|
|Aarhus                  |  22,516|
|Svenska                 |  20,561|
|newsdk                  |  19,893|
|AskReddit               |  16,672|
|copenhagen              |  16,668|
|okpolarncp              |  16,583|
|SwedditUniversalis      |  15,990|
|Sveriges_politik        |  15,058|
|intresseklubben         |  13,246|
|Aktiemarknaden          |  13,202|
|soccer                  |  12,637|
|teenagers               |  10,845|
|Norway                  |  10,680|
|europe                  |  10,247|
|Matinbum                |   9,792|
|oslo                    |   9,650|
|iksdagen                |   9,232|
|Asksweddit              |   8,851|
|Forsvaret               |   8,641|
|Sverigesforsvarsmakt    |   8,469|
|memes                   |   8,299|
|Danish                  |   8,268|
|DANMAG                  |   8,214|
|PewdiepieSubmissions    |   7,800|
|sweddpolitik            |   7,646|
|pinsamt                 |   7,318|
|arbetarrorelsen         |   7,317|
|Ishockey                |   6,824|


## Dataset Creation

### Curation Rationale

The Scandinavian languages do not have many open source social media datasets.

### Source Data

The raw Reddit data was collected through [PushShift](https://files.pushshift.io/reddit/comments/).


## Additional Information

### Dataset Curators

[Dan Saattrup Nielsen](https://saattrupdan.github.io/) from the [The Alexandra
Institute](https://alexandra.dk/) curated this dataset.

### Licensing Information

The dataset is licensed under the [CC BY 4.0
license](https://creativecommons.org/licenses/by/4.0/).
