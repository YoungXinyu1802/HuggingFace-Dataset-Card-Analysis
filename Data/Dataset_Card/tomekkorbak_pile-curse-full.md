## Generation procedure

The dataset was constructed using documents from [the Pile](https://pile.eleuther.ai/) scored using [LDNOOBW](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words) wordlist (a score is number of curses per character). 

The procedure was the following:
1. The first half of the data are 100k documents randomly sampled from the Pile and assigned scores
2. The second half are the most cursing document from the Pile, obtained by scoring the whole Pile and choosing 100k documents with highest scores
3. Then, the dataset was shuffled and a 9:1 train-test split was done

## Basic stats

The average and median scores are 0.013 and 0.019, respectively.