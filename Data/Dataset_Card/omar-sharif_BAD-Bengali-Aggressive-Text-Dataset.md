## Novel Aggressive Text Dataset in Bengali


## Tackling Cyber-Aggression: Identification and Fine-Grained Categorization of Aggressive Texts on Social Media using Weighted Ensemble of Transformers

**Author:** Omar Sharif and Mohammed Moshiul Hoque

**Related Papers:** 

[Paper1 in Neurocomputing Journal](https://www.sciencedirect.com/science/article/abs/pii/S0925231221018567)

[Paper2 in CONSTRAINT@AAAI-2021](https://link.springer.com/chapter/10.1007%2F978-3-030-73696-5_2)

[Paper3 in LTEDI@EACL-2021](https://link.springer.com/chapter/10.1007%2F978-3-030-73696-5_2)

## Abstract

The pervasiveness of aggressive content in social media has become a serious concern for government organizations and tech companies because of its pernicious societal effects. In recent years, social media has been repeatedly used as a tool to incite communal aggression, spread distorted propaganda, damage social harmony and demean the identity of individuals or a community in the public spaces. Therefore, restraining the proliferation of aggressive content and detecting them has become an urgent duty. Studies of the identification of aggressive content have mostly been done for English and other resource-high languages. Automatic systems developed for those languages can not accurately identify detrimental contents written in regional languages like Bengali. To compensate this insufficiency, this work presents a novel Bengali aggressive text dataset (called ‘BAD’) with two-level annotation. In level-A, 14158 texts are labeled as either aggressive or non-aggressive. While in level-B, 6807 aggressive texts are categorized into religious, political, verbal and gendered aggression classes each having 2217, 2085, 2043 and 462 texts respectively. This paper proposes a weighted ensemble technique including m-BERT, distil-BERT, Bangla-BERT and XLM-R as the base classifiers to identify and classify the aggressive texts in Bengali. The proposed model can readdress the softmax probabilities of the participating classifiers depending on their primary outcomes. This weighting technique has enabled the model to outdoes the simple average ensemble and all other machine learning (ML), deep learning (DL) baselines. It has acquired the highest weighted f1-score of 93.43% in the identification task and 93.11% in the categorization task.

## Contribution

Major contributions of this work can be illustrated in the following:

   - Dataset:present a new Bengali aggressive text dataset which contains 6807 aggressive and 7351 non-aggressive texts. Furthermore, by employing a hierarchical annotation schema, aggressive texts are annotated into religious, political, verbal and gendered aggression classes.
   - Insights: provide useful insights and detailed statistics of the data that ensure the quality of the dataset. 
    - Model: develop a weighted ensemble model using m-BERT, distil-BERT, Bangla-BERT, XLM-R to identify and categorize aggressive Bengali texts. The proposed model emphasizes   the participating classifiers' softmax probabilities based on their previous performance on the dataset. This weighting technique outperforms the simple average ensemble approach and enhances the classifier performance in the developed dataset.
  - Benchmarking: investigate and compare the performance of the proposed model with other ML, DL baselines and existing techniques, thus setting up a benchmark work to compare in the future.
- Error analysis: deeply analyze the results and errors of the proposed model. Presents qualitative and quantitative analysis that shed light on the reasons behind some of the errors and provide a few directions that might help to mitigate the system's deficiency.  

This research is one of the pioneering works that aims to identify and classify aggressive texts in Bengali as per our exploration. We expect that the resources developed in this work will pave the way for aggressive text classification researchers in Bengali.


## Ackonwlegements
We sincerely acknowledge the anonymous reviewers for their insightful suggestions, which help to improve the work. This work was supported by the ICT Innovation Fund, ICT Division and Directorate of Research & Extension, CUET. Thanks to [Prof. Dr. Mohammed Moshiul Hoque](https://www.researchgate.net/profile/Moshiul_Hoque) sir for his valuable guidance.

## Cite this work
If you find this repository helpful in your work please cite the following
```
@article{SHARIF2021,
title = {Tackling Cyber-Aggression: Identification and Fine-Grained Categorization of Aggressive Texts on Social Media using Weighted Ensemble of Transformers},
journal = {Neurocomputing},
year = {2021},
issn = {0925-2312},
doi = {https://doi.org/10.1016/j.neucom.2021.12.022},
url = {https://www.sciencedirect.com/science/article/pii/S0925231221018567},
author = {Omar Sharif and Mohammed Moshiul Hoque},
keywords = {Natural language processing, Aggressive text classification, Low resource language, Bengali aggressive text corpus, Deep learning, Transformers, Ensemble},
abstract = {The pervasiveness of aggressive content in social media has become a serious concern for government organizations and tech companies because of its pernicious societal effects. In recent years, social media has been repeatedly used as a tool to incite communal aggression, spread distorted propaganda, damage social harmony and demean the identity of individuals or a community in the public spaces. Therefore, restraining the proliferation of aggressive content and detecting them has become an urgent duty. Studies of the identification of aggressive content have mostly been done for English and other resource-high languages. Automatic systems developed for those languages can not accurately identify detrimental contents written in regional languages like Bengali. To compensate this insufficiency, this work presents a novel Bengali aggressive text dataset (called ‘BAD’) with two-level annotation. In level-A, 14158 texts are labeled as either aggressive or non-aggressive. While in level-B, 6807 aggressive texts are categorized into religious, political, verbal and gendered aggression classes each having 2217, 2085, 2043 and 462 texts respectively. This paper proposes a weighted ensemble technique including m-BERT, distil-BERT, Bangla-BERT and XLM-R as the base classifiers to identify and classify the aggressive texts in Bengali. The proposed model can readdress the softmax probabilities of the participating classifiers depending on their primary outcomes. This weighting technique has enabled the model to outdoes the simple average ensemble and all other machine learning (ML), deep learning (DL) baselines. It has acquired the highest weighted f1-score of 93.43% in the identification task and 93.11% in the categorization task.}
}

@InProceedings{sharif2021constraint,
author="Sharif, Omar
and Hoque, Mohammed Moshiul",
editor="Chakraborty, Tanmoy  and et al.",
title="Identification and Classification of Textual Aggression in Social Media: Resource Creation and Evaluation",
booktitle="Combating Online Hostile Posts in Regional Languages during Emergency Situation",
year="2021",
publisher="Springer Nature Switzerland AG",
pages="1--12",
doi = {https://doi.org/10.1007/978-3-030-73696-5_2},
}

@inproceedings{sharif-etal-2021-nlp,
    title = "{NLP}-{CUET}@{D}ravidian{L}ang{T}ech-{EACL}2021: Offensive Language Detection from Multilingual Code-Mixed Text using Transformers",
    author = "Sharif, Omar  and
      Hossain, Eftekhar  and
      Hoque, Mohammed Moshiul",
    booktitle = "Proceedings of the First Workshop on Speech and Language Technologies for Dravidian Languages",
    month = apr,
    year = "2021",
    address = "Kyiv",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.dravidianlangtech-1.35",
    pages = "255--261",
    abstract = "The increasing accessibility of the internet facilitated social media usage and encouraged individuals to express their opinions liberally. Nevertheless, it also creates a place for content polluters to disseminate offensive posts or contents. Most of such offensive posts are written in a cross-lingual manner and can easily evade the online surveillance systems. This paper presents an automated system that can identify offensive text from multilingual code-mixed data. In the task, datasets provided in three languages including Tamil, Malayalam and Kannada code-mixed with English where participants are asked to implement separate models for each language. To accomplish the tasks, we employed two machine learning techniques (LR, SVM), three deep learning (LSTM, LSTM+Attention) techniques and three transformers (m-BERT, Indic-BERT, XLM-R) based methods. Results show that XLM-R outperforms other techniques in Tamil and Malayalam languages while m-BERT achieves the highest score in the Kannada language. The proposed models gained weighted f{\_}1 score of 0.76 (for Tamil), 0.93 (for Malayalam ), and 0.71 (for Kannada) with a rank of 3rd, 5th and 4th respectively.",
}
```

## Note
`If you find any anomaly or have any query/suggestion feel free to ping.
