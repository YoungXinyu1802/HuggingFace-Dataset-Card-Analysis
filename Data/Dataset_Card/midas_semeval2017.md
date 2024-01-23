A dataset for benchmarking keyphrase extraction and generation techniques from abstracts of english scientific articles. For more details about the dataset please refer the original paper - [https://arxiv.org/abs/1704.02853](https://arxiv.org/abs/1704.02853)

Original source of the data - [https://scienceie.github.io/](https://scienceie.github.io/)

## Dataset Summary
The Semeval-2017 dataset was originally proposed by *Isabelle Augenstein et al.* in the paper titled - [SemEval 2017 Task 10: ScienceIE - Extracting Keyphrases and Relations from Scientific Publications](https://arxiv.org/abs/1704.02853) in the year 2017. The dataset consists of a abstracts of 500 English scientific papers from the ScienceDirect open access publications. The selected articles were evenly distributed among the domains of Computer Science, Material Sciences and Physics. Each paper has a set of keyphrases annotated by student volunteers. Each paper was double-annotated, where the second annotation was done by an expert annotator. In case of disagreement, the annotations done by expert annotators were chosen. The original dataset was divided into train, dev and test splits, evenly distributed across the three domains. The train, dev and test splits had 350, 50 and 100 articles respectively.

 The dataset shared over here categorizes the keyphrases into *extractive* and *abstractive*. **Extractive keyphrases** are those that could be found in the input text and the **abstractive keyphrases** are those that are not present in the input text. In order to get all the meta-data about the documents and keyphrases please refer to the [original source](https://scienceie.github.io/) from which the dataset was taken from. The main motivation behind making this dataset available in the form as presented over here is to make it easy for the researchers to programmatically download it and evaluate their models for the tasks of keyphrase extraction and generation. As keyphrase extraction by treating it as a sequence tagging task and using contextual language models has become popular - [Keyphrase extraction from scholarly articles as sequence labeling using contextualized embeddings](https://arxiv.org/pdf/1910.08840.pdf), we have also made the token tags available in the BIO tagging format.   



## Dataset Structure
Table 1: Statistics on the length of the abstractive keyphrases for Train, Test, and Validation splits of SemEval 2017 dataset.

|                   |  Train |  Test  | Validation |
|:-----------------:|:------:|:------:|:----------:|
|    Single word    | 11.59% | 12.47% |   12.89%   |
|     Two words     | 30.69% | 40.92% |   33.45%   |
|    Three words    | 19.20% | 17.50% |   19.16%   |
|     Four words    | 10.25% | 10.94% |    9.41%   |
|     Five words    |  7.43% |  4.60% |    8.36%   |
|     Six words     |  5.96% |  4.37% |    6.27%   |
|    Seven words    |  4.28% |  2.40% |    3.14%   |
|    Eight words    |  2.59% |  1.75% |    1.34%   |
|     Nine words    |  2.19% |  1.75% |    1.74%   |
|     Ten words     |  1.35% |  1.31% |    0.69%   |
|    Eleven words   |  0.96% |  0.44% |    1.04%   |
|    Twelve words   |  1.13% |  0.44% |    1.04%   |
|   Thirteen words  |   0%   |  0.44% |    0.34%   |
|   Fourteen words  |  0.45% |  0.22% |   0.348%   |
|   Fifteen words   |  0.39% |   0%   |     0%     |
|   Sixteen words   |  0.17% |   0%   |     0%     |
|  Seventeen words  |  0.11% |  0.22% |    0.34%   |
|   Eighteen words  |  0.11% |   0%   |     0%     |
|   Nineteen words  |  0.11% |  0.22% |    0.34%   |
|    Twenty words   |  0.06% |   0%   |     0%     |
|  Twenty-two words |  0.06% |   0%   |     0%     |
| Twenty-five words |   0%   |   0%   |     0%     |

Table 2: Statistics on the length of the extractive keyphrases for Train, Test, and Validation splits of SemEval 2017 dataset.

|                   |  Train |  Test  | Validation |
|:-----------------:|:------:|:------:|:----------:|
|    Single word    | 27.94% | 34.50% |   36.56%   |
|     Two words     | 33.04% | 39.64% |   31.72%   |
|    Three words    | 17.85% | 13.45% |   15.50%   |
|     Four words    |  8.75% |  6.19% |    7.11%   |
|     Five words    |  4.72% |  2.44% |    4.27%   |
|     Six words     |  2.24% |  0.89% |    1.85%   |
|    Seven words    |  1.66% |  0.73% |    1.28%   |
|    Eight words    |  1.33% |  0.48% |    0.43%   |
|     Nine words    |  0.54% |  0.97% |    0.14%   |
|     Ten words     |  0.21% |  0.24% |    0.57%   |
|    Eleven words   |  0.38% | 0.081% |    0.28%   |
|    Twelve words   |   0%   |  0.16% |    0.14%   |
|   Thirteen words  |  0.28% |   0%   |     0%     |
|   Fourteen words  |  0.21% |   0%   |     0%     |
|   Fifteen words   | 0.071% |   0%   |     0%     |
|   Sixteen words   |  0.02% | 0.081% |     0%     |
|   Eighteen words  |   0%   | 0.081% |    0.14    |
|   Nineteen words  |  0.02% |   0%   |     0%     |
| Twenty-five words |  0.04% |   0%   |     0%     |

Table 3: General statistics of the Semeval 2017 dataset.

|                 Type of Analysis                 |        Train        |         Test        |      Validation     |
|:------------------------------------------------:|:-------------------:|:-------------------:|:-------------------:|
|                  Annotator Type                  | Authors and Readers | Authors and Readers | Authors and Readers |
|                   Document Type                  |  Scientific Papers  |  Scientific Papers  |  Scientific Papers  |
|                 No. of Documents                 |         350         |         100         |          50         |
|           Avg. Document length (words)           |        160.5        |        190.4        |        380.8        |
|            Max Document length (words)           |         355         |         297         |         355         |
|  Max no. of abstractive keyphrases in a document |          23         |          13         |          22         |
|  Min no. of abstractive keyphrases in a document |          0          |          0          |          0          |
| Avg. no. of abstractive keyphrases  per document |         5.07        |         4.57        |         5.74        |
|  Max no. of extractive keyphrases in a document  |          29         |          27         |          30         |
|  Min no. of extractive keyphrases in a document  |          2          |          4          |          2          |
|  Avg. no. of extractive keyphrases  per document |         11.9        |        12.26        |        14.06        |

Train

- Percentage of keyphrases that are named entities: 50.09% (named entities detected using scispacy - en-core-sci-lg model)
- Percentage of keyphrases that are noun phrases: 57.65% (noun phrases detected using spacy en-core-web-lg after removing determiners)

Validation

- Percentage of keyphrases that are named entities: 60.02% (named entities detected using scispacy - en-core-sci-lg model)
- Percentage of keyphrases that are noun phrases: 62.87% (noun phrases detected using spacy en-core-web-lg after removing determiners)

Test

- Percentage of keyphrases that are named entities: 59.78% (named entities detected using scispacy - en-core-sci-lg model)
- Percentage of keyphrases that are noun phrases: 66.39% (noun phrases detected using spacy en-core-web-lg after removing determiners)


### Data Fields

- **id**: unique identifier of the document.
- **document**: Whitespace separated list of words in the document.
- **doc_bio_tags**: BIO tags for each word in the document. B stands for the beginning of a keyphrase and I stands for inside the keyphrase. O stands for outside the keyphrase and represents the word that isn't a part of the keyphrase at all.
- **extractive_keyphrases**: List of all the present keyphrases.
- **abstractive_keyphrase**: List of all the absent keyphrases.


### Data Splits

|Split| #datapoints  |
|--|--|
| Train | 350 |
| Test | 100 |
| Validation | 50 |


## Usage

### Full Dataset

```python
from datasets import load_dataset

# get entire dataset
dataset = load_dataset("midas/semeval2017", "raw")

# sample from the train split
print("Sample from train dataset split")
test_sample = dataset["train"][0]
print("Fields in the sample: ", [key for key in test_sample.keys()])
print("Tokenized Document: ", test_sample["document"])
print("Document BIO Tags: ", test_sample["doc_bio_tags"])
print("Extractive/present Keyphrases: ", test_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", test_sample["abstractive_keyphrases"])
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
Sample from train dataset split
Fields in the sample:  ['id', 'document', 'doc_bio_tags', 'extractive_keyphrases', 'abstractive_keyphrases', 'other_metadata']
Tokenized Document:  ['It', 'is', 'well', 'known', 'that', 'one', 'of', 'the', 'long', 'standing', 'problems', 'in', 'physics', 'is', 'understanding', 'the', 'confinement', 'physics', 'from', 'first', 'principles.', 'Hence', 'the', 'challenge', 'is', 'to', 'develop', 'analytical', 'approaches', 'which', 'provide', 'valuable', 'insight', 'and', 'theoretical', 'guidance.', 'According', 'to', 'this', 'viewpoint,', 'an', 'effective', 'theory', 'in', 'which', 'confining', 'potentials', 'are', 'obtained', 'as', 'a', 'consequence', 'of', 'spontaneous', 'symmetry', 'breaking', 'of', 'scale', 'invariance', 'has', 'been', 'developed', '[1].', 'In', 'particular,', 'it', 'was', 'shown', 'that', 'a', 'such', 'theory', 'relies', 'on', 'a', 'scale-invariant', 'Lagrangian', 'of', 'the', 'type', '[2]', '(1)L=14w2−12w−FμνaFaμν,', 'where', 'Fμνa=∂μAνa−∂νAμa+gfabcAμbAνc,', 'and', 'w', 'is', 'not', 'a', 'fundamental', 'field', 'but', 'rather', 'is', 'a', 'function', 'of', '4-index', 'field', 'strength,', 'that', 'is,', '(2)w=εμναβ∂μAναβ.', 'The', 'Aναβ', 'equation', 'of', 'motion', 'leads', 'to', '(3)εμναβ∂βw−−FγδaFaγδ=0,', 'which', 'is', 'then', 'integrated', 'to', '(4)w=−FμνaFaμν+M.', 'It', 'is', 'easy', 'to', 'verify', 'that', 'the', 'Aaμ', 'equation', 'of', 'motion', 'leads', 'us', 'to', '(5)∇μFaμν+MFaμν−FαβbFbαβ=0.', 'It', 'is', 'worth', 'stressing', 'at', 'this', 'stage', 'that', 'the', 'above', 'equation', 'can', 'be', 'obtained', 'from', 'the', 'effective', 'Lagrangian', '(6)Leff=−14FμνaFaμν+M2−FμνaFaμν.', 'Spherically', 'symmetric', 'solutions', 'of', 'Eq.', '(5)', 'display,', 'even', 'in', 'the', 'Abelian', 'case,', 'a', 'Coulomb', 'piece', 'and', 'a', 'confining', 'part.', 'Also,', 'the', 'quantum', 'theory', 'calculation', 'of', 'the', 'static', 'energy', 'between', 'two', 'charges', 'displays', 'the', 'same', 'behavior', '[1].', 'It', 'is', 'well', 'known', 'that', 'the', 'square', 'root', 'part', 'describes', 'string', 'like', 'solutions', '[3,4].']
Document BIO Tags:  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'O', 'B', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'B', 'I', 'O', 'O', 'B', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'O']
Extractive/present Keyphrases:  ['aaμ equation of motion', 'aναβ equation of motion leads', 'confining part', 'coulomb piece', 'develop analytical approaches', 'quantum theory calculation of the static energy between two charges', 'spherically symmetric solutions', 'spontaneous symmetry breaking of scale invariance', 'string like solutions', 'the effective lagrangian', 'understanding the confinement physics from first principles']
Abstractive/absent Keyphrases:  ['(2)w=εμναβ∂μaναβ', 'function of 4-index field strength', 'integrated to (4)w=−fμνafaμν+m', 'leff=−14fμνafaμν+m2−fμνafaμν', 'scale-invariant lagrangian', 'εμναβ∂βw−−fγδafaγδ=0']

-----------

Sample from validation dataset split
Fields in the sample:  ['id', 'document', 'doc_bio_tags', 'extractive_keyphrases', 'abstractive_keyphrases', 'other_metadata']
Tokenized Document:  ['In', 'the', 'current', 'CLSVOF', 'method,', 'the', 'normal', 'vector', 'is', 'calculated', 'directly', 'by', 'discretising', 'the', 'LS', 'gradient', 'using', 'a', 'finite', 'difference', 'scheme.', 'By', 'appropriately', 'choosing', 'one', 'of', 'three', 'finite', 'difference', 'schemes', '(central,', 'forward,', 'or', 'backward', 'differencing),', 'it', 'has', 'been', 'demonstrated', 'that', 'thin', 'liquid', 'ligaments', 'can', 'be', 'well', 'resolved', 'see', 'Xiao', '(2012).', 'Although', 'a', 'high', 'order', 'discretisation', 'scheme', '(e.g.', '5th', 'order', 'WENO)', 'has', 'been', 'found', 'necessary', 'for', 'LS', 'evolution', 'in', 'pure', 'LS', 'methods', 'to', 'reduce', 'mass', 'error,', 'low', 'order', 'LS', 'discretisation', 'schemes', '(2nd', 'order', 'is', 'used', 'here)', 'can', 'produce', 'accurate', 'results', 'when', 'the', 'LS', 'equation', 'is', 'solved', 'and', 'constrained', 'as', 'indicated', 'above', 'in', 'a', 'CLSVOF', 'method', '(see', 'Xiao,', '2012),', 'since', 'the', 'VOF', 'method', 'maintains', '2nd', 'order', 'accuracy.', 'This', 'is', 'a', 'further', 'reason', 'to', 'adopt', 'the', 'CLSVOF', 'method,', 'which', 'has', 'been', 'used', 'for', 'all', 'the', 'following', 'simulations', 'of', 'liquid', 'jet', 'primary', 'breakup.']
Document BIO Tags:  ['O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'B', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'I', 'O', 'B', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'B', 'O', 'O', 'B', 'I', 'I', 'B', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O']
Extractive/present Keyphrases:  ['5th order weno', 'clsvof method', 'finite difference scheme', 'finite difference schemes', 'high order discretisation scheme', 'liquid', 'low order ls discretisation schemes', 'ls', 'reduce mass error', 'vof method']
Abstractive/absent Keyphrases:  ['central, forward, or backward differencing', 'ls methods', 'simulations of liquid jet primary breakup', 'thin liquid ligaments']

-----------

Sample from test dataset split
Fields in the sample:  ['id', 'document', 'doc_bio_tags', 'extractive_keyphrases', 'abstractive_keyphrases', 'other_metadata']
Tokenized Document:  ['Traditionally,', 'archaeologists', 'have', 'recorded', 'sites', 'and', 'artefacts', 'via', 'a', 'combination', 'of', 'ordinary', 'still', 'photographs,', '2D', 'line', 'drawings', 'and', 'occasional', 'cross-sections.', 'Given', 'these', 'constraints,', 'the', 'attractions', 'of', '3D', 'models', 'have', 'been', 'obvious', 'for', 'some', 'time,', 'with', 'digital', 'photogrammetry', 'and', 'laser', 'scanners', 'offering', 'two', 'well-known', 'methods', 'for', 'data', 'capture', 'at', 'close', 'range', '(e.g.', 'Bates', 'et', 'al.,', '2010;', 'Hess', 'and', 'Robson,', '2010).', 'The', 'highest', 'specification', 'laser', 'scanners', 'still', 'boast', 'better', 'positional', 'accuracy', 'and', 'greater', 'true', 'colour', 'fidelity', 'than', 'SfM–MVS', 'methods', '(James', 'and', 'Robson,', '2012),', 'but', 'the', 'latter', 'produce', 'very', 'good', 'quality', 'models', 'nonetheless', 'and', 'have', 'many', 'unique', 'selling', 'points.', 'Unlike', 'traditional', 'digital', 'photogrammetry,', 'little', 'or', 'no', 'prior', 'control', 'of', 'camera', 'position', 'is', 'necessary,', 'and', 'unlike', 'laser', 'scanning,', 'no', 'major', 'equipment', 'costs', 'or', 'setup', 'are', 'involved.', 'However,', 'the', 'key', 'attraction', 'of', 'SfM–MVS', 'is', 'that', 'the', 'required', 'input', 'can', 'be', 'taken', 'by', 'anyone', 'with', 'a', 'digital', 'camera', 'and', 'modest', 'prior', 'training', 'about', 'the', 'required', 'number', 'and', 'overlap', 'of', 'photographs.', 'A', 'whole', 'series', 'of', 'traditional', 'bottlenecks', 'are', 'thereby', 'removed', 'from', 'the', 'recording', 'process', 'and', 'large', 'numbers', 'of', 'archaeological', 'landscapes,', 'sites', 'or', 'artefacts', 'can', 'now', 'be', 'captured', 'rapidly,', 'in', 'the', 'field,', 'in', 'the', 'laboratory', 'or', 'in', 'the', 'museum.', 'Fig.', '2a–c', 'shows', 'examples', 'of', 'terracotta', 'warrior', 'models', 'for', 'which', 'the', 'level', 'of', 'surface', 'detail', 'is', 'considerable.']
Document BIO Tags:  ['O', 'O', 'O', 'O', 'B', 'O', 'B', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'B', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'B', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'B', 'I', 'B', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
Extractive/present Keyphrases:  ['2d line drawings', '3d models', 'archaeological landscapes', 'artefacts', 'control of camera position', 'data capture at close range', 'digital camera', 'digital photogrammetry', 'laser scanners', 'laser scanning', 'ordinary still photographs', 'prior training about the required number and overlap of photographs', 'recording process', 'sfm–mvs', 'sites', 'terracotta warrior models']
Abstractive/absent Keyphrases:  ['occasional cross-sections', 'recorded sites and artefacts', 'sfm–mvs methods', 'traditional digital photogrammetry']

-----------
```

### Keyphrase Extraction
```python
from datasets import load_dataset

# get the dataset only for keyphrase extraction
dataset = load_dataset("midas/semeval2017", "extraction")

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
dataset = load_dataset("midas/semeval2017", "generation")

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
@article{DBLP:journals/corr/AugensteinDRVM17,
  author    = {Isabelle Augenstein and
               Mrinal Das and
               Sebastian Riedel and
               Lakshmi Vikraman and
               Andrew McCallum},
  title     = {SemEval 2017 Task 10: ScienceIE - Extracting Keyphrases and Relations
               from Scientific Publications},
  journal   = {CoRR},
  volume    = {abs/1704.02853},
  year      = {2017},
  url       = {http://arxiv.org/abs/1704.02853},
  eprinttype = {arXiv},
  eprint    = {1704.02853},
  timestamp = {Mon, 13 Aug 2018 16:46:36 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/AugensteinDRVM17.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

## Contributions
Thanks to [@debanjanbhucs](https://github.com/debanjanbhucs), [@dibyaaaaax](https://github.com/dibyaaaaax) and [@ad6398](https://github.com/ad6398) for adding this dataset
