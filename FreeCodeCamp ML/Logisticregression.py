from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
cancer = load_breast_cancer()
X_train, y_train , X_test, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=0)
log_reg = LogisticRegression().fit(X_train, y_train)

print(log_reg.score(X_train, y_train))
print(log_reg.score(X_test, y_test))