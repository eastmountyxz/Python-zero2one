# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-06
# 该部分参考知乎萌弟老师：https://zhuanlan.zhihu.com/p/173945775
import numpy as np
from sklearn import metrics
from sklearn import datasets
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

#------------------------------------------------------------------------
#第一步 导入数据
iris = datasets.load_iris()
X = iris.data[:,[2,3]]
y = iris.target
print("Class labels:",np.unique(y))  #打印分类类别的种类 [0 1 2]
 
#30%测试数据 70%训练数据 stratify=y表示训练数据和测试数据具有相同的类别比例
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1,stratify=y)

#------------------------------------------------------------------------
#第二步 数据标准化
sc = StandardScaler()      #估算训练数据中的mu和sigma
sc.fit(X_train)            #使用训练数据中的mu和sigma对数据进行标准化
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
print(X_train_std)
print(X_test_std)

#------------------------------------------------------------------------
#第三步 可视化函数 画出决策边界
def plot_decision_region(X,y,classifier,resolution=0.02):
    markers = ('s','x','o','^','v')
    colors = ('red','blue','lightgreen','gray','cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    
    # plot the decision surface
    x1_min,x1_max = X[:,0].min()-1,X[:,0].max()+1
    x2_min,x2_max = X[:,1].min()-1,X[:,1].max()+1
    xx1,xx2 = np.meshgrid(np.arange(x1_min,x1_max,resolution),
                         np.arange(x2_min,x2_max,resolution))
    Z = classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1,xx2,Z,alpha=0.3,cmap=cmap)
    plt.xlim(xx1.min(),xx1.max())
    plt.ylim(xx2.min(),xx2.max())
    
    # plot class samples
    for idx,cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl,0],
                   y = X[y==cl,1],
                   alpha=0.8,
                   c=colors[idx],
                   marker = markers[idx],
                   label=cl,
                   edgecolors='black')

#------------------------------------------------------------------------
#第四步 决策树分类
from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier(criterion='gini',max_depth=4,random_state=1)
tree.fit(X_train_std,y_train)
print(X_train_std.shape, X_test_std.shape, len(y_train), len(y_test)) #(105, 2) (45, 2) 105 45
res1 = tree.predict(X_test_std)
print(res1)
print(metrics.classification_report(y_test, res1, digits=4)) #四位小数

plot_decision_region(X_train_std,y_train,classifier=tree,resolution=0.02)
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.title('DecisionTreeClassifier')
plt.legend(loc='upper left')
plt.show()

#------------------------------------------------------------------------
#第五步 KNN分类
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=2,p=2,metric="minkowski")
knn.fit(X_train_std,y_train)
res2 = knn.predict(X_test_std)
print(res2)
print(metrics.classification_report(y_test, res2, digits=4)) #四位小数

plot_decision_region(X_train_std,y_train,classifier=knn,resolution=0.02)
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.title('KNeighborsClassifier')
plt.legend(loc='upper left')
plt.show()
        
#------------------------------------------------------------------------
#第六步 SVM分类 核函数对非线性分类问题建模(gamma=0.20)
from sklearn.svm import SVC
svm = SVC(kernel='rbf',random_state=1,gamma=0.20,C=1.0) #较小的gamma有较松的决策边界
svm = SVC(kernel='rbf',random_state=1,gamma=100.0,C=1.0,verbose=1)
svm.fit(X_train_std,y_train)
res3 = svm.predict(X_test_std)
print(res3)
print(metrics.classification_report(y_test, res3, digits=4))

plot_decision_region(X_train_std,y_train,classifier=svm,resolution=0.02)
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.title('SVM')
plt.legend(loc='upper left')
plt.show()


#------------------------------------------------------------------------
#第七步 逻辑回归分类
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=100.0,random_state=1)
lr.fit(X_train_std,y_train)
res4 = lr.predict(X_test_std)
print(res4)
print(metrics.classification_report(y_test, res4, digits=4))

plot_decision_region(X_train_std,y_train,classifier=lr,resolution=0.02)
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.title('LogisticRegression')
plt.legend(loc='upper left')
plt.show()


#------------------------------------------------------------------------
#第八步 朴素贝叶斯分类
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train_std,y_train)
res5 = gnb.predict(X_test_std)
print(res5)
print(metrics.classification_report(y_test, res5, digits=4))

plot_decision_region(X_train_std,y_train,classifier=gnb,resolution=0.02)
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.title('GaussianNB')
plt.legend(loc='upper left')
plt.show()

#------------------------------------------------------------------------
#第九步 随机森林分类
from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(criterion='gini',
                                n_estimators=25,
                                random_state=1,
                                n_jobs=2,
                                verbose=1)
forest.fit(X_train_std,y_train)
res6 = gnb.predict(X_test_std)
print(res6)
print(metrics.classification_report(y_test, res6, digits=4))

plot_decision_region(X_train_std,y_train,classifier=forest,resolution=0.02)
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.title('RandomForestClassifier')
plt.legend(loc='upper left')
plt.show()

#------------------------------------------------------------------------
#第十步 集成学习分类
from sklearn.ensemble import AdaBoostClassifier
ada = AdaBoostClassifier()
ada.fit(X_train_std,y_train)
res7 = ada.predict(X_test_std)
print(res7)
print(metrics.classification_report(y_test, res7, digits=4))

plot_decision_region(X_train_std,y_train,classifier=forest,resolution=0.02)
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.title('AdaBoostClassifier')
plt.legend(loc='upper left')
plt.show()

#------------------------------------------------------------------------
#第11步 GradientBoosting分类
from sklearn.ensemble import GradientBoostingClassifier
gb = GradientBoostingClassifier()
ada.fit(X_train_std,y_train)
res8 = ada.predict(X_test_std)
print(res8)
print(metrics.classification_report(y_test, res8, digits=4))

plot_decision_region(X_train_std,y_train,classifier=forest,resolution=0.02)
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.title('GradientBoostingClassifier')
plt.legend(loc='upper left')
plt.show()
