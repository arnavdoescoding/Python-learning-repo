from re import X
from tkinter import Y
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
X , y = mglearn.datasets.load_extended_boston()
X_train , y_train , X_test, y_test = train_test_split(X, y, random_state=0)
lasso = Lasso(alpha=0.1, max_iter=100).fit(X_train, y_train)

lasso.score(X_test, y_test)