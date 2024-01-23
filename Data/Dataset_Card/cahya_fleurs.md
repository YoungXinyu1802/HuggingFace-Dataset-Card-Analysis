---
annotations_creators:
- expert-generated
- crowdsourced
- machine-generated
language_creators:
- crowdsourced
- expert-generated
language:
- afr
- amh
- ara
- asm
- ast
- azj
- bel
- ben
- bos
- cat
- ceb
- cmn
- ces
- cym
- dan
- deu
- ell
- eng
- spa
- est
- fas
- ful
- fin
- tgl
- fra
- gle
- glg
- guj
- hau
- heb
- hin
- hrv
- hun
- hye
- ind
- ibo
- isl
- ita
- jpn
- jav
- kat
- kam
- kea
- kaz
- khm
- kan
- kor
- ckb
- kir
- ltz
- lug
- lin
- lao
- lit
- luo
- lav
- mri
- mkd
- mal
- mon
- mar
- msa
- mlt
- mya
- nob
- npi
- nld
- nso
- nya
- oci
- orm
- ory
- pan
- pol
- pus
- por
- ron
- rus
- bul
- snd
- slk
- slv
- sna
- som
- srp
- swe
- swh
- tam
- tel
- tgk
- tha
- tur
- ukr
- umb
- urd
- uzb
- vie
- wol
- xho
- yor
- yue
- zul
license:
- cc-by-4.0
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
task_categories:
- automatic-speech-recognition
task_ids: []
pretty_name: 'The Cross-lingual TRansfer Evaluation of Multilingual Encoders for Speech
  (XTREME-S) benchmark is a benchmark designed to evaluate speech representations
  across languages, tasks, domains and data regimes. It covers 102 languages from
  10+ language families, 3 different domains and 4 task families: speech recognition,
  translation, classification and retrieval.'
tags:
- speech-recognition
---

# FLEURS

## Dataset Description

