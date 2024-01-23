# Dataset Description 


## Dataset Summary

 This dataset was derived from the Los Alamos National Laboratory HIV sequence (LANL) database.
 It contains the most recent version (2016-Full-genome), composed of 1,609 high-quality full-length genomes.
 The genes within these sequences were processed using the GeneCutter tool and translated into corresponding amino acid sequences using the BioPython library Seq.translate function. 

Supported Tasks and Leaderboards: None 

Languages: English 
 
## Dataset Structure

### Data Instances
Each column represents the protein amino acid sequence of the HIV genome. 
The ID field indicates the Genbank reference ID for future cross-referencing. 
There are 1,609 full length HIV genomes. 

Data Fields: ID, gag, pol, env, nef, tat, rev, proteome 

Data Splits: None 
 
## Dataset Creation

Curation Rationale: This dataset was curated to train a model (HIV-BERT) designed to predict a variety of sequence-dependent features regarding HIV.  

Initial Data Collection and Normalization: Dataset was downloaded and curated on 12/21/2021. 

## Considerations for Using the Data

Social Impact of Dataset: This dataset can be used to study sequence-dependent features of HIV, a virus that has claimed the lives of many individuals globally in the last few decades.  

Discussion of Biases: This dataset was derived from the Los Alamos National Laboratory HIV sequence (LANL) database full genome database and contains a representative sample from each subtype and geographic region. 

## Additional Information: 
 - Dataset Curators: Will Dampier 
 - Citation Information: TBA