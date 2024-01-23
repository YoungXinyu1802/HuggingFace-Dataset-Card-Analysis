---
license: mit
---

The `post-data-by-subreddit.tar` file contains 5000 gzipped json files - one for each of the top 5000 subreddits (as roughly measured by subscriber count and comment activity). Each of those json files (e.g. `askreddit.json`) contains an array of the data for the top 1000 posts of all time.

Notes:
 * I stopped crawling a subreddit's top-posts list if I reached a batch that had a post with a score less than 5, so some subreddits won't have the full 1000 posts.
 * No posts comments are included. Only the posts themselves.
 * See the example file `askreddit.json` in this repo if you want to see what you're getting before downloading all the data.
 * The list of subreddits included are listed in `top-5k-subreddits.json`.
 * NSFW subreddits have been included in the crawl, so you might have to filter them out depending on your use case.
 * The Deno scraping/crawling script is included as `crawl.js`, and can be started with `deno run --allow-net --allow-read=. --allow-write=. crawl.js` once you've [installed Deno](https://deno.land/manual/getting_started/installation) and have downloaded `top-5k-subreddits.json` into the same folder as `crawl.js`.