The dataset script is more or less ready and one file has correctly been converted so far: `https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2015-48.tar.gz`

You can try downloading the file as follows:

```python
from datasets import load_dataset
ds = load_dataset("flax-community/german_common_crawl", "first")
```

This can be done on your local computer and should only take around 2GB of disk space.

This however only loads the first of >100 files.

We now need to add **all** other files to this repo. This can be done as follows:

1) Clone this repo (assuming `git lfs` is installed): `git clone https://huggingface.co/datasets/flax-community/german_common_crawl`

2) For each file:
`https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2016-18.tar.gz` - `https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0009_2019-47.tar.gz` 

run the command `./convert_file.sh <file_name>` This command will download the file via `wget`, filter out all text that is below a threshold as explained here: https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0009_2019-47.tar.gz and then converts the file into the correct format.

3) Upload the file to this repo:
`git add . && git commit -m "add file x" && git push

Ideally this can be done in a loop on a computer that has enough CPU memory (Note that if this is done on a TPU VM, make sure to disable the TPU via `export JAX_PLATFORM_NAME=cpu`.

Also some description and file names have to be added correctly to the dataset.py script