---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- as
- bn
- gu
- hi
- kn
- ml
- mr
- or
- pa
- ta
- te
license:
- cc-by-nc-4.0
multilinguality:
- multilingual
pretty_name: IndicHeadlineGeneration
size_categories:
- 27K<n<341K
source_datasets:
- original for Hindi, and modified [IndicGLUE](https://indicnlp.ai4bharat.org/indic-glue/) for other languages.
task_categories:
- conditional-text-generation
task_ids:
- conditional-text-generation-other-headline-generation
---

# Dataset Card for "IndicHeadlineGeneration"

## Table of Contents
- [Dataset Card Creation Guide](#dataset-card-creation-guide)
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
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
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

- **Homepage:** https://indicnlp.ai4bharat.org/indicnlg-suite
- **Paper:** [IndicNLG Suite: Multilingual Datasets for Diverse NLG Tasks in Indic Languages](https://arxiv.org/abs/2203.05437)
- **Point of Contact:** 

### Dataset Summary

IndicHeadlineGeneration is the news headline generation dataset released as part of IndicNLG Suite. Each 
input document is paired with an output as title. We create this dataset in eleven 
languages including as, bn, gu, hi, kn, ml, mr, or, pa, ta, te. The total
size of the dataset is 1.4M. 


### Supported Tasks and Leaderboards

**Tasks:** Headline Generation

**Leaderboards:** Currently there is no Leaderboard for this dataset.

### Languages
-  `Assamese (as)`
-  `Bengali (bn)`
-  `Gujarati (gu)`
-  `Kannada (kn)`
-  `Hindi (hi)`
-  `Malayalam (ml)`
-  `Marathi (mr)`
-  `Oriya (or)`
-  `Punjabi (pa)`
-  `Tamil (ta)`
-  `Telugu (te)`

## Dataset Structure

### Data Instances

One random example from the `hi` dataset is given below in JSON format. 
  ```
  {'id': '14',
 'input': "अमेरिकी सिंगर अरियाना ग्रांडे का नया म्यूजिक एल्बम 'थैंक यू नेक्स्ट' रिलीज हो गया है।एक दिन पहले ही रिलीज हुए इस गाने को देखने वालों की संख्या 37,663,702 पहुंच गई है।यूट्यूब पर अपलोड इस गाने को 24 घंटे के भीतर 3.8 मिलियन लोगों ने पसंद किया है।अरियाना ग्रांडे नई दिल्लीः अमेरिकी सिंगर अरियाना ग्रांडे का नया म्यूजिक एल्बम 'थैंक यू नेक्स्ट' रिलीज हो गया है।एक दिन पहले ही रिलीज हुए इस गाने को देखने वालों की संख्या 37,663,702 पहुंच गई है।यूट्यूब पर अपलोड इस गाने को 24 घंटे के भीतर 3.8 मिलियन लोगों ने पसंद किया है।वहीं इस वीडियो पर कमेंट्स की बाढ़ आ गई है।गाने में मीन गर्ल्स, ब्रिंग इट ऑन, लीगली ब्लॉंड और 13 गोइंग 30 के कुछ फेमस सीन्स को दिखाया गया है।गाने में क्रिस जैनर का कैमियो भी है।बता दें अभी कुछ महीने पहले ही अरियाना के एक्स ब्वॉयफ्रेंड मैक मिलर का 26 साल की उम्र में निधन हो गया था।इस खबर को सुनकर अरियाना टूट सी गई थीं।उन्होंने सोशल मीडिया पर पोस्ट कर कई बार अपनी भावनाएं व्यक्त की।अरियाना ग्रांडे और रैपर मैक मिलर ने करीब 2 साल तक एक दूसरे को डेट किया।मैक के निधन की वजह ड्रग्स की ओवरडोज बताई गई।दोनों की मुलाकात साल 2012 में हुई थी।दोनों ने एक कंसर्ट में साथ कई गानों पर परफॉर्म भी किया था।जिसके बाद दोनों एक दूसरे को डेट करने लगे लेकिन नशे की लत के कारण अरियाना ने उनसे ब्रेकअप कर लिया।पर देश-विदेश की ताजा और स्पेशल स्टोरी पढ़ते हुए अपने आप को रखिए अप-टू-डेट।के लिए क्लिक करें सिनेमा सेक्शन",
 'target': 'अरियाना ग्रांडे का नया गाना रिलीज, सोशल मीडिया पर वायरल',
 'url': 'https://www.indiatv.in/entertainment/hollywood-ariana-grande-shatters-24-hour-views-record-612835'
}
  ```

### Data Fields
-  `id (string)`: Unique identifier.
-  `input (string)`: News article as input.
-  `target (strings)`: Output as headline of the news article.
-  `url (string)`: Source web link of the news article. 


### Data Splits

Here is the number of samples in each split for all the languages.




Language	|	ISO 639-1 Code	|	Train	|	Dev	|	Test	|
----------	|	----------	|	----------	|	----------	|	----------	|
Assamese	|	as	|	29,631	|	14,592	|	14,808	|
Bengali	|	bn	|	113,424	|	14,739	|	14,568	|
Gujarati	|	gu	|	199,972	|	31,270	|	31,215	|
Hindi	|	hi	|	208,221	|	44,738	|	44,514	|
Kannada	|	kn	|	132,380	|	19,416	|	3,261	|
Malayalam	|	ml	|	10,358	|	5,388	|	5,220	|
Marathi	|	mr 	|	114,042	|	14,253	|	14,340	|
Oriya	|	or	|	58,225	|	7,484	|	7,137	|
Punjabi	|	pa 	|	48,441	|	6,108	|	6,086	|
Tamil	|	ta 	|	60,650	|	7,616	|	7,688	|
Telugu	|	te 	|	21,352	|	2,690	|	2,675	|


## Dataset Creation

### Curation Rationale

[Detailed in the paper](https://arxiv.org/abs/2203.05437)

### Source Data

For hindi, web sources like  [Dainik Bhaskar](https://www.bhaskar.com), [Naidunia](https://www.naidunia.com/), [NDTV](https://ndtv.in/), [Business Standard](https://hindi.business-standard.com/) and [IndiaTV](https://www.indiatv.in/). For other languages, modified [IndicGLUE](https://indicnlp.ai4bharat.org/indic-glue/) dataset.

#### Initial Data Collection and Normalization

[Detailed in the paper](https://arxiv.org/abs/2203.05437)


#### Who are the source language producers?

[Detailed in the paper](https://arxiv.org/abs/2203.05437)


### Annotations
[More information needed]
#### Annotation process
[More information needed]

#### Who are the annotators?

[More information needed]

### Personal and Sensitive Information

[More information needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More information needed]

### Discussion of Biases

[More information needed]

### Other Known Limitations

[More information needed]

## Additional Information

### Dataset Curators

[More information needed]

### Licensing Information

Contents of this repository are restricted to only non-commercial research purposes under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/). Copyright of the dataset contents belongs to the original copyright holders.
### Citation Information

If you use any of the datasets, models or code modules, please cite the following paper:
```
@inproceedings{Kumar2022IndicNLGSM,
  title={IndicNLG Suite: Multilingual Datasets for Diverse NLG Tasks in Indic Languages},
  author={Aman Kumar and Himani Shrotriya and Prachi Sahu and Raj Dabre and Ratish Puduppully and Anoop Kunchukuttan and Amogh Mishra and Mitesh M. Khapra and Pratyush Kumar},
  year={2022},
  url = "https://arxiv.org/abs/2203.05437",     
```


### Contributions

[Detailed in the paper](https://arxiv.org/abs/2203.05437)