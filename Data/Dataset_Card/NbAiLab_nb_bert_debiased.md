---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- en
- nb
- 'no'
- nn
- se
- dk
- is
- fo
license:
- odc-by
multilinguality:
- multilingual
size_categories:
- 2G<n<1B
source_datasets:
- original
task_categories:
- text-generation
task_ids:
- language-modeling
pretty_name: NCC
extra_gated_prompt: The Directive on Copyright in the Digital Single Market, which
  came into force on June 6 2019, amends the European Union copyright and database
  legislation and allows for Text and Data Mining (TDM) activities for research organizations
  and cultural heritage institutions. Under the terms of the aforementioned directive,
  by clicking on "Access repository" you agree on using the text and data contained
  in this dataset for non-commercial scientific purposes only.
---
# Dataset Card for NBAiLab/nb_bert_debiased


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
- **Homepage:** https://github.com/NbAiLab/notram
- **Repository:** https://github.com/NbAiLab/notram
- **Paper:** https://arxiv.org/abs/2104.09617
- **Point of Contact:** [Freddy Wetjen](mailto:freddy.wetjen@nb.no)

The Norwegian Colossal Corpus is a collection of multiple smaller Norwegian corpuses suitable for training large language models. We have done extensive cleaning on the datasets, and have made them available in a common format. The total size of the NCC is currently 45GB. 

## How to Use
```python
from datasets import load_dataset
data = load_dataset("NBAiLab/nb_bert_debiased", streaming=True)
```
## Download Data
If you do not want to use the HuggingFace Dataset-library for training, or if you want to do additional pre-processing, it is also possible to download the files locally.
```bash
# Clone the training set
git clone https://huggingface.co/datasets/NbAiLab/nb_bert_debiased

# Create one large training file of all shards without unpacking
cat nb_bert_debiased/data/train*.gz > onefile.json.gz
```

<details>
<summary>List of all the files.</summary>


