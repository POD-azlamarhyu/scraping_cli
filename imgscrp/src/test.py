    
import requests as web
import bs4    


input_word = "オフィスチェア"
list_keywd = ['事故','危険']
resp = web.get('https://www.google.co.jp/search?num=50&q=' + input_word + ' AND (' + ' OR '.join(list_keywd) + ')')
resp.raise_for_status()

        # 取得したHTMLをパースする
soup = bs4.BeautifulSoup(resp.content, "html.parser")

        # タイトルは　　　'BNeawe vvjwJb AP7Wnd'
        # スニペットは　　'BNeawe s3v9rd AP7Wnd'
elems_title = soup.find_all(class_='BNeawe vvjwJb AP7Wnd')
elems_snipt = soup.find_all(class_='BNeawe s3v9rd AP7Wnd')

print(len(elems_snipt))
print(len(elems_snipt))

print(elems_snipt)
# print(elems_title)

# for elem in elems_title:
#     t.parse('')
#     m = t.parseToNode(elem.getText())
#     while m:
#         try:
#             if m.feature.split(',')[0] == '名詞' and m.feature.split(',')[1] != '数' and m.feature.split(',')[6] != '*' and m.feature.split(',')[1] != '固有名詞' \
#                 and m.surface not in list_keywd and m.surface not in STOP_WORDS and m.surface != input_word and model.wv.similarity('事故', m.surface) > 0.1:
#                 if dict.get(m.surface) != None:
#                     dict[m.surface] += 1
#                 else:
#                     dict[m.surface] = 1
#             m = m.next
#         except KeyError as error:
#             m = m.next

# for elem in elems_snipt:
#     t.parse('')
#     m = t.parseToNode(elem.getText())

#     while m:
#         try:
#             if m.feature.split(',')[0] == '名詞' and m.feature.split(',')[1] != '数' and m.feature.split(',')[6] != '*' and m.feature.split(',')[1] != '固有名詞' \
#             and m.surface not in list_keywd and m.surface not in STOP_WORDS and m.surface != input_word and model.wv.similarity('事故', m.surface) > 0.1:
#                 if dict.get(m.surface) != None:
#                     dict[m.surface] += 1
#                 else:
#                     dict[m.surface] = 1
#             m = m.next
#         except KeyError as error:
#             m = m.next