---
annotations_creators:
- crowdsourced
language_creators:
- machinetranslation
size_categories:
- 1M<n<5
source_datasets:
- multi_nli
- anli
- fever
- lingnli
- alisawuffles/WANLI
task_categories:
- text-classification
task_ids:
- natural-language-inference
- multi-input-text-classification
language: 
- multilingual
- zh
- ja
- ar
- ko
- de
- fr
- es
- pt
- hi
- id
- it
- tr
- ru
- bn
- ur
- mr
- ta
- vi
- fa
- pl
- uk
- nl
- sv
- he
- sw
- ps
---

# Datasheet for the dataset: multilingual-NLI-26lang-2mil7

## Dataset Summary

This dataset contains 2 730 000 NLI text pairs in 26 languages spoken by more than 4 billion people. The dataset can be used to train models for multilingual NLI (Natural Language Inference) or zero-shot classification. The dataset is based on the English datasets [MultiNLI](https://huggingface.co/datasets/multi_nli), [Fever-NLI](https://github.com/easonnie/combine-FEVER-NSMN/blob/master/other_resources/nli_fever.md), [ANLI](https://huggingface.co/datasets/anli), [LingNLI](https://arxiv.org/pdf/2104.07179.pdf) and [WANLI](https://huggingface.co/datasets/alisawuffles/WANLI) and was created using the latest open-source machine translation models. 

The dataset is designed to complement the established multilingual [XNLI](https://huggingface.co/datasets/xnli) dataset. XNLI contains older machine translations of the MultiNLI dataset from 2018 for 14 languages, as well as human translations of 2490 texts for validation and 5010 texts for testing per language. multilingual-NLI-26lang-2mil7 is sourced from 5 different NLI datasets and contains 105 000 machine translated texts for each of 26 languages, leading to 2 730 000 NLI text pairs. 

The release of the dataset is accompanied by the fine-tuned [mDeBERTa-v3-base-xnli-multilingual-nli-2mil7](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7) model, which can be used for NLI or zero-shot classification in 100 languages. 

## Dataset Creation

The languages in the dataset are: ['ar', 'bn', 'de', 'es', 'fa', 'fr', 'he', 'hi', 'id', 'it', 'ja', 'ko', 'mr', 'nl', 'pl', 'ps', 'pt', 'ru', 'sv', 'sw', 'ta', 'tr', 'uk', 'ur', 'vi', 'zh'] (see [ISO language codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)) plus the original English texts. The languages were chosen based on two criteria: (1) They are either included in the list of the [20 most spoken languages](https://en.wikipedia.org/wiki/List_of_languages_by_total_number_of_speakers) (excluding Telugu and Nigerian Pidgin, for which no machine translation model was available); (2) or they are spoken in polit-economically important countries such as the [G20](https://en.wikipedia.org/wiki/G20) or Iran and Israel.

For each of the 26 languages, a different random sample of 25 000 hypothesis-premise pairs was taken from each of the following four datasets: [MultiNLI](https://huggingface.co/datasets/multi_nli) (392 702 texts in total), [Fever-NLI](https://github.com/easonnie/combine-FEVER-NSMN/blob/master/other_resources/nli_fever.md) (196 805 texts), [ANLI](https://huggingface.co/datasets/anli) (162 865 texts), [WANLI](https://huggingface.co/datasets/alisawuffles/WANLI) (102 885 texts). Moreover, a sample of 5000 texts was taken from [LingNLI](https://arxiv.org/pdf/2104.07179.pdf) (29 985 texts) given its smaller total size. This leads to a different random sample of 105 000 source texts per target language with a diverse distribution of data from 5 different NLI datasets. 

Each sample was then machine translated using the latest open-source machine translation models available for the respective language: 
- [opus-mt-tc-big models](https://huggingface.co/models?sort=downloads&search=opus-mt-tc-big) were available for English to ['ar', 'es', 'fr', 'it', 'pt', 'tr']
- [opus-mt-models](https://huggingface.co/models?sort=downloads&search=opus-mt) were available for English to ['de', 'he', 'hi', 'id', 'mr', 'nl', 'ru', 'sv', 'sw', 'uk', 'ur', 'vi', 'zh']
- [m2m100_1.2B](https://huggingface.co/facebook/m2m100_1.2B) was used for the remaining languages ['bn', 'fa', 'ja', 'ko', 'pl', 'ps', 'ta']

## DatasetStructure

### Data Splits

The dataset contains 130 splits (26 * 5), one for each language-dataset pair following the format '{language-iso}_{dataset}'. For example, split 'zh_mnli' contains the Chinese translation of 25 000 texts from the MultiNLI dataset etc. 

### Data Fields

- `premise_original`: The original premise from the English source dataset
- `hypothesis_original`: The original hypothesis from the English source dataset
- `label`: The classification label, with possible values `entailment` (0), `neutral` (1), `contradiction` (2).
- `premise`: The machine translated premise in the target language
- `hypothesis`: The machine translated premise in the target language

### Example of a data instance:

```
{
    "premise_original": "I would not be surprised if the top priority for the Navy was to build a new carrier.",
	"hypothesis_original": "The top priority for the Navy is to build a new carrier.",
	"label": 1, 
	"premise": "Ich würde mich nicht wundern, wenn die oberste Priorität für die Navy wäre, einen neuen Träger zu bauen.",
	"hypothesis": "Die oberste Priorität für die Navy ist es, einen neuen Träger zu bauen."
}
```

## Limitations and bias 

Machine translation is not as good as human translation. Machine translation can introduce inaccuracies that can be problematic for complex tasks like NLI. In an ideal world, original NLI data would be available for many languages. Given the lack of NLI data, using the latest open-source machine translation seems like a good solution to improve multilingual NLI. You can use the Hugging Face data viewer to inspect the data and verify the translation quality for your language of interest. Note that grammatical errors are less problematic for zero-shot use-cases as grammar is less relevant for these applications. 

## Other

The machine translation for the full dataset took roughly 100 hours on an A100 GPU, especially due to the size of the [m2m100_1.2B](https://huggingface.co/facebook/m2m100_1.2B) model.

## Ideas for cooperation or questions?
For updates on new models and datasets, follow me on [Twitter](https://twitter.com/MoritzLaurer).
If you have questions or ideas for cooperation, contact me at m{dot}laurer{at}vu{dot}nl or on [LinkedIn](https://www.linkedin.com/in/moritz-laurer/)

### Citation Information

If the dataset is useful for you, please cite the following article: 

```
@article{laurer_less_2022,
	title = {Less {Annotating}, {More} {Classifying} – {Addressing} the {Data} {Scarcity} {Issue} of {Supervised} {Machine} {Learning} with {Deep} {Transfer} {Learning} and {BERT} - {NLI}},
	url = {https://osf.io/74b8k},
	language = {en-us},
	urldate = {2022-07-28},
	journal = {Preprint},
	author = {Laurer, Moritz and Atteveldt, Wouter van and Casas, Andreu Salleras and Welbers, Kasper},
	month = jun,
	year = {2022},
	note = {Publisher: Open Science Framework},
}
```


