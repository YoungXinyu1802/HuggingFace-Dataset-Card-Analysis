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
The dataset contains user reviews about medical facilities.

In total it contains 70,597 reviews. The detailed distribution on sentiment scale is:
- 41,419 positive reviews;
- 29,178 negative reviews.
### Data Fields
Each sample contains the following fields:
- **review_id**;
- **category** category of medical facility (one of 48);
- **title**: review title;
- **content**: review text;
- **sentiment**: sentiment (<em>positive</em> or <em>negative</em>);
- **source_url**.
### Python
```python3
import pandas as pd
df = pd.read_json('healthcare_facilities_reviews.jsonl', lines=True)
df.sample(5)
```
