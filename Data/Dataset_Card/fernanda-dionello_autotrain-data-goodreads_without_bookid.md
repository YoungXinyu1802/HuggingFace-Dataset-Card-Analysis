---
language:
- en
task_categories:
- text-classification

---
# AutoTrain Dataset for project: goodreads_without_bookid

## Dataset Description

This dataset has been automatically processed by AutoTrain for project goodreads_without_bookid.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "target": 5,
    "text": "This book was absolutely ADORABLE!!!!!!!!!!! It was an awesome light and FUN read. \n I loved the characters but I absolutely LOVED Cam!!!!!!!!!!!! Major Swoooon Worthy! J \n You've been checking me out haven't you? In-between your flaming insults? I feel like man candy. \n Seriously between being HOT FUNNY and OH SO VERY ADORABLE Cam was the perfect catch!! \n  I'm not going out with you Cam. \n  I didn't ask you at this moment now did I One side of his lips curved up.  But you will eventually. \n You're delusional \n I'm determined. \n  More like annoying. \n  Most would say amazing. \n Cam and Avery's relationship is tough due to the secrets she keeps but he is the perfect match for breaking her out of her shell and facing her fears. \n This book is definitely a MUST READ. \n Trust me when I say this YOU will not regret it! \n www.Jenreadit.com"
  },
  {
    "target": 4,
    "text": "3.5 stars! \n Abbi Glines' books are a guilty pleasure for me. I love the Southern charm the sexy boys and the beautiful sweet girls. When You're Back is the second book in Reese and Mase's story and other characters from my other favorite books all make appearances here. \n I loved River Captain Kipling! This guy is SEXY and broody. He is a bit mysterious and I am really looking forward to reading more about him! \n I can change your world too sweetheart. But I'll wait my turn. \n We also have Mase's cousin Aida here who gives the cold shoulder to sweet loving Reese. I really liked how Reese blossomed in this book and how loving and devoted Mase is to her. He is one of my favorite of Abbi Glines' characters and he is definitely book boyfriend material. Their scenes are touching sexy and sweet just what I expect from the Rosemary Beach series. I liked this book and recommend it if you are looking for a sexy quick summertime read!"
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "target": "ClassLabel(num_classes=6, names=['0', '1', '2', '3', '4', '5'], id=None)",
  "text": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 2358 |
| valid        | 592 |
