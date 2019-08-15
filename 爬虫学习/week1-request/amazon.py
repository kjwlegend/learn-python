# 和京东代码的不同， 需要修改 header 参数向网站提交伪装请求

import requests
def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers = kv, timeout=30)
        r.raise_for_status() #如果状态不是200， 引发HTTPError 异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "https://www.amazon.cn/dp/B00K76LMDQ?ref_=Oct_DLandingSV2_PC_f35be1ca_1&smid=A26HDXW89ZT98L"
    print(getHTMLText(url))
