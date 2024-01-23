# Reddit Randomness Dataset
A dataset I created because I was curious about how "random" r/random really is.
This data was collected by sending `GET` requests to `https://www.reddit.com/r/random` for a few hours on September 19th, 2021.
I scraped a bit of metadata about the subreddits as well.
`randomness_12k_clean.csv` reports the random subreddits as they happened and `summary.csv` lists some metadata about each subreddit.

# The Data

## `randomness_12k_clean.csv`
This file serves as a record of the 12,055 successful results I got from r/random.
Each row represents one result.

### Fields
* `subreddit`: The name of the subreddit that the scraper recieved from r/random (`string`)
* `response_code`: HTTP response code the scraper recieved when it sent a `GET` request to /r/random (`int`, always `302`)

## `summary.csv`
As the name suggests, this file summarizes `randomness_12k_clean.csv` into the information that I cared about when I analyzed this data.
Each row represents one of the 3,679 unique subreddits and includes some stats about the subreddit as well as the number of times it appears in the results.

### Fields
* `subreddit`: The name of the subreddit (`string`, unique)
* `subscribers`: How many subscribers the subreddit had (`int`, max of `99_886`) 
* `current_users`: How many users accessed the subreddit in the past 15 minutes (`int`, max of `999`)
* `creation_date`: Date that the subreddit was created (`YYYY-MM-DD` or `Error:PrivateSub` or `Error:Banned`)
* `date_accessed`: Date that I collected the values in `subscribers` and `current_users` (`YYYY-MM-DD`)
* `time_accessed_UTC`: Time that I collected the values in `subscribers` and `current_users`, reported in UTC+0 (`HH:MM:SS`)
* `appearances`: How many times the subreddit shows up in `randomness_12k_clean.csv` (`int`, max of `9`)

# Missing Values and Quirks
In the `summary.csv` file, there are three missing values. 
After I collected the number of subscribers and the number of current users, I went back about a week later to collect the creation date of each subreddit.
In that week, three subreddits had been banned or taken private. I filled in the values with a descriptive string.
* SomethingWasWrong (`Error:PrivateSub`)
* HannahowoOnlyfans (`Error:Banned`)
* JanetGuzman (`Error:Banned`)

I think there are a few NSFW subreddits in the results, even though I only queried r/random and not r/randnsfw. 
As a simple example, searching the data for "nsfw" shows that I got the subreddit r/nsfwanimegifs twice.


# License
This dataset is made available under the Open Database License: http://opendatacommons.org/licenses/odbl/1.0/. Any rights in individual contents of the database are licensed under the Database Contents License: http://opendatacommons.org/licenses/dbcl/1.0/