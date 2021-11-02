# Author: kanncaa1
# Source: https://www.kaggle.com/kanncaa1/feature-selection-and-data-visualization/log

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns  # data visualization library
import matplotlib.pyplot as plt
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
import time
from subprocess import check_output
from sklearn.svm import SVC

#print(check_output(["ls", "../input"]).decode("utf8"))
# import warnings library
import warnings

# ignore all warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('../Feature_selection_methods_sample_datasets/SVM_Sample/breast_cancer_data.csv')
print(data.head())  # head method show only first 5 rows

# feature names as a list
col = data.columns  # .columns gives columns names in data
print(col)

# y includes our labels and x includes our features
y = data.diagnosis  # M or B
list = ['Unnamed: 32', 'id', 'diagnosis']
x = data.drop(list, axis=1)
print("New x data head: ", x.head())

print(x.describe())  # detailed statistics description of new x data

# Visualization

# first ten features
data_dia = y
data = x
data_n_2 = (data - data.mean()) / (data.std())  # standardization
data = pd.concat([y, data_n_2.iloc[:, 0:10]], axis=1)
data = pd.melt(data, id_vars="diagnosis",
               var_name="features",
               value_name='value')
plt.figure(figsize=(10, 10))
sns.violinplot(x="features", y="value", hue="diagnosis", data=data, split=True, inner="quart")
plt.xticks(rotation=90)

# As an alternative of violin plot, box plot can be used
# box plots are also useful in terms of seeing outliers
# I do not visualize all features with box plot
# In order to show you lets have an example of box plot
# If you want, you can visualize other features as well.
plt.figure(figsize=(10, 10))
sns.boxplot(x="features", y="value", hue="diagnosis", data=data)
plt.xticks(rotation=90)

# Compare two features in detail

sns.jointplot(x.loc[:, 'concavity_worst'], x.loc[:, 'concave points_worst'], kind="reg", color="#ce1414")

# Visualization to compare three or more features
sns.set(style="white")
df = x.loc[:, ['radius_worst', 'perimeter_worst', 'area_worst']]
g = sns.PairGrid(df, diag_sharey=False)
g.map_lower(sns.kdeplot, cmap="Blues_d")
g.map_upper(plt.scatter)
g.map_diag(sns.kdeplot, lw=3)

# feature comparison using swarm plot
sns.set(style="whitegrid", palette="muted")
data_dia = y
data = x
data_n_2 = (data - data.mean()) / (data.std())  # standardization
data = pd.concat([y, data_n_2.iloc[:, 0:10]], axis=1)
data = pd.melt(data, id_vars="diagnosis",
               var_name="features",
               value_name='value')
plt.figure(figsize=(10, 10))
tic = time.time()
sns.swarmplot(x="features", y="value", hue="diagnosis", data=data)

plt.xticks(rotation=90)

# feature comparison using swarm plot for second set of data

data = pd.concat([y, data_n_2.iloc[:, 10:20]], axis=1)
data = pd.melt(data, id_vars="diagnosis",
               var_name="features",
               value_name='value')
plt.figure(figsize=(10, 10))
sns.swarmplot(x="features", y="value", hue="diagnosis", data=data)
plt.xticks(rotation=90)

# correlation map for all features
f, ax = plt.subplots(figsize=(18, 18))
sns.heatmap(x.corr(), annot=True, linewidths=.5, fmt='.1f', ax=ax)

drop_list1 = ['perimeter_mean', 'radius_mean', 'compactness_mean', 'concave points_mean', 'radius_se', 'perimeter_se',
              'radius_worst', 'perimeter_worst', 'compactness_worst', 'concave points_worst', 'compactness_se',
              'concave points_se', 'texture_worst', 'area_worst']
x_1 = x.drop(drop_list1, axis=1)  # do not modify x, we will use it later
x_1.head()

# correlation map after dropping similar features
f, ax = plt.subplots(figsize=(14, 14))
sns.heatmap(x_1.corr(), annot=True, linewidths=.5, fmt='.1f', ax=ax)

from sklearn.model_selection import train_test_split

# split data train 70 % and test 30 %
x_train, x_test, y_train, y_test = train_test_split(x_1, y, test_size=0.3, random_state=42)

from sklearn.feature_selection import RFE

# Create the RFE object and rank each pixel
clf = SVC(kernel='linear')
rfe = RFE(estimator=clf, n_features_to_select=5, step=1)
rfe = rfe.fit(x_train, y_train)
print('Chosen best 5 feature by rfe:', x_train.columns[rfe.support_])

# Select best features with RFECV
from sklearn.feature_selection import RFECV

# The "accuracy" scoring is proportional to the number of correct classifications
rfecv = RFECV(estimator=clf, step=1, cv=5, scoring='accuracy')  # 5-fold cross-validation
rfecv = rfecv.fit(x_train, y_train)

print('Optimal number of features :', rfecv.n_features_)
print('Best features :', x_train.columns[rfecv.support_])

# Plot number of features VS. cross-validation scores
import matplotlib.pyplot as plt

plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score of number of selected features")
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.show()

