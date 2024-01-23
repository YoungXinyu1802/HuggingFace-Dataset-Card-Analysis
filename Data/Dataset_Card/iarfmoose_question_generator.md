This dataset is made up of data taken from SQuAD v2.0, RACE, CoQA, and MSMARCO. Some examples have been filtered out of the original datasets and others have been modified.

There are two fields; question and text. The question field contains the question, and the text field contains both the answer and the context in the following format:
"\<answer> (answer text) \<context> (context text)"

The <answer> and <context> are included as special tokens in the question generator's tokenizer.

This dataset is intended to be used with the [question_generator repo](https://github.com/AMontgomerie/question_generator) to train the question generator model.
