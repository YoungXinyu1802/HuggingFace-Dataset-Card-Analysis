# Dataset Description 


## Dataset Summary

This dataset was derived from the Los Alamos National Laboratory HIV sequence (LANL) database. 
It contains 2,935 HIV V3 loop protein sequences, which can interact with either CCR5 receptors on T-Cells or CXCR4 receptors on macrophages. 

Supported Tasks and Leaderboards: None 

Languages: English 
 
## Dataset Structure

### Data Instances
Data Instances: Each column represents the protein amino acid sequence of the HIV V3 loop. 
The ID field indicates the Genbank reference ID for future cross-referencing. 
There are 2,935 total V3 sequences, with 91% being CCR5 tropic and 23% CXCR4 tropic. 
Data Fields: ID, sequence, fold, CCR5, CXCR4 
Data Splits: None 
 
## Dataset Creation

Curation Rationale: This dataset was curated to train a model (HIV-BERT-V3) designed to predict whether an HIV V3 loop would be CCR5 or CXCR4 tropic. 

Initial Data Collection and Normalization: Dataset was downloaded and curated on 12/20/2021.  

## Considerations for Using the Data

Social Impact of Dataset: This dataset can be used to study the mechanism by which HIV V3 loops allow for entry into T-cells and macrophages. 

Discussion of Biases: Due to the sampling nature of this database, it is predominantly composed of subtype B sequences from North America and Europe with only minor contributions of Subtype C, A, and D. 
Currently, there was no effort made to balance the performance across these classes. 
As such, one should consider refinement with additional sequences to perform well on non-B sequences. 

## Additional Information: 
 - Dataset Curators: Will Dampier 
 - Citation Information: TBA
