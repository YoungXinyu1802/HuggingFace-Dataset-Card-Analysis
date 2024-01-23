---
license: cc-by-4.0
---

### Abstract 
Social tagging of movies reveals a wide range of heterogeneous information about movies, like the genre, plot structure, soundtracks, metadata, visual and emotional experiences. Such information can be valuable in building automatic systems to create tags for movies. Automatic tagging systems can help recommendation engines to improve the retrieval of similar movies as well as help viewers to know what to expect from a movie in advance. In this paper, we set out to the task of collecting a corpus of movie plot synopses and tags. We describe a methodology that enabled us to build a fine-grained set of around 70 tags exposing heterogeneous characteristics of movie plots and the multi-label associations of these tags with some 14K movie plot synopses. We investigate how these tags correlate with movies and the flow of emotions throughout different types of movies. Finally, we use this corpus to explore the feasibility of inferring tags from plot synopses. We expect the corpus will be useful in other tasks where analysis of narratives is relevant.

### Content
This dataset was first published in LREC 2018 at Miyazaki, Japan.
Please find the paper here:
![MPST: A Corpus of Movie Plot Synopses with Tags](https://aclanthology.org/L18-1274.pdf)



Later, this dataset was enriched with user reviews. The paper is available here:
![Multi-view Story Characterization from Movie Plot Synopses and Reviews](https://aclanthology.org/2020.emnlp-main.454.pdf)
This dataset was published in EMNLP 2020.


### Keywords
Tag generation for movies, Movie plot analysis, Multi-label dataset, Narrative texts

More information is available here
http://ritual.uh.edu/mpst-2018/

Please cite the following papers if you use this dataset:

```
@InProceedings{KAR18.332,
author = {Sudipta Kar and Suraj Maharjan and A. Pastor López-Monroy and Thamar Solorio},
title = {{MPST}: A Corpus of Movie Plot Synopses with Tags},
booktitle = {Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},
year = {2018},
month = {May},
date = {7-12},
location = {Miyazaki, Japan},
editor = {Nicoletta Calzolari (Conference chair) and Khalid Choukri and Christopher Cieri and Thierry Declerck and Sara Goggi and Koiti Hasida and Hitoshi Isahara and Bente Maegaard and Joseph Mariani and Hélène Mazo and Asuncion Moreno and Jan Odijk and Stelios Piperidis and Takenobu Tokunaga},
publisher = {European Language Resources Association (ELRA)},
address = {Paris, France},
isbn = {979-10-95546-00-9},
language = {english}
}
```

```
@inproceedings{kar-etal-2020-multi,
    title = "Multi-view Story Characterization from Movie Plot Synopses and Reviews",
    author = "Kar, Sudipta  and
      Aguilar, Gustavo  and
      Lapata, Mirella  and
      Solorio, Thamar",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.emnlp-main.454",
    doi = "10.18653/v1/2020.emnlp-main.454",
    pages = "5629--5646",
    abstract = "This paper considers the problem of characterizing stories by inferring properties such as theme and style using written synopses and reviews of movies. We experiment with a multi-label dataset of movie synopses and a tagset representing various attributes of stories (e.g., genre, type of events). Our proposed multi-view model encodes the synopses and reviews using hierarchical attention and shows improvement over methods that only use synopses. Finally, we demonstrate how we can take advantage of such a model to extract a complementary set of story-attributes from reviews without direct supervision. We have made our dataset and source code publicly available at https://ritual.uh.edu/multiview-tag-2020.",
}
```


