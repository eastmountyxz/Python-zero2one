# -*- coding: utf-8 -*-
#By:Eastmount CSDN
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.random.normal(5.0, 3.0, 1000)  # mean=5.0 rms=3.0
pData = pd.DataFrame(data)
print(pData)
print(type(pData))
p1 = pData.hist(histtype='stepfilled',bins=30,normed=True)
plt.show() 
