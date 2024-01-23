---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- en
- pt
- es
license:
- cc-by-nc-sa-3.0
multilinguality:
- multilingual
paperswithcode_id: null
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- sequence-modeling
task_ids:
- language-modeling
---


## Dataset Description

- **Homepage:** [scielo.org](https://search.livros.scielo.org/search/?fb=&where=BOOK&filter%5Bis_comercial_filter%5D%5B%5D=f)

### Dataset Summary

This dataset contains all text from open-access PDFs on [scielo.org](https://search.livros.scielo.org/search/?fb=&where=BOOK&filter%5Bis_comercial_filter%5D%5B%5D=f). As of Dec. 5 2021, the total number of books available is 962. Some of them are not in native PDF format (e.g. scanned images) though.

### Supported Tasks and Leaderboards

- `sequence-modeling` or `language-modeling`: The dataset can be used to train a language model.

### Languages

As of Dec. 5 2021, there are 902 books in Portuguese, 55 in Spanish, and 5 in English.

## Dataset Structure

### Data Instances

Provide an JSON-formatted example and brief description of a typical instance in the dataset. If available, provide a link to further examples.

```
{
   "sbid":"23pcw",
   "id":"23pcw",
   "shortname":"",
   "title":"Educa\u00e7\u00e3o, sa\u00fade e esporte: novos\tdesafios \u00e0 Educa\u00e7\u00e3o F\u00edsica",
   "eisbn":"9788574554907",
   "isbn":"9788574554273",
   "author":"Farias, Gelcemar Oliveira; Nascimento, Juarez Vieira do",
   "corporate_authors":"",
   "translators":"",
   "coordinators":"",
   "editors":"",
   "others":"",
   "organizers":"",
   "collaborators":"",
   "publisher":"Editus",
   "language":"pt",
   "year": 2016,
   "synopsis":"\"A colet\u00e2nea contempla cap\u00edtulos que discutem a Educa\u00e7\u00e3o F\u00edsica a partir dos pressupostos da Educa\u00e7\u00e3o, da Sa\u00fade e do Esporte, enquanto importante desafio do momento atual e diante dos avan\u00e7os e das mudan\u00e7as que se consolidaram na forma\u00e7\u00e3o inicial em Educa\u00e7\u00e3o F\u00edsica. A obra convida a todos para a realiza\u00e7\u00e3o de futuras investiga\u00e7\u00f5es, no sentido de concentrar esfor\u00e7os para o fortalecimento de n\u00facleos de estudos e a sistematiza\u00e7\u00e3o de linhas de pesquisa.\"",
   "format":"",
   "type":"book",
   "is_public":"true",
   "is_comercial":"false",
   "publication_date":"2018-11-07",
   "_version_":"1718206093473087488",
   "pdf_url":"http://books.scielo.org//id/23pcw/pdf/farias-9788574554907.pdf",
   "pdf_filename":"farias-9788574554907.pdf",
   "metadata_filename":"farias-9788574554907.json",
   "text":"..."
}
```

### Data Fields

All fields are of string type except `year`. 

### Data Splits

All records are in the default `train` split.

## Dataset Creation

### Curation Rationale

Part of the big science efforts to create lanague modeling datasets.

### Source Data

[scielo.org](https://search.livros.scielo.org/search/?fb=&where=BOOK&filter%5Bis_comercial_filter%5D%5B%5D=f)

#### Initial Data Collection and Normalization

All PDFs are directly downloaded from the website and text is extracted with [pdftotext](https://pypi.org/project/pdftotext/) lib.

#### Who are the source language producers?

NA

### Annotations

No annotation is available.

#### Annotation process

NA

#### Who are the annotators?

NA

### Personal and Sensitive Information

NA

## Considerations for Using the Data

### Social Impact of Dataset

NA

### Discussion of Biases

NA

### Other Known Limitations

NA

## Additional Information

### Dataset Curators

[@chenghao](https://huggingface.co/chenghao)

### Licensing Information

Provide the license and link to the license webpage if available.

[CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)

### Contributions

NA