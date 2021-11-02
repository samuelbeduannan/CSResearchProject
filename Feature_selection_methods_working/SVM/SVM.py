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
from sklearn.feature_selection import RFE

from sklearn.feature_selection import SelectFromModel


data = pd.read_csv('data.csv')

print(data.describe())

print()
# feature names as a list
col = data.columns       # .columns gives columns names in data
print(col)

print()

# y includes our labels and x includes our features
y = data.sample_class                          # M or B
list = ['Samples', 'sample_class'] # This will be dropped because they are not features
x = data.drop(list,axis = 1 )


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
clf = SVC(kernel = 'linear', max_iter=100000)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

print("Y Test: ", y_test, "Y Pred: ", y_pred)
ac = accuracy_score(y_test,y_pred)
print("Accuracy is: ", ac)


cols = X_train.columns
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_train = pd.DataFrame(X_train, columns=[cols])
X_test = pd.DataFrame(X_test, columns=[cols])
X_train.describe()

# we use Recursive Feature Elimination method with cross-validation to find
# the best features which will be ranked by the cross-validation score
rfecv = RFECV(estimator=clf, step=1, min_features_to_select=50, cv=2, scoring='accuracy')
rfecv = rfecv.fit(X_train, y_train)
accuracy = rfecv.score(X_train, y_train)
n = 50 # select top 50 features
feature_ranks = rfecv.ranking_
feature_ranks_with_idx = enumerate(feature_ranks)
sorted_ranks_with_idx = sorted(feature_ranks_with_idx, key=lambda m: m[1])
top_n_idx = [idx for idx, rnk in sorted_ranks_with_idx[:n]]
# print(top_n_idx)
top_n_features = X_train.columns[top_n_idx]
scores = rfecv.grid_scores_[top_n_idx]
print("Best features : ", top_n_features)
print('Each feature score\n', scores)
print('Accuracy RFECV: ', accuracy)

# Plot number of features VS. cross-validation scores (plot gives which number of features has highest classification
# accuracy)

# plt.figure()
# plt.xlabel("Number of features selected")
# plt.ylabel("Cross validation score of number of selected features")
# plt.plot(range(1, len(rfecv.grid_scores_[top_n_idx]) + 1), rfecv.grid_scores_[top_n_idx])
# print(plt.show())
