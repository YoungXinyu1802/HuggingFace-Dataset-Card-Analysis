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
The dataset contains user reviews about restaurants.
In total it contains 47,139 reviews. A review tagged with the <em>general</em> sentiment and sentiments on 3 aspects: <em>food, interior, service</em>.
### Data Fields
Each sample contains the following fields:
- **review_id**;
- **general**;
- **food**;
- **interior**;
- **service**;
- **text** review text.
### Python
```python3
import pandas as pd
df = pd.read_json('restaurants_reviews.jsonl', lines=True)
df.sample(5)
```