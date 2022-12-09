import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Mumbai")
print(response)


#for verfication
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Mumbai")
print(response.status_code)



import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Mumbai")
# print(response.status_code)
soup = BeautifulSoup(response.content,"html.parser")
print(soup)
print(soup.prettify)


#to find something
# find('a')
# find_all('div/img')
# find_parent("a")
#find_next_sibling("a")

card = soup.find("div",attrs={"class":"mb-srp__card__container"})
print(card)
price = card.find("div",attrs={"class":"mb-srp__card__price--amount"})
print(price)

