---
license: mit
---

# Dataset Description 


## Dataset Summary

This dataset was derived from the Stanford HIV Genotype-Phenotype database and contains 1,733 HIV protease sequences. A
pproximately half of the sequences are resistant to at least one antiretroviral therapeutic (ART).  

Supported Tasks and Leaderboards: None 

Languages: English 
 
## Dataset Structure

### Data Instances
Each column represents the protein amino acid sequence of the HIV protease protein. The ID field indicates the Genbank reference ID for future cross-referencing. There are 1,733 total protease sequences. 

Data Fields: ID, sequence, fold, FPV, IDV, NFV, SQV 

Data Splits: None 
 
## Dataset Creation

Curation Rationale: This dataset was curated to train a model (HIV-BERT-PI) designed to predict whether an HIV protease sequence would result in resistance to certain antiretroviral (ART) drugs. 

Initial Data Collection and Normalization: Dataset was downloaded and curated on 12/21/2021. 

## Considerations for Using the Data

Social Impact of Dataset: Due to the tendency of HIV to mutate, drug resistance is a common issue when attempting to treat those infected with HIV. 
Protease inhibitors are a class of drugs that HIV is known to develop resistance via mutations. 
Thus, by providing a collection of protease sequences known to be resistant to one or more drugs, this dataset provides a significant collection of data that could be utilized to perform computational analysis of protease resistance mutations. 

Discussion of Biases: Due to the sampling nature of this database, it is predominantly composed of subtype B sequences from North America and Europe with only minor contributions of Subtype C, A, and D. 
Currently, there was no effort made to balance the performance across these classes. 
As such, one should consider refinement with additional sequences to perform well on non-B sequences. 

## Additional Information: 
 - Dataset Curators: Will Dampier 
 - Citation Information: TBA
 

