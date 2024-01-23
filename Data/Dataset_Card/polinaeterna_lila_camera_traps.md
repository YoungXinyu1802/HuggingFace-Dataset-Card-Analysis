---
annotations_creators:
- expert-generated
license:
- other
language_creators:
- expert-generated
language:
- en
multilinguality:
- monolingual
size_categories:
- 10M<n<100M
source_datasets:
- original
task_categories:
- image-classification
tags:
- biodiversity
- camera trap data
- wildlife monitoring
pretty_name: LILA Camera Traps
duplicated_from: society-ethics/lila_camera_traps
---

# Dataset Card for LILA

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
  - [Usage](#dataset-usage)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://lila.science/
- **Repository:** N/A
- **Paper:** N/A
- **Leaderboard:** N/A
- **Point of Contact:** [info@lila.science](info@lila.science)

### Dataset Summary

LILA Camera Traps is an aggregate data set of images taken by camera traps, which are devices that automatically (e.g. via motion detection) capture images of wild animals to help ecological research.

This data set is the first time when disparate camera trap data sets have been aggregated into a single training environment with a single [taxonomy](https://lila.science/taxonomy-mapping-for-camera-trap-data-sets/).

This data set consists of only camera trap image data sets, whereas the broader [LILA](lila.science/) website also has other data sets related to biology and conservation, intended as a resource for both machine learning (ML) researchers and those that want to harness ML for this topic.


See below for information about each specific dataset that LILA contains:

<details>
<summary> Caltech Camera Traps </summary>

This data set contains 243,100 images from 140 camera locations in the Southwestern United States, with labels for 21 animal categories (plus empty), primarily at the species level (for example, the most common labels are opossum, raccoon, and coyote), and approximately 66,000 bounding box annotations. Approximately 70% of images are labeled as empty.
More information about this data set is available [here](https://beerys.github.io/CaltechCameraTraps/).

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).

For questions about this data set, contact caltechcameratraps@gmail.com.

If you use this data set, please cite the associated manuscript:
```bibtex
    @inproceedings{DBLP:conf/eccv/BeeryHP18,
      author    = {Sara Beery and
                   Grant Van Horn and
                   Pietro Perona},
      title     = {Recognition in Terra Incognita},
      booktitle = {Computer Vision - {ECCV} 2018 - 15th European Conference, Munich,
                   Germany, September 8-14, 2018, Proceedings, Part {XVI}},
      pages     = {472--489},
      year      = {2018},
      crossref  = {DBLP:conf/eccv/2018-16},
      url       = {https://doi.org/10.1007/978-3-030-01270-0\_28},
      doi       = {10.1007/978-3-030-01270-0\_28},
      timestamp = {Mon, 08 Oct 2018 17:08:07 +0200},
      biburl    = {https://dblp.org/rec/bib/conf/eccv/BeeryHP18},
      bibsource = {dblp computer science bibliography, https://dblp.org}
    }
```
</details>

<details>
<summary> ENA24 </summary>

This data set contains approximately 10,000 camera trap images representing 23 classes from Eastern North America, with bounding boxes on each image. The most common classes are “American Crow”, “American Black Bear”, and “Dog”.

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).

Please cite this manuscript if you use this data set:
```bibtex
    @article{yousif2019dynamic,
    title={Dynamic Programming Selection of Object Proposals for Sequence-Level Animal Species Classification in the Wild},
    author={Yousif, Hayder and Kays, Roland and He, Zhihai},
    journal={IEEE Transactions on Circuits and Systems for Video Technology},
    year={2019},
    publisher={IEEE}
    }
```
For questions about this data set, contact [Hayder Yousif](hyypp5@mail.missouri.edu).

</details>

<details>
<summary> Missouri Camera Traps </summary>

This data set contains approximately 25,000 camera trap images representing 20 species (for example, the most common labels are red deer, mouflon, and white-tailed deer). Images within each sequence share the same species label (even though the animal may not have been recorded in all the images in the sequence). Around 900 bounding boxes are included. These are very challenging sequences with highly cluttered and dynamic scenes. Spatial resolutions of the images vary from 1920 × 1080 to 2048 × 1536. Sequence lengths vary from 3 to more than 300 frames.

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).

