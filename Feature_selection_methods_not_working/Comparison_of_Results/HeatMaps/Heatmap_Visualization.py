import seaborn as sns  # data visualization library
import matplotlib.pyplot as plt
import pandas as pd
import time


data = pd.read_csv('data.csv')  #Read dataset
print("Original Data:\n")
print()
OTUs_data = pd.read_csv('filepath../output_ANOVA_50.csv')
x = data[list(OTUs_data.OTUs)] # get selected OTUs value from original dataset
print(x)



"""
Heat Map
"""
f, ax = plt.subplots(figsize=(20, 20)) # create a diagram of dimension 20 by 20
sns.heatmap(x.corr(), annot=True, linewidths=.5, fmt='.1f', ax=ax) #plot a heatmap of the correlated dataset with data labels of size .1f and heatmap cell size of .5


"""
Swarmplot
"""
y = data.sample_class # get the classes of the sample from data
sns.set(style="whitegrid", palette="muted") # define the theme of the swarm plot
data_class = y
data = x
data = pd.concat([y,x.iloc[:,0:10]],axis=1) # combine the sample class dataset with the values of the OTUs into one dataframe
data = pd.melt(data,id_vars="sample_class",
                    var_name="features",
                    value_name='value') #transform the data to have sample_class as the identifier and set x axis label as "features"
plt.figure(figsize=(10,10)) # define the dimensions of the swarmplot
tic = time.time()
sns.swarmplot(x="features", y="value", hue="sample_class", data=data) # construct swarmplot with x as features, colors as the sample_class and data value from the original dataset

plt.xticks(rotation=90)

plt.show()