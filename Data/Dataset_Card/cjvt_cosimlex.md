---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- en
- hr
- sl
- fi
license:
- gpl-3.0
multilinguality:
- multilingual
size_categories:
- n<1K
source_datasets: []
task_categories:
- other
task_ids: []
pretty_name: CoSimLex
tags:
- graded-word-similarity-in-context
---

# Dataset Card for CoSimLex

### Dataset Summary

The dataset contains human similarity ratings for pairs of words. The annotators were presented with contexts that contained both of the words in the pair and the dataset features two different contexts per pair. The words were sourced from the English, Croatian, Finnish and Slovenian versions of the original Simlex dataset.  
Statistics:  
- 340 English pairs (config `en`),
- 112 Croatian pairs (config `hr`),  
- 111 Slovenian pairs (config `sl`),
- 24 Finnish pairs (config `fi`).

### Supported Tasks and Leaderboards

Graded word similarity in context.  

### Languages

English, Croatian, Slovenian, Finnish.

## Dataset Structure

### Data Instances

A sample instance from the dataset:
```
{
  'word1': 'absence', 
  'word2': 'presence', 
  'context1': 'African slaves from Angola and Mozambique were also present, but in fewer numbers than in other Brazilian areas, because Paraná was a poor region that did not need much slave manpower. The immigration grew in the mid-19th century, mostly composed of Italian, German, Polish, Ukrainian, and Japanese peoples. While Poles and Ukrainians are present in Paraná, their <strong>presence</strong> in the rest of Brazil is almost <strong>absence</strong>.', 
  'context2': 'The Chinese had become almost impossible to deal with because of the turmoil associated with the cultural revolution. The North Vietnamese <strong>presence</strong> in Eastern Cambodia had grown so large that it was destabilizing Cambodia politically and economically. Further, when the Cambodian left went underground in the late 1960s, Sihanouk had to make concessions to the right in the <strong>absence</strong> of any force that he could play off against them.', 
  'sim1': 2.2699999809265137, 
  'sim2': 1.3700000047683716, 
  'stdev1': 2.890000104904175, 
  'stdev2': 1.7899999618530273, 
  'pvalue': 0.2409999966621399, 
  'word1_context1': 'absence', 
  'word2_context1': 'presence', 
  'word1_context2': 'absence', 
  'word2_context2': 'presence'
}
```

### Data Fields

- `word1`: a string representing the first word in the pair. Uninflected form.
- `word2`: a string representing the second word in the pair. Uninflected form.
- `context1`: a string representing the first context containing the pair of words. The target words are marked with a `<strong></strong>` labels.
- `context2`: a string representing the second context containing the pair of words. The target words are marked with a `<strong></strong>` labels.
- `sim1`: a float representing the mean of the similarity scores within the first context.
- `sim2`: a float representing the mean of the similarity scores within the second context.
- `stdev1`: a float representing the standard Deviation for the scores within the first context.
- `stdev2`: a float representing the standard deviation for the scores within the second context.
- `pvalue`: a float representing the p-value calculated using the Mann-Whitney U test.
- `word1_context1`: a string representing the inflected version of the first word as it appears in the first context.
- `word2_context1`: a string representing the inflected version of the second word as it appears in the first context.
- `word1_context2`: a string representing the inflected version of the first word as it appears in the second context.
- `word2_context2`: a string representing the inflected version of the second word as it appears in the second context.

## Additional Information

### Dataset Curators

Carlos Armendariz; et al. (please see http://hdl.handle.net/11356/1308 for the full list)

### Licensing Information

GNU GPL v3.0.

### Citation Information

```
@inproceedings{armendariz-etal-2020-semeval,
    title = "{SemEval-2020} {T}ask 3: Graded Word Similarity in Context ({GWSC})",
    author = "Armendariz, Carlos S.  and
      Purver, Matthew  and
      Pollak, Senja  and
      Ljube{\v{s}}i{\'{c}}, Nikola  and
      Ul{\v{c}}ar, Matej  and
      Robnik-{\v{S}}ikonja, Marko and
      Vuli{\'{c}}, Ivan and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 14th International Workshop on Semantic Evaluation",
    year = "2020",
    address="Online"
}
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.