- **Fine-Tuning script:** [pytorch/speech-recognition](https://github.com/huggingface/transformers/tree/main/examples/pytorch/speech-recognition)
- **Paper:** [FLEURS: Few-shot Learning Evaluation of
Universal Representations of Speech](https://arxiv.org/abs/2205.12446)
- **Total amount of disk used:** ca. 350 GB

Fleurs is the speech version of the [FLoRes machine translation benchmark](https://arxiv.org/abs/2106.03193). 
We use 2009 n-way parallel sentences from the FLoRes dev and devtest publicly available sets, in 102 languages. 

Training sets have around 10 hours of supervision. Speakers of the train sets are different than speakers from the dev/test sets. Multilingual fine-tuning is
used and ”unit error rate” (characters, signs) of all languages is averaged. Languages and results are also grouped into seven geographical areas: 

- **Western Europe**: *Asturian, Bosnian, Catalan, Croatian, Danish, Dutch, English, Finnish, French, Galician, German, Greek, Hungarian, Icelandic, Irish, Italian, Kabuverdianu, Luxembourgish, Maltese, Norwegian, Occitan, Portuguese, Spanish, Swedish, Welsh* 
- **Eastern Europe**: *Armenian, Belarusian, Bulgarian, Czech, Estonian, Georgian, Latvian, Lithuanian, Macedonian, Polish, Romanian, Russian, Serbian, Slovak, Slovenian, Ukrainian*
- **Central-Asia/Middle-East/North-Africa**: *Arabic, Azerbaijani, Hebrew, Kazakh, Kyrgyz, Mongolian, Pashto, Persian, Sorani-Kurdish, Tajik, Turkish, Uzbek*
- **Sub-Saharan Africa**: *Afrikaans, Amharic, Fula, Ganda, Hausa, Igbo, Kamba, Lingala, Luo, Northern-Sotho, Nyanja, Oromo, Shona, Somali, Swahili, Umbundu, Wolof, Xhosa, Yoruba, Zulu*
- **South-Asia**: *Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Nepali, Oriya, Punjabi, Sindhi, Tamil, Telugu, Urdu*
- **South-East Asia**: *Burmese, Cebuano, Filipino, Indonesian, Javanese, Khmer, Lao, Malay, Maori, Thai, Vietnamese*
- **CJK languages**: *Cantonese and Mandarin Chinese, Japanese, Korean*


## Supported Tasks

### 1. Speech Recognition (ASR)

```py
from datasets import load_dataset

fleurs_asr = load_dataset("google/fleurs", "af_za")  # for Afrikaans
# to download all data for multi-lingual fine-tuning uncomment following line
# fleurs_asr = load_dataset("google/fleurs", "all")

# see structure
print(fleurs_asr)

# load audio sample on the fly
audio_input = fleurs_asr["train"][0]["audio"]  # first decoded audio sample
transcription = fleurs_asr["train"][0]["transcription"]  # first transcription
# use `audio_input` and `transcription` to fine-tune your model for ASR

# for analyses see language groups
all_language_groups = fleurs_asr["train"].features["lang_group_id"].names
lang_group_id = fleurs_asr["train"][0]["lang_group_id"]

all_language_groups[lang_group_id]
```

### 2. Language Identification

LangID can often be a domain classification, but in the case of FLEURS-LangID, recordings are done in a similar setting across languages and the utterances correspond to n-way parallel sentences, in the exact same domain, making this task particularly relevant for evaluating LangID. The setting is simple, FLEURS-LangID is splitted in train/valid/test for each language. We simply create a single train/valid/test for LangID by merging all.

```py
from datasets import load_dataset

fleurs_langID = load_dataset("google/fleurs", "all") # to download all data

# see structure
print(fleurs_langID)

# load audio sample on the fly
audio_input = fleurs_langID["train"][0]["audio"]  # first decoded audio sample
language_class = fleurs_langID["train"][0]["lang_id"]  # first id class
language = fleurs_langID["train"].features["lang_id"].names[language_class]

# use audio_input and language_class to fine-tune your model for audio classification
```

### 3. Retrieval

Retrieval provides n-way parallel speech and text data. Similar to how XTREME for text leverages Tatoeba to evaluate bitext mining a.k.a sentence translation retrieval, we use Retrieval to evaluate the quality of fixed-size representations of speech utterances. Our goal is to incentivize the creation of fixed-size speech encoder for speech retrieval. The system has to retrieve the English "key" utterance corresponding to the speech translation of "queries" in 15 languages. Results have to be reported on the test sets of Retrieval whose utterances are used as queries (and keys for English). We augment the English keys with a large number of utterances to make the task more difficult.

```py
from datasets import load_dataset

fleurs_retrieval = load_dataset("google/fleurs", "af_za")  # for Afrikaans
# to download all data for multi-lingual fine-tuning uncomment following line
# fleurs_retrieval = load_dataset("google/fleurs", "all")

# see structure
print(fleurs_retrieval)

# load audio sample on the fly
audio_input = fleurs_retrieval["train"][0]["audio"]  # decoded audio sample
text_sample_pos = fleurs_retrieval["train"][0]["transcription"]  # positive text sample
text_sample_neg = fleurs_retrieval["train"][1:20]["transcription"] # negative text samples

# use `audio_input`, `text_sample_pos`, and `text_sample_neg` to fine-tune your model for retrieval
```

Users can leverage the training (and dev) sets of FLEURS-Retrieval with a ranking loss to build better cross-lingual fixed-size representations of speech.

## Dataset Structure

We show detailed information the example configurations `af_za` of the dataset.
All other configurations have the same structure.

### Data Instances

**af_za**
- Size of downloaded dataset files: 1.47 GB
- Size of the generated dataset: 1 MB
- Total amount of disk used: 1.47 GB

An example of a data instance of the config `af_za` looks as follows:

```
{'id': 91,
 'num_samples': 385920,
 'path': '/home/patrick/.cache/huggingface/datasets/downloads/extracted/310a663d52322700b3d3473cbc5af429bd92a23f9bc683594e70bc31232db39e/home/vaxelrod/FLEURS/oss2_obfuscated/af_za/audio/train/17797742076841560615.wav',
 'audio': {'path': '/home/patrick/.cache/huggingface/datasets/downloads/extracted/310a663d52322700b3d3473cbc5af429bd92a23f9bc683594e70bc31232db39e/home/vaxelrod/FLEURS/oss2_obfuscated/af_za/audio/train/17797742076841560615.wav',
  'array': array([ 0.0000000e+00,  0.0000000e+00,  0.0000000e+00, ...,
         -1.1205673e-04, -8.4638596e-05, -1.2731552e-04], dtype=float32),
  'sampling_rate': 16000},
 'raw_transcription': 'Dit is nog nie huidiglik bekend watter aantygings gemaak sal word of wat owerhede na die seun gelei het nie maar jeugmisdaad-verrigtinge het in die federale hof begin',
 'transcription': 'dit is nog nie huidiglik bekend watter aantygings gemaak sal word of wat owerhede na die seun gelei het nie maar jeugmisdaad-verrigtinge het in die federale hof begin',
 'gender': 0,
 'lang_id': 0,
 'language': 'Afrikaans',
 'lang_group_id': 3}
```

### Data Fields

The data fields are the same among all splits.
- **id** (int): ID of audio sample
- **num_samples** (int): Number of float values
- **path** (str): Path to the audio file
- **audio** (dict): Audio object including loaded audio array, sampling rate and path ot audio
- **raw_transcription** (str): The non-normalized transcription of the audio file
- **transcription** (str): Transcription of the audio file
- **gender** (int): Class id of gender
- **lang_id** (int): Class id of language
- **lang_group_id** (int): Class id of language group

### Data Splits

Every config only has the `"train"` split containing of *ca.* 1000 examples, and a `"validation"` and `"test"` split each containing of *ca.* 400 examples.

## Dataset Creation

We collect between one and three recordings for each sentence (2.3 on average), and buildnew train-dev-test splits with 1509, 150 and 350 sentences for
train, dev and test respectively.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset is meant to encourage the development of speech technology in a lot more languages of the world. One of the goal is to give equal access to technologies like speech recognition or speech translation to everyone, meaning better dubbing or better access to content from the internet (like podcasts, streaming or videos).

### Discussion of Biases

Most datasets have a fair distribution of gender utterances (e.g. the newly introduced FLEURS dataset). While many languages are covered from various regions of the world, the benchmark misses many languages that are all equally important. We believe technology built through FLEURS should generalize to all languages.

### Other Known Limitations

The dataset has a particular focus on read-speech because common evaluation benchmarks like CoVoST-2 or LibriSpeech evaluate on this type of speech. There is sometimes a known mismatch between performance obtained in a read-speech setting and a more noisy setting (in production for instance). Given the big progress that remains to be made on many languages, we believe better performance on FLEURS should still correlate well with actual progress made for speech understanding.

## Additional Information

All datasets are licensed under the [Creative Commons license (CC-BY)](https://creativecommons.org/licenses/).

### Citation Information

You can access the FLEURS paper at https://arxiv.org/abs/2205.12446.
Please cite the paper when referencing the FLEURS corpus as:

```
@article{fleurs2022arxiv,
  title = {FLEURS: Few-shot Learning Evaluation of Universal Representations of Speech},
  author = {Conneau, Alexis and Ma, Min and Khanuja, Simran and Zhang, Yu and Axelrod, Vera and Dalmia, Siddharth and Riesa, Jason and Rivera, Clara and Bapna, Ankur},
  journal={arXiv preprint arXiv:2205.12446},
  url = {https://arxiv.org/abs/2205.12446},
  year = {2022},
```

### Contributions

Thanks to [@patrickvonplaten](https://github.com/patrickvonplaten) and [@aconneau](https://github.com/aconneau) for adding this dataset.
