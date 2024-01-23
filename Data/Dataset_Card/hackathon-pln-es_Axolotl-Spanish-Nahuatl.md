---
annotations_creators:
- expert-generated

language_creators:
- expert-generated

language:
- es
language_bcp47:
- es-MX
license:
- mpl-2.0

multilinguality:
- translation

pretty_name: "Axolotl Spanish-Nahuatl parallel corpus , is a digital corpus that compiles several sources with parallel content in these two languages. \n\nA parallel corpus is a type of corpus that contains texts in a source language with their correspondent translation in one or more target languages.
Gutierrez-Vasques, X., Sierra, G., and Pompa, I. H. (2016). Axolotl: a web accessible parallel corpus for spanish-nahuatl. In Proceedings of the Ninth International Conference on Language Resources and Evaluation (LREC 2016), Portoro, Slovenia. European Language Resources Association (ELRA).
Grupo de Ingenieria Linguistica (GIL, UNAM). Corpus paralelo espaÃ±ol-nahuatl. http://www.corpus.unam.mx/axolotl."

size_categories:
- unknown

source_datasets:
- original

task_categories:
- conditional-text-generation

task_ids:
- machine-translation
---

# Axolotl-Spanish-Nahuatl : Parallel corpus for Spanish-Nahuatl machine translation

## Table of Contents
- [Dataset Card for [Axolotl-Spanish-Nahuatl]](#dataset-card-for-Axolotl-Spanish-Nahuatl)


## Dataset Description

- **Source 1:** http://www.corpus.unam.mx/axolotl
- **Source 2:** http://link.springer.com/article/10.1007/s10579-014-9287-y
- **Repository:1** https://github.com/ElotlMX/py-elotl
- **Repository:2** https://github.com/christos-c/bible-corpus/blob/master/bibles/Nahuatl-NT.xml
- **Paper:** https://aclanthology.org/N15-2021.pdf

## Dataset Collection

In order to get a good translator, we collected and cleaned two of the most complete Nahuatl-Spanish parallel corpora available. Those are Axolotl collected by an expert team at UNAM and Bible UEDIN Nahuatl Spanish crawled by Christos Christodoulopoulos and Mark Steedman from Bible Gateway site.

After this, we ended with 12,207 samples from Axolotl due to misalignments and duplicated texts in Spanish in both original and nahuatl columns and 7,821 samples from Bible UEDIN for a total of 20028 utterances.


## Team members
- Emilio Morales [(milmor)](https://huggingface.co/milmor)
- Rodrigo Martínez Arzate  [(rockdrigoma)](https://huggingface.co/rockdrigoma)
- Luis Armando Mercado [(luisarmando)](https://huggingface.co/luisarmando)
- Jacobo del Valle [(jjdv)](https://huggingface.co/jjdv)

## Applications

- MODEL: Spanish Nahuatl Translation Task with a T5 model in ([t5-small-spanish-nahuatl](https://huggingface.co/hackathon-pln-es/t5-small-spanish-nahuatl))
- DEMO: Spanish Nahuatl Translation in ([Spanish-nahuatl](https://huggingface.co/spaces/hackathon-pln-es/Spanish-Nahuatl-Translation))