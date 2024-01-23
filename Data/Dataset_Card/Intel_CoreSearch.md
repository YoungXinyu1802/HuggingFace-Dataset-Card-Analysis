# The CoreSearch Dataset
A large-scale dataset for cross-document event coreference **search**</br>

- **Paper:** Cross-document Event Coreference Search: Task, Dataset and Modeling (link-TBD)

### Languages

English

## Load Dataset
You can read/download the dataset files following Huggingface Hub instructions.</br>
For example, below code will load CoreSearch DPR folder:

```python
from huggingface_hub import hf_hub_url, cached_download
import json
REPO_ID = "datasets/Intel/CoreSearch"
DPR_FILES = "/dpr/"

dpr_files = ["dpr/Dev.json", "dpr/Train.json", "dpr/Test.json"]

dpr_jsons = list()
for _file in dpr_files:
    dpr_jsons.append(json.load(open(cached_download(
        hf_hub_url(REPO_ID, _file)), "r")))
```

### Data Splits
- **Final version of the CD event coreference search dataset**<br>
|                                                    | Train   | Valid | Test | Total |
| -----                                              | ------ | ----- | ----  | ----  |
| WEC-Eng Validated Data                             |        |       |       |       |
| &nbsp;&nbsp;&nbsp;&nbsp;# Clusters                 | 237    |  49   | 236   | 522   | 
| &nbsp;&nbsp;&nbsp;&nbsp;# Passages (with Mentions) | 1,503  |  341  | 1,266 | 3,110 |
| # Added Destructor Passages                        | 922,736  |  923,376  | 923,746   | 2,769,858 |
| # Total Passages                                   | 924,239 |  923,717 | 925,012 | 2,772,968 |

## Citation
```
@inproceedings{TBD}
```


## License
We provide the following data sets under a <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>. It is based on content extracted from Wikipedia that is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License

## Contact
If you have any questions please create a Github issue at <a href="https://github.com/AlonEirew/CoreSearch">https://github.com/AlonEirew/CoreSearch</a>.