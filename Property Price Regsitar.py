import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
# from bs4 import BeautifulSoup
#
df=pd.read_csv(r'C:\Users\Stackedadmin\Desktop\Python\Property_Price_Register_Ireland-28-05-2021.csv')
# # # print(df.head())
# # # print(df.shape)
# # # print(df.info)
# # print(df.columns)
# # # print(df.describe())
# # # df['COUNTY'].value_counts().plot(kind='bar')# Get count of sales by county
# # # plt.title('No of Registrations Per County')
# # # plt.xlabel('County')
# # # plt.ylabel('No Of Houses')
# # # plt.show()
# #
# # # plt.scatter(df['COUNTY'], df['SALE_PRICE'])Loko at sale price by county
# # # plt.xticks(rotation=45)
# # # plt.show()
# #
# # PP = df[(df['COUNTY'] == 'Dublin') & (df['SALE_DATE'] > '20190101')]#Improve this A way of filtering date and county
# #Look at function
# # PP.to_csv(r'C:\Users\Stackedadmin\Desktop\Python\2020c.csv')
# # df = pd.read_csv(r'C:\Users\Stackedadmin\Desktop\Python\Property_Price_Register_Ireland-28-05-2021.csv', index_col=0)
# #setting index_col to zero in this case enables us to slice between dates
# # fig, ax = plt.subplots(2,1)
# # twenty20 = df['2019-01-01':'2020-01-01']
# # print(twenty20.columns)
# # print (twenty20.tail())
# # # ax.plot(twenty20.index)
# # # plt.show()
# uni = requests.get('http://universities.hipolabs.com/search?country=ireland')# going to compare house prices to PLaces with university
# uni2 = pd.DataFrame(uni.json())
# print(uni2['name'])
# # url = 'https://www.gov.ie/en/service/colleges-and-universities-in-ireland/'
# # r = requests.get(url)
# # text = r.text
# # soup = BeautifulSoup(text)
# # text_college = soup.getText()
# # print(text_college)
# # pretty_soup = BeautifulSoup.prettify(soup)
# # print(pretty_soup)
# college_dict={"Dublin City Unniversity":"Dublin", "National Unniversity of Ireland":"Galway",
#               "Maynooth Unniversity":"Kildare"}
#
# # for key,value  in college_dict.items():
# #     print(key,value)
# college_items=college_dict.items()
# college_list = list(college_items)
# college_df = pd.DataFrame(college_list)
# #print(college_df)
# print(college_df.columns)
# print(uni2.columns)
# county = college_df.merge(uni2,on='name',how='left')
#idea is to use API to get college of Ireland-Webscrape Locations of those college sand then
# create Dict with name and location- Then craete DIct into Dataframe and merge that with API DF so we can see what
#counties have colleges. then merge that with house price data to see house prices with Universities verses not.
#print(df['COUNTY'].value_counts())
avg_county = df.groupby('COUNTY')['SALE_PRICE'].mean()
print(avg_county)
















