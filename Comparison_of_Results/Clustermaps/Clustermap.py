import seaborn as sns  # data visualization library
import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import time



data = pd.read_csv('data.csv') # read original dataset


print("Original Data:\n")

print()
OTUs_data = pd.read_csv('C:/Users/sam_bedu-annan/OneDrive - TransCanada Corporation/Desktop/CSResearchProject/Feature_selection_methods_working/Results/SVM/SVM_Results_200.csv') # read OTUs for each feature selection method
x = data[list(OTUs_data.OTUs)] # get selected OTUs value from original dataset
data_class = data.Samples # get 11 samples from original dataset
print(x)
x = pd.concat([x,data_class], axis=1)  # combine dataframe of samples with data frame of OTUs and their values

x = x.set_index('Samples') # change the combined dataframe's index to values of the Samples i.e Wheat_1, Wheat_2, Brassica_2, e.t.c

x = np.transpose(x) # tranpose the data to have the OTUs' names as the new index and sample names as the new columns
print(x)



"""
Cluster Map
"""
sns.clustermap(x, cmap="vlag") #create cluster map of the tranposed dataset
plt.show()

