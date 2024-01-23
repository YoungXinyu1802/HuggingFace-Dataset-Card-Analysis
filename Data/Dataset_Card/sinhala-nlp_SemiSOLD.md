# SOLD - A Benchmark for Sinhala Offensive Language Identification

In this repository, we introduce the {S}inhala {O}ffensive {L}anguage {D}ataset **(SOLD)** and present multiple experiments on this dataset. **SOLD** is a manually annotated dataset containing 10,000 posts from Twitter annotated as offensive and not offensive at both sentence-level and token-level. **SOLD** is the largest offensive language dataset compiled for Sinhala. We also introduce **SemiSOLD**, a larger dataset containing more than 145,000 Sinhala tweets, annotated following a semi-supervised approach.

:warning: This repository contains texts that may be offensive and harmful.

## Annotation
We use an annotation scheme split into two levels deciding (a) Offensiveness of a tweet (sentence-level) and (b) Tokens that contribute to the offence at sentence-level (token-level).

### Sentence-level 
Our sentence-level offensive language detection follows level A in OLID [(Zampieri et al., 2019)](https://aclanthology.org/N19-1144/). We asked annotators to discriminate between the following types of tweets:
* **Offensive (OFF)**: Posts containing any form of non-acceptable language (profanity) or a targeted offence, which can be veiled or direct. This includes insults, threats, and posts containing profane language or swear words.
* **Not Offensive (NOT)**: Posts that do not contain offense or profanity.

Each tweet was annotated with one of the above labels, which we used as the labels in sentence-level offensive language identification.

### Token-level
To provide a human explanation of labelling, we collect rationales for the offensive language. Following HateXplain [(Mathew et al., 2021)](https://ojs.aaai.org/index.php/AAAI/article/view/17745), we define a rationale as a specific text segment that justifies the human annotator’s decision of the sentence-level labels. Therefore, We ask the annotators to highlight particular tokens in a tweet that supports their judgement about the sentence-level label (offensive, not offensive). Specifically, if a tweet is offensive, we guide the annotators to highlight tokens from the text that supports the judgement while including non-verbal expressions such as emojis and morphemes that are used to convey the intention as well. We use this as token-level offensive labels in SOLD.


![Alt text](https://github.com/Sinhala-NLP/SOLD/blob/master/images/SOLD_Annotation.png?raw=true "Annotation Process")

## Data
SOLD is released in HuggingFace. It can be loaded in to pandas dataframes using the following code. 

```python
from datasets import Dataset
from datasets import load_dataset

sold_train = Dataset.to_pandas(load_dataset('sinhala-nlp/SOLD', split='train'))
sold_test = Dataset.to_pandas(load_dataset('sinhala-nlp/SOLD', split='test'))
```
The dataset contains of the following columns. 
* **post_id** - Twitter ID
* **text** - Post text
* **tokens** - Tokenised text. Each token is seperated by a space. 
* **rationals** - Offensive tokens. If a token is offensive it is shown as 1 and 0 otherwise.
* **label** - Sentence-level label, offensive or not-offensive. 

![Alt text](https://github.com/Sinhala-NLP/SOLD/blob/master/images/SOLD_Examples.png?raw=true "Four examples from the SOLD dataset")

SemiSOLD is also released HuggingFace and can be loaded to a pandas dataframe using the following code. 

```python
from datasets import Dataset
from datasets import load_dataset

semi_sold = Dataset.to_pandas(load_dataset('sinhala-nlp/SemiSOLD', split='train'))
```
The dataset contains following columns 
* **post_id** - Twitter ID
* **text** - Post text

Furthermore it contains predicted offensiveness scores from nine classifiers trained on SOLD train; xlmr, xlmt, mbert, sinbert, lstm_ft, cnn_ft, lstm_cbow, cnn_cbow, lstm_sl, cnn_sl and svm


## Experiments
Clone the repository and install the libraries using the following command (preferably inside a conda environment)

~~~
pip install -r requirements.txt
~~~

### Sentence-level
Sentence-level transformer based experiments can be executed using the following command. 

~~~
python -m experiments.sentence_level.sinhala_deepoffense
~~~

The command takes the following arguments;

~~~
--model_type : Type of the transformer model (bert, xlmroberta, roberta etc ).
--model_name : The exact architecture and trained weights to use. This may be a Hugging Face Transformers compatible pre-trained model, a community model, or the path to a directory containing model files.
--transfer : Whether to perform transfer learning or not (true or false).
--transfer_language : The initial language if transfer learning is performed (hi, en or si).
    * hi - Perform transfer learning from HASOC 2019 Hindi dataset (Modha et al., 2019).
    * en - Perform transfer learning from Offenseval English dataset (Zampieri et al., 2019).
    * si - Perform transfer learning from CCMS Sinhala dataset (Rathnayake et al., 2021).
--augment : Perform semi supervised data augmentation.
--std : Standard deviation of the models to cut down data augmentation.
--augment_type: The type of the data augmentation.
    * off - Augment only the offensive instances.
    * normal - Augment both offensive and non-offensive instances.
~~~

Sentence-level CNN and LSTM based experiments can be executed using the following command. 

~~~
python -m experiments.sentence_level.sinhala_offensive_nn
~~~

The command takes the following arguments;

~~~
--model_type : Type of the architecture (cnn2D, lstm).
--model_name : The exact word embeddings to use. This may be a gensim model, or the path to a word embeddinng files.
--augment : Perform semi supervised data augmentation.
--std : Standard deviation of the models to cut down data augmentation.
--augment_type: The type of the data augmentation.
    * off - Augment only the offensive instances.
    * normal - Augment both offensive and non-offensive instances.
~~~

### Token-level
Token-level transformer based experiments can be executed using the following command. 

~~~
python -m experiments.sentence_level.sinhala_mudes
~~~

The command takes the following arguments;

~~~
--model_type : Type of the transformer model (bert, xlmroberta, roberta etc ).
--model_name : The exact architecture and trained weights to use. This may be a Hugging Face Transformers compatible pre-trained model, a community model, or the path to a directory containing model files.
--transfer : Whether to perform transfer learning or not (true or false).
--transfer_language : The initial language if transfer learning is performed (hatex or tsd).
    * hatex - Perform transfer learning from HateXplain dataset (Mathew et al., 2021).
    * tsd - Perform transfer learning from TSD dataset (Pavlopoulos  et al., 2021).
~~~

Token-level LIME experiments can be executed using the following command. 

~~~
python -m experiments.sentence_level.sinhala_lime
~~~

The command takes the following arguments;

~~~
--model_type : Type of the transformer model (bert, xlmroberta, roberta etc ).
--model_name : The exact architecture and trained weights to use. This may be a Hugging Face Transformers compatible pre-trained model, a community model, or the path to a directory containing model files.
~~~


## Acknowledgments
We want to acknowledge Janitha Hapuarachchi, Sachith Suraweera, Chandika Udaya Kumara and Ridmi Randima, the team of volunteer annotators that provided their free time and eﬀorts to help us produce SOLD.

## Citation
If you are using the dataset or the models please cite the following paper
~~~
@article{ranasinghe2022sold,
  title={SOLD: Sinhala Offensive Language Dataset},
  author={Ranasinghe, Tharindu and Anuradha, Isuri and Premasiri, Damith and Silva, Kanishka and Hettiarachchi, Hansi and Uyangodage, Lasitha and Zampieri, Marcos},
  journal={arXiv preprint arXiv:2212.00851},
  year={2022}
}
~~~