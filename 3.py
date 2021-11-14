# to get all hyperlinks in webpage or text from webpage or strings from webpage 'a' represents hyperlinks
import requests
from bs4 import BeautifulSoup

url = 'https://www.stacked.ie/'
r = requests.get(url)
text = r.text
soup = BeautifulSoup(text)
# print(text)
# for link in soup.findAll('a'):
#     print(link.get('href'))
# pretty_soup=BeautifulSoup.prettify(soup)
# print(pretty_soup)
# what_soup=BeautifulSoup.string
# print (what_soup)
stacked_text=soup.getText()
print (stacked_text)
