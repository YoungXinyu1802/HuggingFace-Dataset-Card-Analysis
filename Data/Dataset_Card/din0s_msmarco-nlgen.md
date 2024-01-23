---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- crowdsourced
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: MSMARCO NLGEN
size_categories:
- 100K<n<1M
source_datasets:
- extended|ms_marco
tags:
- msmarco
- natural language generation
- question answering
task_categories:
- question-answering
task_ids:
- open-domain-qa
---

# Dataset Card for MSMARCO - Natural Language Generation Task

## Table of Contents
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
  - [Annotations](#annotations)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://microsoft.github.io/msmarco/
- **Repository:** https://github.com/microsoft/MSMARCO-Question-Answering
- **Paper:** https://arxiv.org/abs/1611.09268
- **Leaderboard:** https://microsoft.github.io/msmarco#qnadataset

### Dataset Summary

The original focus of MSMARCO was to provide a corpus for training and testing systems which given a real domain user query systems would then provide the most likley candidate answer and do so in language which was natural and conversational. All questions have been generated from real anonymized Bing user queries which grounds the dataset in a real world problem and can provide researchers real contrainsts their models might be used in. The context passages, from which the answers in the dataset are derived, are extracted from real web documents using the most advanced version of the Bing search engine. The answers to the queries are human generated.

### Supported Tasks and Leaderboards

Question Answering & Natural Language Generation. [Leaderboard](https://microsoft.github.io/msmarco#qnadataset)

### Languages

- English

## Dataset Structure

### Data Instances

```py
{

   "query_id":604568,
   "query":"what county is columbus city in",
   "passages":[
      {
         "is_selected":0,
         "passage_text":"WELCOME TO COLUMBUS! The City of Columbus includes a mix of residential, rural and commercial property. Columbus boasts large tracts of public land, including Carlos Avery Wildlife Management Area and Lamprey Pass.",
         "url":"http://www.ci.columbus.mn.us/"
      },
      {
         "is_selected":0,
         "passage_text":"The ratio of number of residents in Columbus to the number of sex offenders is 488 to 1. The number of registered sex offenders compared to the number of residents in this city is near the state average. Nearest city with pop. 50,000+: Bloomington, IN (33.3 miles , pop. 69,291).",
         "url":"http://www.city-data.com/city/Columbus-Indiana.html"
      },
      {
         "is_selected":0,
         "passage_text":"Phone Number: Columbus-Muscogee, the first consolidated city-county in Georgia, began development in 1826, building on ceded Creek Indian territory. Muscogee is the name of a branch of the Creek Nation. Columbus, of course, is named for Christopher Columbus.",
         "url":"https://georgia.gov/cities-counties/columbus-muscogee-county"
      },
      {
         "is_selected":1,
         "passage_text":"Sponsored Topics. Columbus ( /kəlʌmbəs/) is a city in and the county seat of Bartholomew County, Indiana, United States. The population was 44,061 at the 2010 census, and the current mayor is Fred Armstrong. Located approximately 40 miles (64 km) south of Indianapolis, on the east fork of the White River, it is the state's 20th largest city.",
         "url":"https://www.mapquest.com/us/in/columbus-282032817"
      },
      {
         "is_selected":0,
         "passage_text":"Columbus, Ohio. Columbus (/kəˈlʌmbəs/; kə-LUM-bəs) is the capital and largest city of the U.S. state of Ohio. It is the 15th-largest city in the United States, with a population of 850,106 as of 2015 estimates. This makes Columbus the fourth-most populous state capital in the United States, and the third-largest city in the Midwestern United States.",
         "url":"https://en.wikipedia.org/wiki/Columbus,_Ohio"
      },
      {
         "is_selected":0,
         "passage_text":"Phone Number: Columbus-Muscogee, the first consolidated city-county in Georgia, began development in 1826, building on ceded Creek Indian territory. Muscogee is the name of a branch of the Creek Nation. Columbus, of course, is named for Christopher Columbus.",
         "url":"https://georgia.gov/cities-counties/columbus"
      },
      {
         "is_selected":0,
         "passage_text":"Latest news from Columbus, IN collected exclusively by city-data.com from local newspapers, TV, and radio stations. Ancestries: American (30.5%), German (13.7%), English (7.7%), Irish (5.3%), European (2.4%), Scottish (1.2%).",
         "url":"http://www.city-data.com/city/Columbus-Indiana.html"
      },
      {
         "is_selected":0,
         "passage_text":"Columbus, Indiana. 1  Columbus: covered Bridge at Mill Race Park. 2  Columbus: A statue in cloumbus. 3  Columbus. Columbus: Bartholomew County Courthouse.  Columbus: Tipton Lakes - A wonderful planned 1  community! Columbus: Barthalomew county memorial for veterans.  Columbus: A sculpter called summer storm in 1  columbus. Columbus: Downtown Columbus.",
         "url":"http://www.city-data.com/city/Columbus-Indiana.html"
      },
      {
         "is_selected":0,
         "passage_text":"The City owns and operates a volunteer fire department through a joint powers agreement with the City of Forest Lake. Police protection is provided through a contract with the Anoka County Sheriff’s Department. Columbus is located within the Forest Lake Area School District (ISD #831).",
         "url":"http://www.ci.columbus.mn.us/"
      },
      {
         "is_selected":0,
         "passage_text":"Acceptable ID for children: State ID, Birth Certificate, or Health Insurance Card. Effective June 27, 2016, the Franklin County Sheriff's Office will be implementing changes to ensure the safety of inmates, staff, and visitors. Printed materials (magazines, books, pamphlets, leaflets, or catalogues) MUST fit all the below criteria:",
         "url":"https://sheriff.franklincountyohio.gov/services/inmate-information.cfm"
      }
   ],
   "query_type":"LOCATION",
   "answers":[
      "Columbus is a city in Bartholomew County."
   ]
}
```

### Data Fields

- `query_id`: a unique id for each query that is used in evaluation
- `query`: a unique query based on initial Bing usage
- `passages`: a list of 10 passages (`passage_text`), URLs (`url`), and an annotation if they were used to formulate the answer (`is_selected`)
- `query_type`: a basic division of queries based on a trained classifier (`LOCATION`,`NUMERIC`,`PERSON`,`DESCRIPTION`,`ENTITY`)
- `answers`: a list of "well-formed" answers generated by human annotators using  natural language

### Data Splits

| **Split** | **Instances** |
|-----------|---------------|
| Train     | 153725        |
| Dev       | 12467         |

## Dataset Creation

### Curation Rationale

What is the differences between MSMARCO and other MRC datasets?

- Real questions: All questions have been sampled from real anonymized bing queries.
- Real Documents: Most of the URLs that the passages were sourced from contain the full web documents (passages).
- Human Generated Well-Formed Answers: All questions have an answer written by a human in natural language.

### Annotations

#### Annotation process

The MSMARCO dataset is generated by a well oiled pipeline optimized for the highest quality examples. The general process runs as follows:

1. Bing logs are sampled, filtered and anonymized to make sure the queries are both useful to the research community and respectful to bing users and fans.
2. Using the sampled and anonymized queries Bing generates the 10 most relevant passages for the query.
3. Highly trained judges read the query and its related passages and if there is an answer present, the supporting passages are annotated and a natural language answer is generated.
4. A smaller proportion of queries(~17% of overall dataset with 182,887 unique queries) are then passed on to a second round of judges who are asked to verify the answer is correct and rewrite(if possible) the query to be a well formed answer. These answers are designed to be understood without perfect context and are designed with smart speakers/digital assistants in mind.

## Additional Information

### Licensing Information

MS MARCO is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

### Citation Information

```
@inproceedings{Bajaj2016Msmarco,
  title={MS MARCO: A Human Generated MAchine Reading COmprehension Dataset},
  author={Payal Bajaj, Daniel Campos, Nick Craswell, Li Deng, Jianfeng Gao, Xiaodong Liu, Rangan Majumder, Andrew McNamara, Bhaskar Mitra, Tri Nguyen, Mir Rosenberg, Xia Song, Alina Stoica, Saurabh Tiwary, Tong Wang},
  booktitle={InCoCo@NIPS},
  year={2016}
}
```

### Contributions

Thanks to [@din0s](https://github.com/din0s) for adding this dataset.