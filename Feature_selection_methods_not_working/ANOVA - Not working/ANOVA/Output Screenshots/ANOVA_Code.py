# Author's Name - Simranjit Kaur
# Creation Date: October 17, 2021

# Used Pandas library to read the data and Pingouin Library to set up the Model
# for ANOVA. It was working, but the probabilty values this code gave were not
# accurate as I was getting a warning that the values might not be accurate as
# the csv file has more that 5000 enteries. So, We decided to split the data
# in two files and then apply the model. 

import pandas as pd
df = pd.read_csv("D:/School/FALL 2021/COMP 4910/Dataset/First_5000_enteries.csv")
df_melt = pd.melt(df.reset_index(), id_vars=['Samples'], value_vars=['Brassica_1', 'Brassica_2', 'Brassica_3', 'Brassica_4', 'Brassica_5', 'Wheat_1', 'Wheat_2', 'Wheat_3', 'Wheat_4', 'Wheat_5', 'Wheat_6'])
df_melt.columns = ['Samples', 'Crops', 'Microbiome']
df_melt.head(5)

import pingouin as pg
res = pg.rm_anova(dv='Microbiome', within='Crops', subject='Samples', data=df_melt, detailed=True)
res

post_hocs = pg.pairwise_ttests(dv='Microbiome', within='Crops', subject='Samples', padjust='fdr_bh', data=df_melt)
post_hocs
