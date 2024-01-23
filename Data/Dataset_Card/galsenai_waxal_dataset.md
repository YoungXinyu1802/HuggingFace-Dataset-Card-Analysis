---
license: creativeml-openrail-m
dataset_info:
  features:
  - name: audio
    dtype: audio
  - name: label
    dtype:
      class_label:
        names:
          '0': A canoon
          '1': A cinj
          '2': A keen
          '3': A lanq
          '4': A ñaaƴ
          '5': A ñamaak
          '6': Alaa
          '7': Bacaac
          '8': Benn
          '9': Bálamuk
          '10': Búbaar
          '11': Caggal
          '12': Ceme
          '13': Ci ginnaaw
          '14': Ci kanam
          '15': Ci kow
          '16': Ci suuf
          '17': Càmmoñ
          '18': Darnde
          '19': Dow
          '20': Doxal
          '21': Déedet
          '22': Eey
          '23': Esuwa
          '24': Eyen
          '25': Eé
          '26': Fatiya
          '27': Fukk
          '28': Funoom
          '29': Futok
          '30': Futok di sibaakiir
          '31': Futok di sigaba
          '32': Futok di sífeejir
          '33': Futok di yákon
          '34': Fácul
          '35': Garab
          '36': Goo
          '37': Hani
          '38': Jaay
          '39': Jeegom
          '40': Jeenay
          '41': Jeetati
          '42': Jeeɗiɗi
          '43': Jik
          '44': Jiku
          '45': Joy
          '46': Juni
          '47': Junne
          '48': Juroom
          '49': Juroom-benn
          '50': Juroom-ñaar
          '51': Juroom-ñeent
          '52': Juroom-ñett
          '53': Jënd
          '54': Kakamben
          '55': Kamay
          '56': Kanoomen
          '57': Kákambul
          '58': Kárir
          '59': Lal
          '60': Lees
          '61': Leng
          '62': Leɗki
          '63': Li
          '64': Mbaamir
          '65': Mbalndi
          '66': Nano
          '67': Naxik
          '68': Nay
          '69': Ndaxar
          '70': Ndeyjoor
          '71': Ndiga
          '72': Ndiiƭ
          '73': Njong
          '74': O ɓox
          '75': Picc
          '76': Rawaandu
          '77': Sappo
          '78': Sibaakiir
          '79': Sigaba
          '80': Solndu
          '81': Soodde
          '82': Sífeejir
          '83': Tadik
          '84': Tati
          '85': Taxawal
          '86': Teemedere
          '87': Teemeed
          '88': Tentaam
          '89': Tik
          '90': Took
          '91': Tus
          '92': Téemeer
          '93': Ub /Tëj
          '94': Ub/Tëj
          '95': Ubbi /Tijji
          '96': Udditde
          '97': Uddude
          '98': Ujaw
          '99': Ujunere
          '100': Ujuum
          '101': Uñen
          '102': Waafulet
          '103': Waaw
          '104': Weg
          '105': Wet
          '106': Wúli
          '107': Xa-aa
          '108': Xaj
          '109': Xarɓaxay
          '110': Yahdu
          '111': Yeeso
          '112': Yeeyde
          '113': Yákon
          '114': Ñaamo
          '115': Ñaar
          '116': Ñeent
          '117': Ñett
          '118': Ɗiɗi
          '119': Ƥetaa-fo-leng
          '120': Ƥetaa-naxak
          '121': Ƥetaa-tadak
          '122': Ƥetaa-ƭaq
          '123': Ƥetik
  - name: translation
    dtype: string
  - name: locale_id
    dtype: int64
  - name: transcript
    dtype: string
  splits:
  - name: train
    num_bytes: 567773923.639
    num_examples: 26387
  download_size: 546144081
  dataset_size: 567773923.639
---

### Dataset Summary

Keyword spotting refers to the task of learning to detect spoken keywords. It interfaces all modern voice-based virtual assistants on the market: Amazon’s Alexa, Apple’s Siri, and the Google Home device. Contrarily to speech recognition models, keyword spotting doesn’t run on the cloud, but directly on the device. 

The motivation of this paper is to extend the Speech commands dataset (Warden 2018) with African languages. In particular, we are going to focus on 4 Senegalese languages: Wolof, Pulaar, Serer, Diola. 

The choice of these languages is guided, on the one hand, by their status as languages considered to be the languages of the first generation, that is to say, the first codified languages (endowed with a writing system and considered by the state of Senegal as national languages) with decree n ° 68-871 of July 24, 1968. On the other hand, they represent the languages that are most spoken in Senegal.

### Languages
The ID of the languages are the following:
- Wolof: `7`
- Pulaar: `5`
- Serer: `6`
- Diola: `3`




## Dataset Structure

```python
from datasets import load_dataset
dataset = load_dataset("galsenai/waxal_dataset")
DatasetDict({
    train: Dataset({
        features: ['audio', 'label', 'translation', 'locale_id'],
        num_rows: 26387
    })
})
```

### Data Fields

- `audio`: Audio file in MP3 format
- `label`: label of the audio file
- `translation` : Translation of the keyword in french
- `locale_id`: ID of the language