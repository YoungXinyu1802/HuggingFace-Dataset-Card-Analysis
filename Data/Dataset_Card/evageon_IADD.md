---
license: cc-by-4.0
---
# IADD

IADD is an Integrated Dataset for Arabic Dialect iDentification Dataset. It contains 136,317 texts representing 5 regions (Maghrebi (MGH) , Levantine (LEV), Egypt (EGY) , Iraq (IRQ) and Gulf (GLF)) and 9 countries (Algeria, Morocco, Tunisia, Palestine, Jordan, Syria, Lebanon, Egypt and Iraq).

IADD is created from the combination of subsets of five corpora: DART, SHAMI, TSAC, PADIC and AOC. The Dialectal ARabic Tweets dataset (DART) [1] has about 25,000 tweets that are annotated via crowdsourcing while the SHAMI dataset [2] consists of 117,805 sentences and covers levantine dialects spoken in Palestine, Jordan, Lebanon and Syria. TSAC [3] is a Tunisian dialect corpus of 17,000 comments collected mainly from Tunisian Facebook pages. Parallel Arabic Dialect Corpus (PADIC) [4] is made of sentences transcribed from recordings or translated from MSA. Finally, the Arabic Online Commentary (AOC) dataset [5] is based on reader commentary from the online versions of three Arabic newspapers, and it consists of 1.4M comments.

IADD is stored in a JSON-like format with the following keys:
- Sentence: contains the sentence/ text;
- Region: stores the corresponding dialectal region (MGH, LEV, EGY, IRQ, GLF or general);
- Country: specifies the corresponding country, if available (MAR, TUN, DZ, EGY, IRQ, SYR, JOR, PSE, LBN);
- DataSource: indicates the source of the data (PADIC, DART, AOC, SHAMI or TSAC).


[1] Alsarsour, I., Mohamed, E., Suwaileh, R., & Elsayed, T. (2018, May). Dart: A large dataset of dialectal arabic tweets. In Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018).
[2] Abu Kwaik, K., Saad, M. K., Chatzikyriakidis, S., & Dobnik, S. (2018). Shami: A corpus of levantine arabic dialects. In Proceedings of the eleventh international conference on language resources and evaluation (LREC 2018).
[3] Mdhaffar, S., Bougares, F., Esteve, Y., & Hadrich-Belguith, L. (2017, April). Sentiment analysis of tunisian dialects: Linguistic ressources and experiments. In Third Arabic Natural Language Processing Workshop (WANLP) (pp. 55-61).
[4] Meftouh, K., Harrat, S., Jamoussi, S., Abbas, M., & Smaili, K. (2015, October). Machine translation experiments on PADIC: A parallel Arabic dialect corpus. In The 29th Pacific Asia conference on language, information and computation.
[5] Zaidan, O., & Callison-Burch, C. (2011, June). The arabic online commentary dataset: an annotated dataset of informal arabic with high dialectal content. In Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies (pp. 37-41).
