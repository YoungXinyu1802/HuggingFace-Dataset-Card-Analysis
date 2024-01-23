---
language:
- nl
license: cc-by-sa-4.0
license_details: https://github.com/UniversalDependencies/UD_Dutch-Alpino/blob/master/LICENSE.txt
pretty_name: UD_Dutch_Alpino
size_categories:
- 10K<100K
task_categories:
- token-classification
task_ids:
- parsing
paperswithcode_id: universal-dependencies
dataset_info:
- config_name: '2.11'
  features:
  - name: idx
    dtype: string
  - name: text
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: upos
    sequence:
      class_label:
        names:
          '0': NOUN
          '1': PUNCT
          '2': ADP
          '3': NUM
          '4': SYM
          '5': SCONJ
          '6': ADJ
          '7': PART
          '8': DET
          '9': CCONJ
          '10': PROPN
          '11': PRON
          '12': X
          '13': _
          '14': ADV
          '15': INTJ
          '16': VERB
          '17': AUX
  - name: xpos
    sequence: string
  - name: feats
    sequence: string
  - name: head
    sequence: string
  - name: deprel
    sequence: string
  - name: deps
    sequence: string
  - name: misc
    sequence: string
  splits:
  - name: train
    num_bytes: 22519230
    num_examples: 12289
  - name: validation
    num_bytes: 1411214
    num_examples: 718
  - name: test
    num_bytes: 1355617
    num_examples: 596
  download_size: 16754680
  dataset_size: 25286061
- config_name: '2.10'
  features:
  - name: idx
    dtype: string
  - name: text
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: upos
    sequence:
      class_label:
        names:
          '0': NOUN
          '1': PUNCT
          '2': ADP
          '3': NUM
          '4': SYM
          '5': SCONJ
          '6': ADJ
          '7': PART
          '8': DET
          '9': CCONJ
          '10': PROPN
          '11': PRON
          '12': X
          '13': _
          '14': ADV
          '15': INTJ
          '16': VERB
          '17': AUX
  - name: xpos
    sequence: string
  - name: feats
    sequence: string
  - name: head
    sequence: string
  - name: deprel
    sequence: string
  - name: deps
    sequence: string
  - name: misc
    sequence: string
  splits:
  - name: train
    num_bytes: 22519230
    num_examples: 12289
  - name: validation
    num_bytes: 1411214
    num_examples: 718
  - name: test
    num_bytes: 1355617
    num_examples: 596
  download_size: 16754680
  dataset_size: 25286061
- config_name: '2.9'
  features:
  - name: idx
    dtype: string
  - name: text
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: upos
    sequence:
      class_label:
        names:
          '0': NOUN
          '1': PUNCT
          '2': ADP
          '3': NUM
          '4': SYM
          '5': SCONJ
          '6': ADJ
          '7': PART
          '8': DET
          '9': CCONJ
          '10': PROPN
          '11': PRON
          '12': X
          '13': _
          '14': ADV
          '15': INTJ
          '16': VERB
          '17': AUX
  - name: xpos
    sequence: string
  - name: feats
    sequence: string
  - name: head
    sequence: string
  - name: deprel
    sequence: string
  - name: deps
    sequence: string
  - name: misc
    sequence: string
  splits:
  - name: train
    num_bytes: 22519230
    num_examples: 12289
  - name: validation
    num_bytes: 1411214
    num_examples: 718
  - name: test
    num_bytes: 1355617
    num_examples: 596
  download_size: 16754680
  dataset_size: 25286061
- config_name: '2.8'
  features:
  - name: idx
    dtype: string
  - name: text
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: upos
    sequence:
      class_label:
        names:
          '0': NOUN
          '1': PUNCT
          '2': ADP
          '3': NUM
          '4': SYM
          '5': SCONJ
          '6': ADJ
          '7': PART
          '8': DET
          '9': CCONJ
          '10': PROPN
          '11': PRON
          '12': X
          '13': _
          '14': ADV
          '15': INTJ
          '16': VERB
          '17': AUX
  - name: xpos
    sequence: string
  - name: feats
    sequence: string
  - name: head
    sequence: string
  - name: deprel
    sequence: string
  - name: deps
    sequence: string
  - name: misc
    sequence: string
  splits:
  - name: train
    num_bytes: 22519220
    num_examples: 12289
  - name: validation
    num_bytes: 1411214
    num_examples: 718
  - name: test
    num_bytes: 1355617
    num_examples: 596
  download_size: 16754670
  dataset_size: 25286051
