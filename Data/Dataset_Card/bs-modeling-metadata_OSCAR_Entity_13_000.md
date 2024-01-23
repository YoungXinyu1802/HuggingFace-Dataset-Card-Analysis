The dataset is in the form of a json lines file with 10,657 examples, where an example consists of text (extracted from the first 13,000 rows of OSCAR unshuffled English dataset) and metadata fields (entities).

Structure of an example.

```
{
    "text": "This is exactly the sort of article to raise the profile of the club around the Midlands. Very positive and really focusses on how the club has improved over a short period of time and the bright prospects for the future \n\"Oxford Town\" - professional as always at the Birmingham Mail. Not only is Oxford a city, but Oxford United are pretty recognisable name to anyone who has ever taken even a vague interest in English football.",
    "metadata": [
      {
        "key": "entity",
        "type": "local",
        "char_start_idx": 80,
        "char_end_idx": 88,
        "value": "Midlands"
      },
      {
        "key": "entity",
        "type": "local",
        "char_start_idx": 225,
        "char_end_idx": 236,
        "value": "Oxford Town"
      },
      {
        "key": "entity",
        "type": "local",
        "char_start_idx": 270,
        "char_end_idx": 285,
        "value": "Birmingham_Mail"
      },
      {
        "key": "entity",
        "type": "local",
        "char_start_idx": 299,
        "char_end_idx": 305,
        "value": "Oxford"
      },
      {
        "key": "entity",
        "type": "local",
        "char_start_idx": 318,
        "char_end_idx": 331,
        "value": "Oxford_United_Stars_F.C."
      },
      {
        "key": "entity",
        "type": "local",
        "char_start_idx": 415,
        "char_end_idx": 422,
        "value": "England"
      }
    ]
  }
```
