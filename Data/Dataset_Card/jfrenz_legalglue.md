---
language:
- en
- da
- de
- nl
- sv
- bg
- cs
- hr
- pl
- sk
- sl
- es
- fr
- it
- pt
- ro
- et
- fi
- hu
- lt
- lv
- el
- mt
multilinguality:
- multilingual
source_datasets:
- extended
task_categories:
- text-classification
- token-classification
task_ids:
- named-entity-recognition
- multi-label-classification
- topic-classification
pretty_name: LegalGLUE
tags:
- german-ler
- lener-br
---

# Dataset Card for "LegalGLUE"

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Repository:** https://git.rwth-aachen.de/johanna.frenz/legalglue

### Dataset Summary

The "Legal General Language Understanding Evaluation" (LegalGLUE) dataset was created as part of a bachelor thesis.
It consists of four already existing datasets covering three task types and a total of 23 different languages.

### Supported Tasks

<table>
<tr><td>Dataset</td><td>Source</td><td>Task Type</td><td>Languages</td><tr>


<tr><td>German_LER</td><td> <a href="https://arxiv.org/abs/2003.13016">Leitner et al.</a></td><td>Named Entity Recognition</td><td>German</td></tr>
<tr><td>LeNER_Br</td><td> <a href="https://github.com/peluz/lener-br"> de Araujo et al., 2018</a></td><td>Named Entity Recognition</td><td> Portuguese </td></tr>
<tr><td>SwissJudgmentPrediction</td><td> <a href="https://arxiv.org/abs/2110.00806">Niklaus et al.</a> </td><td>Binary Text Classification</td><td>German, French, Italian</td></tr>
<tr><td>MultEURLEX</td><td> <a href="https://arxiv.org/abs/2109.00904">Chalkidis et al. </a> </td><td>Multi-label Text Classification</td><td>23 languages (see below)</td></tr>

</table>

### Languages
see Split section

## Dataset Structure

### Data Instances

#### German_LER

German_LER example

```python
from datasets import load_dataset
dataset = load_dataset('jfrenz/legalglue', 'german_ler')
```

```json
{
  'id': '66722',
  'tokens':['4.', 'Die', 'Kostenentscheidung', 'für', 'das', 'gerichtliche', 'Antragsverfahren', 'beruht', 'auf', '§', '21', 'Abs.', '2', 'Satz', '1', 'i.', 'V.', 'm.', '§', '20', 'Abs.', '1', 'Satz', '1', 'WBO', '.'],
  'ner_tags': [38, 38, 38, 38, 38, 38, 38, 38, 38, 3, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 38]
}

```
#### LeNER-Br

LeNER-Br example

```python
from datasets import load_dataset
dataset = load_dataset('jfrenz/legalglue', 'lener_br')
```


```json
{
  'id': '7826',
  'tokens': ['Firmado', 'por', 'assinatura', 'digital', '(', 'MP', '2.200-2/2001', ')', 'JOSÉ', 'ROBERTO', 'FREIRE', 'PIMENTA', 'Ministro', 'Relator', 'fls', '.', 'PROCESSO', 'Nº', 'TST-RR-1603-79.2010.5.20.0001'],
  'ner_tags': [0, 0, 0, 0, 0, 9, 10, 0, 3, 4, 4, 4, 0, 0, 0, 0, 11, 12, 12]}
```

#### SwissJudgmentPrediction

swissJudgmentPrediction_de example

```python
from datasets import load_dataset
dataset = load_dataset('jfrenz/legalglue', 'swissJudgmentPrediction_de')
```

```json
{
  'id': 48755,
  'year': 2014,
  'text': "Sachverhalt: A. X._ fuhr am 25. Juli 2012 bei Mülligen mit seinem Personenwagen auf dem zweiten Überholstreifen der Autobahn A1 in Richtung Zürich. Gemäss Anklage schloss er auf einen Lieferwagen auf und schwenkte vom zweiten auf den ersten Überholstreifen aus. Danach fuhr er an zwei Fahrzeugen rechts vorbei und wechselte auf die zweite Überholspur zurück. B. Das Obergericht des Kantons Aargau erklärte X._ am 14. Januar 2014 zweitinstanzlich der groben Verletzung der Verkehrsregeln schuldig. Es bestrafte ihn mit einer bedingten Geldstrafe von 30 Tagessätzen zu Fr. 430.-- und einer Busse von Fr. 3'000.--. C. X._ führt Beschwerde in Strafsachen. Er beantragt, er sei von Schuld und Strafe freizusprechen. Eventualiter sei die Sache an die Vorinstanz zurückzuweisen. ",
  'label': 0,
  'language': 'de',
  'region': 'Northwestern Switzerland',
  'canton': 'ag',
  'legal area': 'penal law'
}
```

#### MultiEURLEX

Monolingual example out of the MultiEURLEX-Dataset

```python
from datasets import load_dataset
dataset = load_dataset('jfrenz/legalglue', 'multi_eurlex_de')
```


```json
{
  'celex_id': '32002R0130',
  'text': 'Verordnung (EG) Nr. 130/2002 der Kommission\nvom 24. Januar 2002\nbezüglich der im Rahmen der Auss...',
  'labels': [3, 17, 5]}
```

Multilingual example out of the MultiEURLEX-Dataset

```python
from datasets import load_dataset
dataset = load_dataset('jfrenz/legalglue', 'multi_eurlex_all_languages')
```

```json
{
  'celex_id': '32002R0130',
  'text': {
    'bg': None,
    'cs': None,
    'da': 'Kommissionens ...',
    'de': 'Verordnung ... ',
    'el': '...',
    'en': '...',
    ...
    },
    'labels': [3, 17, 5]
  }
```
### Data Fields

#### German_LER

