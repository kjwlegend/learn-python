# 正则表达式

# 正则表达是 简洁 表达字符串的方式

'''
正则表达是是 由字符 和操作符组成的

操作符， 说明， 示例
.   标识任何单个字符
[]  字符集                 [abc]表示a\b\c  [a-z]表示a到z单个字符
[^] 非字符集                [^abc] 表示非a 或b 或c 的单个字符
*   前一个字符0次或无限次扩展   abc* 表示  ab, abc, abcc, abcccc等
+   前一个字符1次或无限次扩展   abc+ 表示  abc, abcc, abccc等
?   前一个字符0次或1次扩展    abc? 表示 ab, abc
|   左右表达式任意一个           abc|def 表示 abc, def

{m} 扩展前一个字符m次         ab{2}c 表示abbc
{m,n}   扩展前一个字符m至n次(包含n)    ab{1,2}c 表示 abc, abbc
^   匹配字符串开头             ^abc 表示 abc且在一个字符串的开头
$   匹配字符串结尾             $abc 表示 abc 在一个字符串的结尾
()  分组标记， 内部职能使用|操作符    (abc) 表示abc, (abc|def) 表示abc、def
\d  数字,等价于[0-9]
\w  单词字符， 等价于[A-Za-z0-9_]
'''
'''
最小匹配操作符

*?      前一个字符0次或无限次扩展， 最小匹配
+?
??
{m,n}?


'''
'''
经典正则表达式示例

由26个字母组成的字符串
^[A-Za-z]+$

由26个字母和数字组成
^[A-Za-z0-9]+$


整数形式的字符串
^-?\d+$

正整数形式的字符串
^[0-9]*[1-9][0-9]*$

中国境内邮政编码， 6位
[1-9]\d{5}

匹配中文字符
[\u4e00-\u9fa5]

国内电话号码 010-123123413
\d{3}-\d{8}|\d{4}-\d{7}

Re 库使用 raw string 类型表示正则表达式
'''

import re

'''
re 库的主要功能函数
re.search(pattern,string,flags=0)         在一个字符串搜索匹配正则表达式的第一个位置，返回match对象
re.match()          在一个字符串的开始位置起匹配正则表达式，返回match对象
re.findall()        搜索字符串， 以列表类型返回全部能匹配的子串
re.split(pattern,string,maxsplit=0,flags=0)          将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
re.finditer()       搜索字符串，返回一个匹配结果的迭代类型， 每个迭代元素是match对象
re.sub(pattern,repl,string,count=0,flags=0)            在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
'''

'''
regex = re.compile(pattern,flags=0)
'''