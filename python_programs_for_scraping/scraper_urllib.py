
from requests import get
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os 
import time

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('log-level=3')


driver = webdriver.Chrome(options = options)


url = 'https://www.thecompleteactor.com/mohanlal-image-gallery/mohanlal-movie-gallery'

driver.get(url)
#button = driver.find_element_by_id("show_more")





# while driver.find_element_by_id("result_count").text == 'Showing 1 - 189 of 189 image album':
#     time.sleep(2)
#     button.click()
#     print(driver.find_element_by_id("result_count").text)






iter = 0

#div_count = 1

url_list = {'Start'}
while iter != 189:
    print("length is ",len(url_list))
    xpatb = '/HTML[1]/BODY[1]/DIV[2]/DIV[2]/DIV[2]/DIV[3]/DIV['
    xpatm = ']/DIV['
    xpate = ']/DIV[1]/DIV[1]/A[1]'

    for sec_count in range(1,7):
        if sec_count !=6 :
            print("esc count is ",sec_count)
            for div_count in range(1,37):
                
                final_xpath = xpatb+str(sec_count)+xpatm+str(div_count)+xpate
                try:
                    div = driver.find_element_by_xpath(final_xpath)
                except:
                    print("Tried")
                    but = driver.find_element_by_xpath('/HTML[1]/BODY[1]/DIV[2]/DIV[2]/DIV[3]/DIV[1]/BUTTON[1]')    
                    but.click()
                   # but.click()
                    time.sleep(2)
                    div = driver.find_element_by_xpath(final_xpath)
                #div.click()
                

                
                r = requests.get(div.get_attribute("href"))
                sp = BeautifulSoup(r.content, 'html.parser')
                print(len(url_list))
                for item in sp.find_all('img'):
                    #print(item['src'])
                    url_list.add(item['src'])
                    # f = open("images/{}.jpg".format(iter),"wb")
                    # kk = requests.get(item['src'])

         
                    # f.write(kk.content)
        
                    

                iter+=1
        else:
            for div_count in range(1,10):
                final_xpath = xpatb+str(sec_count)+xpatm+str(div_count)+xpate
                try:
                    div = driver.find_element_by_xpath(final_xpath)
                except:
                    print("Tried")
                    but = driver.find_element_by_xpath('/HTML[1]/BODY[1]/DIV[2]/DIV[2]/DIV[3]/DIV[1]/BUTTON[1]')    
                    but.click()
                   # but.click()
                    time.sleep(2)
                    div = driver.find_element_by_xpath(final_xpath)
                
                #div.click()
                

                
                r = requests.get(div.get_attribute("href"))
                sp = BeautifulSoup(r.content, 'html.parser')
                for item in sp.find_all('img'):
                    #print(item['src'])
                    url_list.add(item['src'])
                    # f = open("images/{}.jpg".format(iter),"wb")
                    # kk = requests.get(item['src'])
                    
         
            
                    # f.write(kk.content)

                iter+=1

    
fil = open("file2.txt","w")
for i in url_list:
    fil.write(i+"\n")

fil.close()


j=1
for i in url_list:
    f2 = open("images/{}.jpg".format(j),"wb")
    img = requests.get(i)
    f2.write(img.content)
    j+=1











