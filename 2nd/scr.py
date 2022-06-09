import requests as req
import pandas as pds
from bs4 import BeautifulSoup as bs

def scraping():
     url = "https://dividable.net"
     request=req.get(url).text
     category="nav#category ul li a"
     soup=bs(request,'html.parser')
     
     category_list = soup.select(category)
     categoryDict={}

     for i in category_list:
          categoryDict[i.get("href")] = i.string
     
     page_count=1
     category_res=""
     soup=""
     while True:
          category_res=req.get("https://dividable.net/category/python/"+"page/"+str(page_count)).text
          soup=bs(category_res,'html.parser')
          print("{}ページ目".format(page_count))
          next_text=soup.find_all("a",{"class":"next"})
          if next_text:
               page_count+=1
               continue
          break
     
