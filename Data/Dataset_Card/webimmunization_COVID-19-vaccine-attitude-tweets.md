---
annotations_creators:
- crowdsourced
language_creators:
- other
language:
- en
license: [cc-by-4.0]
multilinguality:
- monolingual
pretty_name: twitter covid19 tweets
size_categories:
- 54KB
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- sentiment-classification
- intent-classification
---
# Dataset Card for COVID-19-vaccine-attitude-tweets
## Dataset Description

- **Paper:** [Be Careful Who You Follow. The Impact of the Initial Set of Friends on COVID-19 Vaccine tweets](https://www.researchgate.net/publication/355726080_Be_Careful_Who_You_Follow_The_Impact_of_the_Initial_Set_of_Friends_on_COVID-19_Vaccine_Tweets)
- **Point of Contact:** [Izabela Krysinska](izabela.krysinska@doctorate.put.poznan.pl)

### Dataset Summary

The dataset consists of 2564 manually annotated tweets related to COVID-19 vaccines. The dataset can be used to discover the attitude expressed in the tweet towards the subject of COVID-19 vaccines. Tweets are in English. The dataset was curated in such a way as to maximize the likelihood of tweets with a strong emotional tone. We have assumed the existence of three classes:

- PRO (label 0): positive, the tweet unequivocally suggests support for getting vaccinated against COVID-19
- NEUTRAL (label 1): the tweet is mostly informative, does not show emotions vs. presented information, contains strong positive or negative emotions but concerning politics (vaccine distribution, vaccine passports, etc.)
- AGAINST (label 2): the tweet is clearly against vaccination and contains warnings, conspiracy theories, etc.


The dataset does not contain the content of Twitter statuses. Original tweets can be obtained via Twitter API.
You can use [`twitter`](https://python-twitter.readthedocs.io/en/latest/index.html) library: 

```python
import twitter
from datasets import load_dataset

api = twitter.Api(consumer_key=<consumer key>,
                  consumer_secret=<consumer secret>,
                  access_token_key=<access token>,
                  access_token_secret=<access token secret>,
                  sleep_on_rate_limit=True)

tweets = load_dataset('webimmunization/COVID-19-vaccine-attitude-tweets') 

def add_tweet_content(example):
    try:
        status = api.GetStatus(tweet_id)
    except twitter.TwitterError as err:
        print(err)
        status = {'text': None}
    return {'status': status.text}

tweets_with_text = tweets.map(add_tweet_content)

```


### Supported Tasks and Leaderboards

- `text-classification`: The dataset can be used to discover the attitude expressed in the tweet towards the subject of COVID-19 vaccines, whether the tweet presents a positive, neutral or negative attitude. Success on this task can be measured by achieving a *high* AUROC or [F1](https://huggingface.co/metrics/f1). 

### Languages
[EN] English.
The text that can be accessed via the Twitter API using the identifiers in this dataset is in English.

## Dataset Structure

### Data Instances
The 1st column is Twitter Status ID and the 2nd column is the label denoting the attitude towards vaccines against COVID-19.
Example:

```
{
  'id': '1387627601955545089',
  'attitude': 0  # positive attitude
}
```


### Data Fields


- `attitude`: attitude towards vaccines against COVID-19. `0` denotes positive attitude, `1` denotes neutral attitude, `2` dentoes negative attitude.

- `id`: Twitter status id


### Data Splits
[Needs More Information]

## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

Social media posts.

#### Initial Data Collection and Normalization

We queried the Twitter search engine with manually curated hashtags such as \#coronavaccine, \#getvaccinated, #mRNA, #PfizerGang, #VaccineNoThankYou, #vaccinesWork, #BillGatesVaccine, #VaccinesKill, etc. to fetch tweets related to COVID-19 vaccines. Then we have searched for tweets with conspicuous emotional load, both negative and positive. Once we had the set of emotionally loaded tweets we started fetching other tweets posted by the authors of emotional tweets. We'd been collecting tweets from mid of April for about a month. Then we filtered out tweets that were not related to the vaccines. In this manner, we collected tweets that are more probable to be emotional rather than strictly informative.


#### Who are the source language producers?
The language producers are users of Twitter.

### Annotations

#### Annotation process

We have manually annotated over 2500 tweets using the following annotation protocol. We have assumed the existence of three classes:

- PRO (label 0): positive, the tweet unequivocally suggests support for getting vaccinated against COVID-19
- NEUTRAL(label 1): the tweet is mostly informative, does not show emotions vs. presented information, contains strong positive or negative emotions but concerning politics (vaccine distribution, vaccine passports, etc.)
- AGAINST(label 2): the tweet is clearly against vaccination and contains warnings, conspiracy theories, etc.


The PRO class consists of tweets which explicitly urge people to go get vaccinated. The AGAINST class contains tweets which explicitly warn people against getting the vaccine.

Tweet annotation has been conducted using [Prodigy](https://prodi.gy) tool. The annotators were provided with the following instructions:

- Do not spend too much time on a tweet and try to make a quick decision, the slight discrepancy in labeling (especially if you are deciding between *PRO* and *NEUTRAL*) will not affect the classifier significantly.
- Assign tweets that seem to originate from news sites as *NEUTRAL* and use *PRO* for tweets that express unequivocal support for getting the vaccine.
- There are many tweets on vaccination and politics. They should fall into the *NEUTRAL* class unless they contain a clear call to action: go get vaccinated!
- Use only the contents of the tweet to label it, do not open the links if the content of a tweet is not enough for labeling (e.g., “Hmm, interesting, https://t.co/ki345o2i345”), skip such tweets instead of giving it a label.
 - Use the option to skip a tweet only when there is nothing in the tweet except for an URL or a few meaningless words, otherwise do not hesitate to put the tweet in the *NEUTRAL* class.


We have asked 8 annotators to annotate the same set of 100 tweets using the guidelines proposed in the annotation protocol to verify the annotation protocol. We have measured the interrater agreement using the Fliess' kappa coefficient <cite>[Fleiss 1971][2]</cite>. The results were as follows:
- when measuring the agreement with four possible classes (*PRO*, *NEUTRAL*, *AGAINST*, *NONE*, where the last class represents tweets that were rejected from annotation), the agreement is `kappa=0.3940`
- when measuring the agreement after removing tweets that were rejected, the agreement is `kappa=0.3560`
- when measuring the agreement if rejected tweets are classified as *NEUTRAL*, the agreement is `kappa=0.3753`
- when measuring the agreement for only two classes (using *PRO*, *NEUTRAL* and *NONE* as one class, and *AGAINST* as another class), the agreement is `kappa=0.5419`

#### Who are the annotators?
[Members of the #WebImmunization project](https://webimmunization.cm-uj.krakow.pl/en/team/)

### Personal and Sensitive Information

According to the Twitter developer policy, if displayed content ceases to be available through the Twitter API, it can not be obtained from other sources. Thus, we provide tweets' ids to maintain the integrity of all Twitter content with Twitter service. The proper way to extract tweets' content is via Twitter API. Whenever Twitter decided to suspend the author of the tweet, or the author decides to delete their tweet it won't be possible to obtain the tweet's content with this dataset.


## Considerations for Using the Data

### Social Impact of Dataset

The COVID-19 is a serious global health threat that can be mitigated only by public health interventions that require massive participation. Mass vaccination against COVID-19 is one of the most effective and economically promising solutions to stop the spread of the Sars-Cov-2 virus, which is responsible for the pandemic. Understanding how misinformation about COVID-19 vaccines is spreading in one of the globally most important social networks is paramount.

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

#### Interannotator agreement
According to a popular interpretation of Fleiss' kappa <cite>[Landis 1977][2]</cite>, the annotators are in fair agreement in the first three scenarios and moderate agreement in the last scenario. These results suggest that the annotators are struggling to distinguish between *PRO* and *NEUTRAL* classes, and sometimes they have divergent opinions on whether the tweet should be rejected from training. Still, they are coherent when labeling *AGAINST* tweets.

#### Suspended account & deleted tweets
Some of the statuses from the dataset can not be obtained due to account suspension or tweet deletion. The last time we check (15th of November, 2021), about 12% of tweets were authored by suspended accounts and about 10% were already deleted.


### Dataset Curators

Agata Olejniuk
Poznan University of Technology, Poland

The research leading to these results has received funding from the EEA Financial Mechanism 2014-2021. Project registration number: 2019/35/J/HS6 /03498.

### Licensing Information

[Needs More Information]

### Citation Information

```
@inproceedings{krysinska2021careful,
  title={Be Careful Who You Follow: The Impact of the Initial Set of Friends on COVID-19 Vaccine Tweets},
  author={Krysi{\'n}ska, Izabela and W{\'o}jtowicz, Tomi and Olejniuk, Agata and Morzy, Miko{\l}aj and Piasecki, Jan},
  booktitle={Proceedings of the 2021 Workshop on Open Challenges in Online Social Networks},
  pages={1--8},
  year={2021}
}
```

[DOI](https://doi.org/10.1145/3472720.3483619)

### Contributions

We would like to cordially thank the [members of the #WebImmunization project](https://webimmunization.cm-uj.krakow.pl/en/team/)  for helping with data annotation.


## References

[1]: Joseph L Fleiss. Measuring nominal scale agreement among many raters.Psychological bulletin, 76(5):378, 1971.

[2]: J Richard Landis and Gary G Koch. The measurement of observer agreement for categorical data. biometrics, pages 159–174, 1977.