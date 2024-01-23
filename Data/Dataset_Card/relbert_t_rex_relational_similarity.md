---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- n<1K
pretty_name: T-REX for relational similarity
---

# Dataset Card for "relbert/t_rex_relation_similarity"
## Dataset Description
- **Repository:** [RelBERT](https://github.com/asahi417/relbert)
- **Paper:** [https://aclanthology.org/L18-1544/](https://aclanthology.org/L18-1544/)
- **Dataset:** T-REX for relational similarity

## Dataset Summary
This is the clean version of [T-REX](https://aclanthology.org/L18-1544/) converted into relation similarity dataset format.
The original dataset is [`relbert/t_rex`](https://huggingface.co/datasets/relbert/t_rex).


## Dataset Structure
### Data Instances
An example of `train` looks as follows.

```shell
{
    "relation_type": "[Airline] has a hub in [Location]",
    "positives": [["Korean Air", "Seoul"], ["Asiana Airlines", "Seoul"], ["Cathay Pacific", "Hong Kong"], ["Dragonair", "Hong Kong"], ["Qantas", "Singapore"], ["Air China", "Beijing"], ["Singapore Airlines", "Singapore"]],
    "negatives": [["joint resolution", "United States Congress"], ["joint resolution", "Congress"], ["Great Seal", "United States"], ["trident", "Ukraine"], ["harp", "Ireland"], ["Plantagenet", "England"], ["Pahonia", "Lithuania"], ["slavery", "American Civil War"], ["main asteroid belt", "Solar System"], ["Colorado Desert", "Sonoran Desert"], ["DNA", "genome"], ["Mars", "Solar System"], ["Manchester United", "red"], ["Kermit", "greenness"], ["Ruby", "red"], ["Liberal Party", "red"], ["Macintosh", "Apple"], ["Apple II", "Apple"], ["Apple III", "Apple"], ["PlayStation 2", "Sony"], ["PlayStation 2", "Sony Computer Entertainment"], ["Beatles", "George Martin"], ["Baku", "Azerbaijan"], ["Accra", "Ghana"], ["Amman", "Jordan"], ["Hannover", "Lower Saxony"], ["Agartala", "Tripura"], ["Makassar", "South Sulawesi"], ["Taiwan", "China"], ["Poland", "United Nations"], ["Poland", "Europe"], ["Poland", "European Union"], ["Poland", "NATO"], ["German invasion", "22 June 1941"], ["Operation Barbarossa", "22 June 1941"], ["Brazil", "Catholic Church"], ["Turkey", "Islam"], ["Afghanistan", "Islam"], ["Iraq", "Islam"], ["Finland", "Evangelical Lutheran Church"], ["England", "Roman Catholic"], ["Congress", "United States"], ["Sejm", "Poland"], ["Diet", "Japan"], ["Majlis", "Iran"], ["Riksdag", "Sweden"], ["Croatian Parliament", "Croatia"], ["Knesset", "Israel"], ["Parliament", "Sri Lanka"], ["Russia", "Soviet Union"], ["Ukrainian SSR", "Soviet Union"], ["Royal Flying Corps", "Royal Air Force"], ["Canadian Army", "Canadian Forces"], ["Belarus", "Russian"], ["Russia", "Russian"], ["Ukraine", "Russian"], ["Kerala", "Malayalam"], ["American", "English"], ["zlib license", "Open Source Initiative"], ["EPL", "Open Source Initiative"], ["GNU General Public License", "Open Source Initiative"], ["Wrigley Field", "Cubs"], ["Wrigley Field", "Chicago Cubs"], ["Yankee Stadium", "Yankees"], ["Passaic River", "Newark Bay"], ["Rocky", "Sylvester Stallone"], ["The Godfather", "Francis Ford Coppola"], ["Citizen Kane", "Orson Welles"], ["She Hate Me", "Spike Lee"], ["Raajneeti", "Prakash Jha"], ["Doctor Who", "Patrick Troughton"], ["Doctor Who", "Tom Baker"], ["Jana Gana Mana", "India"], ["President", "White House"], ["Washington", "Federalist Party"], ["George Washington", "Federalist Party"], ["Joseph Stalin", "Communist Party"], ["Mao Zedong", "Communist Party"], ["Lenin", "Communist Party"], ["Nelson Mandela", "ANC"], ["Putin", "Communist Party"], ["Nehru", "Indian National Congress"], ["Nicolas Sarkozy", "UMP"], ["Andreas Papandreou", "PASOK"], ["Tim Cook", "Apple"], ["Israel", "Isaac"], ["Meg", "Peter"], ["Elizabeth II", "Canada"], ["Victor Emmanuel III", "Italy"], ["Umberto I", "Italy"], ["Victor Emmanuel II", "Italy"], ["Brahms", "pianist"], ["Beethoven", "piano"], ["Nicky Hopkins", "pianist"], ["Mozart", "violin"], ["John Zorn", "saxophonist"], ["McCartney", "piano"], ["Russians", "Russian"], ["The Real McCoys", "CBS"], ["Brookside", "Channel 4"], ["The Real McCoys", "ABC"], ["Windows", "Microsoft"], ["Busan", "Gyeongbu Line"], ["Seoul", "Gyeongbu Line"], ["Springer Mountain", "Appalachian Trail"], ["Doctor Who", "BBC One"], ["central time zone", "Illinois"], ["CT", "Canada"], ["Central Time Zone", "Mexico"], ["Central Time Zone", "United States"], ["CT", "American"], ["CT", "Mexico"], ["CT", "United States"], ["central time zone", "Indiana"], ["Central Time Zone", "American"]]
}
```

### Data Splits

| name                                          |   train |   validation |   test |
|:----------------------------------------------|--------:|-------------:|-------:|
| filter_unified.min_entity_1_max_predicate_100 |     208 |          133 |     24 |
| filter_unified.min_entity_1_max_predicate_50  |     204 |          113 |     24 |
| filter_unified.min_entity_1_max_predicate_25  |     202 |           71 |     24 |
| filter_unified.min_entity_1_max_predicate_10  |     192 |           25 |     24 |
| filter_unified.min_entity_2_max_predicate_100 |     188 |          107 |     24 |
| filter_unified.min_entity_2_max_predicate_50  |     184 |           85 |     24 |
| filter_unified.min_entity_2_max_predicate_25  |     181 |           51 |     24 |
| filter_unified.min_entity_2_max_predicate_10  |     171 |           13 |     24 |
| filter_unified.min_entity_3_max_predicate_100 |     166 |           82 |     24 |
| filter_unified.min_entity_3_max_predicate_50  |     157 |           66 |     24 |
| filter_unified.min_entity_3_max_predicate_25  |     156 |           37 |     24 |
| filter_unified.min_entity_3_max_predicate_10  |     148 |           17 |     24 |
| filter_unified.min_entity_4_max_predicate_100 |     150 |           73 |     24 |
| filter_unified.min_entity_4_max_predicate_50  |     145 |           56 |     24 |
| filter_unified.min_entity_4_max_predicate_25  |     141 |           34 |     24 |
| filter_unified.min_entity_4_max_predicate_10  |     128 |           14 |     24 |

## Citation Information
```
@inproceedings{elsahar2018t,
  title={T-rex: A large scale alignment of natural language with knowledge base triples},
  author={Elsahar, Hady and Vougiouklis, Pavlos and Remaci, Arslen and Gravier, Christophe and Hare, Jonathon and Laforest, Frederique and Simperl, Elena},
  booktitle={Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},
  year={2018}
} 
```
