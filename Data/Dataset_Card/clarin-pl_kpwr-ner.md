---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- pl
license:
- cc-by-3.0
multilinguality:
- monolingual
size_categories:
- 18K
- 10K<n<100K
source_datasets:
- original
task_categories:
- other
task_ids:
- named-entity-recognition
pretty_name: KPWr-NER
tags:
- structure-prediction
---

# KPWR-NER

## Description

KPWR-NER is a part the Polish Corpus of Wrocław University of Technology (*Korpus Języka Polskiego Politechniki Wrocławskiej*). Its objective is named entity recognition for fine-grained categories of entities. It is the ‘n82’ version of the KPWr, which means that number of classes is restricted to 82 (originally 120). During corpus creation, texts were annotated by humans from various sources, covering many domains and genres.

## Tasks (input, output and metrics)
Named entity recognition (NER) - tagging entities in text with their corresponding type.

**Input** ('*tokens'* column): sequence of tokens

**Output** ('*ner'* column): sequence of predicted tokens’ classes in BIO notation (82 possible classes, described in detail in the annotation guidelines)

**Measurements**: F1-score (seqeval)

**Example**:

Input: `[‘Roboty’, ‘mają’, ‘kilkanaście’, ‘lat’, ‘i’, ‘pochodzą’, ‘z’, ‘USA’, ‘,’, ‘Wysokie’, ‘napięcie’, ‘jest’, ‘dużo’, ‘młodsze’, ‘,’, ‘powstało’, ‘w’, ‘Niemczech’, ‘.’]`

Input (translated by DeepL): `Robots are more than a dozen years old and come from the US, High Voltage is much younger, having been developed in Germany.`

Output: `[‘B-nam_pro_title’, ‘O’, ‘O’, ‘O’, ‘O’, ‘O’, ‘O’, ‘B-nam_loc_gpe_country’, ‘O’, ‘B-nam_pro_title’, ‘I-nam_pro_title’, ‘O’, ‘O’, ‘O’, ‘O’, ‘O’, ‘O’, ‘B-nam_loc_gpe_country’, ‘O’]`

## Data splits


| Subset | Cardinality (sentences) |
|--------|------------------------:|
| train  |                   13959 |
| dev    |                       0 |
| test   |                    4323 |

## Class distribution (without "O" and "I-*")

