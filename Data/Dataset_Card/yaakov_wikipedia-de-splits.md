---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
pretty_name: wikipedia-de-splits
paperswithcode_id: null
license:
- cc-by-sa-3.0
- gfdl
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
source_datasets:
- wikipedia
size_categories:
- n<1K
- 1K<n<10K
- 10K<n<100K
- 100K<n<1M
- 1M<n<10M
language:
- de
configs:
- "1"
- "2"
- "3"
- "4"
- "5"
- "6"
- "7"
- "8"
- "9"
- "10"
- "11"
- "12"
- "13"
- "14"
- "15"
- "16"
- "17"
- "18"
- "19"
- "20"
- "21"
- "all"
---
# Dataset Card for yaakov/wikipedia-de-splits

## Dataset Description
The only goal of this dataset is to have random German Wikipedia articles at
various dataset sizes:  Small datasets for fast development and large datasets for statistically relevant measurements.

For this purpose, I loaded the 2665357 articles in the `test` set of the pre-processed German Wikipedia dump from 2022-03-01, randomly permuted the articles and created splits of sizes `2**n`: `1, 2, 4, 8, ...`.  The split names are strings.  The split `'all'` contains all 2665357 available articles.

## Dataset creation
This dataset has been created with the following script:

    !apt install git-lfs
    !pip install -q transformers datasets
    
    from huggingface_hub import notebook_login
    notebook_login()
    
    from datasets import load_dataset
    wikipedia_de = load_dataset("wikipedia", "20220301.de")['train']
    
    shuffled = wikipedia_de.shuffle(seed=42)
    
    from datasets import DatasetDict
    res = DatasetDict()
    
    k, n = 0, 1
    while n <= shuffled.num_rows:
        res[str(k)] = shuffled.select(range(n))
        k += 1; n *= 2
    res['all'] = shuffled
    
    res.push_to_hub('yaakov/wikipedia-de-splits')