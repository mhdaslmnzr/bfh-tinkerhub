
from requests import get
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os 
import time
from re import search

# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_argument('--headless')
# options.add_argument('log-level=3')


# driver = webdriver.Chrome(options = options)
# #urls: https://wallpapercave.com/mammootty-wallpapers
#https://wallpapercave.com/mammootty-hd-wallpapers
#https://adhil369.weebly.com/mammookka-gallery-old-images.html
#https://www.99images.com/celebrities/mammootty


url = 'https://www.99images.com/celebrities/mammootty'

# driver.get(url)
# j=232
# r = requests.get(url ,stream=True)
# sp = BeautifulSoup(r.content, 'html.parser')

#print(len(sp.find_all('img')))
#


# for item in sp.find_all('img'):
#     try :print(item['src'])
#     except : pass

#     if search('/uploads/1/',item['src']):

#         f2 = open("mamoot/{}.jpg".format(j),"wb")
#         img = requests.get('https://www.99images.com/celebrities/mammootty'+item['src'])
#         f2.write(img.content)
#         j+=1
#                     #url_list.add(item['src'])








j = 248

for x in range(2,7):
    url2 = 'https://www.99images.com/celebrities/mammootty?page='+str(x)
    
    
    r = requests.get(url2 ,stream=True)
    sp = BeautifulSoup(r.content, 'html.parser')
    for item in sp.find_all('img'):
        try :
            print(item['data-pin-media'])
            f2 = open("mamoot/{}.jpg".format(j),"wb")
            img = requests.get(item['data-pin-media'])
            f2.write(img.content)
            j+=1

        except:
            pass

    