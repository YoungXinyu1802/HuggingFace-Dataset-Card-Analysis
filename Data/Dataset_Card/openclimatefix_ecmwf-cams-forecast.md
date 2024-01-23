---
license: mit
---

# Dataset Card for ECMWF CAMS Forecast

## Dataset Description

- **Homepage: https://ads.atmosphere.copernicus.eu/cdsapp#!/dataset/cams-europe-air-quality-forecasts?tab=overview
- **Repository:** 
- **Paper:** 
- **Leaderboard:** 
- **Point of Contact: jacob@openclimatefix.org

### Dataset Summary

This is a dataset of converted ECMWF CAMS Air Quality forecasts over Europe on a 0.1x0.1 degree grid. The data is available on a 3-year rolling archive, so this repo is attempting to keep more of that data public.
The data has been converted to Zarr, and only the height levels of 0m,50m, 250m,500m,1000m,2000m,3000m,and 5000m have been kept. 
Additionally, the forecasts go out to 96 hours from ECMWF, but this dataset only contains forecasts up to 48 hours into the future, as it is more focused on being useful for short-term solar forecasting over the next 48 hours, and to reduce file size.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

Each day is a Zarr containing 13 different aerosols on the 6 height levels, going out 48 hourly-timesteps to the future, from midnight on that day. These can be opened with Zarr, and have been chunked into quarters spatially (along latitude and longitude),
and in a single chunk temporally and height-wise. In other words, each variable has 4 chunks. No data has been modified or changed from the original values.

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

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

[More Information Needed]