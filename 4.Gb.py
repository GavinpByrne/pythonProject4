import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\Stackedadmin\Desktop\Flash_test_pandas.csv", encoding='iso8859_2')#would not work without encoding possibly due to Euro signs
# print(df.head())
# print(df.info())
# print (df.describe())
# print (df.values)
# print(df.columns)
# print(df.index)
# print(df.sort_values(['Colour_Cost', 'Mono_Cost'], ascending=[False, True]))
# print(df[['Colour_Cost', 'Mono_Cost']])
# cols_to_check = df[['Colour_Cost', 'Mono_Cost']]
# print(cols_to_check)  # using variable to subset
# print(df['Colour_Usage'] > 50)
# print(df[df['Colour_Usage'] > 50])
# print(df[df['code'] == 'FLOMPS002'])
# abcplus3 = df[(df['code'] == '3DENMPS001') | (df['code'] == 'ABCMPS001')]  # | is or operator and & is and operator
# print(abcplus3.head())
#df['Colour_Cost'] = df.astype({'Colour_Cost':float})
#print(df.info)
#print(df['Colour_Cost']*1.04)
df['Colour_Cost'] = df['Colour_Cost']*1.04#just increases amount bu 1.04
df['Colour_Cost_Increase'] = df['Colour_Cost']*1.15#adds column with new amount
print(df.head())


