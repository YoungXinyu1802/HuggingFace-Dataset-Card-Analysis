---
annotations_creators:
- no-annotation
language:
- en
language_creators:
- found
license:
- other
multilinguality:
- monolingual
pretty_name: crello
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- graphic design
- design templates
task_categories:
- unconditional-image-generation
task_ids: []
dataset_info:
  features:
  - name: id
    dtype: string
  - name: length
    dtype: int64
  - name: group
    dtype:
      class_label:
        names:
          '0': BG
          '1': EO
          '2': HC
          '3': MM
          '4': SM
          '5': SMA
  - name: format
    dtype:
      class_label:
        names:
          '0': Album Cover
          '1': Book Cover
          '2': Brochure
          '3': Business card
          '4': Calendar
          '5': Card
          '6': Certificate
          '7': Coupon
          '8': Email header
          '9': FB event cover
          '10': Facebook
          '11': Facebook AD
          '12': Facebook cover
          '13': Flayer
          '14': Gallery Image
          '15': Gift Certificate
          '16': Graphic
          '17': IGTV Cover
          '18': Image
          '19': Infographic
          '20': Instagram
          '21': Instagram AD
          '22': Instagram Highlight Cover
          '23': Instagram Story
          '24': Invitation
          '25': Invoice
          '26': Label
          '27': Large Rectangle
          '28': Leaderboard
          '29': Letterhead
          '30': LinkedIn Cover
          '31': Logo
          '32': Medium Rectangle
          '33': Menu
          '34': Mind Map
          '35': Mobile Presentation
          '36': Mood Board
          '37': Newsletter
          '38': Photo Book
          '39': Pinterest
          '40': Postcard
          '41': Poster
          '42': Poster US
          '43': Presentation
          '44': Presentation Wide
          '45': Proposal
          '46': Recipe Card
          '47': Resume
          '48': Schedule Planner
          '49': Skyscraper
          '50': Snapchat Geofilter
          '51': Snapchat Moment Filter
          '52': Storyboard
          '53': T-Shirt
          '54': Ticket
          '55': Title
          '56': Tumblr
          '57': Twitch Offline Banner
          '58': Twitch Profile Banner
          '59': Twitter
          '60': VK Community Cover
          '61': VK Post with Button
          '62': VK Universal Post
          '63': Web Banner
          '64': Youtube
          '65': Youtube Thumbnail
          '66': Zoom Background
  - name: canvas_width
    dtype:
      class_label:
        names:
          '0': '1000'
          '1': '1008'
          '2': '1024'
          '3': '1080'
          '4': '1128'
          '5': '1190'
          '6': '1200'
          '7': '1280'
          '8': '1296'
          '9': '1500'
          '10': '1590'
          '11': '160'
          '12': '1600'
          '13': '1920'
          '14': '240'
          '15': '241'
          '16': '2560'
          '17': '300'
          '18': '3000'
          '19': '336'
          '20': '360'
          '21': '396'
          '22': '419'
          '23': '420'
          '24': '432'
          '25': '500'
          '26': '537'
          '27': '540'
          '28': '560'
          '29': '576'
          '30': '595'
          '31': '600'
          '32': '635'
          '33': '728'
          '34': '735'
          '35': '792'
          '36': '800'
          '37': '841'
          '38': '842'
          '39': '851'
          '40': '940'
  - name: canvas_height
    dtype:
      class_label:
        names:
          '0': '1055'
          '1': '1080'
          '2': '1102'
          '3': '1200'
          '4': '1296'
          '5': '141'
          '6': '142'
          '7': '1440'
          '8': '1600'
          '9': '1683'
          '10': '1728'
          '11': '191'
          '12': '1920'
          '13': '200'
          '14': '2000'
          '15': '216'
          '16': '2340'
          '17': '240'
          '18': '250'
          '19': '2560'
          '20': '280'
          '21': '288'
          '22': '297'
          '23': '298'
          '24': '315'
          '25': '320'
          '26': '380'
          '27': '400'
          '28': '480'
          '29': '500'
          '30': '504'
          '31': '512'
          '32': '576'
          '33': '595'
          '34': '600'
          '35': '612'
          '36': '628'
          '37': '654'
          '38': '700'
          '39': '720'
          '40': '768'
          '41': '788'
          '42': '810'
          '43': '841'
          '44': '842'
          '45': '90'
  - name: category
    dtype:
      class_label:
        names:
          '0': all
          '1': beauty
          '2': businessFinance
          '3': citiesPlaces
          '4': educationScience
          '5': fashionStyle
          '6': foodDrinks
          '7': handcraftArt
          '8': holidaysCelebration
          '9': homeStuff
          '10': industry
          '11': kidsParents
          '12': leisureEntertainment
          '13': medical
          '14': natureWildlife
          '15': pets
          '16': realEstateBuilding
          '17': religions
          '18': socialActivityCharity
          '19': sportExtreme
          '20': technology
          '21': transportation
          '22': travelsVacations
  - name: title
    dtype: string
  - name: type
    sequence:
      class_label:
        names:
          '0': coloredBackground
          '1': imageElement
          '2': maskElement
          '3': svgElement
          '4': textElement
  - name: left
    sequence: float32
  - name: top
    sequence: float32
  - name: width
    sequence: float32
  - name: height
    sequence: float32
  - name: opacity
    sequence: float32
  - name: text
    sequence: string
  - name: font
    sequence:
      class_label:
        names:
          '0': ''
          '1': Abril Fatface
          '2': Aldrich
          '3': Alef
          '4': Alegreya Sans
          '5': Alfa Slab One
          '6': Alice
          '7': Allerta Stencil
          '8': Allura
          '9': Amatic Sc
          '10': Anton
          '11': Arapey
          '12': Architects Daughter
          '13': Arima Madurai
          '14': Arimo
          '15': Arizonia
          '16': Arkana Script
          '17': Armata
          '18': Assistant
          '19': Bad Script
          '20': Baloo Tamma
          '21': Bangers
          '22': Barrio
          '23': Beacon
          '24': Bebas Neue
          '25': Bellefair
          '26': Bentham
          '27': Berkshire Swash
          '28': Bilbo
          '29': Black Ops One
          '30': Blogger
          '31': Breathe
          '32': Breathe Press
          '33': Brusher
          '34': Brusher Free Font
          '35': Bubbler One
          '36': Buda
          '37': Bungee
          '38': Bungee Shade
          '39': Cabin Sketch
          '40': Caesar Dressing
          '41': Cantarell
          '42': Carter One
          '43': Caveat
          '44': Cedarville Cursive
          '45': Chathura
          '46': Clicker Script
          '47': Comfortaa
          '48': Contrail One
          '49': Cookie
          '50': Copse
          '51': Cormorant Infant
          '52': Courgette
          '53': Cousine
          '54': Covered By Your Grace
          '55': Crete Round
          '56': Cutive Mono
          '57': Damion
          '58': Dancing Script
          '59': David Libre
          '60': Dawning Of A New Day
          '61': Delius
          '62': Delius Swash Caps
          '63': Didact Gothic
          '64': Dorsa
          '65': Dosis
          '66': Droid Serif
          '67': Dukomdesign Constantine
          '68': Eb Garamond
          '69': Economica
          '70': El Messiri
          '71': Elsie
          '72': Elsie Swash Caps
          '73': Euphoria Script
          '74': Ewert
          '75': Exo 2
          '76': Farsan
          '77': Faster One
          '78': Fauna One
          '79': Finger Paint
          '80': Fjalla One
          '81': Forum
          '82': Frank Ruhl Libre
          '83': Fredericka The Great
          '84': Gabriela
          '85': Gaegu
          '86': Geo
          '87': Gfs Didot
          '88': Give You Glory
          '89': Glass Antiqua
          '90': Gluk Glametrix
          '91': Gluk Znikomitno25
          '92': Graduate
          '93': Grand Hotel
          '94': Gravitas One
          '95': Great Vibes
          '96': Gruppo
          '97': Handlee
          '98': Happy Monkey
          '99': Heebo
          '100': Homemade Apple
          '101': Iceberg
          '102': Iceland
          '103': Im Fell
          '104': Im Fell Dw Pica Sc
          '105': Inconsolata
          '106': Italiana
          '107': Italianno
          '108': Jacques Francois Shadow
          '109': Josefin Sans
          '110': Josefin Slab
          '111': Julius Sans One
          '112': Junge
          '113': Jura
          '114': Just Me Again Down Here
          '115': Kalam
          '116': Katibeh
          '117': Kaushan Script
          '118': Kavivanar
          '119': Kelly Slab
          '120': Knewave
          '121': Knewave Outline
          '122': Kreon
          '123': Kristi
          '124': Kumar One
          '125': Kumar One Outline
          '126': Kurale
          '127': La Belle Aurore
          '128': Lalezar
          '129': Lato
          '130': Lauren
          '131': League Script
          '132': Lemon Tuesday
          '133': Libre Baskerville
          '134': Limelight
          '135': Londrina Shadow
          '136': Londrina Sketch
          '137': Loved By The King
          '138': Lovers Quarrel
          '139': Marcellus Sc
          '140': Marck Script
          '141': Mate
          '142': Maven Pro
          '143': Meddon
          '144': Medula One
          '145': Merienda One
          '146': Merriweather
          '147': Mikodacs
          '148': Miriam Libre
          '149': Monda
          '150': Monofett
          '151': Monsieur La Doulaise
          '152': Montserrat
          '153': Montserrat Alternates
          '154': Mr Dafoe
          '155': Mr De Haviland
          '156': Mrs Saint Delafield
          '157': Mrs Sheppards
          '158': Neucha
          '159': Nixie One
          '160': Nothing You Could Do
          '161': Noticia Text
          '162': Nova Square
          '163': Nunito
          '164': Offside
          '165': Okolaks
          '166': Old Standard Tt
          '167': Oleo Script
          '168': Open Sans
          '169': Open Sans Condensed
          '170': Oranienbaum
          '171': Orbitron
          '172': Oswald
          '173': Overlock
          '174': Oxygen
          '175': Pacifico
          '176': Pangolin
          '177': Parisienne
          '178': Pathway Gothic One
          '179': Patrick Hand
          '180': Pattaya
          '181': Patua One
          '182': Permanent Marker
          '183': Petit Formal Script
          '184': Philosopher
          '185': Pinyon Script
          '186': Pirou
          '187': Play
          '188': Playball
          '189': Playfair Display
          '190': Playlist Caps
          '191': Playlist Script
          '192': Podkova
          '193': Poiret One
          '194': Pompiere
          '195': Port Lligat Slab
          '196': Press Start 2P
          '197': Prompt
          '198': Pt Sans
          '199': Quattrocento
          '200': Quicksand
          '201': Racing Sans One
          '202': Radley
          '203': Rakkas
          '204': Raleway
          '205': Raleway Dots
          '206': Rammetto One
          '207': Rationale
          '208': Reem Kufi
          '209': Reenie Beanie
          '210': Righteous
          '211': Rise
          '212': Rissa Typeface
          '213': Roboto
          '214': Rochester
          '215': Rock Salt
          '216': Rokkitt
          '217': Rosario
          '218': Rubik
          '219': Rubik One
          '220': Ruslan Display
          '221': Russo One
          '222': Rye
          '223': Sacramento
          '224': Sansita One
          '225': Satisfy
          '226': Scope One
          '227': Secular One
          '228': Selima Script
          '229': Sensei
          '230': Seymour One
          '231': Shadows Into Light Two
          '232': Share Tech Mono
          '233': Sirin Stencil
          '234': Six Caps
          '235': Source Serif Pro
          '236': Space Mono
          '237': Stalemate
          '238': Stint Ultra Expanded
          '239': Sue Ellen Francisco
          '240': Suez One
          '241': Sunday
          '242': Superclarendon Regular
          '243': Text Me One
          '244': Tinos
          '245': Titillium Web
          '246': Tulpen One
          '247': Underdog
          '248': V T323
          '249': Vampiro One
          '250': Varela Round
          '251': Vast Shadow
          '252': Vollkorn
          '253': Waiting For The Sunrise
          '254': Wire One
          '255': Yanone Kaffeesatz
          '256': Yellowtail
          '257': Yeseva One
          '258': Yesteryear
          '259': Zeyada
          '260': Znikomit
          '261': Znikomitno24
  - name: font_size
    sequence: float32
  - name: text_align
    sequence:
      class_label:
        names:
          '0': ''
          '1': center
          '2': left
          '3': right
  - name: angle
    sequence: float32
  - name: capitalize
    sequence:
      class_label:
        names:
          '0': 'false'
          '1': 'true'
  - name: line_height
    sequence: float32
  - name: letter_spacing
    sequence: float32
  - name: suitability
    sequence:
      class_label:
        names:
          '0': mobile
  - name: keywords
    sequence: string
  - name: industries
    sequence:
      class_label:
        names:
          '0': artCrafts
          '1': beautyCosmetics
          '2': businessFinance
          '3': corporate
          '4': ecologyNature
          '5': educationTraining
          '6': entertainmentLeisure
          '7': familyKids
          '8': fashionStyle
          '9': foodBeverages
          '10': healthWellness
          '11': homeLiving
          '12': hrRecruitment
          '13': marketingAds
          '14': nonProfitCharity
          '15': petsAnimals
          '16': realEstateConstruction
          '17': religionFaith
          '18': retail
          '19': services
          '20': sportFitness
          '21': techGadgets
          '22': transportDelivery
          '23': travelTourism
  - name: color
    sequence:
      sequence: float32
      length: 3
  - name: image
    sequence: image
  splits:
  - name: train
    num_bytes: 3322744283.141
    num_examples: 18659
  - name: test
    num_bytes: 421990602.771
    num_examples: 2371
  - name: validation
    num_bytes: 425905823.995
    num_examples: 2391
  download_size: 4130251706
  dataset_size: 4170640709.9069996
