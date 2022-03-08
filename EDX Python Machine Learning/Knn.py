from calendar import c
from matplotlib import markers, pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix
from pandas import plotting
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import scipy as sp
 
iris_data = load_iris()

X_train , X_test , y_train , y_test = train_test_split(iris_data['data'] , iris_data['target'] , random_state=0)

iris_dataframe = pd.DataFrame(X_train , columns=iris_data.feature_names)

pd.plotting.scatter_matrix(iris_dataframe , c= y_train , figsize=(15 ,15) , marker= 'o')

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train , y_train)
X_new = np.array([[7 , 0.1 , 0.9 , 10]])
prediction = knn.predict(X_new)

flower = iris_data['target_names'][prediction]
for item in flower:
    print(item)
accuracy = knn.score(X_test , y_test)

print(accuracy)