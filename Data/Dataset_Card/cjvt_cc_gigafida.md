---
annotations_creators:
- no-annotation
language:
- sl
language_creators:
- found
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
pretty_name: Written corpus ccGigafida 1.0
size_categories:
- 10K<n<100K
- 100M<n<1B
source_datasets: []
tags:
- gigafida
- gigafida2
- kres
- cckres
- reference corpus
task_categories:
- fill-mask
- text-generation
task_ids:
- masked-language-modeling
- language-modeling
---

# Dataset Card for ccGigafida

This repository by default loads the publicly available dataset ccGigafida, which contains a small subset of the Gigafida/Gigafida2 corpus. 
The full datasets are private due to copyright. **If you happen to have access to the full datasets, the script will also work with those.**
Instead of  
```
datasets.load_dataset("cjvt/cc_gigafida")
```  
please use  
```
datasets.load_dataset("cjvt/cc_gigafida", "private", data_dir="<directory-containing-gigafida(2)-TEI-files>")
```  

**IMPORTANT:** The script will process all `.xml` files in the provided directory and its subdirectories - make sure there are no schema or metadata files in there!  


### Dataset Summary

ccGigafida is a reference corpus of Slovene texts. It is a publicly available subsample of an even larger reference corpus, Gigafida (and its successor Gigafida 2). 
The Gigafida corpus is an extensive collection of Slovene text of various genres, from daily newspapers, magazines, all kinds of books (fiction, non-fiction, textbooks), 
web pages, transcriptions of parliamentary debates and similar.

### Supported Tasks and Leaderboards

Language modeling.

### Languages

Slovenian.

## Dataset Structure

### Data Instances

The data is loaded at document-level, i.e. one instance is one document.
```
{
  'id_doc': 'F0000123',
  'doc_title': 'Novi tednik NT&RC',
  'authors': ['neznani novinar'],
  'publish_date': '1998-03-27',
  'publisher': 'Novi tednik',
  'genres': ['tisk/periodično/časopis'],
  'doc_tokenized': [
    [
      ['Po', 'nekajletnem', 'počitku', 'pa', 'se', 'vračajo', 'tudi', 'kralji', 'dark', 'rock', 'godbe', 'JESUS', 'AND', 'THE', 'MARY', 'CHAIN', '.'],
      ['Brata', 'Reid', 'bosta', 'svojo', 'najnovejšo', 'kreacijo', '»', 'Cracking', 'Up', '«', 'objavila', 'v', 'ponedeljek', 'pri', 'trenutno', 'najuspešnejši', 'neodvisni', 'založbi', 'Creation', '(', 'vodi', 'jo', 'njun', 'nekdanji', 'menager', 'Alan', 'McGee', ',', 'zanjo', 'pa', 'poleg', 'Oasis', 'snema', 'še', 'cel', 'kup', 'popularnih', 'brit', '-', 'popovcev', ')', ',', 'tej', 'pa', 'bo', 'kmalu', 'sledil', 'tudi', 'album', '»', 'Munki', '«', '.']
    ],
    [
      ['Kultni', 'ameriški', 'tehno', 'freak', 'PLASTIKMAN', 'že', 'vrsto', 'let', 'velja', 'za', 'enega', 'izmed', 'najbolj', 'inovativnih', 'in', 'produktivnih', 'ustvarjalcev', 'sodobne', 'elektronske', 'glasbe', '.'],
      ['Za', 'založbo', 'Nova', 'Mute', 'je', 'v', 'preteklih', 'nekaj', 'letih', 'posnel', 'cel', 'kup', 'izvrstnih', 'underground', 'dance', 'glasbenih', 'izdelkov', ',', 'pred', 'nedavnim', 'pa', 'je', 'ljubitelje', 'tovrstne', 'godbe', 'presenetil', 'z', 'ambientalnimi', 'odisejadami', ',', 'zbranimi', 'na', 'LP-ju', '»', 'Refused', '«', ',', 'ki', 'ga', 'lahko', 'od', 'prejšnjega', 'ponedeljka', 'kupite', 'tudi', 'v', 'bolje', 'založenih', 'trgovinah', 'z', 'nosilci', 'zvoka', 'na', 'sončni', 'strani', 'Alp', '.']
    ],
    [
      ['STANE', 'ŠPEGEL']
    ]
  ],
  'doc_lemmas': [...],
  'doc_msds': [...],
  'doc_string': [
    [
      'Po nekajletnem počitku pa se vračajo tudi kralji dark rock godbe JESUS AND THE MARY CHAIN. ',
      'Brata Reid bosta svojo najnovejšo kreacijo »Cracking Up« objavila v ponedeljek pri trenutno najuspešnejši neodvisni založbi Creation (vodi jo njun nekdanji menager Alan McGee, zanjo pa poleg Oasis snema še cel kup popularnih brit-popovcev), tej pa bo kmalu sledil tudi album »Munki«.'
    ],
    [
      'Kultni ameriški tehno freak PLASTIKMAN že vrsto let velja za enega izmed najbolj inovativnih in produktivnih ustvarjalcev sodobne elektronske glasbe. ',
      'Za založbo Nova Mute je v preteklih nekaj letih posnel cel kup izvrstnih underground dance glasbenih izdelkov, pred nedavnim pa je ljubitelje tovrstne godbe presenetil z ambientalnimi odisejadami, zbranimi na LP-ju »Refused«, ki ga lahko od prejšnjega ponedeljka kupite tudi v bolje založenih trgovinah z nosilci zvoka na sončni strani Alp.'
    ],
    [
      'STANE ŠPEGEL'
    ]
  ],
  'id_sents': [['F0000123.000005.0', 'F0000123.000005.1'], ['F0000123.000013.0', 'F0000123.000013.1'], ['F0000123.000020.0']]
}
```


