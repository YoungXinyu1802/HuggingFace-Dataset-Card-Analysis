---
annotations_creators:
- human
license: cc-by-nc-sa-4.0
task_categories:
- question-answering
task_ids:
- open-domain-qa
- extractive-qa
language:
- bn
size_categories:
- 10K<n<100K
---


# Dataset Card for `BanglaRQA`
## Table of Contents
- [Dataset Card for `BanglaRQA`](#dataset-card-for-BanglaRQA)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Languages](#languages)
    - [Usage](#usage)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
  - [Additional Information](#additional-information)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)


## Dataset Description
- **Repository:** [https://github.com/sartajekram419/BanglaRQA](https://github.com/sartajekram419/BanglaRQA)
- **Paper:** [BanglaRQA: A Benchmark Dataset for Under-resourced Bangla Language Reading Comprehension-based Question Answering with Diverse Question-Answer Types](https://aclanthology.org/2022.findings-emnlp.186)

### Dataset Summary
This is a human-annotated Bangla Question Answering (QA) dataset with diverse question-answer types.

### Languages
* `Bangla`


## Dataset Structure
### Data Instances
One example passage along with its question-answer pairs from the dataset is given below in JSON format. 
  ```
  {
    'passage_id': 'bn_wiki_2977',
    'title': 'ফাজিল পরীক্ষা',
    'context': 'ফাজিল পরীক্ষা বাংলাদেশ ও ভারতের আলিয়া মাদ্রাসায় অনুষ্ঠিত একটি সরকারি পরীক্ষা। ফাজিল পরীক্ষা বাংলাদেশে ডিগ্রি সমমানের, কখনো স্নাতক সমমানের একটি পরীক্ষা, যা একটি ফাজিল মাদ্রাসায় অনুষ্ঠিত হয়ে থাকে। তবে ভারতে ফাজিল পরীক্ষাকে উচ্চ মাধ্যমিক শ্রেণীর (১১ বা ১২ ক্লাস) মান বলে বিবেচিত করা হয়। ফাজিল পরীক্ষা বাংলাদেশ ভারত ও পাকিস্তানের সরকারি স্বীকৃত আলিয়া মাদরাসায় প্রচলিত রয়েছে। বাংলাদেশের ফাজিল পরীক্ষা ইসলামি আরবি বিশ্ববিদ্যালয়ের অধীনে অনুষ্ঠিত হয়ে থাকে ও ভারতের ফাজিল পরীক্ষা পশ্চিমবঙ্গ মাদ্রাসা শিক্ষা পর্ষদের অধীনে অনুষ্ঠিত হয়ে থাকে।\n\n১৯৪৭ সালে ঢাকা আলিয়া মাদ্রাসা ঢাকায় স্থানান্তরের পূর্বে বাংলাদেশ ও ভারতের ফাজিল পরীক্ষা কলকাতা আলিয়া মাদ্রাসার অধীনে অনুষ্ঠিত হতো। ফাযিল পরীক্ষা বর্তমানে ইসলামি আরবী বিশ্ববিদ্যালয়ের অধীনে অনুষ্ঠিত হয়। যা পূর্বে মাদরাসা বোর্ড ও ইসলামি বিশ্ববিদ্যালয়ের আধীনে অনুষ্ঠিত হত। মাদ্রাসা-ই-আলিয়া ঢাকায় স্থানান্তরিত হলে ১৯৪৮ সালে মাদ্রাসা বোর্ডের ফাজিলগুলো পরীক্ষা ঢাকা বিশ্ববিদ্যালয় কর্তৃক গৃহীত হতো। ১৯৭৫ সালের কুদরত-এ-খুদা শিক্ষা কমিশনের সুপারিশে মাদ্রাসা বোর্ড নিয়ন্ত্রিত আলিয়া মাদ্রাসাসমূহে জাতীয় শিক্ষাক্রম ও বহুমুখী পাঠ্যসূচি প্রবর্তিত করা হয়। ১৯৮০ সালে অনুষ্ঠিত ফাজিল পরীক্ষায় এই পাঠ্যসুচী কার্যকর হয়। এই শিক্ষা কমিশন অনুসারে ফাজিল শ্রেণীতে ইসলামি শিক্ষার পাশাপাশি সাধারণ পাঠ্যসূচী অন্তর্ভুক্ত করে ফাজিল পরীক্ষাকে সাধারণ উচ্চ মাধ্যমিক এইচ এস সির সমমান ঘোষণা করা হয়।\n\n১৯৭৮ সালে অধ্যাপক মুস্তফা বিন কাসিমের নেতৃত্বে সিনিয়র মাদ্রাসা শিক্ষা ব্যবস্থা কমিটি গঠিত হয়। এই কমিটির নির্দেশনায় ১৯৮৪ সালে সাধারণ শিক্ষার স্তরের সঙ্গে বাংলাদেশ মাদ্রাসা বোর্ড নিয়ন্ত্রিত আলিয়া মাদ্রাসা শিক্ষা স্তরের সামঞ্জস্য করা হয়। ফাজিল স্তরকে ২ বছর মেয়াদী কোর্সে উন্নিত করে, মোট ১৬ বছর ব্যাপী আলিয়া মাদ্রাসার পূর্ণাঙ্গ আধুনিক শিক্ষা ব্যবস্থা প্রবর্তন করা হয়। এই কমিশনের মাধ্যমেই সরকার ফাজিল পরীক্ষাকে সাধারণ ডিগ্রি মান ঘোষণা করে।',
    'qas': [
            {
              'question_id': 'bn_wiki_2977_01',
              'question_text': 'ফাজিল পরীক্ষা বাংলাদেশ ও ভারতের আলিয়া মাদ্রাসায় অনুষ্ঠিত একটি সরকারি পরীক্ষা ?',
              'is_answerable': '1',
              'question_type': 'confirmation',
              'answers': {'answer_text': ['হ্যাঁ', 'হ্যাঁ '], 'answer_type': ['yes/no', 'yes/no']}
            },
            {
              'question_id': 'bn_wiki_2977_02',
              'question_text': ' বাংলাদেশের ফাজিল পরীক্ষা ইসলামি আরবি বিশ্ববিদ্যালয়ের অধীনে অনুষ্ঠিত হয়ে থাকে কেন ?',
              'is_answerable': '0',
              'question_type': 'causal',
              'answers': {'answer_text': ['', ''], 'answer_type': ['', '']}
            },
            {
              'question_id': 'bn_wiki_2977_03',
              'question_text': 'কত সালে ঢাকা আলিয়া মাদ্রাসা ঢাকায় স্থানান্তরের পূর্বে বাংলাদেশ ও ভারতের ফাজিল পরীক্ষা কলকাতা আলিয়া মাদ্রাসার অধীনে অনুষ্ঠিত হতো ?',
              'is_answerable': '1',
              'question_type': 'factoid',
              'answers': {'answer_text': ['১৯৪৭', '১৯৪৭'], 'answer_type': ['single span', 'single span']}
            },
            {
              'question_id': 'bn_wiki_2977_04',
              'question_text': 'মাদ্রাসা-ই-আলিয়া ঢাকায় স্থানান্তরিত হলে কত সালে মাদ্রাসা বোর্ডের ফাজিলগুলো পরীক্ষা ঢাকা বিশ্ববিদ্যালয় কর্তৃক গৃহীত হতো ?',
              'is_answerable': '1',
              'question_type': 'factoid',
              'answers': {'answer_text': ['১৯৪৮', '১৯৪৮'], 'answer_type': ['single span', 'single span']}
            },
            {
              'question_id': 'bn_wiki_2977_05',
              'question_text': 'মোট কত বছর ব্যাপী আলিয়া মাদ্রাসার পূর্ণাঙ্গ আধুনিক শিক্ষা ব্যবস্থা প্রবর্তন করা হয় ?',
              'is_answerable': '1',
              'question_type': 'factoid',
              'answers': {'answer_text': ['১৬', '১৬'], 'answer_type': ['single span', 'single span']}
            }
    ]
  }
  ```


### Data Splits
|   split   |count  |
|----------|--------|
|`train`|  11,912 |
|`validation`| 1,484  |
|`test`| 1,493 |

 

## Additional Information

### Licensing Information

Contents of this repository are restricted to only non-commercial research purposes under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). Copyright of the dataset contents belongs to the original copyright holders.
### Citation Information

If you use the dataset, please cite the following paper:
```
@inproceedings{ekram-etal-2022-banglarqa,
    title = "{B}angla{RQA}: A Benchmark Dataset for Under-resourced {B}angla Language Reading Comprehension-based Question Answering with Diverse Question-Answer Types",
    author = "Ekram, Syed Mohammed Sartaj  and
      Rahman, Adham Arik  and
      Altaf, Md. Sajid  and
      Islam, Mohammed Saidul  and
      Rahman, Mehrab Mustafy  and
      Rahman, Md Mezbaur  and
      Hossain, Md Azam  and
      Kamal, Abu Raihan Mostofa",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2022",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-emnlp.186",
    pages = "2518--2532",
    abstract = "High-resource languages, such as English, have access to a plethora of datasets with various question-answer types resembling real-world reading comprehension. However, there is a severe lack of diverse and comprehensive question-answering datasets in under-resourced languages like Bangla. The ones available are either translated versions of English datasets with a niche answer format or created by human annotations focusing on a specific domain, question type, or answer type. To address these limitations, this paper introduces BanglaRQA, a reading comprehension-based Bangla question-answering dataset with various question-answer types. BanglaRQA consists of 3,000 context passages and 14,889 question-answer pairs created from those passages. The dataset comprises answerable and unanswerable questions covering four unique categories of questions and three types of answers. In addition, this paper also implemented four different Transformer models for question-answering on the proposed dataset. The best-performing model achieved an overall 62.42{\%} EM and 78.11{\%} F1 score. However, detailed analyses showed that the performance varies across question-answer types, leaving room for substantial improvement of the model performance. Furthermore, we demonstrated the effectiveness of BanglaRQA as a training resource by showing strong results on the bn{\_}squad dataset. Therefore, BanglaRQA has the potential to contribute to the advancement of future research by enhancing the capability of language models. The dataset and codes are available at https://github.com/sartajekram419/BanglaRQA",
}

```
