import pandas as pd
from util import get_section_info

def process_dataframe(input_df):
    category_pandas = get_section_info(input_df)
    category_pandas_df = pd.concat(category_pandas, axis=1)
    return category_pandas_df

def main():

    dataset_card = pd.read_parquet('../../Data/Dataset_Info/datasetcard_info.parquet')
    dataset_card = dataset_card.sort_values(by='downloads', ascending=False, ignore_index=True)
    print(len(dataset_card))

    category_pandas_dataset_card = process_dataframe(dataset_card)
    category_pandas_dataset_card.to_parquet('datasetcard_sections_info.parquet')

    return 

if __name__ == '__main__':
    main()
