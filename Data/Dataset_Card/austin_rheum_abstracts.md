# Dataset Card for Rheumatology Abstracts
## Data Source
This dataset comes from PubMed, derived from my fork of the pymed package (no longer maintained). My fork can be found at https://github.com/cmcmaster1/pymed

## Data Structure
The dataset is split into train (80%) and test (20%) files (CSV). Each file contains three columns:
- id
- abstract (minus conclusion)
- conclusion