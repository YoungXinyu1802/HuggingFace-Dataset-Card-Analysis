---
license: mit
task_categories:
- question-answering
- text-retrieval
language:
- fr
tags:
- education
size_categories:
- 10K<n<100K
---

# Alloprof dataset

This is the dataset refered to in our paper:

Alloprof: a new French question-answer education dataset and its use in an information retrieval case study (https://arxiv.org/abs/2302.07738)

This dataset was provided by [AlloProf](https://www.alloprof.qc.ca/), an organisation in Quebec, Canada offering resources and a help forum curated by a large number of teachers to students on all subjects taught from in primary and secondary school.

Raw data on questions is available in the following files:

- `data/questions/categories.json`: subjects and their corresponding id
- `data/questions/comments.json`: explanation (answer) data
- `data/questions/discussions.json`: question data
- `data/questions/grades.json`: grades and their corresponding id
- `data/questions/roles.json`: information about the user type for each user id

Raw data on reference pages is available in the following files:

- `data/pages/page-content-en.json`: data for the reference pages in English
- `data/pages/page-content-fr.json`: data for the reference pages in French

The data can be parsed and structured using the script `scripts/parse_data.py` to create the file `data/alloprof.csv` with the following columns:

- `id` (str) : Id of the document
- `url` (str) : URL of the document
- `text` (str) : Parsed text of the document
- `language` (str) : Either "fr" or "en", the language of the document
- `user` (int) : Id corresponding to the user who asked the question
- `images` (str) : ";" separated list of URLs of images contained in the document
- `relevant` (str) : ";" separated list of document ids appearing as links in the explanation to that document. For files, this will always be empty as there are no corresponding explanation
- `is_query` (bool) : If this document is a question
- `subject` (str) : ";" separated list of school subjects the document is related to
- `grade` (str) : ";" separated list of school grade levels the document is related to
- `possible` (str) : ";" separated list of possible documents ids this document may refer to. This list corresponds to every document of the same subject and grade. For files, this will always be empty to speed up reading and writing

The `possible` column depends on arguments passed to the scripts to add related subjects, and lower and higher grade levels to the possible documents (see paper).
Also note that the provided `alloprof.csv` file is stored with git lfs and can be pulled with `git lfs install && git lfs pull`.

For images, a script to download them is available as `scripts/download_images.py`.

If you have any questions, don't hesitate to mail us at antoine.lefebvre-brossard@mila.quebec.

**Please cite our work as:**

```
@misc{lef23,
  doi = {10.48550/ARXIV.2302.07738},
  url = {https://arxiv.org/abs/2302.07738},
  author = {Lefebvre-Brossard, Antoine and Gazaille, Stephane and Desmarais, Michel C.},
  keywords = {Computation and Language (cs.CL), Information Retrieval (cs.IR), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Alloprof: a new French question-answer education dataset and its use in an information retrieval case study},
  publisher = {arXiv},
  year = {2023},
  copyright = {Creative Commons Attribution Non Commercial Share Alike 4.0 International}
}
```