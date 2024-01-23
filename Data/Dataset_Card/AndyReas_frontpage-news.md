---
dataset_info:
  features:
  - name: meta
    struct:
    - name: article_id
      dtype: string
    - name: outlet
      dtype: string
    - name: date
      dtype: string
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: new_article_id
    dtype: string
  splits:
  - name: train
    num_bytes: 4266768296
    num_examples: 13118041
  download_size: 2268969824
  dataset_size: 4266768296
license: mit
task_categories:
- text-generation
language:
- en
size_categories:
- 10M<n<100M
---
# Dataset Card for "frontpage-news"

## The Data
The data consists of ~13,000,000 English articles from ~90 outlets. The articles were collected from the [Sciride News Mine](http://sciride.org/news.html), after which some additional cleaning / processing was performed on the data. The articles span from 2015-07-18 to 2020-10-17.

### Data processing
- Removing duplicate articles (a result of being on the frontpage for multiple days.)
- Removing repeated "outlet tags" appearing before or after headlines such as "| Daily Mail Online".
- Removing dates that were not part of a natural sentence but rather "tags", such as "\[Some headline\] - 2020-12-03".
- Removing duplicate articles (again. This time due to dates making otherwise identical articles unique. Removing the date made them 100% identical.)
- Removing HTML elements that were missed on the first scraping.
- Unescaping HTML characters, replacing them with "regular" characters.
- Removing "junk" articles such as empty articles and articles with a length below a certain threshold.

Note: the cleaning process was not perfect and some "outlet tags" still remain. 
For instance, some outlets use "--" instead of "|" before a tag, and those were missed. 
There is also the case of uncommon characters, such as "\u00a" being used instead of regular characters. This specific example results in tokenizers not being able to properly tokenize sentences using that space. 
There are possibly (likely) other things, that were overlooked during cleaning.

### Outlets
```
["9news.com.au", "abc.net.au", "abcnews.go.com", "afr.com", "aljazeera.com", "apnews.com", "bbc.com", "bostonglobe.com", "breakingnews.ie", "breitbart.com", "businessinsider.com", "cbc.ca", "cbsnews.com", "channel4.com", "chicagotribune.com", "cnbc.com", "csmonitor.com", "ctvnews.ca", "dailymail.co.uk", "dailystar.co.uk", "dw.com", "economist.com", "edition.cnn.com", "euronews.com", "express.co.uk", "foxnews.com", "france24.com", "globalnews.ca", "huffpost.com", "independent.co.uk", "independent.ie", "inquirer.com", "irishexaminer.com", "irishmirror.ie", "irishtimes.com", "itv.com", "latimes.com", "liverpoolecho.co.uk", "macleans.ca", "metro.co.uk", "mirror.co.uk", "montrealgazette.com", "morningstaronline.co.uk", "msnbc.com", "nbcnews.com", "news.com.au", "news.sky.com", "news.yahoo.com", "newshub.co.nz", "newsweek.com", "npr.org", "nypost.com", "nytimes.com", "nzherald.co.nz", "politico.com", "rcinet.ca", "reuters.com", "rfi.fr", "rnz.co.nz", "rt.com", "rte.ie", "sbs.com.au", "scoop.co.nz", "scotsman.com", "slate.com", "smh.com.au", "standard.co.uk", "stuff.co.nz", "telegraph.co.uk", "theage.com.au", "theatlantic.com", "theglobeandmail.com", "theguardian.com", "thehill.com", "thejournal.ie", "thestar.com", "thesun.co.uk", "thesun.ie", "thetimes.co.uk", "thewest.com.au", "time.com", "torontosun.com", "upi.com", "usatoday.com", "vancouversun.com", "walesonline.co.uk", "washingtonpost.com", "washingtontimes.com", "westernjournal.com", "wnd.com", "wsj.com"]
```

## Features (columns)

### title
A news headline.

### description
A news subheader.

### meta

- article_id: Article ID from the original sciride news mine. A hashing of the original title + description.

- date: The date on which the article appeared on the frontpage.

- outlet: The outlet which published the article on their frontpage.

### new_article_id
A new article ID created by hashing the title + description. Can be different from article_id because titles and descriptions changed during "cleaning".