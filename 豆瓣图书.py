import requests
import re
import os
import time
from pyquery import PyQuery as pq
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
def gettagList(url):
    html = requests.get(url,headers=header)
    doc = pq(html.text)
    taglist = []
    for i in doc('.tag').items():
        if i.text() != '更多»':
            taglist.append(i.text())
    return taglist
def return_url(tag):
    return 'https://book.douban.com/tag/' + tag

def get_book_attr(url):
    html = requests.get(url,headers=header)
    doc = pq(html.text)
    total = doc('.info')
    names = total.find('h2')
    attrs = total('.pub')
    comment1 = total.find('span')
    comments2 = comment1('.rating_nums').items()
    comments3 = comment1('.pl').items()
    BookAttr = []
    for name in names.items():
        BookAttr.append([name.text()])
    i = 0
    try:
        for attr in attrs.items():
            BookAttr[i].extend([attr.text()])
            i += 1
    except:
        pass
    i = 0
    for comment2 in comments2:
        BookAttr[i].extend([comment2.text()])
        i += 1
    i =0
    for comment3 in comments3:
        BookAttr[i].extend([comment3.text()])
        i += 1
    return BookAttr

if __name__ == '__main__':
    url = 'https://book.douban.com/'
    for tag in gettagList(url):
        totalUrl = return_url(tag)
        with open('C:\\Users\\82723\\Desktop\\book.txt','a',encoding='utf-8') as f:
            print(get_book_attr(totalUrl))
            for i in range(len(get_book_attr(totalUrl))):
                f.writelines(','.join(get_book_attr(totalUrl)[i])+'\n')
        time.sleep(30)

