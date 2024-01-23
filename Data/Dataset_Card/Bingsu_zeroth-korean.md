---
language:
- ko
language_creators:
- crowdsourced
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: zeroth-korean
source_datasets:
- extended|kresnik/zeroth_korean
size_categories:
- 10K<n<100K
task_categories:
- automatic-speech-recognition
---
# Zeroth-Korean
## Dataset Description
- **Homepage:** [OpenSLR](https://www.openslr.org/40/)
- **Repository:** [goodatlas/zeroth](https://github.com/goodatlas/zeroth)
- **Download Size** 2.68 GiB
- **Generated Size** 2.85 GiB
- **Total Size** 5.52 GiB

## Zeroth-Korean

The data set contains transcriebed audio data for Korean. There are 51.6 hours transcribed Korean audio for training data (22,263 utterances, 105 people, 3000 sentences) and 1.2 hours transcribed Korean audio for testing data (457 utterances, 10 people). This corpus also contains pre-trained/designed language model, lexicon and morpheme-based segmenter(morfessor).
Zeroth project introduces free Korean speech corpus and aims to make Korean speech recognition more broadly accessible to everyone.
This project was developed in collaboration between Lucas Jo(@Atlas Guide Inc.) and Wonkyum Lee(@Gridspace Inc.).

Contact: Lucas Jo(lucasjo@goodatlas.com), Wonkyum Lee(wonkyum@gridspace.com)

### License

CC BY 4.0

## Dataset Structure

### Data Instance

```pycon
>>> from datasets import load_dataset
>>> dataset = load_dataset("Bingsu/zeroth-korean")
>>> dataset
DatasetDict({
    train: Dataset({
        features: ['audio', 'text'],
        num_rows: 22263
    })
    test: Dataset({
        features: ['text', 'audio'],
        num_rows: 457
    })
})
```

### Data Size

download: 2.68 GiB<br>
generated: 2.85 GiB<br>
total: 5.52 GiB

### Data Fields

- audio: `audio`, sampling rate = 16000
    - A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate.
    - Note that when accessing the audio column: `dataset[0]["audio"]` the audio file is automatically decoded and resampled to `dataset.features["audio"].sampling_rate`. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the "audio" column, i.e. `dataset[0]["audio"]` should always be preferred over `dataset["audio"][0]`.
- text: `string`

```pycon
>>> dataset["train"][0]
{'audio': {'path': None,
  'array': array([-3.0517578e-05,  0.0000000e+00, -3.0517578e-05, ...,
          0.0000000e+00,  0.0000000e+00, -6.1035156e-05], dtype=float32),
  'sampling_rate': 16000},
 'text': '인사를 결정하는 과정에서 당 지도부가 우 원내대표 및 원내지도부와 충분한 상의를 거치지 않은 채 일방적으로 인사를 했다는 불만도 원내지도부를 중심으로 흘러나왔다'}
```


### Data Splits

|            |   train  |  test |
| ---------- | -------- | ----- |
| # of data  |    22263 |   457 |
