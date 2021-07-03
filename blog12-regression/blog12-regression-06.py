# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
from sklearn.linear_model import LinearRegression     
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt       
import numpy as np

#X表示企业成本 Y表示企业利润
X = [[400], [450], [486], [500], [510], [525], [540], [549], [558], [590], [610], [640], [680], [750], [900]]
Y = [[80], [89], [92], [102], [121], [160], [180], [189], [199], [203], [247], [250], [259], [289], [356]]
print('数据集X: ', X)
print('数据集Y: ', Y)

#第一步 线性回归分析
clf = LinearRegression() 
clf.fit(X, Y)                     
X2 = [[400], [750], [950]]
Y2 = clf.predict(X2)
print(Y2)
res = clf.predict(np.array([1200]).reshape(-1, 1))[0]   
print('预测成本1200元的利润：$%.1f' % res) 
plt.plot(X, Y, 'ks')    #绘制训练数据集散点图
plt.plot(X2, Y2, 'g-')  #绘制预测数据集直线

#第二步 多项式回归分析
xx = np.linspace(350,950,100) #350到950等差数列
quadratic_featurizer = PolynomialFeatures(degree = 2) #实例化一个二次多项式
x_train_quadratic = quadratic_featurizer.fit_transform(X) #用二次多项式x做变换
X_test_quadratic = quadratic_featurizer.transform(X2)
regressor_quadratic = LinearRegression()
regressor_quadratic.fit(x_train_quadratic, Y)

#把训练好X值的多项式特征实例应用到一系列点上,形成矩阵
xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1))
plt.plot(xx, regressor_quadratic.predict(xx_quadratic), "r--",
         label="$y = ax^2 + bx + c$",linewidth=2)
plt.legend()
plt.show()    
