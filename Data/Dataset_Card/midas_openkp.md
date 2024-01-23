## Dataset Summary

Original source - [https://github.com/microsoft/OpenKP](https://github.com/microsoft/OpenKP)
## Dataset Structure


### Data Fields

- **id**: unique identifier of the document.
- **document**: Whitespace separated list of words in the document.
- **doc_bio_tags**: BIO tags for each word in the document. B stands for the beginning of a keyphrase and I stands for inside the keyphrase. O stands for outside the keyphrase and represents the word that isn't a part of the keyphrase at all.
- **extractive_keyphrases**: List of all the present keyphrases.
- **abstractive_keyphrase**: List of all the absent keyphrases.


### Data Splits

|Split| #datapoints  |
|--|--|
| Train | 134894 |
| Test | 6614 |
| Validation | 6616 |


## Usage

### Full Dataset

```python
from datasets import load_dataset

# get entire dataset
dataset = load_dataset("midas/openkp", "raw")

# sample from the train split
print("Sample from training data split")
train_sample = dataset["train"][0]
print("Fields in the sample: ", [key for key in train_sample.keys()])
print("Tokenized Document: ", train_sample["document"])
print("Document BIO Tags: ", train_sample["doc_bio_tags"])
print("Extractive/present Keyphrases: ", train_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", train_sample["abstractive_keyphrases"])
print("\n-----------\n")

# sample from the validation split
print("Sample from validation data split")
validation_sample = dataset["validation"][0]
print("Fields in the sample: ", [key for key in validation_sample.keys()])
print("Tokenized Document: ", validation_sample["document"])
print("Document BIO Tags: ", validation_sample["doc_bio_tags"])
print("Extractive/present Keyphrases: ", validation_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", validation_sample["abstractive_keyphrases"])
print("\n-----------\n")

# sample from the test split
print("Sample from test data split")
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
Tokenized Document:  ['Star', 'Trek', 'Discovery', 'Season', '1', 'Director', 'NA', 'Actors', 'Jason', 'Isaacs', 'Doug', 'Jones', 'Shazad', 'Latif', 'Sonequa', 'MartinGreen', 'Genres', 'SciFi', 'Country', 'USA', 'Release', 'Year', '2017', 'Duration', 'NA', 'Synopsis', 'Ten', 'years', 'before', 'Kirk', 'Spock', 'and', 'the', 'Enterprise', 'the', 'USS', 'Discovery', 'discovers', 'new', 'worlds', 'and', 'lifeforms', 'as', 'one', 'Starfleet', 'officer', 'learns', 'to', 'understand', 'all', 'things', 'alien', 'YOU', 'ARE', 'WATCHING', 'Star', 'Trek', 'Discovery', 'Season', '1', '000', '000', 'Loaded', 'Progress', 'The', 'video', 'keeps', 'buffering', 'Just', 'pause', 'it', 'for', '510', 'minutes', 'then', 'continue', 'playing', 'Share', 'Star', 'Trek', 'Discovery', 'Season', '1', 'movie', 'to', 'your', 'friends', 'Share', 'to', 'support', 'Putlocker', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', 'Version', '1', 'Server', 'Mega', 'Play', 'Movie', 'Version', '2', 'Server', 'TheVideo', 'Link', '1', 'Play', 'Movie', 'Version', '3', 'Server', 'TheVideo', 'Link', '2', 'Play', 'Movie', 'Version', '4', 'Server', 'TheVideo', 'Link', '3', 'Play', 'Movie', 'Version', '5', 'Server', 'TheVideo', 'Link', '4', 'Play', 'Movie', 'Version', '6', 'Server', 'NowVideo', 'Play', 'Movie', 'Version', '7', 'Server', 'NovaMov', 'Play', 'Movie', 'Version', '8', 'Server', 'VideoWeed', 'Play', 'Movie', 'Version', '9', 'Server', 'MovShare', 'Play', 'Movie', 'Version', '10', 'Server', 'CloudTime', 'Play', 'Movie', 'Version', '11', 'Server', 'VShare', 'Link', '1', 'Play', 'Movie', 'Version', '12', 'Server', 'VShare', 'Link', '2', 'Play', 'Movie', 'Version', '13', 'Server', 'VShare', 'Link', '3', 'Play', 'Movie', 'Version', '14', 'Server', 'VShare', 'Link', '4', 'Play', 'Movie', 'Version', '15', 'Other', 'Link', '1', 'Play', 'Movie', 'Version', '16', 'Other', 'Link', '2', 'Play', 'Movie', 'Version', '17', 'Other', 'Link', '3', 'Play', 'Movie', 'Version', '18', 'Other', 'Link', '4', 'Play', 'Movie', 'Version', '19', 'Other', 'Link', '5', 'Play', 'Movie', 'Version', '20', 'Other', 'Link', '6', 'Play', 'Movie', 'Version', '21', 'Other', 'Link', '7', 'Play', 'Movie', 'Version', '22', 'Other', 'Link', '8', 'Play', 'Movie', 'Version', '23', 'Other', 'Link', '9', 'Play', 'Movie', 'Version', '24', 'Other', 'Link', '10', 'Play', 'Movie', 'Version', '25', 'Other', 'Link', '11', 'Play', 'Movie', 'Version', '26', 'Other', 'Link', '12', 'Play', 'Movie', 'Version', '27', 'Other', 'Link', '13', 'Play', 'Movie', 'Version', '28', 'Other', 'Link', '14', 'Play', 'Movie', 'Version', '29', 'Other', 'Link', '15', 'Play', 'Movie']
Document BIO Tags:  ['B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
Extractive/present Keyphrases:  ['star trek', 'jason isaacs', 'doug jones']
Abstractive/absent Keyphrases:  []

-----------

Sample from validation data split
Fields in the sample:  ['id', 'document', 'doc_bio_tags', 'extractive_keyphrases', 'abstractive_keyphrases', 'other_metadata']
Tokenized Document:  ['Home', 'Keygen', 'NBA', '2K17', 'nba', '2k17', 'activation', 'key', 'generator', 'nba', '2k17', 'beta', 'keygen', 'free', 'nba', '2k17', 'cd', 'codes', 'free', 'nba', '2k17', 'cd', 'download', 'nba', '2k17', 'cd', 'generator', 'no', 'survey', 'nba', '2k17', 'cd', 'key', 'download', 'without', 'survey', 'NBA', '2K17', 'CD', 'Key', 'Generator', 'No', 'Survey', 'PC', 'PS34', 'Xbox', '360ONE', 'NBA', '2K17', 'CD', 'Key', 'Generator', 'No', 'Survey', 'PC', 'PS34', 'Xbox', '360ONE', 'Penulis', 'Hacker', 'Stock', 'on', 'Friday', '9', 'September', '2016', '1253', 'NBA', '2K17', 'CD', 'Key', 'Generator', 'No', 'Survey', 'PC', 'PS34', 'Xbox', '360ONE', 'Hello', 'everybody', 'welcome', 'on', 'our', 'web', 'site', 'HackerStockcom', 'these', 'days', 'weve', 'a', 'replacement', 'Key', 'Generator', 'for', 'you', 'that', 'is', 'known', 'as', 'NBA', '2K17', 'CD', 'Key', 'Generator', 'No', 'Survey', 'PC', 'PS34', 'Xbox', '360ONE', 'youll', 'be', 'ready', 'to', 'get', 'the', 'game', 'without', 'charge', 'this', 'keygen', 'will', 'find', 'unlimited', 'Activation', 'Codes', 'for', 'you', 'on', 'any', 'platform', 'Steam', 'or', 'Origin', 'on', 'computer', 'or', 'why', 'not', 'PlayStation', 'and', 'Xbox', 'Weve', 'ready', 'one', 'thing', 'special', 'for', 'all', 'NBA', 'fans', 'and', 'players', 'a', 'special', 'tool', 'that', 'were', 'certain', 'that', 'you', 'just', 'will', 'agree', 'Our', 'tool', 'may', 'generate', 'tons', 'of', 'key', 'codes', 'for', 'laptop', 'PlayStation', '3', 'PlayStation', '4', 'Xbox', '360', 'and', 'Xbox', 'ONE', 'So', 'youll', 'get', 'early', 'access', 'to', 'the', 'current', 'game', 'through', 'our', 'key', 'generator', 'for', 'NBA', '2K17', 'simply', 'with', 'few', 'clicks', 'This', 'tool', 'will', 'generate', 'over', '800', '000', 'key', 'codes', 'for', 'various', 'platforms', 'The', 'key', 'code', 'is', 'valid', 'and', 'youll', 'be', 'ready', 'to', 'try', 'it', 'and', 'be', 'able', 'to', 'play', 'NBA', '2K17', 'without', 'charge', 'Our', 'serial', 'key', 'generator', 'tool', 'is', 'NBA', '2K17', 'CD', 'Key', 'Generator', 'No', 'Survey', 'PC', 'PS34', 'Xbox', '360ONE', 'Instructions', 'using', 'the', 'NBA', '2K17', 'CD', 'Key', 'Generator', '2017', 'is', 'quick', 'and', 'easy', 'First', 'just', 'download', 'the', 'exe', 'file', 'and', 'install', 'it', 'on', 'your', 'computer', 'After', 'running', 'the', 'program', 'select', 'the', 'platform', 'on', 'which', 'you', 'want', 'to', 'play', 'NBA', '2K17', 'Next', 'click', 'the', 'GENERATE', 'button', 'This', 'will', 'produce', 'an', 'alphanumeric', 'code', 'also', 'known', 'as', 'your', 'product', 'key', 'You', 'will', 'use', 'it', 'to', 'validate', 'the', 'authenticity', 'of', 'your', 'NBA', '2K17', 'game', 'Now', 'copy', 'and', 'paste', 'the', 'product', 'key', 'onto', 'the', 'serial', 'number', 'window', 'prompt', 'of', 'your', 'NBA', '2K17', 'software', 'You', 'will', 'gain', 'access', 'to', 'NBA', '2K17', 'Finally', 'enjoy', 'your', 'game', 'We', 'designed', 'this', 'NBA', '2K17', 'game', 'key', 'generator', 'to', 'the', 'best', 'of', 'our', 'abilities', 'We', 'truly', 'hope', 'that', 'you', 'take', 'advantage', 'of', 'its', 'features', 'to', 'fully', 'enjoy', 'your', 'NBA', '2K17', 'Please', 'let', 'us', 'know', 'if', 'you', 'encounter', 'any', 'problems', 'with', 'our', 'software', 'We', 'would', 'love', 'to', 'help', 'you', 'out', 'NBA', '2K17', 'nba', '2k17', 'activation', 'key', 'generator', 'nba', '2k17', 'beta', 'keygen', 'free', 'nba', '2k17', 'cd', 'codes', 'free', 'nba', '2k17', 'cd', 'download', 'nba', '2k17', 'cd', 'generator', 'no', 'survey', 'nba', '2k17', 'cd', 'key', 'download', 'without', 'survey', 'nba', '2k17', 'cd', 'key', 'free', 'download', 'nba', '2k17', 'cd', 'key', 'free', 'online', 'nba', '2k17', 'cd', 'key', 'generator', 'no', 'survey', 'nba', '2k17', 'cd', 'key', 'pc', 'download', 'nba', '2k17', 'cd', 'key', 'ps4', 'free', 'download', 'nba', '2k17', 'cd', 'key', 'xbox', 'free', 'download', 'nba', '2k17', 'cd', 'keyexe', 'no', 'survey', 'nba', '2k17', 'crack', 'version', 'download', 'nba', '2k17', 'download', '2016', 'nba', '2k17', 'download', 'for', 'pc', '2016', 'nba', '2k17', 'download', 'full', 'crack', 'nba', 'Posted', 'by', 'Hacker', 'Stock', 'at', '1253', 'Email', 'This', 'BlogThis', 'Labels', 'Keygen', 'NBA', '2K17', 'nba', '2k17', 'activation', 'key', 'generator', 'nba', '2k17', 'beta', 'keygen', 'free', 'nba', '2k17', 'cd', 'codes', 'free', 'nba', '2k17', 'cd', 'download', 'nba', '2k17', 'cd', 'generator', 'no', 'survey', 'nba', '2k17', 'cd', 'key', 'download', 'without', 'survey', 'Older', 'Post', 'Home', 'Subscribe', 'to', 'Post', 'Comments', 'Atom']
Document BIO Tags:  ['O', 'O', 'B', 'I', 'B', 'I', 'O', 'B', 'I', 'B', 'I', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'O', 'B', 'I', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'B', 'I', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'B', 'I', 'O', 'B', 'I', 'B', 'I', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'B', 'I', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'B', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'B', 'I', 'O', 'B', 'I', 'B', 'I', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
Extractive/present Keyphrases:  ['nba 2k17', 'key generator', 'xbox']
Abstractive/absent Keyphrases:  []

-----------

Sample from test data split
Fields in the sample:  ['id', 'document', 'doc_bio_tags', 'extractive_keyphrases', 'abstractive_keyphrases', 'other_metadata']
Tokenized Document:  ['KSLI', '1280', 'AM', 'LATEST', 'POSTS', 'Scotty', 'McCreery', 'and', 'Wife', 'Welcome', 'New', 'Addition', 'to', 'the', 'Family', 'The', 'McCreerys', 'have', 'an', 'announcement', 'to', 'share', 'with', 'fansthe', 'family', 'is', 'getting', 'bigger', 'Wendy', 'Hermanson', '13', 'hours', 'ago', 'Kane', 'Brown', 'Serenades', 'Fans', 'With', 'Michael', 'Jackson', 'Hit', 'Watch', 'Brown', 'dusted', 'off', 'an', '80s', 'gem', 'to', 'post', 'on', 'social', 'media', 'and', 'put', 'smiles', 'on', 'the', 'faces', 'of', 'his', 'followers', 'Wendy', 'Hermanson', '20', 'hours', 'ago', 'Dolly', 'Parton', 'Scores', 'Golden', 'Globe', 'Nod', 'for', 'Girl', 'in', 'the', 'Movies', 'Congratulations', 'This', 'is', 'her', 'sixth', 'nomination', 'Sterling', 'Whitaker', '21', 'hours', 'ago', 'Remember', 'When', 'Johnny', 'Cash', 'Attacked', 'Homer', 'Simpson', 'It', 'was', 'one', 'of', 'the', 'coolest', 'guest', 'appearances', 'in', 'the', 'history', 'of', 'the', 'show', 'Sterling', 'Whitaker', '2', 'days', 'ago', 'Remember', 'Which', 'Country', 'Star', 'Murdered', 'His', 'Wife', 'The', 'career', 'of', 'one', 'of', 'country', 'musics', 'most', 'successful', 'early', 'stars', 'was', 'derailed', 'after', 'he', 'was', 'convicted', 'of', 'murdering', 'his', 'wife', 'Sterling', 'Whitaker', '2', 'days', 'ago', 'William', 'Shatner', 'to', 'Make', 'Grand', 'Ole', 'Opry', 'Debut', 'Hes', 'appearing', 'alongside', 'a', 'legendary', 'country', 'musician', 'Sterling', 'Whitaker', '2', 'days', 'ago', 'Remember', 'Who', 'First', 'Recorded', 'Garths', 'The', 'Thunder', 'Rolls', 'Have', 'you', 'ever', 'heard', 'the', 'extra', 'verse', 'Sterling', 'Whitaker', '2', 'days', 'ago', 'Danielle', 'Bradberys', 'Cover', 'of', 'Post', 'Malones', 'Psycho', 'Is', 'a', 'Stunner', 'Danielle', 'Bradbery', 'is', 'rounding', 'out', 'her', 'Yours', 'Truly', '2018', 'covers', 'project', 'by', 'sharing', 'her', 'take', 'on', 'rapper', 'Post', 'Malones', 'hit', 'Psycho', 'Angela', 'Stefano', '2', 'days', 'ago', 'Enjoy', 'Wild', 'Game', 'at', 'the', 'Texas', 'Wild', 'Bunch', 'Bonanza', 'Cook', 'Off', 'Its', 'time', 'for', 'the', 'Texas', 'Wild', 'Bunch', 'Bonanza', 'Cook', 'Off', 'and', 'Auction', 'All', 'attendees', 'get', 'to', 'sample', 'everything', 'from', 'deer', 'to', 'elk', 'to', 'bacon', 'wrapped', 'jalapeno', 'poppers', 'Rudy', 'Fernandez', '2', 'days', 'ago', 'Kid', 'Rocks', '20Foot', 'Butt', 'Bar', 'Sign', 'Gets', 'Approved', 'in', 'Nashville', 'The', 'crazy', 'sign', 'featuring', 'a', 'womans', 'rear', 'end', 'caused', 'a', 'swirl', 'of', 'discussion', 'Wendy', 'Hermanson', '2', 'days', 'ago', 'Remember', 'When', 'Dolly', 'Parton', 'Surprised', 'Reba', 'McEntire', 'on', 'the', 'Opry', 'Shes', 'made', 'so', 'many', 'special', 'memories', 'on', 'the', 'Opry', 'stage', 'Sterling', 'Whitaker', '3', 'days', 'ago', 'Chris', 'Young', 'Takes', 'on', 'the', 'Hag', 'With', 'Silver', 'Wings', 'Cover', 'Watch', 'In', 'his', 'new', 'single', 'Chris', 'Young', 'proudly', 'proclaims', 'that', 'he', 'was', 'raised', 'on', 'country', 'and', 'he', 'can', 'prove', 'it', 'Angela', 'Stefano', '3', 'days', 'ago', 'The', 'Tractors', 'Guitarist', 'Steve', 'Ripley', 'Dead', 'at', '69', 'Rest', 'in', 'peace', 'Steve', 'Carena', 'Liptak', '3', 'days', 'ago', 'Danielle', 'Bradbery', 'Rounds', 'Out', 'Yours', 'Truly', '2018', 'With', 'Psycho', 'The', 'final', 'third', 'of', 'Bradberys', 'Yours', 'Truly', '2018', 'tribute', 'project', 'is', 'here', 'Carena', 'Liptak', '3', 'days', 'ago', 'Load', 'More', 'Articles', 'Country', 'Music', 'News', 'Kane', 'Brown', 'Serenades', 'Fans', 'With', 'Michael', 'Jackson', 'Hit', 'Watch', 'Scotty', 'McCreery', 'and', 'Wife', 'Welcome', 'New', 'Addition', 'to', 'the', 'Family', 'Meet', 'the', 'Staff', 'Rudy', 'Fernandez', 'Shay', 'Hill', 'Chaz', 'Frank', 'Pain', 'Classic', 'Country', '1280', 'on', 'Facebook', 'Abilene', 'TX', 'January', '7', '2019', '70000', 'AM', 'PST', 'January', '7', '2019', '70000', 'AM', 'PST', 'January', '7', '2019', '70000', 'AM', 'PSTth', '62', 'Clear', '71', '42', 'view', 'forecast', 'VIP', 'Contests', 'New', 'Year', 'New', 'You', '100', 'Amazon', 'Gift', 'Card', 'Small', 'Business', 'Solutions', 'Devote', 'more', 'time', 'to', 'running', 'your', 'business', 'Engage', 'your', 'clients', 'across', 'multiple', 'platforms', 'Reach', 'more', 'customers', 'than', 'ever', 'before', 'Get', 'an', 'Edge', 'on', 'the', 'Competition', 'Today', 'KSLIs', 'Daily', 'Deal', 'Certificate', 'for', 'a', 'Rhythm', 'USA', 'Clock', 'From', 'Jewels', 'of', 'Time']
Document BIO Tags:  ['B', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
Extractive/present Keyphrases:  ['ksli 1280 am']
Abstractive/absent Keyphrases:  []

-----------

```

### Keyphrase Extraction
```python
from datasets import load_dataset

# get the dataset only for keyphrase extraction
dataset = load_dataset("midas/openkp", "extraction")

print("Samples for Keyphrase Extraction")

# sample from the train split
print("Sample from training data split")
train_sample = dataset["train"][0]
print("Fields in the sample: ", [key for key in train_sample.keys()])
print("Tokenized Document: ", train_sample["document"])
print("Document BIO Tags: ", train_sample["doc_bio_tags"])
print("\n-----------\n")

# sample from the validation split
print("Sample from validation data split")
validation_sample = dataset["validation"][0]
print("Fields in the sample: ", [key for key in validation_sample.keys()])
print("Tokenized Document: ", validation_sample["document"])
print("Document BIO Tags: ", validation_sample["doc_bio_tags"])
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
dataset = load_dataset("midas/openkp", "generation")

print("Samples for Keyphrase Generation")

# sample from the train split
print("Sample from training data split")
train_sample = dataset["train"][0]
print("Fields in the sample: ", [key for key in train_sample.keys()])
print("Tokenized Document: ", train_sample["document"])
print("Extractive/present Keyphrases: ", train_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", train_sample["abstractive_keyphrases"])
print("\n-----------\n")

# sample from the validation split
print("Sample from validation data split")
validation_sample = dataset["validation"][0]
print("Fields in the sample: ", [key for key in validation_sample.keys()])
print("Tokenized Document: ", validation_sample["document"])
print("Extractive/present Keyphrases: ", validation_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", validation_sample["abstractive_keyphrases"])
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
@inproceedings{Xiong2019OpenDW,

  title={Open Domain Web Keyphrase Extraction Beyond Language Modeling},

  author={Lee Xiong and Chuan Hu and Chenyan Xiong and Daniel Fernando Campos and Arnold Overwijk},

  booktitle={EMNLP},

  year={2019}

}
```

## Contributions
Thanks to [@debanjanbhucs](https://github.com/debanjanbhucs), [@dibyaaaaax](https://github.com/dibyaaaaax) and [@ad6398](https://github.com/ad6398) for adding this dataset
