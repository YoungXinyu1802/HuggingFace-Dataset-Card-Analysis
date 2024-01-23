---
annotations_creators:
- other
language_creators:
- found
language:
- en
license:
- mit
multilinguality:
- monolingual
pretty_name: Slither Audited Smart Contracts
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- text-classification
- text-generation
task_ids:
- multi-label-classification
- multi-input-text-classification
- language-modeling
---

# Dataset Card for Slither Audited Smart Contracts

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://github.com/mwritescode/slither-audited-smart-contracts
- **Repository:** https://github.com/mwritescode/slither-audited-smart-contracts
- **Point of Contact:** [Martina Rossini](mailto:martina.rossini704@gmail.com)

### Dataset Summary

This dataset contains source code and deployed bytecode for Solidity Smart Contracts that have been verified on Etherscan.io, along with a classification of their vulnerabilities according to the Slither static analysis framework.

### Supported Tasks and Leaderboards

- `text-classification`: The dataset can be used to train a model for both binary and multilabel text classification on smart contracts bytecode and source code. The model performance is evaluated based on the accuracy of the predicted labels as compared to the given labels in the dataset.
- `text-generation`: The dataset can also be used to train a language model for the Solidity programming language
- `image-classification`: By pre-processing the bytecode data to obtain RGB images, the dataset can also be used to train convolutional neural networks for code vulnerability detection and classification.

### Languages

The language annotations are in English, while all the source codes are in Solidity.

## Dataset Structure

### Data Instances

Each data instance contains the following features: `address`, `source_code` and `bytecode`. The label comes in two configuration, either a plain-text cleaned up version of the output given by the Slither tool or a multi-label version, which consists in a simple list of integers, each one representing a particular vulnerability class. Label 4 indicates that the contract is safe.

An example from a plain-text configuration looks as follows:
```
{
'address': '0x006699d34AA3013605d468d2755A2Fe59A16B12B'
'source_code': 'pragma solidity 0.5.4; interface IERC20 { function balanceOf(address account) external ...'
'bytecode': '0x608060405234801561001057600080fd5b5060043610610202576000357c0100000000000000000000000000000000000000000000000000000000900...'
'slither': '{"success": true, "error": null, "results": {"detectors": [{"check": "divide-before-multiply", "impact": "Medium", "confidence": "Medium"}]}}'
}
```

An example from a multi-label configuration looks as follows:
```
{
'address': '0x006699d34AA3013605d468d2755A2Fe59A16B12B'
'source_code': 'pragma solidity 0.5.4; interface IERC20 { function balanceOf(address account) external ...'
'bytecode': '0x608060405234801561001057600080fd5b5060043610610202576000357c0100000000000000000000000000000000000000000000000000000000900...'
'slither': [ 4 ]
}
```

### Data Fields

- `address`: a string representing the address of the smart contract deployed on the Ethereum main net
- `source_code`: a flattened version of the smart contract codebase in Solidity
- `bytecode`: a string representing the smart contract's bytecode, obtained when calling `web3.eth.getCode()`. Note that in some cases where this was not available, the string is simply '0x'.
- `slither`: either a cleaned up version of Slither's JSON output or a list of class labels

### Data Splits

The dataset comes in 6 configurations and train, test and validation splits are only provided for those configurations that do not include `all-` in their names. Test and Validation splits are both about 15% of the total.

## Dataset Creation

### Curation Rationale

slither-audited-smart-contracts was built to provide a freely available large scale dataset for vulnerability detection and classification on verified Solidity smart contracts. Indeed, the biggest open source dataset for this task at the moment of writing is [SmartBugs Wild](https://github.com/smartbugs/smartbugs-wild), containing 47,398 smart contracts that were labeled with 9 tools withing the SmartBugs framework. 

### Source Data

#### Initial Data Collection and Normalization

The dataset was constructed started from the list of verified smart contracts provided at [Smart Contract Sanctuary](https://github.com/tintinweb/smart-contract-sanctuary-ethereum). Then, smart contract source code was either downloaded from the aforementioned repo or downloaded via [Etherscan](https://etherscan.io/apis) and flattened using the Slither contract flattener. The bytecode was downloaded using the Web3.py library, in particular the `web3.eth.getCode()` function and using [INFURA](https://infura.io/) as our endpoint.
Finally, every smart contract was analyzed using the [Slither](https://github.com/crytic/slither) static analysis framework. The tool found 38 different vulnerability classes in the collected contracts and they were then mapped to 9 labels according to what is shown in the file `label_mappings.json`. These mappings were derived by following the guidelines at [Decentralized Application Security Project (DASP)](https://www.dasp.co/) and at [Smart Contract Weakness Classification Registry](https://swcregistry.io/). They were also inspired by the mappings used for Slither's detection by the team that labeled the SmartBugs Wild dataset, which can be found [here](https://github.com/smartbugs/smartbugs-results/blob/master/metadata/vulnerabilities_mapping.cs).

## Additional Information

### Dataset Curators

The dataset was initially created by Martina Rossini during work done for the project of the course Blockchain and Cryptocurrencies of the University of Bologna (Italy). 

### Licensing Information

The license in the file LICENSE applies to all the files in this repository, except for the Solidity source code of the contracts. These are still publicly available, were obtained using the Etherscan APIs, and retain their original licenses.

### Citation Information

If you are using this dataset in your research and paper, here's how you can cite it:

```
@misc{rossini2022slitherauditedcontracts,
    title = {Slither Audited Smart Contracts Dataset},
    author={Martina Rossini},
    year={2022}
}
```

### Contributions
Thanks to [@mwritescode](https://github.com/mwritescode) for adding this dataset.