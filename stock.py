import numpy as np
from datetime import datetime
from bs4 import BeautifulSoup
import YahooFinanceSpider as yfs
import datetime
import pandas as pds
import matplotlib as plt
import openpyxl as px

class Stocks():

     def stock_brand(self):
          c = yfs.Crawler()
          stkCode = c.get_brand_info()
          
          for i in stkCode:
               print("銘柄コード : ",i.code,"\t市場 : ",i.market)
          
          

     def stock_kinds(self):
          c = yfs.Crawler()
          dic = ['0050','1050','2050','3050','3100','3200','3250','3300','3350','3400','3450','3500','3550','3600','3650','3700','3750','3800','4050','5050','5100','5150','5200','5250','6050','6100','7050','7100','7150','7200','8050','9050']
          for i in dic:
               print("業種別コード : ",i)
          
          n = input('上記の業種コードを入力')

          len = 0
          brand = c.get_brand_info(n)
          for i in brand:
               print("銘柄コード : ",i.code,"\t市場 : ",i.market,"\t銘柄名 : ",i.brand,"\t情報 : ",i.intro)
               len += 1


          string = input('取得したデータをcsv,excelに保存しますか? ex. yes or no :')

          if string == 'yes':
               stockCode = [""]*len
               stockMarket = [""]*len
               stockBrand = [""]*len
               idx = ['銘柄コード','市場','銘柄名']
               x = 0
               for i in brand:
                    stockCode[x] = i.code
                    stockMarket[x] = i.market
                    stockBrand[x] = i.brand
                    x = x + 1


               df = pds.DataFrame([stockCode,stockMarket,stockBrand],index=idx)
               data = df.transpose()
               fom = input('保存する形式 :ex.(xlsx or csv ):')
               if fom == "CSV" or fom == "csv":
                    name = input('保存名を入力 : ')
                    path = 'stockdata/'+ name + '.csv'
                    data.to_csv(name)
               elif fom == "xlsx":
                    name = input('保存名を入力 : ')
                    path = 'stockdata/'+ name + '.xlsx'
                    data.to_excel(path,sheet_name = "業種別銘柄データ")
               else:
                    print("形式が間違っています。もう一度やり直してください")
          else:
               print("最初に戻る")
     
     def get_stock(self):
          c = yfs.Crawler()
          len = 0
          print("お好きな株価を取得できる\n")
          print("取得する株価の期間を入力\n")
          str1 = input('取得開始日example. 2044-08-11 : ')
          str2 = input('取得終了日example. 2045-12-24 : ')
          str3 = input('銘柄を入力 : ')

          start_time = datetime.datetime.strptime(str1,'%Y-%m-%d')
          end_time = datetime.datetime.strptime(str2,'%Y-%m-%d')

          brand = c.get_brand_info()
          price = c.get_price(str3,start_time,end_time,yfs.DAILY)
          
          for i in brand:
               if i.code == str3:
                    print("銘柄コード : ",i.code,"\t市場 : ",i.market,"\t銘柄名 : ",i.brand,"\t情報 : ",i.intro)
                    stockname = i.brand
                    break

          
          for i in price:
               print("日時:",i.date,"\t始値:",i.open,"\t高値:",i.high,"\t安値:",i.low,"\t終値:",i.close,"\t出来高:",i.volume)
               len += 1

          string = input('取得したデータをcsv,excelに保存しますか? ex. yes or no :')

          if string == 'yes':
               stockdate = [""]*len
               stockopen = [""]*len
               stockhigh = [""]*len
               stocklow = [""]*len
               stockclose = [""]*len
               stockvolume = [""]*len
               idx = ['日時','始値','高値','安値','終値','出来高']
               x = 0
               for i in price:
                    stockdate[x] = i.date
                    stockopen[x] = i.open
                    stockhigh[x] = i.high
                    stocklow[x] = i.low
                    stockclose[x] = i.close
                    stockvolume[x] = i.volume
                    x += 1

               df = pds.DataFrame([stockdate,stockopen,stockhigh,stocklow,stockclose,stockvolume],index=idx)
               data = df.transpose()
               fom = input('保存する形式 :ex.(xlsx or csv ):')
               if fom == "CSV" or fom == "csv":
                    name = input('保存名を入力 : ')
                    path = 'stockdata/'+ name + '.csv'
                    data.to_csv(name)
               elif fom == "xlsx":
                    name = input('保存名を入力 : ')
                    path = 'stockdata/'+ name + '.xlsx'
                    sheet = stockname + "株価データ"
                    data.to_excel(path,sheet_name = sheet)
               else:
                    print("形式が間違っています。もう一度やり直してください")
          else:
               pass       

def main():
     run = Stocks()
     while (1):
          print("\n----------------------------------------------------------\n")
          print("株価取得コード")
          dic = {"銘柄コード":1,"業種株価":2,"個別株価":3,"終了":4}
          print(dic)

          n = int(input('実行したい数字を入力 : '))

          if n == 1:
               run.stock_brand()
          elif n == 2:
               run.stock_kinds()
          elif n == 3:
               run.get_stock()    
          else:
               break

if __name__ == "__main__":
     main()