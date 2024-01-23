---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- it
license:
- odc-by
multilinguality:
- monolingual
size_categories:
  tiny:
  - 1M<n<10M
  small:
  - 10M<n<100M
  medium:
  - 10M<n<100M
  large:
  - 10M<n<100M
  full:
  - 100M<n<1B
source_datasets:
- extended
task_categories:
- text-generation
task_ids:
- language-modeling
paperswithcode_id: mc4
pretty_name: mC4_it
---

# Dataset Card for Clean Italian mC4 🇮🇹

## Table of Contents

- [Dataset Card for Clean](#dataset-card-for-mc4)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Preprocessing](#preprocessing)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
  - [Considerations for Using the Data](#considerations-for-using-the-data)
    - [Social Impact of Dataset](#social-impact-of-dataset)
    - [Discussion of Biases](#discussion-of-biases)
    - [Other Known Limitations](#other-known-limitations)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Original Homepage:** [HF Hub](https://huggingface.co/datasets/allenai/c4)
- **Paper:** [ArXiv](https://arxiv.org/abs/1910.10683)

### Dataset Summary

A thoroughly cleaned version of the Italian split of the multilingual colossal, cleaned version of Common Crawl's web crawl corpus (mC4). Based on the [Common Crawl dataset](https://commoncrawl.org). The original version was prepared by [AllenAI](https://allenai.org/), hosted at the address [https://huggingface.co/datasets/allenai/c4](https://huggingface.co/datasets/allenai/c4), with subsequent preprocessing performed by [Gabriele Sarti](https://gsarti.com) following a standard procedure for all dataset shards.

### Preprocessing

The preprocessing of the dataset follows the procedure used by Yeb Havinga for training the model [`t5-base-dutch`](https://huggingface.co/flax-community/t5-base-dutch) on a portion of the cleaned Dutch split of mC4. The original code, that was adapted for Italian in this case, is available on [GitLab](https://gitlab.com/yhavinga/c4nlpreproc). In summary, the preprocessing procedure includes:

 - Removing documents containing words from a selection of the [Italian and English List of Dirty Naught Obscene and Otherwise Bad Words](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words).
 
 - Removing sentences containing:
 
   - Less than 3 words.
   
   - A word longer than 1000 characters.
   
   - An end symbol not matching end-of-sentence punctuation.
   
   - Strings associated to javascript code (e.g. `{`), lorem ipsum, policy information in Italian or English.

 - Removing documents (after sentence filtering):
 
   - Containing less than 5 sentences.
   
   - Containing less than 500 or more than 50'000 characters.
   
   - Not identified as prevalently Italian by the `LangDetect` package.

Using parallel processing with 96 CPU cores on a TPUv3 via Google Cloud to perform the complete clean of all the original Italian shards of mC4 (1024 of ~220Mb train, 8 of ~24Mb validation) required roughly 10 hours due to the demanding steps of sentence tokenization and language detection. The total size of compressed `.json.gz` files is roughly halved after the procedure.

## Dataset Structure

### Data Instances

An example from the dataset:

```
{
  'timestamp': '2020-02-22T22:24:31Z', 
  'url': 'https://altreconomia.it/una-rotonda-sul-pane/', 
  'text': 'Per raggiungere il campo attraversiamo la striscia d’asfalto che porta verso la provinciale numero 13. Mettiamo a rischio la nostra incolumità in un territorio di auto e camion. Sullo sfondo, i profili della Grigna e del Resegone. Più vicini, quelli del solito ipermercato di provincia, e delle villette a schiera che avanzano tra le coltivazioni. È lo sprawling, l’avanzata del cemento.\\nDa questo lato dalla strada, invece, è ancora regno contadino. Almeno per ora. Torniamo a Caponago (Mb), Brianza pura, dove ha avuto i natali il progetto “Spiga e madia”. Ne parlammo su Ae nel gennaio 2009: in un territorio “spaesato”, il Comitato “verso il Distretto di economia solidale della Brianza” (Desbri) e la “Retina” dei gruppi di acquisto locali danno vita a un progetto di produzione di frumento, molitura, panificazione e distribuzione in un raggio di 20 chilometri. Si comincia da zero, nel 2007, senza alcun di finanziamento, quando una famiglia del [...]. Il giochino vale almeno 3 miliardi di euro all’anno. La misura, introdotta in via straordinaria con la finanziaria 2005, è stata prorogata anche con l’ultimo decreto “milleproroghe”.'
}
```

### Data Fields

The data contains the following fields:

- `url`: url of the source as a string
- `text`: text content as a string
- `timestamp`: timestamp of extraction as a string

### Data Splits

To build mC4, the original authors used [CLD3](https://github.com/google/cld3) to identify over 100 languages. For Italian, the whole corpus of scraped text was divided in `1032` jsonl files, `1024` for training following the naming style `c4-it.tfrecord-0XXXX-of-01024.json.gz` and 8 for validation following the naming style `c4-it-validation.tfrecord-0000X-of-00008.json.gz`. The full set of preprocessed files takes roughly 215GB of disk space to download with Git LFS.

For ease of use under different storage capacities, the following incremental splits are available (sizes are estimates). **Important**: The sizes in GB represent the estimated weight for :

|split |train size (docs, words, download + preproc disk space)|validation size|
|:-----|------------------------------------------------------:|--------------:|
|tiny  | 10M docs, 4B words (9 GB + 27 GB)                     | 12k docs      |
|small | 20M docs, 8B words (18 GB + 54 GB)                    | 24k docs      |
|medium| 50M docs, 20B words (47 GB + 135 GB)                  | 48k docs      |
|large | 75M docs, 30B words (71 GB + 203 GB)                  | 72k docs      |
|full  | 103M docs, 41B words (109 GB + 279 GB)                | 96k docs      |

You can load any subset like this:

```python
from datasets import load_dataset

mc4_it_tiny = load_dataset("gsarti/clean_mc4_it", "tiny")
```

Since splits are quite large, you may want to traverse them using the streaming mode available starting from 🤗 Datasets v1.9.0:

```python
from datasets import load_dataset

mc4_it_full_stream = load_dataset("gsarti/clean_mc4_it", "full", split='train', streaming=True)
print(next(iter(mc4_it_full_stream))) # Prints the example presented above
```

## Dataset Creation

Refer to the original paper for more considerations regarding the choice of sources and the scraping process for creating `mC4`.

## Considerations for Using the Data

### Social Impact of Dataset

With more than 200GB of cleaned Italian text and more than 41B estimated words, this is by far the largest available corpus for the Italian language. The second largest dataset available is [OSCAR](https://oscar-corpus.com/), which is only 69GB in size for its deduplicated variant. Using this corpus for training language models with adequate computational resources will allow researchers to reach parity with the performances observed for the English language. This can in turn have important repercussions for the development of commercial language technology applications for the Italian language.

### Discussion of Biases

Despit the cleaning procedure aimed at removing vulgarity and profanity, it must be considered that model trained on this scraped corpus will inevitably reflect biases present in blog articles and comments on the Internet. This makes the corpus especially interesting in the context of studying data biases and how to limit their impacts.

## Additional Information

### Dataset Curators

Authors at AllenAI are the original curators for the `mc4` corpus. For inquiries or requests regarding the Italian cleaned portion contained in this repository, please contact me at [gabriele.sarti996@gmail.com](mailto:gabriele.sarti996@gmail.com)

### Licensing Information

AllenAI are releasing this dataset under the terms of ODC-BY. By using this, you are also bound by the Common Crawl terms of use in respect of the content contained in the dataset.

### Citation Information

If you use this dataset in your work, please cite us and the original mC4 authors as:

```
@article{sarti-nissim-2022-it5,
    title={IT5: Large-scale Text-to-text Pretraining for Italian Language Understanding and Generation},
    author={Sarti, Gabriele and Nissim, Malvina},
    journal={ArXiv preprint 2203.03759},
    url={https://arxiv.org/abs/2203.03759},
    year={2022},
    month={mar}
}

@inproceedings{xue-etal-2021-mt5,
    title = "m{T}5: A Massively Multilingual Pre-trained Text-to-Text Transformer",
    author = "Xue, Linting  and
      Constant, Noah  and
      Roberts, Adam  and
      Kale, Mihir  and
      Al-Rfou, Rami  and
      Siddhant, Aditya  and
      Barua, Aditya  and
      Raffel, Colin",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.41",
    doi = "10.18653/v1/2021.naacl-main.41",
    pages = "483--498",
}
```

### Contributions

Thanks to [@dirkgr](https://github.com/dirkgr) and [@lhoestq](https://github.com/lhoestq) for adding this dataset.
