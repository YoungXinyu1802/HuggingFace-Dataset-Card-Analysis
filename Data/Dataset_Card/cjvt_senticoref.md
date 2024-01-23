---
license: cc-by-sa-4.0
task_categories:
- token-classification
language:
- sl
tags:
- coreference resolution
pretty_name: SentiCoref
size_categories:
- n<1K
---

# Dataset Card for SentiCoref

### Dataset Summary

SentiCoref is a Slovenian coreference resolution dataset containing **391962** tokens inside **756** documents*.  
Also contains automatically (?) annotated named entities and manually verified lemmas and morphosyntactic tags (MSD). 

\* This is the latest version of SentiCoref, contained in SUK: Slovenian training corpus.

### Supported Tasks and Leaderboards

Coreference resolution.

### Languages

Slovenian.

## Dataset Structure

### Data Instances

A sample instance from the dataset, with most actual data truncated for the purpose of clarity:
```
{
    "id_doc": "senticoref3408",
    "words": [
        [
            ["Ljubljana", "-", "Upravi", "trgovske", "družbe",  "Mercator", "se", "je", "z", "letom", "2010", ...],
            ...
        ],
        ...
    ],
    "lemmas": [
        [
            ["Ljubljana", "-", "uprava", "trgovski", "družba", "Mercator", "se", "biti", "z", "leto", "2010", ...],
            ...
        ],
        ...
    ],
    "msds": [
        [
            ["mte:Slzei", "mte:U", "mte:Sozed", "mte:Ppnzer", "mte:Sozer", "mte:Slmei", "mte:Zp------k", ...],
            ...
        ],
        ...
    ],
    "ne_tags": [
        [
            ["B-LOC", "O", "O", "O", "O", "B-ORG", "O", "O", ...],
            ...
        ],
        ...
    ],
    "mentions": [
        {
            "id_mention": "senticoref3408.1.1.ne1",
            "mention_data": {
                "idx_par": 0,
                "idx_sent": 0,
                "word_indices": [0],
                "global_word_indices": [0]
            }
        }, 
        ...
    ],
    "coref_clusters": [
        ["senticoref3408.1.1.phr17-1", "senticoref3408.1.2.t7", "senticoref3408.1.2.ne2", "senticoref3408.1.4.ne3"], 
        ...
    ]
}
```

### Data Fields

Please note that documents are represented as lists of paragraphs, which are in turn lists of words. 
This means that `words`, `lemmas`, `msds`, and `ne_tags` are of type List[List[List[string]]].
This is done because it is easier to discard the segmentation information than re-obtain it.

- `id_doc`: the identifier of the document;  
- `words`: words in the document;
- `lemmas`: lemmas in the document;
- `msds`: [morphosyntactic tags](https://nl.ijs.si/ME/V6/msd/) in the document;
- `ne_tags`: named entity annotations in IOB2 format;
- `mentions`: list of entity mentions in the document. Includes named entities, phrases, and single words (e.g., pronouns). Each mention is represented with its ID and the
  indices of contained words: either (1) the index of the paragraph, the sentence inside the paragraph, and the positions inside the sentence, or
  (2) the global word index that can be used on a flattened list of document words;
- `coref_clusters`: coreference clusters present in the document. Each list represents one cluster of entity mentions, represented by their IDs

## Additional Information

### Using the dataset

1. Unless you are doing something more sophisticated, feel free to drop the paragraph and sentence segmentation information by flattening the document words, lemmas, MSDs, and named entity tags:
```python
import datasets

data = datasets.load_dataset("cjvt/senticoref", split="train")
doc = data[0]

flattened_words = [w for par in doc["words"] for sent in par for w in sent]
# ... Do the same for other fields
```

2. To get a better understanding of the entity mentions and coreference clusters in the document, you can convert the mention information into a dictionary and
   link the mentions and clusters to the actual words.
```python
import datasets

data = datasets.load_dataset("cjvt/senticoref", split="train")
doc = data[0]
flattened_words = [w for par in doc["words"] for sent in par for w in sent]

id2mentiondata = {}
for mention in doc["mentions"]:
  id2mentiondata[mention['id_mention']] = mention['mention_data']

# Display the entity mention clusters in the string format
# (1) Using the flattened document structure and global word indices
for cluster in doc["coref_clusters"]:
  print("{")
  for id_mention in cluster:
    print(f"\t{[flattened_words[_i] for _i in id2mentiondata[id_mention]['global_word_indices']]}")
  print("}")
  print("")

# (2) Using the initial document structure and local word indices
for cluster in doc["coref_clusters"]:
  print("{")
  for id_mention in cluster:
    _mention_data = id2mentiondata[id_mention]
    idx_par, idx_sent = _mention_data["idx_par"], _mention_data["idx_sent"]
    print(f"\t{[doc['words'][idx_par][idx_sent][_i] for _i in _mention_data['word_indices']]}")
  print("}")
  print("")
```
**Output:**
```
...
{
	['trgovske', 'družbe', 'Mercator']
	['družbe']
	['Mercator']
	['Mercatorja']
}

{
	['letom', '2010']
	['leta', '2010']
}

... (truncated)
```

### Dataset Curators
 
Špela Arhar Holdt; et al. (please see http://hdl.handle.net/11356/1747 for the full list)

### Licensing Information

CC BY-SA 4.0.  

### Citation Information

```
@misc{suk,
    title = {Training corpus {SUK} 1.0},
    author = {Arhar Holdt, {\v S}pela and Krek, Simon and Dobrovoljc, Kaja and Erjavec, Toma{\v z} and Gantar, Polona and {\v C}ibej, Jaka and Pori, Eva and Ter{\v c}on, Luka and Munda, Tina and {\v Z}itnik, Slavko and Robida, Nejc and Blagus, Neli and Mo{\v z}e, Sara and Ledinek, Nina and Holz, Nanika and Zupan, Katja and Kuzman, Taja and Kav{\v c}i{\v c}, Teja and {\v S}krjanec, Iza and Marko, Dafne and Jezer{\v s}ek, Lucija and Zajc, Anja},
    url = {http://hdl.handle.net/11356/1747},
    note = {Slovenian language resource repository {CLARIN}.{SI}},
    year = {2022}
}
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.