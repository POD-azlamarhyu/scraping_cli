import pandas as pd
import datetime as dt
from datetime import datetime
import pandas_datareader.data as pdrd
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols as gns
from tqdm import tqdm
import os
import openpyxl as pxl

class getNasdaq:
    
    def __init__(self):
        self.stock = []
        self.length = 0
        self.sybl = []
        self.name = []
        self.start = ""
        self.end = ""
        self.ticker = ""
        self.ename = ""

    def getGeneralsymbols(self):
        symbol = gns()
        os.makedirs("stockdata")
        symbol.to_csv("stockdata/StockGeneral.csv")

        print("data save !\n please confirm data!\n")

    def getStockdata(self):

        try:
            data = pd.read_csv(filepath_or_buffer="stockdata/StockGeneral.csv",encoding="ms932",sep=",")
        except Exception as err:
            print("file not found\n please run getGnerarlsymbols!!")

        row = len(data)
        sym = [""]*row
        nem = [""]*row

        for i in range(0,row):
            sym[i] = data.loc[i,"NASDAQ Symbol"]
            nem[i] = data.loc[i,"Security Name"]

        return sym,nem

    def individualStock(self):
        self.sybl,self.name = self.getStockdata()
        self.length = len(self.sybl)

        print(self.sybl," : ",self.name)

        for i in range(0,self.length):
            print("Ticker No, ",i," ",self.sybl[i]," : ",self.name[i])
        
        print("get stockdata in symbol")

        self.srt = "2020/01/01"
        self.end = "2020/10/01"

        num = int(input('imput ticker number : '))
        self.ticker = self.sybl[num]
        self.ename = self.name[num]
        # self.srt=input('input date (exp. 2022/10/01) : ')
        # self.end=input('input date (exp. 2022/10/01) : ')

        df = pdrd.DataReader(self.ticker,'yahoo',self.srt,self.end)
        df = df.drop(columns='Adj Close')
        df.reset_index("Date",inplace=True)
        print(df)
        
        judge = input('do you save data ? @ yes or no : ')
        
        if judge == "yes":
            fom=input('input data type. @ xlsx or csv : ')
            if fom == "xlsx":
                path ='stockdata/'+self.ename+'.xlsx'
                df.to_excel(path,sheet_name="米国個別株データ")
                print("Successful save!!")
            elif fom == "csv":
                path='stockdata/'+self.ename+'.csv'
                df.to_csv(path)
                print("Successful save!!")
            else:
                print("error! unable form!!")
                pass
        else:
            pass
    
    def exchengeFile(self):
        print("\nexchenge file form\n")
        filename = input('please input file name : ')
        path = "stockdata/" + filename + ".csv"
        data = pd.read_csv(path)

        length = len(data)

        date = [""]*length
        opn = [""]*length
        high = [""]*length
        low = [""]*length
        close = [""]*length
        volume = [""]*length

        for i in range(0,length):
            date[i] = data.loc[i,"Date"]
            opn[i] = data.loc[i,"Open"]
            high[i] = data.loc[i,"High"]
            low[i] = data.loc[i,"Low"]
            close[i] = data.loc[i,"Close"]
            volume[i] = data.loc[i,"Volume"]

        idx = ["Date","Open","High","Low","Close","Volume"]
        df = pd.DataFrame([date,opn,high,low,close,volume],index=idx)
        df = df.transpose()
        path = "stockdata/" + filename + ".xlsx"
        df.to_excel(path,encoding="ms932",sheet_name="price")

        print("\nsave successful with Excel file !\n")

if __name__ == "__main__":
    sn = getNasdaq()
    print("\n You can get nasdaq stock data\n")
    
    dic = {"get stock ticker and other ":1, "load Individual stock":2, "exchenge":3, "end":4}

    while True == True:
        for k in dic:
            print(k," : ",dic[k])

        n = int(input('input number of the menu : '))

        if n == 1:
            sn.getGeneralsymbols()
        elif n == 2:
            sn.individualStock()
        elif n == 3:
            sn.exchengeFile()
        elif n == 4:
            print("end ! ")
            break