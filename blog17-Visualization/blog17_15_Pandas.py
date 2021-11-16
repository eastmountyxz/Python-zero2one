# -*- coding: utf-8 -*-
#By:Eastmount CSDN
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv", index_col='year')    
data.plot(kind='bar', stacked=True)
plt.show()