| Class                       |   train |   validation |      test |
|:----------------------------|--------:|-------------:|----------:|
| B-nam_liv_person            | 0.21910 |            - |   0.21422 |
| B-nam_loc_gpe_city          | 0.10101 |            - |   0.09865 |
| B-nam_loc_gpe_country       | 0.07467 |            - |   0.08059 |
| B-nam_org_institution       | 0.05893 |            - |   0.06005 |
| B-nam_org_organization      | 0.04448 |            - |   0.05553 |
| B-nam_org_group_team        | 0.03492 |            - |   0.03363 |
| B-nam_adj_country           | 0.03410 |            - |   0.03747 |
| B-nam_org_company           | 0.02439 |            - |   0.01716 |
| B-nam_pro_media_periodic    | 0.02250 |            - |   0.01896 |
| B-nam_fac_road              | 0.01995 |            - |   0.02144 |
| B-nam_liv_god               | 0.01934 |            - |   0.00790 |
| B-nam_org_nation            | 0.01739 |            - |   0.01828 |
| B-nam_oth_tech              | 0.01724 |            - |   0.01377 |
| B-nam_pro_media_web         | 0.01709 |            - |   0.00903 |
| B-nam_fac_goe               | 0.01596 |            - |   0.01445 |
| B-nam_eve_human             | 0.01573 |            - |   0.01761 |
| B-nam_pro_title             | 0.01558 |            - |   0.00790 |
| B-nam_pro_brand             | 0.01543 |            - |   0.01038 |
| B-nam_org_political_party   | 0.01264 |            - |   0.01309 |
| B-nam_loc_gpe_admin1        | 0.01219 |            - |   0.01445 |
| B-nam_eve_human_sport       | 0.01174 |            - |   0.01242 |
| B-nam_pro_software          | 0.01091 |            - |   0.02190 |
| B-nam_adj                   | 0.00963 |            - |   0.01174 |
| B-nam_loc_gpe_admin3        | 0.00888 |            - |   0.01061 |
| B-nam_pro_model_car         | 0.00873 |            - |   0.00587 |
| B-nam_loc_hydronym_river    | 0.00843 |            - |   0.01151 |
| B-nam_oth                   | 0.00775 |            - |   0.00497 |
| B-nam_pro_title_document    | 0.00738 |            - |   0.01986 |
| B-nam_loc_astronomical      | 0.00730 |            - |   -       |
| B-nam_oth_currency          | 0.00723 |            - |   0.01151 |
| B-nam_adj_city              | 0.00670 |            - |   0.00948 |
| B-nam_org_group_band        | 0.00587 |            - |   0.00429 |
| B-nam_loc_gpe_admin2        | 0.00565 |            - |   0.00813 |
| B-nam_loc_gpe_district      | 0.00504 |            - |   0.00406 |
| B-nam_loc_land_continent    | 0.00459 |            - |   0.00722 |
| B-nam_loc_country_region    | 0.00459 |            - |   0.00090 |
| B-nam_loc_land_mountain     | 0.00414 |            - |   0.00203 |
| B-nam_pro_title_book        | 0.00384 |            - |   0.00248 |
| B-nam_loc_historical_region | 0.00376 |            - |   0.00497 |
| B-nam_loc                   | 0.00361 |            - |   0.00090 |
| B-nam_eve                   | 0.00361 |            - |   0.00181 |
| B-nam_org_group             | 0.00331 |            - |   0.00406 |
| B-nam_loc_land_island       | 0.00331 |            - |   0.00248 |
| B-nam_pro_media_tv          | 0.00316 |            - |   0.00158 |
| B-nam_liv_habitant          | 0.00316 |            - |   0.00158 |
| B-nam_eve_human_cultural    | 0.00316 |            - |   0.00497 |
| B-nam_pro_title_tv          | 0.00309 |            - |   0.00542 |
| B-nam_oth_license           | 0.00286 |            - |   0.00248 |
| B-nam_num_house             | 0.00256 |            - |   0.00248 |
| B-nam_pro_title_treaty      | 0.00248 |            - |   0.00045 |
| B-nam_fac_system            | 0.00248 |            - |   0.00587 |
| B-nam_loc_gpe_subdivision   | 0.00241 |            - |   0.00587 |
| B-nam_loc_land_region       | 0.00226 |            - |   0.00248 |
| B-nam_pro_title_album       | 0.00218 |            - |   0.00158 |
| B-nam_adj_person            | 0.00203 |            - |   0.00406 |
| B-nam_fac_square            | 0.00196 |            - |   0.00135 |
| B-nam_pro_award             | 0.00188 |            - |   0.00519 |
| B-nam_eve_human_holiday     | 0.00188 |            - |   0.00203 |
| B-nam_pro_title_song        | 0.00166 |            - |   0.00158 |
| B-nam_pro_media_radio       | 0.00151 |            - |   0.00068 |
| B-nam_pro_vehicle           | 0.00151 |            - |   0.00090 |
| B-nam_oth_position          | 0.00143 |            - |   0.00226 |
| B-nam_liv_animal            | 0.00143 |            - |   0.00248 |
| B-nam_pro                   | 0.00135 |            - |   0.00045 |
| B-nam_oth_www               | 0.00120 |            - |   0.00451 |
| B-nam_num_phone             | 0.00120 |            - |   0.00045 |
| B-nam_pro_title_article     | 0.00113 |            - |   -       |
| B-nam_oth_data_format       | 0.00113 |            - |   0.00226 |
| B-nam_fac_bridge            | 0.00105 |            - |   0.00090 |
| B-nam_liv_character         | 0.00098 |            - |   -       |
| B-nam_pro_software_game     | 0.00090 |            - |   0.00068 |
| B-nam_loc_hydronym_lake     | 0.00090 |            - |   0.00045 |
| B-nam_loc_gpe_conurbation   | 0.00090 |            - |   -       |
| B-nam_pro_media             | 0.00083 |            - |   0.00181 |
| B-nam_loc_land              | 0.00075 |            - |   0.00045 |
| B-nam_loc_land_peak         | 0.00075 |            - |   -       |
| B-nam_fac_park              | 0.00068 |            - |   0.00226 |
| B-nam_org_organization_sub  | 0.00060 |            - |   0.00068 |
| B-nam_loc_hydronym          | 0.00060 |            - |   0.00023 |
| B-nam_loc_hydronym_sea      | 0.00045 |            - |   0.00068 |
| B-nam_loc_hydronym_ocean    | 0.00045 |            - |   0.00023 |
| B-nam_fac_goe_stop          | 0.00038 |            - |   0.00090 |