If you use this data set, please cite the associated manuscript:
```bibtex
@article{zhang2016animal,
  title={Animal detection from highly cluttered natural scenes using spatiotemporal object region proposals and patch verification},
  author={Zhang, Zhi and He, Zhihai and Cao, Guitao and Cao, Wenming},
  journal={IEEE Transactions on Multimedia},
  volume={18},
  number={10},
  pages={2079--2092},
  year={2016},
  publisher={IEEE}
}
```
For questions about this data set, contact [Hayder Yousif](hyypp5@mail.missouri.edu) and [Zhi Zhang](zzbhf@mail.missouri.edu).
</details>

<details>
<summary> North American Camera Trap Images (NACTI) </summary>

This data set contains 3.7M camera trap images from five locations across the United States, with labels for 28 animal categories, primarily at the species level (for example, the most common labels are cattle, boar, and red deer). Approximately 12% of images are labeled as empty. We have also added bounding box annotations to 8892 images (mostly vehicles and birds).
This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).

Please cite this manuscript if you use this data set:
```bibtex
    @article{tabak2019machine,
      title={Machine learning to classify animal species in camera trap images: Applications in ecology},
      author={Tabak, Michael A and Norouzzadeh, Mohammad S and Wolfson, David W and Sweeney, Steven J and VerCauteren, Kurt C and Snow, Nathan P and Halseth, Joseph M and Di Salvo, Paul A and Lewis, Jesse S and White, Michael D and others},
      journal={Methods in Ecology and Evolution},
      volume={10},
      number={4},
      pages={585--590},
      year={2019},
      publisher={Wiley Online Library}
    }
```

For questions about this data set, contact [northamericancameratrapimages@gmail.com](northamericancameratrapimages@gmail.com).

</details>

<details>
<summary> WCS Camera Traps </summary>

This data set contains approximately 1.4M camera trap images representing around 675 species from 12 countries, making it one of the most diverse camera trap data sets available publicly. Data were provided by the [Wildlife Conservation Society](https://www.wcs.org/). The most common classes are tayassu pecari (peccary), meleagris ocellata (ocellated turkey), and bos taurus (cattle). A complete list of classes and associated image counts is available here. Approximately 50% of images are empty. We have also added approximately 375,000 bounding box annotations to approximately 300,000 of those images, which come from sequences covering almost all locations.

Sequences are inferred from timestamps, so may not strictly represent bursts. Images were labeled at a combination of image and sequence level, so – as is the case with most camera trap data sets – empty images may be labeled as non-empty (if an animal was present in one frame of a sequence but not in others). Images containing humans are referred to in metadata, but are not included in the data files. You can find more information about the data set [on the LILA website](https://lila.science/datasets/wcscameratraps).

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).
</details>

<details>
<summary> Wellington Camera Traps </summary>

This data set contains 270,450 images from 187 camera locations in Wellington, New Zealand. The cameras (Bushnell 119537, 119476, and 119436) recorded sequences of three images when triggered. Each sequence was labelled by citizen scientists and/or professional ecologists from Victoria University of Wellington into 17 classes: 15 animal categories (for example, the most common labels are bird, cat, and hedgehog), empty, and unclassifiable. Approximately 17% of images are labeled as empty. Images within each sequence share the same species label (even though the animal may not have been recorded in all three images).

If you use this data set, please cite the associated manuscript:
```bibtex
    @article{anton2018monitoring,
      title={Monitoring the mammalian fauna of urban areas using remote cameras and citizen science},
      author={Anton, Victor and Hartley, Stephen and Geldenhuis, Andre and Wittmer, Heiko U},
      journal={Journal of Urban Ecology},
      volume={4},
      number={1},
      pages={juy002},
      year={2018},
      publisher={Oxford University Press}
    }
```

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).

For questions about this data set, contact [Victor Anton](vykanton@gmail.com).
</details>

<details>
<summary> Island Conservation Camera Traps </summary>

This data set contains approximately 123,000 camera trap images from 123 camera locations from 7 islands in 6 countries. Data were provided by Island Conservation during projects conducted to prevent the extinction of threatened species on islands.

