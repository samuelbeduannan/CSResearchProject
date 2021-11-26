import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFECV
from sklearn.preprocessing import StandardScaler
import time


start_time = time.time()
data = pd.read_csv('data.csv')

data=np.transpose(data) #Transpose the data
data[5477] = ['sample_class','B','B','B','B','B','W','W','W','W','W','W']
data.columns = data.iloc[0]
data = data.drop(data.index[0])

# feature names as a list
col = data.columns       # .columns gives columns names in data

#
# y includes our labels and x includes our features
y = data.sample_class
list1 = ['sample_class'] # sample_class will be dropped because it is not a feature
x = data.drop(list1,axis = 1 )

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
clf = SVC(kernel = 'linear', max_iter=100000)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
#
ac = accuracy_score(y_test,y_pred)
print("Accuracy is: ", ac)
#
#
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
top_n_features = X_train.columns[top_n_idx].values
print("Best features : ", top_n_features)
print('Accuracy RFECV: ', accuracy)

print("%.10f seconds" %(time.time() - start_time,))

results = list(top_n_features)
# top_n_features.to_csv('SVM_Results_200.csv', encoding='utf-8', index=False)
# pd.DataFrame(results).to_csv('C:/Users/sam_bedu-annan/OneDrive - TransCanada Corporation/Desktop/CSResearchProject/Feature_selection_methods_working/SVM/SVM_Results_200.csv')


