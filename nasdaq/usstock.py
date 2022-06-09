import pandas_datareader.data as pddr
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
from tqdm import tqdm
import datetime as dt
import os
import pandas as pds

def USstock():
     symbol = get_nasdaq_symbols()
     print(symbol.head())
     start = input("input date that get start date exp(2011/10/12) : ")
     end=input("input date end get date exp(2011/10/12) : ")

     print(symbol)
     
     
     symbol.to_csv("usStock_symbol.csv")
     # start="2010/01/01"
     # end="2020/01/01"
     # data={}
     # error=[]
     # for s in tqdm(symbol.index):
     #      try:
     #           data[s]=pddr.DataReader(s,"yahoo",start,end)
     #      except:
     #           error.append(s)
     
     

if __name__ == "__main__":
     USstock()