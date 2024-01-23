# This repo consists of data downloaded from reddit.com/r/writingprompts

## prompt_responses_full.csv
*  There are 193842 prompt responses in the file, and they together represent the 10 years of submissions prior to March, 13th, 2020. 

I gather the following metadata for each top-level comment response to a submission story prompt:
* prompt_id: int
  * The id of the Reddit submission that the writing prompt is from according to the Reddit API.
* prompt: str
  * The text of the writing prompt.
* prompt_score: int
  * The total karma score of the Reddit submission that the writing prompt is from.
* prompt_created_utc: int
  * The prompt creation time in Unix epoch seconds
* response_id: int
  * The id of the Reddit comment containing the response to the writing prompt.
* response: str
  * The text of the response.
* response_score: int
  * The total karma score of the Reddit comment that the given response is from.
* response_created_utc: int
  * The response creation time in Unix epoch seconds.
* response_rank: int
  * The index of the response in the list of responses for the given prompt sorted according to response_score from highest score to lowest.
* num_responses: int
  * The total number of responses to the given prompt.
* response_children: List[str]
  * The subcomments on the comment containing the given response to the given prompt.

## comparisons_train.csv and comparisons_test.csv
The comparison data is extracted from pairs of responses for a given prompt.
* There are 35200 comparisons in comparisons_test.csv and 334704 comparisons in comparisons_train.csv
* The comparisons dataset is filtered to remove comparisons between responses with an absolute difference in score less than 100.
  * This is to ensure that comparisons are only made between responses that have a significant quality difference.

In particular, each row in the comparisons dataframe consists of the following:
* comparison: str
  * The comparison string consists of the writing prompt, the first response, and the second response, separated with labels, and padded on the left to 1023 tokens.
* truth: int
  * 0 if the first response has a higher score, 1 if the second response has a higher score (note that there are no ties because of the minimum score gap constraint)
* prompt_id: int
  * The id of the Reddit submission that the writing prompt is from according to the Reddit API.
* prompt: str
  * The text of the writing prompt.
* zero_id: int
  * The id of the Reddit comment containing the first response in the comparison.
* one_id: int
  * The id of the Reddit comment containing the second response in the comparison.
* zero_response: str
  * The text of the first response in the comparison.
* one_response: str
  * The text of the second response in the comparison.
* score_gap: int
  * The absolute difference between the score of the first response and the score of the second response.
* zero_score: int
  * The score of the first response.
* one_score: int
  * The score of the second response.
* tokens_gap: int
  * The absolute difference between the number of tokens in the first response and the number of tokens in the second response.
* zero_tokens: int
  * The number of tokens in the first response as measured by the gpt2 tokenizer 
* one_tokens: int
  * The number of tokens in the second response as measured by the gpt2 tokenizer 
* zero_delay: int
  * The number of hours elapsed between the Reddit submission containing the prompt and the Reddit comment containing the first response.
* one_delay: int
  * The number of hours elapsed between the Reddit submission containing the prompt and the Reddit comment containing the second response.
 
  


