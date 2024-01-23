# Dataset Card for HowTo100M

## Table of Contents
[Table of Contents](#table-of-contents)
[Dataset Description](#dataset-description)
  [Dataset Summary](#dataset-summary)
  [Dataset Preprocessing](#dataset-preprocessing)
  [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  [Languages](#languages)
[Dataset Structure](#dataset-structure)
  [Data Instances](#data-instances)
  [Data Fields](#data-fields)
  [Data Splits](#data-splits)
[Dataset Creation](#dataset-creation)
  [Curation Rationale](#curation-rationale)
  [Source Data](#source-data)
  [Annotations](#annotations)
  [Personal and Sensitive Information](#personal-and-sensitive-information)
[Considerations for Using the Data](#considerations-for-using-the-data)
  [Social Impact of Dataset](#social-impact-of-dataset)
  [Discussion of Biases](#discussion-of-biases)
  [Other Known Limitations](#other-known-limitations)
[Additional Information](#additional-information)
  [Dataset Curators](#dataset-curators)
  [Licensing Information](#licensing-information)
  [Citation Information](#citation-information)
  [Contributions](#contributions)

## Dataset Description

**Homepage:** [HowTo100M homepage](https://www.di.ens.fr/willow/research/howto100m/)
**Repository:** [Github repo](https://github.com/antoine77340/howto100m)
**Paper:** [HowTo100M: Learning a Text-Video Embedding by Watching Hundred Million Narrated Video Clips](https://github.com/antoine77340/howto100m)
**Point of Contact:** Antoine Miech

### Dataset Summary

HowTo100M is a large-scale dataset of narrated videos with an emphasis on instructional videos where content creators teach complex tasks with an explicit intention of explaining the visual content on screen. HowTo100M features a total of:
136M video clips with captions sourced from 1.2M Youtube videos (15 years of video)
23k activities from domains such as cooking, hand crafting, personal care, gardening or fitness

Each video is associated with a narration available as subtitles automatically downloaded from Youtube.

### Dataset Preprocessing

This dataset does not contain the videos by default. You would need to follow the instructions [here](https://www.di.ens.fr/willow/research/howto100m/) from the dataset creators and fill out a form to get a userd id and a password to download the videos from their server.

Once you have these two, you can fetch the videos by mapping the following function to the `path` column:
```
import requests

USER_ID = "THE_USER_ID"
PASSWORD = "THE_PASSWORD"

def fetch_video(url):
    response = requests.get(url, auth=requests.auth.HTTPBasicAuth(USER_ID, PASSWORD))
    return response.content
```

### Supported Tasks and Leaderboards

`video-to-text`: This dataset can be used to train a model for Video Captioning where the goal is to predict a caption given the video.

### Languages

All captions are in English and are either coming from available YouTube subtitles (manually written) or the output of an Automatic Speech Recognition system.

## Dataset Structure

### Data Instances

Each instance in HowTo100M represents a single video with two lists of start and end of segments and a caption for each segment.

```
{
  'video_id': 'AEytW9ScgCw',
  'path': 'http://howto100m.inria.fr/dataset/AEytW9ScgCw.mp4',
  'category_1': 'Cars & Other Vehicles',
  'category_2': 'Motorcycles',
  'rank': 108,
  'task_description': 'Paint a Motorcycle Tank',
  'starts': [6.019999980926514, 9.449999809265137, 12.539999961853027, 15.449999809265137, 19.5, 23.510000228881836, 24.860000610351562, 27.420000076293945, 29.510000228881836, 33.119998931884766, 34.77000045776367, 40.68000030517578, 42.779998779296875, 45.97999954223633, 48.22999954223633, 51.93000030517578, 101.27999877929688, 112.80999755859375, 120.93000030517578, 123.79000091552734, 127.38999938964844, 134.86000061035156, 142.25999450683594, 145.47999572753906, 148.22000122070312, 150.0399932861328, 152.9499969482422, 154.97000122070312, 158.6300048828125, 159.75999450683594, 164.97999572753906, 166.7899932861328, 170.38999938964844, 174.91000366210938, 181.89999389648438, 184.33999633789062, 188.9499969482422, 194.38999938964844, 197.0, 201.11000061035156, 202.07000732421875, 247.32000732421875, 254.0399932861328, 256.8500061035156, 260.20001220703125, 271.4599914550781, 272.0, 276.55999755859375, 277.3399963378906, 281.6600036621094, 284.05999755859375, 287.5299987792969, 289.5799865722656, 291.5299987792969, 293.8699951171875, 296.0899963378906, 302.80999755859375, 309.0799865722656, 313.5199890136719, 317.17999267578125, 319.7200012207031, 323.0299987792969, 327.0799865722656, 329.1199951171875, 331.7799987792969, 335.3800048828125, 337.489990234375, 340.42999267578125, 345.1300048828125, 348.5899963378906, 351.1600036621094, 354.75, 357.0, 358.739990234375, 360.239990234375, 364.739990234375, 365.9100036621094, 367.5, 369.8399963378906, 371.2799987792969, 373.260009765625, 395.7699890136719, 401.9800109863281, 404.7799987792969, 406.9100036621094, 410.1499938964844, 415.05999755859375, 419.05999755859375, 427.5199890136719, 431.69000244140625, 433.42999267578125],
  'ends': [12.539999961853027, 15.449999809265137, 19.5, 23.510000228881836, 24.860000610351562, 27.420000076293945, 29.510000228881836, 33.119998931884766, 34.77000045776367, 36.93000030517578, 40.68000030517578, 45.97999954223633, 48.22999954223633, 51.93000030517578, 56.529998779296875, 56.529998779296875, 105.38999938964844, 119.25, 127.38999938964844, 134.86000061035156, 141.33999633789062, 141.33999633789062, 148.22000122070312, 150.0399932861328, 152.9499969482422, 154.97000122070312, 158.6300048828125, 159.75999450683594, 164.97999572753906, 166.7899932861328, 170.38999938964844, 174.91000366210938, 181.17999267578125, 181.17999267578125, 188.9499969482422, 194.38999938964844, 197.0, 201.11000061035156, 202.07000732421875, 204.0800018310547, 218.30999755859375, 256.8500061035156, 260.20001220703125, 264.2799987792969, 271.4599914550781, 276.55999755859375, 277.3399963378906, 281.6600036621094, 284.05999755859375, 287.5299987792969, 289.5799865722656, 291.5299987792969, 293.8699951171875, 296.0899963378906, 302.80999755859375, 309.0799865722656, 313.5199890136719, 317.17999267578125, 319.7200012207031, 323.0299987792969, 327.0799865722656, 329.1199951171875, 331.7799987792969, 335.3800048828125, 337.489990234375, 340.42999267578125, 345.1300048828125, 348.5899963378906, 351.1600036621094, 354.75, 357.0, 358.739990234375, 360.239990234375, 364.739990234375, 365.9100036621094, 367.5, 369.8399963378906, 371.2799987792969, 373.260009765625, 378.2099914550781, 379.4200134277344, 404.7799987792969, 406.9100036621094, 410.1499938964844, 415.05999755859375, 419.05999755859375, 427.5199890136719, 431.69000244140625, 433.42999267578125, 436.1300048828125, 438.8299865722656],
  'captions': ['melt alright', 'watching', 'dad stripping paint', 'gas bike frame 1979', 'yamaha xs 1100 got', 'engine rebuilt', 'stripping paint', 'priming bike', 'frame lot time ops', 'stuff bunch information', 'questions', 'stuff stuff bought', 'description use links', 'questions comment', 'brush stuff', 'literally bubbles middle', 'bring into', "here's got stripper", 'wash using', 'stripper removes chemical things', 'rust primer', 'stripping bike use', 'showed', 'mason jar', 'painted melted', 'brush pain', 'get hands burn', 'bad gloves', 'burn gloves', 'burn', 'careful using stuff', 'nasty stuff instead', 'making mess paint brush', 'use spray version', 'leo watches lot stuff', 'nasty paint', 'cbg said rust lot', 'hard rush mean', 'able get time ups', 'time', 'applause', 'use', 'says 30 minutes', 'soak get', 'corners type brush get', 'works', 'coat', 'stuff', 'rust borrow sodium', 'stuff awesome', 'spent think 6', 'rust used used little ah', "use he's little brush", 'brush', 'doing 15 20', 'minutes mean ate rest away', 'majority', 'rust alright', "primed pretty didn't", 'way hang set', 'board use', 'self etching primer', 'sides pretty step', "haven't leaned", 'get', 'touch areas', '400 grit sandpaper', 'rust oleum says use sand', 'little', 'looking good', 'little holes taped little', 'threads took screw', 'went into hole', 'screwed into lot paint', 'wet bed damp', 'screwed', 'clump screwed', 'way little', 'paint come threads', 'way flip threads clean', "here's hyperlapse spray pit", "alright here's frame primed", 'currently flash', 'little imperfection definitely', 'big mistake', 'think', "didn't go direction bar", 'primed 24', 'hours ready sanded alright', 'watching forget', 'subscribe videos']
}
```

### Data Fields

`video_id`: YouTube video ID
`path`: Path to download the videos from the authors once proper access is accredited
`category_1`: Highest level task category from WikiHow
`category_2`: Second highest level task category from WikiHow
`rank`: YouTube serach result rank of the video when querying the task
`starts`: List corresponding to the end timestamps of each segment
`ends`: List corresponding to the end timestamps of each segment
`captions`: List of all the captions (one per segment)

### Data Splits

All the data is contained in training split. The training set has 1M instances.

## Dataset Creation

### Curation Rationale

From the paper:
> we first start by acquiring a large list of activities using WikiHow1 – an online resource that contains 120,000 articles on How to ... for a variety of domains ranging from cooking to human relationships structured in a hierarchy. We are primarily interested in “visual tasks” that involve some interaction with the physical world (e.g. Making peanut butter, Pruning a tree) as compared to others that are more abstract (e.g. Ending a toxic relationship, Choosing a gift). To obtain predominantly visual tasks, we limit them to one of 12 categories (listed in Table 2). We exclude categories such as Relationships and Finance and Business, that may be more abstract. We further refine the set of tasks, by filtering them in a semi-automatic way. In particular, we restrict the primary verb to physical actions, such as make, build and change, and discard non-physical verbs, such as be, accept and feel. This procedure yields 23,611 visual tasks in total.

> We search for YouTube videos related to the task by forming a query with how to preceding the task name (e.g. how to paint furniture). We choose videos that have English subtitles either uploaded manually, generated automatically by YouTube ASR, or generated automatically after translation from a different language by YouTube API. We improve the quality and consistency of the dataset, by adopting the following criteria. We restrict to the top 200 search results, as the latter ones may not be related to the query task. Videos with less than 100 views are removed as they are often of poor quality or are amateurish. We also ignore videos that have less than 100 words as that may be insufficient text to learn a good video-language embedding. Finally, we remove videos longer than 2,000 seconds. As some videos may appear in several tasks, we deduplicate videos based on YouTube IDs. However, note that the dataset may still contain duplicates if a video was uploaded several times or edited and re-uploaded. Nevertheless, this is not a concern at our scale.

### Source Data

The source videos come from YouTube.

#### Initial Data Collection and Normalization

#### Who are the source language producers?

YouTube uploaders.

### Annotations

#### Annotation process

Subtitles are generated or manually written. Note that the narrated captions have been processed. In fact, authors have removed a significant number of stop words
which are not relevant for the learning of the text-video joint embedding. The list of stop words can be found here: https://github.com/antoine77340/howto100m/blob/master/stop_words.py. You can find the unprocessed caption file (i.e. with stop words) [here](https://www.rocq.inria.fr/cluster-willow/amiech/howto100m/raw_caption.zip).

#### Who are the annotators?

YouTube uploaders or machine-generated outputs.

### Personal and Sensitive Information

## Considerations for Using the Data

### Social Impact of Dataset

### Discussion of Biases

### Other Known Limitations

## Additional Information

### Dataset Curators

Antoine Miech, Dimitri Zhukov, Jean-Baptiste Alayrac, Makarand Tapaswi, Ivan Laptev, Josef Sivic

### Licensing Information

Not specified.

### Citation Information

```bibtex
@inproceedings{miech19howto100m,
   title={How{T}o100{M}: {L}earning a {T}ext-{V}ideo {E}mbedding by {W}atching {H}undred {M}illion {N}arrated {V}ideo {C}lips},
   author={Miech, Antoine and Zhukov, Dimitri and Alayrac, Jean-Baptiste and Tapaswi, Makarand and Laptev, Ivan and Sivic, Josef},
   booktitle={ICCV},
   year={2019},
}
```

### Contributions

Thanks to [@VictorSanh](https://github.com/VictorSanh) for adding this dataset.
