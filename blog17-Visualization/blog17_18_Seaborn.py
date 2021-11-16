# -*- coding: utf-8 -*-
#By:Eastmount CSDN
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv",index_col='year')
data = data.corr()
sns.heatmap(data)
plt.show()