- config_name: '2.7'
  features:
  - name: idx
    dtype: string
  - name: text
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: upos
    sequence:
      class_label:
        names:
          '0': NOUN
          '1': PUNCT
          '2': ADP
          '3': NUM
          '4': SYM
          '5': SCONJ
          '6': ADJ
          '7': PART
          '8': DET
          '9': CCONJ
          '10': PROPN
          '11': PRON
          '12': X
          '13': _
          '14': ADV
          '15': INTJ
          '16': VERB
          '17': AUX
  - name: xpos
    sequence: string
  - name: feats
    sequence: string
  - name: head
    sequence: string
  - name: deprel
    sequence: string
  - name: deps
    sequence: string
  - name: misc
    sequence: string
  splits:
  - name: train
    num_bytes: 22503798
    num_examples: 12264
  - name: validation
    num_bytes: 1411177
    num_examples: 718
  - name: test
    num_bytes: 1354832
    num_examples: 596
  download_size: 16858557
  dataset_size: 25269807
- config_name: '2.6'
  features:
  - name: idx
    dtype: string
  - name: text
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: upos
    sequence:
      class_label:
        names:
          '0': NOUN
          '1': PUNCT
          '2': ADP
          '3': NUM
          '4': SYM
          '5': SCONJ
          '6': ADJ
          '7': PART
          '8': DET
          '9': CCONJ
          '10': PROPN
          '11': PRON
          '12': X
          '13': _
          '14': ADV
          '15': INTJ
          '16': VERB
          '17': AUX
  - name: xpos
    sequence: string
  - name: feats
    sequence: string
  - name: head
    sequence: string
  - name: deprel
    sequence: string
  - name: deps
    sequence: string
  - name: misc
    sequence: string
  splits:
  - name: train
    num_bytes: 22503798
    num_examples: 12264
  - name: validation
    num_bytes: 1411177
    num_examples: 718
  - name: test
    num_bytes: 1354832
    num_examples: 596
  download_size: 16858557
  dataset_size: 25269807
- config_name: '2.5'
  features:
  - name: idx
    dtype: string
  - name: text
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: upos
    sequence:
      class_label:
        names:
          '0': NOUN
          '1': PUNCT
          '2': ADP
          '3': NUM
          '4': SYM
          '5': SCONJ
          '6': ADJ
          '7': PART
          '8': DET
          '9': CCONJ
          '10': PROPN
          '11': PRON
          '12': X
          '13': _
          '14': ADV
          '15': INTJ
          '16': VERB
          '17': AUX
  - name: xpos
    sequence: string
  - name: feats
    sequence: string
  - name: head
    sequence: string
  - name: deprel
    sequence: string
  - name: deps
    sequence: string
  - name: misc
    sequence: string
  splits:
  - name: train
    num_bytes: 22503798
    num_examples: 12264
  - name: validation
    num_bytes: 1411177
    num_examples: 718
  - name: test
    num_bytes: 1354832
    num_examples: 596
  download_size: 16858557
  dataset_size: 25269807
- config_name: '2.4'
  features:
  - name: idx
    dtype: string
  - name: text
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: upos
    sequence:
      class_label:
        names:
          '0': NOUN
          '1': PUNCT
          '2': ADP
          '3': NUM
          '4': SYM
          '5': SCONJ
          '6': ADJ
          '7': PART
          '8': DET
          '9': CCONJ
          '10': PROPN
          '11': PRON
          '12': X
          '13': _
          '14': ADV
          '15': INTJ
          '16': VERB
          '17': AUX
  - name: xpos
    sequence: string
  - name: feats
    sequence: string
  - name: head
    sequence: string
  - name: deprel
    sequence: string
  - name: deps
    sequence: string
  - name: misc
    sequence: string
  splits:
  - name: train
    num_bytes: 22609064
    num_examples: 12269
  - name: validation
    num_bytes: 1418698
    num_examples: 718
  - name: test
    num_bytes: 1361104
    num_examples: 596
  download_size: 16599224
  dataset_size: 25388866
