---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- en-US
license:
- cc-by-3.0
multilinguality:
- monolingual
pretty_name: 'Sentence-level formality annotations for news, blogs, email and QA forums.


  Published in "An Empirical Analysis of Formality in Online Communication" (Pavlick
  and Tetreault, 2016) '
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- text-scoring
---


This dataset contains sentence-level formality annotations used in the 2016
TACL paper "An Empirical Analysis of Formality in Online Communication"
(Pavlick and Tetreault, 2016). It includes sentences from four genres (news,
blogs, email, and QA forums), all annotated by humans on Amazon Mechanical
Turk. The news and blog data was collected by Shibamouli Lahiri, and we are
redistributing it here for the convenience of other researchers. We collected
the email and answers data ourselves, using a similar annotation setup to
Shibamouli.

In the original dataset, `answers` and `email` were tokenized. In this version,
Oleksiy Syvokon detokenized them with `moses-detokenizer` and a bunch of
additional regexps.

If you use this data in your work, please cite BOTH of the below papers:

```
@article{PavlickAndTetreault-2016:TACL,
  author =  {Ellie Pavlick and Joel Tetreault},
  title =   {An Empirical Analysis of Formality in Online Communication},
  journal = {Transactions of the Association for Computational Linguistics},
  year =    {2016},
  publisher = {Association for Computational Linguistics}
}

@article{Lahiri-2015:arXiv,
  title={{SQUINKY! A} Corpus of Sentence-level Formality, Informativeness, and Implicature},
  author={Lahiri, Shibamouli},
  journal={arXiv preprint arXiv:1506.02306},
  year={2015}
}
```

## Contents

The annotated data files and number of lines in each are as follows:

* 4977 answers -- Annotated sentences from a random sample of posts from the Yahoo! Answers forums: https://answers.yahoo.com/
* 1821 blog -- Annotated sentences from the top 100 blogs listed on http://technorati.com/ on October 31, 2009.
* 1701 email -- Annotated sentences from a random sample of emails from the Jeb Bush email archive: http://americanbridgepac.org/jeb-bushs-gubernatorial-email-archive/
* 2775 news -- Annotated sentences from the "breaking", "recent", and "local" news sections of the following 20 news sites: CNN, CBS News, ABC News, Reuters, BBC News Online, New York Times, Los Angeles Times, The Guardian (U.K.), Voice of America, Boston Globe, Chicago Tribune, San Francisco Chronicle, Times Online (U.K.), news.com.au, Xinhua, The Times of India, Seattle Post Intelligencer, Daily Mail, and Bloomberg L.P.  

## Format

Each record contains the following fields:

1. `avg_score`: the mean formality rating, which ranges from -3 to 3 where lower scores indicate less formal sentences
2. `sentence`
