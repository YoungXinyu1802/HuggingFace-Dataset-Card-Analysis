---
language:
- nl
license: cc-by-sa-4.0
license_details: https://github.com/UniversalDependencies/UD_Dutch-LassySmall/blob/master/LICENSE.txt
pretty_name: UD_Dutch_LassySmall
size_categories:
- 1K<10K
task_categories:
- token-classification
task_ids:
- parsing
paperswithcode_id: universal-dependencies
dataset_info:
- config_name: r2.11
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
    num_bytes: 9009482
    num_examples: 5789
  - name: validation
    num_bytes: 1360729
    num_examples: 676
  - name: test
    num_bytes: 1393802
    num_examples: 876
  download_size: 7979339
  dataset_size: 11764013
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
    num_bytes: 9009482
    num_examples: 5789
  - name: validation
    num_bytes: 1360729
    num_examples: 676
  - name: test
    num_bytes: 1393802
    num_examples: 876
  download_size: 7979339
  dataset_size: 11764013
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
    num_bytes: 9009482
    num_examples: 5789
  - name: validation
    num_bytes: 1360729
    num_examples: 676
  - name: test
    num_bytes: 1393802
    num_examples: 876
  download_size: 7979339
  dataset_size: 11764013
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
    num_bytes: 9009482
    num_examples: 5789
  - name: validation
    num_bytes: 1360729
    num_examples: 676
  - name: test
    num_bytes: 1393802
    num_examples: 876
  download_size: 7979339
  dataset_size: 11764013
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
    num_bytes: 9009488
    num_examples: 5789
  - name: validation
    num_bytes: 1360729
    num_examples: 676
  - name: test
    num_bytes: 1393802
    num_examples: 876
  download_size: 7979345
  dataset_size: 11764019
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
    num_bytes: 9001538
    num_examples: 5787
  - name: validation
    num_bytes: 1361476
    num_examples: 676
  - name: test
    num_bytes: 1391060
    num_examples: 875
  download_size: 8034396
  dataset_size: 11754074
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
    num_bytes: 9001538
    num_examples: 5787
  - name: validation
    num_bytes: 1361476
    num_examples: 676
  - name: test
    num_bytes: 1391060
    num_examples: 875
  download_size: 8034396
  dataset_size: 11754074
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
    num_bytes: 9001538
    num_examples: 5787
  - name: validation
    num_bytes: 1361476
    num_examples: 676
  - name: test
    num_bytes: 1391060
    num_examples: 875
  download_size: 8034396
  dataset_size: 11754074
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
    num_bytes: 9034318
    num_examples: 5789
  - name: validation
    num_bytes: 1364902
    num_examples: 676
  - name: test
    num_bytes: 1397290
    num_examples: 876
  download_size: 7460170
  dataset_size: 11796510
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
    num_bytes: 9034318
    num_examples: 5789
  - name: validation
    num_bytes: 1364902
    num_examples: 676
  - name: test
    num_bytes: 1397290
    num_examples: 876
  download_size: 7460170
  dataset_size: 11796510
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
    num_bytes: 9009825
    num_examples: 5789
  - name: validation
    num_bytes: 1358969
    num_examples: 676
  - name: test
    num_bytes: 1390320
    num_examples: 876
  download_size: 7435311
  dataset_size: 11759114
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
    num_bytes: 8890996
    num_examples: 6041
  - name: validation
    num_bytes: 1156488
    num_examples: 800
  - name: test
    num_bytes: 1109195
    num_examples: 800
  download_size: 7086385
  dataset_size: 11156679
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
    num_bytes: 7635936
    num_examples: 6041
  - name: validation
    num_bytes: 992236
    num_examples: 800
  - name: test
    num_bytes: 951839
    num_examples: 800
  download_size: 5605504
  dataset_size: 9580011
---
# Universal Dependencies for Dutch: Lassy Small

All original data can be found on [Github](https://github.com/UniversalDependencies/UD_Dutch-LassySmall).

> This corpus contains sentences from the Wikipedia section of the Lassy Small Treebank.
> Universal Dependency annotation was generated automatically from the original annotation in Lassy.

This `datasets` implementation contains all current UDv2 releases. If a new release is missing, feel free to [shoot a message](https://twitter.com/BramVanroy) or post an issue via the Community tab!

# Acknowledegments

The dataset script of this dataset borrows _heavily_ from the [`universal_dependencies`](https://huggingface.co/datasets/universal_dependencies) dataset.
