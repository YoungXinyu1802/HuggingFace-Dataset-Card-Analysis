# Comparing model predictions and ground truth labels with Rubrix and Hugging Face

## Build dataset

You can skip this step if you run:



```python
from datasets import load_dataset
import rubrix as rb

ds = rb.DatasetForTextClassification.from_datasets(load_dataset("rubrix/sst2_with_predictions", split="train"))
```


Otherwise, the following cell will run the pipeline over the training set and store labels and predictions.


```python
from datasets import load_dataset
from transformers import pipeline, AutoModelForSequenceClassification

import rubrix as rb

name = "distilbert-base-uncased-finetuned-sst-2-english"

# Need to define id2label because surprisingly the pipeline has uppercase label names 
model = AutoModelForSequenceClassification.from_pretrained(name, id2label={0: 'negative', 1: 'positive'})
nlp = pipeline("sentiment-analysis", model=model, tokenizer=name, return_all_scores=True)

dataset = load_dataset("glue", "sst2", split="train")

# batch predict
def predict(example):
    return {"prediction": nlp(example["sentence"])}

# add predictions to the dataset
dataset = dataset.map(predict, batched=True).rename_column("sentence", "text")

# build rubrix dataset from hf dataset
ds = rb.DatasetForTextClassification.from_datasets(dataset, annotation="label")
```


```python
# Install Rubrix and start exploring and sharing URLs with interesting subsets, etc.
rb.log(ds, "sst2")
```


```python
ds.to_datasets().push_to_hub("rubrix/sst2_with_predictions")
```


    Pushing dataset shards to the dataset hub:   0%|          | 0/1 [00:00<?, ?it/s]


## Analize misspredictions and ambiguous labels

### With the UI

With Rubrix's UI you can:

- Combine filters and full-text/DSL queries to quickly find important samples
- All URLs contain the state so you can share with collaborator and annotator specific dataset regions to work on.
- Sort examples by score, as well as custom metadata fields.



