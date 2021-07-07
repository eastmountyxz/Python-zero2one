import numpy as np
from sklearn.svm import SVC

X = np.array([[-1, -1], [-2, -2], [1, 3], [4, 6]])  
y = np.array([1, 1, 2, 2])
clf = SVC()  
clf.fit(X, y)   
print(clf)
print(clf.predict([[-0.8,-1], [2,1]]))

#输出结果：[1, 2]
