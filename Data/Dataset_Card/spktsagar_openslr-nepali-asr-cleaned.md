---
license: cc-by-sa-4.0
dataset_info:
- config_name: original
  features:
  - name: utterance_id
    dtype: string
  - name: speaker_id
    dtype: string
  - name: utterance
    dtype:
      audio:
        sampling_rate: 16000
  - name: transcription
    dtype: string
  - name: num_frames
    dtype: int32
  splits:
  - name: train
    num_bytes: 40925646
    num_examples: 157905
  download_size: 9340083067
  dataset_size: 40925646
- config_name: cleaned
  features:
  - name: utterance_id
    dtype: string
  - name: speaker_id
    dtype: string
  - name: utterance
    dtype:
      audio:
        sampling_rate: 16000
  - name: transcription
    dtype: string
  - name: num_frames
    dtype: int32
  splits:
  - name: train
    num_bytes: 40925646
    num_examples: 157905
  download_size: 5978669282
  dataset_size: 40925646
---

# Dataset Card for OpenSLR Nepali Large ASR Cleaned

## Table of Contents
- [Dataset Card for OpenSLR Nepali Large ASR Cleaned](#dataset-card-for-openslr-nepali-large-asr-cleaned)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [How to use?](#how-to-use)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  

## Dataset Description

- **Homepage:** [Original OpenSLR Large Nepali ASR Dataset link](https://www.openslr.org/54/)
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Sagar Sapkota](mailto:spkt.sagar@gmail.com)

### Dataset Summary

This data set contains transcribed audio data for Nepali. The data set consists of flac files, and a TSV file. The file utt_spk_text.tsv contains a FileID, anonymized UserID and the transcription of audio in the file.
The data set has been manually quality-checked, but there might still be errors.

The audio files are sampled at a rate of 16KHz, and leading and trailing silences are trimmed using torchaudio's voice activity detection.

For your reference, following was the function applied on each of the original openslr utterances.
```python
import torchaudio

SAMPLING_RATE = 16000

def process_audio_file(orig_path, new_path):
    """Read and process file in `orig_path` and save it to `new_path`"""
    waveform, sampling_rate = torchaudio.load(orig_path)
    if sampling_rate != SAMPLING_RATE:
        waveform = torchaudio.functional.resample(waveform, sampling_rate, SAMPLING_RATE)
    #  trim end silences with Voice Activity Detection
    waveform = torchaudio.functional.vad(waveform, sample_rate=SAMPLING_RATE)
    torchaudio.save(new_path, waveform, sample_rate=SAMPLING_RATE)
```

### How to use?

There are two configurations for the data: one to download the original data and the other to download the preprocessed data as described above.
1. First, to download the original dataset with HuggingFace's [Dataset](https://huggingface.co/docs/datasets/) API:
```python
from datasets import load_dataset

dataset = load_dataset("spktsagar/openslr-nepali-asr-cleaned", name="original", split='train')
```

2. To download the preprocessed dataset:
```python
from datasets import load_dataset

dataset = load_dataset("spktsagar/openslr-nepali-asr-cleaned", name="cleaned", split='train')
```

### Supported Tasks and Leaderboards

- `automatic-speech-recognition`: The dataset can be used to train a model for Automatic Speech Recognition. 

### Languages

Nepali

## Dataset Structure

### Data Instances

```js
{
    'utterance_id': 'e1c4d414df',
    'speaker_id': '09da0',
    'utterance': {
        'path': '/root/.cache/huggingface/datasets/downloads/extracted/e3cf9a618900289ecfd4a65356633d7438317f71c500cbed122960ab908e1e8a/cleaned/asr_nepali/data/e1/e1c4d414df.flac',
        'array': array([-0.00192261, -0.00204468, -0.00158691, ...,  0.00323486, 0.00256348,  0.00262451], dtype=float32),
        'sampling_rate': 16000
    },
    'transcription': '२००५ मा बिते',
    'num_frames': 42300
}
```

### Data Fields

- utterance_id: a string identifying the utterances
- speaker_id: obfuscated unique id of the speaker whose utterances is in the current instance
- utterance:
    - path: path to the utterance .flac file
    - array: numpy array of the utterance
    - sampling_rate: sample rate of the utterance
- transcription: Nepali text which spoken in the utterance
- num_frames: length of waveform array

### Data Splits

The dataset is not split. The consumer should split it as per their requirements.