dataset_info:
  features:
  - name: id
    dtype: string
  - name: post_text
    sequence: string
  - name: pre_text
    sequence: string
  - name: question
    dtype: string
  - name: answers
    dtype: string
  - name: table
    sequence:
      sequence: string
  splits:
  - name: train
    num_bytes: 26984130
    num_examples: 6251
  - name: validation
    num_bytes: 3757103
    num_examples: 883
  - name: test
    num_bytes: 4838430
    num_examples: 1147
  download_size: 21240722
  dataset_size: 35579663
