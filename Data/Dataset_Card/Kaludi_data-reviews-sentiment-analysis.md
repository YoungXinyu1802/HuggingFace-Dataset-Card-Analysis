---
language:
- en
task_categories:
- text-classification

---
# Dataset for the project: reviews-sentiment-analysis

## Dataset Description

This dataset is for project reviews-sentiment-analysis.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "Now, I won't deny that when I purchased this off eBay, I had high expectations. This was an incredible out-of-print work from the master of comedy that I so enjoy. However, I was soon to be disappointed. Apologies to those who enjoyed it, but I just found the Compleat Al to be very difficult to watch. I got a few smiles, sure, but the majority of the funny came from the music videos (which I've got on DVD) and the rest was basically filler. You could tell that this was not Al's greatest video achievement (that honor goes to UHF). Honestly, I doubt if this will ever make the jump to DVD, so if you're an ultra-hardcore Al fan and just HAVE to own everything, buy the tape off eBay. Just don't pay too much for it.",
    "target": 0
  },
  {
    "text": "The saddest thing about this \"tribute\" is that almost all the singers (including the otherwise incredibly talented Nick Cave) seem to have missed the whole point where Cohen's intensity lies: by delivering his lines in an almost tuneless poise, Cohen transmits the full extent of his poetry, his irony, his all-round humanity, laughter and tears in one.<br /><br />To see some of these singer upstarts make convoluted suffering faces, launch their pathetic squeals in the patent effort to scream \"I'm a singer!,\" is a true pain. It's the same feeling many of you probably had listening in to some horrendous operatic versions of simple songs such as Lennon's \"Imagine.\" Nothing, simply nothing gets close to the simplicity and directness of the original. If there is a form of art that doesn't need embellishments, it's Cohen's art. Embellishments cast it in the street looking like the tasteless make-up of sex for sale.<br /><br />In this Cohen's tribute I found myself suffering and suffering through pitiful tributes and awful reinterpretations, all of them entirely lacking the original irony of the master and, if truth be told, several of these singers sounded as if they had been recruited at some asylum talent show. It's Cohen doing a tribute to them by letting them sing his material, really, not the other way around: they may have been friends, or his daughter's, he could have become very tender-hearted and in the mood for a gift. Too bad it didn't stay in the family.<br /><br />Fortunately, but only at the very end, Cohen himself performed his majestic \"Tower of Song,\" but even that flower was spoiled by the totally incongruous background of the U2, all of them carrying the expression that bored kids have when they visit their poor grandpa at the nursing home.<br /><br />A sad show, really, and sadder if you truly love Cohen as I do.",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(names=['Negative', 'Positive'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follows:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 7499 |
| valid        | 2497 |
