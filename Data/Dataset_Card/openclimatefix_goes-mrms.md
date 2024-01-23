# Dataset Card for Goes-MRMS

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** [Needs More Information]
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

This dataset is a combination of GOES-16 data and MRMS radar precipitation data to roughly match the unreleased dataset used to train Google Research's MetNet. In the papers they used GOES-16 satellite imagery, MultiRadar/Multi-System (MRMS) instantaneous precipitation, hourly cumulative precipitation, and High Resolution Rapid Refresh NWP initializations as inputs to predict future MRMS precipitation rates. The precipitation rates were binned into 0.2mm/hr bins to make the output a classification task, and allow for the models to predict a probability distribution over the region of interest. 

 Additionally, the input image patches are much larger than the target image patches. For MetNet, the input images covered 512x512 km area, while the target was the center 64x64 km crop. For MetNet-2 the input covered 2048x2048 km with the target being the central 512x512 km. 

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

[Needs More Information]

## Dataset Structure

### Data Instances

[Needs More Information]

### Data Fields

[Needs More Information]

### Data Splits

MetNet (January 2018-July 2019) (16 days training, 2 days validation, 2 days test)
MetNet-2 (July 2017-August 2020) (Non-overlapping time ranges with 12 hour black outs in between)
Full (July 2017-January 2022) (Train: 2017-2020. except for first of the month, Validation: first of the month July 2017-2020, Test: 2021-2022)

## Dataset Creation

### Curation Rationale

The original curation rationale was for forecasting precipitation rate in a probabilistic way. This dataset covers a different time period than in the original paper, going from July 2017 through December 2021. There is a split available to match the temporal coverage of the original MetNet paper, (Janurary 2018 to July 2019) or the MetNet-2 paper (July 2017 to August 2020).

### Source Data

#### Initial Data Collection and Normalization

From the MetNet paper: "For both MRMS and GOES we acquired data for the period January 2018 through July 2019.  We split the data temporally into three non-overlapping data sets by repeatedly using approximately 16 days for training followed by two days for validation and two days for testing.  From these temporal splits we randomly extracted 13,717 test and validation samples and kept increasing the training set size until we observed no over-fitting at 1.72 million training samples."

From the MetNet-2 paper: "The training data consists of 1,230,585 patches of size 2048 km x 2048 km at the input and targets of size 512 km x 512 km including all 360 (2 to 720 minutes) time slices.  The training area covers a region of 7000x2500 kilometers.  We sample target patches from the input context region minus an all around border of 512 km.  The input context is padded for all regions outside of the 7000x2500 CONUS. The validation data used for developing the models consists of 11,991 patches and the test data of 39,864 patches.  The training, validation and test data are drawn from non-overlapping ranges of hours, with black out periods of 12 hours in between, over a period of observations of 3 years from July 2017 to August 2020.  This ensures that the model does not learn any spurious training and evaluation correlations within any single day.  HRRR only generates forecasts starting at full hours."

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

Jacob Bieker (jacob@openclimatefix.org)
MetNet-1 split: MetNet Authors
MetNet-2 split: MetNet-2 Authors

### Licensing Information

All data is open and without restrictions from NOAA.

### Citation Information

Please cite NOAA as the data provider.