This dataset was gathered from the [Google Fact Checker API](https://toolbox.google.com/factcheck/explorer), using an automatic web scraper. 10,000 facts were pulled, but for the sake of simplicity, only ones were the ratings were singular words "false" or "true", were kept, which filtered it down to ~3000 fact checks, with about 90% of the facts being false. 

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