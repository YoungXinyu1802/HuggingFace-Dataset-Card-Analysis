---
liscence: mit
---

# Dataset Description 


## Dataset Summary

This dataset is a mirror of the Uniprot/SwissProt database. It contains the names and sequences of >500K proteins. 

This dataset was parsed from the FASTA file at https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz.

Supported Tasks and Leaderboards: None 

Languages: English 
 
## Dataset Structure

### Data Instances

Data Fields: id, description, sequence

Data Splits: None 
 
## Dataset Creation

The dataset was downloaded and parsed into a `dataset` object and uploaded unchanged. 

Initial Data Collection and Normalization: Dataset was downloaded and curated on 03/09/2022. 

## Considerations for Using the Data

Social Impact of Dataset: Due to the tendency of HIV to mutate, drug resistance is a common issue when attempting to treat those infected with HIV. 
Protease inhibitors are a class of drugs that HIV is known to develop resistance via mutations. 
Thus, by providing a collection of protease sequences known to be resistant to one or more drugs, this dataset provides a significant collection of data that could be utilized to perform computational analysis of protease resistance mutations. 

Discussion of Biases: Due to the sampling nature of this database, it is predominantly composed genes from "well studied" genomes. This may impact the "broadness" of the genes contained. 

## Additional Information: 
 - Dataset Curators: Will Dampier 
 - Citation Information: TBA
 