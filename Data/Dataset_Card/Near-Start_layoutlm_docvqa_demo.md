---
license: openrail
---
dataset_info:
  features:
    - name: questionId
      dtype: int64
    - name: question
      dtype: string
    - name: image
      sequence:
        sequence:
          sequence:
            sequence: uint8
    - name: docId
      dtype: int64
    - name: ucsf_document_id
      dtype: string
    - name: ucsf_document_page_no
      dtype: string
    - name: answers
      sequence: string
    - name: data_split
      dtype: string
    - name: words
      sequence: string
    - name: boxes
      sequence:
        sequence: int64
  splits:
    - name: train
      num_bytes: 6387690838
      num_examples: 39463
    - name: val
      num_bytes: 869953677
      num_examples: 5349
    - name: test
      num_examples: 5188
  download_size: 2583317804
  dataset_size: 7257644515