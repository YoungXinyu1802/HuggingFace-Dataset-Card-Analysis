# FindZebra corpus

A collection of 30.658 curated articles about rare diseases gathered from GARD, GeneReviews, Genetics Home Reference, OMIM, Orphanet, and Wikipedia. Each article is referenced with a Concept Unique Identifier ([CUI](https://www.nlm.nih.gov/research/umls/new_users/online_learning/Meta_005.html)).


## Preprocessing

The raw HTML content of each article has been processed using the following code (`text` column):

```python
# Preprocessing code
import math 
import html2text
parser = html2text.HTML2Text()
parser.ignore_links = True
parser.ignore_images = True
parser.ignore_tables = True
parser.ignore_emphasis = True
parser.body_width = math.inf

parser.body_width = math.inf
article_text = parser.handle(article_html)
```