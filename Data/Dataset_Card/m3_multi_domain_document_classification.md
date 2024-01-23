
# multi_domain_document_classification
Multi-domain document classification datasets.
- Biomedical: `chemprot`, `rct-sample`
- Computer Science: `citation_intent`, `sciie`
- Customer Review: `amcd`, `yelp_review`
- Social Media: `tweet_eval_irony`, `tweet_eval_hate`, `tweet_eval_emotion`

The `yelp_review` dataset is randomly downsampled to 2000/2000/8000 for test/validation/train.


|                     |   chemprot |   citation_intent |   hyperpartisan_news |   rct_sample |   sciie |   amcd |   yelp_review |   tweet_eval_irony |   tweet_eval_hate |   tweet_eval_emotion |
|:--------------------|-----------:|------------------:|---------------------:|-------------:|--------:|-------:|--------------:|-------------------:|------------------:|---------------------:|
| word/validation     |         32 |                40 |                  502 |           26 |      32 |     20 |           132 |                 13 |                24 |                   15 |
| word/test           |         32 |                42 |                  612 |           26 |      32 |     19 |           131 |                 14 |                21 |                   15 |
| word/train          |         31 |                42 |                  536 |           26 |      32 |     19 |           133 |                 13 |                20 |                   16 |
| instance/validation |       2427 |               114 |                   64 |        30212 |     455 |    666 |          2000 |                955 |              1000 |                  374 |
| instance/test       |       3469 |               139 |                   65 |        30135 |     974 |   1334 |          2000 |                784 |              2970 |                 1421 |
| instance/train      |       4169 |              1688 |                  516 |          500 |    3219 |   8000 |          6000 |               2862 |              9000 |                 3257 |