---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- it
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- summarization
- text-generation
task_ids: []
pretty_name: change-it
tags:
- conditional-text-generation
- style-transfer
---

# Dataset Card for CHANGE-IT

## Table of Contents

- [Dataset Card for CHANGE-IT](#dataset-card-for-change-it)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
      - [Style Transfer](#style-transfer)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
    - [Dataset Creation](#dataset-creation)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** [https://live.european-language-grid.eu/catalogue/corpus/7373](https://live.european-language-grid.eu/catalogue/corpus/7373)
- **Repository:** [Github](https://github.com/michelecafagna26/CHANGE-IT)
- **Paper:** [CEUR-ws.org](http://ceur-ws.org/Vol-2765/paper169.pdf)
- **Video** [Vimeo](https://vimeo.com/484098874)
- **Point of Contact:** [Lorenzo De Mattei](lorenzo.demattei@gmail.com)
- **Size of downloaded dataset files:** 168.7 MB
- **Size of the generated dataset:** 411 MB
- **Total amount of disk used:** 579.7 MB

### Dataset Summary

The CHANGE-IT dataset contains approximately 152,000 article-headline pairs, collected from two Italian newspapers situated at opposite ends of the political spectrum, namely la Repubblica (left) and Il Giornale (right), with the two newspapers equally represented. The dataset has been used in the context 
of the [CHANGE-IT task](https://sites.google.com/view/change-it) during the [Evalita 2020 evaluation campaign](http://www.evalita.it/2020). CHANGE-IT is a generation task for Italian – more specifically, a style transfer task for headlines of Italian newspapers. Given a (collection of) headlines from one newspaper, namely Il Giornale (G) or La Repubblica (R), it challenges automatic systems to change all G-headlines to headlines in style R, and all R-headlines to headlines in style G. Although the task only concerns headline change, the dataset comprehends both the headlines as well as their respective full articles.

**Disclaimer**: *The CHANGE-IT dataset is hosted by the [European Language Grid](https://live.european-language-grid.eu/) and licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/). To use the dataset using* 🤗 *Datasets, download and unzip the folder from its [ELG page](https://live.european-language-grid.eu/catalogue/corpus/7373) and pass it to the* `load_dataset` *method as:* `datasets.load_dataset('gsarti/change_it', data_dir='path/to/unzipped/folder')`

### Supported Tasks and Leaderboards

#### Style Transfer

The following table is taken from Table 4 of the original paper, where a *pointer-network* architecture is used as a baseline to perform style transfer in two settings. In the **rep2gio** variant the system is trained to summarize Repubblica headlines from full texts (vice versa for **gio2rep**), and the style transfer is performed by summarizing full texts of the other newspaper in the source newspaper's headline style. **avg** is the average of the two settings.

|         |  HH|  AH|Main|Compliancy|
|--------:|---:|---:|---:|---------:|
|`rep2gio`|.649|.876|.799|      .449|
|`gio2rep`|.639|.871|.435|      .240|
|    `avg`|.644|.874|.616|      .345|

Here **Main**, **HH** and **AH** are all BERT-base models trained to evaluate the quality of style transfer as follows:

- **Main**: the model is trained to classify a generated headline either as `ilgiornale` or `repubblica`, achieving ~80% F1 score on gold data. Tests whether the transfer has been successful.
- **Headline-Headline (HH)**: the model is trained to check the compatibility between original and generated headlines. Tests whether the generation is coherent with the reference.
- **Article-Headline (AH)**: the model is trained to check the compatibility between original fulltext article and generated headlines. Tests whether the generation is coherent with the source article.

The final metric, **Overall compliancy**, is a binary metric that is positive if the other three metrics match (**Main** decision is reversed, **HH** and **AH** predict match), and negative otherwise. Refer to Section 3 of the original paper for more details. 

### Languages

The language data in CHANGE-IT is in Italian (BCP-47 `it`)

## Dataset Structure

### Data Instances

A sample from the `test` split of the `ilgiornale` config is provided below. The other configuration, `ilgiornale`, has the same structure.

```json
{
  "id": 0,
  "headline": "Ucraina, coalizione della Timoshenko denuncia irruzione nella sede",
  "full_text": "Rimane alta la tensione in Ucraina , dove da giorni i manifestanti scendono in piazza per protestare contro la decisione del presidente Viktor Yanukovich, che ha deciso di congelare l'accordo di associazione con l'Unione Europea. Il momento è molto delicato. L'opposizione teme una repressione violenza della protesta, con le forze speciali che hanno costretto i manifestanti a Kiev ad allontanarsi dalla sede del governo, per ripiegare su piazza Indipendenza. Il leader d'opposizione Vitaly Klitschko ha invitato il presidente a non utilizzare la forza, se non vuole avere il sangue dei manifestanti sulle sue mani. Nel frattempo il presidente Yanukovich ha aperto alla possibilità di un dialogo, annunciando per domani un incontro con i suoi due predecessori, Leonid Kuchma e Viktor Yushchenko. Ieri un milioni di persone sono scese in piazza, scaduti i due giorni di ultimatum dati al governo per indire nuove elezioni, I manifestanti hanno rovesciato la grande statua di Lenin posta sul boulevard Shevchenko. Piazza Indipendenza (Maidan Nezalezhnosti) resta il punto più caldo della capitale. Qui sono state erette barricate davanti agli ingressi della metropolitana, nel tentativo di preparsi a un'azione della polizia, che al momento non ha però preso iniziative contro i dimostranti. In serata Batkivshcyna, la coalizione dell'ex premier Yulia Timoshenko , ha denunciato l'irruzione di almeno venti agenti della polizia antisommossa nel proprio quartier generale. Il portavoce della polizia, Olga Bilyk, ha smentito: \"Né la polizia di Kiev, né la Berkut - ha dichiarato - hanno condotto operazioni nella sede\".",
  "alignment": "A2"
}
```

The text is provided as-is, without further preprocessing or tokenization.

### Data Fields

- `headline`: The original headline for the newspaper.
- `full_text`: The article full text associated to the respective headline.
- `alignment`: The alignment value used for the style transfer experiments. Values:
  - `A1`: Top 5K pairs, highly aligned.
  - `A2`: Test set, highly aligned.
  - `A3`: 10K to 20K pairs, fairly aligned.
  - `R`: Bottom ~50K pairs, weakly/not aligned.

### Data Splits

|    config|                                 train|        test|
|---------:|-------------------------------------:|-----------:|
|`ilgiornale`|5'000 (A1) + 10'000 (A3) + 48'701 (R) | 5'000 (A2) |
|`repubblica`|5'000 (A1) + 10'000 (A3) + 48'701 (R) | 5'000 (A2) |

### Dataset Creation

Please refer to the original article [CHANGE-IT @ EVALITA 2020: Change Headlines, Adapt News, GEnerate](http://ceur-ws.org/Vol-2765/paper169.pdf) for additional information on dataset creation.

## Additional Information

### Dataset Curators

The organizers of the CHANGE-IT shared tasks are the curators of the original dataset. For problems or updates on the 🤗 Datasets version, please contact [gabriele.sarti996@gmail.com](mailto:gabriele.sarti996@gmail.com).

### Licensing Information

Licensed with Creative Commons Attribution Non Commercial Share Alike 4.0. License available [here](https://creativecommons.org/licenses/by-nc-sa/4.0/).

### Citation Information

Please cite the authors if you use these corpora in your work:

```
@inproceedings{demattei-etal-2020-changeit,
    author = {De Mattei, Lorenzo and Cafagna, Michele and Dell'Orletta, Felice and Nissim, Malvina and Gatt, Albert},
    title = {{CHANGE-IT @ EVALITA 2020}: Change Headlines, Adapt News, GEnerate},
    booktitle = {Proceedings of Seventh Evaluation Campaign of Natural Language Processing and Speech Tools for Italian. Final Workshop (EVALITA 2020)},
    editor = {Basile, Valerio and Croce, Danilo and Di Maro, Maria, and Passaro, Lucia C.},
    publisher = {CEUR.org},
    year = {2020},
    address = {Online}
}
