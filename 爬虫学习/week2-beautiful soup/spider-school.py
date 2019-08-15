# 输入： 大学排名URL 连接
# 输出：大学排名的屏幕输出
# 技术路线： requests-bs4

import requests
from bs4 import BeautifulSoup
import bs4

'''
步骤1： 从网络上获取大学排名网页内容
getHTMLText()

步骤2： 提取网页内容中信息到合适的数据结构
fillUnivList()

步骤3: 利用数据结构展示并输出结果
printUnivList()

'''

def getHTMLText(url):
    try:
        r = requests.get(url, timeout =30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])


def printUnivList(ulist, num):
    tplt = "{0:^10} \t {1:{3}^10} \t {2:^10}"
    print(tplt.format("排名“", "学校", "分数", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2], chr(12288)))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 20 univs

main()