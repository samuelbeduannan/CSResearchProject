

import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, chi2
#from astropy.io import ascii



#load the dataset
tab = pd.read_csv("Dataset.csv", header=0, index_col=0)
table=np.transpose(tab)
Names = list(table.columns)
#print(Names)
#print(table)
#print(table.describe())

# Create features and target
X = table[0:5477]
y = [1,1,1,1,1,2,2,2,2,2,2]
#print(X)
#print(y)


# Create an SelectKBest object to select features with best CHI-SQ F-Values
fvalue_selector = SelectKBest(chi2, k=50)

#print(X.shape)


# Apply the SelectKBest object to the features and target
X_kbest = fvalue_selector.fit_transform(X, y)

X_new = fvalue_selector.transform(X)
#print(fvalue_selector.get_support(indices=True))

# Show results
print('Reduced number of features:', X_kbest.shape[1])
#print(X_kbest[0:11])
#print(X_kbest.shape)
#print(type(X_kbest))

#convert X_kbest to a dataframe.
df = pd.DataFrame(X_kbest)
#print(df)

#get the scores for the selected features
scores = fvalue_selector.scores_
#print(scores)

#Let's get the selected feature names
feature_names = list(X.columns[fvalue_selector.get_support(indices=True)])
print(feature_names)

features = str(feature_names)
