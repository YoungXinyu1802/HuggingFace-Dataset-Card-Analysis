https://opus.nlpl.eu/XLEnt-v1.1.php

Uploaded from Opus to HuggingFace AI by Argos Open Tech.

 Corpus Name: XLEnt
     Package: XLEnt.de-en in Moses format
     Website: http://opus.nlpl.eu/XLEnt-v1.1.php
     Release: v1.1
Release date: Sun May 23 08:35:55 EEST 2021

This corpus is part of OPUS - the open collection of parallel corpora
OPUS Website: http://opus.nlpl.eu

If you use the dataset or code, please cite (pdf):  @inproceedings{elkishky_xlent_2021, author = {El-Kishky, Ahmed and Renduchintala, Adi and Cross, James and Guzmán, Francisco and Koehn, Philipp}, booktitle = {Preprint}, title = {{XLEnt}: Mining Cross-lingual Entities with Lexical-Semantic-Phonetic Word Alignment}, year = {2021}, address = Online, } and, please, acknowledge OPUS (bib, pdf) as well for this service.

This corpus was created by mining CCAligned, CCMatrix, and WikiMatrix parallel sentences. These three sources were themselves extracted from web data from Commoncrawl Snapshots and Wikipedia snapshots. Entity pairs were obtained by performing named entity recognition and typing on English sentences and projecting labels to non-English aligned sentence pairs. No claims of intellectual property are made on the work of preparation of the corpus. XLEnt consists of parallel entity mentions in 120 languages aligned with English. These entity pairs were constructed by performing named entity recognition (NER) and typing on English sentences from mined sentence pairs. These extracted English entity labels and types were projected to the non-English sentences through word alignment. Word alignment was performed by combining three alignment signals ((1) word co-occurence alignment with FastAlign (2) semantic alignment using LASER embeddings, and (3) phonetic alignment via transliteration) into a unified word-alignment model. This lexical/semantic/phonetic alignment approach yielded more than 160 million aligned entity pairs in 120 languages paired with English. Recognizing that each English is often aligned to mulitple entities in different target languages, we can join on English entities to obtain aligned entity pairs that directly pair two non-English entities (e.g., Arabic-French)  The original distribution is available from http://data.statmt.org/xlent/ The difference to version 1 is that pivoting now only uses the link with best score in case of alternative alignments for a pivot entity.

