#Author's Name - Simranjit Kaur
#Creation Date - October 31, 2021
#Last Modified Date - November 14, 2021



#Libraries imported
#pandas - for reading data from csv file
import pandas as pd

#numpy - for mathematical and logical operations
import numpy as np

#sklearn - for implementing ANOVA by using SelectKBest and f_classif objects
from sklearn.feature_selection import SelectKBest, f_classif 




#dataset
#Read data from csv file
datafile = pd.read_csv("filepath.../BIO_dataset.csv", header=0, index_col=0) 

#Transpose the data
data=np.transpose(datafile)

#to get the column names
column_names = list(data.columns) 




#features and target
#put all 5477 features in X from the csv file
X = data[0:5477]

#1 used for first plant samples, 2 used for 2nd plant samples
y = [1,1,1,1,1,2,2,2,2,2,2] 




#ANOVA Implementation
#Create SelectKBest object to select features with best 50 ANOVA F-Values
fvalue_selector = SelectKBest(f_classif, k=50)

#Apply the SelectKBest object to the features and target
X_kbest = fvalue_selector.fit_transform(X, y)

#get the p-values of selected features
valuesP = fvalue_selector.pvalues_ 

#get the names of best selected features
best_feature_names = list(X.columns[fvalue_selector.get_support(indices=True)]) 
print(best_feature_names)

#get the p-values of best selected feature scores
best_feature_valuesP = list(valuesP[fvalue_selector.get_support(indices=True)]) 
print(best_feature_valuesP)

# For saving both p-values and OTUs in a csv file
pd.DataFrame(best_feature_valuesP, best_feature_names).to_csv("filepath.../output_ANOVA_50_OTU_with_P_values.csv")
