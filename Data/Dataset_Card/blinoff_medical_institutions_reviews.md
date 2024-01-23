---
language:
- ru
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
task_categories:
- text-classification
task_ids:
- sentiment-classification
---
### Dataset Summary
The dataset contains user reviews about medical institutions.

In total it contains 12,036 reviews. A review tagged with the <em>general</em> sentiment and sentiments on 5 aspects: <em>quality, service, equipment, food, location</em>.
### Data Fields
Each sample contains the following fields:
- **review_id**;
- **content**: review text;
- **general**;
- **quality**;
- **service**;
- **equipment**;
- **food**;
- **location**.
### Python
```python3
import pandas as pd
df = pd.read_json('medical_institutions_reviews.jsonl', lines=True)
df.sample(5)
```
