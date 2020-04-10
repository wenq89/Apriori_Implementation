-----------------------------------------
TEST CASE: half of data set, support = 500
-----------------------------------------
Time ( 28.18992567062378 ) preprocessing completed
Time ( 28.950919151306152 ) clean up completed
  item_set    sup  set_size
0    22423  851.0         1
1    22457  512.0         1
2    22720  512.0         1
3    47566  591.0         1
4   85099B  665.0         1
5   85123A  928.0         1
Time ( 34.505131006240845 ) Apriori data mining completed
number of frequent item sets:  5
End of process

Process finished with exit code 0

250-78
270-66
275 - Process finished with exit code -1073741819 (0xC0000005)
277-64 19 sec
280-64 17 sec
290-57 -14.744sec  single-item set same
300-52 - 14sec  single-item set same

too many domain items

SEVERAL CHANGES FROM THE PROPOSAL
keep getting MemoryError if I set the support under 260, the memory is exhausted.
I have to find a balance between running time and memory usage.
After several test cases, I found support = 270  is a perfect balance for testing.

speed up the process of discovering subsets - so used stockcode

can not test, it is finding combinations.
Apriori space complexity is exponential, my computer does not support.
unnecessary database scan, but too many combinations.



# preprocessing
# result of the unique countries (call the by method find_countries)
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

# extract the transactions occurred in United Kingdom
Time ( 0.03091573715209961 ) clean up completed
Time(single): 0.0479123592376709

TSET_OUTPUT: frequent single item set: 22
   item_set  sup  set_size
0         2  2.0         1
1     20723  6.0         1
2     20725  5.0         1
3     21033  5.0         1
4     21094  5.0         1
5     21212  6.0         1
6     21559  6.0         1
7     21929  5.0         1
8     21931  6.0         1
9     21975  6.0         1
10    21977  6.0         1
11    22352  6.0         1
12    22386  4.0         1
13        3  3.0         1
14        4  2.0         1
15   84519A  6.0         1
16    84991  5.0         1
17   84997B  4.0         1
18   84997C  5.0         1
19   85071B  6.0         1
20   85099C  5.0         1
21   85183B  6.0         1

----------------------------------------
SMALL DATABASE SIMPLE TEST RESULT
----------------------------------------

TSET_OUTPUT: frequent 2 -item sets end time: 0.24637985229492188
additional frequent item set found:  224
total frequent item set found:  246

TSET_OUTPUT: frequent 3 -item sets end time: 1.4377615451812744
additional frequent item set found:  1411
total frequent item set found:  1657

TSET_OUTPUT: frequent 4 -item sets end time: 6.582533836364746
additional frequent item set found:  6189
total frequent item set found:  7846

TSET_OUTPUT: frequent 5 -item sets end time: 23.02248740196228
additional frequent item set found:  20150
total frequent item set found:  27996

TSET_OUTPUT: frequent 6 -item sets end time: 65.70711374282837
additional frequent item set found:  50651
total frequent item set found:  78647

TSET_OUTPUT: frequent 7 -item sets end time: 171.71623039245605
additional frequent item set found:  100886
total frequent item set found:  179533

TSET_OUTPUT: frequent 8 -item sets end time: 335.6586742401123
additional frequent item set found:  162039
total frequent item set found:  341572

TSET_OUTPUT: frequent 9 -item sets end time: 570.3182363510132
additional frequent item set found:  212323
total frequent item set found:  553895

TSET_OUTPUT: frequent 10 -item sets end time: 843.3851523399353
additional frequent item set found:  228558
total frequent item set found:  782453

TSET_OUTPUT: frequent 11 -item sets end time: 1131.4496388435364
additional frequent item set found:  202731
total frequent item set found:  985184

TSET_OUTPUT: frequent 12 -item sets end time: 1338.7661845684052
additional frequent item set found:  148060
total frequent item set found:  1133244

TSET_OUTPUT: frequent 13 -item sets end time: 1486.3790159225464
additional frequent item set found:  88620
total frequent item set found:  1221864

TSET_OUTPUT: frequent 14 -item sets end time: 1571.9975497722626
additional frequent item set found:  43079
total frequent item set found:  1264943

