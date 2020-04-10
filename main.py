from apriori_algorithm import apriori
from preprocessing import *
import time


def main():
    start_time = time.time()
    # the regeneration only needs to be done once
    # regenerate_new_datafile()
    # end_time = time.time()
    # print("Time (", end_time - start_time, ") preprocessing completed")
    data = cleanup()
    end_time = time.time()
    print("Time (", end_time - start_time, ") clean up completed")
    apr_data = apriori(data, 796)
    end_time = time.time()
    apr_count = len(apr_data.index)
    apr_data.to_excel(CONSTANTS['APRI_OUTPUT_FILE'])
    print("Time (", end_time - start_time, ") Apriori data mining completed")
    # print("number of frequent item sets: ", apr_count)
    # print(apr_data, "\n")
    print("End of process")


main()
