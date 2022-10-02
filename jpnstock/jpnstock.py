
#-*- coding:<UTF-8> -*-

from bs4 import BeautifulSoup as bs
import pandas as pd
import requests as req
from datetime import datetime
import os.path
import os
import time
import openpyxl as px

class JapanStock():
    stock = []
    path = "stockdata/"
    year = []
    name = []

    def __init__(self):
        self.stocknum = stock
        self.homepath = path
        self.year = year
        self.name = name

    def inputStockcode(self):
        x = 0
        stock = []
        while True:
            brandcode = int(input('取得したい日本国内株式の銘柄コードを入力 $: '))
            if brandcode.isnumeric() == False:
                print("入力された値が銘柄コードではありません！\nやり直してください")
            elif brandcode.isnumeric() == True:
                stock[x] = brandcode
                x += 1
            else:
                break

        return stock

    def inputYear(self):
        x = 0
        years = []
        start = int(input('取得を開始する年を入力 exs.2010 $: '))
        end = int(input(''))

    def mainControll(self):
        print("\n取得したい日本国内株式の銘柄コードを配列として生成\n")
        self.stocknum = self.inputStockcode()
        print("\n****************$$$$$$$$$$*****************\n")

        print("取得したい年数を年ごとに配列に格納する")
        print("\n****************$$$$$$$$$$*****************\n")
        self.year = self.inputYear()

        for x in range(0,len(self.stocknum)):
            stockDf = []
            try:
                print("\n****************$$$$$$$$$$*****************\n")
                print("銘柄コード : "+str(self.stocknum[x])+"の株価データを取得する\n")
                if os.path.exists(self.homepath+str(self.stocknum[x])+".csv") == False:
                    stockDf = self.getNewStockdata(self.stocknum[x],self.year)
                else:
                    self.getAddStockdata(self.stocknum[x],year)

                print("\n****************$$$$$$$$$$*****************\n")
                print("銘柄コード : "+str(self.stocknum[x])+"の株価データを取得しました")
                
                self.name[x] = self.getBrandName(self.stocknum[x])
                
                flag = input('取得したデータを保存しますか yes or no : ')
                print("")
                form = input('保存するフォーマットを選択 xlsx or csv : ')
                
                if flag == "yes":
                    self.dataSave(form,self.stocknum[x],self.name[x],stockDf)
                else:
                    pass

            except Exception as err:
                print(err)
                print("株価取得に失敗しました")
                print("****************$$$$$$$$$$*****************\n")

            

    def getNewStockdata(self,code,year):
        dfs = []
        for y in year:
            try:
                url = 'https://kabuoji3.com/stock/{}/{}/'.format(code,y)
                soup = bs(req.get(url).content,'html.parser')
                tag = soup.find_all('tr')
                head=[h.text for h in tag[0].find_all('th')]
                data = []
                
                for x in range(1,len(tag)):
                    data.append([d.text for d in tag[x].find_all('td')])

                df = pd.DataFrame(data, columns = head)

                index = ['始値','高値','安値','終値','出来高','終値調整']

                for idx in index:
                    df[idx] = df[idx].astype(float)

                df['日付'] = [datetime.strptime(i,'%Y-%m-%d') for i in df['日付']]
                dfs.append(df)
            except IndexError:
                print('No data')
        
        data = self.dataSet(dfs)
        print("\n****************$$$$$$$$$$*****************\n")
        print(data)
        return data

    def getBrandName(self,code):
        url = 'https://kabuoji3.com/stock/{}/'.format(code)
        sp = bs(req.get(url).content,'html.parser')
        name = sp("span",class_="jp")

        print("\n銘柄",name,"取得中・・・・・・\n")
        return name

    def dataSet(self,dfs):
        data = pd.concat(dfs,axis=0)
        data = data.reset_index(drop=True)
        index = ['始値','高値','安値','終値','出来高','終値調整']
        for idx in index:
            data[idx] = data[idx].astype(float)
        return data
    
    def dataSave(self,form,code,name,df):
        if form == "csv":
            path = "stockdata/{}.{}".format(code,form)
            df.to_csv(path)
            path = "stockdata/{}.{}".format(name,form)
            df.to_csv(path)
        elif form == "xlsx":
            path = "stockdata/{}.{}".format(code,form)
            sheetName = name+"株価データ"
            df.to_excel(path,sheetName)
            path = "stockdata/{}.{}".format(name,form)
            df.to_excel(path,sheetName)
        else:
            print("\n****************$$$$$$$$$$*****************\n")
            print("ファイル保存失敗")
                        

def main():
    print("************$$$$$$$$$$$$$$$************\n")
    print("日本国内株式データ取得")
    print("************$$$$$$$$$$$$$$$************\n")
    os.mkdir("stockdata")
    getDataRun = JapanStock()
    getDataRun.mainControll()

if __name__ == "__main__":
    main()