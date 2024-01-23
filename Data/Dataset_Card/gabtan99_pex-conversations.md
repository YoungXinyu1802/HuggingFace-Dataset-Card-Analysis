---
language:
- tl
- fil
license:
- unknown
multilinguality:
- multilingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- sequence-modeling
task_ids:
- dialogue-modeling
- language-modeling
pretty_name: PEx Conversations
tags:
- multi-turn
---

# PinoyExchange (PEx) Conversations Dataset

# Summary
PEx Conversations is a dataset composed of collected threads from PinoyExchange.com (Consisting of Tagalog, English, or Taglish responses). 

The corpus consists of 45K total scraped threads from 8 subforums. The data only consists of the user message which means any images, videos, links, or any embdedded html are not collected in the scraping process. All characters have been transliterated to its closest ASCII representation, and unicode errors were fixed. 

# Format
The data is categorized per category. The objects in the list is composed of:
* category - the category of the threads
* conversations - the list of threads

The threads inside conversations have recursive structure consisting of the following:
* text - This is the response/reply/prompt
* replies - This is a list of the replies to this prompt. The replies inside the list has a structure with the same text and replies component.

# Subforum percentages
The amount of data per subforum are as follows:
* Small Talk - 5K conversations with 1.16M utterances
* Food & Drinks - 8.2K conversations with 273K utterances
* Health & Wellness - 6.3K conversations with 93K utterances
* Body & Fitness - 3.9K conversations with 94K utterances
* Home & Garden - 3.6K conversations with 71K utterances
* Style & Fashion - 9.7K conversations with 197K utterances
* Travel & Leisure - 7.3K conversations with 431K utterances
* Visas & Immigration - 1.1K conversations with 99K utterances

# Model Research
[Tagalog DialoGPT](https://huggingface.co/gabtan99/dialogpt-tagalog-medium)