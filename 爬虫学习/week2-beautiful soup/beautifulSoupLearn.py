from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>data</p>', 'html.parser')

'''
BeautifulSoup 的基本元素

Tag 标签
Name 标签的名字  <tag>.name
Attributes 标签的属性  <tag>.attrs
NavigableString:  标签内废属性字符串   <> ..</>中的字符串  <tag>.string
Comments:标签内字符串的注释部分
'''

'''
标签数有三种遍历方式：上行遍历 下行遍历 平行遍历

下行遍历的方式
.contents  子节点的列表， 将<tag>所有儿子节点存入列表
.children 子节点的迭代类型。 与.contents类似， 用于循环遍历儿子节点
.descendants 子孙节点的迭代类型， 包含所有子孙节点， 用于循环遍历

标签树的上行遍历

.parent： 获取父节点
.parents:  节点先辈标签的迭代类型，用于循环遍历先辈节点

平行遍历:

.next_sibling:  返回下一个平行节点
.previous_sibling ：返回上一个平行节点标签
.next_siblings:  迭代类型， 返回后续所有的平行节点标签
.previous_siblings:返回前面的所有平行节点标签
'''

'''
信息提取的方法：
结合解析形式和搜索内容， 进行融合解析的方法。

示例
提取所有a 标签
获取a标签的所有href 内容

'''

'''
beautifulSoup 方法
<tag>.find_all(name,attrs,recursive,string, **kwargs)
name:标签名称的检索字符串
attrs： 对标签 属性值的检索字符串
recursive:是否对子孙进行全部搜索， 默认为True

扩展方法

.find()  搜索且只返回一个结果。 字符串类型
.find_all()
.find_parents() 在先辈节点中搜索， 返回列表
.find_parent() 返回一个结果
.find_next_siblings()
.find_next_sibling()
.find_previous_siblings()
.find_previous_sibling()
'''