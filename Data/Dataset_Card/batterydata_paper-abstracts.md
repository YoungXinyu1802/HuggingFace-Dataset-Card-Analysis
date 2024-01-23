---
language: 
- en
license: 
- apache-2.0
task_categories:
- text-classification
pretty_name: 'Battery Abstracts Dataset'
---

# Battery Abstracts Dataset
This dataset includes 29,472 battery papers and 17,191 non-battery papers, a total of 46,663 papers. These papers are manually labelled in terms of the journals to which they belong. 14 battery journals and 1,044 non battery journals were selected to form this database. 


- training_data.csv: Battery papers: 20,629, Non-battery papers: 12,034. Total: 32,663.
- val_data.csv: Battery papers: 5,895, Non-battery papers: 3,438. Total: 9,333.
- test_data.csv: Battery papers: 2,948, Non-battery papers: 1,719. Total: 4,667.

# Usage
```
from datasets import load_dataset

dataset = load_dataset("batterydata/paper-abstracts")
```
# Citation
```
@article{huang2022batterybert,
  title={BatteryBERT: A Pretrained Language Model for Battery Database Enhancement},
  author={Huang, Shu and Cole, Jacqueline M},
  journal={J. Chem. Inf. Model.},
  year={2022},
  doi={10.1021/acs.jcim.2c00035},
  url={DOI:10.1021/acs.jcim.2c00035},
  pages={DOI: 10.1021/acs.jcim.2c00035},
  publisher={ACS Publications}
}
```