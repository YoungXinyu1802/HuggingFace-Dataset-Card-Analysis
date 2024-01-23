---
annotations_creators:
- expert-generated

language:
- ar
- bn
- en
- es
- fa
- fi
- fr
- hi
- id
- ja
- ko
- ru
- sw
- te
- th
- zh


multilinguality:
- multilingual

pretty_name: MIRACL-corpus
size_categories: []
source_datasets: []
tags: []

task_categories:
- text-retrieval

license:
- apache-2.0

task_ids:
- document-retrieval
---

# Dataset Card for MIRACL Corpus


## Dataset Description
* **Homepage:** http://miracl.ai
* **Repository:** https://github.com/project-miracl/miracl
* **Paper:** https://arxiv.org/abs/2210.09984

MIRACL 🌍🙌🌏 (Multilingual Information Retrieval Across a Continuum of Languages) is a multilingual retrieval dataset that focuses on search across 18 different languages, which collectively encompass over three billion native speakers around the world.

This dataset contains the collection data of the 16 "known languages". The remaining 2 "surprise languages" will not be released until later.

The corpus for each language is prepared from a Wikipedia dump, where we keep only the plain text and discard images, tables, etc. Each article is segmented into multiple passages using WikiExtractor based on natural discourse units (e.g., `\n\n` in the wiki markup). Each of these passages comprises a "document" or unit of retrieval. We preserve the Wikipedia article title of each passage.

## Dataset Structure
Each retrieval unit contains three fields: `docid`, `title`, and `text`. Consider an example from the English corpus:

```
{
    "docid": "39#0",
    "title": "Albedo", 
    "text": "Albedo (meaning 'whiteness') is the measure of the diffuse reflection of solar radiation out of the total solar radiation received by an astronomical body (e.g. a planet like Earth). It is dimensionless and measured on a scale from 0 (corresponding to a black body that absorbs all incident radiation) to 1 (corresponding to a body that reflects all incident radiation)."
}
```
The `docid` has the schema `X#Y`, where all passages with the same `X` come from the same Wikipedia article, whereas `Y` denotes the passage within that article, numbered sequentially. The text field contains the text of the passage. The title field contains the name of the article the passage comes from.


The collection can be loaded using:
```
lang='ar'  # or any of the 16 languages
miracl_corpus = datasets.load_dataset('miracl/miracl-corpus', lang)['train']
for doc in miracl_corpus:
   docid = doc['docid']
   title = doc['title']
   text = doc['text']
```

## Dataset Statistics and Links
The following table contains the number of passage and Wikipedia articles in the collection of each language, along with the links to the datasets and raw Wikipedia dumps.
| Language        | # of Passages | # of Articles | Links | Raw Wiki Dump |
|:----------------|--------------:|--------------:|:------|:------|
| Arabic (ar)     |     2,061,414 |       656,982 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-ar) | [🌏](https://archive.org/download/arwiki-20190201/arwiki-20190201-pages-articles-multistream.xml.bz2)
| Bengali (bn)    |       297,265 |        63,762 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-bn) | [🌏](https://archive.org/download/bnwiki-20190201/bnwiki-20190201-pages-articles-multistream.xml.bz2)
| English (en)    |    32,893,221 |     5,758,285 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-en) | [🌏](https://archive.org/download/enwiki-20190201/enwiki-20190201-pages-articles-multistream.xml.bz2)
| Spanish (es)    |    10,373,953 |     1,669,181 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-es) | [🌏](https://archive.org/download/eswiki-20220301/eswiki-20220301-pages-articles-multistream.xml.bz2)
| Persian (fa)    |     2,207,172 |       857,827 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-fa) | [🌏](https://archive.org/download/fawiki-20220301/fawiki-20220301-pages-articles-multistream.xml.bz2)
| Finnish (fi)    |     1,883,509 |       447,815 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-fi) | [🌏](https://archive.org/download/fiwiki-20190201/fiwiki-20190201-pages-articles-multistream.xml.bz2)
| French (fr)     |    14,636,953 |     2,325,608 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-fr) | [🌏](https://archive.org/download/frwiki-20220301/frwiki-20220301-pages-articles-multistream.xml.bz2)
| Hindi (hi)      |       506,264 |       148,107 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-hi) | [🌏](https://archive.org/download/hiwiki-20220301/hiwiki-20220301-pages-articles-multistream.xml.bz2)
| Indonesian (id) |     1,446,315 |       446,330 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-id) | [🌏](https://archive.org/download/idwiki-20190201/idwiki-20190201-pages-articles-multistream.xml.bz2)
| Japanese (ja)   |     6,953,614 |     1,133,444 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-ja) | [🌏](https://archive.org/download/jawiki-20190201/jawiki-20190201-pages-articles-multistream.xml.bz2)
| Korean (ko)     |     1,486,752 |       437,373 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-ko) | [🌏](https://archive.org/download/kowiki-20190201/kowiki-20190201-pages-articles-multistream.xml.bz2)
| Russian (ru)    |     9,543,918 |     1,476,045 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-ru) | [🌏](https://archive.org/download/ruwiki-20190201/ruwiki-20190201-pages-articles-multistream.xml.bz2)
| Swahili (sw)    |       131,924 |        47,793 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-sw) | [🌏](https://archive.org/download/swwiki-20190201/swwiki-20190201-pages-articles-multistream.xml.bz2)
| Telugu (te)     |       518,079 |        66,353 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-te) | [🌏](https://archive.org/download/tewiki-20190201/tewiki-20190201-pages-articles-multistream.xml.bz2)
| Thai (th)       |       542,166 |       128,179 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-th) | [🌏](https://archive.org/download/thwiki-20190101/thwiki-20190101-pages-articles-multistream.xml.bz2)
| Chinese (zh)    |     4,934,368 |     1,246,389 | [🤗](https://huggingface.co/datasets/miracl/miracl-corpus/tree/main/miracl-corpus-v1.0-zh) | [🌏](https://archive.org/download/zhwiki-20220301/zhwiki-20220301-pages-articles-multistream.xml.bz2)
