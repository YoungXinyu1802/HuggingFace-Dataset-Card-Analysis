---
language:
- en
size_categories:
- 1K<n<10K
task_categories:
- text-classification
---
# Green patents dataset

- num_rows: 9145
- features: [title, label]
- label: 0, 1

The dataset contains patent titles that are labeled as 1 (="green") and 0 (="not green").

"green" patents titles were gathered by searching for CPC class "Y02" with Google Patents (query: "status:APPLICATION type:PATENT (Y02) country:EP,US", 05/01/2023).

"not green" patents titles are derived from the [HUPD dataset](https://huggingface.co/datasets/HUPD/hupd) (random choice of 5000 titles). We could not find any patents in HUPD assigned to any CPC class starting with "Y".