## the_office_lines

<img src="https://a.pinatafarm.com/1351x1232/c8fa71efd1/the-office-handshake.jpg" width="256">

A dataset of lines from the U.S. version of the tv show "The Office". Lines were originally scraped from the website [officequotes.net](https://www.officequotes.net/), are fan-transcribed, and may be of dubious quality.

Contains a train split (47,927 lines), test split (5,991 lines) and validation split (5,991 lines). Contains lines from all 9 seasons, every episode, but may be complete.


Lines are annotated with an ID number, season number, episode number, scene number (within the episode), speaker name, and whether or not the text came from a deleted scene. Here is an example:

```
> dataset["val"][0]
{'id': 3735,
 'season': 2,
 'episode': 5,
 'scene': 32,
 'line_text': 'No, you have the power to undo it.',
 'speaker': 'Creed',
 'deleted': False}
```
