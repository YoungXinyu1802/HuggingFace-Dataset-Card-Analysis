This dataset contains postings and comments from the following recurring threads on [Hacker News](http://news.ycombinator.com/)

1. Ask HN: Who is hiring?
2. Ask HN: Who wants to be hired?
3. Freelancer? Seeking freelancer?

These post types are stored in datasets called `hiring`, `wants_to_be_hired` and `freelancer` respectively. 

Each type of posting has occurred on a regular basis for several years. You can identify when each comment/listing was added through the CommentTime field. The `ParentTitle` also indicates the date of the parent thread in text (e.g. `Ask HN: Who is hiring? (March 2021)`)

This dataset is not programmatically reproducible from source because it was uploaded as an experiment with HF datasets. The raw data was created by querying the public table `bigquery-public-data.hacker_news.full` in Google BigQuery.

Email addresses have been redacted from the dataset.

If this dataset is interesting/useful, I (Dan Becker) will look into improving reproducibility and other general clean-up.

This dataset may be useful for finding trends in tech and tech job listings.