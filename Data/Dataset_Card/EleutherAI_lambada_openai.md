---
pretty_name: LAMBADA OpenAI 
language_creators:
- machine-generated
license: mit
multilinguality:
- translation
task_ids:
- language-modeling
source_datasets:
- lambada
size_categories:
- 1K<n<10K
language:
- de
- en
- es
- fr
- it
dataset_info:
- config_name: default
  features:
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1709449
    num_examples: 5153
  download_size: 1819752
  dataset_size: 1709449
- config_name: de
  features:
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1904576
    num_examples: 5153
  download_size: 1985231
  dataset_size: 1904576
- config_name: en
  features:
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1709449
    num_examples: 5153
  download_size: 1819752
  dataset_size: 1709449
- config_name: es
  features:
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1821735
    num_examples: 5153
  download_size: 1902349
  dataset_size: 1821735
- config_name: fr
  features:
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1948795
    num_examples: 5153
  download_size: 2028703
  dataset_size: 1948795
- config_name: it
  features:
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1813420
    num_examples: 5153
  download_size: 1894613
  dataset_size: 1813420
---

## Dataset Description

- **Repository:** [openai/gpt2](https://github.com/openai/gpt-2)
- **Paper:** Radford et al. [Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf)

### Dataset Summary

This dataset is comprised of the LAMBADA test split as pre-processed by OpenAI (see relevant discussions [here](https://github.com/openai/gpt-2/issues/131#issuecomment-497136199) and [here](https://github.com/huggingface/transformers/issues/491)). It also contains machine translated versions of the split in German, Spanish, French, and Italian.

LAMBADA is used to evaluate the capabilities of computational models for text understanding by means of a word prediction task. LAMBADA is a collection of narrative texts sharing the characteristic that human subjects are able to guess their last word if they are exposed to the whole text, but not if they only see the last sentence preceding the target word. To succeed on LAMBADA, computational models cannot simply rely on local context, but must be able to keep track of information in the broader discourse.


### Languages

English, German, Spanish, French, and Italian.

### Source Data

For non-English languages, the data splits were produced by Google Translate. See the [`translation_script.py`](translation_script.py) for more details.

## Additional Information

### Hash Checksums

For data integrity checks we leave the following checksums for the files in this dataset:

| File Name                                                                | Checksum (SHA-256)                                               |
|--------------------------------------------------------------------------|------------------------------------------------------------------|
| lambada_test_de.jsonl                                                    | 51c6c1795894c46e88e4c104b5667f488efe79081fb34d746b82b8caa663865e |
| [openai/lambada_test.jsonl](https://openaipublic.blob.core.windows.net/gpt-2/data/lambada_test.jsonl) | 4aa8d02cd17c719165fc8a7887fddd641f43fcafa4b1c806ca8abc31fabdb226 |
| lambada_test_en.jsonl                                                    | 4aa8d02cd17c719165fc8a7887fddd641f43fcafa4b1c806ca8abc31fabdb226 |
| lambada_test_es.jsonl                                                    | ffd760026c647fb43c67ce1bc56fd527937304b348712dce33190ea6caba6f9c |
| lambada_test_fr.jsonl                                                    | 941ec6a73dba7dc91c860bf493eb66a527cd430148827a4753a4535a046bf362 |
| lambada_test_it.jsonl                                                    | 86654237716702ab74f42855ae5a78455c1b0e50054a4593fb9c6fcf7fad0850 |

### Licensing

License: [Modified MIT](https://github.com/openai/gpt-2/blob/master/LICENSE)

### Citation

```bibtex
@article{radford2019language,
  title={Language Models are Unsupervised Multitask Learners},
  author={Radford, Alec and Wu, Jeff and Child, Rewon and Luan, David and Amodei, Dario and Sutskever, Ilya},
  year={2019}
}
```

```bibtex
@misc{
    author={Paperno, Denis and Kruszewski, Germán and Lazaridou, Angeliki and Pham, Quan Ngoc and Bernardi, Raffaella and Pezzelle, Sandro and Baroni, Marco and Boleda, Gemma and Fernández, Raquel},
    title={The LAMBADA dataset},
    DOI={10.5281/zenodo.2630551},
    publisher={Zenodo},
    year={2016},
    month={Aug}
}
```

### Contributions

Thanks to Sid Black ([@sdtblck](https://github.com/sdtblck)) for translating the `lambada_openai` dataset into the non-English languages.

Thanks to Jonathan Tow ([@jon-tow](https://github.com/jon-tow)) for adding this dataset. 
