---
language:
- it
license:
- unknown
size_categories:
- unknown
task_categories:
- translation
task_ids: []
pretty_name: mt_nap_it
tags:
- conditional-text-generation
---

# Dataset Card for mt_en_it

## Table of Contents

- [Dataset Card for mt_en_it](#dataset-card-for-mt-en-it)
  - [Table of Contents](#table-of-contents)
  - [Dataset Summary](#dataset-summary)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Dataset Creation](#dataset-creation)

### Dataset Summary
This dataset comprises traditional Neapolitan songs from [napoligrafia](https://www.napoligrafia.it) translated into Italian.

### Languages
- italian-to-neapolitan

### Data Instances
A sample from the dataset.
```python
{
  'url': "url",
  'napoletano': "o, quacche ghiuorno, 'a frennesia mme piglia",
  'italiano': "o, qualche giorno, la rabbia mi prende"
}
```
The text is provided without further preprocessing or tokenization.
### Data Fields
- `url`: source URL.
- `napoletano`: Neapolitan text.
- `italiano`: Italian text.

### Dataset Creation
The dataset was created by scraping [napoligrafia](https://www.napoligrafia.it) songs.