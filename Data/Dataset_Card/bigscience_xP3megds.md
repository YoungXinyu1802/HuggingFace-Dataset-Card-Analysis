---
annotations_creators:
- expert-generated
- crowdsourced
language:
- ak
- ar
- as
- bm
- bn
- ca
- code
- en
- es
- eu
- fon
- fr
- gu
- hi
- id
- ig
- ki
- kn
- lg
- ln
- ml
- mr
- ne
- nso
- ny
- or
- pa
- pt
- rn
- rw
- sn
- st
- sw
- ta
- te
- tn
- ts
- tum
- tw
- ur
- vi
- wo
- xh
- yo
- zh
- zu
programming_language: 
- C
- C++
- C#
- Go
- Java
- JavaScript
- Lua
- PHP
- Python
- Ruby
- Rust
- Scala
- TypeScript
license:
- apache-2.0
multilinguality:
- multilingual
pretty_name: xP3
size_categories:
- 100M<n<1B
task_categories:
- other
---

# Dataset Card for xP3

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Repository:** https://github.com/bigscience-workshop/xmtf
- **Paper:** [Crosslingual Generalization through Multitask Finetuning](https://arxiv.org/abs/2211.01786)
- **Point of Contact:** [Niklas Muennighoff](mailto:niklas@hf.co)

### Dataset Summary

> xP3 (Crosslingual Public Pool of Prompts) is a collection of prompts & datasets across 46 of languages & 16 NLP tasks. It is used for the training of BLOOMZ and mT0, multilingual language models capable of following human instructions in dozens of languages zero-shot.

- **Creation:** The dataset can be recreated using instructions available [here](https://github.com/bigscience-workshop/xmtf#create-xp3). We provide this version to save processing time and ease reproducibility.
- **Languages:** 46 (Can be extended by [recreating with more splits](https://github.com/bigscience-workshop/xmtf#create-xp3))
- **xP3 Dataset Family:**

<table>
  <tr>
<th>Name</th>
<th>Explanation</th>
<th>Example models</th>
</tr>
<tr>
<td><a href=https://huggingface.co/datasets/bigscience/xP3>xP3</a></t> 
<td>Mixture of 13 training tasks in 46 languages with English prompts</td>
<td><a href=https://huggingface.co/bigscience/bloomz>bloomz</a> & <a href=https://huggingface.co/bigscience/mt0-xxl>mt0-xxl</a></td>
</tr>
<tr>
<td><a href=https://huggingface.co/datasets/bigscience/xP3mt>xP3mt</a></t> 
<td>Mixture of 13 training tasks in 46 languages with prompts in 20 languages (machine-translated from English)</td>
<td><a href=https://huggingface.co/bigscience/bloomz-mt>bloomz-mt</a> & <a href=https://huggingface.co/bigscience/mt0-xxl-mt>mt0-xxl-mt</a></td>
</tr>
<tr>
<td><a href=https://huggingface.co/datasets/bigscience/xP3all>xP3all</a></t> 
<td>xP3 + evaluation datasets adding an additional 3 tasks for a total of 16 tasks in 46 languages with English prompts</td>
<td></td>
</tr>
<tr>
<td><a href=https://huggingface.co/datasets/bigscience/xP3megds>xP3megds</a></t> 
<td><a href=https://github.com/bigscience-workshop/Megatron-DeepSpeed>Megatron-DeepSpeed</a> processed version of xP3</td>
<td><a href=https://huggingface.co/bigscience/bloomz>bloomz</a></td>
</tr>
<tr>
<td><a href=https://huggingface.co/datasets/Muennighoff/P3>P3</a></t> 
<td>Repreprocessed version of the English-only <a href=https://huggingface.co/datasets/bigscience/P3>P3</a> with 8 training tasks</td>
<td><a href=https://huggingface.co/bigscience/bloomz-p3>bloomz-p3</a> & <a href=https://huggingface.co/bigscience/mt0-xxl-p3>mt0-xxl-p3</a></td>
</tr>
</table>

## Dataset Structure

### Data Instances

An example of "train" looks as follows:
```json
{
"inputs": "Sentence 1: Fue académico en literatura metafísica, teología y ciencias clásicas.\nSentence 2: Fue académico en literatura metafísica, teología y ciencia clásica.\nQuestion: Can we rewrite Sentence 1 to Sentence 2? Yes or No?",
"targets": "Yes" 
}
```

### Data Fields

The data fields are the same among all splits:
- `inputs`: the natural language input fed to the model
- `targets`: the natural language target that the model has to generate

### Data Splits

The below table summarizes sizes per language (computed from the `merged_{lang}.jsonl` files). Due to languages like `tw` only being single sentence translation samples from Flores, their byte percentage is significantly lower than their sample percentage.

|Language|Kilobytes|%|Samples|%|
|--------|------:|-:|---:|-:|
|tw|106288|0.11|265071|0.34|
|bm|107056|0.11|265180|0.34|
|ak|108096|0.11|265071|0.34|
|eu|108112|0.11|269973|0.34|
|ca|110608|0.12|271191|0.34|
|fon|113072|0.12|265063|0.34|
|st|114080|0.12|265063|0.34|
|ki|115040|0.12|265180|0.34|
|tum|116032|0.12|265063|0.34|
|wo|122560|0.13|365063|0.46|
|ln|126304|0.13|365060|0.46|
|as|156256|0.16|265063|0.34|
|or|161472|0.17|265063|0.34|
|kn|165456|0.17|265063|0.34|
|ml|175040|0.18|265864|0.34|
|rn|192992|0.2|318189|0.4|
|nso|229712|0.24|915051|1.16|
|tn|235536|0.25|915054|1.16|
|lg|235936|0.25|915021|1.16|
|rw|249360|0.26|915043|1.16|
|ts|250256|0.26|915044|1.16|
|sn|252496|0.27|865056|1.1|
|xh|254672|0.27|915058|1.16|
|zu|263712|0.28|915061|1.16|
|ny|272128|0.29|915063|1.16|
|ig|325232|0.34|950097|1.2|
|yo|352784|0.37|918416|1.16|
|ne|393680|0.41|315754|0.4|
|pa|523248|0.55|339210|0.43|
|gu|560688|0.59|347499|0.44|
|sw|560896|0.59|1114455|1.41|
|mr|666240|0.7|417269|0.53|
|bn|832720|0.88|428843|0.54|
|ta|924496|0.97|410633|0.52|
|te|1332912|1.4|573364|0.73|
|ur|1918272|2.02|855756|1.08|
|vi|3101408|3.27|1667306|2.11|
|code|4330752|4.56|2707724|3.43|
|hi|4393696|4.63|1543441|1.96|
|zh|4589904|4.83|3560556|4.51|
|id|4606288|4.85|2627392|3.33|
|ar|4677264|4.93|2148955|2.72|
|fr|5546688|5.84|5055942|6.41|
|pt|6129584|6.46|3562772|4.52|
|es|7571808|7.98|5151349|6.53|
|en|37261104|39.25|31495184|39.93|
|total|94941936|100.0|78883588|100.0|

## Dataset Creation

### Source Data

#### Training datasets

- Code Miscellaneous
  - [CodeComplex](https://huggingface.co/datasets/codeparrot/codecomplex)
  - [Docstring Corpus](https://huggingface.co/datasets/teven/code_docstring_corpus)
  - [GreatCode](https://huggingface.co/datasets/great_code)
  - [State Changes](https://huggingface.co/datasets/Fraser/python-state-changes)
- Closed-book QA
  - [Hotpot QA](https://huggingface.co/datasets/hotpot_qa)
  - [Trivia QA](https://huggingface.co/datasets/trivia_qa)
  - [Web Questions](https://huggingface.co/datasets/web_questions)
  - [Wiki QA](https://huggingface.co/datasets/wiki_qa)  
- Extractive QA
  - [Adversarial QA](https://huggingface.co/datasets/adversarial_qa)
  - [CMRC2018](https://huggingface.co/datasets/cmrc2018)
  - [DRCD](https://huggingface.co/datasets/clue)
  - [DuoRC](https://huggingface.co/datasets/duorc)
  - [MLQA](https://huggingface.co/datasets/mlqa)      
  - [Quoref](https://huggingface.co/datasets/quoref)
  - [ReCoRD](https://huggingface.co/datasets/super_glue)  
  - [ROPES](https://huggingface.co/datasets/ropes)
  - [SQuAD v2](https://huggingface.co/datasets/squad_v2)
  - [xQuAD](https://huggingface.co/datasets/xquad)
  - TyDI QA
    - [Primary](https://huggingface.co/datasets/khalidalt/tydiqa-primary)
    - [Goldp](https://huggingface.co/datasets/khalidalt/tydiqa-goldp)
- Multiple-Choice QA
  - [ARC](https://huggingface.co/datasets/ai2_arc)
  - [C3](https://huggingface.co/datasets/c3)  
  - [CoS-E](https://huggingface.co/datasets/cos_e)
  - [Cosmos](https://huggingface.co/datasets/cosmos)
  - [DREAM](https://huggingface.co/datasets/dream)
  - [MultiRC](https://huggingface.co/datasets/super_glue)
  - [OpenBookQA](https://huggingface.co/datasets/openbookqa)
  - [PiQA](https://huggingface.co/datasets/piqa)  
  - [QUAIL](https://huggingface.co/datasets/quail)
  - [QuaRel](https://huggingface.co/datasets/quarel)
  - [QuaRTz](https://huggingface.co/datasets/quartz)
  - [QASC](https://huggingface.co/datasets/qasc)
  - [RACE](https://huggingface.co/datasets/race)
  - [SciQ](https://huggingface.co/datasets/sciq)    
  - [Social IQA](https://huggingface.co/datasets/social_i_qa)
  - [Wiki Hop](https://huggingface.co/datasets/wiki_hop)
  - [WiQA](https://huggingface.co/datasets/wiqa)  
- Paraphrase Identification
  - [MRPC](https://huggingface.co/datasets/super_glue)
  - [PAWS](https://huggingface.co/datasets/paws)
  - [PAWS-X](https://huggingface.co/datasets/paws-x)  
  - [QQP](https://huggingface.co/datasets/qqp)  
- Program Synthesis
  - [APPS](https://huggingface.co/datasets/codeparrot/apps)
  - [CodeContests](https://huggingface.co/datasets/teven/code_contests)
  - [JupyterCodePairs](https://huggingface.co/datasets/codeparrot/github-jupyter-text-code-pairs)
  - [MBPP](https://huggingface.co/datasets/Muennighoff/mbpp)
  - [NeuralCodeSearch](https://huggingface.co/datasets/neural_code_search)
  - [XLCoST](https://huggingface.co/datasets/codeparrot/xlcost-text-to-code)  
- Structure-to-text
  - [Common Gen](https://huggingface.co/datasets/common_gen)
  - [Wiki Bio](https://huggingface.co/datasets/wiki_bio)
- Sentiment
  - [Amazon](https://huggingface.co/datasets/amazon_polarity)
  - [App Reviews](https://huggingface.co/datasets/app_reviews)
  - [IMDB](https://huggingface.co/datasets/imdb)
  - [Rotten Tomatoes](https://huggingface.co/datasets/rotten_tomatoes)
  - [Yelp](https://huggingface.co/datasets/yelp_review_full)
- Simplification
  - [BiSECT](https://huggingface.co/datasets/GEM/BiSECT)
- Summarization
  - [CNN Daily Mail](https://huggingface.co/datasets/cnn_dailymail)
  - [Gigaword](https://huggingface.co/datasets/gigaword)
  - [MultiNews](https://huggingface.co/datasets/multi_news)
  - [SamSum](https://huggingface.co/datasets/samsum)
  - [Wiki-Lingua](https://huggingface.co/datasets/GEM/wiki_lingua)
  - [XLSum](https://huggingface.co/datasets/GEM/xlsum)
  - [XSum](https://huggingface.co/datasets/xsum)
- Topic Classification
  - [AG News](https://huggingface.co/datasets/ag_news)
  - [DBPedia](https://huggingface.co/datasets/dbpedia_14)
  - [TNEWS](https://huggingface.co/datasets/clue)  
  - [TREC](https://huggingface.co/datasets/trec)
  - [CSL](https://huggingface.co/datasets/clue) 
- Translation
  - [Flores-200](https://huggingface.co/datasets/Muennighoff/flores200)
  - [Tatoeba](https://huggingface.co/datasets/Helsinki-NLP/tatoeba_mt)
- Word Sense disambiguation
  - [WiC](https://huggingface.co/datasets/super_glue)
  - [XL-WiC](https://huggingface.co/datasets/pasinit/xlwic)
  
#### Evaluation datasets (included in [xP3all](https://huggingface.co/datasets/bigscience/xP3all) except for NLI & HumanEval)
  
- Natural Language Inference (NLI)
  - [ANLI](https://huggingface.co/datasets/anli)
  - [CB](https://huggingface.co/datasets/super_glue)
  - [RTE](https://huggingface.co/datasets/super_glue)
  - [XNLI](https://huggingface.co/datasets/xnli)
- Coreference Resolution
  - [Winogrande](https://huggingface.co/datasets/winogrande)
  - [XWinograd](https://huggingface.co/datasets/Muennighoff/xwinograd)
- Program Synthesis
  - [HumanEval](https://huggingface.co/datasets/openai_humaneval)
- Sentence Completion
  - [COPA](https://huggingface.co/datasets/super_glue)
  - [Story Cloze](https://huggingface.co/datasets/story_cloze)
  - [XCOPA](https://huggingface.co/datasets/xcopa)  
  - [XStoryCloze](https://huggingface.co/datasets/Muennighoff/xstory_cloze)

## Additional Information

### Licensing Information

The dataset is released under Apache 2.0.

### Citation Information

```bibtex
@misc{muennighoff2022crosslingual,
      title={Crosslingual Generalization through Multitask Finetuning}, 
      author={Niklas Muennighoff and Thomas Wang and Lintang Sutawika and Adam Roberts and Stella Biderman and Teven Le Scao and M Saiful Bari and Sheng Shen and Zheng-Xin Yong and Hailey Schoelkopf and Xiangru Tang and Dragomir Radev and Alham Fikri Aji and Khalid Almubarak and Samuel Albanie and Zaid Alyafeai and Albert Webson and Edward Raff and Colin Raffel},
      year={2022},
      eprint={2211.01786},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Contributions

Thanks to the contributors of [promptsource](https://github.com/bigscience-workshop/promptsource/graphs/contributors) for adding many prompts used in this dataset.