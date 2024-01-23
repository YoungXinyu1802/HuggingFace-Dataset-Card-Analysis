---
annotations_creators:
  - no-annotation
language:
  - en
language_creators:
  - found
license:
  - gpl-3.0
multilinguality:
  - monolingual
pretty_name: kodak
size_categories:
  - n<1K
source_datasets:
  - original
tags: []
task_categories:
  - other
task_ids: []
dataset_info:
  features:
    - name: image
      dtype: image
  splits:
    - name: test
      num_bytes: 15072
      num_examples: 24
  download_size: 15072
  dataset_size: 15072
---

# Dataset Card for kodak

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** <https://r0k.us/graphics/kodak/>
- **Repository:** <https://github.com/MohamedBakrAli/Kodak-Lossless-True-Color-Image-Suite>
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

The pictures below link to lossless, true color (24 bits per pixel, aka "full
color") images. It is my understanding they have been released by the Eastman
Kodak Company for unrestricted usage. Many sites use them as a standard test
suite for compression testing, etc. Prior to this site, they were only
available in the Sun Raster format via ftp. This meant that the images could
not be previewed before downloading. Since their release, however, the lossless
PNG format has been incorporated into all the major browsers. Since PNG
supports 24-bit lossless color (which GIF and JPEG do not), it is now possible
to offer this browser-friendly access to the images.

### Supported Tasks and Leaderboards

- Image compression

### Languages

- en

## Dataset Structure

### Data Instances

- [![kodak01](https://r0k.us/graphics/kodak/thumbs/kodim01t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim01.png)
- [![kodak02](https://r0k.us/graphics/kodak/thumbs/kodim02t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim02.png)
- [![kodak03](https://r0k.us/graphics/kodak/thumbs/kodim03t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim03.png)
- [![kodak04](https://r0k.us/graphics/kodak/thumbs/kodim04t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim04.png)
- [![kodak05](https://r0k.us/graphics/kodak/thumbs/kodim05t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim05.png)
- [![kodak06](https://r0k.us/graphics/kodak/thumbs/kodim06t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim06.png)
- [![kodak07](https://r0k.us/graphics/kodak/thumbs/kodim07t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim07.png)
- [![kodak08](https://r0k.us/graphics/kodak/thumbs/kodim08t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim08.png)
- [![kodak09](https://r0k.us/graphics/kodak/thumbs/kodim09t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim09.png)
- [![kodak10](https://r0k.us/graphics/kodak/thumbs/kodim10t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim10.png)
- [![kodak11](https://r0k.us/graphics/kodak/thumbs/kodim11t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim11.png)
- [![kodak12](https://r0k.us/graphics/kodak/thumbs/kodim12t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim12.png)
- [![kodak13](https://r0k.us/graphics/kodak/thumbs/kodim13t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim13.png)
- [![kodak14](https://r0k.us/graphics/kodak/thumbs/kodim14t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim14.png)
- [![kodak15](https://r0k.us/graphics/kodak/thumbs/kodim15t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim15.png)
- [![kodak16](https://r0k.us/graphics/kodak/thumbs/kodim16t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim16.png)
- [![kodak17](https://r0k.us/graphics/kodak/thumbs/kodim17t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim17.png)
- [![kodak18](https://r0k.us/graphics/kodak/thumbs/kodim18t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim18.png)
- [![kodak19](https://r0k.us/graphics/kodak/thumbs/kodim19t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim19.png)
- [![kodak20](https://r0k.us/graphics/kodak/thumbs/kodim20t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim20.png)
- [![kodak21](https://r0k.us/graphics/kodak/thumbs/kodim21t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim21.png)
- [![kodak22](https://r0k.us/graphics/kodak/thumbs/kodim22t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim22.png)
- [![kodak23](https://r0k.us/graphics/kodak/thumbs/kodim23t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim23.png)
- [![kodak24](https://r0k.us/graphics/kodak/thumbs/kodim24t.jpg)](https://r0k.us/graphics/kodak/kodak/kodim24.png)

### Data Fields

### Data Splits

## Dataset Creation

### Curation Rationale

### Source Data

#### Initial Data Collection and Normalization

#### Who are the source language producers?

<https://www.kodak.com>

### Annotations

#### Annotation process

#### Who are the annotators?

### Personal and Sensitive Information

## Considerations for Using the Data

### Social Impact of Dataset

### Discussion of Biases

### Other Known Limitations

## Additional Information

### Dataset Curators

### Licensing Information

[LICENSE](LICENSE)

### Citation Information

### Contributions

Thanks to [@Freed-Wu](https://github.com/Freed-Wu) for adding this dataset.
