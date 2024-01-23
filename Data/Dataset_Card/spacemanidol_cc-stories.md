This is a reproduction of the CC-stories dataset as it has been removed from its original source. 
To create this reproduction we process the English common crawl and only keep the top 0.1% of documents measured by their ngram overlap with a source document.
The source document is created by joining the queries from [PDP-60](https://cs.nyu.edu/~davise/papers/WinogradSchemas/PDPChallenge2016.xml) and [WSC273](https://cs.nyu.edu/~davise/papers/WinogradSchemas/WSCollection.xml). Note, as the original dataset does not mention removing duplicate queries, neither do we.

Following the filtering to have top documents we filter to only contain those and produce the dataset which features 2,105,303 lines and 153,176,685 words. 