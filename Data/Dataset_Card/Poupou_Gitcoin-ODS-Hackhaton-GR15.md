---
annotations_creators:
- no-annotation
language:
- en
language_creators: 
- expert-generated
license:
- mit
multilinguality:
- monolingual
pretty_name: Gitcoin FDD Open Data Science Hackathon GR15
size_categories:
- 1M<n<10M
source_datasets:
- original
tags:
- Gitcoin
- Gitcoin Grants
- Sybil
- Sybil Slayers
- FDD
- Web3
- Public Goods
- Fraud Detection
- DAO
- Ethereum
- Polygon
task_categories:
- feature-extraction
task_ids: []
---

# Dataset Card for [Gitcoin ODS Hackathon GR15]

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
- [Dataset Creation](#dataset-creation)
  - [Source Data](#source-data)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://gitcoin.co/issue/29389
- **Repository:** https://github.com/poupou-web3/GC-ODS-Sybil
- **Point of Contact:** https://discord.com/channels/562828676480237578/1024788324826763284

### Dataset Summary

This data set was created in the context of the first [Gitcoin Open Data Science Hackathon](https://go.gitcoin.co/blog/open-data-science-hackathon).
It contains all the transactions on the Ethereum and Polygon chains of the wallet that contributed to the Grant 15 of Gitcoin grants program.
It was created in order to find patterns in the transactions of potential Sybil attackers by exploring their on-chain activity.

## Dataset Creation

### Source Data

The wallet address from grant 15 was extracted from the data put together by the Gitcoin DAO. [GR_15_DATA](https://drive.google.com/drive/folders/17OdrV7SA0I56aDMwqxB6jMwoY3tjSf5w)

The data was produced using [Etherscan API](https://etherscan.io/) and [PolygonScan API](https://polygonscan.com/) and using scripts available later at [repo](https://github.com/poupou-web3/GC-ODS-Sybil).

An address contributing to the [GR_15_DATA](https://drive.google.com/drive/folders/17OdrV7SA0I56aDMwqxB6jMwoY3tjSf5w) with no found transaction on a chain will not appear in the data gathered.

** Careful the transaction data only contains "normal" transactions as described by the API provider.**

## Dataset Structure

### Data Instances

There are 4 CSV files.
- 2 for transactions: one for the Ethereum transactions and one for the Polygon transactions.
- 2 for features: one for the Ethereum transactions and one for the Polygon transactions.

### Data Fields

As provided by the [Etherscan API](https://etherscan.io/) and [PolygonScan API](https://polygonscan.com/).
A column address was added for easier manipulation and to have all the transactions of all addresses in the same file.

It is an unsupervised machine-learning task, there is no target column.

Most of the extracted features have been extracted using [tsfresh](https://tsfresh.readthedocs.io/en/latest/). The code is available in the GitHub [repo](https://github.com/poupou-web3/GC-ODS-Sybil). It allows reproducing the extraction from the 2 transactions CSV. Column names are named by tsfresh, each feature can be found in the documentation for more detailed definitions. Following are the descriptions for features not explained in by tsfresh:
- countUniqueInteracted : Count the number of unique addresses with which the wallet address has interacted.
- countTx: The total number of transactions
- ratioUniqueInteracted : countUniqueInteracted / countTx
- outgoing: Number of outgoing transactions
- outgoingRatio : outgoing / countTx

## Considerations for Using the Data

### Social Impact of Dataset

The creation of the data set may help in fraud detection and defence in public goods funding.

## Additional Information


### Licensing Information

MIT

### Citation Information

Please cite this data set if you use it, especially in the hackathon context.

### Contributions

Thanks to [@poupou-web3](https://github.com/poupou-web3) for adding this dataset.