TSET_OUTPUT: frequent 15 -item sets end time: 1615.4085357189178
additional frequent item set found:  16760
total frequent item set found:  1281703

TSET_OUTPUT: frequent 16 -item sets end time: 1633.0221195220947
additional frequent item set found:  5102
total frequent item set found:  1286805

TSET_OUTPUT: frequent 17 -item sets end time: 1638.8819885253906
additional frequent item set found:  1173
total frequent item set found:  1287978

TSET_OUTPUT: frequent 18 -item sets end time: 1640.4385612010956
additional frequent item set found:  192
total frequent item set found:  1288170

TSET_OUTPUT: frequent 19 -item sets end time: 1640.8170628547668
additional frequent item set found:  20
total frequent item set found:  1288190

TSET_OUTPUT: frequent 20 -item sets end time: 1640.9222934246063
additional frequent item set found:  1
total frequent item set found:  1288191

-----------------------------------------------------------------
Time ( 136.27049446105957 ) preprocessing completed
Time ( 137.85071396827698 ) clean up completed
Time(single): 7.825089454650879

TSET_OUTPUT: frequent single item set: 134
    item_set     sup  set_size
0     15056N   517.0         1
1      20685   905.0         1
2      20713   611.0         1
3      20718   555.0         1
4      20719   543.0         1
5      20723   591.0         1
6      20724   855.0         1
7      20725  1336.0         1
8      20726   791.0         1
9      20727  1013.0         1
10     20728   823.0         1
11     20914  1046.0         1
12     20971   594.0         1
13     20972   743.0         1
14     20975   503.0         1
15     21034  1023.0         1
16     21080  1007.0         1
17     21166   649.0         1
18     21174   578.0         1
19     21175   803.0         1
20     21181   913.0         1
21     21210   580.0         1
22     21212  1526.0         1
23     21213   726.0         1
24     21217   540.0         1
25     21231   947.0         1
26     21232  1550.0         1
27     21314   531.0         1
28     21429   612.0         1
29     21481   529.0         1
..       ...     ...       ...
104    82483   600.0         1
105    82486   681.0         1
106   82494L  1034.0         1
107    82580   661.0         1
108    82583   548.0         1
109    82600   621.0         1
110   84029E   720.0         1
111   84029G   569.0         1
112    84378   509.0         1
113   84406B   531.0         1
114   84520B   547.0         1
115    84692   504.0         1
116    84755   604.0         1
117    84836   809.0         1
118    84879  1246.0         1
119    84946   824.0         1
120   84970L   550.0         1
121   84970S   811.0         1
122    84978   654.0         1
123    84991  1128.0         1
124    84992   742.0         1
125   84997B   517.0         1
126   85099B  1743.0         1
127   85099C   879.0         1
128   85099F   951.0         1
129   85123A  3079.0         1
130    85150   601.0         1
131    85152   742.0         1
132      DOT   702.0         1
133        M   657.0         1
-----------------------------------------------------------
Time ( 1.2971901893615723 ) clean up completed
Time(single): 7.710895776748657

TSET_OUTPUT: frequent single item set: 19
   item_set     sup  set_size
0     20725  1336.0         1
1     20727  1013.0         1
2     20914  1046.0         1
3     21034  1023.0         1
4     21080  1007.0         1
5     21212  1526.0         1
6     21232  1550.0         1
7     21754  1211.0         1
8     21755  1001.0         1
9     21931  1066.0         1
10    22139  1000.0         1
11    22383  1002.0         1
12    22423  1887.0         1
13    22470  1015.0         1
14   82494L  1034.0         1
15    84879  1246.0         1
16    84991  1128.0         1
17   85099B  1743.0         1
18   85123A  3079.0         1

TSET_OUTPUT: no frequent 2 -item sets: 16.871323347091675
Time ( 18.221359968185425 ) Apriori data mining completed
End of process

Process finished with exit code 0
------------------------------------
1000
Time ( 1.396348237991333 ) clean up completed
Time(single): 7.912383556365967

TSET_OUTPUT: frequent single item set: 26
   item_set     sup  set_size
