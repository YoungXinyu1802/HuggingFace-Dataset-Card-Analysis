---
annotations_creators:
- machine-generated
- expert-generated
language:
- id
language_creators:
- machine-generated
- expert-generated
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: IDK-MRC
size_categories:
- 1K<n<10K
source_datasets:
- extended|tydiqa
tags: []
task_categories:
- question-answering
task_ids:
- extractive-qa
---

# Dataset Card for IDK-MRC

## Dataset Description

- **Repository:** [rifkiaputri/IDK-MRC](https://github.com/rifkiaputri/IDK-MRC)
- **Paper:** [arXiv](https://arxiv.org/abs/2210.13778)
- **Point of Contact:** [rifkiaputri](https://github.com/rifkiaputri)

### Dataset Summary

I(n)dontKnow-MRC (IDK-MRC) is an Indonesian Machine Reading Comprehension dataset that covers answerable and unanswerable questions. Based on the combination of the existing answerable questions in TyDiQA, the new unanswerable question in IDK-MRC is generated using a question generation model and human-written question. Each paragraph in the dataset has a set of answerable and unanswerable questions with the corresponding answer.

### Supported Tasks

IDK-MRC is mainly intended to train Machine Reading Comprehension or extractive QA models.

### Languages

Indonesian

## Dataset Structure

### Data Instances

```
{
        "context": "Para ilmuwan menduga bahwa megalodon terlihat seperti hiu putih yang lebih kekar, walaupun hiu ini juga mungkin tampak seperti hiu raksasa (Cetorhinus maximus) atau hiu harimau-pasir (Carcharias taurus). Hewan ini dianggap sebagai salah satu predator terbesar dan terkuat yang pernah ada, dan fosil-fosilnya sendiri menunjukkan bahwa panjang maksimal hiu raksasa ini mencapai 18 m, sementara rata-rata panjangnya berkisar pada angka 10,5 m. Rahangnya yang besar memiliki kekuatan gigitan antara 110.000 hingga 180.000 newton. Gigi mereka tebal dan kuat, dan telah berevolusi untuk menangkap mangsa dan meremukkan tulang.",
        "qas":
        [
            {
                "id": "indonesian--6040202845759439489-1",
                "is_impossible": false,
                "question": "Apakah jenis hiu terbesar di dunia ?",
                "answers":
                [
                    {
                        "text": "megalodon",
                        "answer_start": 27
                    }
                ]
            },
            {
                "id": "indonesian-0426116372962619813-unans-h-2",
                "is_impossible": true,
                "question": "Apakah jenis hiu terkecil di dunia?",
                "answers":
                []
            },
            {
                "id": "indonesian-2493757035872656854-unans-h-2",
                "is_impossible": true,
                "question": "Apakah jenis hiu betina terbesar di dunia?",
                "answers":
                []
            }
        ]
    }
```

### Data Fields

Each instance has several fields:

- `context`: context passage/paragraph as a string
- `qas`: list of questions related to the `context`
  - `id`: question ID as a string
  - `is_impossible`: whether the question is unanswerable (impossible to answer) or not as a boolean
  - `question`: question as a string
  - `answers`: list of answers
    - `text`: answer as a string
    - `answer_start`: answer start index as an integer

### Data Splits

- `train`: 9,332 (5,042 answerable, 4,290 unanswerable)
- `valid`: 764 (382 answerable, 382 unanswerable)
- `test`: 844 (422 answerable, 422 unanswerable)

## Dataset Creation

### Curation Rationale

IDK-MRC dataset is built based on the existing paragraph and answerable questions (ans) in TyDiQA-GoldP (Clark et al., 2020). The new unanswerable questions are automatically generated using the combination of mT5 (Xue et al., 2021) and XLM-R (Conneau et al., 2020) models, which are then manually verified by human annotators (filtered ans and filtered unans). We also asked the annotators to manually write additional unanswerable questions as described in §3.3 (additional unans). Each paragraphs in the final dataset will have a set of filtered ans, filtered unans, and additional unans questions.

### Annotations

#### Annotation process

In our dataset collection pipeline, the annotators are asked to validate the model-generated unanswerable questions and write a new additional unanswerable questions.

#### Who are the annotators?

We recruit four annotators with 2+ years of experience in Indonesian NLP annotation using direct recruitment. All of them are Indonesian native speakers who reside in Indonesia (Java Island) and fall under the 18–34 age category. We set the payment to around $7.5 per hour. Given the annotators’ demographic, we ensure that the payment is above the minimum wage rate (as of December 2021). All annotators also have signed the consent form and agreed to participate in this project.

## Considerations for Using the Data

The paragraphs and answerable questions that we utilized to build IDK-MRC dataset are taken from Indonesian subset of TyDiQA-GoldP dataset (Clark et al., 2020), which originates from Wikipedia articles. Since those articles are written from a neutral point of view, the risk of harmful content is minimal. Also, all model-generated questions in our dataset have been validated by human annotators to eliminate the risk of harmful questions. During the manual question generation process, the annotators are also encouraged to avoid producing possibly offensive questions.

Even so, we argue that further assessment is needed before using our dataset and models in real-world applications. This measurement is especially required for the pre-trained language models used in our experiments, namely mT5 (Xue et al., 2021), IndoBERT (Wilie et al., 2020), mBERT (Devlin et al., 2019), and XLM-R (Conneau et al., 2020). These language models are mostly pre-trained on the common-crawl dataset, which may contain harmful biases or stereotypes.

## Additional Information

### Licensing Information

CC BY-SA 4.0

### Citation Information

```bibtex
@misc{putri2022idk,
    doi = {10.48550/ARXIV.2210.13778},
    url = {https://arxiv.org/abs/2210.13778},
    author = {Putri, Rifki Afina and Oh, Alice},
    title = {IDK-MRC: Unanswerable Questions for Indonesian Machine Reading Comprehension},
    publisher = {arXiv},
    year = {2022},
}
```

