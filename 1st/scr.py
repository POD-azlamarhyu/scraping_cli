from bs4 import BeautifulSoup as bs
import requests as rqs
import pandas as pd

def scraping():
     urlName = input('input url : ')
     response = rqs.get(urlName).text
     soup = bs(response,'html.parser')
     # print(soup.prettify())
     getcode = soup.find_all("td",{"class":"center yjM"})
     getmarket = soup.find_all("td",{"class":"center yjSt"})
     getname = soup.find_all("strong",{"class":"yjMt"})
     getprofile = soup.find_all("span",{"class":"yjSt profile"})
     gettime = soup.find_all("div",{"class":"yjS time"})
     getprice = soup.find_all("div",{"class":"price yjM"})

     columns = ["code","market","name","profile","time","price"]
     df = pd.DataFrame(columns=columns)

     for stock in getcode:
          code = getcode.a.string
          market = getmarket.string
          name = getname.a.string
          profile = getprofile.string
          time = gettime.string
          price = getprice.font.string
          se = pd.Series([code,market,name,profile,time,price],columns)
          df = df.append(se,columns)
     
     data = df.transpose()
     filename = input('determine filename at csv')
     data.to_csv(filename,encoding='utf-8sig')

if __name__ == "__main__":
     scraping()