- config_name: '2.3'
  features:
  - name: idx
    dtype: string
  - name: text
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: upos
    sequence:
      class_label:
        names:
          '0': NOUN
          '1': PUNCT
          '2': ADP
          '3': NUM
          '4': SYM
          '5': SCONJ
          '6': ADJ
          '7': PART
          '8': DET
          '9': CCONJ
          '10': PROPN
          '11': PRON
          '12': X
          '13': _
          '14': ADV
          '15': INTJ
          '16': VERB
          '17': AUX
  - name: xpos
    sequence: string
  - name: feats
    sequence: string
  - name: head
    sequence: string
  - name: deprel
    sequence: string
  - name: deps
    sequence: string
  - name: misc
    sequence: string
  splits:
  - name: train
    num_bytes: 22660621
    num_examples: 12269
  - name: validation
    num_bytes: 1421846
    num_examples: 718
  - name: test
    num_bytes: 1363777
    num_examples: 596
  download_size: 16122348
  dataset_size: 25446244
- config_name: '2.2'
  features:
  - name: idx
    dtype: string
  - name: text
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: upos
    sequence:
      class_label:
        names:
          '0': NOUN
          '1': PUNCT
          '2': ADP
          '3': NUM
          '4': SYM
          '5': SCONJ
          '6': ADJ
          '7': PART
          '8': DET
          '9': CCONJ
          '10': PROPN
          '11': PRON
          '12': X
          '13': _
          '14': ADV
          '15': INTJ
          '16': VERB
          '17': AUX
  - name: xpos
    sequence: string
  - name: feats
    sequence: string
  - name: head
    sequence: string
  - name: deprel
    sequence: string
  - name: deps
    sequence: string
  - name: misc
    sequence: string
  splits:
  - name: train
    num_bytes: 22561306
    num_examples: 12269
  - name: validation
    num_bytes: 1416707
    num_examples: 718
  - name: test
    num_bytes: 1356357
    num_examples: 596
  download_size: 16021555
  dataset_size: 25334370
- config_name: '2.1'
  features:
  - name: idx
    dtype: string
  - name: text
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: upos
    sequence:
      class_label:
        names:
          '0': NOUN
          '1': PUNCT
          '2': ADP
          '3': NUM
          '4': SYM
          '5': SCONJ
          '6': ADJ
          '7': PART
          '8': DET
          '9': CCONJ
          '10': PROPN
          '11': PRON
          '12': X
          '13': _
          '14': ADV
          '15': INTJ
          '16': VERB
          '17': AUX
  - name: xpos
    sequence: string
  - name: feats
    sequence: string
  - name: head
    sequence: string
  - name: deprel
    sequence: string
  - name: deps
    sequence: string
  - name: misc
    sequence: string
  splits:
  - name: train
    num_bytes: 20558599
    num_examples: 12269
  - name: validation
    num_bytes: 1296724
    num_examples: 718
  - name: test
    num_bytes: 1239703
    num_examples: 596
  download_size: 14669029
  dataset_size: 23095026
- config_name: '2.0'
  features:
  - name: idx
    dtype: string
  - name: text
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: upos
    sequence:
      class_label:
        names:
          '0': NOUN
          '1': PUNCT
          '2': ADP
          '3': NUM
          '4': SYM
          '5': SCONJ
          '6': ADJ
          '7': PART
          '8': DET
          '9': CCONJ
          '10': PROPN
          '11': PRON
          '12': X
          '13': _
          '14': ADV
          '15': INTJ
          '16': VERB
          '17': AUX
  - name: xpos
    sequence: string
  - name: feats
    sequence: string
  - name: head
    sequence: string
  - name: deprel
    sequence: string
  - name: deps
    sequence: string
  - name: misc
    sequence: string
  splits:
  - name: train
    num_bytes: 23149433
    num_examples: 12330
  - name: validation
    num_bytes: 1413638
    num_examples: 720
  - name: test
    num_bytes: 1418560
    num_examples: 685
  download_size: 16953990
  dataset_size: 25981631
---
# Universal Dependencies for Dutch: Alpino

All original data can be found on [Github](https://github.com/UniversalDependencies/UD_Dutch-Alpino).

> This corpus consists of samples from various treebanks annotated at the University of Groningen using the Alpino annotation tools and guidelines.

This `datasets` implementation contains all current UDv2 releases. If a new release is missing, feel free to [shoot a message](https://twitter.com/BramVanroy) or post an issue via the Community tab!

# Acknowledegments

The dataset script of this dataset borrows _heavily_ from the [`universal_dependencies`](https://huggingface.co/datasets/universal_dependencies) dataset.