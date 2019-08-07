# 文件和数据格式化
# 格式化就是对规格和样式进行规范

'''
文件的类型

由 单一特定编码组成的文件 如 UTF-8 。 就是文本文件
例如 txt. python

二进制文件， 直接由比特 0 和 1 构成的文件， 不存在特定的编码
如 png . jpg 等

文件的打开关闭
操作步骤： 打开--操作--关闭

a.read(size)
a.readline(size)
a.readlines(hint)

a.write(s) 将文件写入一个字符串或字节
a.writelines(lines)  将列表内容在同一行写入文件
a.seek(offset)   改变当前文件操作指针的位置

offset含义如下：
0 - 开头;
1-当前位置
2-文件结尾
'''

#  <变量名> = open(<文件名>, <打开模式>)
# <变量名>.close()     文件关闭

'''
打开模式有7中
'r' :  只读模式， 默认值
'w' ： 覆盖写模式， 文件不存在则创建。 存在则覆盖
'x' : 创建写模式， 不存在则创建， 存在则报错
'a' : 追加写模式， 不存在则创建， 存在贼在文件最后追加内容
'b' : 二进制文件模式
't' : 文本文件模式， 默认值
'+' :  与r/w/x/a 一同使用， 在原功能基础上增加同时读写功能

读取的方法有
<f>.read(size=-1) 读入前size长度的东西
<f>.readline(size=-1) 读入一行
<f>.readlines(hint=-1) 读入所有行 或参数 前hint 行
'''

# 遍历全文本： 方法一

fname = input("请输入打开的文件名称:")
fo = open(fname, "r")
txt = fo.read()
fo.close()

#方法二
fname = input("请输入打开的文件名称:")
fo = open(fname, "r")
txt = fo.read(2)
    while txt !="":
        #对txt 进行处理
        txt = fo.read(2)
fo.close()

# 逐行遍历方法：方法1

fname = input("请输入打开的文件名称:")
fo = open(fname, "r")
for line in fo.readlines():
    print(line)
fo.close()

# 逐行遍历方法：方法2
fname = input("请输入打开的文件名称:")
fo = open(fname, "r")
for line in fo:
    print(line)
fo.close()

# 数据写入例子

fo = open("output.txt","w+")
ls = [“"中国","法国", "美国"]
fo.writelines(ls)
fo.seek(0)  #不加入指针变换的时候， 下一行 for line in 会从文件结尾开始遍历， 就不会输出任何内容
for line in fo:
    print(line)
fo.close()