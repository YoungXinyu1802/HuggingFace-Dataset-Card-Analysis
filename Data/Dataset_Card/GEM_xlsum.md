---
annotations_creators:
- none
language_creators:
- unknown
language:
- und
license:
- cc-by-nc-sa-4.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- summarization
task_ids: []
pretty_name: xlsum
---

# Dataset Card for GEM/xlsum

## Dataset Description

- **Homepage:** https://github.com/csebuetnlp/xl-sum
- **Repository:** https://huggingface.co/datasets/csebuetnlp/xlsum/tree/main/data
- **Paper:** https://aclanthology.org/2021.findings-acl.413/
- **Leaderboard:** http://explainaboard.nlpedia.ai/leaderboard/task_xlsum/
- **Point of Contact:** Tahmid Hasan

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/xlsum).

### Dataset Summary 

XLSum is a highly multilingual summarization dataset supporting 44 language. The data stems from BBC news articles. 

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/xlsum')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/xlsum).

#### website
[Github](https://github.com/csebuetnlp/xl-sum)

#### paper
[ACL Anthology](https://aclanthology.org/2021.findings-acl.413/)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Github](https://github.com/csebuetnlp/xl-sum)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Huggingface](https://huggingface.co/datasets/csebuetnlp/xlsum/tree/main/data)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://aclanthology.org/2021.findings-acl.413/)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{hasan-etal-2021-xl,
    title = "{XL}-Sum: Large-Scale Multilingual Abstractive Summarization for 44 Languages",
    author = "Hasan, Tahmid  and
      Bhattacharjee, Abhik  and
      Islam, Md. Saiful  and
      Mubasshir, Kazi  and
      Li, Yuan-Fang  and
      Kang, Yong-Bin  and
      Rahman, M. Sohel  and
      Shahriyar, Rifat",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.413",
    pages = "4693--4703",
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Tahmid Hasan

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
tahmidhasan@cse.buet.ac.bd

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
yes

#### Leaderboard Link

<!-- info: Provide a link to the leaderboard. -->
<!-- scope: periscope -->
[Explainaboard](http://explainaboard.nlpedia.ai/leaderboard/task_xlsum/)

#### Leaderboard Details

<!-- info: Briefly describe how the leaderboard evaluates models. -->
<!-- scope: microscope -->
The leaderboard ranks models based on ROUGE scores (R1/R2/RL) of the generated summaries.



### Languages and Intended Use

#### Multilingual?

<!-- quick -->
<!-- info: Is the dataset multilingual? -->
<!-- scope: telescope -->
yes

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`Amharic`, `Arabic`, `Azerbaijani`, `Bengali, Bangla`, `Burmese`, `Chinese (family)`, `English`, `French`, `Gujarati`, `Hausa`, `Hindi`, `Igbo`, `Indonesian`, `Japanese`, `Rundi`, `Korean`, `Kirghiz, Kyrgyz`, `Marathi`, `Nepali (individual language)`, `Oromo`, `Pushto, Pashto`, `Persian`, `Ghanaian Pidgin English`, `Portuguese`, `Panjabi, Punjabi`, `Russian`, `Scottish Gaelic, Gaelic`, `Serbian`, `Romano-Serbian`, `Sinhala, Sinhalese`, `Somali`, `Spanish, Castilian`, `Swahili (individual language), Kiswahili`, `Tamil`, `Telugu`, `Thai`, `Tigrinya`, `Turkish`, `Ukrainian`, `Urdu`, `Uzbek`, `Vietnamese`, `Welsh`, `Yoruba`

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-nc-sa-4.0: Creative Commons Attribution Non Commercial Share Alike 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
Abstractive summarization has centered around the English language, as most large abstractive summarization datasets are available in English only. Though there have been some recent efforts for curating multilingual abstractive summarization datasets, they are limited in terms of the number of languages covered, the number of training samples, or both. To this end, **XL-Sum** presents a large-scale abstractive summarization dataset of 1.35 million news articles from 45 languages crawled from the British Broadcasting Corporation website. It is intended to be used for both multilingual and per-language summarization tasks.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Summarization

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Summarize news-like text in one of 45 languages.


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Bangladesh University of Engineering and Technology

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Tahmid Hasan (Bangladesh University of Engineering and Technology), Abhik Bhattacharjee (Bangladesh University of Engineering and Technology)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
-  `gem_id`: A string representing the article ID.
-  `url`: A string representing the article URL.
-  `title`: A string containing the article title.
-  `summary`: A string containing the article summary.
-  `text` : A string containing the article text. 


#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{
    "gem_id": "GEM-xlsum_english-train-1589",
    "url": "[BBC news](https://www.bbc.com/news)/technology-17657859",
    "title": "Yahoo files e-book advert system patent applications",
    "summary": "Yahoo has signalled it is investigating e-book adverts as a way to stimulate its earnings.",
    "text": "Yahoo's patents suggest users could weigh the type of ads against the sizes of discount before purchase. It says in two US patent applications that ads for digital book readers have been \"less than optimal\" to date. The filings suggest that users could be offered titles at a variety of prices depending on the ads' prominence They add that the products shown could be determined by the type of book being read, or even the contents of a specific chapter, phrase or word. The paperwork was published by the US Patent and Trademark Office late last week and relates to work carried out at the firm's headquarters in Sunnyvale, California. \"Greater levels of advertising, which may be more valuable to an advertiser and potentially more distracting to an e-book reader, may warrant higher discounts,\" it states. Free books It suggests users could be offered ads as hyperlinks based within the book's text, in-laid text or even \"dynamic content\" such as video. Another idea suggests boxes at the bottom of a page could trail later chapters or quotes saying \"brought to you by Company A\". It adds that the more willing the customer is to see the ads, the greater the potential discount. \"Higher frequencies... may even be great enough to allow the e-book to be obtained for free,\" it states. The authors write that the type of ad could influence the value of the discount, with \"lower class advertising... such as teeth whitener advertisements\" offering a cheaper price than \"high\" or \"middle class\" adverts, for things like pizza. The inventors also suggest that ads could be linked to the mood or emotional state the reader is in as a they progress through a title. For example, they say if characters fall in love or show affection during a chapter, then ads for flowers or entertainment could be triggered. The patents also suggest this could applied to children's books - giving the Tom Hanks animated film Polar Express as an example. It says a scene showing a waiter giving the protagonists hot drinks \"may be an excellent opportunity to show an advertisement for hot cocoa, or a branded chocolate bar\". Another example states: \"If the setting includes young characters, a Coke advertisement could be provided, inviting the reader to enjoy a glass of Coke with his book, and providing a graphic of a cool glass.\" It adds that such targeting could be further enhanced by taking account of previous titles the owner has bought. 'Advertising-free zone' At present, several Amazon and Kobo e-book readers offer full-screen adverts when the device is switched off and show smaller ads on their menu screens, but the main text of the titles remains free of marketing. Yahoo does not currently provide ads to these devices, and a move into the area could boost its shrinking revenues. However, Philip Jones, deputy editor of the Bookseller magazine, said that the internet firm might struggle to get some of its ideas adopted. \"This has been mooted before and was fairly well decried,\" he said. \"Perhaps in a limited context it could work if the merchandise was strongly related to the title and was kept away from the text. \"But readers - particularly parents - like the fact that reading is an advertising-free zone. Authors would also want something to say about ads interrupting their narrative flow.\""
}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
The splits in the dataset are specified by the language names, which are as follows:
-  `amharic`
-  `arabic`
-  `azerbaijani`
-  `bengali`
-  `burmese`
-  `chinese_simplified`
-  `chinese_traditional`
-  `english`
-  `french`
-  `gujarati`
-  `hausa`
-  `hindi`
-  `igbo`
-  `indonesian`
-  `japanese`
-  `kirundi`
-  `korean`
-  `kyrgyz`
-  `marathi`
-  `nepali`
-  `oromo`
-  `pashto`
-  `persian`
-  `pidgin`
-  `portuguese`
-  `punjabi`
-  `russian`
-  `scottish_gaelic`
-  `serbian_cyrillic`
-  `serbian_latin`
-  `sinhala`
-  `somali`
-  `spanish`
-  `swahili`
-  `tamil`
-  `telugu`
-  `thai`
-  `tigrinya`
-  `turkish`
-  `ukrainian`
-  `urdu`
-  `uzbek`
-  `vietnamese`
-  `welsh`
-  `yoruba`

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
We used a 80%-10%-10% split for all languages with a few exceptions. `English` was split 93%-3.5%-3.5% for the evaluation set size to resemble that of `CNN/DM` and `XSum`; `Scottish Gaelic`, `Kyrgyz` and `Sinhala` had relatively fewer samples, their evaluation sets were increased to 500 samples for more reliable evaluation. Same articles were used for evaluation in the two variants of Chinese and Serbian to prevent data leakage in multilingual training. Individual dataset download links with train-dev-test example counts are given below:

Language      | ISO 639-1 Code | BBC subdomain(s) | Train | Dev | Test | Total |
--------------|----------------|------------------|-------|-----|------|-------|
Amharic | am | [BBC amharic](https://www.bbc.com/amharic) | 5761 | 719 | 719 | 7199 |
Arabic | ar | [BBC arabic](https://www.bbc.com/arabic) | 37519 | 4689 | 4689 | 46897 |
Azerbaijani | az | [BBC azeri](https://www.bbc.com/azeri) | 6478 | 809 | 809 | 8096 |
Bengali | bn | [BBC bengali](https://www.bbc.com/bengali) | 8102 | 1012 | 1012 | 10126 |
Burmese | my | [BBC burmese](https://www.bbc.com/burmese) | 4569 | 570 | 570 | 5709 |
Chinese (Simplified) | zh-CN | [BBC ukchina](https://www.bbc.com/ukchina)/simp, [BBC zhongwen](https://www.bbc.com/zhongwen)/simp | 37362 | 4670 | 4670 | 46702 |
Chinese (Traditional) | zh-TW | [BBC ukchina](https://www.bbc.com/ukchina)/trad, [BBC zhongwen](https://www.bbc.com/zhongwen)/trad | 37373 | 4670 | 4670 | 46713 |
English | en | [BBC english](https://www.bbc.com/english), [BBC sinhala](https://www.bbc.com/sinhala) `*` | 306522 | 11535 | 11535 | 329592 |
French | fr | [BBC afrique](https://www.bbc.com/afrique) | 8697 | 1086 | 1086 | 10869 |
Gujarati | gu | [BBC gujarati](https://www.bbc.com/gujarati) | 9119 | 1139 | 1139 | 11397 |
Hausa | ha | [BBC hausa](https://www.bbc.com/hausa) | 6418 | 802 | 802 | 8022 |
Hindi | hi | [BBC hindi](https://www.bbc.com/hindi) | 70778 | 8847 | 8847 | 88472 |
Igbo | ig | [BBC igbo](https://www.bbc.com/igbo) | 4183 | 522 | 522 | 5227 |
Indonesian | id | [BBC indonesia](https://www.bbc.com/indonesia) | 38242 | 4780 | 4780 | 47802 |
Japanese | ja | [BBC japanese](https://www.bbc.com/japanese) | 7113 | 889 | 889 | 8891 |
Kirundi | rn | [BBC gahuza](https://www.bbc.com/gahuza) | 5746 | 718 | 718 | 7182 |
Korean | ko | [BBC korean](https://www.bbc.com/korean) | 4407 | 550 | 550 | 5507 |
Kyrgyz | ky | [BBC kyrgyz](https://www.bbc.com/kyrgyz) | 2266 | 500 | 500 | 3266 |
Marathi | mr | [BBC marathi](https://www.bbc.com/marathi) | 10903 | 1362 | 1362 | 13627 |
Nepali | np | [BBC nepali](https://www.bbc.com/nepali) | 5808 | 725 | 725 | 7258 |
Oromo | om | [BBC afaanoromoo](https://www.bbc.com/afaanoromoo) | 6063 | 757 | 757 | 7577 |
Pashto | ps | [BBC pashto](https://www.bbc.com/pashto) | 14353 | 1794 | 1794 | 17941 |
Persian | fa | [BBC persian](https://www.bbc.com/persian) | 47251 | 5906 | 5906 | 59063 |
Pidgin`**` | pcm | [BBC pidgin](https://www.bbc.com/pidgin) | 9208 | 1151 | 1151 | 11510 |
Portuguese | pt | [BBC portuguese](https://www.bbc.com/portuguese) | 57402 | 7175 | 7175 | 71752 |
Punjabi | pa | [BBC punjabi](https://www.bbc.com/punjabi) | 8215 | 1026 | 1026 | 10267 |
Russian | ru | [BBC russian](https://www.bbc.com/russian), [BBC ukrainian](https://www.bbc.com/ukrainian) `*` | 62243 | 7780 | 7780 | 77803 |
Scottish Gaelic | gd | [BBC naidheachdan](https://www.bbc.com/naidheachdan) | 1313 | 500 | 500 | 2313 |
Serbian (Cyrillic) | sr | [BBC serbian](https://www.bbc.com/serbian)/cyr | 7275 | 909 | 909 | 9093 |
Serbian (Latin) | sr | [BBC serbian](https://www.bbc.com/serbian)/lat | 7276 | 909 | 909 | 9094 |
Sinhala | si | [BBC sinhala](https://www.bbc.com/sinhala) | 3249 | 500 | 500 | 4249 |
Somali | so | [BBC somali](https://www.bbc.com/somali) | 5962 | 745 | 745 | 7452 |
Spanish | es | [BBC mundo](https://www.bbc.com/mundo) | 38110 | 4763 | 4763 | 47636 |
Swahili | sw | [BBC swahili](https://www.bbc.com/swahili) | 7898 | 987 | 987 | 9872 |
Tamil | ta | [BBC tamil](https://www.bbc.com/tamil) | 16222 | 2027 | 2027 | 20276 |
Telugu | te | [BBC telugu](https://www.bbc.com/telugu) | 10421 | 1302 | 1302 | 13025 |
Thai | th | [BBC thai](https://www.bbc.com/thai) | 6616 | 826 | 826 | 8268 |
Tigrinya | ti | [BBC tigrinya](https://www.bbc.com/tigrinya) | 5451 | 681 | 681 | 6813 |
Turkish | tr | [BBC turkce](https://www.bbc.com/turkce) | 27176 | 3397 | 3397 | 33970 |
Ukrainian | uk | [BBC ukrainian](https://www.bbc.com/ukrainian) | 43201 | 5399 | 5399 | 53999 |
Urdu | ur | [BBC urdu](https://www.bbc.com/urdu) | 67665 | 8458 | 8458 | 84581 |
Uzbek | uz | [BBC uzbek](https://www.bbc.com/uzbek) | 4728 | 590 | 590 | 5908 |
Vietnamese | vi | [BBC vietnamese](https://www.bbc.com/vietnamese) | 32111 | 4013 | 4013 | 40137 |
Welsh | cy | [BBC cymrufyw](https://www.bbc.com/cymrufyw) | 9732 | 1216 | 1216 | 12164 |
Yoruba | yo | [BBC yoruba](https://www.bbc.com/yoruba) | 6350 | 793 | 793 | 7936 |

`*` A lot of articles in BBC Sinhala and BBC Ukrainian were written in English and Russian respectively. They were identified using [Fasttext](https://arxiv.org/abs/1607.01759) and moved accordingly.
`**` West African Pidgin English



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
Traditional abstractive text summarization has been centered around English and other high-resource languages. **XL-Sum** provides a large collection of high-quality article-summary pairs for 45  languages where the languages range from high-resource to extremely low-resource. This enables the research community to explore the summarization capabilities of different models for multiple languages and languages in isolation. We believe the addition of **XL-Sum** to GEM makes the domain of abstractive text summarization more diversified and inclusive to the research community.  We hope our efforts in this work will encourage the community to push the boundaries of abstractive text summarization beyond the English language, especially for low and mid-resource languages, bringing technological advances to communities of these languages that have been traditionally under-served.


#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
yes

#### Unique Language Coverage

<!-- info: Does this dataset cover other languages than other datasets for the same task? -->
<!-- scope: periscope -->
yes

#### Difference from other GEM datasets

<!-- info: What else sets this dataset apart from other similar datasets in GEM? -->
<!-- scope: microscope -->
The summaries are highly concise and abstractive.

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Conciseness, abstractiveness, and overall summarization capability.


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
no

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
no


### Getting Started with the Task




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Conciseness, abstractiveness, and overall summarization capability.

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`ROUGE`

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
ROUGE is the de facto evaluation metric used for text summarization. However, it was designed specifically for evaluating English texts. Due to the nature of the metric, scores are heavily dependent on text tokenization / stemming / unnecessary character removal, etc. Some modifications to the original ROUGE evaluation were done such as punctuation only removal, language specific tokenization/stemming to enable reliable comparison of source and target summaries across different scripts.

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
no



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
State-of-the-art text summarization models are heavily data-driven, i.e., a large number of article-summary pairs are required to train them effectively. As a result, abstractive summarization has centered around the English language, as most large abstractive summarization datasets are available in English only. Though there have been some recent efforts for curating multilingual abstractive summarization datasets, they are limited in terms of the number of languages covered, the number of training samples, or both. To this end, we curate **XL-Sum**, a large-scale abstractive summarization dataset of 1.35 million news articles from 45 languages crawled from the British Broadcasting Corporation website.


#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Introduce new languages in the english-centric domain of abstractive text summarization and enable both multilingual and per-language summarization.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
yes

#### Source Details

<!-- info: List the sources (one per line) -->
<!-- scope: periscope -->
British Broadcasting Corporation (BBC) news websites.


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Found`

#### Where was it found?

<!-- info: If found, where from? -->
<!-- scope: telescope -->
`Multiple websites`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
The language content was written by professional news editors hired by BBC.

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
News

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
not validated

#### Data Preprocessing

<!-- info: How was the text data pre-processed? (Enter N/A if the text was not pre-processed) -->
<!-- scope: microscope -->
We used 'NFKC' normalization on all text instances.

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
algorithmically

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
We designed a crawler to recursively crawl pages starting from the homepage by visiting different article links present in each page visited. We were able to take advantage of the fact that all BBC sites have somewhat similar structures, and were able to scrape articles from all sites. We discarded pages with no textual contents (mostly pages consisting of multimedia contents) before further processing. We designed a number of heuristics to make the extraction effective by carefully examining the HTML structures of the crawled pages:
1. The desired summary must be present within the beginning two paragraphs of an article.
2. The summary paragraph must have some portion of texts in bold format.
3. The summary paragraph may contain some hyperlinks that may not be bold. The proportion of bold texts and hyperlinked texts to the total length of the paragraph in consideration must be at least 95\%.
4. All texts except the summary and the headline must be included in the input text (including image captions).
5. The input text must be at least twice as large as the summary.



### Structured Annotations

#### Additional Annotations?

<!-- quick -->
<!-- info: Does the dataset have additional annotations for each instance? -->
<!-- scope: telescope -->
none

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
no


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
yes

#### Consent Policy Details

<!-- info: What was the consent policy? -->
<!-- scope: microscope -->
BBC's policy specifies that the text content within its websites can be used for non-commercial research only.


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
likely

#### Categories of PII

<!-- info: What categories of PII are present or suspected in the data? -->
<!-- scope: periscope -->
`generic PII`

#### Any PII Identification?

<!-- info: Did the curators use any automatic/manual method to identify PII in the dataset? -->
<!-- scope: periscope -->
no identification


### Maintenance

#### Any Maintenance Plan?

<!-- info: Does the original dataset have a maintenance plan? -->
<!-- scope: telescope -->
no



## Broader Social Context

### Previous Work on the Social Impact of the Dataset

#### Usage of Models based on the Data

<!-- info: Are you aware of cases where models trained on the task featured in this dataset ore related tasks have been used in automated systems? -->
<!-- scope: telescope -->
no


### Impact on Under-Served Communities

#### Addresses needs of underserved Communities?

<!-- info: Does this dataset address the needs of communities that are traditionally underserved in language technology, and particularly language generation technology? Communities may be underserved for exemple because their language, language variety, or social or geographical context is underepresented in NLP and NLG resources (datasets and models). -->
<!-- scope: telescope -->
yes

#### Details on how Dataset Addresses the Needs

<!-- info: Describe how this dataset addresses the needs of underserved communities. -->
<!-- scope: microscope -->
This dataset introduces  summarization corpus for many languages where there weren't any datasets like this curated before.


### Discussion of Biases

#### Any Documented Social Biases?

<!-- info: Are there documented social biases in the dataset? Biases in this context are variations in the ways members of different social categories are represented that can have harmful downstream consequences for members of the more disadvantaged group. -->
<!-- scope: telescope -->
no

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
Yes



## Considerations for Using the Data

### PII Risks and Liability



### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`research use only`, `non-commercial use only`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`research use only`, `non-commercial use only`


### Known Technical Limitations

#### Technical Limitations

<!-- info: Describe any known technical limitations, such as spurrious correlations, train/test overlap, annotation biases, or mis-annotations, and cite the works that first identified these limitations when possible. -->
<!-- scope: microscope -->
Human evaluation showed most languages had a high percentage of good summaries in the upper nineties, almost none of the summaries contained any conflicting information, while about one-third on average had information that was not directly inferrable from the source article. Since generally multiple articles are written regarding an important event, there could be an overlap between the training and evaluation data in terms on content. 


#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
The dataset is limited to news domain only. Hence it wouldn't be advisable to use a model trained on this dataset for summarizing texts from a different domain i.e. literature, scientific text etc. Another pitfall could be hallucinations in the model generated summary. 

#### Discouraged Use Cases

<!-- info: What are some discouraged use cases of a model trained to maximize the proposed metrics on this dataset? In particular, think about settings where decisions made by a model that performs reasonably well on the metric my still have strong negative consequences for user or members of the public. -->
<!-- scope: microscope -->
ROUGE evaluates the quality of the summary as a whole by considering up to 4-gram overlaps. Therefore, in an article about India if the word "India" in the generated summary gets replaced by "Pakistan" due to model hallucination, the overall score wouldn't be reduced significantly, but the entire meaning could get changed.


