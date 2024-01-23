---
language:
- en
task_categories:
- text-classification

---
# AutoTrain Dataset for project: autotrain_goodreads_string

## Dataset Description

This dataset has been automatically processed by AutoTrain for project autotrain_goodreads_string.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "target": 5,
    "text": "This book was absolutely ADORABLE!!!!!!!!!!! It was an awesome, light and FUN read. \n I loved the characters but I absolutely LOVED Cam!!!!!!!!!!!! Major Swoooon Worthy! J \n \"You've been checking me out, haven't you? In-between your flaming insults? I feel like man candy.\" \n Seriously, between being HOT, FUNNY and OH SO VERY ADORABLE, Cam was the perfect catch!! \n \" I'm not going out with you Cam.\" \n \" I didn't ask you at this moment, now did I\" One side of his lips curved up. \" But you will eventually.\" \n \"You're delusional\" \n \"I'm determined.\" \n \" More like annoying.\" \n \" Most would say amazing.\" \n Cam and Avery's relationship is tough due to the secrets she keeps but he is the perfect match for breaking her out of her shell and facing her fears. \n This book is definitely a MUST READ. \n Trust me when I say this YOU will not regret it! \n www.Jenreadit.com"
  },
  {
    "target": 4,
    "text": "I FINISHED!!! This book took me FOREVER to read! But I am so glad I stuck with it, I really loved it. It took me a while to get into: this book has a TON of characters and storylines. But once I hit about the 100-page mark, I became very invested in the story and couldn't wait to see what would happen with Lizzie, Lane, Edward, Gin and the rest of the family. Oh, and Samuel T. There's a little bit of sex but mostly this is a sweeping romance novel, much like Dynasty and Dallas from the 1980's. If you loved those series, you will love this book. There's betrayal, unrequited love, family fortunes, and much scheming. \n There are many characters to love here and many to hate. Some are over-the-top but I loved the central storyline involving Lane and Lizzie. \n The author really gets the Southern mannerisms right, and the backdrop of the Kentucky Bourbon industry is fascinating. This book ends not so much on a cliffhanger but with many, many loose ends, and I will eagerly pick up the next book in this series."
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "target": "ClassLabel(num_classes=6, names=['0_stars', '1_stars', '2_stars', '3_stars', '4_stars', '5_stars'], id=None)",
  "text": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 2357 |
| valid        | 592 |
