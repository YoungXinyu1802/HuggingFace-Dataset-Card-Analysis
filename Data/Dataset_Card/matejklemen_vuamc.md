---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- found
license:
- other
multilinguality:
- monolingual
pretty_name: VUA Metaphor Corpus
size_categories:
- 10K<n<100K
- 100K<n<1M
source_datasets: []
tags:
- metaphor-classification
- multiword-expression-detection
- vua20
- vua18
- mipvu
task_categories:
- text-classification
- token-classification
task_ids:
- multi-class-classification
---

# Dataset Card for VUA Metaphor Corpus

**Important note#1**: This is a slightly simplified but mostly complete parse of the corpus. What is missing are lemmas and some metadata that was not important at the time of writing the parser. See the section `Simplifications` for more information on this.  

**Important note#2**: The dataset contains metadata - to ignore it and correctly remap the annotations, see the section `Discarding metadata`.

### Dataset Summary

VUA Metaphor Corpus (VUAMC) contains a selection of excerpts from BNC-Baby files that have been annotated for metaphor. There are four registers, each comprising about 50 000 words: academic texts, news texts, fiction, and conversations.
Words have been separately labelled as participating in multi-word expressions (about 1.5%) or as discarded for metaphor analysis (0.02%). Main categories include words that are related to metaphor (MRW), words that signal metaphor (MFlag), and words that are not related to metaphor. For metaphor-related words, subdivisions have been made between clear cases of metaphor versus borderline cases (WIDLII, When In Doubt, Leave It In). Another parameter of metaphor-related words makes a distinction between direct metaphor, indirect metaphor, and implicit metaphor.

### Supported Tasks and Leaderboards

Metaphor detection, metaphor type classification.  

### Languages

English.

## Dataset Structure

### Data Instances

A sample instance from the dataset:
```
{
  'document_name': 'kcv-fragment42', 
  'words': ['', 'I', 'think', 'we', 'should', 'have', 'different', 'holidays', '.'],
  'pos_tags': ['N/A', 'PNP', 'VVB', 'PNP', 'VM0', 'VHI', 'AJ0', 'NN2', 'PUN'],
  'met_type': [
    {'type': 'mrw/met', 'word_indices': [5]}
  ], 
  'meta': ['vocal/laugh', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']
}
```

### Data Fields

The instances are ordered as they appear in the corpus.

- `document_name`: a string containing the name of the document in which the sentence appears;  
- `words`: words in the sentence (`""` when the word represents metadata);  
- `pos_tags`: POS tags of the words, encoded using the BNC basic tagset (`"N/A"` when the word does not have an associated POS tag);   
- `met_type`: metaphors in the sentence, marked by their type and word indices;  
- `meta`: selected metadata tags providing additional context to the sentence. Metadata may not correspond to a specific word. In this case, the metadata is represented with an empty string (`""`) in `words` and a `"N/A"` tag in `pos_tags`.   

## Dataset Creation

For detailed information on the corpus, please check out the references in the `Citation Information` section or contact the dataset authors.

## Simplifications
The raw corpus is equipped with rich metadata and encoded in the TEI XML format. The textual part is fully parsed except for the lemmas, i.e. all the sentences in the raw corpus are present in the dataset.  
However, parsing the metadata fully is unnecessarily tedious, so certain simplifications were made:  
- paragraph information is not preserved as the dataset is parsed at sentence level;  
- manual corrections (`<corr>`) of incorrectly written words are ignored, and the original, incorrect form of the words is used instead;  
- `<ptr>` and `<anchor>` tags are ignored as I cannot figure out what they represent;  
- the attributes `rendition` (in `<hi>` tags) and `new` (in `<shift>` tags) are not exposed.  

## Discarding metadata

The dataset contains rich metadata, which is stored in the `meta` attribute. To keep data aligned, empty words or `"N/A"`s are inserted into the other attributes. If you want to ignore the metadata and correct the metaphor type annotations, you can use code similar to the following snippet:  
```python3
data = datasets.load_dataset("matejklemen/vuamc")["train"]
data = data.to_pandas()

for idx_ex in range(data.shape[0]):
	curr_ex = data.iloc[idx_ex]

	idx_remap = {}
	for idx_word, word in enumerate(curr_ex["words"]):
		if len(word) != 0:
			idx_remap[idx_word] = len(idx_remap)
	
	# Note that lists are stored as np arrays by datasets, while we are storing new data in a list!
	# (unhandled for simplicity)
	words, pos_tags, met_type = curr_ex[["words", "pos_tags", "met_type"]].tolist()
	if len(idx_remap) != len(curr_ex["words"]):
		words = list(filter(lambda _word: len(_word) > 0, curr_ex["words"]))
		pos_tags = list(filter(lambda _pos: _pos != "N/A", curr_ex["pos_tags"]))
		met_type = []

		for met_info in curr_ex["met_type"]:
			met_type.append({
				"type": met_info["type"],
				"word_indices": list(map(lambda _i: idx_remap[_i], met_info["word_indices"]))
			})
``` 

## Additional Information

### Dataset Curators

Gerard Steen; et al. (please see http://hdl.handle.net/20.500.12024/2541 for the full list).  

### Licensing Information

Available for non-commercial use on condition that the terms of the [BNC Licence](http://www.natcorp.ox.ac.uk/docs/licence.html) are observed and that this header is included in its entirety with any copy distributed.

### Citation Information

```
@book{steen2010method,
  title={A method for linguistic metaphor identification: From MIP to MIPVU},
  author={Steen, Gerard and Dorst, Lettie and Herrmann, J. and Kaal, Anna and Krennmayr, Tina and Pasma, Trijntje},
  volume={14},
  year={2010},
  publisher={John Benjamins Publishing}
}
```

```
@inproceedings{leong-etal-2020-report,
    title = "A Report on the 2020 {VUA} and {TOEFL} Metaphor Detection Shared Task",
    author = "Leong, Chee Wee (Ben)  and
      Beigman Klebanov, Beata  and
      Hamill, Chris  and
      Stemle, Egon  and
      Ubale, Rutuja  and
      Chen, Xianyang",
    booktitle = "Proceedings of the Second Workshop on Figurative Language Processing",
    year = "2020",
    url = "https://aclanthology.org/2020.figlang-1.3",
    doi = "10.18653/v1/2020.figlang-1.3",
    pages = "18--29"
}
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.
