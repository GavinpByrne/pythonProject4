import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r'C:\Users\Stackedadmin\Desktop\Python\Property_Price_Register_Ireland-28-05-2021.csv')
# print(df.head())
# print(df.shape)
# print(df.info)
print(df.columns)
# print(df.describe())
# df['COUNTY'].value_counts().plot(kind='bar')
# plt.title('No of Registrations Per County')
# plt.xlabel('County')
# plt.ylabel('No OF Houses')
# plt.show()

plt.scatter(df['COUNTY'], df['SALE_PRICE'])
plt.xticks(rotation=45)
plt.show()



