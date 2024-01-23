---
annotations_creators:
- expert-generated
language:
- en
language_creators: []
license:
- cc-by-nc-sa-4.0
multilinguality: []
pretty_name: MapReader Data SIGSPATIAL 2022
size_categories:
- 10K<n<100K
source_datasets: []
tags:
- maps
- historical
- National Library of Scotland
- heritage
- humanities
task_categories:
- image-classification
task_ids:
- multi-class-image-classification
---

# Gold standards and outputs

## Dataset Description

- MapReader’s GitHub: https://github.com/Living-with-machines/MapReader 
- MapReader paper: https://dl.acm.org/doi/10.1145/3557919.3565812
- Zenodo link for gold standards and outputs: https://doi.org/10.5281/zenodo.7147906
- Contacts: Katherine McDonough, The Alan Turing Institute, kmcdonough at turing.ac.uk; Kasra Hosseini, The Alan Turing Institute, k.hosseinizad at gmail.com

### Dataset Summary

Here we share gold standard annotations and outputs from early experiments using MapReader. MapReader creates datasets for humanities research using historical map scans and metadata as inputs. 

Using maps provided by the National Library of Scotland, these annotations and outputs reflect labeling tasks relevant to historical research on the [Living with Machines](https://livingwithmachines.ac.uk/) project.

Data shared here is derived from maps printed in nineteenth-century Britain by the Ordnance Survey, Britain's state mapping agency. These maps cover England, Wales, and Scotland from 1888 to 1913.

## Directory structure

The gold standards and outputs are stored on [Zenodo](https://doi.org/10.5281/zenodo.7147906). It contains the following directories/files:

```
MapReader_Data_SIGSPATIAL_2022
├── README
├── annotations
│   ├── maps
│   │   ├── map_100942121.png
│   │   ├── ...
│   │   └── map_99383316.png
│   ├── slice_meters_100_100
│   │   ├── test
│   │   │   ├── patch-...PNG
│   │   │   ├── ...
│   │   │   └── patch-...PNG
│   │   ├── train
│   │   │   ├── patch-...PNG
│   │   │   ├── ...
│   │   │   └── patch-...PNG
│   │   └── val
│   │       ├── patch-...PNG
│   │       ├── ...
│   │       └── patch-...PNG
│   ├── test.csv
│   ├── train.csv
│   └── valid.csv
└── outputs
    ├── label_01_03
    │   ├── pred_01_03_all.csv
    │   ├── pred_01_03_keep_01_0250.csv
    │   ├── pred_01_03_keep_05_0500.csv
    │   └── pred_01_03_keep_10_1000.csv
    ├── label_02
    │   ├── pred_02_all.csv
    │   ├── pred_02_keep_01_0250.csv
    │   ├── pred_02_keep_05_0500.csv
    │   └── pred_02_keep_10_1000.csv
    ├── patches_all.csv
    ├── percentage
    │   └── pred_02_keep_1_250_01_03_keep_1_250_percentage.csv
    └── resources
        ├── StopsGB4paper.csv
        └── six_inch4paper.json
```

## annotations

The `annotations` directory is as follows:

```
├── annotations
│   ├── maps
│   │   ├── map_100942121.png
│   │   ├── ...
│   │   └── map_99383316.png
│   ├── slice_meters_100_100
│   │   ├── test
│   │   │   ├── patch-...PNG
│   │   │   ├── ...
│   │   │   └── patch-...PNG
│   │   ├── train
│   │   │   ├── patch-...PNG
│   │   │   ├── ...
│   │   │   └── patch-...PNG
│   │   └── val
│   │       ├── patch-...PNG
│   │       ├── ...
│   │       └── patch-...PNG
│   ├── test.csv
│   ├── train.csv
│   └── valid.csv
```

### annotations/train.csv, valid.csv and test.csv

In the `MapReader_Data_SIGSPATIAL_2022/annotations` directory, there are three CSV files, namely `train.csv`, `valid.csv` and `test.csv`. These files have two columns:

```
image_id,label
slice_meters_100_100/train/patch-1390-3892-1529-4031-#map_101590193.png#.PNG,0
slice_meters_100_100/train/patch-1716-3960-1848-4092-#map_101439245.png#.PNG,0
...
```

in which:

- `image_id`: path to each labelled patch. For example in `slice_meters_100_100/train/patch-1390-3892-1529-4031-#map_101590193.png#.PNG`:
    - `slice_meters_100_100/train`: directory where the patch is stored. (in this example, it is a patch used for training)
    - `patch-1390-3892-1529-4031-#map_101590193.png#.PNG` has two parts itself: `patch-1390-3892-1529-4031` is the patch ID, and the patch itself is extracted from `map_101590193.png` map sheet.
- `label`: label assigned to each patch by an annotator.
    - Labels: 0: no [building or railspace]; 1: railspace; 2: building; and 3: railspace and [non railspace] building.

### annotations/slice_meters_100_100

Patches used for training, validation, and test in PNG format.

```
├── annotations
│   ├── slice_meters_100_100
│   │   ├── test
│   │   │   ├── patch-...PNG
│   │   │   ├── ...
│   │   │   └── patch-...PNG
│   │   ├── train
│   │   │   ├── patch-...PNG
│   │   │   ├── ...
│   │   │   └── patch-...PNG
│   │   └── val
│   │       ├── patch-...PNG
│   │       ├── ...
│   │       └── patch-...PNG
```

### annotations/maps

Map sheets retrieved from the National Library of Scotland via webservers. These maps were later sliced into patches which can be found in `annotations/slice_meters_100_100`.

```
├── annotations
│   ├── maps
│   │   ├── map_100942121.png
│   │   ├── ...
│   │   └── map_99383316.png
```

## outputs

The `outputs` directory is as follows:

```
└── outputs
    ├── label_01_03
    │   ├── pred_01_03_all.csv
    │   ├── pred_01_03_keep_01_0250.csv
    │   ├── pred_01_03_keep_05_0500.csv
    │   └── pred_01_03_keep_10_1000.csv
    ├── label_02
    │   ├── pred_02_all.csv
    │   ├── pred_02_keep_01_0250.csv
    │   ├── pred_02_keep_05_0500.csv
    │   └── pred_02_keep_10_1000.csv
    ├── patches_all.csv
    ├── percentage
    │   └── pred_02_keep_1_250_01_03_keep_1_250_percentage.csv
    └── resources
        ├── StopsGB4paper.csv
        └── six_inch4paper.json
```

### outputs/label_01_03

Starting with:

```
└── outputs
    ├── label_01_03
    │   ├── pred_01_03_all.csv
    │   ├── pred_01_03_keep_01_0250.csv
    │   ├── pred_01_03_keep_05_0500.csv
    │   └── pred_01_03_keep_10_1000.csv
```

The file `pred_01_03_all.csv` contains the following columns:

```
,center_lon,center_lat,pred,conf,mean_pixel_RGB,std_pixel_RGB,mean_pixel_A,image_id,parent_id,pub_date,url,x,y,z,opening_year_quicks,closing_year_quicks,dist2quicks
0,-0.4011055106547341,52.61260776720805,1,0.9898980855941772,0.8450341820716858,0.1668068021535873,1.0,patch-3014-0-3151-137-#map_100890251.png#.PNG,map_100890251.png,1902,https://maps.nls.uk/view/100890251,3880925.8529841416,-27169.29919979412,5044483.051365171,1867,1929,1121.9150481268305
1,-0.399645312864389,52.61260776720805,1,0.9999995231628418,0.823089599609375,0.1925655305385589,1.0,patch-3151-0-3288-137-#map_100890251.png#.PNG,map_100890251.png,1902,https://maps.nls.uk/view/100890251,3880926.544140446,-27070.392789791513,5044483.051365171,1867,1929,1113.0714735200893
...
```

- **center_lon**: longitude of the patch center
- **center_lat**: latitude of the patch center
- **pred**: predicted label for the patch
- **conf**: model confidence
- **mean_pixel_RGB**: mean pixel intensities, using all three channels
- **std_pixel_RGB**: standard deviations of pixel intensities, using all three channels
- **mean_pixel_A**: mean pixel intensities of alpha channel
- **image_id**: patch ID
- **parent_id**: ID of the map sheet that the patch belongs to
- **pub_date**: publication date of the map sheet that the patch belongs to
- **url**: URL of the map sheet that the patch belongs to
- **x, y, z**: to compute distances (using k-d tree)
- **opening_year_quicks**: Date when the railway station first opened
- **closing_year_quicks**: Date when the railway station last closed,
- **dist2quicks**: distance to the closest StopsGB in meters.

NB: See `outputs/resources` below for description of the StopsGB (railway station) data and links to related publications.

---

The other files in `outputs/label_01_03` have the same columns as `pred_01_03_all.csv` (described above). The difference is:

- `pred_01_03_all.csv`: all patches predicted as labels 1 (railspace) or 3 (railspace and [non railspace] building).
- `pred_01_03_keep_01_0250.csv`: similar to `pred_01_03_all.csv` except that we removed those patches that had no other neighboring patches with the same label within a radius of 250 meters. Note 01 and 0250 in the name. 01 means one neighboring patch and 0250 means 250 meters.
- `pred_01_03_keep_05_0500.csv`: similar to `pred_01_03_all.csv` except that we removed those patches that had less than five neighboring patches with the same label within a radius of 500 meters.
- `pred_01_03_keep_10_1000.csv`: similar to `pred_01_03_all.csv` except that we removed those patches that had less than ten neighboring patches with the same label within a radius of 1000 meters.

### outputs/label_02

Next, these files:

```
    ├── label_02
    │   ├── pred_02_all.csv
    │   ├── pred_02_keep_01_0250.csv
    │   ├── pred_02_keep_05_0500.csv
    │   └── pred_02_keep_10_1000.csv
```

Are the same as the files described above for `label_01_03` except for label 02 (i.e., building).


### outputs/patches_all.csv

And last:

```
└── outputs
    ├── patches_all.csv
```

The file `patches_all.csv` has the following columns:

⚠️ this file contains the results for 30,490,411 patches used in the MapReader paper.

```
center_lat,center_lon,pred
52.61260776720805,-0.4332298620423274,0
52.61260776720805,-0.4317696642519822,0
...
```

in which:

- **center_lon**: longitude of the patch center
- **center_lat**: latitude of the patch center
- **pred**: predicted label for the patch


### outputs/percentage

We have added one file in `outputs/percentage`:

```
└── outputs
    ├── percentage
    │   └── pred_02_keep_1_250_01_03_keep_1_250_percentage.csv
```

This file has the following columns:

```
,center_lon,center_lat,pred,conf,mean_pixel_RGB,std_pixel_RGB,mean_pixel_A,image_id,parent_id,pub_date,url,x,y,z,dist2rail,dist2quicks,dist2quicks_km,dist2rail_km,dist2rail_minus_station,dist2quicks_km_quantized,dist2rail_km_quantized,dist2rail_minus_station_quantized,perc_neigh_rails,perc_neigh_builds,harmonic_mean_rail_build
0,-0.4040259062354244,52.61260776720805,2,0.9999010562896729,0.8095282316207886,0.1955385357141494,1.0,patch-2740-0-2877-137-#map_100890251.png#.PNG,map_100890251.png,1902,https://maps.nls.uk/view/100890251,3880924.4631095687,-27367.11196679585,5044483.051365171,197.8176497186437,1164.8640633870857,1.1648640633870857,0.1978176497186437,0.9670464136684418,1.0,0.0,0.5,7.198443579766536,4.669260700389105,5.664349046373668
1,-0.4054861040257695,52.61171342293056,2,0.9999876022338868,0.8741853833198547,0.1160899400711059,1.0,patch-2603-137-2740-274-#map_100890251.png#.PNG,map_100890251.png,1902,https://maps.nls.uk/view/100890251,3881002.836728637,-27466.57793328472,5044422.621073416,296.73252022623865,1290.9640259717814,1.2909640259717814,0.2967325202262386,0.9942315057455428,1.0,0.0,0.5,7.050092764378478,4.452690166975881,5.45813633371237
...
```

in which:

- **center_lon**: longitude of the patch center
- **center_lat**: latitude of the patch center
- **pred**: predicted label for the patch
- **conf**: model confidence
- **mean_pixel_RGB**: mean pixel intensities, using all three channels
- **std_pixel_RGB**: standard deviations of pixel intensities, using all three channels
- **mean_pixel_A**: mean pixel intensities of alpha channel
- **image_id**: patch ID
- **parent_id**: ID of the map sheet that the patch belongs to
- **pub_date**: publication date of the map sheet that the patch belongs to
- **url**: URL of the map sheet that the patch belongs to
- **x, y, z**: to compute distances (using k-d tree)
- **dist2rail**: distance to the closest railspace patch (i.e., the patch that is classified as 1: railspace or 3: railspace and [non railspace] building)
- **dist2quicks**: distance to the closest StopsGB station in meters.
- **dist2quicks_km**: distance to the closest StopsGB station in km.
- **dist2rail_km**: similar to **dist2rail** except in km.
- **dist2rail_minus_station**: | dist2rail_km - dist2quicks_km |
- **dist2quicks_km_quantized**: discrete version of **dist2quicks_km**, we used these intervals: [0. , 0.5), [0.5, 1.), [1., 1.5), ... , [4.5, 5.) and [5., inf).
- **dist2rail_km_quantized**: discrete version of **dist2rail_km**, we used these intervals: [0. , 0.5), [0.5, 1.), [1., 1.5), ... , [4.5, 5.) and [5., inf).
- **dist2rail_minus_station_quantized**: discrete version of **dist2rail_minus_station**, we used these intervals: [0. , 0.5), [0.5, 1.), [1., 1.5), ... , [4.5, 5.) and [5., inf).
- **perc_neigh_rails**: what is the percentage of neighboring patches predicted as rail (labels 01 and 03).
- **perc_neigh_builds**: what is the percentage of neighboring patches predicted as building (label 02).
- **harmonic_mean_rail_build**: Harmonic mean of *perc_neigh_rails* and **perc_neigh_builds**.

These additional `percentage` attributes shed light on the relationship between 'railspace' and stations, something we explore in further Living with Machines research.

### outputs/resources

Finally, we have the following files:

```
└── outputs
    └── resources
        ├── StopsGB4paper.csv
        └── six_inch4paper.json
```

- `StopsGB4paper.csv`: this is a trimmed down version of StopsGB, a dataset documenting passenger railway stations in Great Britain (see [this link](https://bl.iro.bl.uk/concern/datasets/0abea1b1-2a43-4422-ba84-39b354c8bb09?locale=en) for the complete dataset). We filtered the stations as follows:
    - Keep only stations for which "ghost_entry" and "cross_ref" columns are "False". (These two fields help remove records in the StopsGB dataset that are not actually stations, but relics of the original publication formatting.)
    - "Opening" was NOT "unknown".
    - The map sheet was surveyed during a year when the station was operational (i.e., "opening_year_quicks" <= survey_date_of_map_sheet <= "closing_year_quicks").

You can learn more about the StopsGB dataset and how it was created from this paper:

```
Mariona Coll Ardanuy, Kaspar Beelen, Jon Lawrence, Katherine McDonough, Federico Nanni, Joshua Rhodes, Giorgia Tolfo, and Daniel C.S. Wilson. "Station to Station: Linking and Enriching Historical British Railway Data." In Computational Humanities Research (CHR2021). 2021.
```

```bibtex
@inproceedings{lwm-station-to-station-2021,
    title = "Station to Station: Linking and Enriching Historical British Railway Data",
    author = "Coll Ardanuy, Mariona and
      Beelen, Kaspar and
      Lawrence, Jon and
      McDonough, Katherine and
      Nanni, Federico and
      Rhodes, Joshua and
      Tolfo, Giorgia and
      Wilson, Daniel CS",
    booktitle = "Computational Humanities Research",
    year = "2021",
}
```

- `six_inch4paper.json`: similar to [metadata_OS_Six_Inch_GB_WFS_light.json](https://github.com/Living-with-machines/MapReader/blob/main/mapreader/persistent_data/metadata_OS_Six_Inch_GB_WFS_light.json) on MapReader's GitHub with some minor changes.

## Dataset Creation

### Curation Rationale

These annotations of map patches are part of a research project to develop humanistic methods for structuring visual information on digitized historical maps. Dividing thousands of nineteenth-century map sheets into 100m x 100m patches and labeling those patches with historically-meaningful concepts diverges from traditional methods for creating data from maps, both in terms of scale (the number of maps being examined), and of type (raster-style patches vs. pixel-level vector data). For more on the rationale for this approach, see the following paper:

```
Kasra Hosseini, Katherine McDonough, Daniel van Strien, Olivia Vane, Daniel C S Wilson, Maps of a Nation? The Digitized Ordnance Survey for New Historical Research, *Journal of Victorian Culture*, Volume 26, Issue 2, April 2021, Pages 284–299.
```

```bibtex
@article{hosseini_maps_2021,
	title = {Maps of a Nation? The Digitized Ordnance Survey for New Historical Research},
	volume = {26},
	rights = {All rights reserved},
	issn = {1355-5502},
	url = {https://doi.org/10.1093/jvcult/vcab009},
	doi = {10.1093/jvcult/vcab009},
	shorttitle = {Maps of a Nation?},
	pages = {284--299},
	number = {2},
	journaltitle = {Journal of Victorian Culture},
	author = {Hosseini, Kasra and {McDonough}, Katherine and van Strien, Daniel and Vane, Olivia and Wilson, Daniel C S},
	urldate = {2021-05-19},
	date = {2021-04-01},
}
```

### Source Data

#### Initial Data Access

Data was accessed via the National Library of Scotland's Historical Maps API: https://maps.nls.uk/projects/subscription-api/

The data shared here is derived from the six-inch to one mile sheets printed between 1888-1913: https://maps.nls.uk/projects/subscription-api/#gb6inch 

### Annotations and Outputs

The annotations and output datasets collected here are related to experiments to identify the 'footprint' of rail infrastructure in the UK, a concept we call 'railspace'. We also created a dataset to identify buildings on the maps.

#### Annotation process

The custom annotation interface built into MapReader is designed specifically to assist researchers in labeling patches relevant to concepts of interest to their research questions. 

Our **guidelines** for the data shared here were:
- for any non-null label (railspace, building, or railspace + building), if a patch contains any visual signal for that label (e.g. 'railspace'), it should be assigned the relevant label. For example, if it is possible for an annotator to see a railway track passing through the corner of a patch, that patch is labeled as 'railspace'.
- the context around the patch should not be used as an aid in extreme cases where it is nearly impossible to determine whether a patch contains a non-null label
- however, the patch context shown in the annotation interface can be used to quickly distinguish between different content types, particularly where the contiguity of a type across patches is useful in determining what label to assign
- for 'railspace': use this label for any type of rail infrastructure as determined by expert labelers. This includes, for example, single-track mining railroads; larger double-track passenger routes; sidings and embankments; etc. It excludes urban trams.
- for 'building': use this label for any size building
- for 'building + railspace': use this label for patches combining these two types of content

Because 'none' (e.g. null) patches made up the vast majority of patches in the total dataset from these map sheets, we ordered patches to annotate based on their pixel intensity. This allowed us to focus first on patches containing more visual content printed on the map sheet, and later to move more quickly through the patches that captured parts of the map with little to no printed features.


#### Who are the annotators?

Data shared here was annotated by Kasra Hosseini and Katherine McDonough.

Members of the Living with Machines research team contributed early annotations during the development of MapReader: Ruth Ahnert, Kaspar Beelen, Mariona Coll-Ardanuy, Emma Griffin, Tim Hobson, Jon Lawrence, Giorgia Tolfo, Daniel van Strien, Olivia Vane, and Daniel C.S. Wilson.

## Credits and re-use terms 

### MapReader outputs

The files shared here (other than ```resources```) under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (https://creativecommons.org/licenses/by-nc-sa/4.0/) (CC-BY-NC-SA) licence. 

If you are interested in working with OS maps used to create these results, please also note the re-use terms of the original map images and metadata detailed below.

### Digitized maps

MapReader can retrieve maps from NLS (National Library of Scotland) via webservers. For all the digitized maps (retrieved or locally stored), please note the re-use terms:

Use of the digitised maps for commercial purposes is currently restricted by contract. Use of these digitised maps for non-commercial purposes is permitted under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (https://creativecommons.org/licenses/by-nc-sa/4.0/) (CC-BY-NC-SA) licence. Please refer to https://maps.nls.uk/copyright.html#exceptions-os for details on copyright and re-use license.

### Map metadata

We have provided some metadata files in on MapReader’s GitHub page (https://github.com/Living-with-machines/MapReader/tree/main/mapreader/persistent_data). For all these file, please note the re-use terms:

Use of the digitised maps for commercial purposes is currently restricted by contract. Use of these digitised maps for non-commercial purposes is permitted under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (https://creativecommons.org/licenses/by-nc-sa/4.0/) (CC-BY-NC-SA) licence. Please refer to https://maps.nls.uk/copyright.html#exceptions-os for details on copyright and re-use license.

## Acknowledgements

This work was supported by Living with Machines (AHRC grant AH/S01179X/1) and The Alan Turing Institute (EPSRC grant EP/N510129/1). 
Living with Machines, funded by the UK Research and Innovation (UKRI) Strategic Priority Fund, is a multidisciplinary collaboration delivered by the Arts and Humanities Research Council (AHRC), with The Alan Turing Institute, the British Library and the Universities of Cambridge, East Anglia, Exeter, and Queen Mary University of London.