---

# Dataset Card for Crello

## Table of Contents
- [Dataset Card for Crello](#dataset-card-for-crello)
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
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
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

- **Homepage:** [CanvasVAE github](https://github.com/CyberAgentAILab/canvas-vae)
- **Repository:**
- **Paper:** [CanvasVAE: Learning to Generate Vector Graphic Documents](https://arxiv.org/abs/2108.01249)
- **Leaderboard:**
- **Point of Contact:** [Kota Yamaguchi](https://github.com/kyamagu)

### Dataset Summary

The Crello dataset is compiled for the study of vector graphic documents. The dataset contains document meta-data such as canvas size and pre-rendered elements such as images or text boxes. The original templates were collected from [crello.com](https://crello.com) (now [create.vista.com](https://create.vista.com/)) and converted to a low-resolution format suitable for machine learning analysis.

### Supported Tasks and Leaderboards

[CanvasVAE](https://arxiv.org/abs/2108.01249) studies unsupervised document generation.

### Languages

Almost all design templates use English.

## Dataset Structure

### Data Instances

Each instance has scalar attributes (canvas) and sequence attributes (elements). Categorical values are stored as integer values. Check `ClassLabel` features of the dataset for the list of categorical labels.

```
{'id': '592d6c2c95a7a863ddcda140',
 'length': 8,
 'group': 4,
 'format': 20,
 'canvas_width': 3,
 'canvas_height': 1,
 'category': 0,
 'title': 'Beauty Blog Ad Woman with Unusual Hairstyle',
 'type': [1, 3, 3, 3, 3, 4, 4, 4],
 'left': [0.0,
  -0.0009259259095415473,
  0.24444444477558136,
  0.5712962746620178,
  0.2657407522201538,
  0.369228333234787,
  0.2739444375038147,
  0.44776931405067444],
 'top': [0.0,
  -0.0009259259095415473,
  0.37037035822868347,
  0.41296297311782837,
  0.41296297311782837,
  0.8946287035942078,
  0.4549448788166046,
  0.40591198205947876],
 'width': [1.0,
  1.0018517971038818,
  0.510185182094574,
  0.16296295821666718,
  0.16296295821666718,
  0.30000001192092896,
  0.4990740716457367,
  0.11388888955116272],
 'height': [1.0,
  1.0018517971038818,
  0.25833332538604736,
  0.004629629664123058,
  0.004629629664123058,
  0.016611294820904732,
  0.12458471953868866,
  0.02657807245850563],
 'opacity': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
 'text': ['', '', '', '', '', 'STAY WITH US', 'FOLLOW', 'PRESS'],
 'font': [0, 0, 0, 0, 0, 152, 172, 152],
 'font_size': [0.0, 0.0, 0.0, 0.0, 0.0, 18.0, 135.0, 30.0],
 'text_align': [0, 0, 0, 0, 0, 2, 2, 2],
 'angle': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
 'capitalize': [0, 0, 0, 0, 0, 0, 0, 0],
 'line_height': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
 'letter_spacing': [0.0, 0.0, 0.0, 0.0, 0.0, 14.0, 12.55813980102539, 3.0],
 'suitability': [0],
 'keywords': ['beautiful',
  'beauty',
  'blog',
  'blogging',
  'caucasian',
  'cute',
  'elegance',
  'elegant',
  'fashion',
  'fashionable',
  'femininity',
  'glamour',
  'hairstyle',
  'luxury',
  'model',
  'stylish',
  'vogue',
  'website',
  'woman',
  'post',
  'instagram',
  'ig',
  'insta',
  'fashion',
  'purple'],
 'industries': [1, 8, 13],
 'color': [[153.0, 118.0, 96.0],
  [34.0, 23.0, 61.0],
  [34.0, 23.0, 61.0],
  [255.0, 255.0, 255.0],
  [255.0, 255.0, 255.0],
  [255.0, 255.0, 255.0],
  [255.0, 255.0, 255.0],
  [255.0, 255.0, 255.0]],
 'image': [<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=256x256>,
  <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=256x256>,
  <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=256x256>,
  <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=256x256>,
  <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=256x256>,
  <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=256x256>,
  <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=256x256>,
  <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=256x256>]}
```

To get a label for categorical values, use the `int2str` method:

```python
key = "font"
example = dataset[0]

dataset.features[key].int2str(example[key])
```

### Data Fields

In the following, categorical fields are shown as `categorical` type, but the actual storage is `int64`.

**Canvas attributes**

| Field         | Type        | Shape   | Description                                                     |
| ------------- | ----------- | ------- | --------------------------------------------------------------- |
| id            | string      | ()      | Template ID from crello.com                                     |
| group         | categorical | ()      | Broad design groups, such as social media posts or blog headers |
| format        | categorical | ()      | Detailed design formats, such as Instagram post or postcard     |
| category      | categorical | ()      | Topic category of the design, such as holiday celebration       |
| canvas_width  | categorical | ()      | Canvas pixel width                                              |
| canvas_height | categorical | ()      | Canvas pixel height                                             |
| length        | int64       | ()      | Length of elements                                              |
| suitability   | categorical | (None,) | List of display tags, only `mobile` tag exists                  |
| keywords      | string      | (None,) | List of keywords associated to this template                    |
| industries    | categorical | (None,) | List of industry tags like `marketingAds`                       |

**Element attributes**

| Field          | Type        | Shape     | Description                                                          |
| -------------- | ----------- | --------- | -------------------------------------------------------------------- |
| type           | categorical | (None,)   | Element type, such as vector shape, image, or text                   |
| left           | float32     | (None,)   | Element left position normalized to [0, 1] range w.r.t. canvas_width |
| top            | float32     | (None,)   | Element top position normalized to [0, 1] range w.r.t. canvas_height |
| width          | float32     | (None,)   | Element width normalized to [0, 1] range w.r.t. canvas_width         |
| height         | float32     | (None,)   | Element height normalized to [0, 1] range w.r.t. canvas_height       |
| color          | int64       | (None, 3) | Extracted main RGB color of the element                              |
| opacity        | float32     | (None,)   | Opacity in [0, 1] range                                              |
| image          | image       | (None,)   | Pre-rendered 256x256 preview of the element encoded in PNG format    |
| text           | string      | (None,)   | Text content in UTF-8 encoding for text element                      |
| font           | categorical | (None,)   | Font family name for text element                                    |
| font_size      | float32     | (None,)   | Font size (height) in pixels                                         |
| text_align     | categorical | (None,)   | Horizontal text alignment, left, center, right for text element      |
| angle          | float32     | (None,)   | Element rotation angle (radian) w.r.t. the center of the element     |
| capitalize     | categorical | (None,)   | Binary flag to capitalize letters                                    |
| line_height    | float32     | (None,)   | Scaling parameter to line height, default is 1.0                     |
| letter_spacing | float32     | (None,)   | Adjustment parameter for letter spacing, default is 0.0              |

Note that the color and pre-rendered images do not necessarily accurately reproduce the original design templates. The original template is accessible at the following URL if still available.

```
https://create.vista.com/artboard/?template=<template_id>
```

`left` and `top` can be negative because elements can be bigger than the canvas size.

### Data Splits

The Crello dataset has 3 splits: train, validation, and test. The current split is generated such that the same title of the original template shows up in only in one split.

| Split     | Count |
| --------- | ----- |
| train     | 18659 |
| validaton | 2391  |
| test      | 2371  |


### Visualization

Each example can be visualized in the following approach using [`skia-python`](https://kyamagu.github.io/skia-python/). Note the following does not guarantee a similar appearance to the original template. Currently, the quality of text rendering is far from perfect.

```python
import io
from typing import Any, Dict

import numpy as np
import skia


def render(features: datasets.Features, example: Dict[str, Any], max_size: float=512.) -> bytes:
    """Render parsed sequence example onto an image and return as PNG bytes."""
    canvas_width = int(features["canvas_width"].int2str(example["canvas_width"]))
    canvas_height = int(features["canvas_height"].int2str(example["canvas_height"]))

    scale = min(1.0, max_size / canvas_width, max_size / canvas_height)

    surface = skia.Surface(int(scale * canvas_width), int(scale * canvas_height))
    with surface as canvas:
        canvas.scale(scale, scale)
        for index in range(example["length"]):
            pil_image = example["image"][index]
            image = skia.Image.frombytes(
                pil_image.convert('RGBA').tobytes(),
                pil_image.size,
                skia.kRGBA_8888_ColorType)
            left = example["left"][index] * canvas_width
            top = example["top"][index] * canvas_height
            width = example["width"][index] * canvas_width
            height = example["height"][index] * canvas_height
            rect = skia.Rect.MakeXYWH(left, top, width, height)
            paint = skia.Paint(Alphaf=example["opacity"][index], AntiAlias=True)

            angle = example["angle"][index]
            with skia.AutoCanvasRestore(canvas):
                if angle != 0:
                    degree = 180. * angle / np.pi
                    canvas.rotate(degree, left + width / 2., top + height / 2.)
                canvas.drawImageRect(image, rect, paint=paint)

    image = surface.makeImageSnapshot()
    with io.BytesIO() as f:
        image.save(f, skia.kPNG)
        return f.getvalue()
```


## Dataset Creation

### Curation Rationale

The Crello dataset is compiled for the general study of vector graphic documents, with the goal of producing a dataset that offers complete vector graphic information suitable for neural methodologies.

### Source Data

#### Initial Data Collection and Normalization

The dataset is initially scraped from the former `crello.com` and pre-processed to the above format.

#### Who are the source language producers?

While [create.vista.com](https://create.vista.com/) owns those templates, the templates seem to be originally created by a specific group of design studios.

### Personal and Sensitive Information

The dataset does not contain any personal information about the creator but may contain a picture of people in the design template.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset was developed for advancing the general study of vector graphic documents, especially for generative systems of graphic design. Successful utilization might enable the automation of creative workflow that human designers get involved in.

### Discussion of Biases

The templates contained in the dataset reflect the biases appearing in the source data, which could present gender biases in specific design categories.

### Other Known Limitations

Due to the unknown data specification of the source data, the color and pre-rendered images do not necessarily accurately reproduce the original design templates. The original template is accessible at the following URL if still available.

    https://create.vista.com/artboard/?template=<template_id>

## Additional Information

### Dataset Curators

The Crello dataset was developed by [Kota Yamaguchi](https://github.com/kyamagu).

### Licensing Information

The origin of the dataset is [create.vista.com](https://create.vista.com) (formally, `crello.com`).
The distributor ("We") do not own the copyrights of the original design templates.
By using the Crello dataset, the user of this dataset ("You") must agree to the
[VistaCreate License Agreements](https://create.vista.com/faq/legal/licensing/license_agreements/).

The dataset is distributed under [CDLA-Permissive-2.0 license](https://cdla.dev/permissive-2-0/).

**Note**

We do not re-distribute the original files as we are not allowed by terms.

### Citation Information

    @article{yamaguchi2021canvasvae,
      title={CanvasVAE: Learning to Generate Vector Graphic Documents},
      author={Yamaguchi, Kota},
      journal={ICCV},
      year={2021}
    }

### Releases

3.1: bugfix release (Feb 16, 2023)

- Fix a bug that ignores newline characters in some of the texts

3.0: v3 release (Feb 13, 2023)

- Migrate to Hugging Face Hub.
- Fix various text rendering bugs.
- Change split generation criteria for avoiding near-duplicates: no compatibility with v2 splits.
- Incorporate a motion picture thumbnail in templates.
- Add `title`, `keywords`, `suitability`, and `industries` canvas attributes.
- Add `capitalize`, `line_height`, and `letter_spacing` element attributes.

2.0: v2 release (May 26, 2022)

- Add `text`, `font`, `font_size`, `text_align`, and `angle` element attributes.
- Include rendered text element in `image_bytes`.

1.0: v1 release (Aug 24, 2021)


### Contributions

Thanks to [@kyamagu](https://github.com/kyamagu) for adding this dataset.