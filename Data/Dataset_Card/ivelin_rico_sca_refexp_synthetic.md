---
license: apache-2.0
task_categories:
  - question-answering
language:
  - en
pretty_name: RICO SCA RefExp
size_categories:
  - 10K<n<100K
dataset_info:
  - config_name: rico_sca_refexp
    features:
      - name: image
        dtype: image
      - name: image_id
        dtype: string
      - name: labels
        list:
          - name: prompt
            dtype: string
          - name: target_bounding_box
            struct:
              - name: xmin
                dtype: float32
              - name: ymin
                dtype: float32
              - name: xmax
                dtype: float32
              - name: ymax
                dtype: float32
    splits:
      - name: train
        num_bytes: 2605508469
        num_examples: 24063
      - name: validation
        num_bytes: 21192787
        num_examples: 160
      - name: test
        num_bytes: 22057836
        num_examples: 185
    download_size: 6514703641
    dataset_size: 2605508469
---

This dataset is derived from the RICO SCA presented by Google Research in the seq2act paper. This is a synthetically generated dataset for UI RefExp task.
See original repo for details and licensing info:
https://github.com/google-research/google-research/blob/master/seq2act/data_generation/README.md#generate-ricosca-dataset

The splits in this dataset are consistent with the splits in the crowdsourced [UIBert RefExp](https://huggingface.co/datasets/ivelin/ui_refexp_saved) dataset. Training split examples do not include images from the Validation or Test examples in the UI Bert RefExp dataset. Respectively the images in Validation and Test splits here match the images in the Validation and Test splits of UIBert RefExp.
