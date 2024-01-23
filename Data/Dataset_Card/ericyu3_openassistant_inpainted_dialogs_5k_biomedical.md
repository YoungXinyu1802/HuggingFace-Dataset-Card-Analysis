---
license: apache-2.0
size_categories:
- 1K<n<10K
---

This dataset was created by:

* Starting with the [Dialog Inpainting](https://github.com/google-research/dialog-inpainting) dataset
* Labeling the turns of each dialog with `User: ` and `Assistant: `
* Filtering using spaCy, using code similar to the following (written by https://huggingface.co/ontocord):

```
import pandas as pd
import spacy
try:
  if sci is  None: pass
except:
  sci = spacy.load("en_ner_craft_md")
  data = pd.read_parquet('data.parquet', engine='pyarrow')

for a in data['labeleddialog']:
  a = a.replace("this article", "this subject").replace("()", "").replace("  ", " ")
  if 'novel' in a or ' story' in a or 'movie' in a or 'film' in a or 'music' in a:
    #print ('###arts\n', a)
    continue
  if ' game' in a or 'sports' in a or 'football' in a or 'soccer' in a or 'baseball' in a or 'basketball' in a:
    #print ('###sports\n', a)
    continue
  if 'population' in a or 'territory' in a or 'village' in a or 'country' in a or 'county' in a:
    #print ('###place\n', a)
    continue
  if 'ingredient' in a or 'food' in a or 'recipe' in a:
    #print ('###recipe\n', a)
    continue
  if ' rights' in a or ' court ' in a or ' criminal ' in a or ' verdict ' in a or ' guilt ' in a or ' legislat' in a:
    #print ('###law\n', a)
    continue

  doc = sci(a)
  j = 0
  for ent in doc.ents:
    if ent.label == 'SO' or (ent.label == 'CHEBI' and len(ent.text) > 5):
      j+= 1
      if j > 3:
        print ('###biomed\n',a)
        break
      #print (ent.label, ent.text)
```

* Filtering using BERT, using the following code:

```
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
classifier(page_titles, ["Biomedical", "Non-biomedical"])
# Dialogs with page titles with `prob < 0.7` were dropped.
prob = classification_result["scores"][classification_result["labels"].index("Biomedical")]
```