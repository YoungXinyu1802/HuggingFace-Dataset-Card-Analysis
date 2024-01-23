---
license: cc0-1.0
language:
- en
tags:
- tropes
- movies
- recommender
size_categories:
- 1K<n<10K
---
# Dataset Card for Dataset Name

## Dataset Description

### Dataset Summary

The dataset provides a mapping between [TV Tropes](https://tvtropes.org/) and [IMDb](https://www.imdb.com/) entries for about 10K movies.

### Supported Tasks and Leaderboards

No particular task is supported, because the dataset is intended to enrich other datasets
(for instance, [Movielens](https://grouplens.org/datasets/movielens/))

### Languages

Movie titles are provided in English the way they are present on TV Tropes.

## Dataset Structure

The dataset is comprised of two columns: `tvtropes` and `imdb`. The former can be used to access the movie's page on TV Tropes
using the following url template: `https://tvtropes.org/pmwiki/pmwiki.php/Film/{tvtropes}`. The latter can be used to acces the
movie's page on IMDb using the following url template `https://www.imdb.com/title/tt{imdb}/` (note that the imbd id has to be
padded to the left with zeroes if it contains less than seven digits).

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

There is only one split. The data is not meant to be used directly for training/evaluation.

## Dataset Creation

The dataset was created semi-automatically: [Cinemagoer](https://github.com/cinemagoer/cinemagoer) was used to query IMDb for movies with
matching titles, then the resulting output was manually verified.

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

### Annotations

#### Annotation process

The annotation only involved manually verifying that a given TV Tropes entry corresponds to a correct IMDb entry.
However, some are inaccuracies may be still present due to the sheer volume of data.

#### Who are the annotators?

The correctness of the mapping was verified by me (Aleksei Dorkin) personally. 

### Personal and Sensitive Information

Not applicable.

## Considerations for Using the Data

### Social Impact of Dataset

Not applicable. The impact may potentially come from the data that is linked using the dataset.

### Discussion of Biases

Not applicable. The datasets only links together entries for movies on different web resources.

### Other Known Limitations

One potential limitation of the dataset may come from the way TV Tropes pages are organized. It is not always possible to automatically
distinguish a page related to a franchise in general and a paged related to a particular movie in a franchise.

Another thing to consider is that it's pretty common for movies to share the exact same title. At the same time, they can also be quite
similar in content. Thus, it's not always trivial to distinguish movies with the same title if no year is given.

As a result, some inaccuries of this nature may be present in the data.

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

CC0

### Citation Information

[More Information Needed]

### Contributions

Contributions are welcome on this dataset page using the Community tab.