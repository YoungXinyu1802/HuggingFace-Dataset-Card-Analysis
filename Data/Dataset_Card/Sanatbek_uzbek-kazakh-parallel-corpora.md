# To download: 
- from datasets import load_dataset
- uz_dev = load_dataset("Sanatbek/uzbek-kazakh-parallel-corpora", split="train[:13373]")       (*10%*)
- uz_test = load_dataset("Sanatbek/uzbek-kazakh-parallel-corpora", split="train[13374:40120]") (*20%*)
- uz_train = load_dataset("Sanatbek/uzbek-kazakh-parallel-corpora", split="train[40121:]")     (*70%*)