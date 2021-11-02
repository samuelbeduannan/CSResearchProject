#Author - Simranjit Kaur
#Date created - October 14, 2021


# used Pandas to read the data from a csv file with first 5000 enteries.
# I tried to manually enter the names of the Samples in f_oneway ANOVA
# method, but neither gives an error nor any output.
# The problem main problem was in setting up the model, not in the Python Library.

import pandas as pd
df=pd.read_csv("file psth... /First_5000_enteries.csv")
df_melt = pd.melt(df.reset_index(), id_vars=['Samples'], value_vars=['Brassica_1', 'Brassica_2', 'Brassica_3', 'Brassica_4', 'Brassica_5', 'Wheat_1', 'Wheat_2', 'Wheat_3', 'Wheat_4', 'Wheat_5', 'Wheat_6'])
df_melt.columns = ['Samples', 'Crops', 'Microbiome']
df_melt.head(5)


Brassica_1 = df_melt['Microbiome'][df_melt.Crops == 'Brassica_1']
grps = pd.unique(df_melt.Microbiome.values)
d_data = {grp:df_melt['Microbiome'][df_melt.Microbiome == grp] for grp in grps}
k = len(pd.unique(df_melt.Microbiome))  # number of conditions
N = len(df_melt.values)  # conditions times participants
n = df_melt.groupby('Microbiome').size()[0] #Participants in each condition

from scipy import stats
F, p = stats.f_oneway(d_data['Brassica_1'], d_data['Brassica_2'], d_data['Brassica_3'], d_data['Brassica_4'], d_data['Brassica_5'], d_data['Wheat_1'], d_data['Wheat_2'], d_data['Wheat_3'], d_data['Wheat_4'], d_data['Wheat_5'], d_data['Wheat_6'])
print(F, p)
