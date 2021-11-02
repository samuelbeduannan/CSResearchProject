import pandas as pd
from scipy.spatial import distance_matrix

data = pd.read_csv('data.csv')

# feature names as a list
col = data.columns  # .columns gives columns names in data

# y includes our labels and x includes our features
y = data.sample_class  # M or B
list = ['Samples', 'sample_class']  # This will be dropped because they are not features
x = data.drop(list, axis=1)


# Tried separating Wheat from Brassica
drop_list1 = [5, 6, 7, 8, 9, 10]
x_1 = x.drop(drop_list1, axis=0)  # do not modify x, we will use it later
#print(x_1.head(10))


# separating Brassica from Wheat
drop_list2 = [0, 1, 2, 3, 4]
x_2 = x.drop(drop_list2, axis=0)  # do not modify x, we will use it later
#print(x_2.head(10))

print(x_1.columns)

brassica_average = x_1.mean(axis=0)
wheat_average = x_2.mean(axis=0)

# b_df = pd.DataFrame(data=brassica_average)
brassica_average.reset_index(drop=True, inplace=True)
wheat_average.reset_index(drop=True, inplace=True)
features = x_1.columns.values

features_average = pd.concat([brassica_average, wheat_average], axis=1)
features_average.set_axis(features, axis=0, inplace=True)
features_average.set_axis(['brassica_average', 'wheat_average'], axis=1, inplace=True)

print("\n\nAverage of OTU's in Brassica and Wheat")
print(features_average)

distance_matrix_data = pd.DataFrame(distance_matrix(features_average.values, features_average.values), index=features_average.index, columns=features_average.index)

print("\n\nDistance Matrix Data")
print(distance_matrix_data)

distance_matrix_data.to_csv('out.csv', encoding='utf-8', index=False)