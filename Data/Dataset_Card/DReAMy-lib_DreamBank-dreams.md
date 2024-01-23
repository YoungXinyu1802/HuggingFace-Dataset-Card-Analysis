---
dataset_info:
  features:
  - name: dreams
    dtype: string
  - name: series
    dtype: string
  - name: description
    dtype: string
  splits:
  - name: train
    num_bytes: 27263345
    num_examples: 29345
  download_size: 15525739
  dataset_size: 27263345
license: apache-2.0
task_categories:
- text-generation
language:
- en
- de
size_categories:
- 10K<n<100K
---
# DreamBank - Dreams

The dataset is a collection of ~30k textual reports of dreams, originally scraped from the [DreamBank](https://www.dreambank.net/) databased by 
[`mattbierner`](https://github.com/mattbierner/DreamScrape). The DreamBank reports are divided into `series`, 
which are collections of individuals or research projects/groups that have gathered the dreams. The vast majority  of the series are in the 
English language, but a small part of the are in German. These series are indicated by the presence of `.de` in their name.

## Content
The  dataset revolves around three main features:
- `dreams`: the content of each dream report.
- `series`: the series to which a report belongs
- `description`: a brief description of the `series`

## Series distribution
The following is a summary of (alphabetically ordered) DreamBank's series together with their total amount of dream reports. 

- alta: 422
- angie: 48
- arlie: 212
- b: 3114
- b-baseline: 250
- b2: 1138
- bay_area_girls_456: 234
- bay_area_girls_789: 154
- bea1: 223
- bea2: 63
- blind-f: 238
- blind-m: 143
- bosnak: 53
- chris: 100
- chuck: 75
- dahlia: 24
- david: 166
- dorothea: 899
- ed: 143
- edna: 19
- elizabeth: 1707
- emma: 1221
- emmas_husband: 72
- esther: 110
- german-f.de: 397
- german-m.de: 140
- hall_female: 681
- jasmine1: 39
- jasmine2: 269
- jasmine3: 259
- jasmine4: 94
- jeff: 87
- joan: 42
- kenneth: 2021
- lawrence: 206
- mack: 38
- madeline1-hs: 98
- madeline2-dorms: 186
- madeline3-offcampus: 348
- madeline4-postgrad: 294
- mark: 23
- melissa: 89
- melora: 211
- melvin: 128
- merri: 315
- miami-home: 171
- miami-lab: 274
- midwest_teens-f: 111
- midwest_teens-m: 83
- nancy: 44
- natural_scientist: 234
- norman: 1235
- norms-f: 490
- norms-m: 491
- pegasus: 1093
- peru-f: 381
- peru-m: 384
- phil1: 106
- phil2: 220
- phil3: 180
- physiologist: 86
- ringo: 16
- samantha: 63
- seventh_graders: 69
- toby: 33
- tom: 27
- ucsc_women: 81
- vickie: 35
- vietnam_vet: 98
- vonuslar.de: 6094
- wedding: 65
- west_coast_teens: 89
- zurich-f.de: 164
- zurich-m.de: 135