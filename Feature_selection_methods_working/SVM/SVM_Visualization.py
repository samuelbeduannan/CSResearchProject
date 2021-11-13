import seaborn as sns  # data visualization library
import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import time

iris = sns.load_dataset('iris')
species = iris.pop("species")
print(iris.head())
# sns.clustermap(iris)
# plt.show()
data = pd.read_csv('data.csv')


print("Original Data:\n")
# print(data)

print()
OTUs_data = pd.read_csv('C:/Users/sam_bedu-annan/OneDrive - TransCanada Corporation/Desktop/CSResearchProject/Feature_selection_methods_working/Results/ANOVA/output_ANOVA_50.csv')
# print(data[list(OTUs_data.OTUs)])
x = data[list(OTUs_data.OTUs)]
data_class = data.Samples
print(x)
# print(data_class)
x = pd.concat([x,data_class], axis=1)

x = x.set_index('Samples')

x = np.transpose(x)
print(x)

# x = x.set_index('Samples')

# print(x.index)


"""
Heat Map
"""
# f, ax = plt.subplots(figsize=(20, 20))
sns.clustermap(x)
# # # sns.heatmap(x.corr(), annot=True)
plt.show()

"""
Swarmplot
"""
# y = data.sample_class
# sns.set(style="whitegrid", palette="muted")
# data_class = y
# data = x
# # data_n_2 = (data - data.mean()) / (data.std())              # standardization
# data = pd.concat([y,x.iloc[:,0:10]],axis=1)
# data = pd.melt(data,id_vars="sample_class",
#                     var_name="features",
#                     value_name='value')
# plt.figure(figsize=(10,10))
# tic = time.time()
# sns.swarmplot(x="features", y="value", hue="sample_class", data=data)
#
# plt.xticks(rotation=90)
#
#