- `id`: id of the sample
- `tokens`: the tokens of the sample text
- `ner_tags`: the NER tags of each token


#### LeNER_Br

- `id`: id of the sample
- `tokens`: the tokens of the sample text
- `ner_tags`: the NER tags of each token

#### SwissJudgmentPrediction

- `id`: (**int**) ID of the document
- `year`: (**int**) the publication year
- `text`: (**str**) the facts of the case
- `label`: (**class label**) the judgment outcome: 0 (dismissal) or 1 (approval)
- `language`: (**str**) one of (de, fr, it)
- `region`: (**str**) the region of the lower court
- `canton`: (**str**) the canton of the lower court
- `legal area`: (**str**) the legal area of the case


#### MultiEURLEX

Monolingual use:

- `celex_id`: (**str**)  Official Document ID of the document
- `text`: (**str**)  An EU Law
- `labels`: (**List[int]**) List of relevant EUROVOC concepts (labels)

Multilingual use:

- `celex_id`: (**str**)  Official Document ID of the document
- `text`: (dict[**str**])  A dictionary with the 23 languages as keys and the corresponding EU Law as values.
- `labels`: (**List[int]**) List of relevant EUROVOC concepts (labels)

The labels lists consists per default of level 1 EUROVOC concepts. Can be changed by adding the label_level parameter when loading the dataset. (available levels: level_1, level_2, level_3, all_levels)
```python
from datasets import load_dataset
dataset = load_dataset('jfrenz/legalglue', 'multi_eurlex_de', label_level="level_3")
```

### Data Splits

<table>
<tr><th>Dataset</th><th> Language </th> <th>   ISO code </th> <th>   Number of Documents train/dev/test </th> </tr>
<tr><td>German-LER</td><td>German</td> <td><b>de</b></td> <td>  66723 / - / -  </td> </tr>
<tr><td>LeNER-Br</td><td>Portuguese</td> <td><b>pt</b></td> <td>   7828 / 1177 / 1390 </td> </tr>
<tr><td rowspan="3">SwissJudgmentPrediction</td><td>German</td> <td><b>de</b></td> <td>  35458 / 4705 / 9725 </td> </tr>
<tr><td> French </td><td><b>fr</b></td><td>  21179 / 3095 / 6820 </td> </tr>
<tr><td> Italian </td><td><b>it</b></td><td>  3072 / 408 / 812 </td> </tr>
<tr><td rowspan="23">MultiEURLEX</td><td>English     </td> <td><b>en</b></td> <td>  55,000 / 5,000 / 5,000 </td> </tr>
<tr><td> German      </td> <td>  <b>de</b>   </td> <td> 55,000 / 5,000 / 5,000 </td> </tr>
<tr><td> French      </td> <td>  <b>fr</b>   </td> <td> 55,000 / 5,000 / 5,000 </td> </tr>
<tr><td> Italian     </td> <td>  <b>it</b>   </td> <td>  55,000 / 5,000 / 5,000 </td> </tr>
<tr><td> Spanish     </td> <td>  <b>es</b>   </td> <td>  52,785 / 5,000 / 5,000 </td> </tr>
<tr><td> Polish      </td> <td>  <b>pl</b>   </td> <td>  23,197 / 5,000 / 5,000 </td> </tr>  
<tr><td> Romanian    </td> <td>  <b>ro</b>   </td> <td>  15,921 / 5,000 / 5,000 </td> </tr>  
<tr><td> Dutch       </td> <td>  <b>nl</b>   </td> <td>  55,000 / 5,000 / 5,000 </td> </tr>  
<tr><td> Greek       </td> <td>  <b>el</b>   </td> <td>  55,000 / 5,000 / 5,000 </td> </tr>  
<tr><td> Hungarian   </td> <td>  <b>hu</b>   </td> <td>  22,664 / 5,000 / 5,000 </td> </tr>  
<tr><td> Portuguese  </td> <td>  <b>pt</b>   </td> <td>  23,188 / 5,000 / 5,000 </td> </tr>  
<tr><td> Czech       </td> <td>  <b>cs</b>   </td> <td>  23,187 / 5,000 / 5,000 </td> </tr>  
<tr><td> Swedish     </td> <td>  <b>sv</b>   </td> <td>  42,490 / 5,000 / 5,000 </td> </tr>  
<tr><td> Bulgarian   </td> <td>  <b>bg</b>   </td> <td>  15,986 / 5,000 / 5,000 </td> </tr>  
<tr><td> Danish      </td> <td>  <b>da</b>   </td> <td>  55,000 / 5,000 / 5,000 </td> </tr>  
<tr><td> Finnish     </td> <td>  <b>fi</b>   </td> <td>  42,497 / 5,000 / 5,000 </td> </tr>  
<tr><td> Slovak      </td> <td>  <b>sk</b>   </td> <td>  15,986 / 5,000 / 5,000 </td> </tr>  
<tr><td> Lithuanian  </td> <td>  <b>lt</b>   </td> <td>  23,188 / 5,000 / 5,000 </td> </tr>  
<tr><td> Croatian    </td> <td>  <b>hr</b>   </td> <td>  7,944 / 2,500 / 5,000  </td> </tr>  
<tr><td> Slovene     </td> <td>  <b>sl</b>   </td> <td>  23,184 / 5,000 / 5,000 </td> </tr>  
<tr><td> Estonian    </td> <td>  <b>et</b>   </td> <td>  23,126 / 5,000 / 5,000 </td> </tr>
<tr><td> Latvian     </td> <td>  <b>lv</b>   </td> <td>  23,188 / 5,000 / 5,000 </td> </tr>  
<tr><td> Maltese     </td> <td>  <b>mt</b>   </td> <td>  17,521 / 5,000 / 5,000 </td> </tr>  
</table>

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

[More Information Needed]
