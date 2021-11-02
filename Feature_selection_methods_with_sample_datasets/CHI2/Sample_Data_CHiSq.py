import pandas as pd
from scipy.stats import chi2_contingency

# defining the table
data = [[207, 282, 241], [258, 242, 299],[207, 282, 241],[207, 182, 241]]
stat, p, dof, expected = chi2_contingency(data)

print(stat, p, dof, expected)
# interpret p-value
alpha = 0.05
print("p value is " + str(p))
if p <= alpha:
    print('Dependent (reject H0)')
else:
    print('Independent (H0 holds true)')




