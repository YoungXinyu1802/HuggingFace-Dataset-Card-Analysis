---
license: cc-by-sa-4.0
---

Possibly a placeholder dataset for the original here: https://huggingface.co/datasets/bigscience-catalogue-data/bias-shades

# Data Statement for SHADES

> **How to use this document:**
> Fill in each section according to the instructions. Give as much detail as you can, but there's no need to extrapolate. The goal is to help people understand your data when they approach it. This could be someone looking at it in ten years, or it could be you yourself looking back at the data in two years.

> For full details, the best source is the original Data Statements paper, here: https://www.aclweb.org/anthology/Q18-1041/ .

> Instruction fields are given as blockquotes; delete the instructions when you're done, and provide the file with your data, for example as "DATASTATEMENT.md". The lists in some blocks are designed to be filled in, but it's good to also leave a written description of what's happening, as well as the list. It's fine to skip some fields if the information isn't known.

> Only blockquoted content should be deleted; the final about statement should be left intact.

Data set name: Bias-Shades

Citation (if available): TODO.

Data set developer(s): This dataset was compiled by dozens of research scientists through the BigScience open science collaboration. Collaborators, representing numerous cultures and languages, joined the project of their own volition.

Data statement author(s): Shayne Longpre, Aurélie Névéol, Shanya Sharma[Add name here if you add/edit the data statement :)].

Others who contributed to this document: N/A

License: Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0).

## A. CURATION RATIONALE 

> *Explanation.* Which texts were included and what were the goals in selecting texts, both in the original collection and in any further sub-selection? This can be especially important in datasets too large to thoroughly inspect by hand. An explicit statement of the curation rationale can help dataset users make inferences about what other kinds of texts systems trained with them could conceivably generalize to.

This dataset was curated by hand-crafting stereotype sentences by native speakers from the culture which is being targeted. An initial set of sentences was inferred from stereotypes expressed in the crowS-pairs data set(Nangia et al.). Native speakers first crafted templates for sentences expressing a stereotype. These templates are marked for gender and plurality of the target nouns, so the template can be reused by substituting different targets. Next, the template-target noun pair combinations were annotated for the veracity/reliability of the expressed stereotype. The resulting sentences express common and less common stereotypes in a variety of cultures and languages.


## B. LANGUAGE VARIETY/VARIETIES

> *Explanation.* Languages differ from each other in structural ways that can interact with NLP algorithms. Within a language, regional or social dialects can also show great variation (Chambers and Trudgill, 1998). The language and language variety should be described with a language tag from BCP-47 identifying the language variety (e.g., en-US or yue-Hant-HK), and a prose description of the language variety, glossing the BCP-47 tag and also providing further information (e.g., "English as spoken in Palo Alto, California", or "Cantonese written with traditional characters by speakers in Hong Kong who are bilingual in Mandarin").

* BCP-47 language tags: en-US, fr-FR, hi-IN, es-DO, ar-LY, ru-RU, de-DE, nl-NL, ta-IN.
* Language variety description: English spoken by native speakers of the United States, native French people from metropolitan France, native Hindi and Tamil speakers from India, Spanish speakers from the Dominican Republic, Arabic speakers from Libya, Russian speakers from Russia, German speakers from Germany, and Dutch speakers from the Netherlands.

## C. CONTRIBUTOR DEMOGRAPHIC
> ## C. SPEAKER DEMOGRAPHIC

> *Explanation.* Sociolinguistics has found that variation (in pronunciation, prosody, word choice, and grammar) correlates with speaker demographic characteristics (Labov, 1966), as speakers use linguistic variation to construct and project identities (Eckert and Rickford, 2001). Transfer from native languages (L1) can affect the language produced by non-native (L2) speakers (Ellis, 1994, Ch. 8). A further important type of variation is disordered speech (e.g., dysarthria). Specifications include: 

Participants to the collection project were recruited through the HuggingFace BigScience project, and specifically the Bias and Fairness Evaluation group. Listed below.

Speakers:
* [ADD YOURSELF!]
* Shayne Longpre: English-speaking, male, 28 years old, culturally Canadian.
* Aurélie Névéol: French (native), English and Spanish speaking, female, 44 years old, culturally French (also familiar with American culture)
* Shanya Sharma: Hindi(native), English speaking, female, 24 years old, culturally Indian
* Margaret Mitchell: English, female, mid-30s, U.S.A.
* Maraim Masoud: Arabic, English Speaking female.

 
## D. ANNOTATOR DEMOGRAPHIC

> *Explanation.* What are the demographic characteristics of the annotators and annotation guideline developers? Their own “social address” influences their experience with language and thus their perception of what they are annotating. Specifications include:

Participants to the collection project were recruited through the HuggingFace BigScience project, and specifically the Bias and Fairness Evaluation group. Speaker and annotator contributors listed in section C.


## E. SPEECH SITUATION

N/A

## F. TEXT CHARACTERISTICS

> *Explanation.* Both genre and topic influence the vocabulary and structural characteristics of texts (Biber, 1995), and should be specified.

Collected data is a collection of offensive stereotyped statements in numerous languages and cultures. They might be upsetting and/or offensive.

Along with these stereotyped statements are annotation judgements of how prevalent/real the expressed stereotypes are in the real world. Some statements were created from templates with substituted target nouns, and therefore may express an uncommon or unlikely stereotype.

## G. RECORDING QUALITY

N/A

## H. OTHER

> *Explanation.* There may be other information of relevance as well. Please use this space to develop any further categories that are relevant for your dataset. 

## I. PROVENANCE APPENDIX

This initiative is part of the BigScience Workshop: https://bigscience.huggingface.co/.


## About this document

A data statement is a characterization of a dataset that provides context to allow developers and users to better understand how experimental results might generalize, how software might be appropriately deployed, and what biases might be reflected in systems built on the software.

Data Statements are from the University of Washington. Contact: [datastatements@uw.edu](mailto:datastatements@uw.edu). This document template is licensed as [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/).

This version of the markdown Data Statement is from June 4th 2020. The Data Statement template is based on worksheets distributed at the [2020 LREC workshop on Data Statements](https://sites.google.com/uw.edu/data-statements-for-nlp/), by Emily M. Bender, Batya Friedman, and Angelina McMillan-Major. Adapted to community Markdown template by Leon Dercyznski.