import pandas as pd 
from scipy import stats
data= '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]

column_names = data[0] 
data_rows= data[1::]
df = pd.DataFrame(data_rows,columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

mu_A = df['Alcohol'].mean()
me_A = df['Alcohol'].median()
mo_A = stats.mode(df['Alcohol'])[0][0]
ran_A = max(df['Alcohol']) - min(df['Alcohol'])
std_A = df['Alcohol'].std() 
var_A = df['Alcohol'].var()
 

mu_T = df['Tobacco'].mean()
me_T = df['Tobacco'].median()
mo_T = stats.mode(df["Tobacco"])[0][0]
ran_T = max(df['Tobacco']) - min(df['Tobacco'])
std_T = df['Tobacco'].std()
var_T = df['Tobacco'].var()
print("The mean for the Alcohol and Tobacco dataset are " + str(mu_A) + " and " + str(mu_T))
print("The median for the Alcohol and Tobacco dataset are " + str(me_A) + " and " + str(me_T))
print("The mode for the Alcohol and Tobacco dataset are " + str(mo_A) + " and " + str(mo_T))
print("The range for the Alcohol and Tobacco dataset are " + str(ran_A) + " and " + str(ran_T))
print("The standard deviation for the Alcohol and Tobacco dataset are " + str(std_A) + " and " + str(std_T))
print("The variance for the Alcohol and Tobacco dataset are " + str(var_A) + " and " + str(var_T))
