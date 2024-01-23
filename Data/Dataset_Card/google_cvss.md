---
license: cc-by-4.0
---

# CVSS: A Massively Multilingual Speech-to-Speech Translation Corpus


*CVSS* is a massively multilingual-to-English speech-to-speech translation corpus, covering sentence-level parallel speech-to-speech translation pairs from 21 languages into English. CVSS is derived from the [Common Voice](https://commonvoice.mozilla.org/) speech corpus and the [CoVoST 2](https://github.com/facebookresearch/covost) speech-to-text translation corpus. The translation speech in CVSS is synthesized with two state-of-the-art TTS models trained on the [LibriTTS](http://www.openslr.org/60/) corpus.

CVSS includes two versions of spoken translation for all the 21 x-en language pairs from CoVoST 2, with each version providing unique values:

 - *CVSS-C*: All the translation speeches are in a single canonical speaker's voice. Despite being synthetic, these speeches are of very high naturalness and cleanness, as well as having a consistent speaking style. These properties ease the modeling of the target speech and enable models to produce high quality translation speech suitable for user-facing applications.

 - *CVSS-T*: The translation speeches are in voices transferred from the corresponding source speeches. Each translation pair has similar voices on the two sides despite being in different languages, making this dataset suitable for building models that preserve speakers' voices when translating speech into different languages.

Together with the source speeches originated from Common Voice, they make two multilingual speech-to-speech translation datasets each with about 1,900 hours of speech.

In addition to translation speech, CVSS also provides normalized translation text matching the pronunciation in the translation speech (e.g. on numbers, currencies, acronyms, etc.), which can be used for both model training as well as standardizing evaluation.

Please check out [our paper](https://arxiv.org/abs/2201.03713) for the detailed description of this corpus, as well as the baseline models we trained on both datasets.


# Load the data


The following example loads the translation speech (i.e. target speech) and the normalized translation text (i.e. target text) released in CVSS corpus. You'll need to load the source speech and optionally the source text from [Common Voice v4.0](https://huggingface.co/datasets/mozilla-foundation/common_voice_4_0) separately, and join them by the file names.

```py
from datasets import load_dataset

# Load only ar-en and ja-en language pairs. Omitting the `languages` argument
# would load all the language pairs.
cvss_c = load_dataset('google/cvss', 'cvss_c', languages=['ar', 'ja'])

# Print the structure of the dataset.
print(cvss_c)
```

# License

CVSS is released under the very permissive [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license.


## Citation

Please cite this paper when referencing the CVSS corpus:

```
@inproceedings{jia2022cvss,
    title={{CVSS} Corpus and Massively Multilingual Speech-to-Speech Translation},
    author={Jia, Ye and Tadmor Ramanovich, Michelle and Wang, Quan and Zen, Heiga},
    booktitle={Proceedings of Language Resources and Evaluation Conference (LREC)},
    pages={6691--6703},
    year={2022}
}
```

