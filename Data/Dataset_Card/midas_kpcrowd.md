## Dataset Summary

A dataset for benchmarking keyphrase extraction and generation techniques from english news articles. For more details about the dataset please refer the original paper - [https://arxiv.org/abs/1306.4886](https://arxiv.org/abs/1306.4886)

Original source of the data - []()


## Dataset Structure
### Dataset Statistics

Table 1: Statistics on the length of the extractive keyphrases for Train, Test splits of kpcrowd dataset.

|             |  Train |  Test  |
|:-----------:|:------:|:------:|
| Single word | 81.62% | 80.27% |
|  Two words  | 14.41% | 15.44% |
| Three words |  2.79% |  3.36% |
|  Four words |  0.78% |  0.56% |
|  Five words |  0.20% |  0.25% |
|  Six words  |  0.12% |  0.05% |
| Seven words |   0%   |  0.05% |
| Eight words |  0.01% |   0%   |

Table 2: Statistics on the length of the abstractive keyphrases for Train, Test splits of kpcrowd dataset.

|             |   Train  |   Test   |
|:-----------:|:--------:|:--------:|
|  Zero words |   0.24%  |    0%    |
| Single word | 22.38  % | 21.81%   |
|  Two words  |  45.14%  |  43.03%  |
| Three words |  18.35%  |  19.69%  |
|  Four words |   7.71%  |   7.28%  |
|  Five words |   3.09%  |   3.94%  |
|  Six words  |   1.51%  |   3.33%  |
| Seven words |   0.82%  |  0.61%%  |
| Eight words |   0.55%  |   0.30%  |
|  Nine words |   0.17%  |    0%    |

Table 3: General statistics of the kpcrowd dataset.

|                 Type of Analysis                 |     Train     |      Test     |
|:------------------------------------------------:|:-------------:|:-------------:|
|                  Annotator Type                  |    Authors    |    Authors    |
|                   Document Type                  | News Articles | News Articles |
|                 No. of Documents                 |      450      |       50      |
|           Avg. Document length (words)           |     511.89    |     465.3     |
|            Max Document length (words)           |      7006     |      1609     |
|  Max no. of abstractive keyphrases in a document |       66      |       30      |
|  Min no. of abstractive keyphrases in a document |       0       |       0       |
| Avg. no. of abstractive keyphrases per document |      6.45     |      6.6      |
|  Max no. of extractive keyphrases in a document  |      231      |       86      |
|  Min no. of extractive keyphrases in a document  |       5       |       9       |
|  Avg. no. of extractive keyphrases per document |     42.81     |     39.24     |

### Data Fields

- **id**: unique identifier of the document.
- **document**: Whitespace separated list of words in the document.
- **doc_bio_tags**: BIO tags for each word in the document. B stands for the beginning of a keyphrase and I stands for inside the keyphrase. O stands for outside the keyphrase and represents the word that isn't a part of the keyphrase at all.
- **extractive_keyphrases**: List of all the present keyphrases.
- **abstractive_keyphrase**: List of all the absent keyphrases.


### Data Splits

|Split| #datapoints  |
|--|--|
| Train | 450 |
| Test | 50 |


## Usage

### Full Dataset

```python
from datasets import load_dataset

# get entire dataset
dataset = load_dataset("midas/kpcrowd", "raw")

# sample from the train split
print("Sample from train dataset split")
test_sample = dataset["train"][0]
print("Fields in the sample: ", [key for key in test_sample.keys()])
print("Tokenized Document: ", test_sample["document"])
print("Document BIO Tags: ", test_sample["doc_bio_tags"])
print("Extractive/present Keyphrases: ", test_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", test_sample["abstractive_keyphrases"])
print("\n-----------\n")

# sample from the test split
print("Sample from test dataset split")
test_sample = dataset["test"][0]
print("Fields in the sample: ", [key for key in test_sample.keys()])
print("Tokenized Document: ", test_sample["document"])
print("Document BIO Tags: ", test_sample["doc_bio_tags"])
print("Extractive/present Keyphrases: ", test_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", test_sample["abstractive_keyphrases"])
print("\n-----------\n")
```
**Output**

```bash
Sample from training data split
Fields in the sample:  ['id', 'document', 'doc_bio_tags', 'extractive_keyphrases', 'abstractive_keyphrases', 'other_metadata']
Tokenized Document:  ['James', 'Cameron', 'and', 'the', 'Future', 'of', 'Cinema', 'This', 'past', 'week', 'at', 'Cinemacon', ',', 'which', 'is', 'known', 'as', 'the', "''", '``', 'official', 'convention', 'of', 'the', 'National', 'Organization', 'of', 'Theatre', 'Owners', "''", "''", 'or', 'NATO', '-LRB-', 'really', '?', '-RRB-', ',', 'industry', 'professionals', 'of', 'all', 'sorts', 'gathered', 'at', 'Caesar', "'s", 'Palace', 'in', 'Las', 'Vegas', '.', 'The', 'convention', ',', 'previously', 'known', 'as', 'ShoWest', 'is', "''", '``', 'the', 'largest', 'cinema', 'trade', 'show', 'in', 'the', 'world', "''", "''", '-LRB-', 'www.cinemacon.com', '-RRB-', 'It', 'was', 'at', 'this', 'convention', 'that', 'filmmaker', 'James', 'Cameron', '-LRB-', 'Titanic', ',', 'Avatar', '-RRB-', 'delivered', 'a', 'presentation', 'entitled', "''", '``', 'A', 'Demonstration', 'and', 'Exclusive', 'Look', 'at', 'the', 'Future', 'of', 'Cinema', '.', "''", "''", 'The', 'last', 'time', 'Cameron', 'spoke', 'at', 'ShoWest', ',', 'he', 'and', 'George', 'Lucas', 'had', 'presented', 'a', 'plea', 'to', 'the', 'movie', 'industry', 'to', 'begin', 'its', 'huge', 'investment', 'in', 'digital', 'filmmaking', 'technology', 'in', 'preparation', 'of', 'the', '3D', 'revolution', 'that', 'was', 'bound', 'to', 'take', 'over', 'cinema', '.', 'One', 'year', 'removed', 'from', 'the', 'release', 'of', 'Cameron', "'s", 'technologically', 'groundbreaking', 'and', 'box', 'office', 'titan', 'Avatar', ',', 'the', 'film', 'industry', 'seems', 'to', 'have', 'done', 'exactly', 'what', 'Cameron', 'and', 'Lucas', 'predicted', '.', 'With', 'the', 'addition', 'of', 'digital', 'projection', 'systems', 'to', 'nearly', 'every', 'major', 'cineplex', 'or', 'theater', 'around', 'the', 'nation', 'and', 'of', 'course', 'the', 'overwhelming', 'use', 'of', '3D', ',', 'one', 'can', 'not', 'help', 'but', 'trust', 'that', 'Cameron', 'knows', 'what', 'he', 'is', 'talking', 'about.When', 'he', 'spoke', 'this', 'year', 'at', 'Cinemacon', ',', 'he', ',', 'once', 'again', ',', 'spoke', 'of', 'a', 'revolution', '.', 'Instead', 'of', 'promoting', '3D', 'cinema', ',', 'this', 'time', 'around', 'Cameron', 'talked', 'framerates', '.', 'Framerates', ',', 'for', 'those', 'not', 'fluent', 'in', 'film', 'jargon', ',', 'is', 'the', 'term', 'used', 'to', 'describe', 'the', 'speed', 'at', 'which', 'a', 'camera', 'shoots', 'and', 'subsequently', 'plays', 'back', 'individual', 'frames', 'on', 'a', 'film', 'strip', '.', 'The', 'industry', 'standard', 'has', 'been', '24', 'frames', 'per', 'second', '-LRB-', 'fps', '-RRB-', 'since', 'around', 'the', 'mid-20', "''", '``', 's', ',', 'as', 'it', 'is', 'believed', 'to', 'be', 'the', 'closest', 'to', 'mimicking', 'reality', '.', 'However', ',', 'filmmakers', 'have', 'always', 'experimented', 'with', 'framerates', 'whether', 'it', 'be', 'shooting', 'at', 'slower', 'frame', 'rates', 'to', 'produce', 'a', 'sensation', 'of', 'fast', 'motion', '-LRB-', 'think', ':', 'the', 'this', 'scene', 'in', 'Stanley', 'Kubrick', "'s", 'A', 'Clockwork', 'Orange', '-RRB-', 'or', 'shooting', 'at', 'faster', 'framerates', 'like', '48', 'fps', 'to', 'produce', 'what', 'is', 'known', 'as', 'slow', 'motion', '-LRB-', 'think', ':', 'sports', 'instant', 'replays', ',', 'or', 'this', 'funny', 'video', '.', "''", "''", 'Advertisement', 'Cameron', 'wants', 'the', 'industry', 'standard', 'to', 'change', '.', 'He', 'believes', 'that', 'by', 'making', 'the', 'industry', 'standard', 'something', 'like', '48', 'fps', ',', 'not', 'only', 'does', 'the', 'clarity', 'of', 'the', 'image', 'go', 'from', "''", '``', 'Good', "''", "''", 'to', "''", '``', 'Holy', 'S%@#!,', "''", "''", 'he', 'believes', 'it', 'will', 'improve', 'and', 'smooth', 'out', 'any', 'movement', 'that', 'the', 'camera', 'utilizes', '.', 'With', 'handheld', 'footage', 'practically', 'being', 'an', 'independent', 'film', 'standard', ',', 'it', 'will', 'help', 'translate', 'to', 'a', 'smoother', ',', 'more', 'pleasurable', 'film', 'experience', '.', 'His', 'argument', 'is', 'an', 'interesting', 'one', 'and', 'one', 'that', 'is', 'technically', 'relevant', 'and', 'affordable', 'for', 'all', 'kinds', 'of', 'filmmakers', '.', 'With', 'the', 'almost', 'overwhelming', 'transition', 'from', 'film', 'to', 'digital', ',', 'the', 'cost', 'of', 'shooting', 'at', 'higher', 'framerates', 'is', 'almost', 'null', 'and', 'void', '.', 'Most', 'of', 'the', 'newest', 'digital', 'video', 'cameras', 'like', 'Canon', "'s", '5D', 'and', '7D', 'already', 'shoot', 'at', 'a', 'standard', 'close', 'to', '30', 'fps', '.', 'So', ',', 'shooting', 'digitally', ',', 'one', 'does', "n't", 'have', 'to', 'empty', 'their', 'wallet', 'too', 'much', 'to', 'afford', 'to', 'shoot', 'at', 'higher', 'framerates', '.', 'That', 'being', 'said', ',', 'Cameron', "'s", 'proposal', 'presents', 'an', 'interesting', 'direction', 'for', 'the', 'future', 'of', 'cinema', '.', 'Many', 'filmmakers', 'like', 'Peter', 'Jackson', 'and', 'of', 'course', 'James', 'Cameron', 'have', 'already', 'experimented', 'with', 'increased', 'framerates', ',', 'and', 'their', 'arument', 'is', 'surely', 'a', 'compelling', 'one', ',', 'one', 'the', 'industry', 'will', 'have', 'to', 'keep', 'an', 'eye', 'on', '.']
Document BIO Tags:  ['B', 'I', 'O', 'O', 'B', 'I', 'I', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'B', 'I', 'O', 'O', 'B', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'B', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'B', 'I', 'O', 'B', 'O', 'B', 'O', 'B', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'B', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'B', 'O', 'B', 'O', 'B', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'B', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'B', 'O', 'O', 'B', 'O', 'B', 'I', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'B', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'B', 'O', 'B', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'B', 'O', 'O', 'B', 'O', 'B', 'O', 'O', 'B', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'B', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'B', 'O', 'B', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'B', 'B', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'B', 'O', 'O', 'B', 'O', 'O', 'O', 'B', 'I', 'I', 'O', 'O', 'B', 'O', 'B', 'I', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O']
Extractive/present Keyphrases:  ['technically relevant', 'framerates', 'interesting', 'las vegas', 'shooting', '7d', 'cinemacon', 'exclusive look', 'nato', 'clockwork', 'future of cinema', 'showest', 'george lucas', 'cinema', 'newest digital video cameras', 'peter jackson', 'holy s', 'advertisement', '30 fps', '48 fps', 'wwwcinemaconcom', 'national organization of theatre owners', 'james cameron', 'filmmakers', 'higher', 'movement', 'digital', 'jargon', 'independent', 'afford', 'keep', 'arument', 'wallet', 'subsequently', 'closest', 'motion', 'nation', 'sensation', 'pleasurable', 'experience', 'fluent', 'camera', 'cameron', 'clarity', 'revolution', 'industry standard', 'industry', 'preparation', 'scene', 'smoother', 'demonstration', 'huge investment', 'proposal', 'translate', 'produce', 'technology', 'footage', 'technologically', 'argument', 'affordable', 'box office', 'improve', 'standard']
Abstractive/absent Keyphrases:  ['increased framerates', "canon's 5d", "stanley kubrick's", 'future', 'titanic avatar', "caesar's palace", 'mid20s', "cameron's", 'exclusive', 'theatre owners', 'largest cinema', 'faster framerates', 'interesting direction', 'like peter jackson', 'newest', 'fast motion', 'official convention of the national organization', 'relevant', 'digital projection', 'movie industry']

-----------

Sample from test data split
Fields in the sample:  ['id', 'document', 'doc_bio_tags', 'extractive_keyphrases', 'abstractive_keyphrases', 'other_metadata']
Tokenized Document:  ['&', 'lsquo', ';', 'Miral', '&', 'rsquo', ';', ':', 'Director', 'has', 'conflict', 'of', 'interest', '``', 'Miral', "''", 'Rated', 'PG', '-', '13', '.', 'At', 'Kendall', 'Square', 'Cinema', ':', 'C', '+', 'Painter-turned-director', 'Julian', 'Schnabel', '-LRB-', 'Oscar-nominated', 'for', 'his', 'exquisite', '``', 'The', 'Diving', 'Bell', 'and', 'the', 'Butterfly', "''", '-RRB-', 'has', 'built', 'a', 'terrific', 'second', 'career', 'from', 'filmed', 'biographies', '-LRB-', 'also', 'in-cluding', '``', 'Before', 'Night', 'Falls', "''", 'and', '``', 'Basquiat', "''", '-RRB-', 'that', 'deal', 'with', 'people', 'confined', 'by', 'circumstance', 'yearning', 'to', 'break', 'free', '.', 'I', "'d", 'love', 'to', 'report', 'that', 'his', 'fourth', 'film', ',', '``', 'Miral', ',', "''", 'continues', 'the', 'upward', 'trend', ',', 'but', 'the', 'screenplay', 'by', 'Schnabel', "'s", 'girlfriend', ',', 'Palestinian', 'journalist', 'Rula', 'Jebreal', '-LRB-', 'based', 'on', 'her', 'semiautobiographical', 'novel', '-RRB-', ',', 'contains', 'too', 'many', 'earnest', 'platitudes', 'in', 'its', 'one-sided', 'look', 'at', 'four', 'women', "'s", 'intertwining', 'lives', 'during', 'the', 'first', 'intifada', 'of', 'the', '1980s', '.', '-LRB-', 'Some', 'musical', 'choices', ',', 'such', 'as', 'Tom', 'Waits', "'", '``', 'All', 'the', 'World', 'Is', 'Green', "''", 'playing', 'over', 'a', 'climactic', 'funeral', ',', 'also', 'stand', 'out', 'in', 'a', 'bad', 'way', '.', '-RRB-', 'Miral', '-LRB-', 'Freida', 'Pinto', ',', '``', 'Slumdog', 'Millionaire', "''", '-RRB-', ',', 'the', 'young', 'Arab', 'woman', 'growing', 'up', 'in', 'Jerusalem', 'during', 'this', 'period', ',', 'does', "n't", 'enter', 'the', 'picture', 'immediately', ',', 'and', 'when', 'she', 'does', ',', 'she', 'does', "n't", 'have', 'much', 'to', 'say', '--', 'at', 'first', '.', '-LRB-', 'A', 'bit', 'of', 'a', 'good', 'thing', ',', 'because', 'Pinto', "'s", 'Indian-accented', 'English', 'does', "n't", 'quite', 'jibe', 'with', 'the', 'Arabic-tinged', 'tongues', 'of', 'her', 'co-stars', '.', '-RRB-', 'Beginning', 'in', 'war-torn', 'Jerusalem', 'circa', '1948', ',', 'when', '``', 'Mama', "''", 'Hind', 'Husseini', '-LRB-', 'Hiam', 'Abbass', ',', '``', 'The', 'Visitor', "''", '-RRB-', 'established', 'an', 'orphanage', 'for', 'refugees', 'that', 'quickly', 'becomes', 'home', 'to', '2,000', ',', 'the', 'movie', 'spans', 'the', 'next', '50', 'years', ',', 'and', 'though', 'Schnabel', "'s", 'artist', "'s", 'eye', 'is', 'on', 'display', ',', 'the', 'Israel', '/', 'Palestine', 'conflict', 'is', 'a', 'subject', 'that', 'he', 'never', 'brings', 'into', 'clear', 'focus', '--', 'at', 'least', 'with', 'regard', 'to', 'Israelis', '.', 'And', 'when', 'he', 'presents', 'what', 'some', 'would', 'believe', 'terrorist', 'actions', 'of', 'his', 'protagonists', ',', 'he', 'sidesteps', 'the', 'potentially', 'horrible', 'consequences', ':', 'a', 'disgraced', 'former', 'nurse', '--', 'a', 'lifesaver', '--', 'plants', 'a', 'bomb', 'in', 'a', 'crowded', 'movie', 'theater', '-LRB-', 'playing', ',', 'without', 'a', 'hint', 'of', 'subtlety', ',', 'Roman', 'Polanski', "'s", '``', 'Repulsion', "''", '-RRB-', 'but', 'the', 'device', 'fails', 'to', 'explode', ';', 'a', 'car', 'bomb', 'is', 'set', 'off', 'by', 'Miral', "'s", 'political', 'activist', 'boyfriend', '--', 'though', 'there', 'are', 'seemingly', 'no', 'casualties', '.', 'So', 'much', 'for', 'the', 'horrors', 'of', 'war', '.', '-LRB-', '``', 'Miral', "''", 'contains', 'anger-inducing', 'violent', 'themes', ',', 'particularly', 'for', 'those', 'sympathetic', 'to', 'Israel', '.', '-RRB-']
Document BIO Tags:  ['O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'B', 'O', 'B', 'I', 'I', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
Extractive/present Keyphrases:  ['conflict of interest', 'arabictinged tongues', 'slumdog millionaire', 'kendall square cinema', 'before night falls', 'earnest platitudes', 'basquiat', 'biographies', 'jerusalem circa', 'butterfly', 'musical choices', 'terrific second', 'tom waits', 'miral', 'director', 'conflict']
Abstractive/absent Keyphrases:  ['lsquomiralrsquo director', 'mama hind husseini', 'miral rated pg 13', 'painterturneddirector julian schnabel oscarnominated', 'schnabels girlfriend palestinian journalist rula jebreal', 'exquisite the diving bell', 'interest']

-----------
```

### Keyphrase Extraction
```python
from datasets import load_dataset

# get the dataset only for keyphrase extraction
dataset = load_dataset("midas/kpcrowd", "extraction")

print("Samples for Keyphrase Extraction")

# sample from the train split
print("Sample from train data split")
test_sample = dataset["train"][0]
print("Fields in the sample: ", [key for key in test_sample.keys()])
print("Tokenized Document: ", test_sample["document"])
print("Document BIO Tags: ", test_sample["doc_bio_tags"])
print("\n-----------\n")

# sample from the test split
print("Sample from test data split")
test_sample = dataset["test"][0]
print("Fields in the sample: ", [key for key in test_sample.keys()])
print("Tokenized Document: ", test_sample["document"])
print("Document BIO Tags: ", test_sample["doc_bio_tags"])
print("\n-----------\n")
```

### Keyphrase Generation
```python
# get the dataset only for keyphrase generation
dataset = load_dataset("midas/kpcrowd", "generation")

print("Samples for Keyphrase Generation")

# sample from the train split
print("Sample from train data split")
test_sample = dataset["train"][0]
print("Fields in the sample: ", [key for key in test_sample.keys()])
print("Tokenized Document: ", test_sample["document"])
print("Extractive/present Keyphrases: ", test_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", test_sample["abstractive_keyphrases"])
print("\n-----------\n")

# sample from the test split
print("Sample from test data split")
test_sample = dataset["test"][0]
print("Fields in the sample: ", [key for key in test_sample.keys()])
print("Tokenized Document: ", test_sample["document"])
print("Extractive/present Keyphrases: ", test_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", test_sample["abstractive_keyphrases"])
print("\n-----------\n")
```

## Citation Information
```
@misc{marujo2013supervised,
      title={Supervised Topical Key Phrase Extraction of News Stories using Crowdsourcing, Light Filtering and Co-reference Normalization}, 
      author={Luis Marujo and Anatole Gershman and Jaime Carbonell and Robert Frederking and João P. Neto},
      year={2013},
      eprint={1306.4886},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Contributions
Thanks to [@debanjanbhucs](https://github.com/debanjanbhucs), [@dibyaaaaax](https://github.com/dibyaaaaax) and [@ad6398](https://github.com/ad6398) for adding this dataset