0     20725  1336.0         1
1     20727  1013.0         1
2     20914  1046.0         1
3     21034  1023.0         1
4     21080  1007.0         1
5     21212  1526.0         1
6     21232  1550.0         1
7     21754  1211.0         1
8     21755  1001.0         1
9     21843   953.0         1
10    21931  1066.0         1
11    21977   975.0         1
12    22138   961.0         1
13    22139  1000.0         1
14    22383  1002.0         1
15    22411   958.0         1
16    22423  1887.0         1
17    22469   955.0         1
18    22470  1015.0         1
19    48138   991.0         1
20   82494L  1034.0         1
21    84879  1246.0         1
22    84991  1128.0         1
23   85099B  1743.0         1
24   85099F   951.0         1
25   85123A  3079.0         1

TSET_OUTPUT: no frequent 2 -item sets: 20.056144952774048
Time ( 21.504354000091553 ) Apriori data mining completed
End of process

Process finished with exit code 0
-----------------------------------------------
900
Time ( 1.366607904434204 ) clean up completed
Time(single): 8.754156112670898

TSET_OUTPUT: frequent single item set: 35
   item_set     sup  set_size
0     20685   905.0         1
1     20725  1336.0         1
2     20727  1013.0         1
3     20914  1046.0         1
4     21034  1023.0         1
5     21080  1007.0         1
6     21181   913.0         1
7     21212  1526.0         1
8     21231   947.0         1
9     21232  1550.0         1
10    21733   949.0         1
11    21754  1211.0         1
12    21755  1001.0         1
13    21790   907.0         1
14    21843   953.0         1
15    21931  1066.0         1
16    21977   975.0         1
17    22138   961.0         1
18    22139  1000.0         1
19    22197   903.0         1
20    22383  1002.0         1
21    22384   908.0         1
22    22386   919.0         1
23    22411   958.0         1
24    22423  1887.0         1
25    22469   955.0         1
26    22470  1015.0         1
27    47566   908.0         1
28    48138   991.0         1
29   82494L  1034.0         1
30    84879  1246.0         1
31    84991  1128.0         1
32   85099B  1743.0         1
33   85099F   951.0         1
34   85123A  3079.0         1

TSET_OUTPUT: no frequent 2 -item sets: 27.104284286499023
Time ( 28.533745288848877 ) Apriori data mining completed
End of process

Process finished with exit code 0
---------------------------------------------------------
750
Time ( 1.3937854766845703 ) clean up completed
Time(single): 7.978210687637329

TSET_OUTPUT: frequent single item set: 55

TSET_OUTPUT: no frequent 2 -item sets, Time( 2 -itemset): 41.90137839317322
Time ( 43.353007078170776 ) Apriori data mining completed
End of process

Process finished with exit code 0
---------------------------------------------
730
Time ( 1.3264753818511963 ) clean up completed
Time(single): 8.350975036621094

TSET_OUTPUT: frequent single item set: 61
MemoryError

Process finished with exit code 1
---------------------------------------------
740
Time ( 1.311554193496704 ) clean up completed
Time(single): 7.797938585281372

TSET_OUTPUT: frequent single item set: 58
MemoryError

Process finished with exit code 1
-------------------------------------------
745
Time ( 1.4805920124053955 ) clean up completed
Time(single): 8.37757420539856

TSET_OUTPUT: frequent single item set: 55

TSET_OUTPUT: no frequent 2 -item sets, Time( 2 -itemset): 43.43062925338745
Time ( 44.97705149650574 ) Apriori data mining completed
End of process

Process finished with exit code 0
-----------------------------------------------
743
Time ( 1.8651962280273438 ) clean up completed
Time(single): 8.67062497138977

TSET_OUTPUT: frequent single item set: 56

TSET_OUTPUT: no frequent 2 -item sets, Time( 2 -itemset): 45.82539892196655
Time ( 47.74844670295715 ) Apriori data mining completed
End of process

Process finished with exit code 0
-------------------------------------------------
742
Time ( 1.3174543380737305 ) clean up completed
Time(single): 7.906069040298462

TSET_OUTPUT: frequent single item set: 58
MemoryError

Process finished with exit code 1
------------------------------------------