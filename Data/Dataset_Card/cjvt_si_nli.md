---
annotations_creators:
- expert-generated
language:
- sl
language_creators:
- found
- expert-generated
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
pretty_name: Slovene natural language inference dataset
size_categories:
- 1K<n<10K
source_datasets: []
tags: []
task_categories:
- text-classification
task_ids:
- multi-class-classification
- natural-language-inference
---

# Dataset Card for SI-NLI

### Dataset Summary

SI-NLI (Slovene Natural Language Inference Dataset) contains 5,937 human-created Slovene sentence pairs (premise and hypothesis) that are manually labeled with the labels "entailment", "contradiction", and "neutral". We created the dataset using sentences that appear in the Slovenian reference corpus [ccKres](http://hdl.handle.net/11356/1034). Annotators were tasked to modify the hypothesis in a candidate pair in a way that reflects one of the labels. The dataset is balanced since the annotators created three modifications (entailment, contradiction, neutral) for each candidate sentence pair. The dataset is split into train, validation, and test sets, with sizes of 4,392, 547, and 998.  

Only the hypothesis and premise are given in the test set (i.e. no annotations) since SI-NLI is integrated into the Slovene evaluation framework [SloBENCH](https://slobench.cjvt.si/). If you use the dataset to train your models, please consider submitting the test set predictions to SloBENCH to get the evaluation score and see how it compares to others.  

If you have access to the private test set (with labels), you can load it instead of the public one by setting the environment variable `SI_NLI_TEST_PATH` to the file path.  

### Supported Tasks and Leaderboards

Natural language inference.  

### Languages

Slovenian.  

## Dataset Structure

### Data Instances

A sample instance from the dataset:
```
{
  'pair_id': 'P0', 
  'premise': 'Vendar se je anglikanska večina v grofijah na severu otoka (Ulster) na plebiscitu odločila, da ostane v okviru Velike Britanije.', 
  'hypothesis': 'A na glasovanju o priključitvi ozemlja k Severni Irski so se prebivalci ulsterskih grofij, pretežno anglikanske veroizpovedi, izrekli o obstanku pod okriljem VB.', 
  'annotation1': 'entailment', 
  'annotator1_id': 'annotator_C', 
  'annotation2': 'entailment', 
  'annotator2_id': 'annotator_A', 
  'annotation3': '', 
  'annotator3_id': '', 
  'annotation_final': 'entailment', 
  'label': 'entailment'
}
```

### Data Fields

- `pair_id`: string identifier of the pair (`""` in the test set),  
- `premise`: premise sentence,  
- `hypothesis`: hypothesis sentence,  
- `annotation1`: the first annotation (`""` if not available), 
- `annotator1_id`: anonymized identifier of the first annotator (`""` if not available), 
- `annotation2`: the second annotation (`""` if not available),   
- `annotator2_id`: anonymized identifier of the second annotator (`""` if not available),  
- `annotation3`: the third annotation (`""` if not available),  
- `annotator3_id`: anonymized identifier of the third annotator (`""` if not available), 
- `annotation_final`: aggregated annotation where it could be unanimously determined (`""` if not available or an unanimous agreement could not be reached),  
- `label`: aggregated annotation: either same as `annotation_final` (in case of agreement), same as `annotation1` (in case of disagreement), or `""` (in the test set). **Note that examples with disagreement are all put in the training set**. This aggregation is just the most simple possibility and the user may instead do something more advanced based on the individual annotations (e.g., learning with disagreement).   

\* A small number of examples did not go through the annotation process because they were constructed by the authors when writing the guidelines. The quality of these was therefore checked by the authors. Such examples do not have the individual annotations and the annotator IDs.  

## Additional Information

### Dataset Curators

Matej Klemen, Aleš Žagar, Jaka Čibej, Marko Robnik-Šikonja. 

### Licensing Information

CC BY-NC-SA 4.0.

### Citation Information

```
@misc{sinli,
    title = {Slovene Natural Language Inference Dataset {SI}-{NLI}},
    author = {Klemen, Matej and {\v Z}agar, Ale{\v s} and {\v C}ibej, Jaka and Robnik-{\v S}ikonja, Marko},
    url = {http://hdl.handle.net/11356/1707},
    note = {Slovenian language resource repository {CLARIN}.{SI}},
    year = {2022}
}
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.