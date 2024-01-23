---
license: apache-2.0
task_categories:
- text-classification
tags:
- sentence classification
- aerospace requirements
- design
- functional
- performance
- requirements
- NLP4RE
pretty_name: requirements_classification_dataset.txt
size_categories:
- n<1K
language:
- en
---

# Dataset Card for aeroBERT-classification

## Dataset Description

- **Paper:** aeroBERT-Classifier: Classification of Aerospace Requirements using BERT
- **Point of Contact:** archanatikayatray@gmail.com

### Dataset Summary

This dataset contains requirements from the aerospace domain. The requirements are tagged based on the "type"/category of requirement they belong to.
The creation of this dataset is aimed at -  <br> 
(1) Making available an **open-source** dataset for aerospace requirements which are often proprietary <br> 
(2) Fine-tuning language models for **requirements classification** specific to the aerospace domain <br> 

This dataset can be used for training or fine-tuning language models for the identification of the following types of requirements - <br> 
<br> 
**Design Requirement** - Dictates "how" a system should be designed given certain technical standards and specifications; 
**Example:** Trim control systems must be designed to prevent creeping in flight.<br> 
<br> 
**Functional Requirement** - Defines the functions that need to be performed by a system in order to accomplish the desired system functionality; 
**Example:** Each cockpit voice recorder shall record the voice communications of flight crew members on the flight deck.<br> 
<br> 
**Performance Requirement** - Defines "how well" a system needs to perform a certain function; 
**Example:** The airplane must be free from flutter, control reversal, and divergence for any configuration and condition of operation.<br> 

## Dataset Structure

The tagging scheme followed: <br> 
(1) Design requirements: 0 (Count = 149) <br> 
(2) Functional requirements: 1 (Count = 99) <br> 
(3) Performance requirements: 2 (Count = 62) <br> 
<br> 

The dataset is of the format: ``requirements | label`` <br>

| requirements      | label   |                    
| :----:        |    :----:              |                            
| Each cockpit voice recorder shall record voice communications transmitted from or received in the airplane by radio.| 1 | 
| Each recorder container must be either bright orange or bright yellow.| 0     | 
| Single-engine airplanes, not certified for aerobatics, must not have a tendency to inadvertently depart controlled flight.    | 2| 
| Each part of the airplane must have adequate provisions for ventilation and drainage. | 0   | 
| Each baggage and cargo compartment must have a means to prevent the contents of the compartment from becoming a hazard by impacting occupants or shifting.     | 1      | 

## Dataset Creation

### Source Data

A total of 325 aerospace requirements were collected from Parts 23 and 25 of Title 14 of the Code of Federal Regulations (CFRs) and annotated (refer to the paper for more details). <br> 

### Importing dataset into Python environment 

Use the following code chunk to import the dataset into Python environment as a DataFrame. 

```
from datasets import load_dataset
import pandas as pd

dataset = load_dataset("archanatikayatray/aeroBERT-classification")

#Converting the dataset into a pandas DataFrame
dataset = pd.DataFrame(dataset["train"]["text"])
dataset = dataset[0].str.split('*', expand = True)

#Getting the headers from the first row
header = dataset.iloc[0]

#Excluding the first row since it contains the headers
dataset = dataset[1:]

#Assigning the header to the DataFrame
dataset.columns = header

#Viewing the last 10 rows of the annotated dataset
dataset.tail(10)

```


### Annotations

#### Annotation process

A Subject Matter Expert (SME) was consulted for deciding on the annotation categories for the requirements.

The final classification dataset had 149 Design requirements, 99 Functional requirements, and 62 Performance requirements.
Lastly, the 'labels' attached to the requirements (design requirement, functional requirement, and performance requirement) were converted into numeric values: 0, 1, and 2 respectively.

### Limitations

(1)The dataset is an imbalanced dataset (more Design requirements as compared to the other types). Hence, using ``Accuracy`` as a metric for the model performance is
NOT a good idea. The use of Precision, Recall, and F1 scores are suggested for model performance evaluation. 

(2)This dataset does not contain a test set. Hence, it is suggested that the user split the dataset into training/validation/testing after importing the data into a Python environment.
Please refer to the Appendix of the paper for information on the test set. 

### Citation Information

```
@Article{tikayatray_aeroBERT-C,
AUTHOR = {Tikayat Ray, Archana and Cole, Bjorn F. and Pinon Fischer, Olivia J. and White, Ryan T. and Mavris, Dimitri N.},
TITLE = {aeroBERT-Classifier: Classification of Aerospace Requirements Using BERT},
JOURNAL = {Aerospace},
VOLUME = {10},
YEAR = {2023},
NUMBER = {3},
ARTICLE-NUMBER = {279},
URL = {https://www.mdpi.com/2226-4310/10/3/279},
ISSN = {2226-4310},
DOI = {10.3390/aerospace10030279}
}

```