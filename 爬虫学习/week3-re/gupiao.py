# 使用爬虫获取股票信息并保存到文件中
# 源头信息： 百度股票， 东方财富

'''
程序结构设计
步骤1：从东方财富网获取股票列表
步骤2：将股票列表按照百度个股查询股票信息
步骤3：保存资料到文件中
'''

import requests
from bs4 import BeautifulSoup
import traceback
import re


def getHTMLText(url, code='utf-8'):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout = 30, verify=False)
        r.raise_for_status()
        r.encoding = code
        return  r.text
    except:
        return ""

def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            stockID = re.findall(r"[s][hz]\d{6}", href)
            lst.append(stockID[0])
        except:
            continue
    print(lst)
def getStockInfo(lst, stockURL, fpath):
    count = 0

    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({
                '股票名称': name.text.split()[0]
            })

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] =  val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print('\r当前速度: {:.2f}%'.format(count*100/len(lst)), end='')

        except:
            count = count + 1
            print('\r当前速度: {0:.2f}%, 访问: {1:}'.format(count * 100 / len(lst), url), end='')
            traceback.print_exc()
            continue



def main():
    stock_list_url = "http://app.finance.ifeng.com/list/stock.php"
    stock_info_url ="http://gupiao.baidu.com/stock/"
    output_file = 'gupiao.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)

main()