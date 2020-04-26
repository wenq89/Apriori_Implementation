run main.py
-
There are three major steps in this program:
1. preprocessing
2. cleaning
3. apriori

the program takes about 5 minutes for preprocessing, but it only needs to be done once.
If you accidently deleted refined_dataset.xlsx, please uncomment regenerate_new_datafile() in main.py and run the program.

preprocessing:find unique countries, regenerate the data set
-
Result of the unique countries (call the by method find_countries)

United Kingdom          485852
EIRE                      9670
Germany                   8129
France                    5772
Netherlands               2769
Spain                     1278
Switzerland               1187
Portugal                  1101
Belgium                   1054
Channel Islands            906
Sweden                     902
Italy                      731
Australia                  654
Cyprus                     554
Austria                    537
Greece                     517
United Arab Emirates       432
Denmark                    428
Norway                     369
Finland                    354
Unspecified                310
USA                        244
Japan                      224
Poland                     194
Malta                      172
Lithuania                  154
Singapore                  117
RSA                        111
Bahrain                    107
Canada                      77
Thailand                    76
Hong Kong                   76
Israel                      74
Iceland                     71
Korea                       63
Brazil                      62
West Indies                 54
Bermuda                     34
Nigeria                     32
Lebanon                     13

We will only extract the transactions occurred in United Kingdom to a new file named "refined_dataset.xlsx"

cleaning
-
clean up extra characters in the data set, e.g., [ ]

files
-
all the files are under "files" directory.
- files/online_retail_II.xlsx
original file downloaded from http://archive.ics.uci.edu/ml/datasets.php?format=&task=cla&att=&area=&numAtt=&numIns=&type=&sort=dateDown&view=table
- files/refined_dataset.xlsx
the file that is generated by preprocessing process
- files/apriori_result.xlsx
final output which contains all the frequent item sets.
- test files: simpleTest.xlsx,Test_Retail.xlsx,testhalf_reail.xlsx

testing: using different support values | big datset and small dataset
-
find test_result file

Apriori algorithm running time analysis
-
find files under images/ directory1
