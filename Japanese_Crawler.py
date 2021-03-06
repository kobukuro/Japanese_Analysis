import requests as rq
from bs4 import BeautifulSoup
import re
import time
from fake_useragent import UserAgent
#抓国語辞書
def crawlJap():
    #全部的字首
    all_chars_ori = ['あ','い','う','え','お',
                     'か','き','く','け','こ',
                     'さ','し','す','せ','そ',
                     'た','ち','つ','て','と',
                     'な','に','ぬ','ね','の',
                     'は','ひ','ふ','へ','ほ',
                     'ま','み','む','め','も',
                     'や','ゆ','よ',
                     'ら','り','る','れ','ろ',
                     'わ','を',
                     'ん',
                     'が','ぎ','ぐ','げ','ご',
                     'ざ','じ','ず','ぜ','ぞ',
                     'だ','ぢ','づ','で','ど',
                     'ば','び','ぶ','べ','ぼ',
                     'ぱ','ぴ','ぷ','ぺ','ぽ']
    #要爬的字首
    all_chars = ['が','ぎ','ぐ','げ','ご',
                 'ざ','じ','ず','ぜ','ぞ',
                 'だ','ぢ','づ','で','ど',
                 'ば','び','ぶ','べ','ぼ',
                 'ぱ','ぴ','ぷ','ぺ','ぽ']
    for char in all_chars:
        main_url = 'https://dictionary.goo.ne.jp/jn/index/'+char+'/'
        user_agent = UserAgent().random
        response = rq.get(main_url, headers={ 'user-agent': user_agent })
        html_doc = response.text
        # print(html_doc)
        soup = BeautifulSoup(response.text, "lxml")
        #總頁數
        l_m = soup.find('li', {'class': 'last-num'})
        if type(l_m) == type(None):
            li_last_num = 1
        else:
            li_last_num = int(soup.find('li', {'class': 'last-num'}).text)
        with open('jap\\'+char+'.csv', 'w', encoding='utf-8') as file:
            for num in range(1,li_last_num+1):
                print(num)
                url = main_url + str(num)
                # print(url)
                user_agent = UserAgent().random
                response = rq.get(url, headers={ 'user-agent': user_agent })
                soup = BeautifulSoup(response.text, "lxml")
                # print(li_last_num)
                all_div_ex_sen_a = soup.find('div', {'class': 'example_sentence'}).findAll('a')
                for div_ex_sen_a in all_div_ex_sen_a:
                    file.write(div_ex_sen_a.find('p',{'class':'title'}).text)
                    file.write('\n')
                # print('----------------------')
#抓和英辞書
def crawlJapEng():
    #全部的字首
    all_chars_ori = ['あ','い','う','え','お',
                     'か','き','く','け','こ',
                     'さ','し','す','せ','そ',
                     'た','ち','つ','て','と',
                     'な','に','ぬ','ね','の',
                     'は','ひ','ふ','へ','ほ',
                     'ま','み','む','め','も',
                     'や','ゆ','よ',
                     'ら','り','る','れ','ろ',
                     'わ','を',
                     'ん',
                     'が','ぎ','ぐ','げ','ご',
                     'ざ','じ','ず','ぜ','ぞ',
                     'だ',     'づ','で','ど',
                     'ば','び','ぶ','べ','ぼ',
                     'ぱ','ぴ','ぷ','ぺ','ぽ']
    #要爬的字首
    all_chars = ['あ','い','う','え','お',
                 'か','き','く','け','こ',
                 'さ','し','す','せ','そ',
                 'た','ち','つ','て','と',
                 'な','に','ぬ','ね','の',
                 'は','ひ','ふ','へ','ほ',
                 'ま','み','む','め','も',
                 'や','ゆ','よ',
                 'ら','り','る','れ','ろ',
                 'わ','を',
                 'ん',
                 'が','ぎ','ぐ','げ','ご',
                 'ざ','じ','ず','ぜ','ぞ',
                 'だ',     'づ','で','ど',
                 'ば','び','ぶ','べ','ぼ',
                 'ぱ','ぴ','ぷ','ぺ','ぽ']
    for char in all_chars:
        main_url = 'https://dictionary.goo.ne.jp/en/index/'+char+'/'
        user_agent = UserAgent().random
        response = rq.get(main_url, headers={ 'user-agent': user_agent })
        html_doc = response.text
        # print(html_doc)
        soup = BeautifulSoup(response.text, "lxml")
        #總頁數
        l_m = soup.find('li', {'class': 'last-num'})
        if type(l_m) == type(None):
            li_last_num = 1
        else:
            li_last_num = int(soup.find('li', {'class': 'last-num'}).text)
        with open('jap_eng\\'+char+'.csv', 'w', encoding='utf-8') as file:
            for num in range(1,li_last_num+1):
                print(num)
                url = main_url + str(num)
                # print(url)
                user_agent = UserAgent().random
                response = rq.get(url, headers={ 'user-agent': user_agent })
                soup = BeautifulSoup(response.text, "lxml")
                # print(li_last_num)
                all_div_ex_sen_a = soup.find('div', {'class': 'example_sentence'}).findAll('a')
                for div_ex_sen_a in all_div_ex_sen_a:
                    file.write(div_ex_sen_a.find('p',{'class':'title'}).text)
                    file.write('\n')
                # print('----------------------')

crawlJapEng()