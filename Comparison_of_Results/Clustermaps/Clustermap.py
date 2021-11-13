import seaborn as sns  # data visualization library
import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import time


data = pd.read_csv('data.csv')


print("Original Data:\n")

print()
OTUs_data = pd.read_csv('/Feature_selection_methods_working/Results/ANOVA/output_ANOVA_50.csv')
x = data[list(OTUs_data.OTUs)]
data_class = data.Samples
print(x)
x = pd.concat([x,data_class], axis=1)

x = x.set_index('Samples')

x = np.transpose(x)
print(x)



"""
Cluster Map
"""
# f, ax = plt.subplots(figsize=(20, 20))
sns.clustermap(x)
# # # sns.heatmap(x.corr(), annot=True)
plt.show()

