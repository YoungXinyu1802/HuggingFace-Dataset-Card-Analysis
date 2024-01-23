# Dataset Description 


## Dataset Summary

This dataset was derived from the Los Alamos National Laboratory HIV sequence (LANL) database. 
It contains 5,510 unique V3 sequences, each annotated with its corresponding bodysite that it was associated with. 
Supported Tasks and Leaderboards: None 

Languages: English 
 
## Dataset Structure

### Data Instances
Data Instances: Each column represents the protein amino acid sequence of the HIV V3 loop. 
The ID field indicates the Genbank reference ID for future cross-referencing. 
There are 2,935 total V3 sequences, with 91% being CCR5 tropic and 23% CXCR4 tropic. 
Data Fields: ID, sequence, fold, periphery-tcell, periphery-monocyte, CNS, lung, breast-milk, gastric, male-genitals, female-genitals, umbilical-cord, organ
Data Splits: None 
 
## Dataset Creation

Curation Rationale: 

Initial Data Collection and Normalization: Dataset was downloaded and curated on 12/20/2021.  

## Considerations for Using the Data

Social Impact of Dataset: This dataset can be used to study the mechanism by which HIV V3 loops allow for study of HIV compartmentalization. 

Discussion of Biases: DDue to the sampling nature of this database, it is predominantly composed of subtype B sequences from North America and Europe with only minor contributions of Subtype C, A, and D. 
Currently, there was no effort made to balance the performance across these classes. 
As such, one should consider refinement with additional sequences to perform well on non-B sequences. 
Additionally, this dataset is highly biased to peripheral T-cells. 

## Additional Information: 
 - Dataset Curators: Will Dampier 
 - Citation Information: TBA


---
license: mit
---