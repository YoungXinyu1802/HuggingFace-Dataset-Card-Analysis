---
annotations_creators:
- expert-generated
language:
- en
- zh
- de
language_creators:
- crowdsourced
license:
- cc-by-nc-sa-4.0
multilinguality:
- multilingual
pretty_name: xmediasum
size_categories:
- 10K<n<100K
source_datasets:
- original
tags: []
task_categories:
- summarization
task_ids: []
---

# Dataset Card for XMediaSum


### Dataset Summary

We present XMediaSum, a cross-lingual dialogue summarization dataset with 40K English(dialogues)->Chinese(summaries) and 40K English (dialogues)->German(summaries) samples. XMediaSum is created by manually translating the English summaries of MediaSum (a English monolingual dialogue summarization dataset) to both Chinese and German.

- Paper: [ClidSum: A Benchmark Dataset for Cross-Lingual Dialogue Summarization](https://aclanthology.org/2022.emnlp-main.526/) (EMNLP 2022)
- GitHub: https://github.com/krystalan/ClidSum

### Supported Task

- Cross-Lingual Summarization
- Cross-Lingual Dialogue Summarization

### Languages

- source language: English
- target language: Chinese and German

## Dataset Structure

### Data Instances
One example is given below in JSON format:
```json
{
    "dialogue": "MADELELEINE BRAND, host: OK, here's some good news on the jobs front for both men and women. A new survey out today from the employment firm Manpower finds that about a quarter of employers will add jobs this summer. That's for adults, but for teenagers this summer's job market is shaping up to be the weakest in more than 50 years.\r\nALEX COHEN, host: So, how do you get your teenage kids not to spend the entire summer glued to the couch? You're about to get some tips from Michelle Singletary. She's Day to Day's personal finance contributor. Hi, Michelle!\r\nMICHELLE SINGLETARY: Hi!\r\nALEX COHEN, host: So why is the summer job market so hard for teens this year?\r\nMICHELLE SINGLETARY: Lot of things going on right now. We've got a tough economy. We've got a lot of college graduates going into the market. We have people who are losing their jobs and taking jobs that would traditionally go to teens, like in restaurants and retailers. And we have a lot of older people holding on to their jobs and not retiring because they can't afford to retire. And that puts teens at the end of the line when it comes to these types of jobs.\r\nALEX COHEN, host: So you've got a teenager at home, a little bit young for the working world just yet, but what would you say to a teenager who's out there hunting around for a job?\r\nMICHELLE SINGLETARY: If you absolutely need a job, keep looking. You know, obviously the types of jobs that teens tend to go for in retail, fast food, you know, they still need people. And oftentimes you know, listen, you may not get the job at the beginning of the summer, but hold on because in late summer, when some of those college students are going back and perhaps some of those people who lost their jobs are finding permanent positions with more pay, you might be able to still get that job. So don't give up, you may spend a month or month and a half without it, but go back to those retailers and those restaurants and those fast food places to see if they still need someone.\r\nALEX COHEN, host: And now I know parents like having the break from providing allowance. But, you know, is - are there reasons maybe not to push your teen towards taking a job?\r\nMICHELLE SINGLETARY: I think it absolutely is. In fact I think too many teens are working and they don't need to work. They're some who absolutely need, they're contributing to their household or they're putting money into their own college fund. But more often than not, what parents do is say you've got to get a job, and then the teens get the job and they spend all the money on clothes and you know videos and iPods and paying their cell phone bills because they don't need a cell phone anyway.\r\nALEX COHEN, host: So it's not going towards the college tuition at all.\r\nMICHELLE SINGLETARY: It is not. It's just disposable income that they're disposing of. And parents are not setting any limits and you know and then the kids get used to the fact that they're using all of their paycheck. That's another bad habit. Because they don't have to pay bills and all, all their income goes through you know this stuff.\r\nMICHELLE SINGLETARY: And when it comes time to get a real job, they're surprised they don't have enough money. And so you know what? You can wait to work. Instead, maybe they can spend the summer volunteering at a charitable organization or you know going back to school and boosting up their math skills or their English skills. We push the teens out into the market too soon, I think for some families.\r\nALEX COHEN, host: But now let's say your kid is working. What tips can parents provide in terms of holding on to that summer money?\r\nMICHELLE SINGLETARY: You know, before they get their job, they need to sit down with them and do a budget. So before they actually work and get that first paycheck I mean, you know, have them draw up a budge where the money is going. And you ought to have some requirements for some of their money. That's right, be a parent.\r\nMICHELLE SINGLETARY: So make them put some of it towards their college fund, if in fact they're headed for college. You know what? Make them put some away, I call it the tax fund, even though they may not have to pay taxes, but to pay for long-term things that they may want. You know, books once they get to college, or maybe they want to get a car, and they can actually pay cash for it, with some of these funds. Don't let them just go out and spend it on movies and stuff. You ought to set some guidelines - this is where you should put the money. And look at their budget.\r\nALEX COHEN, host: Day to Day's personal finance contributor Michelle Singletary. Thank you, Michelle!\r\nMICHELLE SINGLETARY: You're welcome.\r\nALEX COHEN, host: Stay with us. NPR's Day to Day continues.",
    "summary": "The tight job market could be bad news for teens seeking summer work. If your teen does find a job, will he or she know how to manage those paychecks? Our personal finance contributor talks with Alex Cohen about ways to help teens find a job.",
    "summary_de": "Der angespannte Arbeitsmarkt könnte für Jugendliche, die Sommerarbeit suchen, eine schlechte Nachricht sein. Wenn Ihr Teenager einen Job findet, wird er oder sie wissen, wie er mit diesen Gehaltsschecks umgeht? Unser Mitarbeiter für persönliche Finanzen spricht mit Alex Cohen darüber, wie Teenager bei der Jobsuche unterstützt werden können.",
    "summary_zh": "紧张的就业市场对寻找暑期工作的青少年来说可能是个坏消息。如果你的孩子找到了一份工作，他/她懂得怎么管理这些薪水吗？我们的个人理财撰稿人与亚历克斯·科恩谈论如何帮助青少年找到工作。"
},
```


### Data Fields

- 'dialogue': An English dialogue
- 'summary': the original English summary of the corresponding dialogue (provided by MediaSum)
- 'summary_de': the human-translated German summary
- 'summary_zh': the human-translated Chinese summary

### Data Splits
- training set: 20K samples
- validation set: 10K samples
- testing set: 10K samples


## Dataset Creation

Please refer to [our paper](https://aclanthology.org/2022.emnlp-main.526/) for more details.

## Considerations for Using the Data

Please refer to [our paper](https://aclanthology.org/2022.emnlp-main.526/) for more details.

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/krystalan/ClidSum)

### Licensing Information

License: CC BY-NC-SA 4.0

### Citation Information

```
@inproceedings{wang-etal-2022-clidsum,
    title = "{C}lid{S}um: A Benchmark Dataset for Cross-Lingual Dialogue Summarization",
    author = "Wang, Jiaan  and
      Meng, Fandong  and
      Lu, Ziyao  and
      Zheng, Duo  and
      Li, Zhixu  and
      Qu, Jianfeng  and
      Zhou, Jie",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.emnlp-main.526",
    pages = "7716--7729",
    abstract = "We present ClidSum, a benchmark dataset towards building cross-lingual summarization systems on dialogue documents. It consists of 67k+ dialogue documents and 112k+ annotated summaries in different target languages. Based on the proposed ClidSum, we introduce two benchmark settings for supervised and semi-supervised scenarios, respectively. We then build various baseline systems in different paradigms (pipeline and end-to-end) and conduct extensive experiments on ClidSum to provide deeper analyses. Furthermore, we propose mDialBART which extends mBART via further pre-training, where the multiple objectives help the pre-trained model capture the structural characteristics as well as key content in dialogues and the transformation from source to the target language. Experimental results show the superiority of mDialBART, as an end-to-end model, outperforms strong pipeline models on ClidSum. Finally, we discuss specific challenges that current approaches faced with this task and give multiple promising directions for future research. We have released the dataset and code at https://github.com/krystalan/ClidSum.",
}
```

### Contributions

Thanks to [@krystalan](https://github.com/krystalan) for adding this dataset.