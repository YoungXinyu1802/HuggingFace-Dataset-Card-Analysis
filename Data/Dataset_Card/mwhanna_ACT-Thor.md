# Dataset Card for ACT-Thor

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Repository:** https://github.com/hannamw/ACT-Thor
- **Paper:** Paper ACT-Thor: A Controlled Benchmark for Embodied Action Understanding in Simulated Environments (COLING 2022; Link to be added soon)
- **Point of Contact:** Michael Hanna (m.w.hanna@uva.nl)

### Dataset Summary

This dataset is intended to test models' abilities to understand actions, and to do so in a controlled fashion. It is generated automatically using [AI2-Thor](https://ai2thor.allenai.org/), and thus contains images of a virtual house. Models receive an image of an object in a house (the before-image), an action, and four after-images that might have potentially resulted from performing the action on the object. Then, they must predict which of the after-images actually resulted from performing the action in the before-image.

### Supported Tasks

This dataset implements the contrast set task discussed in the paper: given a before image and an action, predict which of 4 after images is the actual result of performing the action in the before image. However, the raw data (not included here) could be used for other tasks, e.g. given a before and after image, infer the action taken. Feel free to reach out and request the full data (with all of the metadata and other information that might be useful), or collect it automatically using the scripts available on the project's [GitHub repo](https://github.com/hannamw/ACT-Thor)!

## Dataset Structure

### Data Instances

There are 4441 instances in the dataset, each consisting of the fields below:

### Data Fields

- id: integer ID of the example
- object: name (string) of the object of interest
- action: name (string) of the action taken
- action_id: integer ID of the action taken
- scene: the ID (string) of the scene from which this example comes
- before_image: The before image
- after_image_{0-3}: The after images, from which the correct image is to be chosen
- label: The index (0-3) of the correct after image

Only the action_id, before_image, and after_image need be fed into the model, which should predict the label.

### Data Splits

We create 3 different train-valid-test splits. In the sample split, each examples has been randomly assigned to either the train, valid, and test split, without any special organization. The object split introduces new objects in the test split, to test object generalization. Finally, the scene split is organized such that the scenes contained in train, valid, and test are disjoint (to test scene generalization).

## Dataset Creation

### Curation Rationale

This dataset was curated for two reasons. Its main purpose is to test models' abilities to understand the consequences of actions. However, its creation also intends to showcase the potential of virtual platforms as sites for the collection of data, especially in a highly controlled fashion.

### Source Data

#### Initial Data Collection and Normalization

All of the data is collected by navigating throughout AI2-Thor virtual environments and recording images in metadata. Check out the paper, where we describe this process in detail!

### Annotations

#### Annotation process

This dataset is generated entirely automatically using AI2-Thor, so there are no annotations. In the paper, we discuss annotations created by humans performing the task; these are only used to check that the task is feasible for humans. We're happy to release these if requested; these were collected from students at 2 universities.

## Considerations for Using the Data

### Discussion of Biases

This paper uses artificially generated images of homes from AI2-Thor. Because of the limited variety of homes, a model performing well on this dataset might not perform well in the context of other homes (e.g. of different designs, from different cultures, etc.)

### Other Known Limitations

This dataset is small, so updating it to include a greater diversity of actions / objects would be very useful. If these actions / objects are added to AI2-Thor, more data can be collected using the script on our [GitHub repo](https://github.com/hannamw/ACT-Thor).

## Additional Information

### Dataset Curators

Michael Hanna (m.w.hanna@uva.nl), Federico Pedeni (federico.pedeni@studenti.unitn.it)

### Licensing Information

Creative Commons 4.0

### Citation Information

Please cite the associated COLING 2022 paper, "Paper ACT-Thor: A Controlled Benchmark for Embodied Action Understanding in Simulated Environments". The full citation will be added here when the paper is published.

### Contributions

Thanks to [@hannamw](https://github.com/hannamw) for adding this dataset.