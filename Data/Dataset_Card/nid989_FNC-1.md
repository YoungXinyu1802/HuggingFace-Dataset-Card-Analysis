### Dataset Summary

The data provided is (headline, body, stance) instances, where the stance is one of {unrelated, discuss, agree, disagree}.

**Input**
* A headline and a body text - either from the same news article or from two different articles.

**Output**

* Classify the stance of the body text relative to the claim made in the headline into one of four categories:
  * Agrees: The body text agrees with the headline.
  * Disagrees: The body text disagrees with the headline.
  * Discusses: The body text discuss the same topic as the headline, but does not take a position
  * Unrelated: The body text discusses a different topic than the headline

The distribution of Stance classes in the entire dataset is as follows:

|  rows   | unrelated | discuss |   agree   |  disagree  |
|---------|-----------|---------|-----------|----------- |
|  49972  |  0.73131  | 0.17828 | 0.0736012 |  0.016809  |

### Source Data

[FNC-1 Official webpage.](http://www.fakenewschallenge.org/)

- annotations_creators: found
- language_creators: found
- languages: en-US
- licenses: apache-2.0
- multilingualism: monolingual
- pretty_name: FNC-1
- size_categories: unknown
- source_datasets: original
- task_categories:text-classification
- task_ids 
  - multi-class-classification
  - natural-language-inference
  - multi-label-classification
  - intent-classification