This dataset contains a pre-processed version from Wikipedia suitable for semantic search.

You can load the dataset like this:

```python
from datasets import load_dataset
lang = 'en'
data = load_dataset(f"Cohere/wikipedia-22-12", lang, split='train', streaming=True)
for row in data:
   print(row)
   break
```

This will load the dataset in a streaming mode (so that you don't need to download the whole dataset) and you can process it row-by-row.

The articles are splitted into paragraphs. Further, for each article we added statistics on the page views in 2022 as well as in how many other languages an article is available. 
The dataset is sorted by page views, so that the most popular Wikipedia articles come first. So if you e.g. read the top-100k rows, you get quite a good coverage on topics that
are broadly interesting for people.

## Semantic Search Embeddings

We also provide versions where documents have been embedded using the [cohere multilingual embedding model](https://txt.cohere.ai/multilingual/), 
e.g. [wikipedia-22-12-en-embeddings](https://huggingface.co/datasets/Cohere/wikipedia-22-12-en-embeddings) contains the paragraphs and their respective embeddings for English.
You can find the embeddings for other languages in the datasets `wikipedia-22-12-{lang}-embeddings`.


## Dataset Creation
The [XML data dumps](https://dumps.wikimedia.org/backup-index.html) from December 20th, 2022 where downloaded and processed 
with [wikiextractor](https://github.com/attardi/wikiextractor) (with Version: 2.75) and the following command:
```
python WikiExtractor.py --json -s --lists ../dumps/dewiki-20210101-pages-articles.xml.bz2 -o text_de
```

To count in how many languages an article is available, we downloaded the SQL files with language links from:
```
https://dumps.wikimedia.org/{lang}wiki/{datestr}/{filename}
```
And processed the SQL file to read for each article the outbound links.

Pageviews where downloaded from:
```
https://dumps.wikimedia.org/other/pageviews/{year}/{year}-{month_str}/pageviews-{year}{month_str}{day_str}-{hour_str}0000.gz
```

We downloaded for each day the pageviews for a random hour. We then computed the harmonic mean of page views. We used harmonic mean to address cases where articles receive
a very high number of page views at e.g. a certain time point. We use the log scores for the page views to increase the numerical stability.

Code to compute the page views was:
```python
import gzip
import sys
from collections import Counter, defaultdict
import math
import tqdm
import json


title_views = {}

#Score: Harmonic mean  (View_Day_1 * View_Day_2 * View_day_3)
# Add log for better numerical stabilitiy
# Add +1 to avoid log(0)
# Compare the sum, so that days without view are counted as 0 views
for filepath in tqdm.tqdm(sys.argv[1:]):
    with gzip.open(filepath, "rt") as fIn:
        for line in fIn:
            splits = line.strip().split()
            if len(splits) == 4:
                lang, title, views, _ = line.strip().split()
                lang = lang.lower()

                if lang.endswith(".m"): #Add mobile page scores to main score
                    lang = lang[0:-2]
                
                if lang.count(".") > 0:
                    continue

                if lang not in title_views:
                    title_views[lang] = {}
                if title not in title_views[lang]:
                    title_views[lang][title] = 0.0

                title_views[lang][title] += math.log(int(views)+1)



#Save results
for lang in title_views:
    with open(f"pageviews_summary/{lang}.json", "w") as fOut:
        fOut.write(json.dumps(title_views[lang]))
```


We filter out paragraphs that start with `BULLET::::`, `Section::::`, `<templatestyles`, or `[[File:`. 
Further, we also only include paragraphs with at least 100 characters (using Python len method=. 