* [train-shard-0001-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0001-of-0033.json.gz)
* [train-shard-0002-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0002-of-0033.json.gz)
* [train-shard-0003-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0003-of-0033.json.gz)
* [train-shard-0004-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0004-of-0033.json.gz)
* [train-shard-0005-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0005-of-0033.json.gz)
* [train-shard-0006-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0006-of-0033.json.gz)
* [train-shard-0007-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0007-of-0033.json.gz)
* [train-shard-0008-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0008-of-0033.json.gz)
* [train-shard-0009-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0009-of-0033.json.gz)
* [train-shard-0010-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0010-of-0033.json.gz)
* [train-shard-0011-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0011-of-0033.json.gz)
* [train-shard-0012-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0012-of-0033.json.gz)
* [train-shard-0013-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0013-of-0033.json.gz)
* [train-shard-0014-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0014-of-0033.json.gz)
* [train-shard-0015-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0015-of-0033.json.gz)
* [train-shard-0016-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0016-of-0033.json.gz)
* [train-shard-0017-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0017-of-0033.json.gz)
* [train-shard-0018-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0018-of-0033.json.gz)
* [train-shard-0019-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0019-of-0033.json.gz)
* [train-shard-0020-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0020-of-0033.json.gz)
* [train-shard-0021-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0021-of-0033.json.gz)
* [train-shard-0022-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0022-of-0033.json.gz)
* [train-shard-0023-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0023-of-0033.json.gz)
* [train-shard-0024-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0024-of-0033.json.gz)
* [train-shard-0025-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0025-of-0033.json.gz)
* [train-shard-0026-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0026-of-0033.json.gz)
* [train-shard-0027-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0027-of-0033.json.gz)
* [train-shard-0028-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0028-of-0033.json.gz)
* [train-shard-0029-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0029-of-0033.json.gz)
* [train-shard-0030-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0030-of-0033.json.gz)
* [train-shard-0031-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0031-of-0033.json.gz)
* [train-shard-0032-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0032-of-0033.json.gz)
* [train-shard-0033-of-0033](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/train-shard-0033-of-0033.json.gz)
* [validation-shard-0001-of-0001](https://huggingface.co/datasets/NbAiLab/nb_bert_debiased/resolve/main/data/validation-shard-0001-of-0001.json.gz)


</details>

### Dataset Summary
The nb_bert_debiased dataset contains json lines with language training data. Here is an example json line:
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
|**doc_type** | String describing type of media text extracted from (I.e. book,newspaper etc)|
|**publish_year** | Integer. The year text published. When year is undetermined it is set to 2021.|
|**lang_fasttext** | String. Language of text identified by FastText|
|**lang_fasttext_conf** | String. Confidence calculated by FastText|
|**text** | String. The complete utf-8 document. If longer than 1M characters it is split.|

### Dataset Creation
We are providing a **train** and a **validation** split. The standard size of the validation is a single 1GB file, while train is sharded in 1GB chunks.
All files are gzipped.

Build date: 01042022

#### Initial Data Collection and Curation
The procedure for the dataset creation is described in detail in our paper.

### Summary
| Words         | Documents   |   Words/Document |
|--------------:|------------:|-----------------:|
| 4,886,201,920 | 10,859,366  |              449 |

### Document Types
| Source                                | Words         | Documents   | Words/Document   |
|--------------------------------------:|--------------:|------------:|-----------------:|
| parliament                            | 1,260,502,586 | 9,225       | 136,639          |
| books                                 | 835,555,215   | 23,539      | 35,496           |
| newspapers_online_nb                  | 482,883,100   | 3,415,325   | 141              |
| maalfrid_regjeringen                  | 357,127,434   | 911,741     | 391              |
| maalfrid_ssb                          | 277,248,313   | 844,469     | 328              |
| maalfrid_uio                          | 180,254,856   | 764,578     | 235              |
| government_nb                         | 132,914,771   | 3,451       | 38,514           |
| wikipedia_download_nbo                | 109,831,216   | 518,951     | 211              |
| maalfrid_fylkesmannen                 | 101,893,489   | 458,784     | 222              |
| publicreports                         | 78,212,608    | 3,271       | 23,910           |
| maalfrid_nve                          | 66,092,070    | 299,384     | 220              |
| maalfrid_patentstyret                 | 64,430,833    | 212,117     | 303              |
| maalfrid_ntnu                         | 57,279,188    | 197,519     | 289              |
| newspapers_online_nn                  | 41,771,521    | 165,737     | 252              |
| lovdata_cd_odelsting_2005             | 36,005,494    | 1,932       | 18,636           |
| maalfrid_vegvesen                     | 33,131,414    | 164,695     | 201              |
| maalfrid_fhi                          | 32,476,731    | 142,987     | 227              |
| maalfrid_norad                        | 32,408,703    | 92,215      | 351              |
| maalfrid_skatteetaten                 | 32,317,533    | 81,905      | 394              |
| maalfrid_uib                          | 28,160,639    | 114,731     | 245              |
| wikipedia_download_nno                | 26,831,488    | 141,872     | 189              |
| maalfrid_forskningsradet              | 23,876,921    | 72,746      | 328              |
| maalfrid_nasjonalparkstyre            | 21,130,603    | 93,013      | 227              |
| government_nn                         | 18,106,305    | 1,053       | 17,194           |
| maalfrid_nmbu                         | 17,892,631    | 69,032      | 259              |
| maalfrid_oslomet                      | 17,565,000    | 46,619      | 376              |
| maalfrid_domstol                      | 16,546,095    | 50,584      | 327              |
| maalfrid_banenor                      | 16,296,418    | 69,765      | 233              |
| maalfrid_nav                          | 16,112,370    | 73,396      | 219              |
| maalfrid_landbruksdirektoratet        | 12,988,620    | 47,537      | 273              |
| maalfrid_helsedirektoratet            | 12,894,141    | 48,874      | 263              |
| maalfrid_nokut                        | 10,028,741    | 38,243      | 262              |
| maalfrid_hi                           | 9,956,191     | 38,683      | 257              |
| maalfrid_norges-bank                  | 9,825,026     | 36,807      | 266              |
| maalfrid_udir                         | 9,767,693     | 38,341      | 254              |
| maalfrid_vkm                          | 9,743,704     | 31,997      | 304              |
| maalfrid_nbim                         | 9,562,477     | 17,995      | 531              |
| maalfrid_miljodirektoratet            | 9,406,572     | 34,369      | 273              |
| maalfrid_distriktssenteret            | 9,301,190     | 38,197      | 243              |
| maalfrid_ngu                          | 9,160,389     | 34,305      | 267              |
| maalfrid_ptil                         | 9,112,264     | 33,902      | 268              |
| maalfrid_nord                         | 8,917,259     | 44,408      | 200              |
| maalfrid_fiskeridir                   | 8,221,774     | 33,078      | 248              |
| maalfrid_hivolda                      | 7,752,415     | 26,223      | 295              |
| maalfrid_difi                         | 7,720,133     | 35,475      | 217              |
| maalfrid_mattilsynet                  | 7,412,149     | 26,741      | 277              |
| maalfrid_havarikommisjonen            | 7,376,668     | 24,777      | 297              |
| maalfrid_kulturradet                  | 7,132,304     | 22,237      | 320              |
| maalfrid_ks                           | 6,841,571     | 27,134      | 252              |
| maalfrid_kystverket                   | 6,648,764     | 30,711      | 216              |
| maalfrid_udi                          | 6,362,856     | 18,908      | 336              |
| maalfrid_uia                          | 5,901,573     | 23,628      | 249              |
| maalfrid_hjelpemiddeldatabasen        | 5,843,648     | 33,848      | 172              |
| maalfrid_khrono                       | 5,805,461     | 19,756      | 293              |
| maalfrid_helsetilsynet                | 5,725,414     | 18,140      | 315              |
| maalfrid_moreforsk                    | 5,575,963     | 21,398      | 260              |
| maalfrid_jernbanedirektoratet         | 5,427,230     | 21,485      | 252              |
| maalfrid_veiviseren                   | 5,261,440     | 17,865      | 294              |
| lovdata_cd_somb_rundskriv_2005        | 5,242,676     | 3,201       | 1,637            |
| maalfrid_dsb                          | 5,149,282     | 17,635      | 291              |
| lovdata_cd_sentrale_forskrifter_2005  | 5,007,812     | 11,381      | 440              |
| maalfrid_husbanken                    | 4,668,798     | 14,910      | 313              |
| maalfrid_legemiddelverket             | 4,646,007     | 20,011      | 232              |
| maalfrid_vetinst                      | 4,619,818     | 14,350      | 321              |
| maalfrid_imdi                         | 4,588,421     | 15,135      | 303              |
| maalfrid_forsvarsbygg                 | 4,530,038     | 18,707      | 242              |
| maalfrid_sdir                         | 4,497,418     | 15,079      | 298              |
| maalfrid_konkurransetilsynet          | 4,470,281     | 12,486      | 358              |
| maalfrid_arkivverket                  | 4,466,215     | 16,396      | 272              |
| maalfrid_dsa                          | 4,456,010     | 15,772      | 282              |
| maalfrid_hiof                         | 4,429,234     | 22,915      | 193              |
| maalfrid_ehelse                       | 4,339,382     | 22,355      | 194              |
| maalfrid_inn                          | 4,289,871     | 26,033      | 164              |
| maalfrid_klagenemndssekretariatet     | 4,160,203     | 11,848      | 351              |
| maalfrid_sprakradet                   | 4,046,761     | 15,025      | 269              |
| maalfrid_nhh                          | 3,950,920     | 15,582      | 253              |
| maalfrid_dibk                         | 3,925,849     | 15,343      | 255              |
| maalfrid_kartverket                   | 3,690,053     | 18,511      | 199              |
| maalfrid_riksrevisjonen               | 3,661,977     | 10,871      | 336              |
| maalfrid_toll                         | 3,478,604     | 13,678      | 254              |
| maalfrid_nibio                        | 3,427,231     | 16,942      | 202              |
| maalfrid_met                          | 3,421,328     | 18,123      | 188              |
| maalfrid_bufdir                       | 3,329,773     | 11,382      | 292              |
| maalfrid_artsdatabanken               | 3,174,117     | 8,955       | 354              |
| maalfrid_politiet                     | 3,138,300     | 10,389      | 302              |
| maalfrid_nkom                         | 3,099,581     | 9,892       | 313              |
| maalfrid_vestlandfylke                | 3,035,002     | 11,974      | 253              |
| maalfrid_uis                          | 2,893,474     | 9,730       | 297              |
| maalfrid_sykkelbynettverket           | 2,800,659     | 11,722      | 238              |
| maalfrid_nlr                          | 2,621,712     | 15,694      | 167              |
| maalfrid_seniorporten                 | 2,590,273     | 8,044       | 322              |
| maalfrid_npd                          | 2,571,771     | 10,669      | 241              |
| maalfrid_custompublish                | 2,419,117     | 9,128       | 265              |
| maalfrid_aldringoghelse               | 2,397,641     | 6,716       | 357              |
| maalfrid_bioteknologiradet            | 2,378,816     | 5,962       | 398              |
| maalfrid_arbeidstilsynet              | 2,368,908     | 6,833       | 346              |
| maalfrid_nyemetoder                   | 2,347,435     | 10,643      | 220              |
| maalfrid_riksantikvaren               | 2,234,416     | 8,679       | 257              |
| maalfrid_sjt                          | 2,220,680     | 11,082      | 200              |
| lovdata_cd_lokaleforskrifter_2005     | 2,165,875     | 22,106      | 97               |
| maalfrid_hvl                          | 2,122,182     | 9,291       | 228              |
| maalfrid_luftfartstilsynet            | 2,080,150     | 9,780       | 212              |
| maalfrid_dfo                          | 2,065,318     | 9,087       | 227              |
| maalfrid_ldo                          | 2,036,871     | 7,250       | 280              |
| maalfrid_kompetansenorge              | 1,932,064     | 10,175      | 189              |
| maalfrid_forbrukerradet               | 1,928,045     | 7,246       | 266              |
| maalfrid_himolde                      | 1,903,669     | 9,889       | 192              |
| maalfrid_usn                          | 1,772,050     | 7,330       | 241              |
| lovdata_cd_norgeslover_2005           | 1,768,056     | 1,383       | 1,278            |
| maalfrid_naku                         | 1,724,479     | 5,154       | 334              |
| maalfrid_medietilsynet                | 1,595,414     | 6,554       | 243              |
| maalfrid_matematikksenteret           | 1,554,763     | 7,230       | 215              |
| maalfrid_diku                         | 1,533,863     | 6,185       | 247              |
| maalfrid_forskningsetikk              | 1,528,351     | 5,488       | 278              |
| maalfrid_godeidrettsanlegg            | 1,498,095     | 6,081       | 246              |
| maalfrid_dirmin                       | 1,451,325     | 5,246       | 276              |
| maalfrid_diskrimineringsnemnda        | 1,446,778     | 4,130       | 350              |
| maalfrid_naturfag                     | 1,426,975     | 5,911       | 241              |
| maalfrid_arbeidsretten                | 1,422,959     | 4,693       | 303              |
| maalfrid_fellesstudentsystem          | 1,348,423     | 10,234      | 131              |
| lovdata_cd_rtv_rundskriv_2005         | 1,341,173     | 9,528       | 140              |
| maalfrid_nupi                         | 1,277,307     | 5,437       | 234              |
| maalfrid_kriminalitetsforebygging     | 1,191,809     | 4,634       | 257              |
| maalfrid_anskaffelser                 | 1,178,401     | 5,426       | 217              |
| maalfrid_folketrygdfondet             | 1,172,842     | 4,201       | 279              |
| maalfrid_miljopakken                  | 1,162,877     | 5,466       | 212              |
| lovdata_cd_skatt_rundskriv_2005       | 1,113,374     | 396         | 2,811            |
| maalfrid_nih                          | 1,107,364     | 5,246       | 211              |
| maalfrid_statsbygg                    | 1,093,882     | 4,375       | 250              |
| maalfrid_nb                           | 1,047,952     | 4,122       | 254              |
| maalfrid_npolar                       | 1,045,552     | 2,642       | 395              |
| maalfrid_unit                         | 1,038,636     | 6,274       | 165              |
| maalfrid_valgdirektoratet             | 996,239       | 9,035       | 110              |
| maalfrid_barneombudet                 | 968,955       | 2,766       | 350              |
| maalfrid_datatilsynet                 | 960,327       | 2,924       | 328              |
| maalfrid_lottstift                    | 952,738       | 3,550       | 268              |
| maalfrid_aho                          | 948,960       | 4,489       | 211              |
| maalfrid_sykehuspartner               | 926,472       | 4,525       | 204              |
| maalfrid_naturfagsenteret             | 896,048       | 3,844       | 233              |
| maalfrid_khio                         | 844,370       | 3,346       | 252              |
| maalfrid_spesialenheten               | 821,619       | 2,127       | 386              |
| maalfrid_xn--miljlftet-o8ab           | 796,916       | 3,360       | 237              |
| maalfrid_samordnaopptak               | 779,679       | 2,333       | 334              |
| maalfrid_helsenorge                   | 774,308       | 3,017       | 256              |
| maalfrid_skrivesenteret               | 769,883       | 4,128       | 186              |
| maalfrid_mareano                      | 755,280       | 3,679       | 205              |
| maalfrid_fiskeridirektoratet          | 745,427       | 2,414       | 308              |
| maalfrid_sykehusinnkjop               | 731,256       | 4,289       | 170              |
| maalfrid_matportalen                  | 623,335       | 2,348       | 265              |
| maalfrid_spk                          | 602,237       | 2,115       | 284              |
| maalfrid_pasientsikkerhetsprogrammet  | 593,147       | 4,670       | 127              |
| maalfrid_justervesenet                | 584,862       | 1,876       | 311              |
| maalfrid_nhn                          | 580,465       | 3,563       | 162              |
| maalfrid_sshf                         | 566,623       | 1,883       | 300              |
| maalfrid_bibliotekutvikling           | 556,597       | 3,190       | 174              |
| maalfrid_nysgjerrigper                | 554,331       | 2,983       | 185              |
| maalfrid_nodnett                      | 531,154       | 2,650       | 200              |
| maalfrid_giek                         | 511,920       | 1,785       | 286              |
| maalfrid_une                          | 505,306       | 1,227       | 411              |
| maalfrid_samas                        | 497,271       | 2,533       | 196              |
| maalfrid_kriminalomsorgen             | 492,290       | 1,937       | 254              |
| maalfrid_kjonnsforskning              | 481,527       | 1,421       | 338              |
| lovdata_cd_rundskriv_lovavdeling_2005 | 468,349       | 408         | 1,147            |
| maalfrid_kunstkultursenteret          | 464,656       | 1,419       | 327              |
| maalfrid_nynorsksenteret              | 452,817       | 2,074       | 218              |
| maalfrid_stami                        | 442,196       | 1,154       | 383              |
| maalfrid_ceres                        | 439,453       | 1,916       | 229              |
| maalfrid_nsm                          | 436,831       | 1,519       | 287              |
| maalfrid_nfi                          | 418,595       | 1,510       | 277              |
| maalfrid_gjenopptakelse               | 414,616       | 1,446       | 286              |
| maalfrid_nidsenter                    | 406,139       | 1,620       | 250              |
| maalfrid_forbrukertilsynet            | 385,587       | 1,216       | 317              |
| maalfrid_nasjonalmuseet               | 383,916       | 1,070       | 358              |
| maalfrid_natursekken                  | 375,039       | 3,535       | 106              |
| maalfrid_fordelingsutvalget           | 350,682       | 1,372       | 255              |
| maalfrid_digdir                       | 349,083       | 2,095       | 166              |
| maalfrid_forsvaret                    | 329,307       | 1,209       | 272              |
| maalfrid_beccle                       | 326,693       | 1,503       | 217              |
| maalfrid_romsenter                    | 325,796       | 1,120       | 290              |
| maalfrid_geonorge                     | 296,865       | 1,606       | 184              |
| maalfrid_universell                   | 262,248       | 2,152       | 121              |
| maalfrid_ovf                          | 260,108       | 919         | 283              |
| maalfrid_forbrukereuropa              | 256,472       | 1,008       | 254              |
| maalfrid_politihogskolen              | 255,500       | 1,216       | 210              |
| maalfrid_vinmonopolet                 | 242,793       | 663         | 366              |
| maalfrid_energimerking                | 234,655       | 1,027       | 228              |
| maalfrid_ombudsmann                   | 226,797       | 416         | 545              |
| maalfrid_vea-fs                       | 223,018       | 1,251       | 178              |
| maalfrid_traumebevisst                | 221,606       | 2,409       | 91               |
| maalfrid_npe                          | 203,452       | 992         | 205              |
| maalfrid_pkh                          | 201,011       | 791         | 254              |
| maalfrid_helfo                        | 192,164       | 975         | 197              |
| maalfrid_opplaringslovutvalget        | 191,387       | 542         | 353              |
| maalfrid_regionaleforskningsfond      | 185,201       | 979         | 189              |
| maalfrid_nafkam                       | 174,285       | 563         | 309              |
| maalfrid_jernbanemagasinet            | 173,851       | 411         | 422              |
| maalfrid_polarhistorie                | 170,535       | 383         | 445              |
| maalfrid_aasentunet                   | 159,465       | 522         | 305              |
| maalfrid_riksteatret                  | 156,872       | 782         | 200              |
| maalfrid_realfagsloyper               | 155,802       | 740         | 210              |
| maalfrid_koro                         | 153,577       | 567         | 270              |
| maalfrid_squarespace                  | 144,234       | 497         | 290              |
| maalfrid_politietssikkerhetstjeneste  | 141,433       | 462         | 306              |
| maalfrid_unknown                      | 139,391       | 696         | 200              |
| maalfrid_whocc                        | 119,423       | 647         | 184              |
| maalfrid_konfliktraadet               | 115,529       | 361         | 320              |
| maalfrid_okokrim                      | 114,946       | 367         | 313              |
| maalfrid_riksmekleren                 | 111,169       | 560         | 198              |
| maalfrid_sismo                        | 110,707       | 310         | 357              |
| maalfrid_brreg                        | 109,013       | 553         | 197              |
| maalfrid_akkreditert                  | 99,469        | 500         | 198              |
| maalfrid_sivilforsvaret               | 98,232        | 512         | 191              |
| maalfrid_radetfordyreetikk            | 94,594        | 427         | 221              |
| maalfrid_digidel                      | 92,808        | 598         | 155              |
| maalfrid_lanekassen                   | 91,949        | 295         | 311              |
| maalfrid_uit                          | 90,660        | 598         | 151              |
| maalfrid_nyinorge                     | 89,346        | 201         | 444              |
| maalfrid_lokforerskolen               | 88,289        | 465         | 189              |
| maalfrid_generaladvokaten             | 87,571        | 284         | 308              |
| maalfrid_varsom                       | 84,645        | 554         | 152              |
| maalfrid_kulturminnefondet            | 79,735        | 419         | 190              |
| maalfrid_ffi                          | 79,606        | 214         | 371              |
| maalfrid_unesco                       | 76,476        | 374         | 204              |
| maalfrid_yrkesfisker                  | 72,721        | 491         | 148              |
| maalfrid_dekom                        | 72,501        | 1,298       | 55               |
| maalfrid_omsorgsforskning             | 71,981        | 323         | 222              |
| maalfrid_lektor2                      | 68,003        | 543         | 125              |
| maalfrid_openaccess                   | 63,876        | 193         | 330              |
| maalfrid_ssn                          | 61,318        | 293         | 209              |
| maalfrid_lokalhistorie                | 60,633        | 245         | 247              |
| maalfrid_laudim                       | 58,222        | 392         | 148              |
| maalfrid_nlb                          | 57,131        | 197         | 290              |
| maalfrid_riksadvokaten                | 55,995        | 150         | 373              |
| maalfrid_denkulturelleskolesekken     | 45,031        | 240         | 187              |
| maalfrid_sivilrett                    | 43,904        | 141         | 311              |
| maalfrid_htu                          | 41,234        | 161         | 256              |
| maalfrid_yr                           | 40,051        | 554         | 72               |
| maalfrid_informasjonskompetanse       | 39,227        | 320         | 122              |
| maalfrid_finansportalen               | 38,872        | 180         | 215              |
| maalfrid_kulturped                    | 37,389        | 98          | 381              |
| maalfrid_dep                          | 36,476        | 121         | 301              |
| maalfrid_feide                        | 36,352        | 265         | 137              |
| maalfrid_kulturoghelse                | 34,331        | 185         | 185              |
| maalfrid_fug                          | 33,825        | 119         | 284              |
| maalfrid_helseklage                   | 33,081        | 124         | 266              |
| maalfrid_nbsk                         | 30,683        | 210         | 146              |
| maalfrid_matogindustri                | 30,599        | 200         | 152              |
| maalfrid_sinn                         | 27,629        | 152         | 181              |
| maalfrid_vergemal                     | 23,367        | 78          | 299              |
| maalfrid_konkursradet                 | 23,326        | 76          | 306              |
| maalfrid_transport21                  | 22,917        | 82          | 279              |
| maalfrid_norec                        | 21,585        | 74          | 291              |
| maalfrid_pts                          | 21,215        | 80          | 265              |
| maalfrid_nasjonaleturistveger         | 19,757        | 109         | 181              |
| maalfrid_hjelpelinjen                 | 19,099        | 85          | 224              |
| maalfrid_iearth                       | 18,844        | 148         | 127              |
| maalfrid_russamtalen                  | 18,703        | 67          | 279              |
| maalfrid_xn--kvinneligomskjring-1ub   | 18,506        | 78          | 237              |
| maalfrid_nynorskbok                   | 17,294        | 95          | 182              |
| maalfrid_memu                         | 16,875        | 94          | 179              |
| maalfrid_regjeringsadvokaten          | 16,862        | 53          | 318              |
| maalfrid_xn--forskerfr-t8a            | 16,026        | 171         | 93               |
| maalfrid_xn--tilbakefring-2jb         | 15,787        | 48          | 328              |
| maalfrid_skattefunn                   | 15,501        | 53          | 292              |
| maalfrid_ringerikefengsel             | 15,018        | 26          | 577              |
| maalfrid_samfunnskunnskap             | 14,898        | 58          | 256              |
| maalfrid_skeivtarkiv                  | 14,859        | 67          | 221              |
| maalfrid_fordelingsutvalet            | 14,658        | 34          | 431              |
| maalfrid_shiprep                      | 14,451        | 142         | 101              |
| maalfrid_sevuppt                      | 13,985        | 54          | 258              |
| maalfrid_haldenfengsel                | 13,218        | 37          | 357              |
| maalfrid_forbrukerklageutvalget       | 12,953        | 49          | 264              |
| maalfrid_mhfa                         | 11,966        | 132         | 90               |
| maalfrid_ah                           | 11,787        | 36          | 327              |
| maalfrid_nettvett                     | 11,353        | 44          | 258              |
| maalfrid_uh-it                        | 11,020        | 274         | 40               |
| maalfrid_fishgen                      | 10,151        | 28          | 362              |
| maalfrid_designavgang                 | 10,083        | 73          | 138              |
| maalfrid_global                       | 9,363         | 43          | 217              |
| maalfrid_valg                         | 8,778         | 47          | 186              |
| maalfrid_havmiljo                     | 8,734         | 69          | 126              |
| maalfrid_miljoklagenemnda             | 7,797         | 35          | 222              |
| maalfrid_altinn                       | 7,636         | 47          | 162              |
| maalfrid_spinn-inn                    | 7,381         | 46          | 160              |
| maalfrid_kantinekurset                | 7,302         | 53          | 137              |
| maalfrid_bastoyfengsel                | 6,990         | 54          | 129              |
| maalfrid_voldsoffererstatning         | 6,079         | 27          | 225              |
| maalfrid_norskpetroleum               | 5,953         | 117         | 50               |
| maalfrid_musikkbasertmiljobehandling  | 4,895         | 36          | 135              |
| maalfrid_prosjektveiviseren           | 4,860         | 13          | 373              |
| maalfrid_fmfiavo@fylkesmannen         | 4,740         | 69          | 68               |
| maalfrid_aldersvennlig                | 4,643         | 31          | 149              |
| maalfrid_barentswatch                 | 4,575         | 31          | 147              |
| maalfrid_kk-utvalget                  | 4,474         | 18          | 248              |
| maalfrid_agropub                      | 4,434         | 17          | 260              |
| maalfrid_utdanningiverden             | 3,845         | 13          | 295              |
| maalfrid_overgangsbolig               | 3,769         | 35          | 107              |
| maalfrid_forsvaretsmuseer             | 3,744         | 34          | 110              |
| maalfrid_okopark                      | 3,282         | 12          | 273              |
| maalfrid_sikkerhverdag                | 2,786         | 19          | 146              |
| maalfrid_pst                          | 2,643         | 13          | 203              |
| maalfrid_arkitektur                   | 2,321         | 14          | 165              |
| maalfrid_velgekte                     | 2,287         | 10          | 228              |
| maalfrid_addlab                       | 2,107         | 11          | 191              |
| maalfrid_romerikefengsel              | 2,017         | 17          | 118              |
| maalfrid_utdanning                    | 2,009         | 12          | 167              |
| maalfrid_grunderskolen                | 1,994         | 7           | 284              |
| maalfrid_umb                          | 1,958         | 9           | 217              |
| maalfrid_oslofengsel                  | 1,756         | 8           | 219              |
| maalfrid_alleteller                   | 1,511         | 7           | 215              |
| maalfrid_lykillinn                    | 1,349         | 4           | 337              |
| maalfrid_kulturfag                    | 1,215         | 6           | 202              |
| maalfrid_hjorteviltregisteret         | 1,020         | 3           | 340              |
| maalfrid_unimus                       | 940           | 4           | 235              |
| maalfrid_anleggsregisteret            | 928           | 5           | 185              |
| maalfrid_webhuset                     | 883           | 3           | 294              |
| maalfrid_mangfoldsprisen              | 597           | 3           | 199              |
| maalfrid_algae2future                 | 456           | 8           | 57               |
| maalfrid_mammapresenterer             | 447           | 2           | 223              |
| maalfrid_karriereveiledning           | 382           | 26          | 14               |
| maalfrid_nodsms                       | 351           | 4           | 87               |
| maalfrid_kildekompasset               | 302           | 1           | 302              |
| maalfrid_praksisfou                   | 297           | 1           | 297              |
| maalfrid_retttilaalese                | 246           | 3           | 82               |
| maalfrid_indreostfoldfengsel          | 215           | 3           | 71               |
| maalfrid_xn--kroppsvingsforskning-gcc | 205           | 2           | 102              |
| maalfrid_pahoyden                     | 154           | 1           | 154              |
| maalfrid_norren                       | 42            | 1           | 42               |

### Languages
| Language   | Words         | Documents   | Words/Document   |
|-----------:|--------------:|------------:|-----------------:|
| no         | 3,208,084,695 | 8,290,110   | 386              |
| da         | 917,080,415   | 322,045     | 2,847            |
| en         | 462,136,101   | 1,422,633   | 324              |
| nn         | 174,514,916   | 467,956     | 372              |
| fr         | 48,750,032    | 104,698     | 465              |
| de         | 26,433,213    | 61,760      | 427              |
| sv         | 15,535,094    | 55,596      | 279              |
| es         | 8,379,358     | 31,395      | 266              |
| fi         | 3,857,523     | 10,268      | 375              |
| pt         | 2,476,848     | 14,558      | 170              |
| oc         | 2,104,415     | 4,845       | 434              |
| nl         | 1,872,692     | 7,153       | 261              |
| zh         | 1,452,798     | 7,540       | 192              |
| uk         | 1,420,173     | 4,290       | 331              |
| ca         | 1,361,797     | 3,577       | 380              |
| la         | 1,280,142     | 500         | 2,560            |
| it         | 1,255,675     | 6,812       | 184              |
| ru         | 1,201,770     | 5,717       | 210              |
| et         | 1,030,612     | 3,892       | 264              |
| cs         | 909,670       | 4,254       | 213              |
| eu         | 827,380       | 3,091       | 267              |
| pl         | 745,342       | 5,022       | 148              |
| fa         | 487,145       | 1,984       | 245              |
| ja         | 340,847       | 3,481       | 97               |
| is         | 303,953       | 979         | 310              |
| id         | 213,904       | 1,228       | 174              |
| ar         | 207,081       | 1,145       | 180              |
| hu         | 190,336       | 1,290       | 147              |
| vi         | 134,034       | 616         | 217              |
| so         | 128,476       | 589         | 218              |
| el         | 116,643       | 604         | 193              |
| hr         | 109,342       | 493         | 221              |
| lv         | 106,145       | 63          | 1,684            |
| sl         | 91,364        | 648         | 140              |
| tr         | 88,945        | 1,006       | 88               |
| eo         | 80,138        | 473         | 169              |
| ro         | 78,492        | 440         | 178              |
| lt         | 65,104        | 545         | 119              |
| sr         | 64,233        | 764         | 84               |
| gl         | 62,865        | 570         | 110              |
| ko         | 54,321        | 893         | 60               |
| war        | 53,809        | 228         | 236              |
| th         | 52,614        | 350         | 150              |
| am         | 45,893        | 321         | 142              |
| ceb        | 35,257        | 264         | 133              |
| ml         | 34,523        | 148         | 233              |
| sq         | 31,866        | 152         | 209              |
| tl         | 30,909        | 161         | 191              |
| kk         | 26,605        | 68          | 391              |
| mn         | 21,540        | 22          | 979              |
| sw         | 18,626        | 64          | 291              |
| pnb        | 18,203        | 80          | 227              |
| sk         | 17,548        | 196         | 89               |
| gu         | 16,973        | 13          | 1,305            |
| bg         | 16,746        | 96          | 174              |
| sh         | 15,627        | 127         | 123              |
| ur         | 15,353        | 138         | 111              |
| mk         | 12,193        | 62          | 196              |
| ckb        | 9,350         | 44          | 212              |
| ku         | 8,316         | 48          | 173              |
| ast        | 7,828         | 58          | 134              |
| az         | 7,585         | 47          | 161              |
| uz         | 6,873         | 34          | 202              |
| ta         | 4,177         | 59          | 70               |
| fy         | 3,567         | 26          | 137              |
| ms         | 3,535         | 100         | 35               |
| hy         | 3,409         | 31          | 109              |
| pa         | 3,283         | 16          | 205              |
| hi         | 2,810         | 40          | 70               |
| bo         | 2,551         | 1           | 2,551            |
| ht         | 2,534         | 11          | 230              |
| be         | 2,418         | 42          | 57               |
| min        | 2,155         | 7           | 307              |
| cy         | 1,984         | 40          | 49               |
| jv         | 1,887         | 30          | 62               |
| su         | 1,840         | 23          | 80               |
| als        | 1,826         | 40          | 45               |
| bn         | 1,791         | 20          | 89               |
| ps         | 1,740         | 14          | 124              |
| af         | 1,703         | 20          | 85               |
| bs         | 1,516         | 23          | 65               |
| qu         | 1,484         | 13          | 114              |
| nds        | 1,370         | 78          | 17               |
| my         | 1,107         | 15          | 73               |
| ga         | 967           | 26          | 37               |
| mt         | 937           | 12          | 78               |
| si         | 858           | 21          | 40               |
| te         | 853           | 17          | 50               |
| ilo        | 733           | 15          | 48               |
| io         | 693           | 11          | 63               |
| km         | 690           | 12          | 57               |
| tt         | 675           | 20          | 33               |
| jbo        | 621           | 27          | 23               |
| gn         | 595           | 7           | 85               |
| as         | 584           | 2           | 292              |
| ug         | 581           | 6           | 96               |
| kv         | 562           | 3           | 187              |
| kn         | 531           | 19          | 27               |
| br         | 522           | 19          | 27               |
| pam        | 476           | 1           | 476              |
| he         | 396           | 14          | 28               |
| kw         | 327           | 5           | 65               |
| ka         | 311           | 16          | 19               |
| vep        | 302           | 13          | 23               |
| wa         | 266           | 38          | 7                |
| yo         | 261           | 5           | 52               |
| ky         | 232           | 11          | 21               |
| azb        | 216           | 1           | 216              |
| ba         | 203           | 5           | 40               |
| gom        | 164           | 9           | 18               |
| ia         | 131           | 12          | 10               |
| tg         | 129           | 3           | 43               |
| mr         | 122           | 6           | 20               |
| lmo        | 87            | 23          | 3                |
| lb         | 77            | 17          | 4                |
| pms        | 76            | 10          | 7                |
| vec        | 67            | 3           | 22               |
| rue        | 67            | 2           | 33               |
| ne         | 51            | 5           | 10               |
| hsb        | 51            | 2           | 25               |
| cbk        | 46            | 2           | 23               |
| or         | 44            | 2           | 22               |
| ie         | 38            | 5           | 7                |
| tk         | 36            | 4           | 9                |
| eml        | 31            | 4           | 7                |
| arz        | 31            | 1           | 31               |
| sco        | 30            | 1           | 30               |
| bar        | 30            | 3           | 10               |
| gd         | 29            | 2           | 14               |
| li         | 22            | 3           | 7                |
| mg         | 22            | 4           | 5                |
| lrc        | 20            | 1           | 20               |
| diq        | 20            | 2           | 10               |
| dsb        | 19            | 1           | 19               |
| yue        | 19            | 1           | 19               |
| os         | 15            | 2           | 7                |
| wuu        | 14            | 1           | 14               |
| sd         | 14            | 1           | 14               |
| nah        | 14            | 2           | 7                |
| cv         | 12            | 1           | 12               |
| scn        | 9             | 2           | 4                |
| bcl        | 8             | 1           | 8                |
| bh         | 8             | 1           | 8                |
| new        | 4             | 1           | 4                |
| ce         | 4             | 1           | 4                |
| mzn        | 3             | 1           | 3                |
| frr        | 3             | 1           | 3                |
| gv         | 3             | 1           | 3                |
| vo         | 3             | 2           | 1                |
| lo         | 2             | 1           | 2                |

### Publish Periode
|   Decade | Words         | Documents   | Words/Document   |
|---------:|--------------:|------------:|-----------------:|
|     2020 | 4,052,373,794 | 10,835,886  | 1,425            |
|     2010 | 17,009,855    | 940         | 141,801          |
|     2000 | 56,172,494    | 2,884       | 200,149          |
|     1990 | 114,019,082   | 5,874       | 197,169          |
|     1980 | 39,419,883    | 1,480       | 266,616          |
|     1970 | 21,512,880    | 841         | 251,649          |
|     1960 | 17,545,214    | 469         | 373,059          |
|     1950 | 17,141,714    | 341         | 480,561          |
|     1940 | 28,883,477    | 532         | 513,832          |
|     1930 | 35,093,392    | 693         | 504,374          |
|     1920 | 51,125,258    | 1,067       | 483,297          |
|     1910 | 61,224,579    | 1,207       | 498,450          |
|     1900 | 59,281,717    | 1,124       | 523,247          |
|     1890 | 85,597,278    | 1,746       | 486,711          |
|     1880 | 58,217,754    | 1,062       | 551,360          |
|     1870 | 25,602,577    | 614         | 404,544          |
|     1860 | 39,006,777    | 692         | 547,879          |
|     1850 | 52,875,326    | 838         | 628,249          |
|     1840 | 30,500,062    | 516         | 588,425          |
|     1830 | 18,072,551    | 363         | 487,067          |
|     1820 | 4,554,472     | 141         | 338,978          |
|     1810 | 971,784       | 56          | 127,989          |

## Considerations for Using the Data
This corpus contains data under copyright and is not allowed to be used outide the National Library of Norway. The dataset should not be distributed.

### Discussion of Biases
Please refer to our paper.

### Dataset Curators
[Freddy Wetjen](mailto:Freddy.wetjen@nb.no) and [Per Egil Kummervold](mailto:Per.Kummervold@nb.no)


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
in several token and sequence classification tasks for both Norwegian Bokm{aa}l and Norwegian Nynorsk. Our model also improves the mBERT performance for other
languages present in the corpus such as English, Swedish, and Danish. For languages not included in the corpus, the weights degrade moderately while keeping strong multilingual properties. Therefore,
we show that building high-quality models within a memory institution using somewhat noisy optical character recognition (OCR) content is feasible, and we hope to pave the way for other memory institutions to follow.",
}
```
