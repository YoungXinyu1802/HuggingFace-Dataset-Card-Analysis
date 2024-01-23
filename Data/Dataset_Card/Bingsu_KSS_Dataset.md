---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- ko
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
pretty_name: Korean Single Speaker Speech Dataset
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-to-speech
task_ids: []
---

## Dataset Description

- **Homepage:** [Korean Single Speaker Speech Dataset](https://www.kaggle.com/datasets/bryanpark/korean-single-speaker-speech-dataset)
- **Repository:** [Kyubyong/kss](https://github.com/Kyubyong/kss)
- **Paper:** N/A
- **Leaderboard:** N/A
- **Point of Contact:** N/A

# Description of the original author

### KSS Dataset: Korean Single speaker Speech Dataset

KSS Dataset is designed for the Korean text-to-speech task. It consists of audio files recorded by a professional female voice actoress and their aligned text extracted from my books. As a copyright holder, by courtesy of the publishers, I release this dataset to the public. To my best knowledge, this is the first publicly available speech dataset for Korean.

### File Format

Each line in `transcript.v.1.3.txt` is delimited by `|` into six fields.
- A. Audio file path
- B. Original script
- C. Expanded script
- D. Decomposed script
- E. Audio duration (seconds)
- F. English translation

e.g.,

1/1_0470.wav|저는 보통 20분 정도 낮잠을 잡니다.|저는 보통 이십 분 정도 낮잠을 잡니다.|저는 보통 이십 분 정도 낮잠을 잡니다.|4.1|I usually take a nap for 20 minutes.

### Specification

- Audio File Type: wav
- Total Running Time: 12+ hours
- Sample Rate: 44,100 KHZ
- Number of Audio Files: 12,853
- Sources
  - |1| [Kyubyong Park, 500 Basic Korean Verbs, Tuttle Publishing, 2015.](https://www.amazon.com/500-Basic-Korean-Verbs-Comprehensive/dp/0804846057/ref=sr_1_1?s=books&ie=UTF8&qid=1522911616&sr=1-1&keywords=kyubyong+park)|
  - |2| [Kyubyong Park, 500 Basic Korean Adjectives 2nd Ed., Youkrak, 2015.](http://www.hanbooks.com/500bakoad.html)|
  - |3| [Kyubyong Park, Essential Korean Vocabulary, Tuttle Publishing, 2015.](https://www.amazon.com/Essential-Korean-Vocabulary-Phrases-Fluently/dp/0804843252/ref=sr_1_3?s=books&ie=UTF8&qid=1522911806&sr=1-3&keywords=kyubyong+park)|
  - |4| [Kyubyong Park, Tuttle Learner's Korean-English Dictionary, Tuttle Publishing, 2012.](https://www.amazon.com/Tuttle-Learners-Korean-English-Dictionary-Essential/dp/0804841500/ref=sr_1_8?s=books&ie=UTF8&qid=1522911806&sr=1-8&keywords=kyubyong+park)|
  
### License

NC-SA 4.0. You CANNOT use this dataset for ANY COMMERCIAL purpose. Otherwise, you can freely use this.

### Citation

If you want to cite KSS Dataset, please refer to this:

Kyubyong Park, KSS Dataset: Korean Single speaker Speech Dataset, https://kaggle.com/bryanpark/korean-single-speaker-speech-dataset, 2018

### Reference

Check out [this](https://github.com/Kyubyong/kss) for a project using this KSS Dataset.

### Contact

You can contact me at kbpark.linguist@gmail.com.

April, 2018.

Kyubyong Park

### Dataset Summary

12,853 Korean audio files with transcription.

### Supported Tasks and Leaderboards

text-to-speech

### Languages

korean

## Dataset Structure

### Data Instances

```python
>>> from datasets import load_dataset

>>> dataset = load_dataset("Bingsu/KSS_Dataset")
>>> dataset["train"].features
{'audio': Audio(sampling_rate=44100, mono=True, decode=True, id=None),
 'original_script': Value(dtype='string', id=None),
 'expanded_script': Value(dtype='string', id=None),
 'decomposed_script': Value(dtype='string', id=None),
 'duration': Value(dtype='float32', id=None),
 'english_translation': Value(dtype='string', id=None)}
```
```python
>>> dataset["train"][0]
{'audio': {'path': None,
  'array': array([ 0.00000000e+00,  3.05175781e-05, -4.57763672e-05, ...,
          0.00000000e+00, -3.05175781e-05, -3.05175781e-05]),
  'sampling_rate': 44100},
 'original_script': '그는 괜찮은 척하려고 애쓰는 것 같았다.',
 'expanded_script': '그는 괜찮은 척하려고 애쓰는 것 같았다.',
 'decomposed_script': '그는 괜찮은 척하려고 애쓰는 것 같았다.',
 'duration': 3.5,
 'english_translation': 'He seemed to be pretending to be okay.'}
```
### Data Splits

|               | train |
|---------------|------:|
| # of examples | 12853 |