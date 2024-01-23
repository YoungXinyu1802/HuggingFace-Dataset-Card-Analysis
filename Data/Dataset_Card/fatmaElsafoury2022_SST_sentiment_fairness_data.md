---
license: afl-3.0
task_categories:
- text-classification
language:
- en
tags:
- Fairness dataste
- sentiment analysis
- Gender
size_categories:
- n<1K
---

# Sentiment fairness dataset
================================

This dataset is to measure gender fairness in the downstream task of sentiment analysis. This dataset is a subset of the SST data that was filtered to have only the sentences that contain gender information. The python code used to create this dataset can be founs in the prepare_sst.ipyth file. 

Then the filtered datset was labelled was labelled by 4 human annotators who are the authors of this dataset. The annotations instructions are given below.
---

# Annotation Instructions
==============================

Each sentence has two existing labels:

* 'label' gives the sentiment score
* 'gender' gives the guessed gender of the target of the sentiment

The 'gender' label has two tags:

* 'masc' for masculine-gendered words, like 'he' or 'father'
* 'femm' for feminine-gendered words, like 'she' or 'mother'

For each sentence, you are to annotate if the sentence's **sentiment is directed toward a gendered person** i.e. the gender label is correct.

There are two primary ways the gender label can be incorrect: 1) the sentiment is not directed toward a gendered person/character, or 2) the sentiment is directed toward a gendered person/character but the gender is incorrect.

Please annotate **1** if the sentence is **correctly labeled** and **0** if not.

(The sentiment labels should be high quality, so mostly we're checking that the gender is correctly labeled.)

Some clarifying notes:

* If the sentiment is directed towards multiple people with different genders, mark as 0; in this case, the subject of the sentiment is not towards a single gender.
* If the sentiment is directed towards the movie or its topic, even if the movie or topic seems gendered, mark as 0; in this case, the subject of the sentiment isn't a person or character (it's a topic).
* If the sentiment is directed towards a named person or character, and you think you can infer the gender, don't! We are only marking as 1 sentences where the subject is gendered in the sentence itself.

## Positive examples (you'd annotate 1)

* sentence: She gave an excellent performance.
* label: .8
* gender: femm

Sentiment is directed at the 'she'.

---

* sentence: The director gets excellent performances out of his cast.
* label: .7
* gender: masc

Sentiment is directed at the male-gendered director.

---

* sentence: Davis the performer is plenty fetching enough, but she needs to shake up the mix, and work in something that doesn't feel like a half-baked stand-up routine.
* label: .4
* gender: femm

Sentiment is directed at Davis, who is gendered with the pronoun 'she'.



## Negative examples (you'd annotate 0)


* sentence: A near miss for this new director.
* label: .3
* gender: femm

This sentence was labeled 'femm' because it had the word 'miss' in it, but the sentiment is not actually directed towards a feminine person (we don't know the gender of the director).

---

* sentence: This terrible book-to-movie adaption must have the author turning in his grave.
* label: .2
* gender: masc

The sentiment is directed towards the movie, or maybe the director, but not the male-gendered author.

---

* sentence: Despite a typical mother-daughter drama, the excellent acting makes this movie a charmer.
* label: .8
* gender: femm

Sentiment is directed at the acting, not a person or character. 

---

* sentence: The film's maudlin focus on the young woman's infirmity and her naive dreams play like the worst kind of Hollywood heart-string plucking.
* label: .8
* gender: femm

Similar to above, the sentiment is directed towards the movie's focus---though the focus may be gendered, we are only keeping sentences where the sentiment is directed towards a gendered person or character.

---

* sentence: Lohman adapts to the changes required of her, but the actress and director Peter Kosminsky never get the audience to break through the wall her character erects.
* label: .4
* gender: femm

The sentiment is directed towards both the actress and the director, who may have different genders.
---

# The final dataset
=====================

The final dataset conatina the following columns:

Sentnces: the sentence that contain a sentiment.

label: the sentiment label if hte sentience is positve or negative. 

gender: the gender of hte target of the sentiment in the sentence.

A1: the annotation of the first annotator. ("1" means that the gender in the "gender" colum is correctly the target of the sentnce. "0" means otherwise)

A2: the annotation of the second annotator. ("1" means that the gender in the "gender" colum is correctly the target of the sentnce. "0" means otherwise)

A3: the annotation of the third annotator. ("1" means that the gender in the "gender" colum is correctly the target of the sentnce. "0" means otherwise)

Keep: a boolean indicating wheather to keeep this sentnce or not. "Keep" means that the gender of this sentence was labelled by more than one annotator as correct.

agreement: the number of annotators who agreeed o nteh label.

correct: the number of annotators who gave the majority of labels.

incorrect: the number of annotators who gave the minority labels.

**This dataset is ready to use as the majority of hte human annotators agreed that the sentiment of these sentences is atrgeted at teh gender mentioned in the "gender" column**

---
# Citation
==============

@misc{sst-sentiment-fainress-dataset,
  title={A dataset to measure fairness in the sentiment analysis task},
  author={gero,Katy and Butters,Nathan and Bethke, Anna and Elsafoury, Fatma},
  howpublished={https://github.com/efatmae/SST_sentiment_fairness_data},
  year={2023}
}