## Citation

```
@inproceedings{broda-etal-2012-kpwr,
    title = "{KPW}r: Towards a Free Corpus of {P}olish",
    author = "Broda, Bartosz  and
      Marci{\'n}czuk, Micha{\l}  and
      Maziarz, Marek  and
      Radziszewski, Adam  and
      Wardy{\'n}ski, Adam",
    booktitle = "Proceedings of the Eighth International Conference on Language Resources and Evaluation ({LREC}'12)",
    month = may,
    year = "2012",
    address = "Istanbul, Turkey",
    publisher = "European Language Resources Association (ELRA)",
    url = "http://www.lrec-conf.org/proceedings/lrec2012/pdf/965_Paper.pdf",
    pages = "3218--3222",
    abstract = "This paper presents our efforts aimed at collecting and annotating a free Polish corpus. The corpus will serve for us as training and testing material for experiments with Machine Learning algorithms. As others may also benefit from the resource, we are going to release it under a Creative Commons licence, which is hoped to remove unnecessary usage restrictions, but also to facilitate reproduction of our experimental results. The corpus is being annotated with various types of linguistic entities: chunks and named entities, selected syntactic and semantic relations, word senses and anaphora. We report on the current state of the project as well as our ultimate goals.",
}
```

## License

```
Creative Commons Attribution 3.0 Unported Licence
```

## Links

