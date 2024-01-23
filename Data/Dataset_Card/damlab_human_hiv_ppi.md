---
license: mit
---

# Dataset Description 


## Dataset Summary

This dataset was parsed from the Human-HIV Interaction dataset maintained by the NCBI. 
It contains a >16,000 pairs of interactions between HIV and Human proteins.
Sequences of the interacting proteins were retrieved from the NCBI protein database and added to the dataset.
The raw data is available from the [NBCI FTP site](https://ftp.ncbi.nlm.nih.gov/gene/GeneRIF/hiv_interactions.gz) and the curation strategy is described in the [NAR Research paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4383939/) announcing the dataset. 

## Dataset Structure

### Data Instances

Data Fields: hiv_protein_product, hiv_protein_name, interaction_type, human_protein_product, human_protein_name, reference_list, description, hiv_protein_sequence, human_protein_sequence

Data Splits: None 
 
## Dataset Creation

Curation Rationale: This dataset was curated train models to recognize proteins that interact with HIV.

Initial Data Collection and Normalization: Dataset was downloaded and curated on 4/4/2022 but the most recent update of the underlying NCBI database was 2016. 

## Considerations for Using the Data

Discussion of Biases: This dataset of protein interactions was manually curated by experts utilizing published scientific literature.
This inherently biases the collection to well-studied proteins and known interactions.
The dataset does not contain _negative_ interactions.

## Additional Information: 
 - Dataset Curators: Will Dampier 
 - Citation Information: TBA