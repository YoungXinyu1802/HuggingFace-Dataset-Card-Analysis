# Malay-TTS-Osman

All notebooks and code related at https://github.com/huseinzol05/malaya-speech/tree/master/data/azure-tts

## Attributes

### Wiki and News

- 24000 sample rate, super clean.
- narrator `ms-MY-OsmanNeural`.
- approximate 94.5 hours
- Texts from Malay Wikipedia and News.
- Sentences between 2 words and 20 words.

### Parliament

- 24000 sample rate, super clean.
- narrator `ms-MY-OsmanNeural`.
- approximate 133.2 hours.
- Texts from Malaysia Malay Parliament.
- Sentences between 2 words and 25 words.

## how-to

### Wiki and News

1. Download [populated-text.json](populated-text.json) and [tts-malay-osman.tar.gz](tts-malay-osman.tar.gz).

2. To get wav and transcript,

```python
import json
import soundfile as sf

with open('populated-text.json') as fopen:
    texts = json.load(fopen)

index = 0
text = texts[index]
y, sr = sf.read(f'male/{index}.wav')
```

### Parliament

1. Download [populated-parliament.json](populated-parliament.json) and [tts-malay-osman-parliament.tar.gz](tts-malay-osman-parliament.tar.gz).

2. To get wav and transcript,

```python
import json
import soundfile as sf

with open('populated-parliament.json') as fopen:
    texts = json.load(fopen)

index = 0
text = texts[index]
y, sr = sf.read(f'male-parliament/{index}.wav')
```