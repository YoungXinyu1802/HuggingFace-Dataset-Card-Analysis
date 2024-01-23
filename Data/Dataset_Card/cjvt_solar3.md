---
annotations_creators:
- expert-generated
language_creators:
- other
language:
- sl
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
- 1K<n<10K
source_datasets:
- original
task_categories:
- text2text-generation
- other
task_ids: []
pretty_name: solar3
tags:
- grammatical-error-correction
- other-token-classification-of-text-errors
---

# Dataset Card for solar3

### Dataset Summary

Šolar* is a developmental corpus of 5485 school texts (e.g., essays), written by students in Slovenian secondary schools 
(age 15-19) and pupils in the 7th-9th grade of primary school (13-15), with a small percentage also from the 6th grade. 
Part of the corpus (1516 texts) is annotated with teachers' corrections using a system of labels described in the 
document available at https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1589/Smernice-za-oznacevanje-korpusa-Solar_V1.1.pdf (in Slovenian).

\(*) pronounce "š" as "sh" in "shoe".

By default the dataset is provided at **sentence-level** (125867 instances): each instance contains a source (the original) and a target (the corrected) sentence. Note that either the source or the target sentence in an instance may be missing - this usually happens when a source sentence is marked as redundant or when a new sentence is added by the teacher. Additionally, a source or a target sentence may appear in multiple instances - for example, this happens when one sentence gets divided into multiple sentences.

There is also an option to aggregate the instances at the **document-level** or **paragraph-level** 
by explicitly providing the correct config:  
```
datasets.load_dataset("cjvt/solar3", "paragraph_level")`
datasets.load_dataset("cjvt/solar3", "document_level")`  
```

### Supported Tasks and Leaderboards

Error correction, e.g., at token/sequence level, as token/sequence classification or text2text generation.

### Languages

Slovenian.

## Dataset Structure

### Data Instances

A sample instance from the dataset:
```json
{
	'id_doc': 'solar1', 
	'doc_title': 'KUS-G-slo-1-GO-E-2009-10001', 
	'is_manually_validated': True, 
	'src_tokens': ['”', 'Ne', 'da', 'sovražim', ',', 'da', 'ljubim', 'sem', 'na', 'svetu', '”', ',', 'izreče', 'Antigona', 'v', 'bran', 'kralju', 'Kreonu', 'za', 'svoje', 'nasprotno', 'mišljenje', 'pred', 'smrtjo', '.'], 
	'src_ling_annotations': {
		# truncated for conciseness
		'lemma': ['”', 'ne', 'da', 'sovražiti', ...], 
		'ana': ['mte:U', 'mte:L', 'mte:Vd', ...],		
		'msd': ['UPosTag=PUNCT', 'UPosTag=PART|Polarity=Neg', 'UPosTag=SCONJ', ...], 
		'ne_tag': [..., 'O', 'B-PER', 'O', ...],
        'space_after': [False, True, True, False, ...]
	}, 
	'tgt_tokens': ['„', 'Ne', 'da', 'sovražim', ',', 'da', 'ljubim', 'sem', 'na', 'svetu', ',', '”', 'izreče', 'Antigona', 'sebi', 'v', 'bran', 'kralju', 'Kreonu', 'za', 'svoje', 'nasprotno', 'mišljenje', 'pred', 'smrtjo', '.'], 
	# omitted for conciseness, the format is the same as in 'src_ling_annotations'
	'tgt_ling_annotations': {...}, 
	'corrections': [
		{'idx_src': [0], 'idx_tgt': [0], 'corr_types': ['Z/LOČ/nerazvrščeno']}, 
		{'idx_src': [10, 11], 'idx_tgt': [10, 11], 'corr_types': ['Z/LOČ/nerazvrščeno']}, 
		{'idx_src': [], 'idx_tgt': [14], 'corr_types': ['O/KAT/povratnost']}
	]
}
```

The instance represents a correction in the document 'solar1' (`id_doc`), which were manually assigned/validated (`is_manually_validated`). More concretely, the source sentence contains three errors (as indicated by three elements in `corrections`):  
- a punctuation change: '”' -> '„';  
- a punctuation change: ['”', ','] -> [',', '”'] (i.e. comma inside the quote, not outside);
- addition of a new word: 'sebi'.

### Data Fields

- `id_doc`: a string containing the identifying name of the document in which the sentence appears;  
- `doc_title`: a string containing the assigned document title;  
- `is_manually_validated`: a bool indicating whether the document in which the sentence appears was reviewed by a teacher;   
- `src_tokens`: words in the source sentence (`[]` if there is no source sentence);  
- `src_ling_annotations`: a dict containing the lemmas (key `"lemma"`), morphosyntactic descriptions using UD (key `"msd"`) and JOS/MULTEXT-East (key `"ana"`) specification, named entity tags encoded using IOB2 (key `"ne_tag"`) for the source tokens (**automatically annotated**), and spacing information (key `"space_after"`), i.e. whether there is a whitespace after each token;   
- `tgt_tokens`: words in the target sentence (`[]` if there is no target sentence);  
- `tgt_ling_annotations`: a dict containing the lemmas (key `"lemma"`), morphosyntactic descriptions using UD (key `"msd"`) and JOS/MULTEXT-East (key `"ana"`) specification, named entity tags encoded using IOB2 (key `"ne_tag"`) for the target tokens (**automatically annotated**), and spacing information (key `"space_after"`), i.e. whether there is a whitespace after each token;
- `corrections`: a list of the corrections, with each correction represented with a dictionary, containing the indices of the source tokens involved (`idx_src`), target tokens involved (`idx_tgt`), and the categories of the corrections made (`corr_types`). Please note that there can be multiple assigned categories for one annotated correction, in which case `len(corr_types) > 1`.  


## Dataset Creation

The Developmental corpus Šolar consists of 5,485 texts written by students in Slovenian secondary schools (age 15-19) and pupils in the 7th-9th grade of primary school (13-15), with a small percentage also from the 6th grade. The information on school (elementary or secondary), subject, level (grade or year), type of text, region, and date of production is provided for each text. School essays form the majority of the corpus while other material includes texts created during lessons, such as text recapitulations or descriptions, examples of formal applications, etc.

Part of the corpus (1516 texts) is annotated with teachers' corrections using a system of labels described in the attached document (in Slovenian). Teacher corrections were part of the original files and reflect real classroom situations of essay marking. Corrections were then inserted into texts by annotators and subsequently categorized. Due to the annotations being gathered in a practical (i.e. classroom) setting, only the most relevant errors may sometimes be annotated, e.g., not all incorrectly placed commas are annotated if there is a bigger issue in the text. 

## Additional Information

### Dataset Curators

Špela Arhar Holdt; et al. (please see http://hdl.handle.net/11356/1589 for the full list)

### Licensing Information

CC BY-NC-SA 4.0.

### Citation Information

```
@misc{solar3,
  title = {Developmental corpus {\v S}olar 3.0},
  author = {Arhar Holdt, {\v S}pela and Rozman, Tadeja and Stritar Ku{\v c}uk, Mojca and Krek, Simon and Krap{\v s} Vodopivec, Irena and Stabej, Marko and Pori, Eva and Goli, Teja and Lavri{\v c}, Polona and Laskowski, Cyprian and Kocjan{\v c}i{\v c}, Polonca and Klemenc, Bojan and Krsnik, Luka and Kosem, Iztok},
   url = {http://hdl.handle.net/11356/1589},
   note = {Slovenian language resource repository {CLARIN}.{SI}},
   year = {2022}
 }
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.
