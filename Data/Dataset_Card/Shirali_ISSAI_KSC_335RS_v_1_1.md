---
dataset_info:
  features:
  - name: uttID
    dtype: string
  - name: deviceID
    dtype: int64
  - name: text
    dtype: string
  - name: audio
    dtype: audio
  splits:
  - name: dev
    num_bytes: 391608860.227
    num_examples: 3283
  - name: test
    num_bytes: 372725363.792
    num_examples: 3334
  - name: train
    num_bytes: 19832618976.144
    num_examples: 147236
  download_size: 19079278086
  dataset_size: 20596953200.163002
task_categories:
- automatic-speech-recognition
language:
- kk
---
# Dataset Card for "ISSAI_KSC_335RS_v_1_1"

Kazakh Speech Corpus (KSC)
Identifier: SLR102

Summary: A crowdsourced open-source Kazakh speech corpus developed by ISSAI (330 hours)

Category: Speech

License: Attribution 4.0 International (CC BY 4.0)

Downloads (use a mirror closer to you):
ISSAI_KSC_335RS_v1.1_flac.tar.gz [19G]   (speech, transcripts and metadata )   Mirrors: [US]   [EU]   [CN]  


About this resource:

A crowdsourced open-source speech corpus for the Kazakh language. The KSC contains around 332 hours of transcribed audio comprising over 153,000 utterances spoken by participants from different regions and age groups, as well as both genders. It was carefully inspected by native Kazakh speakers to ensure high quality. The dataset is primarily intended to be used for training automatic speech recognition systems.
You can find more information about the dataset here.

To cite the dataset, please use the following BibTeX entry:

@inproceedings{khassanov-etal-2021-crowdsourced,
  title = "A Crowdsourced Open-Source {K}azakh Speech Corpus and Initial Speech Recognition Baseline",
  author={Yerbolat Khassanov and Saida Mussakhojayeva and Almas Mirzakhmetov and Alen Adiyev and Mukhamet Nurpeiissov and Huseyin Atakan Varol},
  booktitle = "Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume",
  month = apr,
  year = "2021",
  address = "Online",
  publisher = "Association for Computational Linguistics",
  url = "https://aclanthology.org/2021.eacl-main.58",
  doi = "10.18653/v1/2021.eacl-main.58",
  pages = "697--706"
}
