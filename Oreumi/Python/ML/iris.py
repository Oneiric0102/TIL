from sklearn.datasets import load_iris
import pandas as pd
import mglearn
import numpy as np

iris_dataset = load_iris()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)

iris_dataframe=pd.DataFrame(X_train, columns=iris_dataset.feature_names)
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)


from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train)

X_new = np.array([[4.3, 2.9, 0.7, 0.2]])
prediction = model.predict(X_new)
print(f"예측: {prediction}")
print(f"예측한 타깃의 이름: {iris_dataset['target_names'][prediction]}")

y_p = model.predict(X_test)
print(f"테스트 세트에 대한 예측값: {y_p}")
print(f"테스트 세트에 대한 실제값: {y_test}")
print("테스트 세트의 정확도: {:.2f}".format(np.mean(y_p == y_test)))
print("테스트 세트의 정확도: {:.2f}".format(model.score(X_test, y_test)))