A dataset for benchmarking keyphrase extraction and generation techniques from abstracts of English scientific papers. For more details about the dataset please refer the original paper - [https://dl.acm.org/doi/pdf/10.3115/1119355.1119383](https://dl.acm.org/doi/pdf/10.3115/1119355.1119383).

Data source - [https://github.com/boudinfl/ake-datasets/tree/master/datasets/Inspec](https://github.com/boudinfl/ake-datasets/tree/master/datasets/Inspec)

## Dataset Summary
The Inspec dataset was originally proposed by *Hulth* in the paper titled - [Improved automatic keyword extraction given more linguistic knowledge](https://aclanthology.org/W03-1028.pdf) in the year 2003. The dataset consists of abstracts of 2,000 English scientific papers from the [Inspec database](https://clarivate.com/webofsciencegroup/solutions/webofscience-inspec/). The abstracts are from papers belonging to the scientific domains of *Computers and Control* and *Information Technology* published between 1998 to 2002. Each abstract has two sets of keyphrases annotated by professional indexers - *controlled* and *uncontrolled*. The *controlled* keyphrases are obtained from the Inspec thesaurus and therefore are often not present in the abstract's text. Only 18.1% of the *controlled* keyphrases are actually present in the abstract's text. The *uncontrolled* keyphrases are those selected by the indexers after reading the full-length scientific articles and 76.2% of them are present in the abstract's text. There is no information in the original paper about how these 2,000 scientific papers were selected. It is unknown whether the papers were randomly selected out of all the papers published between 1998-2002 in the *Computers and Control* and *Information Technology* domains or were there only 2,000 papers in this domain that were indexed by Inspec. The train, dev and test splits of the data were arbitrarily chosen. 

One of the key aspect of this dataset which makes it unique is that it provides keyphrases assigned by professional indexers, which is uncommon in the keyphrase literature. Most of the datasets in this domain have author assigned keyphrases as the ground truth. The dataset shared over here does not explicitly presents the *controlled* and *uncontrolled* keyphrases instead it only categorizes the keyphrases into *extractive* and *abstractive*. **Extractive keyphrases** are those that could be found in the input text and the **abstractive keyphrases** are those that are not present in the input text. In order to get all the meta-data about the documents and keyphrases please refer to the [original source](https://github.com/boudinfl/ake-datasets/tree/master/datasets/Inspec) from which the dataset was taken from. The main motivation behind making this dataset available in the form as presented over here is to make it easy for the researchers to programmatically download it and evaluate their models for the tasks of keyphrase extraction and generation. As keyphrase extraction by treating it as a sequence tagging task and using contextual language models has become popular - [Keyphrase extraction from scholarly articles as sequence labeling using contextualized embeddings](https://arxiv.org/pdf/1910.08840.pdf), we have also made the token tags available in the BIO tagging format.  

## Dataset Structure

## Dataset Statistics 
Table 1: Statistics on the length of the abstractive keyphrases for Train, Test, and Validation splits of Inspec dataset.

|                 | Train | Test | Validation |
|:---------------:|:-----------------------:|:----------------------:|:------------------------:|
|   Single word  |           9.0%          |           9.5%        |           10.1%           |
|    Two words   |           50.4%          |          48.2%          |           45.7%           |
|   Three words  |           27.6%         |          28.6%          |           29.8%           |
|   Four words   |           9.3%            |          10.3%          |           10.3%           |
|   Five words   |           2.4%           |           2.0%          |            3.2%           |
|    Six words   |           0.9%          |           1.2%          |            0.7%           |
|   Seven words  |           0.3%           |           0.2%          |            0.2%           |
| Eight words    |           0.1%           |            0%           |            0.1%           |
|   Nine words   |            0%          |           0.1%          |             0%            |

Table 2: Statistics on the length of the extractive keyphrases for Train, Test, and Validation splits of Inspec dataset.

|              | Train | Test | Validation |
|:------------:|:-----------------------:|:----------------------:|:------------------------:|
| Single word |           16.2%          |          15.4%          |           17.0%           |
|  Two words  |           52.4%          |          54.8%          |           51.6%           |
| Three words |           24.3%          |          22.99%         |           24.3%           |
|  Four words |           5.6%           |          4.96%          |            5.8%           |
|  Five words |           1.2%           |           1.3%          |            1.1%           |
|  Six words  |           0.2%           |          0.36%          |            0.2%           |
| Seven words |           0.1%           |          0.06%          |            0.1%           |
| Eight words |            0%            |            0%           |           0.03%           |

Table 3: General statistics of the Inspec dataset.

|                Type of Analysis                |       Train      |       Test       |    Validation    |
|:----------------------------------------------:|:------------------------------:|:------------------------------:|:------------------------------:|
|                 Annotator Type                 |      Professional Indexers      |      Professional Indexers      |      Professional Indexers      |
|                  Document Type                 | Abstracts from Inspec Database | Abstracts from Inspec Database | Abstracts from Inspec Database |
|                 No. of Documents                |              1000              |               500              |               500              |
|              Avg. Document length (words)              |              141.5             |              134.6             |              132.6             |
|               Max Document length (words)             |               557              |               384              |               330              |
|  Max no. of abstractive keyphrases in a document |               17               |               20               |               14               |
|  Min no. of abstractive keyphrases in a document |                0               |                0               |                0               |
| Avg. no. of abstractive keyphrases  per document |              3.39              |              3.26              |              3.12              |
|  Max no. of extractive keyphrases in a document  |               24               |               27               |               22               |
|  Min no. of extractive keyphrases in a document  |                0               |                0               |                0               |
|  Avg. no. of extractive keyphrases  per document |              6.39              |              6.56              |              5.95              |


- Percentage of keyphrases that are named entities:  55.25% (named entities detected using scispacy - en-core-sci-lg model)

- Percentage of keyphrases that are noun phrases:  73.59% (noun phrases detected using spacy after removing determiners)


### Data Fields

- **id**: unique identifier of the document.
- **document**: Whitespace separated list of words in the document.
- **doc_bio_tags**: BIO tags for each word in the document. B stands for the beginning of a keyphrase and I stands for inside the keyphrase. O stands for outside the keyphrase and represents the word that isn't a part of the keyphrase at all.
- **extractive_keyphrases**: List of all the present keyphrases.
- **abstractive_keyphrase**: List of all the absent keyphrases.


### Data Splits

|Split| No. of datapoints  |
|--|--|
| Train | 1,000 |
| Test | 500 |
| Validation | 500 |

## Usage

### Full Dataset

```python
from datasets import load_dataset

# get entire dataset
dataset = load_dataset("midas/inspec", "raw")

# sample from the train split
print("Sample from training dataset split")
train_sample = dataset["train"][0]
print("Fields in the sample: ", [key for key in train_sample.keys()])
print("Tokenized Document: ", train_sample["document"])
print("Document BIO Tags: ", train_sample["doc_bio_tags"])
print("Extractive/present Keyphrases: ", train_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", train_sample["abstractive_keyphrases"])
print("\n-----------\n")

# sample from the validation split
print("Sample from validation dataset split")
validation_sample = dataset["validation"][0]
print("Fields in the sample: ", [key for key in validation_sample.keys()])
print("Tokenized Document: ", validation_sample["document"])
print("Document BIO Tags: ", validation_sample["doc_bio_tags"])
print("Extractive/present Keyphrases: ", validation_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", validation_sample["abstractive_keyphrases"])
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
Tokenized Document:  ['A', 'conflict', 'between', 'language', 'and', 'atomistic', 'information', 'Fred', 'Dretske', 'and', 'Jerry', 'Fodor', 'are', 'responsible', 'for', 'popularizing', 'three', 'well-known', 'theses', 'in', 'contemporary', 'philosophy', 'of', 'mind', ':', 'the', 'thesis', 'of', 'Information-Based', 'Semantics', '-LRB-', 'IBS', '-RRB-', ',', 'the', 'thesis', 'of', 'Content', 'Atomism', '-LRB-', 'Atomism', '-RRB-', 'and', 'the', 'thesis', 'of', 'the', 'Language', 'of', 'Thought', '-LRB-', 'LOT', '-RRB-', '.', 'LOT', 'concerns', 'the', 'semantically', 'relevant', 'structure', 'of', 'representations', 'involved', 'in', 'cognitive', 'states', 'such', 'as', 'beliefs', 'and', 'desires', '.', 'It', 'maintains', 'that', 'all', 'such', 'representations', 'must', 'have', 'syntactic', 'structures', 'mirroring', 'the', 'structure', 'of', 'their', 'contents', '.', 'IBS', 'is', 'a', 'thesis', 'about', 'the', 'nature', 'of', 'the', 'relations', 'that', 'connect', 'cognitive', 'representations', 'and', 'their', 'parts', 'to', 'their', 'contents', '-LRB-', 'semantic', 'relations', '-RRB-', '.', 'It', 'holds', 'that', 'these', 'relations', 'supervene', 'solely', 'on', 'relations', 'of', 'the', 'kind', 'that', 'support', 'information', 'content', ',', 'perhaps', 'with', 'some', 'help', 'from', 'logical', 'principles', 'of', 'combination', '.', 'Atomism', 'is', 'a', 'thesis', 'about', 'the', 'nature', 'of', 'the', 'content', 'of', 'simple', 'symbols', '.', 'It', 'holds', 'that', 'each', 'substantive', 'simple', 'symbol', 'possesses', 'its', 'content', 'independently', 'of', 'all', 'other', 'symbols', 'in', 'the', 'representational', 'system', '.', 'I', 'argue', 'that', 'Dretske', "'s", 'and', 'Fodor', "'s", 'theories', 'are', 'false', 'and', 'that', 'their', 'falsehood', 'results', 'from', 'a', 'conflict', 'IBS', 'and', 'Atomism', ',', 'on', 'the', 'one', 'hand', ',', 'and', 'LOT', ',', 'on', 'the', 'other']
Document BIO Tags:  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'O', 'B', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'B', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O']
Extractive/present Keyphrases:  ['philosophy of mind', 'content atomism', 'ibs', 'language of thought', 'lot', 'cognitive states', 'beliefs', 'desires']
Abstractive/absent Keyphrases:  ['information-based semantics']

-----------

Sample from validation data split
Fields in the sample:  ['id', 'document', 'doc_bio_tags', 'extractive_keyphrases', 'abstractive_keyphrases', 'other_metadata']
Tokenized Document:  ['Impact', 'of', 'aviation', 'highway-in-the-sky', 'displays', 'on', 'pilot', 'situation', 'awareness', 'Thirty-six', 'pilots', '-LRB-', '31', 'men', ',', '5', 'women', '-RRB-', 'were', 'tested', 'in', 'a', 'flight', 'simulator', 'on', 'their', 'ability', 'to', 'intercept', 'a', 'pathway', 'depicted', 'on', 'a', 'highway-in-the-sky', '-LRB-', 'HITS', '-RRB-', 'display', '.', 'While', 'intercepting', 'and', 'flying', 'the', 'pathway', ',', 'pilots', 'were', 'required', 'to', 'watch', 'for', 'traffic', 'outside', 'the', 'cockpit', '.', 'Additionally', ',', 'pilots', 'were', 'tested', 'on', 'their', 'awareness', 'of', 'speed', ',', 'altitude', ',', 'and', 'heading', 'during', 'the', 'flight', '.', 'Results', 'indicated', 'that', 'the', 'presence', 'of', 'a', 'flight', 'guidance', 'cue', 'significantly', 'improved', 'flight', 'path', 'awareness', 'while', 'intercepting', 'the', 'pathway', ',', 'but', 'significant', 'practice', 'effects', 'suggest', 'that', 'a', 'guidance', 'cue', 'might', 'be', 'unnecessary', 'if', 'pilots', 'are', 'given', 'proper', 'training', '.', 'The', 'amount', 'of', 'time', 'spent', 'looking', 'outside', 'the', 'cockpit', 'while', 'using', 'the', 'HITS', 'display', 'was', 'significantly', 'less', 'than', 'when', 'using', 'conventional', 'aircraft', 'instruments', '.', 'Additionally', ',', 'awareness', 'of', 'flight', 'information', 'present', 'on', 'the', 'HITS', 'display', 'was', 'poor', '.', 'Actual', 'or', 'potential', 'applications', 'of', 'this', 'research', 'include', 'guidance', 'for', 'the', 'development', 'of', 'perspective', 'flight', 'display', 'standards', 'and', 'as', 'a', 'basis', 'for', 'flight', 'training', 'requirements']
Document BIO Tags:  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'B', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
Extractive/present Keyphrases:  ['flight simulator', 'pilots', 'cockpit', 'flight guidance', 'situation awareness', 'flight path awareness']
Abstractive/absent Keyphrases:  ['highway-in-the-sky display', 'human factors', 'aircraft display']

-----------

Sample from test data split
Fields in the sample:  ['id', 'document', 'doc_bio_tags', 'extractive_keyphrases', 'abstractive_keyphrases', 'other_metadata']
Tokenized Document:  ['A', 'new', 'graphical', 'user', 'interface', 'for', 'fast', 'construction', 'of', 'computation', 'phantoms', 'and', 'MCNP', 'calculations', ':', 'application', 'to', 'calibration', 'of', 'in', 'vivo', 'measurement', 'systems', 'Reports', 'on', 'a', 'new', 'utility', 'for', 'development', 'of', 'computational', 'phantoms', 'for', 'Monte', 'Carlo', 'calculations', 'and', 'data', 'analysis', 'for', 'in', 'vivo', 'measurements', 'of', 'radionuclides', 'deposited', 'in', 'tissues', '.', 'The', 'individual', 'properties', 'of', 'each', 'worker', 'can', 'be', 'acquired', 'for', 'a', 'rather', 'precise', 'geometric', 'representation', 'of', 'his', '-LRB-', 'her', '-RRB-', 'anatomy', ',', 'which', 'is', 'particularly', 'important', 'for', 'low', 'energy', 'gamma', 'ray', 'emitting', 'sources', 'such', 'as', 'thorium', ',', 'uranium', ',', 'plutonium', 'and', 'other', 'actinides', '.', 'The', 'software', 'enables', 'automatic', 'creation', 'of', 'an', 'MCNP', 'input', 'data', 'file', 'based', 'on', 'scanning', 'data', '.', 'The', 'utility', 'includes', 'segmentation', 'of', 'images', 'obtained', 'with', 'either', 'computed', 'tomography', 'or', 'magnetic', 'resonance', 'imaging', 'by', 'distinguishing', 'tissues', 'according', 'to', 'their', 'signal', '-LRB-', 'brightness', '-RRB-', 'and', 'specification', 'of', 'the', 'source', 'and', 'detector', '.', 'In', 'addition', ',', 'a', 'coupling', 'of', 'individual', 'voxels', 'within', 'the', 'tissue', 'is', 'used', 'to', 'reduce', 'the', 'memory', 'demand', 'and', 'to', 'increase', 'the', 'calculational', 'speed', '.', 'The', 'utility', 'was', 'tested', 'for', 'low', 'energy', 'emitters', 'in', 'plastic', 'and', 'biological', 'tissues', 'as', 'well', 'as', 'for', 'computed', 'tomography', 'and', 'magnetic', 'resonance', 'imaging', 'scanning', 'information']
Document BIO Tags:  ['O', 'O', 'B', 'I', 'I', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'B', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'B', 'I', 'I', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'O', 'B', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'B', 'O', 'B', 'I', 'O', 'O', 'B', 'I', 'I', 'I', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'B', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'B', 'I', 'I', 'I', 'I']
Extractive/present Keyphrases:  ['computational phantoms', 'monte carlo calculations', 'in vivo measurements', 'radionuclides', 'tissues', 'worker', 'precise geometric representation', 'mcnp input data file', 'scanning data', 'computed tomography', 'brightness', 'graphical user interface', 'computation phantoms', 'calibration', 'in vivo measurement systems', 'signal', 'detector', 'individual voxels', 'memory demand', 'calculational speed', 'plastic', 'magnetic resonance imaging scanning information', 'anatomy', 'low energy gamma ray emitting sources', 'actinides', 'software', 'automatic creation']
Abstractive/absent Keyphrases:  ['th', 'u', 'pu', 'biological tissues']

-----------

```

### Keyphrase Extraction
```python
from datasets import load_dataset

# get the dataset only for keyphrase extraction
dataset = load_dataset("midas/inspec", "extraction")

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
dataset = load_dataset("midas/inspec", "generation")

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
Please cite the works below if you use this dataset in your work.

```
@inproceedings{hulth2003improved,
  title={Improved automatic keyword extraction given more linguistic knowledge},
  author={Hulth, Anette},
  booktitle={Proceedings of the 2003 conference on Empirical methods in natural language processing},
  pages={216--223},
  year={2003}
}
```
and

```
@InProceedings{10.1007/978-3-030-45442-5_41,
author="Sahrawat, Dhruva
and Mahata, Debanjan
and Zhang, Haimin
and Kulkarni, Mayank
and Sharma, Agniv
and Gosangi, Rakesh
and Stent, Amanda
and Kumar, Yaman
and Shah, Rajiv Ratn
and Zimmermann, Roger",
editor="Jose, Joemon M.
and Yilmaz, Emine
and Magalh{\~a}es, Jo{\~a}o
and Castells, Pablo
and Ferro, Nicola
and Silva, M{\'a}rio J.
and Martins, Fl{\'a}vio",
title="Keyphrase Extraction as Sequence Labeling Using Contextualized Embeddings",
booktitle="Advances in Information Retrieval",
year="2020",
publisher="Springer International Publishing",
address="Cham",
pages="328--335",
abstract="In this paper, we formulate keyphrase extraction from scholarly articles as a sequence labeling task solved using a BiLSTM-CRF, where the words in the input text are represented using deep contextualized embeddings. We evaluate the proposed architecture using both contextualized and fixed word embedding models on three different benchmark datasets, and compare with existing popular unsupervised and supervised techniques. Our results quantify the benefits of: (a) using contextualized embeddings over fixed word embeddings; (b) using a BiLSTM-CRF architecture with contextualized word embeddings over fine-tuning the contextualized embedding model directly; and (c) using domain-specific contextualized embeddings (SciBERT). Through error analysis, we also provide some insights into why particular models work better than the others. Lastly, we present a case study where we analyze different self-attention layers of the two best models (BERT and SciBERT) to better understand their predictions.",
isbn="978-3-030-45442-5"
}
```

and

```
@article{kulkarni2021learning,
  title={Learning Rich Representation of Keyphrases from Text},
  author={Kulkarni, Mayank and Mahata, Debanjan and Arora, Ravneet and Bhowmik, Rajarshi},
  journal={arXiv preprint arXiv:2112.08547},
  year={2021}
}

```

## Contributions
Thanks to [@debanjanbhucs](https://github.com/debanjanbhucs), [@dibyaaaaax](https://github.com/dibyaaaaax), [@UmaGunturi](https://github.com/UmaGunturi) and [@ad6398](https://github.com/ad6398) for adding this dataset
