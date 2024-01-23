# Dataset Card for NBAiLab/NCC_small_100


annotations_creators:
- no-annotation
language_creators:
- found
languages:
- en,nb,no,nn,se,dk,is,fo
licenses:
- odc-by-1.0
multilinguality:
- multilingual
pretty_name: NCC
size_categories:
- 2G<n<1B
source_datasets:
- original
task_categories:
- sequence-modeling
task_ids:
- language-modeling


## Table of Contents
- [Dataset Description](#dataset-description)
- [Dataset Summary](#dataset-summary)
- [Data Fields](#data-fiels)
- [Dataset Creation](#dataset-creation)
- [Statistics](#statistics)
- [Document Types](#document-types)
- [Languages](#languages)
- [Publish Periode](#publish-periode)
- [Considerations for Using the Data](#considerations-for-using-the-data)
- [Social Impact of Dataset](#social-impact-of-dataset)
- [Discussion of Biases](#discussion-of-biases)
- [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
- [Dataset Curators](#dataset-curators)
- [Licensing Information](#licensing-information)
- [Citation Information](#citation-information)

## Dataset Description
- **Homepage:** https://github.com/NBAiLab/notram
- **Repository:** https://github.com/NBAiLab/notram
- **Paper:** https://arxiv.org/abs/2104.09617
- **Point of Contact:** [Freddy Wetjen](mailto:freddy.wetjen@nb.no)

The Norwegian Colossal Corpus is a collection of multiple smaller Norwegian corpuses suitable for training large language models. We have done extensive cleaning on the datasets, and have made them available in a common format. The total size of the NCC is currently 45GB. 

## How to Use
```python
from datasets import load_dataset
data = load_dataset("NBAiLab/NCC_small_100", streaming=True)
```
## Download Data
If you do not want to use the HuggingFace Dataset-library for training, or if you want to do additional pre-processing, it is also possible to download the files locally.
```bash
# Download all files in one batch operation

for i in $(seq -f "%04g" 1 100): do wget https://huggingface.co/datasets/NbAiLab/NCC_small_100/blob/main/data/train-shard-$i-of-0100.json.gz &; done
# Create one large training file of all shards without unpacking
cat *.gz > onefile.json.gz
```

<details>
<summary>List of all the files.</summary>


* [train-shard-0001-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0001-of-0100.json.gz)
* [train-shard-0002-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0002-of-0100.json.gz)
* [train-shard-0003-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0003-of-0100.json.gz)
* [train-shard-0004-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0004-of-0100.json.gz)
* [train-shard-0005-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0005-of-0100.json.gz)
* [train-shard-0006-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0006-of-0100.json.gz)
* [train-shard-0007-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0007-of-0100.json.gz)
* [train-shard-0008-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0008-of-0100.json.gz)
* [train-shard-0009-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0009-of-0100.json.gz)
* [train-shard-0010-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0010-of-0100.json.gz)
* [train-shard-0011-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0011-of-0100.json.gz)
* [train-shard-0012-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0012-of-0100.json.gz)
* [train-shard-0013-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0013-of-0100.json.gz)
* [train-shard-0014-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0014-of-0100.json.gz)
* [train-shard-0015-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0015-of-0100.json.gz)
* [train-shard-0016-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0016-of-0100.json.gz)
* [train-shard-0017-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0017-of-0100.json.gz)
* [train-shard-0018-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0018-of-0100.json.gz)
* [train-shard-0019-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0019-of-0100.json.gz)
* [train-shard-0020-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0020-of-0100.json.gz)
* [train-shard-0021-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0021-of-0100.json.gz)
* [train-shard-0022-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0022-of-0100.json.gz)
* [train-shard-0023-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0023-of-0100.json.gz)
* [train-shard-0024-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0024-of-0100.json.gz)
* [train-shard-0025-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0025-of-0100.json.gz)
* [train-shard-0026-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0026-of-0100.json.gz)
* [train-shard-0027-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0027-of-0100.json.gz)
* [train-shard-0028-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0028-of-0100.json.gz)
* [train-shard-0029-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0029-of-0100.json.gz)
* [train-shard-0030-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0030-of-0100.json.gz)
* [train-shard-0031-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0031-of-0100.json.gz)
* [train-shard-0032-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0032-of-0100.json.gz)
* [train-shard-0033-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0033-of-0100.json.gz)
* [train-shard-0034-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0034-of-0100.json.gz)
* [train-shard-0035-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0035-of-0100.json.gz)
* [train-shard-0036-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0036-of-0100.json.gz)
* [train-shard-0037-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0037-of-0100.json.gz)
* [train-shard-0038-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0038-of-0100.json.gz)
* [train-shard-0039-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0039-of-0100.json.gz)
* [train-shard-0040-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0040-of-0100.json.gz)
* [train-shard-0041-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0041-of-0100.json.gz)
* [train-shard-0042-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0042-of-0100.json.gz)
* [train-shard-0043-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0043-of-0100.json.gz)
* [train-shard-0044-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0044-of-0100.json.gz)
* [train-shard-0045-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0045-of-0100.json.gz)
* [train-shard-0046-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0046-of-0100.json.gz)
* [train-shard-0047-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0047-of-0100.json.gz)
* [train-shard-0048-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0048-of-0100.json.gz)
* [train-shard-0049-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0049-of-0100.json.gz)
* [train-shard-0050-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0050-of-0100.json.gz)
* [train-shard-0051-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0051-of-0100.json.gz)
* [train-shard-0052-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0052-of-0100.json.gz)
* [train-shard-0053-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0053-of-0100.json.gz)
* [train-shard-0054-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0054-of-0100.json.gz)
* [train-shard-0055-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0055-of-0100.json.gz)
* [train-shard-0056-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0056-of-0100.json.gz)
* [train-shard-0057-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0057-of-0100.json.gz)
* [train-shard-0058-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0058-of-0100.json.gz)
* [train-shard-0059-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0059-of-0100.json.gz)
* [train-shard-0060-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0060-of-0100.json.gz)
* [train-shard-0061-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0061-of-0100.json.gz)
* [train-shard-0062-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0062-of-0100.json.gz)
* [train-shard-0063-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0063-of-0100.json.gz)
* [train-shard-0064-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0064-of-0100.json.gz)
* [train-shard-0065-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0065-of-0100.json.gz)
* [train-shard-0066-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0066-of-0100.json.gz)
* [train-shard-0067-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0067-of-0100.json.gz)
* [train-shard-0068-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0068-of-0100.json.gz)
* [train-shard-0069-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0069-of-0100.json.gz)
* [train-shard-0070-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0070-of-0100.json.gz)
* [train-shard-0071-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0071-of-0100.json.gz)
* [train-shard-0072-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0072-of-0100.json.gz)
* [train-shard-0073-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0073-of-0100.json.gz)
* [train-shard-0074-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0074-of-0100.json.gz)
* [train-shard-0075-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0075-of-0100.json.gz)
* [train-shard-0076-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0076-of-0100.json.gz)
* [train-shard-0077-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0077-of-0100.json.gz)
* [train-shard-0078-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0078-of-0100.json.gz)
* [train-shard-0079-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0079-of-0100.json.gz)
* [train-shard-0080-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0080-of-0100.json.gz)
* [train-shard-0081-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0081-of-0100.json.gz)
* [train-shard-0082-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0082-of-0100.json.gz)
* [train-shard-0083-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0083-of-0100.json.gz)
* [train-shard-0084-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0084-of-0100.json.gz)
* [train-shard-0085-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0085-of-0100.json.gz)
* [train-shard-0086-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0086-of-0100.json.gz)
* [train-shard-0087-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0087-of-0100.json.gz)
* [train-shard-0088-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0088-of-0100.json.gz)
* [train-shard-0089-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0089-of-0100.json.gz)
* [train-shard-0090-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0090-of-0100.json.gz)
* [train-shard-0091-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0091-of-0100.json.gz)
* [train-shard-0092-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0092-of-0100.json.gz)
* [train-shard-0093-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0093-of-0100.json.gz)
* [train-shard-0094-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0094-of-0100.json.gz)
* [train-shard-0095-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0095-of-0100.json.gz)
* [train-shard-0096-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0096-of-0100.json.gz)
* [train-shard-0097-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0097-of-0100.json.gz)
* [train-shard-0098-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0098-of-0100.json.gz)
* [train-shard-0099-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0099-of-0100.json.gz)
* [train-shard-0100-of-0100](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/train-shard-0100-of-0100.json.gz)
* [validation-shard-0001-of-0001](https://huggingface.co/datasets/NbAiLab/NCC_small_100/resolve/main/data/validation-shard-0001-of-0001.json.gz)


</details>

### Dataset Summary
The NCC_small_100 dataset contains json lines with language training data. Here is an example json line:
```json
{
"id": "1006205",
"doc_type": "cc100",
"publish_year": 2021,
"lang_fasttext": "nn",
"lang_fasttext_conf": "0.641",
"text": "Eg har ein PLAN! KOS deg og ha ei fin helg"
}
```
## Data Fields
|**id:** | String with id to source of line and a unique identifier|
|:-----------|:------------|
|**doc_type ** | String describing type of media text extracted from (I.e. book,newspaper etc)|
|**publish_year ** | Integer. The year text published. When year is undetermined it is set to 2021.|
|**lang_fasttext ** | String. Language of text identified by FastText|
|**lang_fasttext_conf ** | String. Confidence calculated by FastText|
|**text ** | String. The complete utf-8 document. If longer than 1M characters it is split.|

### Dataset Creation
We are providing a **train** and a **validation** split. The standard size of the validation is a single 1GB file, while train is sharded in 1GB chunks.
All files are gzipped.

Build date: 03122021

#### Initial Data Collection and Curation
The procedure for the dataset creation is described in detail in our paper.

### Summary
| Words       | Documents   |   Words/Document |
|------------:|------------:|-----------------:|
| 152,828,370 | 452,838     |              337 |

### Document Types
| Source                                | Words      | Documents   | Words/Document   |
|--------------------------------------:|-----------:|------------:|-----------------:|
| newspaper_ocr                         | 42,875,141 | 214,047     | 200              |
| parliament                            | 27,906,014 | 201         | 138,835          |
| books                                 | 19,806,532 | 546         | 36,275           |
| newspapers_online_nb                  | 10,681,495 | 75,216      | 142              |
| maalfrid_regjeringen                  | 7,884,471  | 20,124      | 391              |
| maalfrid_ssb                          | 6,101,595  | 18,502      | 329              |
| maalfrid_uio                          | 3,891,127  | 16,548      | 235              |
| government_nb                         | 3,399,192  | 100         | 33,991           |
| wikipedia_download_nbo                | 2,520,875  | 11,481      | 219              |
| maalfrid_fylkesmannen                 | 2,234,608  | 10,150      | 220              |
| publicreports                         | 2,198,220  | 82          | 26,807           |
| maalfrid_nve                          | 1,430,464  | 6,458       | 221              |
| maalfrid_patentstyret                 | 1,367,518  | 4,551       | 300              |
| maalfrid_ntnu                         | 1,266,953  | 4,378       | 289              |
| newspapers_online_nn                  | 913,353    | 3,679       | 248              |
| maalfrid_fhi                          | 729,409    | 3,167       | 230              |
| maalfrid_vegvesen                     | 710,333    | 3,545       | 200              |
| maalfrid_norad                        | 708,294    | 2,017       | 351              |
| lovdata_cd_odelsting_2005             | 696,273    | 43          | 16,192           |
| maalfrid_skatteetaten                 | 679,125    | 1,753       | 387              |
| maalfrid_uib                          | 615,724    | 2,483       | 247              |
| wikipedia_download_nno                | 592,536    | 3,181       | 186              |
| maalfrid_forskningsradet              | 526,472    | 1,604       | 328              |
| maalfrid_nasjonalparkstyre            | 467,226    | 2,013       | 232              |
| maalfrid_nmbu                         | 406,053    | 1,578       | 257              |
| maalfrid_domstol                      | 382,629    | 1,121       | 341              |
| maalfrid_oslomet                      | 380,272    | 1,002       | 379              |
| maalfrid_nav                          | 363,539    | 1,670       | 217              |
| maalfrid_banenor                      | 338,844    | 1,479       | 229              |
| maalfrid_landbruksdirektoratet        | 293,549    | 1,048       | 280              |
| maalfrid_helsedirektoratet            | 289,269    | 1,076       | 268              |
| government_nn                         | 281,763    | 25          | 11,270           |
| maalfrid_udir                         | 228,128    | 874         | 261              |
| maalfrid_nokut                        | 226,072    | 877         | 257              |
| maalfrid_norges-bank                  | 224,812    | 829         | 271              |
| maalfrid_vkm                          | 214,855    | 683         | 314              |
| maalfrid_nbim                         | 214,235    | 417         | 513              |
| maalfrid_hi                           | 209,748    | 848         | 247              |
| maalfrid_ngu                          | 209,454    | 794         | 263              |
| maalfrid_miljodirektoratet            | 208,346    | 757         | 275              |
| maalfrid_distriktssenteret            | 204,538    | 847         | 241              |
| maalfrid_ptil                         | 204,458    | 753         | 271              |
| maalfrid_nord                         | 193,119    | 961         | 200              |
| maalfrid_difi                         | 172,807    | 788         | 219              |
| maalfrid_fiskeridir                   | 172,337    | 714         | 241              |
| maalfrid_hivolda                      | 168,122    | 564         | 298              |
| maalfrid_mattilsynet                  | 165,226    | 616         | 268              |
| maalfrid_havarikommisjonen            | 164,555    | 555         | 296              |
| maalfrid_kulturradet                  | 151,989    | 472         | 322              |
| maalfrid_kystverket                   | 151,671    | 686         | 221              |
| maalfrid_ks                           | 149,000    | 563         | 264              |
| maalfrid_udi                          | 141,628    | 429         | 330              |
| maalfrid_uia                          | 134,214    | 535         | 250              |
| maalfrid_hjelpemiddeldatabasen        | 129,178    | 764         | 169              |
| maalfrid_dsb                          | 127,197    | 423         | 300              |
| maalfrid_khrono                       | 124,208    | 432         | 287              |
| maalfrid_helsetilsynet                | 123,804    | 397         | 311              |
| lovdata_cd_somb_rundskriv_2005        | 121,983    | 68          | 1,793            |
| maalfrid_veiviseren                   | 116,185    | 388         | 299              |
| lovdata_cd_sentrale_forskrifter_2005  | 114,379    | 251         | 455              |
| maalfrid_moreforsk                    | 114,223    | 451         | 253              |
| maalfrid_husbanken                    | 112,257    | 359         | 312              |
| maalfrid_forsvarsbygg                 | 109,309    | 441         | 247              |
| maalfrid_imdi                         | 108,090    | 357         | 302              |
| maalfrid_jernbanedirektoratet         | 107,264    | 435         | 246              |
| maalfrid_konkurransetilsynet          | 106,330    | 296         | 359              |
| maalfrid_inn                          | 102,298    | 613         | 166              |
| maalfrid_legemiddelverket             | 100,455    | 452         | 222              |
| maalfrid_dsa                          | 100,141    | 353         | 283              |
| maalfrid_hiof                         | 99,743     | 528         | 188              |
| maalfrid_vetinst                      | 97,390     | 312         | 312              |
| maalfrid_ehelse                       | 95,975     | 496         | 193              |
| maalfrid_arkivverket                  | 94,310     | 360         | 261              |
| maalfrid_sdir                         | 94,192     | 311         | 302              |
| maalfrid_klagenemndssekretariatet     | 87,830     | 258         | 340              |
| maalfrid_dibk                         | 84,106     | 336         | 250              |
| maalfrid_nhh                          | 81,294     | 317         | 256              |
| maalfrid_sprakradet                   | 80,918     | 315         | 256              |
| maalfrid_toll                         | 79,364     | 305         | 260              |
| maalfrid_politiet                     | 78,471     | 240         | 326              |
| maalfrid_vestlandfylke                | 77,600     | 304         | 255              |
| maalfrid_riksrevisjonen               | 77,117     | 225         | 342              |
| maalfrid_met                          | 76,310     | 400         | 190              |
| maalfrid_artsdatabanken               | 76,117     | 200         | 380              |
| maalfrid_kartverket                   | 75,468     | 397         | 190              |
| maalfrid_bufdir                       | 75,375     | 262         | 287              |
| maalfrid_nibio                        | 74,594     | 386         | 193              |
| maalfrid_nkom                         | 63,734     | 215         | 296              |
| maalfrid_npd                          | 63,605     | 260         | 244              |
| maalfrid_nlr                          | 61,251     | 364         | 168              |
| maalfrid_aldringoghelse               | 58,322     | 147         | 396              |
| maalfrid_uis                          | 57,580     | 190         | 303              |
| maalfrid_custompublish                | 56,876     | 219         | 259              |
| maalfrid_nyemetoder                   | 56,634     | 245         | 231              |
| maalfrid_sykkelbynettverket           | 53,461     | 230         | 232              |
| maalfrid_arbeidstilsynet              | 52,903     | 127         | 416              |
| maalfrid_luftfartstilsynet            | 51,929     | 221         | 234              |
| maalfrid_seniorporten                 | 50,569     | 159         | 318              |
| maalfrid_bioteknologiradet            | 49,956     | 129         | 387              |
| maalfrid_riksantikvaren               | 49,722     | 187         | 265              |
| maalfrid_sjt                          | 47,006     | 230         | 204              |
| maalfrid_dfo                          | 46,582     | 206         | 226              |
| maalfrid_hvl                          | 46,544     | 202         | 230              |
| lovdata_cd_lokaleforskrifter_2005     | 46,482     | 476         | 97               |
| maalfrid_forbrukerradet               | 44,620     | 157         | 284              |
| maalfrid_himolde                      | 43,761     | 226         | 193              |
| maalfrid_kompetansenorge              | 43,626     | 213         | 204              |
| maalfrid_ldo                          | 41,409     | 153         | 270              |
| lovdata_cd_norgeslover_2005           | 40,450     | 32          | 1,264            |
| maalfrid_forskningsetikk              | 39,574     | 127         | 311              |
| maalfrid_naku                         | 37,039     | 107         | 346              |
| maalfrid_usn                          | 35,982     | 154         | 233              |
| maalfrid_godeidrettsanlegg            | 35,482     | 145         | 244              |
| maalfrid_naturfag                     | 34,881     | 132         | 264              |
| maalfrid_matematikksenteret           | 34,258     | 158         | 216              |
| maalfrid_medietilsynet                | 33,904     | 145         | 233              |
| maalfrid_diskrimineringsnemnda        | 33,264     | 89          | 373              |
| maalfrid_nupi                         | 31,508     | 121         | 260              |
| maalfrid_miljopakken                  | 31,029     | 140         | 221              |
| lovdata_cd_rtv_rundskriv_2005         | 30,518     | 222         | 137              |
| maalfrid_dirmin                       | 30,360     | 117         | 259              |
| maalfrid_diku                         | 29,246     | 135         | 216              |
| maalfrid_arbeidsretten                | 27,492     | 92          | 298              |
| maalfrid_fellesstudentsystem          | 27,029     | 197         | 137              |
| maalfrid_kriminalitetsforebygging     | 26,971     | 104         | 259              |
| maalfrid_statsbygg                    | 26,256     | 102         | 257              |
| maalfrid_nb                           | 25,375     | 94          | 269              |
| maalfrid_nih                          | 25,036     | 112         | 223              |
| maalfrid_folketrygdfondet             | 25,027     | 91          | 275              |
| maalfrid_npolar                       | 24,843     | 62          | 400              |
| maalfrid_valgdirektoratet             | 23,205     | 205         | 113              |
| maalfrid_lottstift                    | 22,736     | 78          | 291              |
| maalfrid_naturfagsenteret             | 22,618     | 95          | 238              |
| maalfrid_samordnaopptak               | 22,400     | 56          | 400              |
| maalfrid_sykehuspartner               | 21,855     | 108         | 202              |
| maalfrid_unit                         | 21,305     | 135         | 157              |
| lovdata_cd_rundskriv_lovavdeling_2005 | 21,295     | 10          | 2,129            |
| maalfrid_anskaffelser                 | 21,097     | 104         | 202              |
| maalfrid_barneombudet                 | 20,092     | 65          | 309              |
| maalfrid_mareano                      | 19,922     | 91          | 218              |
| maalfrid_datatilsynet                 | 19,845     | 55          | 360              |
| maalfrid_fiskeridirektoratet          | 18,831     | 60          | 313              |
| maalfrid_spesialenheten               | 18,550     | 47          | 394              |
| maalfrid_xn--miljlftet-o8ab           | 18,447     | 78          | 236              |
| lovdata_cd_skatt_rundskriv_2005       | 18,316     | 7           | 2,616            |
| maalfrid_skrivesenteret               | 17,951     | 102         | 175              |
| maalfrid_khio                         | 16,924     | 63          | 268              |
| maalfrid_bibliotekutvikling           | 16,631     | 89          | 186              |
| maalfrid_helsenorge                   | 15,431     | 60          | 257              |
| maalfrid_sykehusinnkjop               | 15,204     | 92          | 165              |
| maalfrid_spk                          | 13,824     | 44          | 314              |
| maalfrid_aho                          | 13,268     | 78          | 170              |
| maalfrid_matportalen                  | 12,756     | 51          | 250              |
| maalfrid_nfi                          | 12,696     | 36          | 352              |
| maalfrid_samas                        | 12,650     | 62          | 204              |
| maalfrid_kunstkultursenteret          | 12,307     | 35          | 351              |
| maalfrid_nhn                          | 12,156     | 77          | 157              |
| maalfrid_pasientsikkerhetsprogrammet  | 11,892     | 91          | 130              |
| maalfrid_ceres                        | 11,310     | 44          | 257              |
| maalfrid_nysgjerrigper                | 11,177     | 63          | 177              |
| maalfrid_une                          | 11,036     | 23          | 479              |
| maalfrid_nynorsksenteret              | 10,822     | 45          | 240              |
| maalfrid_natursekken                  | 10,060     | 73          | 137              |
| maalfrid_nidsenter                    | 9,996      | 34          | 294              |
| maalfrid_nsm                          | 9,926      | 39          | 254              |
| maalfrid_justervesenet                | 9,847      | 29          | 339              |
| maalfrid_giek                         | 9,769      | 39          | 250              |
| maalfrid_digdir                       | 9,675      | 54          | 179              |
| maalfrid_stami                        | 9,518      | 22          | 432              |
| maalfrid_sshf                         | 9,488      | 37          | 256              |
| maalfrid_kriminalomsorgen             | 9,126      | 32          | 285              |
| maalfrid_vinmonopolet                 | 9,094      | 22          | 413              |
| maalfrid_nodnett                      | 8,738      | 50          | 174              |
| maalfrid_gjenopptakelse               | 8,249      | 30          | 274              |
| maalfrid_fordelingsutvalget           | 8,242      | 28          | 294              |
| maalfrid_kjonnsforskning              | 8,010      | 22          | 364              |
| maalfrid_nasjonalmuseet               | 7,935      | 21          | 377              |
| maalfrid_forsvaret                    | 7,614      | 27          | 282              |
| maalfrid_ombudsmann                   | 7,496      | 12          | 624              |
| maalfrid_forbrukereuropa              | 7,260      | 28          | 259              |
| maalfrid_romsenter                    | 7,219      | 27          | 267              |
| maalfrid_ovf                          | 6,699      | 28          | 239              |
| maalfrid_beccle                       | 6,686      | 33          | 202              |
| maalfrid_forbrukertilsynet            | 6,440      | 19          | 338              |
| maalfrid_helfo                        | 5,746      | 21          | 273              |
| maalfrid_politietssikkerhetstjeneste  | 5,570      | 16          | 348              |
| maalfrid_geonorge                     | 5,228      | 35          | 149              |
| maalfrid_realfagsloyper               | 5,155      | 22          | 234              |
| maalfrid_opplaringslovutvalget        | 5,062      | 11          | 460              |
| maalfrid_vea-fs                       | 5,026      | 28          | 179              |
| maalfrid_energimerking                | 4,842      | 25          | 193              |
| maalfrid_jernbanemagasinet            | 4,663      | 14          | 333              |
| maalfrid_traumebevisst                | 4,456      | 50          | 89               |
| maalfrid_politihogskolen              | 4,434      | 27          | 164              |
| maalfrid_universell                   | 4,138      | 37          | 111              |
| maalfrid_nafkam                       | 4,096      | 11          | 372              |
| maalfrid_koro                         | 3,781      | 10          | 378              |
| maalfrid_npe                          | 3,744      | 21          | 178              |
| maalfrid_regionaleforskningsfond      | 3,512      | 23          | 152              |
| maalfrid_denkulturelleskolesekken     | 3,375      | 7           | 482              |
| maalfrid_squarespace                  | 3,310      | 12          | 275              |
| maalfrid_riksteatret                  | 3,143      | 12          | 261              |
| maalfrid_riksmekleren                 | 2,936      | 15          | 195              |
| maalfrid_pkh                          | 2,927      | 9           | 325              |
| maalfrid_konfliktraadet               | 2,918      | 9           | 324              |
| maalfrid_aasentunet                   | 2,713      | 8           | 339              |
| maalfrid_radetfordyreetikk            | 2,579      | 12          | 214              |
| maalfrid_generaladvokaten             | 2,428      | 7           | 346              |
| maalfrid_lanekassen                   | 2,237      | 7           | 319              |
| maalfrid_okokrim                      | 2,184      | 10          | 218              |
| maalfrid_kulturminnefondet            | 2,157      | 10          | 215              |
| maalfrid_whocc                        | 2,143      | 13          | 164              |
| maalfrid_brreg                        | 2,140      | 13          | 164              |
| maalfrid_polarhistorie                | 2,016      | 7           | 288              |
| maalfrid_unknown                      | 2,015      | 11          | 183              |
| maalfrid_ffi                          | 2,010      | 6           | 335              |
| maalfrid_finansportalen               | 1,967      | 7           | 281              |
| maalfrid_digidel                      | 1,701      | 10          | 170              |
| maalfrid_sismo                        | 1,685      | 6           | 280              |
| maalfrid_nlb                          | 1,665      | 5           | 333              |
| maalfrid_lektor2                      | 1,397      | 8           | 174              |
| maalfrid_sivilforsvaret               | 1,365      | 8           | 170              |
| maalfrid_konkursradet                 | 1,309      | 4           | 327              |
| maalfrid_varsom                       | 1,281      | 10          | 128              |
| maalfrid_informasjonskompetanse       | 1,254      | 8           | 156              |
| maalfrid_skattefunn                   | 1,171      | 3           | 390              |
| maalfrid_sivilrett                    | 1,166      | 3           | 388              |
| maalfrid_uit                          | 1,112      | 16          | 69               |
| maalfrid_yrkesfisker                  | 1,110      | 10          | 111              |
| maalfrid_nbsk                         | 1,098      | 8           | 137              |
| maalfrid_lokforerskolen               | 1,075      | 7           | 153              |
| maalfrid_laudim                       | 1,069      | 8           | 133              |
| maalfrid_nyinorge                     | 1,064      | 2           | 532              |
| maalfrid_transport21                  | 1,030      | 4           | 257              |
| maalfrid_openaccess                   | 953        | 3           | 317              |
| maalfrid_sinn                         | 924        | 5           | 184              |
| maalfrid_htu                          | 881        | 4           | 220              |
| maalfrid_yr                           | 865        | 12          | 72               |
| maalfrid_akkreditert                  | 856        | 4           | 214              |
| maalfrid_helseklage                   | 855        | 3           | 285              |
| maalfrid_ssn                          | 841        | 5           | 168              |
| maalfrid_fug                          | 816        | 2           | 408              |
| maalfrid_matogindustri                | 780        | 6           | 130              |
| maalfrid_fordelingsutvalet            | 772        | 2           | 386              |
| maalfrid_dekom                        | 764        | 18          | 42               |
| maalfrid_lokalhistorie                | 753        | 3           | 251              |
| maalfrid_unesco                       | 749        | 4           | 187              |
| maalfrid_omsorgsforskning             | 711        | 5           | 142              |
| maalfrid_pts                          | 651        | 2           | 325              |
| maalfrid_valg                         | 638        | 2           | 319              |
| maalfrid_forbrukerklageutvalget       | 626        | 2           | 313              |
| maalfrid_miljoklagenemnda             | 625        | 3           | 208              |
| maalfrid_regjeringsadvokaten          | 616        | 2           | 308              |
| maalfrid_iearth                       | 552        | 3           | 184              |
| maalfrid_skeivtarkiv                  | 552        | 4           | 138              |
| maalfrid_xn--kvinneligomskjring-1ub   | 514        | 1           | 514              |
| maalfrid_haldenfengsel                | 469        | 1           | 469              |
| maalfrid_hjelpelinjen                 | 466        | 2           | 233              |
| maalfrid_sevuppt                      | 429        | 1           | 429              |
| maalfrid_norec                        | 376        | 1           | 376              |
| maalfrid_kk-utvalget                  | 348        | 1           | 348              |
| maalfrid_ah                           | 346        | 1           | 346              |
| maalfrid_lykillinn                    | 331        | 1           | 331              |
| maalfrid_vergemal                     | 319        | 1           | 319              |
| maalfrid_riksadvokaten                | 315        | 2           | 157              |
| maalfrid_global                       | 301        | 1           | 301              |
| maalfrid_webhuset                     | 280        | 1           | 280              |
| maalfrid_xn--tilbakefring-2jb         | 267        | 2           | 133              |
| maalfrid_oslofengsel                  | 266        | 1           | 266              |
| maalfrid_nasjonaleturistveger         | 227        | 1           | 227              |
| maalfrid_kulturped                    | 172        | 1           | 172              |
| maalfrid_altinn                       | 170        | 2           | 85               |
| maalfrid_shiprep                      | 165        | 2           | 82               |
| maalfrid_kulturoghelse                | 161        | 4           | 40               |
| maalfrid_kantinekurset                | 145        | 1           | 145              |
| maalfrid_designavgang                 | 145        | 1           | 145              |
| maalfrid_memu                         | 126        | 2           | 63               |
| maalfrid_alleteller                   | 123        | 1           | 123              |
| maalfrid_havmiljo                     | 118        | 1           | 118              |
| maalfrid_fmfiavo@fylkesmannen         | 81         | 2           | 40               |
| maalfrid_okopark                      | 61         | 1           | 61               |
| maalfrid_nynorskbok                   | 52         | 1           | 52               |
| maalfrid_uh-it                        | 47         | 2           | 23               |
| maalfrid_bastoyfengsel                | 46         | 1           | 46               |
| maalfrid_overgangsbolig               | 40         | 1           | 40               |
| maalfrid_spinn-inn                    | 37         | 2           | 18               |
| maalfrid_karriereveiledning           | 31         | 1           | 31               |
| maalfrid_norskpetroleum               | 15         | 2           | 7                |
| maalfrid_feide                        | 9          | 1           | 9                |

### Languages
| Language   | Words       | Documents   | Words/Document   |
|-----------:|------------:|------------:|-----------------:|
| no         | 110,561,181 | 373,475     | 296              |
| da         | 22,054,103  | 12,507      | 1,763            |
| en         | 10,551,361  | 33,082      | 318              |
| nn         | 6,400,816   | 21,583      | 296              |
| fr         | 1,150,970   | 2,354       | 488              |
| de         | 848,915     | 1,804       | 470              |
| sv         | 290,653     | 2,578       | 112              |
| es         | 238,453     | 910         | 262              |
| fi         | 138,410     | 984         | 140              |
| et         | 71,255      | 507         | 140              |
| cs         | 57,634      | 465         | 123              |
| oc         | 51,457      | 109         | 472              |
| pt         | 49,471      | 326         | 151              |
| nl         | 38,024      | 266         | 142              |
| la         | 36,388      | 20          | 1,819            |
| uk         | 31,820      | 107         | 297              |
| zh         | 27,640      | 181         | 152              |
| eu         | 25,582      | 74          | 345              |
| it         | 24,134      | 199         | 121              |
| ru         | 24,022      | 149         | 161              |
| pl         | 23,919      | 216         | 110              |
| ca         | 23,748      | 84          | 282              |
| gu         | 16,739      | 1           | 16,739           |
| fa         | 11,657      | 49          | 237              |
| hu         | 10,583      | 173         | 61               |
| is         | 10,225      | 37          | 276              |
| ja         | 9,563       | 109         | 87               |
| el         | 5,320       | 20          | 266              |
| id         | 5,254       | 44          | 119              |
| ar         | 4,268       | 20          | 213              |
| so         | 3,343       | 13          | 257              |
| sl         | 3,243       | 47          | 69               |
| vi         | 3,077       | 22          | 139              |
| sr         | 2,022       | 29          | 69               |
| hr         | 1,947       | 23          | 84               |
| tr         | 1,802       | 41          | 43               |
| gl         | 1,709       | 17          | 100              |
| mn         | 1,575       | 1           | 1,575            |
| lt         | 1,442       | 15          | 96               |
| am         | 1,405       | 6           | 234              |
| ko         | 1,301       | 29          | 44               |
| sq         | 1,265       | 8           | 158              |
| ro         | 1,214       | 13          | 93               |
| kk         | 1,092       | 2           | 546              |
| ur         | 1,003       | 5           | 200              |
| ml         | 986         | 6           | 164              |
| sh         | 939         | 5           | 187              |
| eo         | 755         | 14          | 53               |
| th         | 550         | 12          | 45               |
| ta         | 505         | 6           | 84               |
| sw         | 468         | 3           | 156              |
| sk         | 442         | 12          | 36               |
| war        | 369         | 3           | 123              |
| tl         | 340         | 2           | 170              |
| bg         | 327         | 1           | 327              |
| pnb        | 276         | 1           | 276              |
| bs         | 230         | 2           | 115              |
| ceb        | 196         | 6           | 32               |
| cy         | 182         | 2           | 91               |
| ku         | 175         | 1           | 175              |
| ga         | 102         | 6           | 17               |
| my         | 82          | 1           | 82               |
| hy         | 66          | 2           | 33               |
| ast        | 59          | 1           | 59               |
| ms         | 53          | 13          | 4                |
| be         | 40          | 1           | 40               |
| nds        | 30          | 6           | 5                |
| lv         | 30          | 3           | 10               |
| als        | 22          | 3           | 7                |
| mk         | 21          | 2           | 10               |
| as         | 17          | 1           | 17               |
| br         | 16          | 3           | 5                |
| af         | 13          | 1           | 13               |
| tt         | 12          | 2           | 6                |
| si         | 10          | 1           | 10               |
| su         | 8           | 1           | 8                |
| bn         | 8           | 1           | 8                |
| hsb        | 6           | 1           | 6                |
| jv         | 5           | 1           | 5                |
| fy         | 5           | 2           | 2                |
| az         | 5           | 1           | 5                |
| pms        | 4           | 1           | 4                |
| jbo        | 4           | 1           | 4                |
| lb         | 3           | 1           | 3                |
| io         | 3           | 1           | 3                |
| he         | 1           | 1           | 1                |

### Publish Periode
|   Decade | Words      | Documents   | Words/Document   |
|---------:|-----------:|------------:|-----------------:|
|     2020 | 90,368,489 | 238,255     | 568              |
|     2010 | 7,706,272  | 52,464      | 1,483            |
|     2000 | 10,118,391 | 36,978      | 3,135            |
|     1990 | 16,379,779 | 54,636      | 2,989            |
|     1980 | 3,378,092  | 11,838      | 2,845            |
|     1970 | 4,041,362  | 17,805      | 2,261            |
|     1960 | 3,523,333  | 17,974      | 1,971            |
|     1950 | 2,128,506  | 10,387      | 2,058            |
|     1940 | 2,662,606  | 12,271      | 2,521            |
|     1930 | 964,846    | 20          | 383,978          |
|     1920 | 744,560    | 16          | 328,756          |
|     1910 | 1,701,319  | 31          | 527,445          |
|     1900 | 1,183,273  | 24          | 414,972          |
|     1890 | 2,246,433  | 40          | 461,126          |
|     1880 | 1,059,838  | 19          | 490,702          |
|     1870 | 999,024    | 15          | 521,165          |
|     1860 | 842,042    | 17          | 533,772          |
|     1850 | 1,408,491  | 25          | 434,091          |
|     1840 | 627,004    | 10          | 398,914          |
|     1830 | 695,289    | 11          | 475,094          |
|     1820 | 49,421     | 2           | 49,421           |

## Considerations for Using the Data
This corpus contains data under copyright and is not allowed to be used outide the National Library of Norway. The dataset should not be distributed.

### Discussion of Biases
Please refer to our paper.

### Dataset Curators
Freddy.wetjen@nb.no
Per.Kummervold@nb.no

## License
Various licences applies to different parts of the corpus. Every document in the corpus has a tag telling what **"doc_type"** it belongs to. If you are unable to accept any of the licenses, you should filter out the **"doc_type"** with a conflicting license. 

| Doc_type  | License  | 
| :-------- | :------------- |  
| government_nb, government_nn, parliament, publicreports, lovdata_cd_\*, maalfrid_\* | [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|
| newspapers_ocr, newspapers_pdf, books| [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)|
| newspapers_online_nb, newspapers_online_nn | [CC BY-NC 2.0](https://creativecommons.org/licenses/by-nc/2.0/)|
| opensubtitles, wikipedia | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
|

### Citation Information
We are preparing an article with detailed information about this corpus. Until it is published, please cite out paper discussing the first version of this corpus:
```
@inproceedings{kummervold-etal-2021-operationalizing,
title = {Operationalizing a National Digital Library: The Case for a {N}orwegian Transformer Model},
author = {Kummervold, Per E  and
De la Rosa, Javier  and
Wetjen, Freddy  and
Brygfjeld, Svein Arne",
booktitle = {Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa)},
year = "2021",
address = "Reykjavik, Iceland (Online)",
publisher = {Link{"o}ping University Electronic Press, Sweden},
url = "https://aclanthology.org/2021.nodalida-main.3",
pages = "20--29",
abstract = "In this work, we show the process of building a large-scale training set from digital and digitized collections at a national library.
The resulting Bidirectional Encoder Representations from Transformers (BERT)-based language model for Norwegian outperforms multilingual BERT (mBERT) models
in several token and sequence classification tasks for both Norwegian Bokm{aa}l and Norwegian Nynorsk. Our model also improves the mBERT performance for other languages present in the corpus such as English, Swedish, and Danish. For languages not included in the corpus, the weights degrade moderately while keeping strong multilingual properties. Therefore, we show that building high-quality models within a memory institution using somewhat noisy optical character recognition (OCR) content is feasible, and we hope to pave the way for other memory institutions to follow.",
}
```
