# Author's Name - Simranjit Kaur
# creation Data - October 10, 2021

# Used Pandas library to read the data from CSV file. Used pingouin Llibrary
# to set up the model for ANOVA. It gives the p-value 9.82 * 10 raise to power
# of -18 which shows that there is at least one group of samples that is different.
# so, to find which group is actually different, post hoc test was performed. 
# The post hoc test gives the probability value for each pair of samples. Based
# on that the best features were selcted.

# After getting feedback from the Client, I realized that we need to find the
# best OTU samples, not the plant samples.

# All in all, this library and model works, but the client wanted something else.


import pandas as pd
df=pd.read_csv("file path... /BIO_dataset.csv")
df_melt = pd.melt(df.reset_index(), id_vars=['Samples'], value_vars=['Brassica_1', 'Brassica_2', 'Brassica_3', 'Brassica_4', 'Brassica_5', 'Wheat_1', 'Wheat_2', 'Wheat_3', 'Wheat_4', 'Wheat_5', 'Wheat_6'])
df_melt.columns = ['Samples', 'Crops', 'Microbiome']
df_melt.head(5)


import pingouin as pg
res = pg.rm_anova(dv='Microbiome', within='Crops', subject='Samples', data=df_melt, detailed=True)
res
post_hocs = pg.pairwise_ttests(dv='Microbiome', within='Crops', subject='Samples', padjust='fdr_bh', data=df_melt)
post_hocs
import pingouin as pg
pg.sphericity(data=df_melt, dv='Microbiome', subject='Samples', within='Crops')[-1]
pg.normality(data=df_melt, dv='Microbiome', group='Crops')
