# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 10:12 下午
# @Author  : Zehua Yu
# @Email   : 19zhyu@stu.edu.cn
# @File    : get_V_from_or.py
# @Software : PyCharm

import pandas as pd
import csv

"""
m is month，days is the numbers of day you want.

Base on the points we chose before, we get the data from original datasets.

Before run this part, you have to download the original datasets and finish the points choosing.
"""



m = 4
days = 18
point = 'ch_point.csv'
out = 'PeMSD3_V_228_Avg_speed.csv'
out_flow = 'PeMSD3_V_228_Total_flow.csv'

df_p = pd.read_csv(point, header=None)
time_step = []
num = []
total_flow = []
avg_speed = []

for d in range(days):
    out1 = f'{m}_{d}days_avgspeed.csv'
    out2 = f'{m}_{d}days_totalflow.csv'
    if d < 9:
        in_data_file = f'd03_text_station_5min_2020_0{m}_0{d + 1}.csv'
    else:
        in_data_file = f'd03_text_station_5min_2020_0{m}_{d + 1}.csv'
    df_n = pd.read_csv(in_data_file, header=None)
    df_rows = len(df_n)
    for j in range(228):
        point_n = df_p.iloc[0, j]
        for i in range(df_rows):
            if df_n.iloc[i, 1] == point_n:
                total_flow.append(df_n.iloc[i, 9])
                avg_speed.append(df_n.iloc[i, 11])
        with open(out1, "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(avg_speed)
            csv_file.close()
        with open(out2, "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(total_flow)
            csv_file.close()
        total_flow = []
        avg_speed = []
        print(point_n)
    print(m, ".", d + 1, "is done.")

for d in range(days):
    out1 = f'{m}_{d}days_avgspeed.csv'
    out2 = f'{m}_{d}days_totalflow.csv'
    df_tran = pd.read_csv(out2, header=None)
    df_tran.values
    data = df_tran.iloc[:, :].values
    data = list(map(list, zip(*data)))
    data = pd.DataFrame(data)
    data.to_csv(out_flow, mode='a', header=0, index=0)
    print(m, ".", d + 1, "is done.")
