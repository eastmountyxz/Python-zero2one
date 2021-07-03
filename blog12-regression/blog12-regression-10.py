# -*- coding: utf-8 -*-
# By:Eastmount CSDN 2021-07-03
from sklearn.linear_model import LogisticRegression  #导入逻辑回归模型 
clf = LogisticRegression()
print(clf)
clf.fit(train_feature,label)
predict['label'] = clf.predict(predict_feature)