### Data Fields

- `id_doc`: the document ID (string); 
- `doc_title`: the document title (string);
- `authors`: author(s) of the document (list of string): "neznani novinar" (sl) = ("unknown/unspecified journalist");
- `publish_date`: publish date (string);
- `publisher`: publisher, e.g., the name of a news agency (string);
- `genres`: genre(s) of the document (list of string) - possible genres: `['tisk', 'tisk/knjižno', 'tisk/knjižno/leposlovno', 'tisk/knjižno/strokovno', 'tisk/periodično', 'tisk/periodično/časopis', 'tisk/periodično/revija', 'tisk/drugo', 'internet']`;
- `doc_tokenized`: tokenized document - the top level lists represent paragraphs, the lists in the level deeper represent sentences, and each sentence contains tokens;
- `doc_lemmas`: lemmatized document - same structure as `doc_tokenized`;
- `doc_msds`: MSD tags of the document - same structure as `doc_tokenized` ([tagset](http://nl.ijs.si/ME/V6/msd/html/msd-sl.html));
- `doc_string`: same as `doc_tokenized` but with properly placed spaces in sentences;
- `id_sents`: IDs of sentences contained inside paragraphs of the document.   

## Dataset Creation

Gigafida consists of texts which were published between 1990 and 2011. The texts come from printed sources and from the web. 
Printed part contains fiction, non-fiction and textbooks, and periodicals such as daily newspapers and magazines. 
Texts originating from the web were published on news portals, pages of big Slovene companies and more important governmental, 
educational, research, cultural and similar institutions.  

For more information, please check http://eng.slovenscina.eu/korpusi/gigafida.

## Additional Information

### Dataset Curators

Nataša Logar; et al. (please see http://hdl.handle.net/11356/1035 for the full list)

### Licensing Information

CC BY-NC-SA 4.0.

### Citation Information

```
@misc{ccGigafida,
    title = {Written corpus {ccGigafida} 1.0},
    author = {Logar, Nata{\v s}a and Erjavec, Toma{\v z} and Krek, Simon and Gr{\v c}ar, Miha and Holozan, Peter},
    url = {http://hdl.handle.net/11356/1035},
    note = {Slovenian language resource repository {CLARIN}.{SI}},
    copyright = {Creative Commons - Attribution-{NonCommercial}-{ShareAlike} 4.0 International ({CC} {BY}-{NC}-{SA} 4.0)},
    issn = {2820-4042},
    year = {2013}
}
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.
