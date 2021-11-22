import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\Stackedadmin\Desktop\Python\Flash01.csv', encoding='ISO-8859-1')

df.loc[df['Mono_Charge'] < 0, 'Drop_Below_Zero'] = 0
df.loc[df['Mono_Charge'] > 0, 'Drop_Below_Zero'] = df[
    'Mono_Charge']  # Basically like a IF statement-Creates new column taking out <0
print(df.head())
df['Mono_Charge'].sum() / 15 * 21 + (df['Colour_Charge'].sum() / 15 * 21)

# df.loc[:, 'Row_Total'] = df.sum(numeric_only=True, axis=1)#Creates New Column with row total
# df.loc['Colum_Total'] = df.sum(numeric_only=True,axis=0)#CReates new Column with Column Total
df.loc['FLash_Figure'] = df['Mono_Charge'].sum() / 15 * 21 + (df['Colour_Charge'].sum() / 15 * 21)
print(df.tail())
# df.to_csv(r'C:\Users\Stackedadmin\Desktop\Python\Amended_File.csv')
# print(df.info())
print(df.groupby('code')['Colour_Charge'].agg([np.mean, np.max]))
print(df.pivot_table(values='code', index='Colour_Charge', columns='NAME', aggfunc=np.median))
