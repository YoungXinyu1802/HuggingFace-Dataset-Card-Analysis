---
language:
- en
task_categories:
- text-classification

---
# AutoTrain Dataset for project: books-rating-analysis

## Dataset Description

This dataset has been automatically processed by AutoTrain for project books-rating-analysis.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "feat_Unnamed: 0": 1976,
    "feat_user_id": "792500e85277fa7ada535de23e7eb4c3",
    "feat_book_id": 18243288,
    "feat_review_id": "7f8219233a62bde2973ddd118e8162e2",
    "target": 2,
    "text": "This book is kind of tricky. It is pleasingly written stylistically and it's an easy read so I cruised along on the momentum of the smooth prose and the potential of what this book could have and should have been for a while before I realized that it is hollow and aimless. \n This is a book where the extraordinary is deliberately made mundane for some reason and characters are stubbornly underdeveloped. It is as if all the drama has been removed from this story, leaving a bloodless collection of 19th industrial factoids sprinkled amidst a bunch of ciphers enduring an oddly dull series of tragedies. \n Mildly entertaining for a while but ultimately unsatisfactory.",
    "feat_date_added": "Mon Apr 27 11:37:36 -0700 2015",
    "feat_date_updated": "Mon May 04 08:50:42 -0700 2015",
    "feat_read_at": "Mon May 04 08:50:42 -0700 2015",
    "feat_started_at": "Mon Apr 27 00:00:00 -0700 2015",
    "feat_n_votes": 0,
    "feat_n_comments": 0
  },
  {
    "feat_Unnamed: 0": 523,
    "feat_user_id": "01ec1a320ffded6b2dd47833f2c8e4fb",
    "feat_book_id": 18220354,
    "feat_review_id": "c19543fab6b2386df92c1a9ba3cf6e6b",
    "target": 4,
    "text": "4.5 stars!! I am always intrigued to read a novel written from a male POV. I am equally fascinated by pen names, and even when the writer professes to be one gender or the other (or leaves it open to the imagination such as BG Harlen), I still wonder at the back of my mind whether the author is a male or female. Do some female writers have a decidedly masculine POV? Yes, there are several that come to mind. Do some male writers have a feminine \"flavor\" to their writing? It seems so. \n And so we come to the fascinating Thou Shalt Not. I loved Luke's story, as well as JJ Rossum's writing style, and don't want to be pigeon-holed into thinking that the author is male or female. That's just me. Either way, it's a very sexy and engaging book with plenty of steamy scenes to satisfy even the most jaded erotic romance reader (such as myself). The story carries some very weighty themes (domestic violence, adultery, the nature of beauty), but the book is very fast-paced and satisfying. Will Luke keep himself out of trouble with April? Will he learn to really love someone again? No spoilers here, but the author answers these questions while exploring what qualities are really important and what makes someone worthy of love. \n This book has a very interesting conclusion that some readers will love, and some might find a little challenging. I loved it and can't wait to read more from this author. \n *ARC provided by the author in exchange for an honest review.",
    "feat_date_added": "Mon Jul 29 16:04:04 -0700 2013",
    "feat_date_updated": "Thu Dec 12 21:43:54 -0800 2013",
    "feat_read_at": "Fri Dec 06 00:00:00 -0800 2013",
    "feat_started_at": "Thu Dec 05 00:00:00 -0800 2013",
    "feat_n_votes": 10,
    "feat_n_comments": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "feat_Unnamed: 0": "Value(dtype='int64', id=None)",
  "feat_user_id": "Value(dtype='string', id=None)",
  "feat_book_id": "Value(dtype='int64', id=None)",
  "feat_review_id": "Value(dtype='string', id=None)",
  "target": "ClassLabel(names=['0', '1', '2', '3', '4', '5'], id=None)",
  "text": "Value(dtype='string', id=None)",
  "feat_date_added": "Value(dtype='string', id=None)",
  "feat_date_updated": "Value(dtype='string', id=None)",
  "feat_read_at": "Value(dtype='string', id=None)",
  "feat_started_at": "Value(dtype='string', id=None)",
  "feat_n_votes": "Value(dtype='int64', id=None)",
  "feat_n_comments": "Value(dtype='int64', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 2397 |
| valid        | 603 |
