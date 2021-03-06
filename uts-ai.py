# -*- coding: utf-8 -*-
"""Visualisasi Dataset Pengunjung Mall.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TvUEUfV03-TxqwnZ4NMTrVPX_40F1EeS
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('mall_customers.csv')
df

df.head

df.dtypes

df.tail(5)

plt.figure(figsize=(12,8))
x = df.sort_values(by='Age')['Gender'].tail(5)
y = df.sort_values(by='Gender')['Age'].tail(5)
plt.bar(x,y)
plt.grid()
plt.title('Rata Rata Umur dan Jenis Kelamin Pengunjung Mall')