The most common classes are rabbit, rat, petrel, iguana, cat, goat, and pig, with both rat and cat represented between multiple island sites representing significantly different ecosystems (tropical forest, dry forest, and temperate forests). Additionally, this data set represents data from locations and ecosystems that, to our knowledge, are not well represented in publicly available datasets including >1,000 images each of iguanas, petrels, and shearwaters. A complete list of classes and associated image counts is available here. Approximately 60% of the images are empty. We have also included approximately 65,000 bounding box annotations for about 50,000 images.

In general cameras were dispersed across each project site to detect the presence of invasive vertebrate species that threaten native island species. Cameras were set to capture bursts of photos for each motion detection event (between three and eight photos) with a set delay between events (10 to 30 seconds) to minimize the number of photos. Images containing humans are referred to in metadata, but are not included in the data files.

For questions about this data set, contact [David Will](david.will@islandconservation.org) at Island Conservation.

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).

The original data set included a “human” class label; for privacy reasons, we have removed those images from this version of the data set. Those labels are still present in the metadata. If those images are important to your work, contact us; in some cases it will be possible to release those images under an alternative license.
</details>

<details>
<summary> Channel Islands Camera Traps </summary>

This data set contains 246,529 camera trap images from 73 camera locations in the Channel Islands, California. All animals are annotated with bounding boxes. Data were provided by The Nature Conservancy. Animals are classified as rodent1 (82914), fox (48150), bird (11099), skunk (1071), or other (159). 114,949 images (47%) are empty. All images of rats were taken on islands already known to have rat populations.

If you use these data in a publication or report, please use the following citation:

The Nature Conservancy (2021): Channel Islands Camera Traps 1.0. The Nature Conservancy. Dataset.

For questions about this data set, contact [Nathaniel Rindlaub](nathaniel.rindlaub@TNC.ORG) at The Nature Conservancy.

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).

The original data set included a “human” class label; for privacy reasons, we have removed those images from this version of the data set. Those labels are still present in the metadata.

</details>

<details>
<summary> Idaho Camera Traps </summary>

This data set contains approximately 1.5 million camera trap images from Idaho. Labels are provided for 62 categories, most of which are animal classes (“deer”, “elk”, and “cattle” are the most common animal classes), but labels also include some state indicators (e.g. “snow on lens”, “foggy lens”). Approximately 70.5% of images are labeled as empty. Annotations were assigned to image sequences, rather than individual images, so annotations are meaningful only at the sequence level.

The metadata contains references to images containing humans, but these have been removed from the dataset (along with images containing vehicles and domestic dogs).

Images were provided by the Idaho Department of Fish and Game. No representations or warranties are made regarding the data, including but not limited to warranties of non-infringement or fitness for a particular purpose. Some information shared under this agreement may not have undergone quality assurance procedures and should be considered provisional. Images may not be sold in any format, but may be used for scientific publications. Please acknowledge the Idaho Department of Fish and Game when using images for publication or scientific communication.
</details>

<details>
<summary> Snapshot Serengeti </summary>

