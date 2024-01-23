---
license: mit
---

This repository is for the paper "Decomposing a Recurrent Neural Network into Modules for Enabling Reusability and Replacement". To use the data, there are two directories:

1. language datasets: Contains the necessary Tatoeba files used for the experiments. We have experimented with 4 languages(English, French, Italian and German).
2. language_models: Contains all trained language models and scripts to train them. It's organized in this way: language_models/{X}: contains language models for X, X={Vanilla RNN,LSTM,GRU}.

   language_models/{X}/motivating example models/problem1: Contains models needed to reproduce motivating example Problem 1.
   language_models/{X}/motivating example models/problem2: Contains models needed to reproduce motivating example Problem 2.
   language_models/{X}/reuse models: Contains combined models needed for reuse experiments.
   language_models/{X}/rq1 models: Contains all models needed for rq1.
   language_models/{X}/training script: Contains the training script to get the models.

   Note: To run the training scripts, direct the source path to /language datasets/Tatoeba/<name.txt> depending on the requirement.
   