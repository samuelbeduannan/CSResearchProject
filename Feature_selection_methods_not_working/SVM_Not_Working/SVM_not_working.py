# Author: Samuel Oliver Bedu-Annan
# Date Created:
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import RFECV
from sklearn.preprocessing import StandardScaler

from sklearn.feature_selection import SelectFromModel

data = pd.read_csv('data.csv')

# print(data.describe())
#
# print()
# feature names as a list
col = data.columns  # .columns gives columns names in data
# print(col)

# print()

# y includes our labels and x includes our features
y = data.sample_class  # M or B
list = ['Samples', 'sample_class']  # This will be dropped because they are not features
x = data.drop(list, axis=1)
# print(x.head())

# print()

# Tried separating Wheat from Brassica
drop_list1 = [5, 6, 7, 8, 9, 10]
x_1 = x.drop(drop_list1, axis=0)  # do not modify x, we will use it later
print(x_1.head(10))

# separating Brassica from Wheat
drop_list2 = [0, 1, 2, 3, 4]
x_2 = x.drop(drop_list2, axis=0)  # do not modify x, we will use it later
print(x_2.head(10))

# Training data samples with Brassica. Failed to work because data had only one class.
# Resolution was to avoid separating Brassica from Wheat so we have at least 2 classes to train dataset
X_train, X_test, y_train, y_test = train_test_split(x_1, y, test_size=0.2)
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Not able to ran because data failed to train
print("Y Test: ", y_test, "Y Pred: ", y_pred)
ac = accuracy_score(y_test, y_pred)
print("Accuracy is: ", ac)

# Not able to ran because data failed to train
# lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(x_1, y)
select_feature = SelectKBest(LinearSVC, k=5).fit(X_train, y_train)
print('Score list:', select_feature.scores_)
print('Feature list:', X_train.columns)

# Not able to ran because data failed to train
cols = X_train.columns
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_train = pd.DataFrame(X_train, columns=[cols])
X_test = pd.DataFrame(X_test, columns=[cols])
# X_train.describe()

# Not able to ran because data failed to train
# Finding the best features with Recursive Feature Elimination method
clf_svc = LinearSVC()
rfecv = RFECV(estimator=clf_svc, step=1, cv=5, scoring='accuracy')
rfecv = rfecv.fit(X_train, y_train)
#
print('Optimal number of features :', rfecv.n_features_)
print('Best features :', X_train.columns[rfecv.support_])

# Not able to ran because data failed to train

# Plot number of features VS. cross-validation scores (plot gives which number of features has highest classification
# accuracy)
plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score of number of selected features")
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
print(plt.show())

# Not able to ran because data failed to train
# selector is a RFECV fitted object
feature_importance = rfecv.estimator_.feature_importances_  # or coef_
feature_importance_sorted = sorted(enumerate(feature_importance), key=lambda x: x[1])
top_n_idx = [idx for idx, _ in feature_importance_sorted[:n]]
print(top_n_idx)

# Not able to ran because data failed to train
print(top_n_features)
print('Optimal number of features :', rfecv.n_features_)
print('Best features :', X_train.columns[rfecv.support_])
print('Each feature score\n', rfecv.grid_scores_)

# Not able to ran because data failed to train
rfe = RFE(estimator=clf, n_features_to_select=50, step=1)
rfe = rfe.fit(X_train, y_train)
print('Optimal number of features :', rfe.n_features_)
print('Best features :', X_train.columns[rfe.support_])

# Not able to ran because data failed to train
# Plot number of features VS. cross-validation scores (plot gives which number of features has highest classification
# accuracy)
plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score of number of selected features")
plt.plot(range(1, len(rfe.cv_results_) + 1), rfe.cv_results_)
print(plt.show())