This data set contains approximately 2.65M sequences of camera trap images, totaling 7.1M images, from seasons one through eleven of the [Snapshot Serengeti project](https://snapshotserengeti.org/) -- the flagship project of the Snapshot Safari network. Using the same camera trapping protocols at every site, Snapshot Safari members are collecting standardized data from many protected areas in Africa, which allows for cross-site comparisons to assess the efficacy of conservation and restoration programs. Serengeti National Park in Tanzania is best known for the massive annual migrations of wildebeest and zebra that drive the cycling of its dynamic ecosystem.

Labels are provided for 61 categories, primarily at the species level (for example, the most common labels are wildebeest, zebra, and Thomson’s gazelle). Approximately 76% of images are labeled as empty. A full list of species and associated image counts is available [here](https://lilablobssc.blob.core.windows.net/snapshotserengeti-v-2-0/SnapshotSerengeti_S1-11_v2.1.species_list.csv). We have also added approximately 150,000 bounding box annotations to approximately 78,000 of those images.

The images and species-level labels are described in more detail in the associated manuscript:

```bibtex
  @misc{dryad_5pt92,
    title = {Data from: Snapshot Serengeti, high-frequency annotated camera trap images of 40 mammalian species in an African savanna},
    author = {Swanson, AB and Kosmala, M and Lintott, CJ and Simpson, RJ and Smith, A and Packer, C},
    year = {2015},
    journal = {Scientific Data},
    URL = {https://doi.org/10.5061/dryad.5pt92},
    doi = {doi:10.5061/dryad.5pt92},
    publisher = {Dryad Digital Repository}
  }
```

For questions about this data set, contact [Sarah Huebner](huebn090@umn.edu) at the University of Minnesota.

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).
</details>

<details>
<summary> Snapshot Karoo </summary>

This data set contains 14889 sequences of camera trap images, totaling 38074 images, from the [Snapshot Karoo](https://www.zooniverse.org/projects/shuebner729/snapshot-karoo) project, part of the Snapshot Safari network. Using the same camera trapping protocols at every site, Snapshot Safari members are collecting standardized data from many protected areas in Africa, which allows for cross-site comparisons to assess the efficacy of conservation and restoration programs. Karoo National Park, located in the arid Nama Karoo biome of South Africa, is defined by its endemic vegetation and mountain landscapes. Its unique topographical gradient has led to a surprising amount of biodiversity, with 58 mammals and more than 200 bird species recorded, as well as a multitude of reptilian species.

Labels are provided for 38 categories, primarily at the species level (for example, the most common labels are gemsbokoryx, hartebeestred, and kudu). Approximately 83.02% of images are labeled as empty. A full list of species and associated image counts is available [here](https://lilablobssc.blob.core.windows.net/snapshot-safari/KAR/SnapshotKaroo_S1_v1.0.species_list.csv).

For questions about this data set, contact [Sarah Huebner](huebn090@umn.edu) at the University of Minnesota.

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).
</details>


<details>
<summary> Snapshot Kgalagadi </summary>

This data set contains 3611 sequences of camera trap images, totaling 10222 images, from the [Snapshot Kgalagadi](https://www.zooniverse.org/projects/shuebner729/snapshot-kgalagadi/) project, part of the Snapshot Safari network. Using the same camera trapping protocols at every site, Snapshot Safari members are collecting standardized data from many protected areas in Africa, which allows for cross-site comparisons to assess the efficacy of conservation and restoration programs. The Kgalagadi Transfrontier Park stretches from the Namibian border across South Africa and into Botswana, covering a landscape commonly referred to as the Kalahari – an arid savanna. This region is of great interest to help us understand how animals cope with extreme temperatures at both ends of the scale.

Labels are provided for 31 categories, primarily at the species level (for example, the most common labels are gemsbokoryx, birdother, and ostrich). Approximately 76.14% of images are labeled as empty. A full list of species and associated image counts is available [here](https://lilablobssc.blob.core.windows.net/snapshot-safari/KGA/SnapshotKgalagadi_S1_v1.0.species_list.csv).

For questions about this data set, contact [Sarah Huebner](huebn090@umn.edu) at the University of Minnesota.

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).
</details>


<details>
<summary> Snapshot Enonkishu </summary>

This data set contains 13301 sequences of camera trap images, totaling 28544 images, from the [Snapshot Enonkishu](https://www.zooniverse.org/projects/aguthmann/snapshot-enonkishu) project, part of the Snapshot Safari network. Using the same camera trapping protocols at every site, Snapshot Safari members are collecting standardized data from many protected areas in Africa, which allows for cross-site comparisons to assess the efficacy of conservation and restoration programs. Enonkishu Conservancy is located on the northern boundary of the Mara-Serengeti ecosystem in Kenya, and is managed by a consortium of stakeholders and land-owning Maasai families. Their aim is to promote coexistence between wildlife and livestock in order to encourage regenerative grazing and build stability in the Mara conservancies.

Labels are provided for 39 categories, primarily at the species level (for example, the most common labels are impala, warthog, and zebra). Approximately 64.76% of images are labeled as empty. A full list of species and associated image counts is available [here](https://lilablobssc.blob.core.windows.net/snapshot-safari/ENO/SnapshotEnonkishu_S1_v1.0.species_list.csv).

For questions about this data set, contact [Sarah Huebner](huebn090@umn.edu) at the University of Minnesota.

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).
</details>


<details>
<summary> Snapshot Camdeboo </summary>

This data set contains 12132 sequences of camera trap images, totaling 30227 images, from the [Snapshot Camdeboo](https://www.zooniverse.org/projects/shuebner729/snapshot-camdeboo) project, part of the Snapshot Safari network. Using the same camera trapping protocols at every site, Snapshot Safari members are collecting standardized data from many protected areas in Africa, which allows for cross-site comparisons to assess the efficacy of conservation and restoration programs. Camdeboo National Park, South Africa is crucial habitat for many birds on a global scale, with greater than fifty endemic and near-endemic species and many migratory species.

Labels are provided for 43 categories, primarily at the species level (for example, the most common labels are kudu, springbok, and ostrich). Approximately 43.74% of images are labeled as empty. A full list of species and associated image counts is available [here](https://lilablobssc.blob.core.windows.net/snapshot-safari/CDB/SnapshotCamdeboo_S1_v1.0.species_list.csv).

For questions about this data set, contact [Sarah Huebner](huebn090@umn.edu) at the University of Minnesota.

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).
</details>


<details>
<summary> Snapshot Mountain Zebra </summary>

This data set contains 71688 sequences of camera trap images, totaling 73034 images, from the [Snapshot Mountain Zebra](https://www.zooniverse.org/projects/meredithspalmer/snapshot-mountain-zebra/) project, part of the Snapshot Safari network. Using the same camera trapping protocols at every site, Snapshot Safari members are collecting standardized data from many protected areas in Africa, which allows for cross-site comparisons to assess the efficacy of conservation and restoration programs. Mountain Zebra National Park is located in the Eastern Cape of South Africa in a transitional area between several distinct biomes, which means it is home to many endemic species. As the name suggests, this park contains the largest remnant population of Cape Mountain zebras, ~700 as of 2019 and increasing steadily every year.

Labels are provided for 54 categories, primarily at the species level (for example, the most common labels are zebramountain, kudu, and springbok). Approximately 91.23% of images are labeled as empty. A full list of species and associated image counts is available [here](https://lilablobssc.blob.core.windows.net/snapshot-safari/MTZ/SnapshotMountainZebra_S1_v1.0.species_list.csv).

For questions about this data set, contact [Sarah Huebner](huebn090@umn.edu) at the University of Minnesota.

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).
</details>


<details>
<summary> Snapshot Kruger </summary>

This data set contains 4747 sequences of camera trap images, totaling 10072 images, from the [Snapshot Kruger](https://www.zooniverse.org/projects/shuebner729/snapshot-kruger) project, part of the Snapshot Safari network. Using the same camera trapping protocols at every site, Snapshot Safari members are collecting standardized data from many protected areas in Africa, which allows for cross-site comparisons to assess the efficacy of conservation and restoration programs. Kruger National Park, South Africa has been a refuge for wildlife since its establishment in 1898, and it houses one of the most diverse wildlife assemblages remaining in Africa. The Snapshot Safari grid was established in 2018 as part of a research project assessing the impacts of large mammals on plant life as boundary fences were removed and wildlife reoccupied areas of previous extirpation.

Labels are provided for 46 categories, primarily at the species level (for example, the most common labels are impala, elephant, and buffalo). Approximately 61.60% of images are labeled as empty. A full list of species and associated image counts is available [here](https://lilablobssc.blob.core.windows.net/snapshot-safari/KRU/SnapshotKruger_S1_v1.0.species_list.csv).

For questions about this data set, contact [Sarah Huebner](huebn090@umn.edu) at the University of Minnesota.

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).
</details>


<details>
<summary> SWG Camera Traps </summary>

This data set contains 436,617 sequences of camera trap images from 982 locations in Vietnam and Lao, totaling 2,039,657 images. Labels are provided for 120 categories, primarily at the species level (for example, the most common labels are “Eurasian Wild Pig”, “Large-antlered Muntjac”, and “Unidentified Murid”). Approximately 12.98% of images are labeled as empty. A full list of species and associated image counts is available here. 101,659 bounding boxes are provided on 88,135 images.

This data set is provided by the Saola Working Group; providers include:

- IUCN SSC Asian Wild Cattle Specialist Group’s Saola Working Group (SWG)
- Asian Arks
- Wildlife Conservation Society (Lao)
- WWF Lao
- Integrated Conservation of Biodiversity and Forests project, Lao (ICBF)
- Center for Environment and Rural Development, Vinh University, Vietnam

If you use these data in a publication or report, please use the following citation:

SWG (2021): Northern and Central Annamites Camera Traps 2.0. IUCN SSC Asian Wild Cattle Specialist Group’s Saola Working Group. Dataset.

For questions about this data set, contact saolawg@gmail.com.

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).

</details>

<details>
<summary> Orinoquia Camera Traps </summary>

This data set contains 104,782 images collected from a 50-camera-trap array deployed from January to July 2020 within the private natural reserves El Rey Zamuro (31 km2) and Las Unamas (40 km2), located in the Meta department in the Orinoquía region in central Colombia. We deployed cameras using a stratified random sampling design across forest core area strata. Cameras were spaced 1 km apart from one another, located facing wildlife trails, and deployed with no bait. Images were stored and reviewed by experts using the Wildlife Insights platform.

This data set contains 51 classes, predominantly mammals such as the collared peccary, black agouti, spotted paca, white-lipped peccary, lowland tapir, and giant anteater. Approximately 20% of images are empty.

The main purpose of the study is to understand how humans, wildlife, and domestic animals interact in multi-functional landscapes (e.g., agricultural livestock areas with native forest remnants). However, this data set was also used to review model performance of AI-powered platforms – Wildlife Insights (WI), MegaDetector (MD), and Machine Learning for Wildlife Image Classification (MLWIC2). We provide a demonstration of the use of WI, MD, and MLWIC2 and R code for evaluating model performance of these platforms in the accompanying [GitHub repository](https://github.com/julianavelez1/Processing-Camera-Trap-Data-Using-AI).

If you use these data in a publication or report, please use the following citation:
```bibtex
    @article{velez2022choosing,
      title={Choosing an Appropriate Platform and Workflow for Processing Camera Trap Data using Artificial Intelligence},
      author={V{\'e}lez, Juliana and Castiblanco-Camacho, Paula J and Tabak, Michael A and Chalmers, Carl and Fergus, Paul and Fieberg, John},
      journal={arXiv preprint arXiv:2202.02283},
      year={2022}
    }
```
For questions about this data set, contact [Juliana Velez Gomez](julianavelezgomez@gmail.com).

This data set is released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/).
</details>

### Supported Tasks and Leaderboards

No leaderboards exist for LILA.

### Languages

The [LILA taxonomy](https://lila.science/taxonomy-mapping-for-camera-trap-data-sets/) is provided in English.

## Dataset Structure

### Data Instances

The data annotations are provided in [COCO Camera Traps](https://github.com/Microsoft/CameraTraps/blob/master/data_management/README.md#coco-cameratraps-format) format.

All of the datasets share a common category taxonomy, which is defined on the [LILA website](https://lila.science/taxonomy-mapping-for-camera-trap-data-sets/).

### Data Fields

Different datasets may have slightly varying fields, which include:

`file_name`: the file name \
`width` and `height`: the dimensions of the image \
`study`: which research study the image was collected as part of \
`location` : the name of the location at which the image was taken \
 `annotations`: information about image annotation, which includes the taxonomy information, bounding box/boxes (`bbox`/`bboxes`) if any, as well as any other annotation information. \
 `image` : the `path` to download the image and any other information that is available, e.g. its size in `bytes`.


### Data Splits

This dataset does not have a predefined train/test split.

## Dataset Creation

### Curation Rationale

The datasets that constitute LILA have been provided by the organizations, projects and researchers who collected them.

### Source Data

#### Initial data collection and normalization

N/A

#### Who are the source language producers?

N/A

### Annotations

#### Annotation process

Each dataset has been annotated by the members of the project/organization that provided it.

#### Who are the annotators?

The annotations have been provided by domain experts in fields such as biology and ecology.

### Personal and Sensitive Information

Some of the original data sets included a “human” class label; for privacy reasons, these images were removed. Those labels are still present in the metadata. If those images are important to your work, contact the [LILA maintainers](mailto:info@lila.science), since in some cases it will be possible to release those images under an alternative license.

## Considerations for Using the Data

### Social Impact of Dataset

Machine learning depends on labeled data, but accessing such data in biology and conservation is a challenge. Consequently, everyone benefits when labeled data is made available. Biologists and conservation scientists benefit by having data to train on, and free hosting allows teams to multiply the impact of their data (we suggest listing this benefit in grant proposals that fund data collection). ML researchers benefit by having data to experiment with.

### Discussion of Biases

These datasets do not represent global diversity, but are examples of local ecosystems and animals.

### Other Known Limitations

N/A

## Additional Information

### Working with Taxonomies

All the taxonomy categories are saved as ClassLabels, which can be converted to strings as needed. Strings can likewise be converted to integers as needed, to filter the dataset. In the example below we filter the "Caltech Camera Traps" dataset to find all the entries with a "felis catus" as the species for the first annotation.

```python
dataset = load_dataset("society-ethics/lila_camera_traps", "Caltech Camera Traps", split="train")
taxonomy = dataset.features["annotations"].feature["taxonomy"]

# Filters to show only cats
cats = dataset.filter(lambda x: x["annotations"]["taxonomy"][0]["species"] == taxonomy["species"].str2int("felis catus"))
```

The original common names have been saved with their taxonomy mappings in this repository in `common_names_to_tax.json`. These can be used, for example, to map from a taxonomy combination to a common name to help make queries more legible. Note, however, that there is a small number of duplicate common names with different taxonomy values which you will need to disambiguate.

The following example loads the first "sea turtle" in the "Island Conservation Camera Traps" dataset.

```python
LILA_COMMON_NAMES_TO_TAXONOMY = pd.read_json("https://huggingface.co/datasets/society-ethics/lila_camera_traps/raw/main/data/common_names_to_tax.json", lines=True).set_index("common_name")
dataset = load_dataset("society-ethics/lila_camera_traps", "Island Conservation Camera Traps", split="train")
taxonomy = dataset.features["annotations"].feature["taxonomy"]

sea_turtle = LILA_COMMON_NAMES_TO_TAXONOMY.loc["sea turtle"].to_dict()
sea_turtle = {k: taxonomy[k].str2int(v) if v is not None else v for k, v in sea_turtle.items()}  # Map to ClassLabel integers

sea_turtle_dataset = ds.filter(lambda x: x["annotations"]["taxonomy"][0] == sea_turtle)
```

The example below selects a random item from the dataset, and then maps from the taxonomy to a common name:

```python
LILA_COMMON_NAMES_TO_TAXONOMY = pd.read_json("https://huggingface.co/datasets/society-ethics/lila_camera_traps/raw/main/data/common_names_to_tax.json", lines=True).set_index("common_name")

dataset = load_dataset("society-ethics/lila_camera_traps", "Caltech Camera Traps", split="train")
taxonomy = dataset.features["annotations"].feature["taxonomy"]

random_entry = dataset.shuffle()[0]
filter_taxonomy = random_entry["annotations"]["taxonomy"][0]

filter_keys = list(map(lambda x: (x[0], taxonomy[x[0]].int2str(x[1])), filter(lambda x: x[1] is not None, list(filter_taxonomy.items()))))

if len(filter_keys) > 0:
    print(LILA_COMMON_NAMES_TO_TAXONOMY[np.logical_and.reduce([
        LILA_COMMON_NAMES_TO_TAXONOMY[k] == v for k,v in filter_keys
    ])])
else:
    print("No common name found for the item.")
```


### Dataset Curators

LILA BC is maintained by a working group that includes representatives from Ecologize, Zooniverse, the Evolving AI Lab, Snapshot Safari, and Microsoft AI for Earth. Hosting on Microsoft Azure is provided by Microsoft AI for Earth.

### Licensing Information

Many, but not all, LILA data sets were released under the [Community Data License Agreement (permissive variant)](https://cdla.io/permissive-1-0/). Check the details of the specific dataset you are using in its section above.

### Citation Information

Citations for each dataset  (if they exist) are provided in its section above.

### Contributions

Thanks to [@NimaBoscarino](https://github.com/NimaBoscarino/) for adding this dataset.
