# 向百度和360 提交请求并获取结果

import requests

keyword = "Python"


def getHTMLText(url):
    try:
        kv = {
            'wd': keyword
        }
        r = requests.get(url, params = kv, timeout=30)
        r.raise_for_status() #如果状态不是200， 引发HTTPError 异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "https://www.baidu.com/s"
    print(getHTMLText(url))
