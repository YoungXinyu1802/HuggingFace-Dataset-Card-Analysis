---
task_categories:
- question-answering
- token-classification
language:
- en
---
# Metaphors and analogies datasets

These datasets contain word pairs and quadruples forming analogies, metaphoric mapping or sematically unacceptable compositions.


- Pair instances are pairs of nouns A and B in a sentence of the form "A is a B".


- Quadruple instances are of the form : < (A,B),(C,D) >
There is an analogy when A is to B what C is to D.
The analogy is also a metaphor when the (A,B) and (C,D) form a metaphoric mapping, usually when they come from different domains.

## Dataset Description

- **Homepage:** 
- **Repository:** 
- **Paper:** 
- **Leaderboard:** 
- **Point of Contact:** 


Language : English




### Datasets and paper links

| Name       | Size    | Labels     | Description                                                         |
| ---------: | :-----  |:--------   | :-------------------------------------------------------------------------- |
| `Cardillo` | 260 *2  | 1, 2      | Pairs of "A is-a B" sentences composed of one metaphoric and one literal sentence. The two sentences of a given pair share the same B term. |
| `Jankowiak`| 120*3   | 0, 1, 2    | Triples of "A is-a/is-like-a B" sentences with exactly one literal, one semantic abnormal and one metaphoric sentence. |
| `Green`    | 40*3    | 0, 1, 2    | Triples of proportional analogies, made of 4 terms <A, B, Ci, Di> each. One stem <A,B> is composed with 3 different <Ci,Di> pairs, to form exaclty one near analogy, one far analogy and one non analogic quadruple|
| `Kmiecik`  |   720   | 0, 1, 2    | Quadruples <A,B,C,D> labelled as analogy:True/False and far_analogy: True/False|
| `SAT-met`  | 160?*5  | 0, 1, 2, 12 |  One pair stem <A,B> to combine with 5 different pairs <Ci,Di> and attempt to form proportional analogies. Only one <Ci,Di> forms an analogy with <A,B> We additionally labelled the analogies as **metaphoric**:True/False|



