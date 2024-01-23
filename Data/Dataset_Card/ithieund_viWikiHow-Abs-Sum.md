# viWikiHow-Abs-Sum
A dataset for Vietnamese Abstractive Summarization task.
It includes all Vietnamese posts from WikiHow which was released in WikiLingua dataset.

# Introduction
This dataset was extracted from Train/Test split of WikiLingua dataset. As the target language is Vietnamese, we remove all other files, just keep train.\*.vi, test.\*.vi, and val.\*.vi for Vietnamese Abstractive Summarization task. The raw files then are stored in the *raw* director and after that, we run the python script to generate ready-to-use data files in TSV and JSONLINE formats which are stored in *processed* directory to be easily used for future training scripts.

# Directory structure
- raw: contains raw text files from WikiLingua
  - test.src.vi
  - test.tgt.vi
  - train.src.vi
  - train.tgt.vi
  - val.src.vi
  - val.tgt.vi
- processed: contains generated TSV and JSONLINE files
  - test.tsv
  - train.tsv
  - valid.tsv
  - test.jsonl
  - train.jsonl
  - valid.jsonl
  - [and other variants]

# Credits
- Special thanks to WikiLingua authors: https://github.com/esdurmus/Wikilingua
- Article provided by <a href="https://www.wikihow.com/Main-Page" target="_blank">wikiHow</a>, a wiki that is building the world's largest and highest quality how-to manual. Please edit this article and find author credits at the original wikiHow article on How to Tie a Tie. Content on wikiHow can be shared under a <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/" target="_blank">Creative Commons License</a>.
