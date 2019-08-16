'''
常用命令

startproject        创建一个新工程
genspider           创建一个爬虫
settings            获取爬虫配置信息
crawl               运行一个爬虫
list                列出工程中所有爬虫
shell               启动URL调试命令行

'''

'''

Scrapy 爬虫的使用步骤
步骤1：创建工程和spider模板
步骤2： 编写Spider
步骤3：编写 item Pipeline
步骤4：优化配置策略

Scrapy爬虫的数据类型

Request类

.url            对应的请求URL地址
.method         对应的请求方法’get‘post等
.headers        字典类型风格的请求头
.body           请求内容主题，字符串类型
.meta           用户添加的扩展信息，在scrapy内部模块间传递信息使用
.copy()         复制该请求


Response 类
.url            response对应的URL地址
.status         HTTP状态码， 默认是200
.headers        Response对应的头部信息
.body           response对应的内容，字符串类型
.flags          一组标记
.request        产生response类型对应的request对象
.copy()         复制该响应


Item 类
从一个HTML页面中提取的信息需求

CSS Selector 的基本使用
<html>.css('a::attr(href)').extract()


'''