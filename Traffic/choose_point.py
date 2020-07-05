# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 10:12 下午
# @Author  : Zehua Yu
# @Email   : 19zhyu@stu.edu.cn
# @File    : choose_point.py
# @Software : PyCharm

"""
This is for choosing valid stations of PeMS Data.

You can set the column, which you want to get.(Here is 11, which is the Avg_speed)
You can set the numbers of stations you want to check.(Here is 2000)

The data is not a 0 or None is valid in our method.
"""

import pandas as pd
import csv

df1 = pd.read_csv('d03_text_station_5min_2020_03_01.csv', header=None)
point = 'ch_point.csv'
df1.fillna(0)

p_n = []
for i in range(2000):
    if df1.iloc[i, 11] > 0:
        print(df1.iloc[i, 11])
        p_n.append(df1.iloc[i, 1])

with open(point, "a") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(p_n)
    csv_file.close()
