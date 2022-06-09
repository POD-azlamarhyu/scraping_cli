import requests as req
import pandas as pd
from bs4 import BeautifulSoup as bs

def scraping():
     columns=["url","title","category"]
     df=pd.DataFrame(columns=columns)
     url="https://dividable.net/"
     res=req.get(url).text
     category_path="nav#category ul li a"
     soup=bs(res,'html.parser')
     category_list=soup.select(category_path)
     category_dict={}
     for category in category_list:
          category_dict[category.get("href")]=category.string
     
     for key,val in category_dict.items():
          print("--カテゴリ : {",val,"}---")
          page_count=1
          category_res=""
          soup=""
          while True:
               print("---{ ",page_count," }page ----")
               cagegory_res=req.get(key+"page/"+str(page_count)).text
               soup=bs(category_res,'html.parser')
               post_tags=soup.select("div.post")
               for tag in post_tags:
                    title=tag.select("h3")[0].text
                    uri=tag.select("a")[0].get("href")
                    se=pd.Series([title,uri,val],columns)
                    df=df.append(se,ignore_index=True)
               
               next_tag=soup.find_all("a",{"class":"next"})
               if next_tag:
                    page_count += 1
                    continue
               break
     
     df.to_csv("result.csv")


if __name__ == "__main__":
     scraping()


     