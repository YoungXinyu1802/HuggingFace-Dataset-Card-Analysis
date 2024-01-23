This dataset is designed to support the reproduction of the results presented in ``DeepCC: Learning to Complete Code via Multiple Context Channels with Multiple Pre-training Objectives''. The dataset includes all the necessary data and codes to reproduce the experiments.

Data:

The dataset contains all the raw data used in the experiments:
- Raw dataset: The original Py150 dataset can be accessed here: https://www.sri.inf.ethz.ch/py150.
  
- DeepCC Processed Dataset:
- DeepCC pre-training dataset can be located in the pretrain_ds folder
- DeepCC fine-tuning dataset can be located in the finetune_ds folder
- DeepCC evaluation dataset can be located in the eval_ds folder

Code:

The dataset also includes all the code used in the experiments:

Dataset preprocessing scripts - The script to preprocess the input channels is located in the DeepCC_Preprocessing.ipynb file.

Training and evaluation scripts - The code to build the DeepCC model is found in DeepCC.ipynb file. Our tokenizer is also included in the tokenizer.zip file. 

Baseline comparison scripts - You can find the script we used to compare with other baseline models in the baseline_comparison.ipynb file.


Instructions to train the model:

1. Clone the repository to your local machine,
2. Open the DeepCC.ipynb notebook,
3. Correct the dataset directory path,
4. Run each notebook one by one until pre-training/fine-tuning. Evaluation scripts are also included in the same notebook.
