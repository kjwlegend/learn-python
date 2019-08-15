'''
#学习request 库
'''
'''
Request 库的7个主要方法
requests.request() 构造一个请求
requests.get(url,params=None, **kwargs) 获取HTML网页的主要方法 对应HTTP 的get
requests.head(url, **kwargs) 获取网页头信息
requests.post(url,data=None, json=None **kwargs) 提交POST 请求
requests.put(url, data=None **kwargs) 提交PUT 请求
requests.patch(url,data=None **kwargs) 提交局部修改请求
requests.delete(url, **kwargs) 提交删除请求

Response 对象的5 个最重要的属性
r.status_code :  200标识成功， 404 标识失败
r.text： 响应内容的字符串形式， 即页面内容
r.encoding： 内容编码方式
r.apparent_encoding： 备选编码方式
r.content： 响应内容的二进制形式

Requests 库的常用异常
requests.ConnectionError :连接异常， DNS 查询失败拒绝连接等
requests.HTTPError HTTP 错误异常
requests.URLRequired 缺失URL
requests.TooManyRedirects   重定向异常
requests.Connectimeout 连接远程服务器超时异常
requests.Timeout 请求URL超时， 产生超时异常

HTTP 协议对资源的操作
GET 请求获取URL位置的资源
HEAD 请求获取URL位置资源的响应消息报告， 即获取头部信息
POST 请求向URL位置的资源后附加新的数据
PUT 请求向URL 位置存储一个资源， 覆盖 原URL位置的资源
PATCH 请求局部更新URL位置的资源，即改变该处资源的部分内容
DELETE 请求删除URL位置存储的资源

PATCH 和PUT 的区别：
假设用户有很多字段， 用户只想改变其用户名
PATCH：只需要提交新的用户名的字段
PUT：需要把用户相关的所有字段全部重新提交。

理解异常
r.raise_for_status()  如果不是200， 产生异常requests.HTTPError

# requests.request(method, url, **kwargs)

method: 请求方式， 对应get、PUT/ post等7中
url： 连额吉
**kwargs： 控制访问的参数， 共13个
访问参数有:
params:字典或字节序列，作为参数增加到URL中
data：字典、字节序列或文件对象， 作为request的内容
json: JSON格式的数据， 作为内容部分提交
headers: 字典， HTTP定制头
cookies: 字典或者CookeJar
auth: 元组， 支持HTTP认证功能
files: 字典类型， 传输文件
timeout: 设定超时时间，以秒为单位
proxies:字典类型，设定访问代理服务器，可以增加登录认证
allow_redirects:True/False 重定向开关，默认为开
stream: True/False 默认为True， 获取内容立即下载开关
verify:True/False  默认为True， 认证SSL 证书开关
cert: 本地SSL证书路径
'''
import requests
import time

# 爬取网页的通用代码框架

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() #如果状态不是200， 引发HTTPError 异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))

def main(n):
    start = time.perf_counter()

    for i in range(n):
        getHTMLText(url)

    end = time.perf_counter()
    print("爬虫耗时: {} s".format(end-start))

main(100)