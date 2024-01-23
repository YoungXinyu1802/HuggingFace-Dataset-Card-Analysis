This dataset is based on the "cumulative" configuration of the MultiWoz 2.2 dataset available also on the [HuggingFace Hub](https://huggingface.co/datasets/multi_woz_v22). 
Therefore, the system and user utterances, the active intents, and the services are exactly the same.

In addition to the data present in version 2.2, this dataset contains, for each dialogue turn, the annotations from versions 2.1, 2.3, and 2.4.


NOTE:

  - Each dialogue turn is composed of a system utterance and a user utterance, in this exact order
  
  - The initial system utterance is filled in with the `none` string
 
  - In the last dialogue turn is always the system that greets the user; this last turn is kept and the user utterance is filled in with the `none` string (usually during evaluation this dialogue turn is not considered)
  
  - To be able to save data as an arrow file you need to "pad" the states to all have the same keys. To do this the None value is introduced. Therefore, when you load it back it is convenient to have a way to remove the "padding". In order to do so, a function like the following can help
  
  ```python 
  def remove_empty_slots(state: Union[Dict[str, Union[List[str], None]], None]) -> Union[Dict[str, List[str]], None]:

    if state is None:
        return None

    return {k: v for k, v in state.items() if v is not None}
  ```
  
  - The schema has been updated to make all the versions compatible. Basically, the "book" string has been removed from slots in v2.2. The updated schema is the following
  
```yaml
attraction-area
attraction-name
attraction-type
hotel-area
hotel-day
hotel-internet
hotel-name
hotel-parking
hotel-people
hotel-pricerange
hotel-stars
hotel-stay
hotel-type
restaurant-area
restaurant-day
restaurant-food
restaurant-name
restaurant-people
restaurant-pricerange
restaurant-time
taxi-arriveby
taxi-departure
taxi-destination
taxi-leaveat
train-arriveby
train-day
train-departure
train-destination
train-leaveat
train-people
```