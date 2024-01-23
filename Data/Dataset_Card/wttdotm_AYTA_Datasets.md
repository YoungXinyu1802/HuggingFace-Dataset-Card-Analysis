---
tags:
- Reddit
- OpenAI
- GPT-3
- Davinci-002
- PRAW
- PMAW
size_categories:
- 10K<n<100K
---
# Are You The Asshole Training Data
These are the datasets used for a project Alex Petros and I made called [AreYouTheAsshole.com](https://www.areyoutheasshole.com). The site is intended to give users a fun and interactive way to experience the effect of bias in AI due to skewed data. We achieved this by fine-tuning three GPT-3 Davinci-002 models on the prompt/completion pairs you see here.

Each prompt/completion pair constitutes a post body (the prompt) and a comment (the completion). Just as there may be multiple comments to a single post, there may be multiple completions for a single prompt.

The dataset was filtered down from >100,000 post/comment pairs to only those whose comments started with a clear acronym judgement. So, comments like "Well I think YTA because..." were filtered out, whereas comments like "YTA and it's not even close..." were kept.

After filtering for clear judgement, we had our neutral dataset, the one you can find in "Neutral_Dataset.jsonl". In order to create intentionally biased data, we then split that dataset into two subsets based on whether a given post/comment pair's comment judged the poster as The Asshole or Not The Asshole. Some edge cases were also filtered out.

The dataset contains three sets:
- Neutral_Dataset.jsonl (contains all clear judgements, YTA, NTA, etc.)
- YTA_Dataset.jsonl (only contains judgements of YTA or similar)
- NTA_Dataset.jsonl (only contains judgements of NTA or similar)

### Data Collection:
This data was collected from Reddit's r/AmITheAsshole subreddit using PMAW/PRAW and the Reddit API