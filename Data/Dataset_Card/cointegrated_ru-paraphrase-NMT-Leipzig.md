---
annotations_creators:
- no-annotation
language_creators:
- machine-generated
language:
- ru
license:
- cc-by-4.0
multilinguality:
- translation
size_categories:
- 100K<n<1M
source_datasets:
- extended|other
task_categories:
- text-generation 
pretty_name: ru-paraphrase-NMT-Leipzig
tags:
- conditional-text-generation
- paraphrase-generation
- paraphrase
---

# Dataset Card for **cointegrated/ru-paraphrase-NMT-Leipzig**

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
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

- **Paper:** https://habr.com/ru/post/564916/
- **Point of Contact:** [@cointegrated](https://huggingface.co/cointegrated) 

### Dataset Summary

The dataset contains 1 million Russian sentences and their automatically generated paraphrases. 

It was created by David Dale ([@cointegrated](https://huggingface.co/cointegrated)) by translating the `rus-ru_web-public_2019_1M` corpus from [the Leipzig collection](https://wortschatz.uni-leipzig.de/en/download) into English and back into Russian. A fraction of the resulting paraphrases are invalid, and should be filtered out.

The blogpost ["Перефразирование русских текстов: корпуса, модели, метрики"](https://habr.com/ru/post/564916/) provides a detailed description of the dataset and its properties.

The dataset can be loaded with the following code:
```Python
import datasets
data = datasets.load_dataset(
    'cointegrated/ru-paraphrase-NMT-Leipzig', 
    data_files={"train": "train.csv","val": "val.csv","test": "test.csv"},
)
```
Its output should look like
```
DatasetDict({
    train: Dataset({
        features: ['idx', 'original', 'en', 'ru', 'chrf_sim', 'labse_sim'],
        num_rows: 980000
    })
    val: Dataset({
        features: ['idx', 'original', 'en', 'ru', 'chrf_sim', 'labse_sim'],
        num_rows: 10000
    })
    test: Dataset({
        features: ['idx', 'original', 'en', 'ru', 'chrf_sim', 'labse_sim'],
        num_rows: 10000
    })
})
```


### Supported Tasks and Leaderboards

The dataset can be used to train and validate models for paraphrase generation or (if negative sampling is used) for paraphrase detection.

### Languages

Russian (main), English (auxilliary).

## Dataset Structure

### Data Instances

Data instances look like

```
{
  "labse_sim": 0.93502015,
  "chrf_sim": 0.4946451012684782,
  "idx": 646422,
  "ru": "О перспективах развития новых медиа-технологий в РФ расскажут на медиафоруме Енисея.",
  "original": "Перспективы развития новых медиатехнологий в Российской Федерации обсудят участники медиафорума «Енисей.",
  "en": "Prospects for the development of new media technologies in the Russian Federation will be discussed at the Yenisey Media Forum."
}
```

Where `original` is the original sentence, and `ru` is its machine-generated paraphrase.

### Data Fields

- `idx`: id of the instance in the original corpus
- `original`: the original sentence	
- `en`: automatic translation of `original` to English
- `ru`: automatic translation of `en` back to Russian, i.e. a paraphrase of `original`
- `chrf_sim`: [ChrF++](https://huggingface.co/metrics/chrf) similarity of `original` and `ru`
- `labse_sim`: cosine similarity of [LaBSE](https://huggingface.co/cointegrated/LaBSE-en-ru) embedings of `original` and `ru`
- `forward_entailment`: predicted probability that `original` entails `ru`
- `backward_entailment`: predicted probability that `ru` entails `original`
- `p_good`: predicted probability that `ru` and `original` have equivalent meaning

### Data Splits

Train – 980K, validation – 10K, test – 10K. The splits were generated randomly.

## Dataset Creation

### Curation Rationale

There are other Russian paraphrase corpora, but they have major drawbacks:
- The best known [corpus from paraphraser.ru 2016 contest](http://paraphraser.ru/download/) is rather small and covers only the News domain.
- [Opusparcus](https://huggingface.co/datasets/GEM/opusparcus), [ParaPhraserPlus](http://paraphraser.ru/download/), and [corpora of Tamara Zhordanija](https://github.com/tamriq/paraphrase) are noisy, i.e. a large proportion of sentence pairs in them have substantial difference in meaning.
- The Russian part of [TaPaCo](https://huggingface.co/datasets/tapaco) has very high lexical overlap in the sentence pairs; in other words, their paraphrases are not diverse enough.

The current corpus is generated with a dual objective: the parphrases should be semantically as close as possible to the original sentences, while being lexically different from them. Back-translation with restricted vocabulary seems to achieve this goal often enough.

### Source Data

#### Initial Data Collection and Normalization

The `rus-ru_web-public_2019_1M` corpus from [the Leipzig collection](https://wortschatz.uni-leipzig.de/en/download) as is.

The process of its creation is described [in this paper](http://www.lrec-conf.org/proceedings/lrec2012/pdf/327_Paper.pdf):

D. Goldhahn, T. Eckart & U. Quasthoff: Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages.
In: *Proceedings of the 8th International Language Resources and Evaluation (LREC'12), 2012*.


#### Automatic paraphrasing

The paraphrasing was carried out by translating the original sentence to English and then back to Russian. 
The models [facebook/wmt19-ru-en](https://huggingface.co/facebook/wmt19-ru-en) and [facebook/wmt19-en-ru](https://huggingface.co/facebook/wmt19-en-ru) were used for translation.
To ensure that the back-translated texts are not identical to the original texts, the final decoder was prohibited to use the token n-grams from the original texts.
The code below implements the paraphrasing function. 

```python
import torch
from transformers import FSMTModel, FSMTTokenizer, FSMTForConditionalGeneration
tokenizer = FSMTTokenizer.from_pretrained("facebook/wmt19-en-ru")
model = FSMTForConditionalGeneration.from_pretrained("facebook/wmt19-en-ru")
inverse_tokenizer = FSMTTokenizer.from_pretrained("facebook/wmt19-ru-en")
inverse_model = FSMTForConditionalGeneration.from_pretrained("facebook/wmt19-ru-en")
model.cuda();
inverse_model.cuda();

def paraphrase(text, gram=4, num_beams=5, **kwargs):
    """ Generate a paraphrase using back translation. 
    Parameter `gram` denotes size of token n-grams of the original sentence that cannot appear in the paraphrase.
    """
    input_ids = inverse_tokenizer.encode(text, return_tensors="pt")
    with torch.no_grad():
        outputs = inverse_model.generate(input_ids.to(inverse_model.device), num_beams=num_beams, **kwargs)
    other_lang = inverse_tokenizer.decode(outputs[0], skip_special_tokens=True)
    # print(other_lang)
    input_ids = input_ids[0, :-1].tolist()
    bad_word_ids = [input_ids[i:(i+gram)] for i in range(len(input_ids)-gram)]
    input_ids = tokenizer.encode(other_lang, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(input_ids.to(model.device), num_beams=num_beams, bad_words_ids=bad_word_ids, **kwargs)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded
```

The corpus was created by running the above `paraphrase` function on the original sentences with parameters `gram=3, num_beams=5, repetition_penalty=3.14, no_repeat_ngram_size=6`.

### Annotations

#### Annotation process

The dataset was annotated by several automatic metrics: 
- [ChrF++](https://huggingface.co/metrics/chrf) between `original` and `ru` sentences;
- cosine similarity between [LaBSE](https://huggingface.co/cointegrated/LaBSE-en-ru) embeddings of these sentences;
- forward and backward entailment probabilites predictd by the [rubert-base-cased-nli-twoway](https://huggingface.co/cointegrated/rubert-base-cased-nli-twoway) model;
- `p_good`, a metric aggregating the four metrics above into a single number. It is obtained with a logistic regression trained on 100 randomly chosen from the train set and manually labelled sentence pairs.

#### Who are the annotators?

Human annotation was involved only for a small subset used to train the model for `p_good`. It was conduced by the dataset author, @cointegrated.

### Personal and Sensitive Information

The dataset is not known to contain any personal or sensitive information. 
The sources and processes of original data collection are described at https://wortschatz.uni-leipzig.de/en/download. 

## Considerations for Using the Data

### Social Impact of Dataset

The dataset may enable creation for paraphrasing systems that can be used both for "good" purposes (such as assisting writers or augmenting text datasets), and for "bad" purposes (such as disguising plagiarism). The authors are not responsible for any uses of the dataset.

### Discussion of Biases

The dataset may inherit some of the biases of [the underlying Leipzig web corpus](https://wortschatz.uni-leipzig.de/en/download) or the neural machine translation models ([1](https://huggingface.co/facebook/wmt19-ru-en), [2](https://huggingface.co/facebook/wmt19-en-ru)) with which it was generated.

### Other Known Limitations

Most of the paraphrases in the dataset are valid (by a rough estimante, at least 80%). However, in some sentence pairs there are faults:
- Named entities are often spelled in different ways (e.g. `"Джейкоб" -> "Яков") or even replaced with other entities (e.g. `"Оймякон" -> "Оймянск" or `"Верхоянск" -> "Тольятти"`).
- Sometimes the meaning of words or phrases changes signigicantly, e.g. `"полустанок" -> "полумашина"`, or `"были по колено в грязи" -> "лежали на коленях в иле"`.
- Sometimes the syntax is changed in a meaning-altering way, e.g. `"Интеллектуальное преимущество Вавилова и его соратников над демагогами из рядов сторонников новой агробиологии разительно очевидно." -> "Интеллектуал Вавилов и его приспешники в новой аграрной биологии явно превзошли демогогов."`.
- Grammatical properties that are present in Russian morphology but absent in English, such as gender, are often lost, e.g. `"Я не хотела тебя пугать" -> "Я не хотел пугать вас"`.

The field `labse_sim` reflects semantic similarity between the sentences, and it can be used to filter out at least some poor paraphrases.

## Additional Information

### Dataset Curators

The dataset was created by [David Dale](https://daviddale.ru/en), a.k.a. [@cointegrated](https://huggingface.co/cointegrated).

### Licensing Information

This corpus, as well as the original Leipzig corpora, are licensed under [CC BY](http://creativecommons.org/licenses/by/4.0/).

### Citation Information

[This blog post](https://habr.com/ru/post/564916/) can be cited:

```
@misc{dale_paraphrasing_2021, 
   author = "Dale, David",
   title  = "Перефразирование русских текстов: корпуса, модели, метрики", 
   editor = "habr.com", 
   url    = "https://habr.com/ru/post/564916/", 
   month  = {June},
   year   = {2021},   
   note = {[Online; posted 28-June-2021]},
}
```

### Contributions

Thanks to [@avidale](https://github.com/avidale) for adding this dataset.