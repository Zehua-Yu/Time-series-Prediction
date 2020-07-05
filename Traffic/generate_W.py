# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 10:12 下午
# @Author  : Zehua Yu
# @Email   : 19zhyu@stu.edu.cn
# @File    : generate_W.py
# @Software : PyCharm

import pandas as pd
from statsmodels.tsa.arima_model import ARMA
import csv
import os
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

"""
 Using V，calculate the ARIMA order. Then, calculate the adjacency matrix W(consist of Euclidean distance)
 using order parameters.
 
 You can set the order of diff and ARMA(p,q).
"""

diff = 3
df1 = pd.read_csv(f'PeMSD3_V_228.csv', header=None)
output_pa = f'Covid19_vector_pa_ucc_0607_{diff}diff.csv'
sum_c = 0
for i in range(228):
    timeseries = []
    if i >= 0:
        for j in range(288*44):
            if j <= (288*34):
                timeseries.append(df1.iloc[j, i])
        p = 5
        q = 0
        print(p, q)
        model = ARMA(timeseries, order=(p, q)).fit()
        data_h = model.summary()
        print(data_h)
        B = []
        for k in range(p+q):
            B.append(data_h[k])
        with open(output_pa, "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(B)
            csv_file.close()
        print(i + 1, 'is done.')

output_eucl_ntran = f'Covid19_W_ucc0607_{diff}diff_ntran.csv'
output_eucl = f'Covid19_W_ucc0607_{diff}difflogturn_51.csv'
df4 = pd.read_csv(output_pa, header=None)

df4.values
data = df4.iloc[:, :].values
data = list(map(list, zip(*data)))
data = pd.DataFrame(data)
data.to_csv(output_eucl_ntran, header=0, index=0)
df2 = pd.read_csv(output_eucl_ntran, header=None)
vec = []
A = []
i = 0
j = 0
for i in range(228):
    for j in range(5):
        A.append(complex(df2.iloc[j, i])*10)
    vec.append(1)
    vec[i] = A
    A = []

distA = pdist(vec, metric='euclidean')
distB = squareform(distA)
for a in range(228):
    A = []
    for b in range(228):
        A.append(distB[a, b])
    with open(output_eucl, "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(A)
        csv_file.close()
os.remove(output_eucl_ntran)
os.remove(output_pa)
