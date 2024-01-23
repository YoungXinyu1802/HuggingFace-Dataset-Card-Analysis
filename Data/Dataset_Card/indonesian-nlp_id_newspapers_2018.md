---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- id
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- text-generation
task_ids:
- language-modeling
pretty_name: Indonesian Newspapers 2018
---

# Dataset of Indonesian Online Newspaper

This is a copy of dataset created by **Feryandi Nurdiantoro** (<https://github.com/feryandi/Dataset-Artikel>). The original dataset in json format is stored uncompressed in Google Drive in more than 500K files, one file per article. Unfortunately, due to its size, it is impossible to download the whole dataset as one big compressed file (it takes forever to compress it online). Therefore I provide here a copy and its cleaned version as compressed files.

The dataset contains around 500K articles (136M of words) from 7 Indonesian newspapers: Detik, Kompas, Tempo, CNN Indonesia, Sindo, Republika and Poskota. The articles are dated between 1st January 2018 and 20th August 2018 (with few exceptions dated earlier). The size of uncompressed 500K json files (newspapers-json.tgz) is around 2.2GB, and the cleaned uncompressed in a big text file (newspapers.txt.gz) is about 1GB. The original source in Google Drive contains also a dataset in html format which include raw data (pictures, css, javascript, ...) from the online news website. I don't copy it here since it is about 60GB and mostly we only need the text content for NLP research.

Following is the compressed files:

* newspaper-json.gz: the compressed original 500K json files.
* newspaper.txt.gz: a dump of all json files in one big cleaned text file which is normally the only one needed for language model training.

The license has been copied from the source:

## License

Proyek ini dilisensikan dibawah lisensi **Creative Commons Attribution-ShareAlike 4.0 International License**\*. Kumpulan data yang dibagikan bertujuan untuk ilmu pengetahuan, pembelajaran, dan penelitian Bahasa Indonesia (komputasi maupun lingusitik), dan hanya dapat digunakan untuk hal tersebut. Kepemilikan data untuk setiap artikel dimiliki oleh media yang bersangkutan dimana data tersebut diambil; dan pemilik repository ini tidak melakukan klaim kepemilikan atas konten tersebut. Jika Anda mendapati bahwa data ini telah melanggar suatu hak cipta; mohon kontak pengelola repository ini.

This work is licensed under a **Creative Commons Attribution-ShareAlike 4.0 International License**. The dataset is shared for the sole purpose of aiding open scientific research in Bahasa Indonesia (computing or linguistics), and can only be used for that purpose. The ownership of each article within the dataset belongs to the respective newspaper from which it was extracted; and the maintainer of the repository does not claim ownership of any of the content within it. If you think, by any means, that this dataset breaches any established copyrights; please contact the repository maintainer.
