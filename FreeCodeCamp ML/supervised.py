import mglearn
import mglearn
from sklearn import neighbors
from sklearn.model_selection import train_test_split
X , y = mglearn.datasets.make_forge()
X_train , X_test, y_train, y_test = train_test_split(X, y, random_state=0)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))