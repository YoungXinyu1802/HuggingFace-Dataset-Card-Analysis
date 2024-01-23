---
license: cc-by-4.0
---

# The Sentence Splitter (SS) for Clinical Cases Written in Spanish

## Introduction
This repository contains the sentence splitting model trained using the SPACCC_SPLIT corpus (https://github.com/PlanTL-SANIDAD/SPACCC_SPLIT). The model was trained using the 90% of the corpus (900 clinical cases) and tested against the 10% (100 clinical cases). This model is a great resource to split sentences in biomedical documents, specially clinical cases written in Spanish. This model obtains a F-Measure of 98.75%.

This model was created using the Apache OpenNLP machine learning toolkit (https://opennlp.apache.org/), with the release number 1.8.4, released in December 2017.

This repository contains the model, training set, testing set, Gold Standard, executable file, and the source code.

## Prerequisites
This software has been compiled with Java SE 1.8 and it should work with recent versions. You can download Java from the following website: https://www.java.com/en/download

The executable file already includes the Apache OpenNLP dependencies inside, so the download of this toolkit is not necessary. However, you may download the latest version from this website: https://opennlp.apache.org/download.html

The library file we have used to compile is "opennlp-tools-1.8.4.jar". The source code should be able to compile with the latest version of OpenNLP, "opennlp-tools-*RELEASE_NUMBER*.jar". In case there are compilation or execution errors, please let us know and we will make all the necessary updates.

## Directory structure
<pre>
exec/
  An executable file that can be used to apply the sentence splitter to your documents.
  You can find the notes about its execution below in section "Usage".

gold_standard/
  The clinical cases used as gold standard to evaluate the model's performance.

model/
  The sentence splitting model, "es-sentence-splitter-model-spaccc.bin", a binary file.

src/
  The source code to create the model (CreateModelSS.java) and evaluate it (EvaluateModelSS.java).
  The directory includes an example about how to use the model inside your code (SentenceSplitter.java).
  File "abbreviations.dat" contains a list of abbreviations, essential to build the model.

test_set/
  The clinical cases used as test set to evaluate the model's performance.

train_set/
  The clinical cases used to build the model. We use a single file with all documents present in
  directory "train_set_docs" concatented.

train_set_docs/
  The clinical cases used to build the model. For each record the sentences are already splitted.

</pre>

## Usage
The executable file *SentenceSplitter.jar* is the program you need to split the sentences of the document. For this program, two arguments are needed: (1) the text file to split the sentences, and (2) the model file (*es-sentence-splitter-model-spaccc.bin*). The program will display all sentences splitted in the terminal, with one sentence per line.

From the `exec` folder, type the following command in your terminal:

<pre>
$ java -jar SentenceSplitter.jar INPUT_FILE MODEL_FILE
</pre>

## Examples

Assuming you have the executable file, the input file and the model file in the same directory:
<pre>
$ java -jar SentenceSplitter.jar file_with_sentences_not_splitted.txt es-sentence-splitter-model-spaccc.bin
</pre>

## Model creation
To create this sentence splitting model, we used the following training parameters (class *TrainingParameters* in OpenNLP) to get the best performance:
- Number of iterations: 4000.
- Cutoff parameter: 3.
- Trainer type parameter: *EventTrainer.EVENT_VALUE*.
- Algorithm: Maximum Entropy (*ModelType.MAXENT.name()*).

Meanwhile, we used the following parameters for the sentence split builder (class *SentenceDetectorFactory* in OpenNLP) to get the best performance:
- Subclass name: null value.
- Language code: *es* (for Spanish).
- Use token end: true.
- Abbreviation dictionary: file "abbreviations.dat" (included in the `src/` directory).
- End of file characters: ".", "?" and "!".

## Model evaluation

After tuning the model using different values for each parameter mentioned above, we got the best performance with the values mentioned above.

|      | Value |
| ----------------------------------------: | :------ |
| Number of sentences in the gold standard | 1445   |
| Number of sentences generated            | 1447   |
| Number of sentences correctly splitted   | 1428   |
| Number of sentences wrongly splitted     | 12     |
| Number of sentences missed     | 5     |
| **Precision**                                | **98.69%** |
| **Recall**                                   | **98.82%** |
| **F-Measure**                                | **98.75%**|

Table 1: Evaluation statistics for the sentence splitting model.


## Contact

Ander Intxaurrondo (ander.intxaurrondo@bsc.es)


## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

Copyright (c) 2018 Secretaría de Estado para el Avance Digital (SEAD)
