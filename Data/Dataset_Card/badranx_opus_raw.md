## Load mono corpora from OPUS

OPUS provides many parallel corpora, but it has more data for a single language. This enables you to load any raw mono corpus from [opus.nlpl.eu](https://opus.nlpl.eu/). Please check [opus.nlpl.eu](https://opus.nlpl.eu/) for the available corpora and licenses. The targeted corpus is called raw corpus on OPUS.

To use it, you need the name of the corpus, the version, and the target language code. The corpus name and version are provided in one string seperated by space (e.g. 'News-Commentary v16'). All of these can be found on [opus.nlpl.eu](https://opus.nlpl.eu/).

I didn't provide any default dataset, because this targets different datasets at once. You must provide two parameters as configurations: corpus and lang, see the example below.

## Example:
```python
dataset = load_dataset('badranx/opus_raw', corpus="News-Commentary v16", lang="de")
```
## Structure
The structure is simple.
```python
{
   "id": datasets.Value("string"),
   "text": datasets.Value("string"),
}
```

"text" can be one or more sentences, but not more than a paragraph.