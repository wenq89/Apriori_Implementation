import pandas as pd
import time
from itertools import combinations
from operator import itemgetter
from pandas import DataFrame
# from files import CONSTANTS


def apriori(data_df, support):
    # create an empty data frame which will be returned by Apriori function
    # apr_df = pd.DataFrame()

    # add item_counts column to dataset representing how many items in the corresponding transaction.
    data_df['item_counts'] = data_df['StockCode'].str.count(" ") + 1
    # print(data_df)

    start_time = time.time()

    # frequent single item set
    freq_single_itemssets = (data_df['StockCode'].str.split(" ", expand=True))\
        .apply(pd.value_counts).sum(axis=1)\
        .where(lambda item_count: item_count >= support)\
        .dropna()

    end_time = time.time()
    print("Time(single):", end_time - start_time)

    # add to data frame
    apr_df = pd.DataFrame(
        {
            'item_set': freq_single_itemssets.index,
            'sup': freq_single_itemssets.values,
            'set_size': 1
        }
    )

    print("\nTSET_OUTPUT: frequent single item set:", len(apr_df.index))
    # print(apr_df)

    # mapping
    data_df['StockCode'] = data_df['StockCode'].apply(lambda item_set: set(map(str, item_set.split(" "))))

    freq_single_items_set = set(freq_single_itemssets.index)

    # find frequent itemsets where size >= 2
    for k in range(2, len(freq_single_items_set)):

        # select transactions which contain at least k-items
        data_df = data_df[data_df['item_counts'] >= k]

        # generate frequent k-itemsets
        freq_k_itemssets = data_df['StockCode']\
            .apply(lambda tran: pd.Series(
                com if set(com).issubset(tran)
                else None for com in combinations(freq_single_items_set, k)))\
            .apply(lambda col: [col.dropna().unique()[0], col.count()] if col.count() >= support else None)\
            .dropna()

        # no more frequent itemset in this level, then end the process.
        if freq_k_itemssets.empty:
            end_time = time.time()
            print("\nTSET_OUTPUT: no frequent", k, "-item sets, Time(",k,"-itemset):", end_time - start_time)
            # print("additional frequent item set found: ", len(temp_df.index))
            # print("total frequent item set found: ", len(apr_df))
            break

        # otherwise add to apr_df
        temp_df = pd.DataFrame(
            {
                'item_set': list(map(itemgetter(0), freq_k_itemssets.values)),
                'sup': list(map(itemgetter(1), freq_k_itemssets.values)),
                'set_size': k
            }
        )

        apr_df: DataFrame = apr_df.append(temp_df, ignore_index=True, sort=True)

        end_time = time.time()
        print("\nTSET_OUTPUT: frequent", k, "-item sets end time:", end_time - start_time)
        print("additional frequent item set found: ", len(temp_df.index))
        print("total frequent item set found: ", len(apr_df))

    # apr_df.to_excel(CONSTANTS['APRI_OUTPUT_FILE'])
    return apr_df
