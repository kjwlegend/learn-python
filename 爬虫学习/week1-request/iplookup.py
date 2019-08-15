import requests

url = "http://www.ip138.com/ip.asp?ip="
ip = '123.123.123.123'
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url + ip, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")
