# WEC-Eng
A large-scale dataset for cross-document event coreference extracted from English Wikipedia. </br>

- **Repository (Code for generating WEC):** https://github.com/AlonEirew/extract-wec
- **Paper:** https://aclanthology.org/2021.naacl-main.198/

### Languages

English

## Load Dataset
You can read in WEC-Eng files as follows (using the **huggingface_hub** library):

```json
from huggingface_hub import hf_hub_url, cached_download
import json
REPO_ID = "datasets/Intel/WEC-Eng"
splits_files = ["Dev_Event_gold_mentions_validated.json",
                "Test_Event_gold_mentions_validated.json",
                "Train_Event_gold_mentions.json"]
wec_eng = list()
for split_file in splits_files:
    wec_eng.append(json.load(open(cached_download(
        hf_hub_url(REPO_ID, split_file)), "r")))
```

## Dataset Structure

### Data Splits
- **Final version of the English CD event coreference dataset**<br>
    - Train - Train_Event_gold_mentions.json 
    - Dev - Dev_Event_gold_mentions_validated.json
    - Test - Test_Event_gold_mentions_validated.json

|                             | Train   | Valid | Test |
| -----                       | ------ | ----- | ----  |
| Clusters                    | 7,042  |  233  | 322   |
| Event Mentions              | 40,529 |  1250 | 1,893 |

- **The non (within clusters) controlled version of the dataset (lexical diversity)**<br>
    - All (experimental) - All_Event_gold_mentions_unfiltered.json

### Data Instances

```json
{
        "coref_chain": 2293469,
        "coref_link": "Family Values Tour 1998",
        "doc_id": "House of Pain",
        "mention_context": [
            "From",
            "then",
            "on",
            ",",
            "the",
            "members",
            "continued",
            "their"
  ],
  "mention_head": "Tour",
  "mention_head_lemma": "Tour",
  "mention_head_pos": "PROPN",
  "mention_id": "108172",
  "mention_index": 1,
  "mention_ner": "UNK",
  "mention_type": 8,
  "predicted_coref_chain": null,
  "sent_id": 2,
  "tokens_number": [
    50,
    51,
    52,
    53
  ],
  "tokens_str": "Family Values Tour 1998",
  "topic_id": -1
}
```

### Data Fields

|Field|Value Type|Value|
|---|:---:|---|
|coref_chain|Numeric|Coreference chain/cluster ID|
|coref_link|String|Coreference link wikipeida page/article title|
|doc_id|String|Mention page/article title|
|mention_context|List[String]|Tokenized mention paragraph (including mention)|
|mention_head|String|Mention span head token|
|mention_head_lemma|String|Mention span head token lemma|
|mention_head_pos|String|Mention span head token POS|
|mention_id|String|Mention id|
|mention_index|Numeric|Mention index in json file|
|mention_ner|String|Mention NER|
|tokens_number|List[Numeric]|Mentions tokens ids within the context|
|tokens_str|String|Mention span text|
|topic_id|Ignore|Ignore|
|mention_type|Ignore|Ignore|
|predicted_coref_chain|Ignore|Ignore|
|sent_id|Ignore|Ignore|

## Citation
```
@inproceedings{eirew-etal-2021-wec,
    title = "{WEC}: Deriving a Large-scale Cross-document Event Coreference dataset from {W}ikipedia",
    author = "Eirew, Alon  and
      Cattan, Arie  and
      Dagan, Ido",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.198",
    doi = "10.18653/v1/2021.naacl-main.198",
    pages = "2498--2510",
    abstract = "Cross-document event coreference resolution is a foundational task for NLP applications involving multi-text processing. However, existing corpora for this task are scarce and relatively small, while annotating only modest-size clusters of documents belonging to the same topic. To complement these resources and enhance future research, we present Wikipedia Event Coreference (WEC), an efficient methodology for gathering a large-scale dataset for cross-document event coreference from Wikipedia, where coreference links are not restricted within predefined topics. We apply this methodology to the English Wikipedia and extract our large-scale WEC-Eng dataset. Notably, our dataset creation method is generic and can be applied with relatively little effort to other Wikipedia languages. To set baseline results, we develop an algorithm that adapts components of state-of-the-art models for within-document coreference resolution to the cross-document setting. Our model is suitably efficient and outperforms previously published state-of-the-art results for the task.",
}
```


## License
We provide the following data sets under a <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>. It is based on content extracted from Wikipedia that is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License

## Contact
If you have any questions please create a Github issue at https://github.com/AlonEirew/extract-wec.