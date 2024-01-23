---
license:
- cc-by-sa-4.0
language:
- de
multilinguality:
- monolingual
size_categories:
- 10M<n<100M
task_categories:
- sentence-similarity
---

# German Backtranslated Paraphrase Dataset
This is a dataset of more than 21 million German paraphrases.
These are text pairs that have the same meaning but are expressed with different words.
The source of the paraphrases are different parallel German / English text corpora.
The English texts were machine translated back into German to obtain the paraphrases.

This dataset can be used for example to train semantic text embeddings.
To do this, for example, [SentenceTransformers](https://www.sbert.net/)
and the [MultipleNegativesRankingLoss](https://www.sbert.net/docs/package_reference/losses.html#multiplenegativesrankingloss)
can be used.

## Maintainers
[![One Conversation](https://huggingface.co/datasets/deutsche-telekom/ger-backtrans-paraphrase/resolve/main/1c-logo.png)](https://www.welove.ai/)

This dataset is open sourced by [Philip May](https://may.la/)
and maintained by the [One Conversation](https://www.welove.ai/)
team of [Deutsche Telekom AG](https://www.telekom.com/).

## Our pre-processing
Apart from the back translation, we have added more columns (for details see below). We have carried out the following pre-processing and filtering:
- We dropped text pairs where one text was longer than 499 characters.
- In the [GlobalVoices v2018q4](https://opus.nlpl.eu/GlobalVoices-v2018q4.php) texts we have removed the `" · Global Voices"` suffix.

## Your post-processing
You probably don't want to use the dataset as it is, but filter it further.
This is what the additional columns of the dataset are for.
For us it has proven useful to delete the following pairs of sentences:

- `min_char_len` less than 15
- `jaccard_similarity` greater than 0.3
- `de_token_count` greater than 30
- `en_de_token_count` greater than 30
- `cos_sim` less than 0.85

## Columns description
- **`uuid`**: a uuid calculated with Python `uuid.uuid4()`
- **`en`**: the original English texts from the corpus
- **`de`**: the original German texts from the corpus
- **`en_de`**: the German texts translated back from English (from `en`)
- **`corpus`**: the name of the corpus
- **`min_char_len`**: the number of characters of the shortest text
- **`jaccard_similarity`**: the [Jaccard similarity coefficient](https://en.wikipedia.org/wiki/Jaccard_index) of both sentences - see below for more details
- **`de_token_count`**: number of tokens of the `de` text, tokenized with [deepset/gbert-large](https://huggingface.co/deepset/gbert-large)
- **`en_de_token_count`**: number of tokens of the `de` text, tokenized with [deepset/gbert-large](https://huggingface.co/deepset/gbert-large)
- **`cos_sim`**: the [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) of both sentences measured with [sentence-transformers/paraphrase-multilingual-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2)

## Anomalies in the texts
It is noticeable that the [OpenSubtitles](https://opus.nlpl.eu/OpenSubtitles-v2018.php) texts have weird dash prefixes. This looks like this:

```
- Hast du was draufgetan?
```

To remove them you could apply this function:

```python
import re

def clean_text(text):
    text = re.sub("^[-\s]*", "", text)
    text = re.sub("[-\s]*$", "", text)
    return text

df["de"] = df["de"].apply(clean_text)
df["en_de"] = df["en_de"].apply(clean_text)
```

## Parallel text corpora used
| Corpus name & link                                                    | Number of paraphrases |
|-----------------------------------------------------------------------|----------------------:|
| [OpenSubtitles](https://opus.nlpl.eu/OpenSubtitles-v2018.php)         |            18,764,810 |
| [WikiMatrix v1](https://opus.nlpl.eu/WikiMatrix-v1.php)               |             1,569,231 |
| [Tatoeba v2022-03-03](https://opus.nlpl.eu/Tatoeba-v2022-03-03.php)   |               313,105 |
| [TED2020 v1](https://opus.nlpl.eu/TED2020-v1.php)                     |               289,374 |
| [News-Commentary v16](https://opus.nlpl.eu/News-Commentary-v16.php)   |               285,722 |
| [GlobalVoices v2018q4](https://opus.nlpl.eu/GlobalVoices-v2018q4.php) |                70,547 |
| **sum**                                                               |.       **21,292,789** |

## Back translation
We have made the back translation from English to German with the help of [Fairseq](https://github.com/facebookresearch/fairseq).
We used the `transformer.wmt19.en-de` model for this purpose:

```python
en2de = torch.hub.load(
    "pytorch/fairseq",
    "transformer.wmt19.en-de",
    checkpoint_file="model1.pt:model2.pt:model3.pt:model4.pt",
    tokenizer="moses",
    bpe="fastbpe",
)
```

## How the Jaccard similarity was calculated
To calculate the [Jaccard similarity coefficient](https://en.wikipedia.org/wiki/Jaccard_index)
we are using the [SoMaJo tokenizer](https://github.com/tsproisl/SoMaJo)
to split the texts into tokens.
We then `lower()` the tokens so that upper and lower case letters no longer make a difference. Below you can find a code snippet with the details:

```python
from somajo import SoMaJo

LANGUAGE = "de_CMC"
somajo_tokenizer = SoMaJo(LANGUAGE)

def get_token_set(text, somajo_tokenizer):
    sentences = somajo_tokenizer.tokenize_text([text])
    tokens = [t.text.lower() for sentence in sentences for t in sentence]
    token_set = set(tokens)
    return token_set

def jaccard_similarity(text1, text2, somajo_tokenizer):
    token_set1 = get_token_set(text1, somajo_tokenizer=somajo_tokenizer)
    token_set2 = get_token_set(text2, somajo_tokenizer=somajo_tokenizer)
    intersection = token_set1.intersection(token_set2)
    union = token_set1.union(token_set2)
    jaccard_similarity = float(len(intersection)) / len(union)
    return jaccard_similarity
```

## Load this dataset

### With Hugging Face Datasets

```python
# pip install datasets
from datasets import load_dataset

dataset = load_dataset("deutsche-telekom/ger-backtrans-paraphrase")
train_dataset = dataset["train"]
```

### With Pandas
If you want to download the csv file and then load it with Pandas you can do it like this:
```python
df = pd.read_csv("train.csv")
```

## Citations & Acknowledgements

**OpenSubtitles**
- citation: P. Lison and J. Tiedemann, 2016, [OpenSubtitles2016: Extracting Large Parallel Corpora from Movie and TV Subtitles](http://www.lrec-conf.org/proceedings/lrec2016/pdf/947_Paper.pdf). In Proceedings of the 10th International Conference on Language Resources and Evaluation (LREC 2016)
- also see http://www.opensubtitles.org/
- license: no special license has been provided at OPUS for this dataset

**WikiMatrix v1**
- citation: Holger Schwenk, Vishrav Chaudhary, Shuo Sun, Hongyu Gong and Paco Guzman, [WikiMatrix: Mining 135M Parallel Sentences in 1620 Language Pairs from Wikipedia](https://arxiv.org/abs/1907.05791), arXiv, July 11 2019
- license: [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

**Tatoeba v2022-03-03**
- citation: J. Tiedemann, 2012, [Parallel Data, Tools and Interfaces in OPUS](https://opus.nlpl.eu/Tatoeba-v2022-03-03.php). In Proceedings of the 8th International Conference on Language Resources and Evaluation (LREC 2012)
- license: [CC BY 2.0 FR](https://creativecommons.org/licenses/by/2.0/fr/)
- copyright: https://tatoeba.org/eng/terms_of_use

**TED2020 v1**
- citation: Reimers, Nils and Gurevych, Iryna, [Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation](https://arxiv.org/abs/2004.09813), In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing, November 2020
- acknowledgements to [OPUS](https://opus.nlpl.eu/) for this service
- license: please respect the [TED Talks Usage Policy](https://www.ted.com/about/our-organization/our-policies-terms/ted-talks-usage-policy)

**News-Commentary v16**
- citation: J. Tiedemann, 2012, [Parallel Data, Tools and Interfaces in OPUS](https://opus.nlpl.eu/Tatoeba-v2022-03-03.php). In Proceedings of the 8th International Conference on Language Resources and Evaluation (LREC 2012)
- license: no special license has been provided at OPUS for this dataset

**GlobalVoices v2018q4**
- citation: J. Tiedemann, 2012, [Parallel Data, Tools and Interfaces in OPUS](https://opus.nlpl.eu/Tatoeba-v2022-03-03.php). In Proceedings of the 8th International Conference on Language Resources and Evaluation (LREC 2012)
- license: no special license has been provided at OPUS for this dataset

## Licensing
Copyright (c) 2022 [Philip May](https://may.la/),
[Deutsche Telekom AG](https://www.telekom.com/)

This work is licensed under [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
