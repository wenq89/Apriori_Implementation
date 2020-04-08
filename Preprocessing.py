import pandas as pd
import numpy as np
# from mlxtend.frequent_patterns import apriori, association_rules
# import time
from itertools import combinations
from operator import itemgetter
pd.options.mode.chained_assignment = None

CONSTANTS = {
    'ORIGINAL_FILE': 'Test_Retail.xlsx',  # online_retail_II.xlsx Test_Retail.xlsx
    'REFINED_FILE': 'refined_Test_Retail.xlsx' # refined_dataset.xlsx refined_Test_Retail.xlsx
}


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
    excel_data_df['Description'].replace('', np.nan, inplace=True)
    excel_data_df.dropna(subset=['Description'], inplace=True)

    # select only three columns that will be used later
    excel_data_df = excel_data_df[['Invoice', 'StockCode', 'Description']]

    # group by same transaction ID
    data_series = excel_data_df.groupby('Invoice')['StockCode'].unique()
    # print(data_series)
    # data_series.to_frame()
    for index in range(len(data_series.values)):
        if "\'" in str(data_series.values[index]):
            data_series.values[index] = str(data_series.values[index]).replace('\'', '')

    # data_series.values[0] = str(data_series.values[0]).replace('\'', '')


    #
    # print(data_series.values[0][0])
    # print(data_series.values[0][1])
    # print(data_series.values[0][2])
    # print(data_series.values[0][3])
    # print(data_series.values[0][4])
    # # print(type(x))
    # print(type(data_series.values[0]))
    # print(data_series['StockCode'])
    # extract to new excel file
    data_series.to_excel('refined2.xlsx')
    # print(excel_data_df)

# find_countries()
# regenerate_new_datafile()

def test():
    data = pd.read_excel('refined2.xlsx')
    # print(type(refined_data_df['StockCode'][0]))
    # print(refined_data_df['StockCode'][0].replace('[', ''))
    # perform_apriori(data=refined_data_df, support_count=1)

    # trim out [ at the beginning and ] at the end.
    for ch in ['[', ']']:
        data['StockCode'] = data['StockCode'].str.replace(ch, '')

    print(data)
    print("asdasdsssssssssssssssssssssssssssssss")

    # for index in range(len(data['StockCode'])):
    #     for ch in ['[', ']']:
    #         data['StockCode'][index] = data['StockCode'][index].replace(ch, '')
        # print(data['StockCode'][index])

    # single item set
    support_count = 2
    freq_single_items = (data['StockCode'].str.split(" ", expand=True))\
        .apply(pd.value_counts).sum(axis=1).where(lambda value: value >= support_count).dropna()
    # print(single_items)

    # store single item set to new data frame
    apriori_df = pd.DataFrame(
        {'items': freq_single_items.index,
         'support_count': freq_single_items.values,
         'freq_item_setsize': 1})
    # print(apriori_df)

    # add set_size column to original dataset representing how many items in the corresponding transaction.
    data['set_size'] = data['StockCode'].str.count(" ") + 1
    # print(data)

    data['StockCode'] = data['StockCode'].apply(lambda item_set: set(map(str, item_set.split(" "))))
    # print(data)

    freq_single_items_set = set(freq_single_items.index)
    # print(freq_single_items_set)
    # print("--------------------------------------==========================")
    #
    for length in range(2, 3): #len(freq_single_items_set)
        # if the transaction has more than "length"-itemsets
        data = data[data['set_size'] >= length]
        d = data['StockCode'] \
            .apply(lambda st: pd.Series(s if set(s).issubset(st) else None for s in combinations(freq_single_items_set, length))) \
            .apply(lambda col: [col.dropna().unique()[0], col.count()] if col.count() >= support_count else None).dropna()
        # print(d)
        # print("--------------------------------------")
        if d.empty:
            break

        apriori_df = apriori_df.append(pd.DataFrame(
            {'items': list(map(itemgetter(0), d.values)), 'support_count': list(map(itemgetter(1), d.values)),
             'freq_item_setsize': length}), ignore_index=True, sort=True)
        # print(apriori_df)
        # print("--------------------------------------")

    print(apriori_df)


# string clean [ and ]
# split string, and count each item store in global dict



    #print(refined_data_df['Description'][0].split(' \'|[''}')[1])
    #print(refined_data_df['Description'][0].split(' \'|['|'}')[2])

test()
# def test():
#     # refined_data_df = pd.read_excel(CONSTANTS['REFINED_FILE'])
#     # print(refined_data_df['Description'][0].split(' ')[0])
#     start_time = time.time()
#     data = pd.read_excel('Test_Retail.xlsx')
#     # load, explore phase
#     # load data and explore the columns of data and different regions of transactions.
#     data.head()
#     data.columns
#     data.Country.unique()
#
#     # cleaning phase
#     # Stripping extra spaces in the description
#     # data['Description'] = data['Description'].str.strip()
#     Uk_transactions = (data[data['Country'] == "United Kingdom"]
#                        .groupby(['Invoice', 'Description'])['Quantity']
#                        .sum().unstack().reset_index().fillna(0)
#                        .set_index('Invoice'))
#
#     # print(list(basket_UK['ASSORTED COLOUR BIRD ORNAMENT']))
#
#     # Defining the hot encoding function to make the data suitable
#     # for the concerned libraries
#     def hot_encode(x):
#         if x <= 0:
#             return 0
#         if x >= 1:
#             return 1
#
#     # Encoding the datasets
#     basket_encoded = Uk_transactions.applymap(hot_encode)
#     Uk_transactions = basket_encoded
#
#     # Building the model
#     frq_items = apriori(Uk_transactions, min_support=0.05, use_colnames=True)
#
#     end_time = time.time()
#     print("Time elapsed_Building Model: ", end_time - start_time)
#
#     # Collecting the inferred rules in a dataframe
#     rules = association_rules(frq_items, metric="lift", min_threshold=1)
#     rules = rules.sort_values(['confidence', 'lift'], ascending=[False, False])
#     print(rules.head())
#
#     # f = open('output.txt', 'w')
#     # with np.printoptions(threshold=False):
#     #     print(basket_UK, file=f)
#     #     print(rules.head(), file=f)
#
#     end_time = time.time()
#     print("Time elapsed: ", end_time - start_time)
#
# test()