![example.png](https://huggingface.co/datasets/rubrix/sst2_with_predictions/resolve/main/example.png)


### Programmatically

Let's find all the wrong predictions from Python. This is useful for bulk operations (relabelling, discarding, etc.) as well as 


```python
import pandas as pd

# Get dataset slice with wrong predictions
df = rb.load("sst2", query="predicted:ko").to_pandas()

# display first 20 examples
with pd.option_context('display.max_colwidth', None):
    display(df[["text", "prediction", "annotation"]].head(20))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>text</th>
      <th>prediction</th>
      <th>annotation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>this particular , anciently demanding métier</td>
      <td>[(negative, 0.9386059045791626), (positive, 0.06139408051967621)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>1</th>
      <td>under our skin</td>
      <td>[(positive, 0.7508484721183777), (negative, 0.24915160238742828)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>2</th>
      <td>evokes a palpable sense of disconnection , made all the more poignant by the incessant use of cell phones .</td>
      <td>[(negative, 0.6634528636932373), (positive, 0.3365470767021179)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>3</th>
      <td>plays like a living-room war of the worlds , gaining most of its unsettling force from the suggested and the unknown .</td>
      <td>[(positive, 0.9968075752258301), (negative, 0.003192420583218336)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>4</th>
      <td>into a pulpy concept that , in many other hands would be completely forgettable</td>
      <td>[(positive, 0.6178210377693176), (negative, 0.3821789622306824)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>5</th>
      <td>transcends ethnic lines .</td>
      <td>[(positive, 0.9758220314979553), (negative, 0.024177948012948036)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>6</th>
      <td>is barely</td>
      <td>[(negative, 0.9922297596931458), (positive, 0.00777028314769268)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>7</th>
      <td>a pulpy concept that , in many other hands would be completely forgettable</td>
      <td>[(negative, 0.9738760590553284), (positive, 0.026123959571123123)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>8</th>
      <td>of hollywood heart-string plucking</td>
      <td>[(positive, 0.9889695644378662), (negative, 0.011030420660972595)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>9</th>
      <td>a minimalist beauty and the beast</td>
      <td>[(positive, 0.9100378751754761), (negative, 0.08996208757162094)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>10</th>
      <td>the intimate , unguarded moments of folks who live in unusual homes --</td>
      <td>[(positive, 0.9967381358146667), (negative, 0.0032618637196719646)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>11</th>
      <td>steals the show</td>
      <td>[(negative, 0.8031412363052368), (positive, 0.1968587338924408)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>12</th>
      <td>enough</td>
      <td>[(positive, 0.7941301465034485), (negative, 0.2058698982000351)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>13</th>
      <td>accept it as life and</td>
      <td>[(positive, 0.9987508058547974), (negative, 0.0012492131209000945)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>14</th>
      <td>this is the kind of movie that you only need to watch for about thirty seconds before you say to yourself , ` ah , yes ,</td>
      <td>[(negative, 0.7889454960823059), (positive, 0.21105451881885529)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>15</th>
      <td>plunges you into a reality that is , more often then not , difficult and sad ,</td>
      <td>[(positive, 0.967541515827179), (negative, 0.03245845437049866)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>16</th>
      <td>overcomes the script 's flaws and envelops the audience in his character 's anguish , anger and frustration .</td>
      <td>[(positive, 0.9953157901763916), (negative, 0.004684178624302149)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>17</th>
      <td>troubled and determined homicide cop</td>
      <td>[(negative, 0.6632784008979797), (positive, 0.33672159910202026)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>18</th>
      <td>human nature is a goofball movie , in the way that malkovich was , but it tries too hard</td>
      <td>[(positive, 0.5959018468856812), (negative, 0.40409812331199646)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>19</th>
      <td>to watch too many barney videos</td>
      <td>[(negative, 0.9909896850585938), (positive, 0.00901023019105196)]</td>
      <td>positive</td>
    </tr>
  </tbody>
</table>
</div>



```python
df.annotation.hist()
```




    <AxesSubplot:>




    
![png](https://huggingface.co/datasets/rubrix/sst2_with_predictions/resolve/main/output_9_1.png)
    



```python
# Get dataset slice with wrong predictions
df = rb.load("sst2", query="predicted:ko and annotated_as:negative").to_pandas()

# display first 20 examples
with pd.option_context('display.max_colwidth', None):
    display(df[["text", "prediction", "annotation"]].head(20))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>text</th>
      <th>prediction</th>
      <th>annotation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>plays like a living-room war of the worlds , gaining most of its unsettling force from the suggested and the unknown .</td>
      <td>[(positive, 0.9968075752258301), (negative, 0.003192420583218336)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a minimalist beauty and the beast</td>
      <td>[(positive, 0.9100378751754761), (negative, 0.08996208757162094)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>2</th>
      <td>accept it as life and</td>
      <td>[(positive, 0.9987508058547974), (negative, 0.0012492131209000945)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>3</th>
      <td>plunges you into a reality that is , more often then not , difficult and sad ,</td>
      <td>[(positive, 0.967541515827179), (negative, 0.03245845437049866)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>4</th>
      <td>overcomes the script 's flaws and envelops the audience in his character 's anguish , anger and frustration .</td>
      <td>[(positive, 0.9953157901763916), (negative, 0.004684178624302149)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>5</th>
      <td>and social commentary</td>
      <td>[(positive, 0.7863275408744812), (negative, 0.2136724889278412)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>6</th>
      <td>we do n't get williams ' usual tear and a smile , just sneers and bile , and the spectacle is nothing short of refreshing .</td>
      <td>[(positive, 0.9982783794403076), (negative, 0.0017216014675796032)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>7</th>
      <td>before pulling the plug on the conspirators and averting an american-russian armageddon</td>
      <td>[(positive, 0.6992855072021484), (negative, 0.30071452260017395)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>8</th>
      <td>in tight pants and big tits</td>
      <td>[(positive, 0.7850217819213867), (negative, 0.2149781733751297)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>9</th>
      <td>that it certainly does n't feel like a film that strays past the two and a half mark</td>
      <td>[(positive, 0.6591460108757019), (negative, 0.3408539891242981)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>10</th>
      <td>actress-producer and writer</td>
      <td>[(positive, 0.8167378306388855), (negative, 0.1832621842622757)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>11</th>
      <td>gives devastating testimony to both people 's capacity for evil and their heroic capacity for good .</td>
      <td>[(positive, 0.8960123062133789), (negative, 0.10398765653371811)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>12</th>
      <td>deep into the girls ' confusion and pain as they struggle tragically to comprehend the chasm of knowledge that 's opened between them</td>
      <td>[(positive, 0.9729612469673157), (negative, 0.027038726955652237)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>13</th>
      <td>a younger lad in zen and the art of getting laid in this prickly indie comedy of manners and misanthropy</td>
      <td>[(positive, 0.9875985980033875), (negative, 0.012401451356709003)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>14</th>
      <td>get on a board and , uh , shred ,</td>
      <td>[(positive, 0.5352609753608704), (negative, 0.46473899483680725)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>15</th>
      <td>so preachy-keen and</td>
      <td>[(positive, 0.9644021391868591), (negative, 0.035597823560237885)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>16</th>
      <td>there 's an admirable rigor to jimmy 's relentless anger , and to the script 's refusal of a happy ending ,</td>
      <td>[(positive, 0.9928517937660217), (negative, 0.007148175034672022)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>17</th>
      <td>` christian bale 's quinn ( is ) a leather clad grunge-pirate with a hairdo like gandalf in a wind-tunnel and a simply astounding cor-blimey-luv-a-duck cockney accent . '</td>
      <td>[(positive, 0.9713286757469177), (negative, 0.028671346604824066)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>18</th>
      <td>passion , grief and fear</td>
      <td>[(positive, 0.9849751591682434), (negative, 0.015024829655885696)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>19</th>
      <td>to keep the extremes of screwball farce and blood-curdling family intensity on one continuum</td>
      <td>[(positive, 0.8838250637054443), (negative, 0.11617499589920044)]</td>
      <td>negative</td>
    </tr>
  </tbody>
</table>
</div>



```python
# Get dataset slice with wrong predictions
df = rb.load("sst2", query="predicted:ko and score:{0.99 TO *}").to_pandas()

# display first 20 examples
with pd.option_context('display.max_colwidth', None):
    display(df[["text", "prediction", "annotation"]].head(20))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>text</th>
      <th>prediction</th>
      <th>annotation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>plays like a living-room war of the worlds , gaining most of its unsettling force from the suggested and the unknown .</td>
      <td>[(positive, 0.9968075752258301), (negative, 0.003192420583218336)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>1</th>
      <td>accept it as life and</td>
      <td>[(positive, 0.9987508058547974), (negative, 0.0012492131209000945)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>2</th>
      <td>overcomes the script 's flaws and envelops the audience in his character 's anguish , anger and frustration .</td>
      <td>[(positive, 0.9953157901763916), (negative, 0.004684178624302149)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>3</th>
      <td>will no doubt rally to its cause , trotting out threadbare standbys like ` masterpiece ' and ` triumph ' and all that malarkey ,</td>
      <td>[(negative, 0.9936562180519104), (positive, 0.006343740504235029)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>4</th>
      <td>we do n't get williams ' usual tear and a smile , just sneers and bile , and the spectacle is nothing short of refreshing .</td>
      <td>[(positive, 0.9982783794403076), (negative, 0.0017216014675796032)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>5</th>
      <td>somehow manages to bring together kevin pollak , former wrestler chyna and dolly parton</td>
      <td>[(negative, 0.9979034662246704), (positive, 0.002096540294587612)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>6</th>
      <td>there 's an admirable rigor to jimmy 's relentless anger , and to the script 's refusal of a happy ending ,</td>
      <td>[(positive, 0.9928517937660217), (negative, 0.007148175034672022)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>7</th>
      <td>the bottom line with nemesis is the same as it has been with all the films in the series : fans will undoubtedly enjoy it , and the uncommitted need n't waste their time on it</td>
      <td>[(positive, 0.995850682258606), (negative, 0.004149340093135834)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>8</th>
      <td>is genial but never inspired , and little</td>
      <td>[(negative, 0.9921030402183533), (positive, 0.007896988652646542)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>9</th>
      <td>heaped upon a project of such vast proportions need to reap more rewards than spiffy bluescreen technique and stylish weaponry .</td>
      <td>[(negative, 0.9958089590072632), (positive, 0.004191054962575436)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>10</th>
      <td>than recommended -- as visually bland as a dentist 's waiting room , complete with soothing muzak and a cushion of predictable narrative rhythms</td>
      <td>[(negative, 0.9988711476325989), (positive, 0.0011287889210507274)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>11</th>
      <td>spectacle and</td>
      <td>[(positive, 0.9941601753234863), (negative, 0.005839805118739605)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>12</th>
      <td>groan and</td>
      <td>[(negative, 0.9987359642982483), (positive, 0.0012639997294172645)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>13</th>
      <td>'re not likely to have seen before , but beneath the exotic surface ( and exotic dancing ) it 's surprisingly old-fashioned .</td>
      <td>[(positive, 0.9908103942871094), (negative, 0.009189637377858162)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>14</th>
      <td>its metaphors are opaque enough to avoid didacticism , and</td>
      <td>[(negative, 0.990602970123291), (positive, 0.00939704105257988)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>15</th>
      <td>by kevin bray , whose crisp framing , edgy camera work , and wholesale ineptitude with acting , tone and pace very obviously mark him as a video helmer making his feature debut</td>
      <td>[(positive, 0.9973387122154236), (negative, 0.0026612314395606518)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>16</th>
      <td>evokes the frustration , the awkwardness and the euphoria of growing up , without relying on the usual tropes .</td>
      <td>[(positive, 0.9989104270935059), (negative, 0.0010896018939092755)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>17</th>
      <td>, incoherence and sub-sophomoric</td>
      <td>[(negative, 0.9962475895881653), (positive, 0.003752368036657572)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>18</th>
      <td>seems intimidated by both her subject matter and the period trappings of this debut venture into the heritage business .</td>
      <td>[(negative, 0.9923072457313538), (positive, 0.007692818529903889)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>19</th>
      <td>despite downplaying her good looks , carries a little too much ai n't - she-cute baggage into her lead role as a troubled and determined homicide cop to quite pull off the heavy stuff .</td>
      <td>[(negative, 0.9948075413703918), (positive, 0.005192441400140524)]</td>
      <td>positive</td>
    </tr>
  </tbody>
</table>
</div>



```python
# Get dataset slice with wrong predictions
df = rb.load("sst2", query="predicted:ko and score:{* TO 0.6}").to_pandas()

# display first 20 examples
with pd.option_context('display.max_colwidth', None):
    display(df[["text", "prediction", "annotation"]].head(20))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>text</th>
      <th>prediction</th>
      <th>annotation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>get on a board and , uh , shred ,</td>
      <td>[(positive, 0.5352609753608704), (negative, 0.46473899483680725)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>1</th>
      <td>is , truly and thankfully , a one-of-a-kind work</td>
      <td>[(positive, 0.5819814801216125), (negative, 0.41801854968070984)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>2</th>
      <td>starts as a tart little lemon drop of a movie and</td>
      <td>[(negative, 0.5641832947731018), (positive, 0.4358167052268982)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>3</th>
      <td>between flaccid satire and what</td>
      <td>[(negative, 0.5532692074775696), (positive, 0.44673076272010803)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>4</th>
      <td>it certainly does n't feel like a film that strays past the two and a half mark</td>
      <td>[(negative, 0.5386656522750854), (positive, 0.46133431792259216)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>5</th>
      <td>who liked there 's something about mary and both american pie movies</td>
      <td>[(negative, 0.5086333751678467), (positive, 0.4913666248321533)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>6</th>
      <td>many good ideas as bad is the cold comfort that chin 's film serves up with style and empathy</td>
      <td>[(positive, 0.557632327079773), (negative, 0.44236767292022705)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>7</th>
      <td>about its ideas and</td>
      <td>[(positive, 0.518638551235199), (negative, 0.48136141896247864)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>8</th>
      <td>of a sick and evil woman</td>
      <td>[(negative, 0.5554516315460205), (positive, 0.4445483684539795)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>9</th>
      <td>though this rude and crude film does deliver a few gut-busting laughs</td>
      <td>[(positive, 0.5045541524887085), (negative, 0.4954459071159363)]</td>
      <td>negative</td>
    </tr>
    <tr>
      <th>10</th>
      <td>to squeeze the action and our emotions into the all-too-familiar dramatic arc of the holocaust escape story</td>
      <td>[(negative, 0.5050069093704224), (positive, 0.49499306082725525)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>11</th>
      <td>that throws a bunch of hot-button items in the viewer 's face and asks to be seen as hip , winking social commentary</td>
      <td>[(negative, 0.5873904228210449), (positive, 0.41260960698127747)]</td>
      <td>positive</td>
    </tr>
    <tr>
      <th>12</th>
      <td>'s soulful and unslick</td>
      <td>[(positive, 0.5931627750396729), (negative, 0.40683719515800476)]</td>
      <td>negative</td>
    </tr>
  </tbody>
</table>
</div>



```python
from rubrix.metrics.commons import *
```


```python
text_length("sst2", query="predicted:ko").visualize()
```
![example.png](https://huggingface.co/datasets/rubrix/sst2_with_predictions/resolve/main/output_14_0.png)