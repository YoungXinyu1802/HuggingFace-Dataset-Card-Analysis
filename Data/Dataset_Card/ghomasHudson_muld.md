---
annotations_creators:
- found
- crowdsourced
language_creators:
- found
language:
- en
- de
license: []
multilinguality:
- translation
- monolingual
size_categories:
- unknown
source_datasets:
- original
- extended|hotpot_qa
- extended|open_subtitles
task_categories:
- question-answering
- summarization
- text-generation
- translation
task_ids:
- abstractive-qa
pretty_name: The Multitask Long Document Benchmark
tags:
- conditional-text-generation
---

# MuLD
> The Multitask Long Document Benchmark

![](https://user-images.githubusercontent.com/13795113/154329681-f4aa675f-bef1-46ee-9f28-f4ddb71676dd.png)

MuLD (Multitask Long Document Benchmark) is a set of 6 NLP tasks where the inputs consist of at least 10,000 words. The benchmark covers a wide variety of task types including translation, summarization, question answering, and classification. Additionally there is a range of output lengths from a single word classification label all the way up to an output longer than the input text.

- **Repository:** https://github.com/ghomasHudson/muld
- **Paper:** https://arxiv.org/abs/2202.07362

### Supported Tasks and Leaderboards

The 6 MuLD tasks consist of:
- **NarrativeQA** - A question answering dataset requiring an understanding of the plot of books and films.
- **HotpotQA** - An expanded version of HotpotQA requiring multihop reasoning between multiple wikipedia pages. This expanded version includes the full Wikipedia pages.
- **OpenSubtitles** - A translation dataset based on the OpenSubtitles 2018 dataset. The entire subtitles for each tv show is provided, one subtitle per line in both English and German.
- **VLSP (Very Long Scientific Papers)** - An expanded version of the Scientific Papers summarization dataset. Instead of removing very long papers (e.g. thesis), we explicitly include them removing any short papers.
- **AO3 Style Change Detection** - Consists of documents formed from the work of multiple [Archive of Our Own](ao3.org) authors, where the task is to predict the author for each paragraph.
- **Movie Character Types** - Predicting whether a named character is the Hero/Villain given a movie script.

### Dataset Structure
The data is presented in a text-to-text format where each instance contains a input string, output string and (optionally) json encoded metadata.
```
{'input: 'Who was wearing the blue shirt? The beginning...', 'output': ['John'], 'metadata': ''}
```

### Data Fields
- `input`: a string which has a differing structure per task but is presented in a unified format
- `output`: a list of strings where each is a possible answer. Most instances only have a single answer, but some such as narrativeQA and VLSP may have multiple.
- `metadata`: Additional metadata which may be helpful for evaluation. In this version, only the OpenSubtitles task contains metadata (for the ContraPro annotations).

### Data Splits
Each tasks contains different splits depending what was available in the source datasets:

| Task Name                  | Train | Validation | Test |
|----------------------------|----|----|-----|
| NarrativeQA                | ✔️ | ✔️ | ✔️ |
| HotpotQA                   | ✔️ | ✔️ |    |
| AO3 Style Change Detection | ✔️ | ✔️ | ✔️ |
| Movie Character Types      | ✔️ | ✔️ | ✔️ |
| VLSP                       |    |    | ✔️ |
| OpenSubtitles              | ✔️ |    | ✔️ |

### Citation Information
```
@misc{hudson2022muld,
      title={MuLD: The Multitask Long Document Benchmark}, 
      author={G Thomas Hudson and Noura Al Moubayed},
      year={2022},
      eprint={2202.07362},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
Please also cite the papers directly used in this benchmark.