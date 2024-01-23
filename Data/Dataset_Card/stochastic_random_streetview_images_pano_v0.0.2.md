---
annotations_creators:
- expert-generated
language: []
language_creators:
- expert-generated
license:
- mit
multilinguality:
- multilingual
pretty_name: panoramic, street view images of random places on Earth
size_categories:
- 10K<n<100K
source_datasets:
- original
tags: []
task_categories:
- image-classification
task_ids:
- multi-label-image-classification
---

# Dataset Card for panoramic street view images (v.0.0.2)

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

- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

The random streetview images dataset are labeled, panoramic images scraped from randomstreetview.com. Each image shows a location
accessible by Google Streetview that has been roughly combined to provide ~360 degree view of a single location. The dataset was designed with the intent to geolocate an image purely based on its visual content.

### Supported Tasks and Leaderboards

None as of now!

### Languages

labels: Addresses are written in a combination of English and the official language of country they belong to.

images: There are some images with signage that can contain a language. Albeit, they are less common.

## Dataset Structure

For now, images exist exclusively in the `train` split and it is at the user's discretion to split the dataset how they please.

### Data Instances

For each instance, there is:
- timestamped file name: '{YYYYMMDD}_{address}.jpg`
- the image
- the country iso-alpha2 code
- the latitude
- the longitude
- the address 

Fore more examples see the [dataset viewer](https://huggingface.co/datasets/stochastic/random_streetview_images_pano_v0.0.2/viewer/stochastic--random_streetview_images_pano_v0.0.2/train)
```
{
filename: '20221001_Jarše Slovenia_46.1069942_14.9378597.jpg'
country_iso_alpha2 : 'SI'
latitude: '46.028223'
longitude: '14.345106'
address: 'Jarše Slovenia_46.1069942_14.9378597'
}

```

### Data Fields

- country_iso_alpha2: a unique 2 character code for each country in the world following the ISO 3166 standard
- latitude: the angular distance of a place north or south of the earth's equator
- longitude: the angular distance of a place east or west of the standard meridian of the Earth
- address: the physical address written from most micro -> macro order (Street, Neighborhood, City, State, Country)

### Data Splits

'train': all images are currently contained in the 'train' split

## Dataset Creation

### Curation Rationale

Google StreetView Images [requires money per image scraped](https://developers.google.com/maps/documentation/streetview/usage-and-billing).

This dataset provides about 10,000 of those images for free.

### Source Data

#### Who are the source image producers?

Google Street View provide the raw image, this dataset combined various cuts of the images into a panoramic.

[More Information Needed]

### Annotations

#### Annotation process

The address, latitude, and longitude are all scraped from the API response. While portions of the data has been manually validated, the assurance in accuracy is based on the correctness of the API response.

### Personal and Sensitive Information

While Google Street View does blur out images and license plates to the best of their ability, it is not guaranteed as can been seen in some photos. Please review [Google's documentation](https://www.google.com/streetview/policy/) for more information


## Considerations for Using the Data

### Social Impact of Dataset

This dataset was designed after inspiration from playing the popular online game, [geoguessr.com[(geoguessr.com). We ask that users of this dataset consider if their geolocation based application will harm or jeopardize any fair institution or system.

### Discussion of Biases

Out of the ~195 countries that exists, this dataset only contains images from about 55 countries. Each country has an average of 175 photos, with some countries having slightly less.

The 55 countries are: 
["ZA","KR","AR","BW","GR","SK","HK","NL","PE","AU","KH","LT","NZ","RO","MY","SG","AE","FR","ES","IT","IE","LV","IL","JP","CH","AD","CA","RU","NO","SE","PL","TW","CO","BD","HU","CL","IS","BG","GB","US","SI","BT","FI","BE","EE","SZ","UA","CZ","BR","DK","ID","MX","DE","HR","PT","TH"]

In terms of continental representation:

| continent              | Number of Countries Represented |
|:-----------------------| -------------------------------:|
| Europe                 |                              30 |
| Asia                   |                              13 |
| South America          |                               5 |
| Africa                 |                               3 |
| North America          |                               3 |
| Oceania                |                               2 |

This is not a fair representation of the world and its various climates, neighborhoods, and overall place. But it's a start!
### Other Known Limitations

As per [Google's policy](https://www.google.com/streetview/policy/): __"Street View imagery shows only what our cameras were able to see on the day that they passed by the location. Afterwards, it takes months to process them. This means that content you see could be anywhere from a few months to a few years old."__

### Licensing Information

MIT License

### Citation Information



### Contributions

Thanks to [@WinsonTruong](https://github.com/WinsonTruong) and [@
David Hrachovy](https://github.com/dayweek) for helping developing this dataset.
This dataset was developed for a Geolocator project with the aforementioned developers, [@samhita-alla](https://github.com/samhita-alla) and [@yiyixuxu](https://github.com/yiyixuxu).

Thanks to [FSDL](https://fullstackdeeplearning.com) for a wonderful class and online cohort.