---
license: mit
language:
- en
pretty_name: SynthIE
---

# Dataset Card for Dataset Name

## Dataset Description

- **Homepage and Repository:** https://github.com/epfl-dlab/SynthIE
- **Paper:** https://arxiv.org/abs/2303.04132

### Dataset Summary

[Exploiting Asymmetry for Synthetic Training Data Generation: SynthIE and the Case of Information Extraction](https://arxiv.org/abs/2303.04132) builds on the idea that even for hard tasks of interest (with input X and Y) -- for which human-annotation is not practical and high-quality annotated data is not available -- by reversing the task (from Y to X), useful data can be synthetically generated even when that original task cannot be solved directly by the LLM. This process enables the creation of a high-quality dataset of X-Y pairs that will enable the training/fine-tuning of models for the original task of interest.
In particular, the paper studies the idea in the context of closed information extraction (IE), where a model is tasked with extracting the exhaustive set of facts expressed in natural language text. The synthetic data generation pipeline proposed in the paper comprises three primary components: (i) construction of a knowledge graph containing the entities and relations of interest; (ii) sampling of coherent triplet sets from the KG with comprehensive coverage of the entities and relations, and (iii) generation of high-quality text, expressing the triplets without any supplementary information. For more details regarding the dataset construction procedure, see the [paper](https://arxiv.org/abs/2303.04132).

We used this pipeline to generate two large high-quality datasets:<br>
**SynthIE-code**: consisting of around 1.8M training, 10K validation, and 50K test samples generated with [code-davinci-002](https://platform.openai.com/docs/models/gpt-3-5) <br>
**SynthIE-text**: consisting of 10K validation and 50K test samples generated with [text-davinci-003](https://platform.openai.com/docs/models/gpt-3-5) <br>
The text for the validation and test data points in SynthIE-code and SynthIE-text corresponds to the same triplet sets.

The resulting data is then used to train [SynthIE](https://github.com/epfl-dlab/SynthIE), a series of T5-based versions of [GenIE](https://github.com/epfl-dlab/GenIE) -- a recently proposed autoregressive closed IE system; as well as to enable a more accurate evaluation. As a baseline, T5 versions of GenIE are trained on the same dataset, [REBEL](https://aclanthology.org/2021.findings-emnlp.204.pdf), as the original work. The (processed) version of this dataset, suitable for closed IE and used in the paper's experiments, is provided in this repository.
According to the human evaluation conducted in the paper, the synthetically generated data is substantially more faithful than the distantly supervised REBEL and contains around 15\% false negative (opposed to REBEL's 70\%) and 22\% false positive (opposed to REBEL's 56\%) annotations while uniformly covering all relations (see the paper for more details).

### Languages

To stay comparable to GenIE, [SynthIE](https://github.com/epfl-dlab/SynthIE) considers only English. Therefore, the text in SynthIE-code and SynthIE-text is generated in English only. However, the triplets' constituents come from WikiData and are language invariant. Therefore, triplet sets with labels for many languages can easily be obtained.

## Dataset Structure

The SynthIE meta-dataset actually comprises 3 datasets:
- **SynthIE-code** (`synthie_code`)
- **SynthIE-text** (`synthie_text`)
- **REBEL** (`rebel`)

**SynCode**

The samples in this dataset were generated with `code-davinci-002`.

|                            | Train   | Valid | Test |
| -----                      | ----- | ----- | ----- |
| Data Points            |  1,815,378  | 10,000 | 50,286 |
| Triplets          |  6,055,911 | 34,262 | 172,991 |
| Entities |  1,806,126 | 27,553 | 105,176 |
| Relations |  888 | 883 | 888 |

**SynthIE-text**

The samples in this dataset were generated with `text-davinci-003`.

|                            | Train   | Valid | Test |
| -----                      | ----- | ----- | ----- |
| Data Points            |  -- | 10,000 | 50,286 |
| Triplets          |  -- | 34,262 | 172,991 |
| Entities |  -- | 27,553 | 105,176 |
| Relations |  -- | 883 | 888 |

**REBEL**

The samples in this dataset are processed and further annotated from the already existing [REBEL](https://huggingface.co/datasets/Babelscape/rebel-dataset) dataset.

|                            | Train   | Valid | Test |
| -----                      | ----- | ----- | ----- |
| Data Points            |  2,813,210 | 155,926 | 156,449 |
| Triplets          |  7,187,915 | 397,326 | 398,252 |
| Entities |  2,038,741 | 205,080 | 205,549 |
| Relations |  1071 | 691 | 690 |

Note that REBEL is substantially more skewed than SynCode and SynthIE-text. Here are the relation frequency (in terms of data points) statistics for REBEL and SynCode.
|                            | min   | 1st quantile | median | 3rd quantile | max |
| -----                      | ----- | ----- | ----- | ----- | ----- |
| SynCode            |  61 | 1043 | 1691 | 3944 | 499,783 |
| REBEL            |  1  | 7 | 47 | 625 | 1,202,489 |


**SynCode/SynthIE-text/REBEL processed**

Additionally, we provide a processed version (that was used in the paper) of each dataset. The processing consists of pre-computations/pre-processing that were run to speed the data loading for the experiments. The key difference is that in the processed version of SynthIE-code and SynthIE-text, the target triplets are consistently ordered according to a heuristic detecting the constituent entities' appearance position in the text, with triplets corresponding to entities appearing earlier in the output linearization (cf. paper). The triplets for REBEL are ordered even in the "unprocessed version". To load the processed version of the dataset, add the suffix "_pc" to the original identifier (i.e., synthie_code_pc, synthie_text_pc, rebel_pc). The processing is performed by applying [this](https://github.com/epfl-dlab/SynthIE/blob/main/scripts/pre_computing.py) script on the original data. 


### Data Fields

All of the datasets share the same schema. Here is a list of the fields paired with a description.

- `id`: A unique numeric identifier, starting from 0 for each dataset.
- `text`: A string expressing the text corresponding to this sample.
- `triplets`: A list of triplets that are expressed in the text. Each triplet corresponds to a dictionary
  - `subject`: The subject refers to an entity. It is a dictionary of:
    - `surfaceform`: A textual label corresponding to the title of the entity's English Wikipedia page
    - `uri`: A string corresponding to the entity's WikiData identifier 
  - `relation`: The relation refers to a relation. It is a dictionary of:
    - `surfaceform`: The textual label assigned to the WikiData item corresponding to the given relation.
    - `uri`: A string corresponding to the relation's WikiData identifier 
  - `object`: Same as the subject, the object refers to an entity and corresponds to a dictionary with the same structure.
- `entities`: A list comprising all the entities expressed in the text (appearing as a subject or an object in any of the triplets). Each entity is expressed as a dictionary following the same structure as the `subject` and `object` entities in the triplet list. 
- `relations`: A list comprising all the relations expressed in the text (appearing as the relation in any of the triplets). Each relation is expressed as a dictionary following the same structure as the `relation` in the triplet list. 

Here is an example of a data point:

```
{'id': 1,
 'text': 'The Journal of Colloid and Interface Science is a bibliographic '
         'review indexed in Scopus and published by Elsevier. Its main subject '
         'is chemical engineering, and it is written in the English language. '
         'It is based in the United States, and is owned by Elsevier, the same '
         'company that owns Scopus.',
 'triplets': [{'subject': "{'surfaceform': "
                          "'Journal_of_Colloid_and_Interface_Science', 'uri': "
                          "'Q3902043'}",
               'predicate': "{'surfaceform': 'indexed in bibliographic "
                            "review', 'uri': 'P8875'}",
               'object': "{'surfaceform': 'Scopus', 'uri': 'Q371467'}"},
              {'subject': "{'surfaceform': "
                          "'Journal_of_Colloid_and_Interface_Science', 'uri': "
                          "'Q3902043'}",
               'predicate': "{'surfaceform': 'main subject', 'uri': 'P921'}",
               'object': "{'surfaceform': 'Chemical_engineering', 'uri': "
                         "'Q83588'}"},
              {'subject': "{'surfaceform': "
                          "'Journal_of_Colloid_and_Interface_Science', 'uri': "
                          "'Q3902043'}",
               'predicate': "{'surfaceform': 'language of work or name', "
                            "'uri': 'P407'}",
               'object': "{'surfaceform': 'English_language', 'uri': 'Q1860'}"},
              {'subject': "{'surfaceform': "
                          "'Journal_of_Colloid_and_Interface_Science', 'uri': "
                          "'Q3902043'}",
               'predicate': "{'surfaceform': 'publisher', 'uri': 'P123'}",
               'object': "{'surfaceform': 'Elsevier', 'uri': 'Q746413'}"},
              {'subject': "{'surfaceform': "
                          "'Journal_of_Colloid_and_Interface_Science', 'uri': "
                          "'Q3902043'}",
               'predicate': "{'surfaceform': 'country of origin', 'uri': "
                            "'P495'}",
               'object': "{'surfaceform': 'United_States', 'uri': 'Q30'}"},
              {'subject': "{'surfaceform': 'Scopus', 'uri': 'Q371467'}",
               'predicate': "{'surfaceform': 'owned by', 'uri': 'P127'}",
               'object': "{'surfaceform': 'Elsevier', 'uri': 'Q746413'}"}],
 'entities': [{'surfaceform': 'Journal_of_Colloid_and_Interface_Science',
               'uri': 'Q3902043'},
              {'surfaceform': 'Scopus', 'uri': 'Q371467'},
              {'surfaceform': 'Chemical_engineering', 'uri': 'Q83588'},
              {'surfaceform': 'English_language', 'uri': 'Q1860'},
              {'surfaceform': 'Elsevier', 'uri': 'Q746413'},
              {'surfaceform': 'United_States', 'uri': 'Q30'}],
 'relations': [{'surfaceform': 'indexed in bibliographic review',
                'uri': 'P8875'},
               {'surfaceform': 'main subject', 'uri': 'P921'},
               {'surfaceform': 'language of work or name', 'uri': 'P407'},
               {'surfaceform': 'publisher', 'uri': 'P123'},
               {'surfaceform': 'country of origin', 'uri': 'P495'},
               {'surfaceform': 'owned by', 'uri': 'P127'}]}
```

### Data Splits

Each dataset (except SynthIE-text, which does not have a train set) has the same 4 splits: 
- `train`
- `validation`
- `test`
- `test_small`

The first three are self-explanatory; the `test_small` split corresponds to a randomly sampled subset of the `test` split in which the IDs of the data points are kept the same as in the test set from which they were sampled (i.e., after the sampling IDs are not reset to 0 and resigned).


## Dataset Creation

Collecting datasets for the closed IE task is time-consuming, expensive, and even hardly feasible, as it requires annotators to know the entire entity and relation catalogs and reason about all possible facts expressed in the text. As a result, only small or noisy datasets exist. The only large dataset available, REBEL, suffers from several problems: (i) Noise: it is constructed based on distant supervision, and for many data points, the target set does not contain all the facts expressed in the text or is partially incorrect; (ii) Skewness: most relations appear only a few times in the dataset, resulting in models that ignore most of the information when used for training and poor estimates of performance when used for evaluation.

This dataset is constructed using a synthetic data generation pipeline, proposed in the paper [Exploiting Asymmetry for Synthetic Training Data Generation: SynthIE and the Case of Information Extraction](https://arxiv.org/abs/2303.04132), and serves as a use case for a task for which (i) high-quality annotated data is not available; (ii) human-annotation is not practical; (iii) the direct task (closed IE) is challenging for an LLM. Concretely, by reversing the task and generating the data in the opposite direction -- going from triplets to text -- high-quality useful data can be generated. The pipeline used to construct the dataset comprises three components: (i) construction of a knowledge graph containing the entities and relations of interest; (ii) sampling of coherent triplet sets from the KG with comprehensive coverage of the entities and relations, and (iii) generation of high-quality text, expressing the triplets without any supplementary information. For more details regarding the dataset construction procedure and considerations for using the data, see the "Synthetic Data Generation", "Discussion", and "Limitations" sections of the [paper](https://arxiv.org/abs/2303.04132).

## Additional Information

### Licensing Information

The dataset is licensed under the terms of the MIT license.

### Citation Information
```
@article{josifoski2023exploiting,
  title={Exploiting Asymmetry for Synthetic Training Data Generation: {S}ynth{IE} and The Case of Information Extraction},
  author={Josifoski, Martin and Sakota, Marija and Peyrard, Maxime and West, Robert},
  journal={arXiv preprint arXiv:2303.04132},
  year={2023}
}
```
