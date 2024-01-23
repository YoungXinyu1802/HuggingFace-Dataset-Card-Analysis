---
language:
- en
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
task_categories:
- summarization
---
# MediaSum
## Description
This large-scale media interview dataset contains 463.6K transcripts with abstractive summaries, 
collected from interview transcripts and overview / topic descriptions from NPR and CNN.

### **NOTE: The authors have requested that this dataset be used for research purposes only**


## Homepage
https://github.com/zcgzcgzcg1/MediaSum
## Paper
https://arxiv.org/abs/2103.06410
## Authors
### Chenguang Zhu*, Yang Liu*, Jie Mei, Michael Zeng
#### Microsoft Cognitive Services Research Group
{chezhu,yaliu10,jimei,nzeng}@microsoft.com

## Citation

@article{zhu2021mediasum,  
  title={MediaSum: A Large-scale Media Interview Dataset for Dialogue Summarization},  
  author={Zhu, Chenguang and Liu, Yang and Mei, Jie and Zeng, Michael},  
  journal={arXiv preprint arXiv:2103.06410},  
  year={2021}  
}

## Dataset size
Train: 443,596  
Validation: 10,000  
Test: 10,000   

The splits were made by using the file located here: https://github.com/zcgzcgzcg1/MediaSum/tree/main/data

## Data details
- id (string): unique identifier
- program (string): the program this transcript came from
- date (string): date of program
- url (string): link to where audio and transcript are located
- title (string): title of the program. some datapoints do not have a title
- summary (string): summary of the program
- utt (list of string): list of utterances by the speakers in the program. corresponds with `speaker`
- speaker (list of string): list of speakers, corresponds with `utt`


Example:
```
{
  "id": "NPR-11",
  "program": "Day to Day",
  "date": "2008-06-10",
  "url": "https://www.npr.org/templates/story/story.php?storyId=91356794",
  "title": "Researchers Find Discriminating Plants",
  "summary": "The \"sea rocket\" shows preferential treatment to plants that are its kin. Evolutionary plant ecologist Susan Dudley of McMaster University in Ontario discusses her discovery.",
  "utt": [
    "This is Day to Day.  I'm Madeleine Brand.",
    "And I'm Alex Cohen.",
    "Coming up, the question of who wrote a famous religious poem turns into a very unchristian battle.",
    "First, remember the 1970s?  People talked to their houseplants, played them classical music. They were convinced plants were sensuous beings and there was that 1979 movie, \"The Secret Life of Plants.\"",
    "Only a few daring individuals, from the scientific establishment, have come forward with offers to replicate his experiments, or test his results. The great majority are content simply to condemn his efforts without taking the trouble to investigate their validity.",
    ...
    "OK. Thank you.",
    "That's Susan Dudley. She's an associate professor of biology at McMaster University in Hamilt on Ontario. She discovered that there is a social life of plants."
  ],
  "speaker": [
    "MADELEINE BRAND, host",
    "ALEX COHEN, host",
    "ALEX COHEN, host",
    "MADELEINE BRAND, host",
    "Unidentified Male",    
    ..."
    Professor SUSAN DUDLEY (Biology, McMaster University)",
    "MADELEINE BRAND, host"
  ]
}
  ```
## Using the dataset
```python
from datasets import load_dataset
ds = load_dataset("nbroad/mediasum")
```
## Data location
https://drive.google.com/file/d/1ZAKZM1cGhEw2A4_n4bGGMYyF8iPjLZni/view?usp=sharing

## License
No license specified, but the authors have requested that this dataset be used for research purposes only.