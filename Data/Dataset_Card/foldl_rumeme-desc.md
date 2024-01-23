---
license: cc-by-sa-4.0
language:
- ru
tags:
- ru
- memes
- text2image
- image2text
pretty_name: rumeme-desc
size_categories:
- 1K<n<10K
---

# Dataset Card for ruMeme Descriptions

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
- [Considerations for Using the Data](#considerations-for-using-the-data)
- [Contributions](#contributions)

## Dataset Description

### Dataset Summary
This is a dataset of more than 2500 memes in Russian and their descriptions from parsing https://vk.com/textmeme.

### Supported Tasks and Leaderboards

`text2image` - generate meme from its textual description

`image2text` - generate description of given meme

### Languages

The text in the dataset is in only in Russian. The associated BCP-47 code is `ru`.

## Dataset Structure

### Data Fields

- `Image`: Meme itself at 512 by 512px (image)
- `Text`: Description (str)

### Data Splits

There is not enough examples yet to split it to train/test/val in my opinion.

## Dataset Creation

As already mentioned, data was gathered from parsing https://vk.com/textmeme.