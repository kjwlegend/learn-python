
# 程序的结构设计
#
# 步骤1：提交商品搜索请求， 循环获取页面
# 步骤2: 对每一个获得的页面进行解析
# 步骤3：将淘宝的商品信息输出到屏幕上


import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "获取失败"

def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        print(plt)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        print(tlt)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("解析失败")
"view_price":"53.00"


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods = '书包'
    depths = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depths):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()