| Name       | Paper Citation    | Paper link | Dataset link                                        |
| ---------: | :------- | :------------------------------ |-----------------------------------------: |
| `Cardillo` |       |  [Cardillo (2010)](https://link.springer.com/article/10.3758/s13428-016-0717-1) [Cardillo (2017)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2952404/ )     |  |
| `Jankowiak`|     |   [Jankowiak (2020)]( https://link-springer-com.abc.cardiff.ac.uk/article/10.1007/s10936-020-09695-7) | |
| `Green`    | Green, A. E., Kraemer, D. J. M., Fugelsang, J., Gray, J. R., & Dunbar, K. (2010). Connecting Long Distance: Semantic Distance in Analogical Reasoning Modulates Frontopolar Cortex Activity. Cerebral Cortex, 10, 70-76.    | [Green (20)]() ||
| `Kmiecik`  |Kmiecik, M. J., Brisson, R. J., & Morrison, R. G. (2019). The time course of semantic and relational processing during verbal analogical reasoning. Brain and Cognition, 129, 25-34. | [Kmiecik (20)]() ||
| `SAT-met`  |   |  [Turney (2005)](https://arxiv.org/pdf/cs/0508053.pdf)   | |




### Labels :

- Pairs

    - **0** : anomaly
    - **1** : literal
    - **2** : metaphor 
    
    
- Quadruples :
    - **0** : not an analogy
    - **1** : an analogy but not a metaphor
    - **2** : an analogy and a metaphor or a far analogy
    - **12** : maybe a metaphor, somewhere between 1 and 2


### Dataset Splits

- Both lexical and random splits are available for classification experiments.

	- Size of the splits :

		- **train** : 50 %
		- **validation** : 10 %
		- **test** : 40 %

- Additionally, for all datasets, the `5-folds` field gives frozen splits for a five-folds cross validation experiment with train/val/test = 70/10/20% of the sets.

# Datasets for Classification 

- Task : binary classification or 3-classes classification of pairs or quadruples. Each pair or quadruple is to classify between anomaly, non-metaphoric and metaphoric.


		
## Pairs

### Datasets names & splits :

| Original set | Dataset name |  Split  |
|-------------:| :------------ | :------ |
| Cardillo     | Pairs\_Cardillo\_random_split   | random  |
|              | Pairs\_Cardillo\_lexical_split  | lexical |
| Jankowiac    | Pairs\_Jankowiac\_random_split  | random  |
|              | Pairs\_Jankowiac\_lexical_split | lexical |



### Data fields :
	
| Field | Description | Type |
| -------------:| :------------ | ---- |
| corpus | name of the orgiginal dataset | str |
| id | instance id | str |
| set_id | id of the set containing the given instance in the multiple choice task | int |
| label | 0, 1, 2 | int |
| sentence | A is-a B sentence. | str |
| A | A expression in the sentence | str |
| B | B expression in the sentence | str |
| A\_position | position of A in the sentence | list(int) |
| B\_position | position of B in the sentence | list(int) |
| 5-folds | frozen splits for cross validation | list(str) |


### Examples :
	
|  Name |  Example | Label|
| -------: | :------------------------------------- | :-------- |
|Cardillo    |          |  |
|Jankowiac  |        |  |

	

## Quadruples

### Datasets names & splits

| Original set | dataset name |  Split |
| -------: | :------------------------------------- | :-------- |
|Green    | Quadruples\_Green\_random_split          | random |
|         | Quadruples\_Green\_lexical_split         | lexical |
|Kmiecik  | Quadruples\_Kmiecik\_random_split        | random |
|         | Quadruples\_Kmiecik\_lexical\_split\_on\_AB | lexical AB |
|         | Quadruples\_Kmiecik\_lexical_split\_on\_CD | lexical CD |
|SAT      | Quadruples\_SAT\_random\_split | random   | random |
|         | Quadruples\_SAT\_lexical\_split | lexical | lexical |



### Data fields :
	
| Field| Description |	Type |
| -------------: | :------------ | :------------ |
| corpus | Name of the orgiginal dataset | str |
| id | Element id | str |
| set\_id | Id of the set containing the given instance in the multiple-choice task datasets | int |
| label | 0, 1, 2, 12 | int |
| AB | pair of terms | list(str) |
| CD | pair of terms | list(str) |
| 5-folds | frozen splits for cross validation | list(str) |	
	

### Examples :

|  Name |  Example | Label|
|-------: | :------------------------------------- | :-------- |
|Green    |          |  |
|Kmiecik  |        |  |
| SAT     |                                        |  |



# Datasets for multiple choice questions or permutation

- Task : One stem and multiple choices. The stem and its possible combinations are to be combined to form a sentence. The resulting sentence has a label <0,1,2>. 
	
## Pairs

### Datasets names & splits :
	
| Original set | dataset name | Split |
| -----------|------| :---- |
| Cardillo   | Pairs\_Cardillo\_set | test only |
| Jankowiac  | Pairs\_Jankowiac\_set |test only |


### Data fields :


| Field | Description | Type |
| -------------: | :------------ | :------------ |	
| corpus | Name of the orgiginal dataset | str |
| id | Element id | str |
| pair_ids | Ids of each pair as appearing in the classification datasets. | list(str) |
| labels | 0, 1, 2 | list(int) |
| sentences |  List of the sentences composing the set | list(str) |
| A\_positions | Positions of the A's in each sentence  | list(list(int)) |
| B\_positions | Positions of the B's in each sentence | list(list(int)) |
| answer | Index of the metaphor  | int  |
| stem | Term shared between the sentences of the set. | str |
| 5-folds | frozen splits for cross validation | list(str) |


### Examples :

|  Name |  Stem | Sentences |Label|
|-------: |-------: | :------------------------------------- | :-------- |
|Cardillo | comet  | The astronomer's obssession was a comet. | 1 |
|          |  | The politician's career was a comet. | 2 | 
| Jankoviac |   harbour   | This banana is like a harbour | 0 |
|          |         | A house is a harbour | 2|
|          |       | This area is a harbour | 1 |

	
	
## Quadruples

### Datasets names & splits :


| Original set | dataset name | Split |
| ----------: | :------| :---- |
| Green      | Quadruples\_Green\_set | test only |
| SAT        | Quadruples\_SAT\_met_set | test only |



### Data fields : 


| Field | Description | Type |
|-------------: | :------------ | :------------ |
| corpus | name of the orgiginal dataset | str |
| id | Element id | str |
| pair\_ids | Ids of the instances as appearing in the clasification datasets | list(str) |
| labels | 0, 1, 2, 12 | list(int) |
| answer | temp | int |
| stem | Word pair to compose with all the other pairs of the set | list(str) |
| pairs | List of word pairs | list(list(str)) |
| 5-folds | Frozen splits for cross validation | list(str) |


### Examples :
	
	
|  Name |  Example | Label|
|-------: | :------------------------------------- | :-------- |
|Green    |          |  |
|     |  | |
| SAT     |                                        |  |
	
	







