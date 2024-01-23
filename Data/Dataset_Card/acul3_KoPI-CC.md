---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- id
license: cc
multilinguality:
- monolingual
source_datasets:
- original
task_categories:
- text-generation
task_ids:
- language-modeling
paperswithcode_id: oscar
---

  

### Dataset Summary

KoPI-CC (Korpus Perayapan Indonesia)-CC is Indonesian only extract from Common Crawl snapshots using [ungoliant](https://github.com/oscar-corpus/ungoliant), each snapshot also filtered using some some deduplicate technique such as exact hash(md5) dedup technique and minhash LSH neardup
 

### Preprocessing

Each folder name inside snapshots folder denoted preprocessing technique that has been applied .

 - **Raw**
	 - this processed directly from cc snapshot using ungoliant without any addition filter ,you can read it in their paper (citation below)
	 - use same "raw cc snapshot" for `2021_10` and `2021_49` which  can be found in oscar dataset ([2109](https://huggingface.co/datasets/oscar-corpus/OSCAR-2109/tree/main/packaged_nondedup/id) and [2201](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201/tree/main/compressed/id_meta))
 - **Dedup**
	 - use data from raw folder
	 - apply cleaning techniques for every text in documents such as 
		 - fix html
		 - remove noisy unicode
		 - fix news tag
		 - remove control char
	 - filter by removing short text (20 words)
	 - filter by character ratio occurred inside text such as
		 - min_alphabet_ratio (0.75)
		 - max_upper_ratio (0.10)
		 - max_number_ratio(0.05)
	
	 - filter by exact dedup technique
		 - hash all text with md5 hashlib
		 - remove non-unique hash
	 - full code about dedup step adapted from [here](https://huggingface.co/datasets/Finnish-NLP/mc4_fi_cleaned/tree/main)
 - **Neardup**
	 - use data from dedup folder
	
	 - create index cluster using neardup [Minhash and LSH](http://ekzhu.com/datasketch/lsh.html) with following config :
		 - use 128 permuation
		 - 6 n-grams size
		 - use word tokenization (split sentence by space)
		 - use 0.8 as similarity score
	
	 - fillter by removing all index from cluster
	 - full code about neardup step adapted from  [here](https://github.com/ChenghaoMou/text-dedup)
 - **Neardup_clean**
	 -    use data from neardup folder
	 -    Removing documents containing words from a selection of the  [Indonesian Bad Words](https://github.com/acul3/c4_id_processed/blob/67e10c086d43152788549ef05b7f09060e769993/clean/badwords_ennl.py#L64).
	
    
	-   Removing sentences containing:
	    
	    -   Less than 3 words.
	        
	    -   A word longer than 1000 characters.
	        
	    -   An end symbol not matching end-of-sentence punctuation.
	        
	    -   Strings associated to javascript code (e.g.  `{`), lorem ipsum, policy information in indonesia
        
	-   Removing documents (after sentence filtering):
	    
	    -   Containing less than 5 sentences.
	        
	    -   Containing less than 500 or more than 50'000 characters.
	 - full code about neardup_clean step adapted from [here](https://gitlab.com/yhavinga/c4nlpreproc)

	       
## Dataset Structure

### Data Instances

An example from the dataset:
```

{'text': 'Panitia Kerja (Panja) pembahasan RUU Cipta Kerja (Ciptaker) DPR RI memastikan naskah UU Ciptaker sudah final, tapi masih dalam penyisiran. Penyisiran dilakukan agar isi UU Ciptaker sesuai dengan kesepakatan dalam pembahasan dan tidak ada salah pengetikan (typo).\n"Kan memang sudah diumumkan, naskah final itu sudah. Cuma kita sekarang … DPR itu kan punya waktu 7 hari sebelum naskah resminya kita kirim ke pemerintah. Nah, sekarang itu kita sisir, jangan sampai ada yang salah pengetikan, tapi tidak mengubah substansi," kata Ketua Panja RUU Ciptaker Supratman Andi Agtas saat berbincang dengan detikcom, Jumat (9/10/2020) pukul 10.56 WIB.\nSupratman mengungkapkan Panja RUU Ciptaker menggelar rapat hari ini untuk melakukan penyisiran terhadap naskah UU Ciptaker. Panja, sebut dia, bekerja sama dengan pemerintah dan ahli bahasa untuk melakukan penyisiran naskah.\n"Sebentar, siang saya undang seluruh poksi-poksi (kelompok fraksi) Baleg (Badan Legislasi DPR), anggota Panja itu datang ke Baleg untuk melihat satu per satu, jangan sampai …. Karena kan sekarang ini tim dapur pemerintah dan DPR lagi bekerja bersama dengan ahli bahasa melihat jangan sampai ada yang typo, redundant," terangnya.\nSupratman membenarkan bahwa naskah UU Ciptaker yang final itu sudah beredar. Ketua Baleg DPR itu memastikan penyisiran yang dilakukan tidak mengubah substansi setiap pasal yang telah melalui proses pembahasan.\n"Itu yang sudah dibagikan. Tapi kan itu substansinya yang tidak mungkin akan berubah. Nah, kita pastikan nih dari sisi drafting-nya yang jadi kita pastikan," tutur Supratman.\nLebih lanjut Supratman menjelaskan DPR memiliki waktu 7 hari untuk melakukan penyisiran. Anggota DPR dari Fraksi Gerindra itu memastikan paling lambat Selasa (13/10) pekan depan, naskah UU Ciptaker sudah bisa diakses oleh masyarakat melalui situs DPR.\n"Kita itu, DPR, punya waktu sampai 7 hari kerja. Jadi harusnya hari Selasa sudah final semua, paling lambat. Tapi saya usahakan hari ini bisa final. Kalau sudah final, semua itu langsung bisa diakses di web DPR," terang Supratman.\nDiberitakan sebelumnya, Wakil Ketua Baleg DPR Achmad Baidowi mengakui naskah UU Ciptaker yang telah disahkan di paripurna DPR masih dalam proses pengecekan untuk menghindari kesalahan pengetikan. Anggota Komisi VI DPR itu menyinggung soal salah ketik dalam revisi UU KPK yang disahkan pada 2019.\n"Mengoreksi yang typo itu boleh, asalkan tidak mengubah substansi. Jangan sampai seperti tahun lalu, ada UU salah ketik soal umur \'50 (empat puluh)\', sehingga pemerintah harus mengonfirmasi lagi ke DPR," ucap Baidowi, Kamis (8/10).',
 'url': 'https://news.detik.com/berita/d-5206925/baleg-dpr-naskah-final-uu-ciptaker-sedang-diperbaiki-tanpa-ubah-substansi?tag_from=wp_cb_mostPopular_list&_ga=2.71339034.848625040.1602222726-629985507.1602222726',
 'timestamp': '2021-10-22T04:09:47Z',
 'meta': '{"warc_headers": {"content-length": "2747", "content-type": "text/plain", "warc-date": "2021-10-22T04:09:47Z", "warc-record-id": "<urn:uuid:a5b2cc09-bd2b-4d0e-9e5b-2fcc5fce47cb>", "warc-identified-content-language": "ind,eng", "warc-target-uri": "https://news.detik.com/berita/d-5206925/baleg-dpr-naskah-final-uu-ciptaker-sedang-diperbaiki-tanpa-ubah-substansi?tag_from=wp_cb_mostPopular_list&_ga=2.71339034.848625040.1602222726-629985507.1602222726", "warc-block-digest": "sha1:65AWBDBLS74AGDCGDBNDHBHADOKSXCKV", "warc-type": "conversion", "warc-refers-to": "<urn:uuid:b7ceadba-7120-4e38-927c-a50db21f0d4f>"}, "identification": {"label": "id", "prob": 0.6240405}, "annotations": null, "line_identifications": [null, {"label": "id", "prob": 0.9043896}, null, null, {"label": "id", "prob": 0.87111086}, {"label": "id", "prob": 0.9095224}, {"label": "id", "prob": 0.8579232}, {"label": "id", "prob": 0.81366056}, {"label": "id", "prob": 0.9286813}, {"label": "id", "prob": 0.8435194}, {"label": "id", "prob": 0.8387821}, null]}'}
```
### Data Fields
The data contains the following fields:
- `url`: url of the source as a string
- `text`: text content as a string
- `timestamp`: timestamp of extraction as a string
- `meta` : json representation of the original from ungoliant tools,can be found [here](https://oscar-corpus.com/post/oscar-v22-01/) (warc_heder) 

  
  
## Additional Information

### Dataset Curators
For inquiries or requests regarding the KoPI-CC contained in this repository, please contact me at [samsulrahmadani@gmail.com](mailto:samsulrahmadani@gmail.com)


### Licensing Information
    These data are released under this licensing scheme
    I do not own any of the text from which these data has been extracted.
   	the license actual packaging of these data under the Creative Commons CC0 license ("no rights reserved") http://creativecommons.org/publicdomain/zero/1.0/
    Should you consider that data contains material that is owned by you and should therefore not be reproduced here, please:
    * Clearly identify yourself, with detailed contact data such as an address, telephone number or email address at which you can be contacted.
    * Clearly identify the copyrighted work claimed to be infringed.
    * Clearly identify the material that is claimed to be infringing and information reasonably sufficient to allow us to locate the material.
    I will comply to legitimate requests by removing the affected sources from the next release of the corpus.

  

### Citation Information

 
```

  

@ARTICLE{2022arXiv220106642A,

author = {{Abadji}, Julien and {Ortiz Suarez}, Pedro and {Romary}, Laurent and {Sagot}, Beno{\^\i}t},

title = "{Towards a Cleaner Document-Oriented Multilingual Crawled Corpus}",

journal = {arXiv e-prints},

keywords = {Computer Science - Computation and Language},

year = 2022,

month = jan,

eid = {arXiv:2201.06642},

pages = {arXiv:2201.06642},

archivePrefix = {arXiv},

eprint = {2201.06642},

primaryClass = {cs.CL},

adsurl = {https://ui.adsabs.harvard.edu/abs/2022arXiv220106642A},

adsnote = {Provided by the SAO/NASA Astrophysics Data System}

}

@inproceedings{AbadjiOrtizSuarezRomaryetal.2021,

author = {Julien Abadji and Pedro Javier Ortiz Su{\'a}rez and Laurent Romary and Beno{\^i}t Sagot},

title = {Ungoliant: An optimized pipeline for the generation of a very large-scale multilingual web corpus},

series = {Proceedings of the Workshop on Challenges in the Management of Large Corpora (CMLC-9) 2021. Limerick, 12 July 2021 (Online-Event)},

editor = {Harald L{\"u}ngen and Marc Kupietz and Piotr Bański and Adrien Barbaresi and Simon Clematide and Ines Pisetta},

publisher = {Leibniz-Institut f{\"u}r Deutsche Sprache},

address = {Mannheim},

doi = {10.14618/ids-pub-10468},

url = {https://nbn-resolving.org/urn:nbn:de:bsz:mh39-104688},

pages = {1 -- 9},

year = {2021},

abstract = {Since the introduction of large language models in Natural Language Processing, large raw corpora have played a crucial role in Computational Linguistics. However, most of these large raw corpora are either available only for English or not available to the general public due to copyright issues. Nevertheless, there are some examples of freely available multilingual corpora for training Deep Learning NLP models, such as the OSCAR and Paracrawl corpora. However, they have quality issues, especially for low-resource languages. Moreover, recreating or updating these corpora is very complex. In this work, we try to reproduce and improve the goclassy pipeline used to create the OSCAR corpus. We propose a new pipeline that is faster, modular, parameterizable, and well documented. We use it to create a corpus similar to OSCAR but larger and based on recent data. Also, unlike OSCAR, the metadata information is at the document level. We release our pipeline under an open source license and publish the corpus under a research-only license.},

language = {en}

}

  
  

```