import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import time


def algorithm():
    # display complete contents of a dataframe without any kind of truncation
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)

    start_time = time.time();
    data = pd.read_excel('Test_Retail.xlsx')  # Online_Retail.xlsx Test_Retail.xlsx

    # load, explore phase
    # load data and explore the columns of data and different regions of transactions.
    data.head()
    data.columns
    data.Country.unique()

    # cleaning phase
    # Stripping extra spaces in the description
    data['Description'] = data['Description'].str.strip()

    # Dropping the rows without any invoice number
    data.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
    data['InvoiceNo'] = data['InvoiceNo'].astype('str')

    # Dropping all transactions which were done on credit
    # data = datUk_transactions = (data[data['Country'] == "United Kingdom"]
    #                  .groupby(['InvoiceNo', 'Description'])['Quantity']
    #                  .sum().unstack().reset_index().fillna(0)
    #                  .set_index('InvoiceNo'))
    #
    #     print(data[data['Country'] == "United Kingdom"]
    #                  .groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack())
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
    #
    #     f = open('output.txt', 'w')
    #     with np.printoptions(threshold=False):
    #         print(basket_UK, file=f)
    #         print(rules.head(), file=f)
    #
    #     end_time = time.time()
    #     print("Time elapsed: ", end_time - start_time)a[~data['InvoiceNo'].str.contains('C')]

    # Transactions done in the United Kingdom


algorithm()