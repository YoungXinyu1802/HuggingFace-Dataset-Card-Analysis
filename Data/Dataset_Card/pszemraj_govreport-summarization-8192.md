---
task_categories:
- summarization
language:
- en
pretty_name: GovReport Summarization - 8192 tokens
size_categories:
- 1K<n<10K
source_datasets: ccdv/govreport-summarization
---

# GovReport Summarization - 8192 tokens

- `ccdv/govreport-summarization` with the changes of:
  - total tokens for each column computed and added in new columns according to the `long-t5` tokenizer
  - data cleaned with `clean-text`

---

## train info

```python
RangeIndex: 8200 entries, 0 to 8199
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype 
---  ------             --------------  ----- 
 0   report             8200 non-null   string
 1   summary            8200 non-null   string
 2   input_token_len    8200 non-null   Int64 
 3   summary_token_len  8200 non-null   Int64 
dtypes: Int64(2), string(2)
memory usage: 272.4 KB
```

## token length distribution (long-t5)

![tokens](https://i.imgur.com/RS4fQLw.png)

---