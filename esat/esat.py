
#-*- coding:<UTF-8> -*-

import pandas as pd
from bs4 import BeautifulSoup as bs
import requests as req
import pickle as pcl
import japandas as jpd
from tqdm import tqdm as tqd
import os
import openpyxl as opx


class statics():
    
    data = []
    key = ''
    url = ''
    homepath='esatGovdata'
    fom1 = 'pkl'
    fom2 = 'xlsx'
    fom3 = 'csv'
    code = []

    def __init__(self):
        self.data = data
        self.key = key
        self.code = code
        self.url = url
        self.homepath = homepath
        self.fom1 = fom1
        self.fom2 = fom2
        self.fom3 = fom3

    def getStatics(self):
        try:
            self.url = 'https://www.e-stat.go.jp/api/api-info/api-data'
            sp = bs(req.get(self.url).content,'lxml')
            td = sp.find_all('td')
            goStatCode = [v.text for i , v in enumerate(td) if i % 3 == 0]
            statName = [v.text for i , v in enumerate(td) if i % 3 == 1]
            goOrg = [v.text for i,v in enumerate(td) if i % 3 == 2]

            index = ['政府統計コード','統計調査名','作成機関名']

            df = pd.DataFrame(columns=index)
            df['政府統計コード'] = goStatCode
            df['統計調査名'] = statName
            df['作成機関名'] = goOrg

            self.saveDatapkl(df)

            print("*******************$$$$$$$$$$$*******************\n")
            print("統計コード取得完了")

            df.head()
        except Exception as e:
            print(e)
            print('------データの取得に失敗しました------')
        

    def saveDatapkl(self,data):

        print('-------------------取得データ保存-------------------\n')
        flag = input('取得したデータを保存しますか  @yes or no : ')

        if flag == 'yes':
            try:
                path = self.homepath+"/govstatcode.{}".format(self.fom1)
                data.to_pickle(path)

                print('\n-----------------------------------------------------\n')
                print('データを保存しました')
            except Exception as e:
                print(e)
                print("\nデータの保存に失敗しました")
        else:
            pass
    
    def getStaticData(self):
        self.key = 'fb08269a71d54fbcb82f20a03c506663efffa990'
        print('------------政府統計データの取得を行います------------\n')

        if os.path.exists(self.homepath+'govstatcode.{}'.format(self.fom1)) == True:
            codeList = pd.read_pickle(self.homepath+'govstatcode.{}'.format(self.fom1))
        else:
            print('政府統計データがありません')

        
        list = []
        l = len(self.code)
        for x in range(0,l):
            data = []
            try:
                data = jpd.DataReader(self.code[x],'estat',appid=self.key)
                list.append(data)
            except:
                list.append(None)

        print('\n-----------------------------------------------------\n')
        print("データの取得を完了しました\n")

        return data


                

        

    def mainControll(self):
        print("*************$$$$$$$$$$$$$$$$*************")
        print("政府統計データをスクレイピングします")
        print("*************$$$$$$$$$$$$$$$$*************\n")

        if os.path.exists(self.homepath+'/govstatcode.{}'.format(self.fom1)) == False:
            self.getStatics()
        else:
            self.data = pd.read_pickle(self.homepath+'/govstatcode.{}'.format(self.fom1))
            self.data.head()

        print("---------------$$$$$$$$$$$$$$$$$---------------")
        print("収集する統計データの政府統計コードを入力するしてください\n")
        self.code = self.inputCode()
        self.data = pd.DataFrame(self.getStaticData())
        
        print("---------------$$$$$$$$$$$$$$$$$---------------")
        flag = input('取得したデータを保存しますか？ @ yes or no $ : ')
        if flag == 'yes':
            self.dataSave()
        else:
            pass

    def dataSave(self):
        print("---------------$$$$$$$$$$$$$$$$$---------------")
        print("取得した統計データを保存します")

        name = input('保存するデータ名を入力してください @xxxxxxx $ : ')
        try:
            self.data.to_csv(self.homepath+'/{}.{}'.format(name,self.fom3))
        except:
            print('データの保存に失敗しました')



    def inputCode(self):
        code = []
        x = 0
        print('入力を終えるにはエンターを押してください enter : ')
        while (1):
            statscode = int(input('取得したいデータの政府統計コードを入力してください @0000233521 $ : '))
            if statscode.isnumeric() == False:
                print("入力されたデータは政府統計コードではありません、やり直してください\n")
            elif statscode.isnumeric() == True:
                code[x] = statscode
                x += 1
            elif statscode == "":
                break
            else:
                break

        return code



def main():
    print("------------政府統計データ取得プログラム-------------")
    if os.path.exists('esatGovdata') == True:
        os.mkdir('esatGovdata')
    
    Statsgorun = statics()

if __name__ == '__main__':
    main()