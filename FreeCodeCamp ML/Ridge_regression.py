from statistics import LinearRegression, linear_regression
import mglearn
from sklearn.model_selection import train_test_split
X, y = mglearn.datasets.load_extended_boston()
X_train , y_train, X_test, y_test = train_test_split(X , y , random_state=0)
lin = LinearRegression(X_train, y_train)

print(lin.score(X_train, y_train))