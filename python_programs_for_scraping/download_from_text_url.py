
import requests


#import urllib.request

file = open("file2.txt","r")

ls = list(file.readlines())


i = 592
j = 592


for cont in range(i,len(ls)+1):
    
    stri = ls[cont]
    #print(type(stri))
    stri = stri.replace("\n","")
    img = requests.get(stri)
    print(stri)
    
   
    with open("images/{}.jpg".format(j),"wb+") as f:
         f.write(img.content)

    


    j+=1
