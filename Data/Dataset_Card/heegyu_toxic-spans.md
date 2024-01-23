---
license: cc0-1.0
---
# Toxic Spans
TOXICSPANS contains the 11,035 posts we annotated for toxic spans. The unique posts are actually 11,006, since a few were duplicates and were removed in subsequent experiments. A few other posts were used as quiz questions to check the reliability of candidate annotators and were also discarded in subsequent experiments.

original data from https://github.com/ipavlopoulos/toxic_spans/tree/master/ACL2022

- 10006 train set
- 1000 test set

## Columns
- probability = a dict with the first and the last character offsets of each token (that was rated by at least one annotator as toxic) as a key, and the average toxicity as a value
- position = the character offsets of all the toxic spans(avg toxicity > 50%) found by the annotators (ground truth)
- text = the average toxicity of each token that was rated by at least one annotator as toxic
- type = the type of toxicity of each toxic span
- support = the number of annotators per post
- text_of_post = the text of the post
- position_probability = the average toxicity of each character offset that was found by at least one annotator as toxic
- toxic = (Not in original) If the probability of at least 1 token is greather than 0.5



### Sample
```
{
    "probability": {
        "(5, 11)": 1.0,
        "(286, 294)": 0.6666666667,
        "(120, 126)": 0.6666666667,
        "(350, 356)": 0.6666666667
    },
    "position": [
        5,
        6,
        7,
        8,
        9,
        10,
        120,
        121,
        122,
        123,
        124,
        125,
        286,
        287,
        288,
        289,
        290,
        291,
        292,
        293,
        350,
        351,
        352,
        353,
        354,
        355
    ],
    "text": {
        "stupid": 1.0,
        "ignorant": 0.6666666667,
        "Stupid": 0.6666666667
    },
    "type": {
        "profane\/obscene": 0.3333333333,
        "insult": 0.6666666667
    },
    "support": 3,
    "text_of_post": "Yes, stupid on steroids does afflict the nation. The biggest problem, of course, is they either don't see themselves as stupid, or are so proud of the fact they are they have no intention of remedying the situation.  In fact, that's the definition of stupid in my book: You know you're ignorant, proud of it, and have no intention of alleviating it. Stupid. \n\nI wonder how they'd like their doctors to say to them \"Oh, I didn't go to medical school; that's for elites.  The need for a formal education is fake news. I studied at home for a couple of years and got an alternative medical education.  Trust me, I'm as good a doctor as any. Now, when did you want to schedule that surgery?\"  I wonder how they'd like an unlicensed pilot in charge of getting them from point A to Point B?  \n\nI think they're all just lazy. They want all the benefits of an education, but don't want to put in the time.",
    "position_probability": {
        "5": 1.0,
        "6": 1.0,
        "7": 1.0,
        "8": 1.0,
        "9": 1.0,
        "10": 1.0,
        "286": 0.6666666667,
        "287": 0.6666666667,
        "288": 0.6666666667,
        "289": 0.6666666667,
        "290": 0.6666666667,
        "291": 0.6666666667,
        "292": 0.6666666667,
        "293": 0.6666666667,
        "120": 0.6666666667,
        "121": 0.6666666667,
        "122": 0.6666666667,
        "123": 0.6666666667,
        "124": 0.6666666667,
        "125": 0.6666666667,
        "350": 0.6666666667,
        "351": 0.6666666667,
        "352": 0.6666666667,
        "353": 0.6666666667,
        "354": 0.6666666667,
        "355": 0.6666666667
    },
    "toxic": true
}
```