# -*- coding: utf-8 -*-
"""Kfold_SVM_Caesar Noor_1207070025

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16YjUH04Lea7XsHmmcQu7M-ofA-NTyPFi
"""

import numpy as np # Mengimpor library numpy berguna untuk kalkulasi data
import pandas as pd # Memanipulasi data dalam bentuk tabel
from matplotlib import pyplot as plt # Visualisasi
import seaborn as sns # Visualisasi lebih mudah

from sklearn.svm import SVC # Mengimpor SVC dari library sklearn folder sub-library svm
from sklearn.datasets import make_classification # Membuat dataset generated
from sklearn.model_selection import KFold, train_test_split # Evaluasi data

X, y = make_classification(n_features = 1, random_state = 0, n_informative = 1, n_redundant = 0, n_clusters_per_class = 1)

sns.scatterplot(x=X.ravel(), y=y)

svc = SVC(kernel = 'linear', random_state = 0)
svc.fit(X, y)

prediction = svc.predict(X)
print(prediction)

sns.scatterplot(x=X.ravel(), y=y, hue=prediction)

svc.predict([[0]])

X = np.array([
    [0],
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]
])
y = np.array([1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1])
sns.scatterplot(x=X.ravel(), y=y)

svc = SVC(kernel = 'poly', degree=2, random_state = 0)
svc.fit(X, y)
prediction = svc.predict(X)

sns.scatterplot(x=X.ravel(), y=y, hue=prediction)
sns.lineplot(x=X.ravel(), y=prediction)
plt.show()

svc = SVC(kernel = 'rbf', random_state = 0)
svc.fit(X, y)
prediction = svc.predict(X)

sns.scatterplot(x=X.ravel(), y=y, hue=prediction)
sns.lineplot(x=X.ravel(), y=prediction)
plt.show()

## GUNAKAN K-FOLD CROSS VALIDATION UNTUK MENGEVALUASI DATA TERSEBUT

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm

X, y = datasets.load_iris(return_X_y=True)
X.shape, y.shape

X_train, X_test, y_train, y_test = train_test_split(
   X, y, test_size=0.4, random_state=0)

X_train.shape, y_train.shape
((90, 4), (90,))
X_test.shape, y_test.shape
((60, 4), (60,))

clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
clf.score(X_test, y_test)

import numpy as np
from sklearn.model_selection import KFold

X = np.array([
    [0],
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]
])
y = np.array([1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1])
kf = KFold(n_splits=2)

for train, test in kf.split(X):
  print("%s %s" % (train, test))

sns.scatterplot(x=X.ravel(), y=y, hue=prediction)
sns.lineplot(x=X.ravel(), y=prediction)
plt.show()