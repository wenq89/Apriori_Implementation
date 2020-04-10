import pandas as pd
import numpy as np
from files import CONSTANTS
# import time
# pd.options.mode.chained_assignment = None


# unique countries in online_retail_II, see result in README
def find_countries():
    excel_data_df = pd.read_excel(CONSTANTS['ORIGINAL_FILE'])
    countries = excel_data_df.Country.value_counts()
    print(countries)


# select transaction histories that are happened in UK to excel file, output to refined_dataset.xlsx
def regenerate_new_datafile():
    excel_data_df = pd.read_excel(CONSTANTS['ORIGINAL_FILE'])

    # select UK and remove transactions without items.
    excel_data_df = excel_data_df.loc[excel_data_df['Country'] == 'United Kingdom']
    excel_data_df['StockCode'].replace('', np.nan, inplace=True)
    excel_data_df.dropna(subset=['StockCode'], inplace=True)

    # select only three columns that will be used later
    excel_data_df = excel_data_df[['Invoice', 'StockCode', 'Description']]

    # group by same transaction ID
    data_series = excel_data_df.groupby('Invoice')['StockCode'].unique()
    # print(data_series)

    for index in range(len(data_series.values)):
        if "\'" in str(data_series.values[index]):
            data_series.values[index] = str(data_series.values[index]).replace('\'', '')

    data_series.to_excel(CONSTANTS['REFINED_FILE'])


def cleanup():
    data = pd.read_excel(CONSTANTS['REFINED_FILE'])

    # trim out [ at the beginning and ] at the end.
    for ch in ['[', ']']:
        data['StockCode'] = data['StockCode'].str.replace(ch, '')

    return data

# find_countries()
# regenerate_new_datafile()
