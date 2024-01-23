---
task_categories:
- tabular-classification
tags:
- tabular
pretty_name: Tabular letter recognition
size_categories:
- 10K<n<100K
---

## Source:

Creator:

David J. Slate
Odesta Corporation; 1890 Maple Ave; Suite 115; Evanston, IL 60201

Donor:

David J. Slate (dave '@' math.nwu.edu) (708) 491-3867

## Data Set Information:

The objective is to identify each of a large number of black-and-white rectangular pixel displays as one of the 26 capital letters in the English alphabet. The character images were based on 20 different fonts and each letter within these 20 fonts was randomly distorted to produce a file of 20,000 unique stimuli. Each stimulus was converted into 16 primitive numerical attributes (statistical moments and edge counts) which were then scaled to fit into a range of integer values from 0 through 15. We typically train on the first 16000 items and then use the resulting model to predict the letter category for the remaining 4000. See the article cited above for more details.

### Attribute Information:

1. x-box horizontal position of box (integer)
2. y-box vertical position of box (integer)
3. width width of box (integer)
4. high height of box (integer)
5. onpix total # on pixels (integer)
6. x-bar mean x of on pixels in box (integer)
7. y-bar mean y of on pixels in box (integer)
8. x2bar mean x variance (integer)
9. y2bar mean y variance (integer)
10. xybar mean x y correlation (integer)
11. x2ybr mean of x * x * y (integer)
12. xy2br mean of x * y * y (integer)
13. x-ege mean edge count left to right (integer)
14. xegvy correlation of x-ege with y (integer)
15. y-ege mean edge count bottom to top (integer)
16. yegvx correlation of y-ege with x (integer)