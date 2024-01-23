---
language:
- en
tags:
- youtube
- timeseries
- time series
- tsd
- trending videos
size_categories:
- 1M<n<10M
pretty_name: timeseries trending youtube videos 2019-04-15 to 2020-04-15
---

*Timeseries Trending YouTube Videos: 2019-04-15 to 2020-04-15*

This dataset is a csv of one of the archived historical database tables queried from my non public database that contains time series data for period of 2019-04-15 to 2020-04-15. Video data was captured from the time they first appeared on trending list, and TSD exists until the video is removed from trending list.

This snapshot contains data for the 11,369 videos that appeared on trending within the timeframe, with 1,541,128 records total TSD.

TSD in this dataset was spidered on variable frequency at the start, however it should stabilize to every 30 minutes later in the dataset.

Data provided in this dataset is:

ytvideoid (the id of the video according to Youtube), views, comments, likes, dislikes (This is prior to the removal of dislikes as publicly viewable data)

Information for this dataset is also available on github: 

https://github.com/jettisonthenet/timeseries_trending_youtube_videos_2019-04-15_to_2020-04-15