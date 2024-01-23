---
license: apache-2.0
---
The Dataset was built on 2022/03/29 to contribute to improve the representation of the Spanish language in NLP tasks tasks in the HuggingFace platform.

The dataset contains 2,471 tweets obtained from their tweet_id. The dataset considers the following columns:
- Column 1( Status_id): Corresponds to the unique identification number of the tweet in the social network.
- Column 2( text): Corresponds to the text (in Spanish) linked to the corresponding "Status_Id", which is used to perform the sexism analysis.
- Column 3 (Category): Corresponds to the classification that has been made when analyzing the text (in Spanish), considering three categories: (SEXIST,NON_SEXIST,DOUBTFUL)

The dataset has been built thanks to the previous work of : F. Rodríguez-Sánchez, J. Carrillo-de-Albornoz and L. Plaza. from MeTwo Machismo and Sexism Twitter Identification dataset.
For more information on the categorization process check: https://ieeexplore.ieee.org/document/9281090 