[HuggingFace](https://huggingface.co/datasets/clarin-pl/kpwr-ner)

[Source](https://clarin-pl.eu/index.php/kpwr-en/)

[Paper](https://aclanthology.org/L12-1574/)

[KPWr annotation guidelines](http://www.nlp.pwr.wroc.pl/narzedzia-i-zasoby/zasoby/kpwr-lemma/16-narzedzia-zasoby/79-wytyczne)

[KPWr annotation guidelines - named entities](https://clarin-pl.eu/dspace/handle/11321/294)

## Examples

### Loading

```python
from pprint import pprint

from datasets import load_dataset

dataset = load_dataset("clarin-pl/kpwr-ner")
pprint(dataset['train'][0])

# {'lemmas': ['roborally', 'czy', 'wysoki', 'napięcie', '?'],
#  'ner': [73, 160, 73, 151, 160],
#  'orth': ['subst:sg:nom:n',
#           'qub',
#           'adj:sg:nom:n:pos',
#           'subst:sg:nom:n',
#           'interp'],
#  'tokens': ['RoboRally', 'czy', 'Wysokie', 'napięcie', '?']}
```

### Evaluation

```python
import random
from pprint import pprint

from datasets import load_dataset, load_metric

dataset = load_dataset("clarin-pl/kpwr-ner")
references = dataset["test"]["ner"]

# generate random predictions
predictions = [
    [
        random.randrange(dataset["train"].features["ner"].feature.num_classes)
        for _ in range(len(labels))
    ]
    for labels in references
]

# transform to original names of labels
references_named = [
    [dataset["train"].features["ner"].feature.names[label] for label in labels]
    for labels in references
]
predictions_named = [
    [dataset["train"].features["ner"].feature.names[label] for label in labels]
    for labels in predictions
]

# utilise seqeval to evaluate
seqeval = load_metric("seqeval")
seqeval_score = seqeval.compute(
    predictions=predictions_named, references=references_named, scheme="IOB2"
)

pprint(seqeval_score, depth=1)

# {'nam_adj': {...},
#  'nam_adj_city': {...},
#  'nam_adj_country': {...},
#  'nam_adj_person': {...},
#  'nam_eve': {...},
#  'nam_eve_human': {...},
#  'nam_eve_human_cultural': {...},
#  'nam_eve_human_holiday': {...},
#  'nam_eve_human_sport': {...},
#  'nam_fac_bridge': {...},
#  'nam_fac_goe': {...},
#  'nam_fac_goe_stop': {...},
#  'nam_fac_park': {...},
#  'nam_fac_road': {...},
#  'nam_fac_square': {...},
#  'nam_fac_system': {...},
#  'nam_liv_animal': {...},
#  'nam_liv_character': {...},
#  'nam_liv_god': {...},
#  'nam_liv_habitant': {...},
#  'nam_liv_person': {...},
#  'nam_loc': {...},
#  'nam_loc_astronomical': {...},
#  'nam_loc_country_region': {...},
#  'nam_loc_gpe_admin1': {...},
#  'nam_loc_gpe_admin2': {...},
#  'nam_loc_gpe_admin3': {...},
#  'nam_loc_gpe_city': {...},
#  'nam_loc_gpe_conurbation': {...},
#  'nam_loc_gpe_country': {...},
#  'nam_loc_gpe_district': {...},
#  'nam_loc_gpe_subdivision': {...},
#  'nam_loc_historical_region': {...},
#  'nam_loc_hydronym': {...},
#  'nam_loc_hydronym_lake': {...},
#  'nam_loc_hydronym_ocean': {...},
#  'nam_loc_hydronym_river': {...},
#  'nam_loc_hydronym_sea': {...},
#  'nam_loc_land': {...},
#  'nam_loc_land_continent': {...},
#  'nam_loc_land_island': {...},
#  'nam_loc_land_mountain': {...},
#  'nam_loc_land_peak': {...},
#  'nam_loc_land_region': {...},
#  'nam_num_house': {...},
#  'nam_num_phone': {...},
#  'nam_org_company': {...},
#  'nam_org_group': {...},
#  'nam_org_group_band': {...},
#  'nam_org_group_team': {...},
#  'nam_org_institution': {...},
#  'nam_org_nation': {...},
#  'nam_org_organization': {...},
#  'nam_org_organization_sub': {...},
#  'nam_org_political_party': {...},
#  'nam_oth': {...},
#  'nam_oth_currency': {...},
#  'nam_oth_data_format': {...},
#  'nam_oth_license': {...},
#  'nam_oth_position': {...},
#  'nam_oth_tech': {...},
#  'nam_oth_www': {...},
#  'nam_pro': {...},
#  'nam_pro_award': {...},
#  'nam_pro_brand': {...},
#  'nam_pro_media': {...},
#  'nam_pro_media_periodic': {...},
#  'nam_pro_media_radio': {...},
#  'nam_pro_media_tv': {...},
#  'nam_pro_media_web': {...},
#  'nam_pro_model_car': {...},
#  'nam_pro_software': {...},
#  'nam_pro_software_game': {...},
#  'nam_pro_title': {...},
#  'nam_pro_title_album': {...},
#  'nam_pro_title_article': {...},
#  'nam_pro_title_book': {...},
#  'nam_pro_title_document': {...},
#  'nam_pro_title_song': {...},
#  'nam_pro_title_treaty': {...},
#  'nam_pro_title_tv': {...},
#  'nam_pro_vehicle': {...},
#  'overall_accuracy': 0.006156203762418094,
#  'overall_f1': 0.0009844258777797407,
#  'overall_precision': 0.0005213624939842789,
#  'overall_recall': 0.008803611738148984}
```