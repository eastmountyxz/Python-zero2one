# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
from sklearn import linear_model     #导入线性模型
import matplotlib.pyplot as plt       
import numpy as np

#X表示企业成本 Y表示企业利润
X = [[400], [450], [486], [500], [510], [525], [540], [549], [558], [590], [610], [640], [680], [750], [900]]
Y = [[80], [89], [92], [102], [121], [160], [180], [189], [199], [203], [247], [250], [259], [289], [356]]
print('数据集X: ', X)
print('数据集Y: ', Y)

#回归训练
clf = linear_model.LinearRegression() 
clf.fit(X, Y)

#预测结果
X2 = [[400], [750], [950]]
Y2 = clf.predict(X2)
print(Y2)
res = clf.predict(np.array([1200]).reshape(-1, 1))[0]   
print('预测成本1200元的利润：$%.1f' % res) 

#绘制线性回归图形
plt.plot(X, Y, 'ks')                 #绘制训练数据集散点图
plt.plot(X2, Y2, 'g-')               #绘制预测数据集直线
plt.show()

print('系数', clf.coef_)
print('截距', clf.intercept_)
print('评分函数', clf.score(X, Y))

'''
系数 [[ 0.62402912]]
截距 [-173.70433885]
评分函数 0.911831188777
'''
