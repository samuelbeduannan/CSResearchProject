#Author's Name - Simranjit Kaur
#Creation Date - October 20, 2021
#Last Modified Date - October 24, 2021



#Libraries imported
import pandas as pd #pandas - for reading data from csv file
import numpy as np #numpy - for mathematical and logical operations
from sklearn.feature_selection import SelectKBest, f_classif #sklearn - for implementing ANOVA by using SelectKBest and f_classif objects



#dataset
datafile = pd.read_csv("file path.../BIO_dataset.csv", header=0, index_col=0) #Read data from csv file
data=np.transpose(datafile) #Transpose the data
column_names = list(data.columns) # to get the column names
print(column_names) #print column names
print(data) #print all the data of the file
print(data.describe()) #print the data samples with their count, mean, standard deviation etc.



#features and target
X = data[0:5477] #put all 5477 features in X from the csv file
y = [1,1,1,1,1,2,2,2,2,2,2] #1 used for first plant samples, 2 used for 2nd plant samples
print(X) # print all features
print(y) # print the target



#ANOVA Implementation

fvalue_selector = SelectKBest(f_classif, k=50)#Create SelectKBest object to select features with best 50 ANOVA F-Values
print(X.shape) #print the shape of the data


X_kbest = fvalue_selector.fit_transform(X, y)#Apply the SelectKBest object to the features and target
print(fvalue_selector.get_support(indices=True)) #print the best feature values


print('Total number of features:', X.shape[1]) #print the total number of features
print('Selected number of features:', X_kbest.shape[1]) #print the selected number of features
print(X_kbest[0:11]) #print best 50 feature values for 11 samples
print(X_kbest.shape) #print shape of the best features
print(type(X_kbest)) #print type of best features 


df = pd.DataFrame(X_kbest) #convert X_kbest to a dataframe
print(df) #print the dataframe


scores = fvalue_selector.scores_ #get the scores for all features
print(scores) #print all the scores

print(scores[X_kbest]) #print the scores of best features

df1 = pd.DataFrame(scores[X_kbest]) #convert the best scores to dataframe
print(df1) #print the dataframe of scores of best features


best_feature_scores = list(scores[fvalue_selector.get_support(indices=True)]) #get the scores of best selected features
print(best_feature_scores) #print scores of best selected features


best_feature_names = list(X.columns[fvalue_selector.get_support(indices=True)]) #get the names of best selected features
print(best_feature_names) #print names of best selected features

