# 学习解析网页中的图片并下载

import requests
from bs4 import BeautifulSoup
import re
import lxml
import os

def header(referer):
    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers

def intro():
    print("本程序将在XX网站根据关键词搜索所有合适图片")

    keyword = eval(input("请输入要搜索的图片关键词： "))

    return keyword


def getHTMLText(url, code='utf-8'):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
    }
    cookie = {}
    try:
        r = requests.get(url,  headers=header, cookies=cookie, timeout=30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        print('无法解析网页')


def parsePage(ulist, html):
    soup = BeautifulSoup(html, "html.parser" )
    i = 1
    for author in soup.find_all('small'):
        yield {
            'index': i+1,
            'author' : author.get_text()
        }

def getPageList():
    getHTMLText(url)


def saveFile():
    return ""

def main():
    baseUrl = 'https://www.mzitu.com/'
    html = getHTMLText(url)
    iList = {}
    parsePage(iList, html)
    print(iList)

main()