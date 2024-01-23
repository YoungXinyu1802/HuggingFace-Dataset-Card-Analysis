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
paperswithcode_id: librispeech-1
pretty_name: 'The Cross-lingual TRansfer Evaluation of Multilingual Encoders for Speech
  (XTREME-S) benchmark is a benchmark designed to evaluate speech representations
  across languages, tasks, domains and data regimes. It covers 102 languages from 10+ language families, 3 different domains and 4 task families: speech recognition, translation, classification and retrieval.'
size_categories:
- 10K<n<100K
source_datasets:
- extended|multilingual_librispeech
- extended|covost2
task_categories:
- automatic-speech-recognition
- speech-processing
task_ids:
- speech-recognition
---

# XTREME-S

## Dataset Description

- **Fine-Tuning script:** [research-projects/xtreme-s](https://github.com/huggingface/transformers/tree/master/examples/research_projects/xtreme-s)
- **Paper:** [XTREME-S: Evaluating Cross-lingual Speech Representations](https://arxiv.org/abs/2203.10752)
- **Leaderboard:** [TODO(PVP)]()
- **FLEURS amount of disk used:** 350 GB
- **Multilingual Librispeech amount of disk used:** 2700 GB 
- **Voxpopuli amount of disk used:** 400 GB 
- **Covost2 amount of disk used:** 70 GB 
- **Minds14 amount of disk used:** 5 GB 
- **Total amount of disk used:** ca. 3500 GB 

The Cross-lingual TRansfer Evaluation of Multilingual Encoders for Speech (XTREME-S) benchmark is a benchmark designed to evaluate speech representations across languages, tasks, domains and data regimes. It covers 102 languages from 10+ language families, 3 different domains and 4 task families: speech recognition, translation, classification and retrieval.

***TLDR; XTREME-S is the first speech benchmark that is both diverse, fully accessible, and reproducible. All datasets can be downloaded with a single line of code. 
An easy-to-use and flexible fine-tuning script is provided and actively maintained.***

XTREME-S covers speech recognition with Fleurs, Multilingual LibriSpeech (MLS) and VoxPopuli, speech translation with CoVoST-2, speech classification with LangID (Fleurs) and intent classification (MInds-14) and finally speech(-text) retrieval with Fleurs. Each of the tasks covers a subset of the 102 languages included in XTREME-S, from various regions: 

- **Western Europe**: *Asturian, Bosnian, Catalan, Croatian, Danish, Dutch, English, Finnish, French, Galician, German, Greek, Hungarian, Icelandic, Irish, Italian, Kabuverdianu, Luxembourgish, Maltese, Norwegian, Occitan, Portuguese, Spanish, Swedish, Welsh* 
- **Eastern Europe**: *Armenian, Belarusian, Bulgarian, Czech, Estonian, Georgian, Latvian, Lithuanian, Macedonian, Polish, Romanian, Russian, Serbian, Slovak, Slovenian, Ukrainian*
- **Central-Asia/Middle-East/North-Africa**: *Arabic, Azerbaijani, Hebrew, Kazakh, Kyrgyz, Mongolian, Pashto, Persian, Sorani-Kurdish, Tajik, Turkish, Uzbek*
- **Sub-Saharan Africa**: *Afrikaans, Amharic, Fula, Ganda, Hausa, Igbo, Kamba, Lingala, Luo, Northern-Sotho, Nyanja, Oromo, Shona, Somali, Swahili, Umbundu, Wolof, Xhosa, Yoruba, Zulu*
- **South-Asia**: *Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Nepali, Oriya, Punjabi, Sindhi, Tamil, Telugu, Urdu*
- **South-East Asia**: *Burmese, Cebuano, Filipino, Indonesian, Javanese, Khmer, Lao, Malay, Maori, Thai, Vietnamese*
- **CJK languages**: *Cantonese and Mandarin Chinese, Japanese, Korean*


## Design principles

### Diversity

XTREME-S aims for task, domain and language
diversity. Tasks should be diverse and cover several domains to
provide a reliable evaluation of model generalization and
robustness to noisy naturally-occurring speech in different
environments. Languages should be diverse to ensure that
models can adapt to a wide range of linguistic and phonological
phenomena.

### Accessibility

The sub-dataset for each task can be downloaded 
with a **single line of code** as shown in [Supported Tasks](#supported-tasks).
Each task is available under a permissive license that allows the use and redistribution 
of the data for research purposes. Tasks have been selected based on their usage by 
pre-existing multilingual pre-trained models, for simplicity.

### Reproducibility

We produce fully **open-sourced, maintained and easy-to-use** fine-tuning scripts 
for each task as shown under [Fine-tuning Example](#fine-tuning-and-evaluation-example).
XTREME-S encourages submissions that leverage publicly available speech and text datasets. Users should detail which data they use. 
In general, we encourage settings that can be reproduced by the community, but also encourage the exploration of new frontiers for speech representation learning.
 
## Fine-tuning and Evaluation Example

We provide a fine-tuning script under [**research-projects/xtreme-s**](https://github.com/huggingface/transformers/tree/master/examples/research_projects/xtreme-s).
The fine-tuning script is written in PyTorch and allows one to fine-tune and evaluate any [Hugging Face model](https://huggingface.co/models) on XTREME-S.
The example script is actively maintained by [@anton-l](https://github.com/anton-l) and [@patrickvonplaten](https://github.com/patrickvonplaten). Feel free 
to reach out via issues or pull requests on GitHub if you have any questions.

## Leaderboards

The leaderboard for the XTREME-S benchmark can be found at [this address (TODO(PVP))]().

## Supported Tasks

Note that the suppoprted tasks are focused particularly on linguistic aspect of speech,
while nonlinguistic/paralinguistic aspects of speech relevant to e.g. speech synthesis or voice conversion are **not** evaluated.

<p align="center">
  <img src="https://github.com/patrickvonplaten/scientific_images/raw/master/xtreme_s.png" alt="Datasets used in XTREME"/>
</p>

### 1. Speech Recognition (ASR)

We include three speech recognition datasets: FLEURS-ASR, MLS and VoxPopuli (optionally BABEL). Multilingual fine-tuning is used for these three datasets.

#### FLEURS-ASR

*FLEURS-ASR* is the speech version of the FLORES machine translation benchmark, covering 2000 n-way parallel sentences in n=102 languages.

```py
from datasets import load_dataset

fleurs_asr = load_dataset("google/xtreme_s", "fleurs.af_za")  # for Afrikaans
# to download all data for multi-lingual fine-tuning uncomment following line
# fleurs_asr = load_dataset("google/xtreme_s", "fleurs.all")

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

#### Multilingual LibriSpeech (MLS)

*MLS* is a large multilingual corpus derived from read audiobooks from LibriVox and consists of 8 languages. For this challenge the training data is limited to 10-hours splits.

```py
from datasets import load_dataset

mls = load_dataset("google/xtreme_s", "mls.pl")  # for Polish
# to download all data for multi-lingual fine-tuning uncomment following line
# mls = load_dataset("google/xtreme_s", "mls.all")

# see structure
print(mls)

# load audio sample on the fly
audio_input = mls["train"][0]["audio"]  # first decoded audio sample
transcription = mls["train"][0]["transcription"]  # first transcription

# use `audio_input` and `transcription` to fine-tune your model for ASR
```

#### VoxPopuli

*VoxPopuli* is a large-scale multilingual speech corpus for representation learning and semi-supervised learning, from which we use the speech recognition dataset. The raw data is collected from 2009-2020 European Parliament event recordings. We acknowledge the European Parliament for creating and sharing these materials.

**VoxPopuli has to download the whole dataset 100GB since languages 
are entangled into each other - maybe not worth testing here due to the size**

```py
from datasets import load_dataset

voxpopuli = load_dataset("google/xtreme_s", "voxpopuli.ro")  # for Romanian
# to download all data for multi-lingual fine-tuning uncomment following line
# voxpopuli = load_dataset("google/xtreme_s", "voxpopuli.all")

# see structure
print(voxpopuli)

# load audio sample on the fly
audio_input = voxpopuli["train"][0]["audio"]  # first decoded audio sample
transcription = voxpopuli["train"][0]["transcription"]  # first transcription

# use `audio_input` and `transcription` to fine-tune your model for ASR
```

#### (Optionally) BABEL

*BABEL* from IARPA is a conversational speech recognition dataset in low-resource languages. First, download LDC2016S06, LDC2016S12, LDC2017S08, LDC2017S05 and LDC2016S13. BABEL is the only dataset in our benchmark who is less easily accessible, so you will need to sign in to get access to it on LDC. Although not officially part of the XTREME-S ASR datasets, BABEL is often used for evaluating speech representations on a difficult domain (phone conversations).

```py
from datasets import load_dataset

babel = load_dataset("google/xtreme_s", "babel.as")
```

**The above command is expected to fail with a nice error message,
explaining how to download BABEL**

The following should work:

```py
from datasets import load_dataset
babel = load_dataset("google/xtreme_s", "babel.as", data_dir="/path/to/IARPA_BABEL_OP1_102_LDC2016S06.zip")

# see structure
print(babel)

# load audio sample on the fly
audio_input = babel["train"][0]["audio"]  # first decoded audio sample
transcription = babel["train"][0]["transcription"]  # first transcription
# use `audio_input` and `transcription` to fine-tune your model for ASR
```

### 2. Speech Translation (ST)

We include the CoVoST-2 dataset for automatic speech translation.

#### CoVoST-2

The *CoVoST-2* benchmark has become a commonly used dataset for evaluating automatic speech translation. It covers language pairs from English into 15 languages, as well as 21 languages into English. We use only the "X->En" direction to evaluate cross-lingual representations. The amount of supervision varies greatly in this setting, from one hour for Japanese->English to 180 hours for French->English. This makes pretraining particularly useful to enable such few-shot learning. We enforce multiligual fine-tuning for simplicity. Results are splitted in high/med/low-resource language pairs as explained in the [paper (TODO(PVP))].

```py
from datasets import load_dataset

covost_2 = load_dataset("google/xtreme_s", "covost2.id.en") # for Indonesian to English
# to download all data for multi-lingual fine-tuning uncomment following line
# covost_2 = load_dataset("google/xtreme_s", "covost2.all")

# see structure
print(covost_2)

# load audio sample on the fly
audio_input = covost_2["train"][0]["audio"]  # first decoded audio sample
transcription = covost_2["train"][0]["transcription"]  # first transcription

translation = covost_2["train"][0]["translation"]  # first translation

# use audio_input and translation to fine-tune your model for AST
```

### 3. Speech Classification

We include two multilingual speech classification datasets: FLEURS-LangID and Minds-14.

#### Language Identification - FLEURS-LangID

LangID can often be a domain classification, but in the case of FLEURS-LangID, recordings are done in a similar setting across languages and the utterances correspond to n-way parallel sentences, in the exact same domain, making this task particularly relevant for evaluating LangID. The setting is simple, FLEURS-LangID is splitted in train/valid/test for each language. We simply create a single train/valid/test for LangID by merging all.

```py
from datasets import load_dataset

fleurs_langID = load_dataset("google/xtreme_s", "fleurs.all") # to download all data

# see structure
print(fleurs_langID)

# load audio sample on the fly
audio_input = fleurs_langID["train"][0]["audio"]  # first decoded audio sample
language_class = fleurs_langID["train"][0]["lang_id"]  # first id class
language = fleurs_langID["train"].features["lang_id"].names[language_class]

# use audio_input and language_class to fine-tune your model for audio classification
```

#### Intent classification - Minds-14

Minds-14 is an intent classification made from e-banking speech datasets in 14 languages, with 14 intent labels. We impose a single multilingual fine-tuning to increase the size of the train and test sets and reduce the variance associated with the small size of the dataset per language.

```py
from datasets import load_dataset

minds_14 = load_dataset("google/xtreme_s", "minds14.fr-FR") # for French
# to download all data for multi-lingual fine-tuning uncomment following line
# minds_14 = load_dataset("google/xtreme_s", "minds14.all")

# see structure
print(minds_14)

# load audio sample on the fly
audio_input = minds_14["train"][0]["audio"]  # first decoded audio sample
intent_class = minds_14["train"][0]["intent_class"]  # first transcription
intent = minds_14["train"].features["intent_class"].names[intent_class]

# use audio_input and language_class to fine-tune your model for audio classification
```

### 4. (Optionally) Speech Retrieval 

We optionally include one speech retrieval dataset: FLEURS-Retrieval as explained in the [FLEURS paper](https://arxiv.org/abs/2205.12446).

#### FLEURS-Retrieval

FLEURS-Retrieval provides n-way parallel speech and text data. Similar to how XTREME for text leverages Tatoeba to evaluate bitext mining a.k.a sentence translation retrieval, we use FLEURS-Retrieval to evaluate the quality of fixed-size representations of speech utterances. Our goal is to incentivize the creation of fixed-size speech encoder for speech retrieval. The system has to retrieve the English "key" utterance corresponding to the speech translation of "queries" in 15 languages. Results have to be reported on the test sets of FLEURS-Retrieval whose utterances are used as queries (and keys for English). We augment the English keys with a large number of utterances to make the task more difficult.

```py
from datasets import load_dataset

fleurs_retrieval = load_dataset("google/xtreme_s", "fleurs.af_za")  # for Afrikaans
# to download all data for multi-lingual fine-tuning uncomment following line
# fleurs_retrieval = load_dataset("google/xtreme_s", "fleurs.all")

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

The XTREME-S benchmark is composed of the following datasets:

- [FLEURS](https://huggingface.co/datasets/google/fleurs#dataset-structure)
- [Multilingual Librispeech (MLS)](https://huggingface.co/datasets/facebook/multilingual_librispeech#dataset-structure)
  Note that for MLS, XTREME-S uses `path` instead of `file` and `transcription` instead of `text`.
- [Voxpopuli](https://huggingface.co/datasets/facebook/voxpopuli#dataset-structure)
- [Minds14](https://huggingface.co/datasets/polyai/minds14#dataset-structure)
- [Covost2](https://huggingface.co/datasets/covost2#dataset-structure)
  Note that for Covost2, XTREME-S uses `path` instead of `file` and `transcription` instead of `sentence`.
- [BABEL](https://huggingface.co/datasets/ldc/iarpa_babel#dataset-structure)

Please click on the link of the dataset cards to get more information about its dataset structure.

## Dataset Creation

The XTREME-S benchmark is composed of the following datasets:

- [FLEURS](https://huggingface.co/datasets/google/fleurs#dataset-creation)
- [Multilingual Librispeech (MLS)](https://huggingface.co/datasets/facebook/multilingual_librispeech#dataset-creation)
- [Voxpopuli](https://huggingface.co/datasets/facebook/voxpopuli#dataset-creation)
- [Minds14](https://huggingface.co/datasets/polyai/minds14#dataset-creation)
- [Covost2](https://huggingface.co/datasets/covost2#dataset-creation)
- [BABEL](https://huggingface.co/datasets/ldc/iarpa_babel#dataset-creation)

Please visit the corresponding dataset cards to get more information about the source data.

## Considerations for Using the Data

### Social Impact of Dataset
This dataset is meant to encourage the development of speech technology in a lot more languages of the world. One of the goal is to give equal access to technologies like speech recognition or speech translation to everyone, meaning better dubbing or better access to content from the internet (like podcasts, streaming or videos).

### Discussion of Biases
Most datasets have a fair distribution of gender utterances (e.g. the newly introduced FLEURS dataset). While many languages are covered from various regions of the world, the benchmark misses many languages that are all equally important. We believe technology built through XTREME-S should generalize to all languages.

### Other Known Limitations
The benchmark has a particular focus on read-speech because common evaluation benchmarks like CoVoST-2 or LibriSpeech evaluate on this type of speech. There is sometimes a known mismatch between performance obtained in a read-speech setting and a more noisy setting (in production for instance). Given the big progress that remains to be made on many languages, we believe better performance on XTREME-S should still correlate well with actual progress made for speech understanding.

## Additional Information

All datasets are licensed under the [Creative Commons license (CC-BY)](https://creativecommons.org/licenses/).

### Citation Information

#### XTREME-S
```
@article{conneau2022xtreme,
  title={XTREME-S: Evaluating Cross-lingual Speech Representations},
  author={Conneau, Alexis and Bapna, Ankur and Zhang, Yu and Ma, Min and von Platen, Patrick and Lozhkov, Anton and Cherry, Colin and Jia, Ye and Rivera, Clara and Kale, Mihir and others},
  journal={arXiv preprint arXiv:2203.10752},
  year={2022}
}
```

#### MLS
```
@article{Pratap2020MLSAL,
  title={MLS: A Large-Scale Multilingual Dataset for Speech Research},
  author={Vineel Pratap and Qiantong Xu and Anuroop Sriram and Gabriel Synnaeve and Ronan Collobert},
  journal={ArXiv},
  year={2020},
  volume={abs/2012.03411}
}
```

#### VoxPopuli
```
@article{wang2021voxpopuli,
  title={Voxpopuli: A large-scale multilingual speech corpus for representation learning, semi-supervised learning and interpretation},
  author={Wang, Changhan and Riviere, Morgane and Lee, Ann and Wu, Anne and Talnikar, Chaitanya and Haziza, Daniel and Williamson, Mary and Pino, Juan and Dupoux, Emmanuel},
  journal={arXiv preprint arXiv:2101.00390},
  year={2021}
}
```

#### CoVoST 2
```
@article{DBLP:journals/corr/abs-2007-10310,
  author    = {Changhan Wang and
               Anne Wu and
               Juan Miguel Pino},
  title     = {CoVoST 2: {A} Massively Multilingual Speech-to-Text Translation Corpus},
  journal   = {CoRR},
  volume    = {abs/2007.10310},
  year      = {2020},
  url       = {https://arxiv.org/abs/2007.10310},
  eprinttype = {arXiv},
  eprint    = {2007.10310},
  timestamp = {Thu, 12 Aug 2021 15:37:06 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2007-10310.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

#### Minds14
```
@article{gerz2021multilingual,
  title={Multilingual and cross-lingual intent detection from spoken data},
  author={Gerz, Daniela and Su, Pei-Hao and Kusztos, Razvan and Mondal, Avishek and Lis, Micha{\l} and Singhal, Eshan and Mrk{\v{s}}i{\'c}, Nikola and Wen, Tsung-Hsien and Vuli{\'c}, Ivan},
  journal={arXiv preprint arXiv:2104.08524},
  year={2021}
}
```

### Contributions

Thanks to [@patrickvonplaten](https://github.com/patrickvonplaten), [@anton-l](https://github.com/anton-l), [@aconneau](https://github.com/aconneau) for adding this dataset
