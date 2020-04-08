import pandas as pd
import numpy as np

CONSTANTS = {
    'FILE': 'online_retail_II.xlsx'  # online_retail_II.xlsx Test_Retail.xlsx
}


# unique countries in online_retail_II, see result in README
def find_countries():
    excel_data_df = pd.read_excel(CONSTANTS['FILE'])
    countries = excel_data_df.Country.value_counts()
    print(countries)


# select transaction histories that are happened in UK to excel file, output to refined_dataset.xlsx
def regenerate_new_datafile():
    excel_data_df = pd.read_excel(CONSTANTS['FILE'])

    # select UK and remove transactions without items.
    excel_data_df = excel_data_df.loc[excel_data_df['Country'] == 'United Kingdom']
    excel_data_df['Description'].replace('', np.nan, inplace=True)
    excel_data_df.dropna(subset=['Description'], inplace=True)

    # select only three columns that will be used later
    excel_data_df = excel_data_df[['Invoice', 'StockCode', 'Description']]

    # group by same transaction ID
    data_series = excel_data_df.groupby('Invoice')['Description'].unique()

    # extract to new excel file
    data_series.to_excel('refined_dataset.xlsx')
    # print(excel_data_df)

# find_countries()
regenerate_new_datafile()

