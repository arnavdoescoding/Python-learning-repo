import mglearn
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
X, y = mglearn.datasets.load_extended_boston()
X_train, y_train, X_test, y_test = train_test_split(X, y, random_state=0)
ridge = Ridge().fit(X_train, y_train)

print(ridge.score(X_train, y_train))