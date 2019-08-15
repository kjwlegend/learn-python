# 图片爬取

import requests
import os

root = "C://Users//JingWei J Kong//Desktop//采集测试//"
url = "https://brup.shengri.cn/goods/2016/03/FnAXPEw2l6I-EnO9B5YV-WNOAiL7.jpg"
path = root + url.split('/')[-1]
print(path)
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")