---
license:
- cc-by-nc-sa-4.0
converted_from: kaggle
kaggle_id: roamresearch/prescriptionbasedprediction
---

# Dataset Card for Prescription-based prediction

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

- **Homepage:** https://kaggle.com/datasets/roamresearch/prescriptionbasedprediction
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

This is the dataset used in the Roam blog post [Prescription-based prediction](http://roamanalytics.com/2016/09/13/prescription-based-prediction/). It is derived from a variety of US open health datasets, but the bulk of the data points come from the [Medicare Part D](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Part-D-Prescriber.html) dataset and the [National Provider Identifier](https://npiregistry.cms.hhs.gov) dataset.

The prescription vector for each doctor tells a rich story about that doctor's attributes, including specialty, gender, age, and region. There are 239,930 doctors in the dataset.

The file is in JSONL format (one JSON record per line):

<pre>
{
    'provider_variables': 
        {
            'brand_name_rx_count': int,
            'gender': 'M' or 'F',
            'generic_rx_count': int,
            'region': 'South' or 'MidWest' or 'Northeast' or 'West',
            'settlement_type': 'non-urban' or 'urban'
            'specialty': str
            'years_practicing': int
        },
     'npi': str,
     'cms_prescription_counts':
        {
            `drug_name`: int, 
            `drug_name`: int, 
            ...
        }
}
</pre>

The brand/generic classifications behind `brand_name_rx_count` and `generic_rx_count` are defined heuristically.
For more details, see [the blog post](http://roamanalytics.com/2016/09/13/prescription-based-prediction/) or go directly to [the associated code](https://github.com/roaminsight/roamresearch/tree/master/BlogPosts/Prescription_based_prediction).

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

This dataset was shared by [@roamresearch](https://kaggle.com/roamresearch)

### Licensing Information

The license for this dataset is cc-by-nc-sa-4.0

### Citation Information

```bibtex
[More Information Needed]
```

### Contributions

[More Information Needed]