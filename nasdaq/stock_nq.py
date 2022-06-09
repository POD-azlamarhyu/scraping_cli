import pandas_datareader.data as pddr
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
from tqdm import tqdm
import datetime as dt
import os
import pandas as pds

class Stock_Naq:

     def getSymbol(self):

          symbol = get_nasdaq_symbols()
          symbol.to_csv("usStock_symbol.csv")          

     def getStockdata(self):

          # read csv file
          try:
               data=pds.read_csv(filepath_or_buffer="stockdata/usStock_symbol.csv",encoding="ms932",sep=",")
          # if it is not found file,run getSymbol method
          except Exception as err:
               print("file not found\n run getSymbol")
               # getSymbol()
          
          # print(data.columns)
          
          row = len(data)
          symbol=[""]*row
          name=[""]*row
          
          for i in range(0,row):
               symbol[i] = data.loc[i,"NASDAQ Symbol"]
               name[i] = data.loc[i,"Security Name"]

          
          
          
          return symbol,name

     def Individual_stock(self):
          
          # load general stock data
          symbol,name = self.getStockdata()
          
          # get data length
          row = len(symbol)
          # show stock ticker and stock name
          for i in range(0,row):
               print("No,",i,"  ",symbol[i]," : ",name[i])
          
          print("get stock data in symbol")

          #debuge
          start="2010/01/01"
          end="2020/01/01"
          # input ticker

          num=int(input('input ticker number :'))
          ticker=symbol[num]
          # start=input('input date (exp. 2022/10/01) : ')
          # end=input('input date (exp. 2022/10/01) : ')

          # load stock data with pansas-reader API
          df=pddr.DataReader(ticker,'yahoo',start,end)
          # cut index from dataframe
          df=df.drop(columns='Adj Close')
          df.reset_index("Date",inplace=True)
          # rename index columns
          df= df.rename(columns={'Date': 'DATE','High': 'HIGH', 'Low': 'LOW',  'Open': 'OPEN', 'Close': 'CLOSE',  'Volume': 'VOL' })
          df=df[['DATE','CLOSE','HIGH','LOW','OPEN','VOL']]
          df.set_index("DATE",inplace=True)
          # print data's general
          print(df)
          # select save data or none
          judge=input('do you save data ? @ yes or no : ')
          if judge == "yes":
               fom=input('input data type. @ xlsx or csv : ')
               if fom == "xlsx":
                    path='stockdata/'+ticker+'.xlsx'
                    df.to_excel(path,sheet_name="米国個別株データ")
                    print("Successful save!!")
               elif fom == "csv":
                    path='stockdata/'+ticker+'.csv'
                    df.to_csv(path)
                    print("Successful save!!")
               else:
                    print("error! unable form!!")
                    pass
          else:
               pass


if __name__ == "__main__":
     sn = Stock_Naq()
     print("\n You can get nasdaq stock data \n")
     while True == True:
          dic={"get stock ticker and other ":1,"load Individual stock":2," end ":3}
          for k ,v in dic:
               print(k," : ", v)
          n = input('input number on the manu : ')
          
          if n == 1:
               sn.getSymbol()
          elif n == 2:
               sn.Individual_stock()
          else:
               print("progrum finish !!")
               break