import pandas as pd
datafile = "C:/Users/simra/OneDrive/Desktop/ANOVA_Samples/Sample_3/plantGrowth.csv"

data = pd.read_csv(datafile)

data.head()






#boxplot

data.boxplot('weight', by='group')





grps = pd.unique(data.group.values)
d_data = {grp:data['weight'][data.group == grp] for grp in grps}

k= len(pd.unique(data.group))
N= len(data.values)
n= data.groupby('group').size()[0]




# one-way ANOVA using SciPy
from scipy import stats

f, p = stats.f_oneway(d_data['ctrl'], d_data['trt1'], d_data['trt2'])

f,p
