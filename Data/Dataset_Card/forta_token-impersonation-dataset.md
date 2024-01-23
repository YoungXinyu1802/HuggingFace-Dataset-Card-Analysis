---
license: mit
---
# Token Impersonation Dataset

This dataset contains 375 erc-like token impersonation contracts used for phishing scams and 85,716 legitimate Etherscan verified contracts.

The dataset includes the following data attributes:

* contract_address: smart contract address on Ethereum
* contract_creation_tx: smart contract deployment tx
* malicious: boolean flag whether a contract is a token impersonation contract or not
* creation_bytecode: smart contract bytecode that includes both contract initialization and execution code
* contract_creator_etherscan_label: contract creator's Etherscan label
* decompiled_opcodes: bytecode decompiled into EVM opcodes
* contract_tag: contract's Etherscan wallet tag
* contract_creator_tag: contract creator's Etherscan wallet tag
