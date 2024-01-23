---
license: mit
---

The dataset contains the main components of the news articles published online by the newspaper named <a href="https://gazzettadimodena.gelocal.it/modena">Gazzetta di Modena</a>: url of the web page, title, sub-title, text, date of publication, crime category assigned to each news article by the author.

The news articles are written in Italian and describe 11 types of crime events occurred in the province of Modena between the end of 2011 and 2021.

Moreover, the dataset includes data derived from the abovementioned components thanks to the application of Natural Language Processing techniques. Some examples are the place of the crime event occurrence (municipality, area, address and GPS coordinates), the date of the occurrence, and the type of the crime events described in the news article obtained by an automatic categorization of the text.

In the end, news articles describing the same crime events (duplciates) are detected by calculating the document similarity.

Now, we are working on the application of question answering to extract the 5W+1H and we plan to extend the current dataset with the obtained data.

Other researchers can employ the dataset to apply other algorithms of text categorization and duplicate detection and compare their results with the benchmark. The dataset can be useful for several scopes, e.g., geo-localization of the events, text summarization, crime analysis, crime prediction, community detection, topic modeling.
