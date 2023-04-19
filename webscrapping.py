import requests
from bs4 import BeautifulSoup 
import pandas as pd
import numpy as np

def get_price(soup):
  try:
    product_price = single_product_soup.find('span', attrs={'class':'a-offscreen'}).text
  except:
    product_price = ""
  return product_price

def get_title(soup):
  try:
    product_title = single_product_soup.find('span', attrs={'id':'productTitle'}).text.strip()
  except:
    product_title = ""
  return product_title

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', 'Accept-Language':'en-US, en;q=0.5'})
URL = "https://www.amazon.com/s?k=ear+buds&crid=8E82VVFVPGTB&sprefix=ear+buds%2Caps%2C1100&ref=nb_sb_noss_1"

page = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(page.content, 'html.parser')

links = soup.find_all('a', attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

links_list = []

#loop execute
for link in links:
  links_list.append("https://www.amazon.com" + link.get("href"))

d = {"Title":[], "Price":[]}
for link in links_list:
  product_page = requests.get(link, headers=HEADERS)
  single_product_soup = BeautifulSoup(product_page.content, 'html.parser')

  d['Title'].append(get_title(single_product_soup))
  d['Price'].append(get_price(single_product_soup))

amazon_data_frame = pd.DataFrame.from_dict(d)
amazon_data_frame['Title'].replace('', np.nan, inplace=True)
amazon_data_frame=amazon_data_frame.dropna(subset=['Title'])
amazon_data_frame.to_csv("Amazona_Data.csv",header=True,index=False)

amazon_data_frame

# links_list


# link = "https://www.amazon.com" + links[0].get("href")

# product_page = requests.get(link, headers=HEADERS)
# single_product_soup = BeautifulSoup(product_page.content, 'html.parser')

# product_title = single_product_soup.find('span', attrs={'id':'productTitle'}).text.strip()
# product_price = single_product_soup.find('span', attrs={'class':'a-offscreen'}).text

# product_price




