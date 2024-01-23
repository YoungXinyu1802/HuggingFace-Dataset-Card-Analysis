---
license:
- unknown
zenodo_id: '6606485'
converted_from: zenodo
---

# Dataset Card for Electrical half hourly raw and cleaned datasets for Great Britain from 2008-11-05

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

- **Homepage:** https://zenodo.org/record/6606485
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

<p><strong>A journal paper published in Energy Strategy Reviews details the method to create the data.</strong></p>

<p><strong>https://www.sciencedirect.com/science/article/pii/S2211467X21001280</strong></p>

<p>&nbsp;</p>

<p>2021-09-09: Version 6.0.0 was created. Now includes data for the North Sea Link (NSL) interconnector from Great Britain to Norway (https://www.northsealink.com). The previous version (5.0.4) should not be used - as there was an error with interconnector data having a static value over the summer 2021.</p>

<p>&nbsp;</p>

<p>2021-05-05: Version 5.0.0 was created. Datetimes now in ISO 8601 format (with capital letter &#39;T&#39; between the date and time) rather than previously with a space (to RFC 3339 format) and with an offset to identify both UTC and localtime. MW values now all saved as integers rather than floats. Elexon data as always from www.elexonportal.co.uk/fuelhh, National Grid data from&nbsp;https://data.nationalgrideso.com/demand/historic-demand-data &nbsp; Raw data now added again for comparison of pre and post cleaning - to allow for training of additional cleaning methods. If using Microsoft Excel, the T between the date and time can be removed using the =SUBSTITUTE() command - and substitute &quot;T&quot; for a space &quot; &quot;</p>

<p>_____________________________________________________________________________________________________</p>

<p>2021-03-02: Version 4.0.0 was created. Due to a new interconnecter (IFA2 -&nbsp;https://en.wikipedia.org/wiki/IFA-2) being commissioned in Q1 2021, there is an additional column with data from National Grid - this is called &#39;POWER_NGEM_IFA2_FLOW_MW&#39; in the espeni dataset. In addition, National Grid has dropped&nbsp;the column name &#39;FRENCH_FLOW&#39; that used to provide&nbsp;the value for the column&nbsp;&#39;POWER_NGEM_FRENCH_FLOW_MW&#39; in previous espeni versions. However, this has been changed to &#39;IFA_FLOW&#39; in National Grid&#39;s original data, which is now called &#39;POWER_NGEM_IFA_FLOW_MW&#39; in the espeni dataset. Lastly, the IO14 columns have all been dropped by National Grid - and potentially unlikely to appear again in future.</p>

<p>2020-12-02: Version 3.0.0 was created. There was a problem with earlier versions&nbsp;local time format - where the +01:00 value was not carried through into the data properly. Now addressed - therefore - local time now has the format e.g.&nbsp;2020-03-31 20:00:00+01:00 when in British Summer Time.</p>

<p>2020-10-03: Version 2.0.0 was created as it looks like National Grid has&nbsp;had a significant change&nbsp;to the methodology underpinning the embedded wind calculations. The wind profile seems similar to previous values, but with an increasing value in comparison&nbsp;to the value published in earlier&nbsp;the greater the embedded value is. The &#39;new&#39; values are from&nbsp;https://data.nationalgrideso.com/demand/daily-demand-update from 2013.</p>

<p>Previously: raw and cleaned datasets for Great Britain&#39;s&nbsp;publicly available electrical data from&nbsp;Elexon (www.elexonportal.co.uk) and National Grid (https://demandforecast.nationalgrid.com/efs_demand_forecast/faces/DataExplorer). Updated versions with more recent data will be uploaded with a differing&nbsp;version number and doi</p>

<p>All data is released in accordance with Elexon&#39;s disclaimer and reservation of rights.</p>

<p>https://www.elexon.co.uk/using-this-website/disclaimer-and-reservation-of-rights/</p>

<p>This disclaimer is also felt to cover&nbsp;the data from National Grid, and the parsed data from the Energy Informatics Group at the University of Birmingham.</p>

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

The class labels in the dataset are in English

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

This dataset was shared by Grant Wilson, Noah Godfrey

### Licensing Information

The license for this dataset is https://creativecommons.org/licenses/by-nc/4.0/legalcode

### Citation Information

```bibtex
@dataset{grant_wilson_2022_6606485,
  author       = {Grant Wilson and
                  Noah Godfrey},
  title        = {{Electrical half hourly raw and cleaned datasets 
                   for Great Britain from 2008-11-05}},
  month        = jun,
  year         = 2022,
  note         = {{Grant funding as part of Research Councils (UK) 
                   EP/L024756/1 - UK Energy Research Centre research
                   programme Phase 3 Grant funding as part of
                   Research Councils (UK) EP/V012053/1 - The Active
                   Building Centre Research Programme (ABC RP)}},
  publisher    = {Zenodo},
  version      = {6.0.9},
  doi          = {10.5281/zenodo.6606485},
  url          = {https://doi.org/10.5281/zenodo.6606485}
}
```

### Contributions

[More Information Needed]