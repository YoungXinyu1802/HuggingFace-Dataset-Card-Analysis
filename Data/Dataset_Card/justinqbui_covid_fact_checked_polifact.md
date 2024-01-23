This dataset was gathered by using an automated web scraper that scraped [polifact covid fact checker](https://www.politifact.com/coronavirus/). This dataset contains three columns, the text, the rating given by polifact (half-true, full-flop,  pants-fire, barely-true true, mostly-true, and false), and the adjusted rating.

The adjusted rating was created by mapping the raw rating given by polifact
```
true -> true
mostly-true -> true
half-true -> misleading
barely-true -> misleading
false -> false
pants-fire -> false
full-flop -> false
```

annotations_creators:
- expert-generated
language_creators:
- crowdsourced
languages:
- en-US
licenses:
- unknown
multilinguality:
- monolingual
pretty_name: polifact-covid-fact-checker
size_categories:
- unknown
source_datasets:
- original
task_categories:
- text-classification
- question-answering
task_ids:
- fact-checking
- multi-label-classification
- sentiment-classification
- closed-domain-qa
- extractive-qa