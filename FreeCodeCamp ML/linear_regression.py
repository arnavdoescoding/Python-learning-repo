import mglearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
X, y = mglearn.datasets.make_wave(n_samples=50)
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=42)
lin = LinearRegression()
lin.fit(X_train, y_train)
#print(lin.coef_, lin.intercept_)
print(lin.score(X_test, y_test), lin.score(X_test, y_test))